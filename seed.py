from app import app, db
from app.models import User, Question, Tag

def seed_database():
    with app.app_context():
        # Criar tags
        tag1 = Tag(name="Matemática")
        tag2 = Tag(name="Gramática")
        db.session.add_all([tag1, tag2])
        
        # Criar usuário teste
        user = User(username="professor")
        user.set_password("senha123")
        db.session.add(user)
        
        # Criar questão objetiva
        question = Question(
            title="Área do Triângulo",
            type="objetiva",
            support="<p>Calcule a área de um triângulo com base 5 e altura 3.</p>",
            command="<p>Qual é a área do triângulo?</p>",
            alternatives={"A": "7.5", "B": "15", "C": "10", "D": "12", "E": "8"},
            correct_answer="A",
            user_id=1
        )
        question.tags.append(tag1)
        db.session.add(question)
        
        db.session.commit()
        print("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    seed_database()