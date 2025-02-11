from enum import Enum

class PortalResponseType(Enum):
    success = 0
    err = 1
    info = 2
    warn = 3 

class PortalResponse:
    def __init__(self, pOk: bool = True, pDinResponseType: PortalResponseType = PortalResponseType.success, pError = '',pResponse = None):
        self.ok = pOk
        self.type = pDinResponseType.value      
        self.error = pError
        self.response = pResponse

    def toJson(self):
        content = {'ok':self.ok,'type':self.type,'error':self.error, 'response':self.response }
        return content