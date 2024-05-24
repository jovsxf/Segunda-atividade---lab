from database import Database 
from teacher_crud import TeacherCLI
from sistema_database import SistemaDatabase
from query import Query

db = Database("neo4j+s://a3570bcc.databases.neo4j.io", "neo4j", "iv0Verih76RZwESiVHnXbdvXOapm9nqc2pSkjgnUCtI") 

teacher_crud = SistemaDatabase(db)
teacher_cli = TeacherCLI(teacher_crud)
teacher_cli.run()

# Questão 1

queries = Query(db)

a = queries.get_teacher_by_name("Renzo")
print(a)

b = queries.get_teachers_starting_with("M")
print(b)

c = queries.get_all_city_names()
print(c)

d = queries.get_schools_by_number_range(150, 550)
print(d)

# Questão 2

e = queries.get_youngest_and_oldest_teacher_birth_years()
print(e)

f = queries.get_average_population()
print(f)

g = queries.get_city_by_cep_replace_letter_a("37540-000")
print(g)

h = queries.get_third_character_from_teacher_names()
print(h)

# Questão 3

teacher_crud.create(name="Chris Lima", ano_nasc=1956, cpf="189.052.396-66")
teacher = teacher_crud.read("Chris Lima")
print(teacher)
teacher_crud.update(name="Chris Lima", new_cpf="162.052.777-77")
updated_teacher = teacher_crud.read("Chris Lima")
print("Updated Teacher:", updated_teacher)



db.close()