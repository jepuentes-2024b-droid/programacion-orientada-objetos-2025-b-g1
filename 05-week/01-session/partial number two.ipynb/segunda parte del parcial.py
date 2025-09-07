# Simulación de constantes
class ItemType:
    BOOK = "Libro"
    MAGAZINE = "Revista"

# Excepciones simuladas
class LoanError(Exception):
    pass


# Servicios
class InventoryService:
    def __init__(self):
        self.users = {}      # dict con {documento: nombre}
        self.items = {}      # dict con {titulo: {"tipo":..., "stock":...}}

    def create_user(self, name, document_id):
        if document_id in self.users:
            raise ValueError("Documento ya registrado")
        self.users[document_id] = name

    def list_users(self):
        return [(doc, name) for doc, name in self.users.items()]

    def create_item(self, item_type, title, stock):
        if title in self.items:
            raise ValueError("Ya existe un material con ese título")
        self.items[title] = {"tipo": item_type, "stock": stock}

    def list_items(self):
        return [(title, data["tipo"], data["stock"]) for title, data in self.items.items()]


class LoanService:
    def __init__(self, inventory):
        self.inventory = inventory
        self.loans = []  # lista de préstamos activos

    def loan_item(self, document_id, title):
        if document_id not in self.inventory.users:
            raise LoanError("Usuario no existe")
        if title not in self.inventory.items:
            raise LoanError("Material no existe")
        if self.inventory.items[title]["stock"] <= 0:
            raise LoanError("Sin stock disponible")

        self.inventory.items[title]["stock"] -= 1
        self.loans.append({"doc": document_id, "title": title})
        return {"doc": document_id, "title": title}

    def return_item(self, document_id, title):
        found = None
        for loan in self.loans:
            if loan["doc"] == document_id and loan["title"] == title:
                found = loan
                break
        if not found:
            raise LoanError("Préstamo no encontrado")

        self.loans.remove(found)
        self.inventory.items[title]["stock"] += 1
        return 0  # penalización ficticia


class ReportService:
    def __init__(self, loans):
        self.loans = loans

    def active_loans(self):
        return self.loans.loans

    def overdue_loans(self):
        # simplificado: no calculamos fechas, solo simulamos vacío
        return []


# Funciones auxiliares 
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ingrese un número válido.")


def prompt(msg):
    return input(msg).strip()


# Acciones del menú 
def create_user(inv):
    name = prompt("Nombre: ")
    doc = prompt("Documento (único): ")
    try:
        inv.create_user(name, doc)
        print("✔ Usuario creado.")
    except ValueError as e:
        print(f"✖ Error: {e}")


def list_users(inv):
    users = inv.list_users()
    if not users:
        print("(sin usuarios)")
    for doc, name in users:
        print(f"- {name} (doc: {doc})")


def create_item(inv):
    title = prompt("Título del material: ")
    print("Tipo: 1) Libro  2) Revista")
    choice = prompt("Seleccione tipo: ")
    item_type = ItemType.BOOK if choice == "1" else ItemType.MAGAZINE if choice == "2" else None
    if not item_type:
        print("Tipo inválido.")
        return
    stock = input_int("Stock (>=0): ")
    try:
        inv.create_item(item_type, title, stock)
        print("✔ Material creado.")
    except ValueError as e:
        print(f"✖ Error: {e}")


def list_items(inv):
    items = inv.list_items()
    if not items:
        print("(sin materiales)")
    for i, (title, tipo, stock) in enumerate(items, 1):
        print(f"{i}. {tipo} - '{title}' | stock: {stock}")


def loan_item(loans):
    doc = prompt("Documento del usuario: ")
    title = prompt("Título exacto del material: ")
    try:
        loans.loan_item(doc, title)
        print("✔ Préstamo registrado.")
    except LoanError as e:
        print(f"✖ No se pudo prestar: {e}")


def return_item(loans):
    doc = prompt("Documento del usuario: ")
    title = prompt("Título exacto del material: ")
    try:
        penalty = loans.return_item(doc, title)
        print(f"✔ Devolución registrada. Penalización: ${penalty}")
    except LoanError as e:
        print(f"✖ No se pudo devolver: {e}")


def report_active(reports, inv):
    active = reports.active_loans()
    if not active:
        print("(sin préstamos activos)")
    for l in active:
        user = inv.users[l["doc"]]
        print(f"- {user} tiene '{l['title']}'")


def report_overdue(reports):
    overdue = reports.overdue_loans()
    if not overdue:
        print("(sin préstamos vencidos)")


# Programa principal 
def main():
    inventory = InventoryService()
    loans = LoanService(inventory)
    reports = ReportService(loans)

    MENU = """
================= Biblioteca Digital (CLI) =================
1. Crear usuario
2. Listar usuarios
3. Crear material (Libro/Revista)
4. Listar materiales
5. Prestar material
6. Devolver material
7. Reporte: Préstamos activos
8. Reporte: Préstamos vencidos
0. Salir
============================================================
"""

    actions = {
        "1": lambda: create_user(inventory),
        "2": lambda: list_users(inventory),
        "3": lambda: create_item(inventory),
        "4": lambda: list_items(inventory),
        "5": lambda: loan_item(loans),
        "6": lambda: return_item(loans),
        "7": lambda: report_active(reports, inventory),
        "8": lambda: report_overdue(reports),
    }

    while True:
        print(MENU)
        op = prompt("Seleccione una opción: ")
        if op == "0":
            print("¡Hasta luego!")
            break
        action = actions.get(op)
        if action:
            action()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
