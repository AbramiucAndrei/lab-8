from domain.entities import Disciplina,Student,Note
from repo.repoError import RepoError
class DisciplinaRepo:
    def __init__(self):
        self.discipline=[]


    def store(self,disc):
        for elem in self.discipline:
            if elem.get_id()==disc.get_id():
                 raise RepoError("ID-ul disciplinei e deja in memorie")

        self.discipline.append(disc)

    def sterge(self,id):
        for elem in self.discipline:
            if elem.get_id()==id:
                self.discipline.remove(elem)
                return
        raise RepoError("Nu exista disciplina cu acest ID")

    def modifica_nume(self,nume_nou,_id):
        """
        modificarea numelui studentului/disciplinei cu id ul primit ca parametru
        :param nume: noul nume
        :return: lista dupa modificare
        """
        for elem in self.discipline:
            if elem.get_id() == _id:
                elem.set_nume(nume_nou)
                return elem
        raise RepoError("Nu exista disciplina cu acest ID")

    def modifica_profesor(self, profesor_nou, _id):
        """
        modificarea profesorului de la disciplina cu id ul primit
        :param profesor_nou: numele noului profesor
        :return: lista dupa modificare
        """
        for elem in self.discipline:
            if elem.get_id() == _id:
                elem.set_profesor(profesor_nou)
                return elem
        raise RepoError("Nu exista disciplina cu acest ID")

    def cauta_disciplina(self,_id):
        for disc in self.discipline:
            if disc.get_id() == _id:
                return disc
        raise RepoError("Nu exista disciplina cu acest ID")
    def maxID(self):
        max_id=0
        for elem in self.discipline:
            if elem.get_id() > max_id:
                max_id = elem.get_id()
        return max_id
    def get_discipline(self):
        return list(self.discipline)

class StudentRepo:
    def __init__(self):
        self.students = []

    def store(self, stud):
        for elem in self.students:
            if elem.get_id() == stud.get_id():
                raise RepoError("ID-ul studentului e deja in memorie")

        self.students.append(stud)

    def sterge(self, id):
        for elem in self.students:
            if elem.get_id() == id:
                self.students.remove(elem)
                return
        raise RepoError("ID ul nu se afla in lista")

    def modifica_nume(self, nume_nou,_id):
        """
        modificarea numelui studentului/disciplinei cu id ul primit ca parametru
        :param nume: noul nume
        :return: lista dupa modificare
        """

        for elem in self.students:
            if elem.get_id()== _id:
                elem.set_nume(nume_nou)
                return elem
        raise RepoError("Nu exista niciun student cu acest ID")
    def cauta_student(self,_id):
        for stud in self.students:
            if stud.get_id() == _id:
                return stud
        raise RepoError("Nu exista student cu acest ID")

    def maxID(self):
        max_id = 0
        for elem in self.students:
            if elem.get_id() > max_id:
                max_id = elem.get_id()

        return max_id

    def get_students(self):
        return list(self.students)


class NoteRepo:
    def __init__(self):
        self.note = []

    def store(self,nota):
        for notes in self.note:
            if notes.getIDnota() == nota.getIDnota():
                raise RepoError("Exista deja aceasta nota(Id identic)")
        self.note.append(nota)

    def maxID(self):
        max_id=0
        for notes in self.note:
            if notes.getIDnota() > max_id:
                max_id=notes.getIDnota()
        return max_id

    def get_note(self):
        return list(self.note)

def test_NoteRepo():
    r=NoteRepo()
    nota=Note(1,1,1,10)
    r.store(nota)
    try:
        nota1=Note(1,2,2,7)
        r.store(nota1)
        assert False
    except RepoError as re:
        assert re.getErrors()=="Exista deja aceasta nota(Id identic)"

    assert r.maxID()==1
    assert nota in r.get_note()
test_NoteRepo()

def test_StudentRepo():
    r=StudentRepo()
    st=Student(1,"Matei")
    r.store(st)
    try:
        st1=Student(1,"Andrei")
        r.store(st1)
        assert False
    except RepoError as re:
        assert re.getErrors()=="ID-ul studentului e deja in memorie"

    st1=Student(2,"Andrei")
    r.store(st1)

    assert r.cauta_student(2) != None
    try:
        r.cauta_student(3)
        assert False
    except RepoError as er:
        assert  er.getErrors()=="Nu exista student cu acest ID"

    assert r.maxID()==2
    assert st in r.get_students()
    assert st1 in r.get_students()
    r.sterge(2)
    try:
        r.sterge(2)
        assert False
    except RepoError as re:
        assert re.getErrors()=="ID ul nu se afla in lista"

    assert r.modifica_nume("Adrian",1).get_nume()=="Adrian"
    try:
        r.modifica_nume("Ionut",2)
        assert False
    except RepoError as re:
        re.getErrors()=="Nu exista niciun student cu acest ID"
test_StudentRepo()

def test_DisciplinaRepo():
    r=DisciplinaRepo()
    dc=Disciplina(1,"Ioan","Matematica")
    r.store(dc)
    try:
        dc1=Disciplina(1,"Ioan","Matematica")
        r.store(dc1)
        assert False
    except RepoError as re:
        assert re.getErrors()=="ID-ul disciplinei e deja in memorie"

    assert r.modifica_nume("Romana",1).get_nume()=="Romana"
    try:
        r.modifica_nume("Romana",2)
        assert False
    except RepoError as re:
        assert re.getErrors()=="Nu exista disciplina cu acest ID"

    assert r.modifica_profesor("Ilie", 1).get_profesor() == "Ilie"
    try:
        r.modifica_nume("Ilie", 2)
        assert False
    except RepoError as re:
        assert re.getErrors() == "Nu exista disciplina cu acest ID"
    assert r.cauta_disciplina(1)==dc
test_DisciplinaRepo()