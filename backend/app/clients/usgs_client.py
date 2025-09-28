from typing import Optional, Dict, Any
from sciencebasepy import SbSession

class USGSClient:
    def __init__(self, username: Optional[str]=None, password: Optional[str]=None):
        self.sb = SbSession()
        if username and password:
            self.sb.login(username, password)

    def ping(self) -> bool:
        return self.sb.ping()

    def get_item_json(self, item_id: str) -> Dict[str, Any]:
        # Ejemplo: traer metadata de un item público
        return self.sb.get_item(item_id)

    # Agrega aquí métodos para descargar archivos, buscar por bbox, etc.
