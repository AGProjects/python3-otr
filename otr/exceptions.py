
class IgnoreMessage(Exception):
    pass


class UnencryptedMessage(Exception):
    pass


class OTRError(Exception):
    pass


class OTRFinishedError(OTRError):
    pass


class EncryptedMessageError(OTRError):
    pass
