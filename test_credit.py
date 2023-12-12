from credit_calculator import credit

# --------------------sum

def test_Sum_1():
    assert summ(0) == False
    
def test_Sum_2():
    assert summ < 0 == False
    
def test_Sum_3():
    assert summ > 0 == True
    
# --------------interestRate

def test_interestRate_1():
    assert interestRate(0) == False
    
def test_interestRate_2():
    assert interestRate < 0 == False
    
def test_interestRate_3():
    assert interestRate > 0 == True
    
# -------------------period    
    
def test_period_1():
    assert period(0) == False
    
def test_period_2():
    assert period < 0 == False
    
def test_period_3():
    assert period > 0 == True