def testLambda(fn):
    fn(9)

testLambda(lambda x=7: print(x))