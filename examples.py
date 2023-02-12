# def read_faculty_by_acronym(self, faculty_acronym: str):
#     faculty = self.db.query(Faculty).filter(Faculty.acronym.ilike(f"%{faculty_acronym}%")).all()
#
#     return faculty
#
#
# def read_faculty_by_city(self, city: str):
#     faculty = self.db.query(Faculty).filter(Faculty.city.ilike(f"%{city}%")).all()
#     return faculty
#
#
# def read_faculty_by_name(self, name: str):
#     faculty = self.db.query(Faculty).filter(Faculty.name.ilike(f"%{name}%")).all()
#     return faculty
#
#
# def read_faculty_by_name_or_city(self, namecity: str):
#     faculty = self.db.query(Faculty).filter(Faculty.name.ilike(f"%{namecity}%")).all()
#     return faculty
