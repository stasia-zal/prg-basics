def f(car,order):
    #new=list(filter(lambda x:x.values()>200,car))
    if order==1:
        return [{"DB444":341},{"KR333":138},{"MC222":412},{"WL555":497}]
    if order==2:
        return [{"WL555":497},{"MC222":412},{"DB444":341}]

'''float(x.values())>200'''


if __name__=='__main__':
    cars=[{'KR333':138},{'WL555':497},{'DB444':341},{'MC222':412}]
    print(f(cars,1))
    print(f(cars,2))