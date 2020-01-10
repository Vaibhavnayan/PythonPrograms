class test:
  def __init__(self, name, gpa):
    self.name=name
    self.gpa=gpa

  def checkGPA(self):
    if self.gpa >=10:
      return "Topper"
    else:
      return "FAIL"