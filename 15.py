from hdbcli import dbapi
from datetime import datetime
# проверка на профиль + тип одежды
# Функция для проверки соответствия customer_profile
def check_profile(base_customer_profile, profile):
    # Логика для "Women" профилей
    if base_customer_profile == "Women Regular":
        return profile in ["Women Regular", "Women Young"]
    elif base_customer_profile == "Women Young":
        return profile in ["Women Regular", "Women Young"]
    elif base_customer_profile == "Women Queens":
        return profile == "Women Queens"
    
    # Логика для "Men" профилей
    elif base_customer_profile == "Men Regular":
        return profile in ["Men Regular", "Men Young"]
    elif base_customer_profile == "Men Young":
        return profile in ["Men Regular", "Men Young"]
    
    # Если профиль не соответствует ни одному из условий, возвращаем False
    return False

# Установка соединения с базой данных
conn = dbapi.connect(
   #
)

# Пользовательский артикул
base_article = input("Введите артикул (например, M241M00747): ")

# Получаем сегодняшнюю дату в нужном формате
current_date = datetime.today().strftime('%Y%m%d')

try:
    # Создаем курсор для выполнения запросов
    cursor = conn.cursor()

    # Первый запрос для получения данных по артикулу
    query1 = f"""
    
    """

    cursor.execute(query1)
    results1 = cursor.fetchall()
    columns1 = [desc[0] for desc in cursor.description]

    # Получаем значения customer_profile и material_group для выбранного артикула
    base_customer_profile = None
    base_material_group = None
    for row in results1:
        base_customer_profile = row[3]  # customer_profile
        base_material_group = row[4]    # material_group
        break  # Делаем break, чтобы не перебирать все строки, так как они одинаковы для одного артикула

    if not base_customer_profile or not base_material_group:
        print("Не удалось найти данные для указанного артикула.")
        cursor.close()
        conn.close()
        exit()

    # Логика проверки профилей
    print(f"Профиль для артикула {base_article}: {base_customer_profile}")
    print(f"Группа материалов для артикула {base_article}: {base_material_group}")

    # Второй запрос для выборки артикули с 1 до 999
    query2 = f"""
    
    """

    cursor.execute(query2)
    results2 = cursor.fetchall()
    columns2 = [desc[0] for desc in cursor.description]

    # Перебор результатов и проверка условий
    count = 0
    for row in results2:
        article = row[0]
        customer_profile = row[1]
        material_group = row[2]

        # Проверка соответствия профилей
        if check_profile(base_customer_profile, customer_profile) and material_group == base_material_group:
            print(f"Найдено совпадение: Артикул {article}, Профиль: {customer_profile}, Группа материалов: {material_group}")
            count += 1

    print(f"\nВсего найдено совпадений: {count}.")

    # Закрытие соединения
    cursor.close()
    conn.close()
    input("Нажмите Enter, чтобы выйти...")

except dbapi.Error as e:
    print(f"Ошибка выполнения запроса: {e}")
