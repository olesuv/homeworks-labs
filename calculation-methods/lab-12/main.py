def Adams():
    global a, b, h, FI, X, FIfc
    kmax = 100
    x0 = a
    y0 = 1
    eps = 1e-6
    epse = abs(fe(x0)-y0)
    x1 = x0 + h
    k1 = f(x0, y0)
    k2 = f(x0 + h * 0.5, y0 + h * k1 * 0.5)
    k3 = f(x0 + h * 0.5, y0 + h * k2 * 0.5)
    k4 = f(x0 + h, y0 + h * k3)
    y1 = y0 + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    epse = abs(fe(x1) - y1)x2 = x0
    y2 = y1
    x1 = x0
    y1 = y0
    y1f = y0
    y1c = y0
    while(True):
        x0 = x1
        y0 = y1
        x1 = x2
        y1 = y2
        x2 = x1 + h
        y2f = y1 + h/2 * (3*f(x1, y1) - f(x0, y0))
        yi1 = y2f + 5/6 * (y1c - y1f)
        k = 0
        while(True):
            yi0 = yi1
            yi1 = y1 + h/2 * (f(x2, yi0) + f(x1, y1))
            k += 1
            if (k >= kmax):
                print("Max iterations")
                print("x1={0}\tfe(x1)={1}\ty1={2}\tepse={3}\teps_fc={4}".format(x1, fe(x1), y1, epse, eps_fc))
                break
            if (abs(yi1-yi0) < eps): break

            y2c = yi1
            y2 = y2c - 1/6 * (y2c - y2f)
            if (x2 >= b): break
            epse = abs(fe(x2) - y2)
            eps_fc = abs(y2c - y2f)
            FI.append(epse)
            X.append(x2)
            FIfc.append(eps_fc)

            if (x2 >= b): break
            print("x2={0}\tfe(x2)={1}\ty2={2}\tepse={3}\teps_fc={4}\tk={5}\ty_f={6}".format(x2, fe(x2), y2, epse, eps_fc, k, y2f))
