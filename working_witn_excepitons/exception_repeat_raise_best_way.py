### Exceptions

class OrderCreationException(Exception):
    pass


class OrderNotFound(OrderCreationException):
    def __init__(self, order_id):
        self.order_id = order_id
        super().__init__(
            f"Order {order_id} was not found in db "
            "to emit."
        )


class ReceiptGenerationFailed(OrderCreationException):
    def __init__(self, order_id):
        self.order_id = order_id
        super().__init__(
            "Error found during emission! "
            f"Order: {order_id}"
        )


class ReceiptEmissionFailed(OrderCreationException):
    def __init__(self, order_id):
        self.order_id = order_id
        super().__init__(
            "Emission failed! "
            f"Order: {order_id} "
        )


class OrderFacade:  # Renamed to match what it actually is
    def emit(self, order_id: str) -> dict:
        try:
            # NOTE: info logging still happens inside
            status_service.ensure_order_unlocked(order_id)
            receipt_note = receipt_service.create(order_id)
            broker.emit_receipt_note(receipt_note)
            order_status = status_service.get_order_status(order_id)
        except OrderAlreadyInProgress as e:
            # New block
            logger.info("Aborting emission request because it is already in progress!")
            return {"order_id": order_id, "order_status": e.order_status.value}
        except OrderAlreadyEmitted as e:
            # New block
            logger.info(f"Aborting emission because it already happened! {e}")
            return {"order_id": order_id, "order_status": e.order_status.value}
        except OrderNotFound:
            logger.exception("We got a database exception")
            raise
        except ReceiptGenerationFailed:
            logger.exception("We got a problem generating the receipt")
            raise
        except ReceiptEmissionFailed:
            logger.exception("Unable to emit the receipt")
            raise
        else:
            return {"order_id": order_id, "order_status": order_status.value}
