from domain.entities import Note,Disciplina,Student
from domain.validators import Validate_note,ValidationError
from repo.inmemory import StudentRepo,DisciplinaRepo,NoteRepo
from repo.repoError import RepoError
class ServiceNote:
    def __init__(self,repo,validator,studRepo :StudentRepo,discRepo :DisciplinaRepo):
        self.repo=repo
        self.validator=validator
        self.studRepo=studRepo
        self.discRepo=discRepo

    def createNota(self,idStud,idDisc,nota):
        #se verifica daca exista un student cu id-ul idStud
        self.studRepo.cauta_student(idStud)
        #se verifica daca exista o disciplina cu id-ul idDisc
        self.discRepo.cauta_disciplina(idDisc)


        maxID=self.repo.maxID()
        nota_noua=Note(maxID+1,idStud,idDisc,nota)
        #se creeaza obictul de tip nota
        self.validator.validate(nota_noua)
        self.repo.store(nota_noua)
    def getAllGrades(self):
        #returneaza lista de note
        return self.repo.get_note()

def test_ServiceNote():
    r=NoteRepo()
    v=Validate_note()
    d=DisciplinaRepo()
    new_disc=Disciplina(1,"Ioan","Matematica")
    d.store(new_disc)

    s=StudentRepo()
    new_stud=Student(1,"Andrei")
    s.store(new_stud)
    sr=ServiceNote(r,v,s,d)
    sr.createNota(1,1,5)
    try:
        sr.createNota(1,1,0)
        assert False
    except ValidationError as ve:
        assert len(ve.getErrors())==1

    try:
        sr.createNota(0,0,11)
        assert False
    except RepoError:
        assert True


    assert len(sr.getAllGrades())==1
test_ServiceNote()

