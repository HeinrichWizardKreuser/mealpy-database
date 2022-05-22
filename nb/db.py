data = [
    # Ackley
    dict(
        dimensions="d",
        domain=[-32, 32],
        domain_latex=
            r"xi ∈ [-32.768, 32.768], for all i = 1, …, d, although it may also be restricted to a smaller domain",
            r"x_i \in [-32, 32], i=1,...,n",
            r"$x_i \in [-32, 32]$ for all $i = 1,...,n$",
        latex=
            r"f_{\text{Ackley}}(\mathbf{x}) = -20e^{-0.2 \sqrt{\frac{1}{n} \sum_{i=1}^n x_i^2}} - e^{ \frac{1}{n} \sum_{i=1}^n \cos(2 \pi x_i)} + 20 + e",
            r"$$f(\textbf{x}) = f(x_1, ..., x_n)= -a.exp(-b\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2})-exp(\frac{1}{n}\sum_{i=1}^{n}cos(cx_i))+ a + exp(1)$$",
        links=[
            "https://www.sfu.ca/~ssurjano/ackley.html",
            "http://infinity77.net/global_optimization/test_functions_nd_A.html#go_benchmark.Ackley",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/ackleyfcn.markdown",
        ],
        method=benchmarknd.Functions()._ackley__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has one global minimum at: $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, ..., 0)$.",
        name="Ackley",
        references=
            ['Adorio, E. P., & Diliman, U. P. MVF - Multivariate Test Functions Library in C for Unconstrained Global Optimization (2005). Retrieved June 2013, from http://http://www.geocities.ws/eadorio/mvf.pdf.', 'Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June 2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf.', 'Back, T. (1996). Evolutionary algorithms in theory and practice: evolution strategies, evolutionary programming, genetic algorithms. Oxford University Press on Demand.'],
            ['http://www.sfu.ca/~ssurjano/ackley.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'http://www.cs.unm.edu/~neal.holts/dga/benchmarkFunction/ackley.html'],
        tags=TODO,
    ),
    # Ackley N2
    dict(
        dimensions="TODO",
        domain=[-32, 32],
        domain_latex=r"$x_i \in [-32, 32]$ for $i=1, 2$",
        latex=r"$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}}$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/ackleyn2fcn.markdown",
        ],
        method=benchmark2d.Functions()._ackley_n2__,
        minima=None,
        minima_latex=r"The function has a global minimum at $f(\textbf{x}^{\ast})=-200$ located at $\mathbf{x^\ast}=(0, 0)$.",
        name="Ackley N. 2",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. H. Ackley, “A Connectionist Machine for Genetic Hill-Climbing,” Kluwer, 1987'],
        tags=TODO,
    ),
    # Ackley N3
    dict(
        dimensions="TODO",
        domain=[-32, 32],
        domain_latex=r"$x_i \in [-32, 32]$ for $i=1, 2$",
        latex=r"$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}} + 5e^{cos(3x) + sin(3y)}$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/ackleyn3fcn.markdown",
        ],
        method=benchmark2d.Functions()._ackley_n3__,
        minima=None,
        minima_latex=r"The function has two global minima at $f(\textbf{x}^{\ast})\approx -195.629028238419$ located at $\mathbf{x^\ast}=(\pm0.682584587365898, -0.36075325513719)$.",
        name="Ackley N. 3",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), arXiv:1308.400', '. H. Ackley, “A Connectionist Machine for Genetic Hill-Climbing,” Kluwer, 1987', 'ayak B., Dash S.K., Sahu J.B. (2019) Validation of Well-Known Population-Based Stochastic Optimization Algorithms Using Benchmark Functions. In: Bansal J., Das K., Nagar A., Deep K., Ojha A. (eds) Soft Computing for Problem Solving. Advances in Intelligent Systems and Computing, vol 816. Springer, Singapor'],
        tags=TODO,
    ),
    # Ackley N4
    dict(
        dimensions="TODO",
        domain=[-35, 35],
        domain_latex=r"$x_i \in [-35, 35]$ for $i=1, ..., n$",
        latex=r"$$f(\textbf{x})=\sum_{i=1}^{n-1}\left( e^{-0.2}\sqrt{x_i^2+x_{i+1}^2} + 3\left( cos(2x_i) + sin(2x_{i+1}) \right) \right)$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/ackleyn4fcn.markdown",
        ],
        method=benchmarknd.Functions()._ackley_n4__,
        minima=None,
        minima_latex=r"On the 2-dimensional space, the function has one global minima at $f(\textbf{x}^{\ast}) = -4.590101633799122$ located at $\mathbf{x^\ast}=(-1.51, -0.755)$.",
        name="Ackley N. 4",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Adjiman
    dict(
        dimensions="TODO",
        domain=[-1, 2],
        domain_latex=
            r"x_1 \in [-1, 2], x_2 \in [-1, 1]",
            r"$x \in [-1, 2]$ and $y \in [-1, 1]$",
        latex=
            r"f_{\text{Adjiman}}(\mathbf{x}) = \cos(x_1)\sin(x_2) - \frac{x_1}{(x_2^2 + 1)}",
            r"$$f(x, y)=cos(x)sin(y) - \frac{x}{y^2+1}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_A.html#go_benchmark.Adjiman",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/adjimanfcn.markdown",
        ],
        method=benchmark2d.Functions()._adjiman__,
        minima=dict("f(x_i)"=-2.02181, "\mathbf{x}"=[2, 0.10578]),
        minima_latex=
            r"f(x_i) = -2.02181 for \mathbf{x} = [2, 0.10578]",
            r"On the on $x \in [-1, 2]$ and $x \in [-1, 1]$ cube, the global minimum $f(\textbf{x}^{\ast})=-2.02181$ is located at $\mathbf{x^\ast}=(0, 0)$.",
        name="Adjiman",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. S. Adjiman, S. Sallwig, C. A. Flouda, A. Neumaier, "A Global Optimization Method, aBB for General Twice-Differentiable NLPs-1, Theoretical Advances," Computers Chemical Engineering, vol. 22, no. 9, pp. 1137-1158, 1998', 'ing, A., "Differential Evolution: Fundamentals and Applications in Electrical Engineering", Wiley, 2009. [https://books.google.com/books?id=Pp-SHz6dIJ0C'],
        tags=TODO,
    ),
    # Alpine N1
    dict(
        dimensions="TODO",
        domain=
            [-10, 10],
            [0, 10],
        domain_latex=
            r"x_i \in [-10, 10], i=1,...,n",
            r"$x_i \in [0, 10]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Alpine01}}(\mathbf{x}) = \sum_{i=1}^{n} \lvert {x_i \sin \left( x_i \right) + 0.1 x_i} \rvert",
            r"$$f(\mathbf x)=f(x_1, ..., x_n) = \sum_{i=1}^{n}|x_i sin(x_i)+0.1x_i|$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_A.html#go_benchmark.Alpine01",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/alpinen1fcn.markdown",
        ],
        method=benchmarknd.Functions()._alpine_n1__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has a global minimum  $f(\textbf{x}^{\ast})=0$ located at $\mathbf{x^\ast}=(0, ..., 0)$.",
        name=
            "Alpine 1",
            "Alpine N. 1",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. Clerc, “The Swarm and the Queen, Towards a Deterministic and Adaptive Particle Swarm Optimization, ” IEEE Congress on Evolutionary Computation, Washington DC, USA, pp. 1951-1957, 1999'],
        tags=TODO,
    ),
    # Alpine N2
    dict(
        dimensions="TODO",
        domain=[0, 10],
        domain_latex=
            r"x_i \in [0, 10], i=1,...,n",
            r"$x_i \in [0, 10]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Alpine02}}(\mathbf{x}) = \prod_{i=1}^{n} \sqrt{x_i} \sin(x_i)",
            r"$$f(\mathbf x)=f(x_1, ..., x_n) = \prod_{i=1}^{n}\sqrt{x_i}sin(x_i)$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_A.html#go_benchmark.Alpine02",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/alpinen2fcn.markdown",
        ],
        method=benchmarknd.Functions()._alpine_n2__,
        minima=dict("f(x_i)"=-6.1295, "x_i"=7.917),
        minima_latex=
            r"f(x_i) = -6.1295 for x_i = 7.917 for i=1,...,n",
            r"The function was devised By Clerc as a maximization problem and hence, the orginial paper gave  $f(\textbf{x}^{\ast})=2.808^n$, ",
        name=
            "Alpine 2",
            "Alpine N. 2",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. Clerc, “The Swarm and the Queen, Towards a Deterministic and Adaptive Particle Swarm Optimization, ” IEEE Congress on Evolutionary Computation, Washington DC, USA, pp. 1951-1957, 1999'],
        tags=TODO,
    ),
    # Bartels Conn
    dict(
        dimensions="TODO",
        domain=
            [-50, 50],
            [-500, 500],
        domain_latex=
            r"x_i \in [-50, 50], i=1,...,n",
            r"$x \in [-500, 500]$ and $y \in [-500, 500]$",
        latex=
            r"f_{\text{BartelsConn}}(\mathbf{x}) = \lvert {x_1^2 + x_2^2 + x_1x_2} \rvert + \lvert {\sin(x_1)} \rvert + \lvert {\cos(x_2)} \rvert",
            r"$$f(x,y)=|x^2 + y^2 + xy| + |sin(x)| + |cos(y)|$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_B.html#go_benchmark.BartelsConn",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/bartelsconnfcn.markdown",
        ],
        method=benchmark2d.Functions()._bartels_conn__,
        minima=dict("f(x_i)"=1, "x_i"=0),
        minima_latex=
            r"f(x_i) = 1 for x_i = 0 for i=1,...,n",
            r"The global minimum $f(\textbf{x}^{\ast})=1$ is located at $\mathbf{x^\ast}=(0, 0)$.",
        name=
            "Bartels Conn",
            "Bartels-Conn",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Beale
    dict(
        dimensions=2,
        domain=
            [-10, 10],
            [-4.5, 4.5],
        domain_latex=
            r"xi ∈ [-4.5, 4.5], for all i = 1, 2",
            r"x_i \in [-10, 10], i=1,2",
            r"$x \in [-4.5, 4.5]$ for all $i = 1, 2$",
        latex=
            r"f_{\text{Beale}}(\mathbf{x}) = \left(x_1 x_2 - x_1 + 1.5\right)^{2} + \left(x_1 x_2^{2} - x_1 + 2.25\right)^{2} + \left(x_1 x_2^{3} - x_1 + 2.625\right)^{2}",
            r"$$f(x, y) = (1.5-x+xy)^2+(2.25-x+xy^2)^2+(2.625-x+xy^3)^2$$",
        links=[
            "https://www.sfu.ca/~ssurjano/beale.html",
            "http://infinity77.net/global_optimization/test_functions_nd_B.html#go_benchmark.Beale",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/bealefcn.markdown",
        ],
        method=benchmark2d.Functions()._beale__,
        minima=dict("f(x_i)"=0, "\mathbf{x}"=[3, 0.5]),
        minima_latex=
            r"f(x_i) = 0 for \mathbf{x} = [3, 0.5]",
            r"The function has one global minimum at: $f(x^*)=0$ at $\textbf{x}^{\ast} = (3, 0.5)$.",
        name="Beale",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.'],
            ['http://www.sfu.ca/~ssurjano/ackley.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO_files/Page288.htm'],
        tags=TODO,
    ),
    # Bird
    dict(
        dimensions="TODO",
        domain=
            [-2np.pi, 2np.pi],
            [-2*np.pi, 2*np.pi],
        domain_latex=
            r"x_i \in [-2\pi, 2\pi], i=1,2",
            r"$x_i \in [-2\pi, 2\pi]$ for $i=1, 2$",
        latex=
            r"f_{\text{Bird}}(\mathbf{x}) = \left(x_1 - x_2\right)^{2} + e^{\left[1 - \sin\left(x_1\right) \right]^{2}} \cos\left(x_2\right) + e^{\left[1 - \cos\left(x_2\right)\right]^{2}} \sin\left(x_1\right)",
            r"$$f(x, y) = sin(x)e^{(1-cos(y))^2}+cos(y)e^{(1-sin(x))^2}+(x-y)^2$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_B.html#go_benchmark.Bird",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/birdfcn.markdown",
        ],
        method=benchmark2d.Functions()._bird__,
        minima=dict("f(x_i)"=-106.7645367198034, "\mathbf{x}"=[4.701055751981055 , 3.152946019601391]),
        minima_latex=
            r"f(x_i) = -106.7645367198034 for \mathbf{x} = [4.701055751981055 , 3.152946019601391] or\n\mathbf{x} = [-1.582142172055011, -3.130246799635430]",
            r"The function has two global minima at $f(\textbf{x}^{\ast}) = -106.764537$ located at $\mathbf{x^\ast}=(4.70104, 3.15294)$ and $\mathbf{x^\ast}=(-1.58214, -3.13024)$.",
        name="Bird",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. K. Mishra, “Global Optimization By Differential Evolution and Particle Swarm Methods: Evaluation On Some Benchmark Functions,” Munich Research Papers in Economics, Available Online: [http://mpra.ub.uni-muenchen.de/1005/'],
        tags=TODO,
    ),
    # Bohachevskyn N1
    dict(
        dimensions=2,
        domain=
            [-15, 15],
            [-100, 100],
        domain_latex=
            r"xi ∈ [-100, 100], for all i = 1, 2",
            r"x_i \in [-15, 15], i=1,...,n",
            r"$x_i \in [-100, 100]$ for $i = 1, 2$",
        latex=
            r"f_{\text{Bohachevsky}}(\mathbf{x}) = \sum_{i=1}^{n-1}\left[x_i^2 + 2x_{i+1}^2 - 0.3\cos(3\pi x_i) - 0.4\cos(4\pi x_{i+1}) + 0.7\right]",
            r"$$f(x, y) = x^2 + 2y^2 -0.3cos(3\pi x)-0.4cos(4\pi y)+0.7$$",
        links=[
            "https://www.sfu.ca/~ssurjano/boha.html",
            "http://infinity77.net/global_optimization/test_functions_nd_B.html#go_benchmark.Bohachevsky",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/bohachevskyn1fcn.markdown",
        ],
        method=benchmark2d.Functions()._bohachevskyn_n1__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has one local minimum at: $f(\textbf{x}^{\ast}) = 0$ at $\textbf{x}^{\ast} = (0, 0)$",
        name=
            "Bohachevsky",
            "Bohachevsky Functions",
            "Bohachevsky N. 1",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.'],
            ['ttp://www.sfu.ca/~ssurjano/boha.htm'],
        tags=TODO,
    ),
    # Bohachevskyn N2
    dict(
        dimensions="TODO",
        domain=[-100, 100],
        domain_latex=r"$x_i \in [-100, 100]$ for $i=1, 2$",
        latex=r"$$f(x, y)=x^2 + 2y^2 -0.3cos(3\pi x)cos(4\pi y)+0.3$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/bohachevskyn2fcn.markdown",
        ],
        method=benchmark2d.Functions()._bohachevskyn_n2__,
        minima=None,
        minima_latex=r"The function has one global minimum $f(\textbf{x}^{\ast}) = 0$ located at $\mathbf{x^\ast}=(0, 0)$.",
        name="Bohachevsky N. 2",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. O. Bohachevsky, M. E. Johnson, M. L. Stein, “General Simulated Annealing for Function Optimization,” Technometrics, vol. 28, no. 3, pp. 209-217, 1986'],
        tags=TODO,
    ),
    # Booth
    dict(
        dimensions=2,
        domain=[-10, 10],
        domain_latex=
            r"xi ∈ [-10, 10], for all i = 1, 2",
            r"$x_i \in [-10, 10]$ for all $i = 1,2$",
        latex=r"$$f(x,y)=(x+2y-7)^2+(2x+y-5)^2$$",
        links=[
            "https://www.sfu.ca/~ssurjano/booth.html",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/boothfcn.markdown",
        ],
        method=benchmark2d.Functions()._booth__,
        minima=None,
        minima_latex=r"The function has one global minimum at: $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (1,3)$.",
        name="Booth",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.'],
            ['http://www.sfu.ca/~ssurjano/booth.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Brent
    dict(
        dimensions="TODO",
        domain=
            [-10, 10],
            [-20, 0],
        domain_latex=
            r"x_i \in [-10, 10], i=1,2",
            r"$x_i \in [-20, 0]$ for $i=1, 2$",
        latex=
            r"f_{\text{Brent}}(\mathbf{x}) = (x_1 + 10)^2 + (x_2 + 10)^2 + e^{(-x_1^2-x_2^2)}",
            r"$$f(x, y) = (x + 10)^2 + (y + 10)^2 + e^{-x^2 - y^2}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_B.html#go_benchmark.Brent",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/brentfcn.markdown",
        ],
        method=benchmark2d.Functions()._brent__,
        minima=dict("f(x_i)"=0, "\mathbf{x}"=[-10, -10]),
        minima_latex=
            r"f(x_i) = 0 for \mathbf{x} = [-10, -10]",
            r"The function has one global minimum at $f(\textbf{x}^{\ast})= e^{-200}$ located at $\mathbf{x^\ast}=(-10, -10)$.",
        name="Brent",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Brown
    dict(
        dimensions="TODO",
        domain=[-1, 4],
        domain_latex=
            r"x_i \in [-1, 4], i=1,...,n",
            r"$x_i \in [-1, 4]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Brown}}(\mathbf{x}) = \sum_{i=1}^{n-1}\left[ \left(x_i^2\right)^{x_{i+1}^2+1} + \left(x_{i+1}^2\right)^{x_i^2+1} \right]",
            r"$$f(\textbf{x}) = \sum_{i=1}^{n-1}(x_i^2)^{(x_{i+1}^{2}+1)}+(x_{i+1}^2)^{(x_{i}^{2}+1)}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_B.html#go_benchmark.Brown",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/brownfcn.markdown",
        ],
        method=benchmarknd.Functions()._brown__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has one global minimum at $f(\textbf{x}^{\ast})= 0$ located at $\mathbf{x^\ast}=\textbf{0}$.",
        name="Brown",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Bukin N6
    dict(
        dimensions=2,
        domain=[-15, -5],
        domain_latex=
            r"x1 ∈ [-15, -5], x2 ∈ [-3, 3]",
            r"x_1 \in [-15, -5], x_2 \in [-3, 3]",
            r"$x \in [-15, -5]$ and $y \in [-3, 3]$ ",
        latex=
            r"f_{\text{Bukin06}}(\mathbf{x}) = 100 \sqrt{ \lvert{x_2 - 0.01 x_1^{2}} \rvert} + 0.01 \lvert{x_1 + 10} \rvert",
            r"$$f(x,y)=100\sqrt{|y-0.01x^2|}+0.01|x+10|$$",
        links=[
            "https://www.sfu.ca/~ssurjano/bukin6.html",
            "http://infinity77.net/global_optimization/test_functions_nd_B.html#go_benchmark.Bukin06",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/bukinn6fcn.markdown",
        ],
        method=benchmark2d.Functions()._bukin_n6__,
        minima=dict("f(x_i)"=0, "\mathbf{x}"=[-10, 1]),
        minima_latex=
            r"f(x_i) = 0 for \mathbf{x} = [-10, 1]",
            r"The function has one global minimum at: $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (-10,1)$.",
        name=
            "Bukin 6",
            "Bukin Function N. 6",
            "Bukin N. 6",
        references=
            ['Global Optimization Test Functions Index. Retrieved June 2013, from http://infinity77.net/global_optimization/test_functions.html#test-functions-index.'],
            ['http://www.sfu.ca/~ssurjano/booth.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Cross In Tray
    dict(
        dimensions=2,
        domain=
            [-15, 15],
            [-10, 10],
        domain_latex=
            r"xi ∈ [-10, 10], for all i = 1, 2",
            r"x_i \in [-15, 15], i=1,2",
            r"$x \in [-10, 10]$ and $y \in [-10, 10]$ ",
        latex=
            r"f_{\text{CrossInTray}}(\mathbf{x}) = - 0.0001 \left(\left|{e^{\left|{100 - \frac{\sqrt{x_{1}^{2} + x_{2}^{2}}}{\pi}}\right|} \sin\left(x_{1}\right) \sin\left(x_{2}\right)}\right| + 1\right)^{0.1}",
            r"$$f(x,y)=-0.0001(|sin(x)sin(y)exp(|100-\frac{\sqrt{x^2+y^2}}{\pi}|)|+1)^{0.1}$$",
        links=[
            "https://www.sfu.ca/~ssurjano/crossit.html",
            "http://infinity77.net/global_optimization/test_functions_nd_C.html#go_benchmark.CrossInTray",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/crossintrayfcn.markdown",
        ],
        method=benchmark2d.Functions()._cross_in_tray__,
        minima=dict("f(x_i)"=-2.062611870822739, "x_i"=r"\pm 1.349406608602084"),
        minima_latex=
            r"f(x_i) = -2.062611870822739 for x_i = \pm 1.349406608602084 for i=1,2",
            r"The function has four global minima $f(\textbf{x}^{\ast})=-2.06261218$ at $\textbf{x}^{\ast} = (\pm1.349406685353340,\pm1.349406608602084)$.",
        name="Cross-in-Tray",
        references=
            ['Test functions for optimization. In Wikipedia. Retrieved June 2013, from https://en.wikipedia.org/wiki/Test_functions_for_optimization.'],
            ['http://www.sfu.ca/~ssurjano/crossit.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Deckkers Aarts
    dict(
        dimensions="TODO",
        domain=[-20, 20],
        domain_latex=
            r"x_i \in [-20, 20], i=1,2",
            r"$x_i \in [-20, 20]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{DeckkersAarts}}(\mathbf{x}) = 10^5x_1^2 + x_2^2 - (x_1^2 + x_2^2)^2 + 10^{-5}(x_1^2 + x_2^2)^4",
            r"$$f(x, y) = 10^5x^2 + y^2 -(x^2 + y^2)^2 + 10^{-5}(x^2 + y^2)^4$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_D.html#go_benchmark.DeckkersAarts",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/deckkersaartsfcn.markdown",
        ],
        method=benchmark2d.Functions()._deckkers_aarts__,
        minima=dict("f(x_i)"=-24777, "\mathbf{x}"=r"[0, \pm 15]"),
        minima_latex=
            r"f(x_i) = -24777 for \mathbf{x} = [0, \pm 15]",
            r"The global minima $f(\textbf{x}^{\ast})=-24771.09375$ are located at $\mathbf{x^\ast}=(0, \pm 15)$.",
        name="Deckkers-Aarts",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. M. Ali, C. Khompatraporn, Z. B. Zabinsky, “A Numerical Evaluation of Several Stochastic Algorithms on Selected Continuous Global Optimization Test Problems,” Journal of Global Optimization, vol. 31, pp. 635-672, 2005'],
        tags=TODO,
    ),
    # Drop Wave
    dict(
        dimensions=2,
        domain=
            [-5.12, 5.12],
            [-5.2, 5.2],
        domain_latex=
            r"xi ∈ [-5.12, 5.12], for all i = 1, 2",
            r"x_i \in [-5.12, 5.12], i=1,2",
            r"$x_i \in [-5.2, 5.2]$ for $i = 1, 2$",
        latex=
            r"f_{\text{DropWave}}(\mathbf{x}) = - \frac{1 + \cos\left(12 \sqrt{\sum_{i=1}^{n} x_i^{2}}\right)}{2 + 0.5 \sum_{i=1}^{n} x_i^{2}}",
            r"$$f(x, y) = - \frac{1 + cos(12\sqrt{x^{2} + y^{2}})}{(0.5(x^{2} + y^{2}) + 2)}$$",
        links=[
            "https://www.sfu.ca/~ssurjano/drop.html",
            "http://infinity77.net/global_optimization/test_functions_nd_D.html#go_benchmark.DropWave",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/dropwavefcn.markdown",
        ],
        method=benchmark2d.Functions()._drop_wave__,
        minima=dict("f(x_i)"=-1, "x_i"=0),
        minima_latex=
            r"f(x_i) = -1 for x_i = 0 for i=1,2",
            r"$f(\textbf{x}^{\ast}) = -1$ at $\textbf{x}^{\ast} = (0, 0)$",
        name=
            "Drop-Wave",
            "DropWave",
        references=
            ['Global Optimization Test Functions Index. Retrieved June 2013, from http://infinity77.net/global_optimization/test_functions.html#test-functions-index.'],
            ['ttp://www.sfu.ca/~ssurjan'],
        tags=TODO,
    ),
    # Easom
    dict(
        dimensions=2,
        domain=[-100, 100],
        domain_latex=
            r"xi ∈ [-100, 100], for all i = 1, 2",
            r"x_i \in [-100, 100], i=1,2",
            r"$x \in [-100, 100]$ and $y \in [-100, 100]$ ",
        latex=
            r"f_{\text{Easom}}(\mathbf{x}) = a - \frac{a}{e^{b \sqrt{\frac{\sum_{i=1}^{n} x_i^{2}}{n}}}} + e - e^{\frac{\sum_{i=1}^{n} \cos\left(c x_i\right)}{n}}",
            r"$$f(x,y)=−cos(x)cos(y) exp(−(x − \pi)^2−(y − \pi)^2)$$",
        links=[
            "https://www.sfu.ca/~ssurjano/easom.html",
            "http://infinity77.net/global_optimization/test_functions_nd_E.html#go_benchmark.Easom",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/easomfcn.markdown",
        ],
        method=benchmark2d.Functions()._easom__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,2",
            r"The function has four global minima $f(x^{\ast}, y^{\ast})=-1$ at $(x^{\ast}, y^{\ast}) = (\pi,\pi)$.",
        name="Easom",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.'],
            ['http://www.sfu.ca/~ssurjano/easom.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', 'http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO_files/Page1361.htm'],
        tags=TODO,
    ),
    # Egg Crate
    dict(
        dimensions="TODO",
        domain=[-5, 5],
        domain_latex=
            r"x_i \in [-5, 5], i=1,2",
            r"$x_i \in [-5, 5]$ for $i=1, 2$",
        latex=
            r"f_{\text{EggCrate}}(\mathbf{x}) = x_1^2 + x_2^2 + 25 \left[ \sin^2(x_1) + \sin^2(x_2) \right]",
            r"$$f(x,y)=x^2 + y^2 + 25(sin^2(x) + sin^2(y))$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_E.html#go_benchmark.EggCrate",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/eggcratefcn.markdown",
        ],
        method=benchmark2d.Functions()._egg_crate__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,2",
            r"The global minimum $f(\textbf{x}^{\ast})=0$ is located at $\mathbf{x^\ast}=(0, 0)$.",
        name="Egg Crate",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', 'http://al-roomi.org/benchmarks/unconstrained/2-dimensions/122-egg-crate-function', 'hawdhry, P. K., Roy, R., & Pant, R. K. (2012). Soft Computing in Engineering Design and Manufacturing. London: Springer Science & Business Media', 'ang, X.S. (2008). Nature-Inspired Metaheuristic Algorithms, Luniver Press'],
        tags=TODO,
    ),
    # Exponential
    dict(
        dimensions="TODO",
        domain=[-1, 1],
        domain_latex=
            r"x_i \in [-1, 1], i=1,...,n",
            r"$x_i \in [-1, 1]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Exponential}}(\mathbf{x}) = -e^{-0.5 \sum_{i=1}^n x_i^2}",
            r"$$f(\mathbf{x})=f(x_1, ..., x_n)=-exp(-0.5\sum_{i=1}^n{x_i^2})$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_E.html#go_benchmark.Exponential",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/exponentialfcn.markdown",
        ],
        method=benchmarknd.Functions()._exponential__,
        minima=dict("f(x_i)"=-1, "x_i"=0),
        minima_latex=
            r"f(x_i) = -1 for x_i = 0 for i=1,...,n",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=$ at $\mathbf{x^\ast}=0$.",
        name="Exponential",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. Rahnamyan, H. R. Tizhoosh, N. M. M. Salama, “Opposition-Based Differential Evolution (ODE) with Variable Jumping Rate,” IEEE Sympousim Foundations Computation Intelligence, Honolulu, HI, pp. 81-88, 2007'],
        tags=TODO,
    ),
    # Goldstein Price
    dict(
        dimensions=2,
        domain=[-2, 2],
        domain_latex=
            r"xi ∈ [-2, 2], for all i = 1, 2",
            r"x_i \in [-2, 2], i=1,2",
            r"$x \in [-2, 2]$ and $y \in [-2, 2]$ ",
        latex=
            r"f_{\text{GoldsteinPrice}}(\mathbf{x}) = \left[ 1+(x_1+x_2+1)^2(19-14x_1+3x_1^2-14x_2+6x_1x_2+3x_2^2) \right] \left[ 30+(2x_1-3x_2)^2(18-32x_1+12x_1^2+48x_2-36x_1x_2+27x_2^2) \right]",
            r"$$f(x,y)=[1 + (x + y + 1)^2(19 − 14x+3x^2− 14y + 6xy + 3y^2)][30 + (2x − 3y)^2(18 − 32x + 12x^2 + 4y − 36xy + 27y^2)]$$",
        links=[
            "https://www.sfu.ca/~ssurjano/goldpr.html",
            "http://infinity77.net/global_optimization/test_functions_nd_G.html#go_benchmark.GoldsteinPrice",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/goldsteinpricefcn.markdown",
        ],
        method=benchmark2d.Functions()._goldstein_price__,
        minima=dict("f(x_i)"=3, "\mathbf{x}"=[0, -1]),
        minima_latex=
            r"f(x_i) = 3 for \mathbf{x} = [0, -1]",
            r"The function has four global minima $f(\textbf{x}^{\ast})=3$ at $\textbf{x}^{\ast} = (0, -1)$.",
        name="Goldstein-Price",
        references=
            ['Dixon, L. C. W., & Szego, G. P. (1978). The global optimization problem: an introduction. Towards global optimization, 2, 1-15.', 'Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June 2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf.', 'Picheny, V., Wagner, T., & Ginsbourger, D. (2012). A benchmark of kriging-based infill criteria for noisy optimization.'],
            ['http://www.sfu.ca/~ssurjano/goldpr.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Gramacy Lee
    dict(
        dimensions=1,
        domain=[-0.5, 2.5],
        domain_latex=
            r"x ∈ [0.5, 2.5]",
            r"$x \in [-0.5, 2.5]$",
        latex=r"$$f(x) = \frac{sin(10\pi x)}{2x} + (x-1)^4$$",
        links=[
            "https://www.sfu.ca/~ssurjano/grlee12.html",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/gramacyleefcn.markdown",
        ],
        method=benchmark1d.Functions()._gramacy_lee__,
        minima=None,
        minima_latex=r"The function has one local minimum at: $f(x^*)=-0.869011134989500$ at $\textbf{x}^{\ast} = 0.548563444114526$.",
        name=
            "Gramacy & Lee",
            "Gramacy & Lee (2012)",
        references=
            ['Gramacy, R. B., & Lee, H. K. (2012). Cases for the nugget in modeling computer experiments. Statistics and Computing, 22(3), 713-722.', 'Ranjan, P. (2013). Comment: EI Criteria for Noisy Computer Simulators. Technometrics, 55(1), 24-28.'],
            ['http://www.sfu.ca/~ssurjano/boha.html', 'http://al-roomi.org/benchmarks/unconstrained/1-dimension/258-gramacy-lee-s-function-no-1'],
        tags=TODO,
    ),
    # Griewank
    dict(
        dimensions="d",
        domain=[-600, 600],
        domain_latex=
            r"xi ∈ [-600, 600], for all i = 1, …, d",
            r"x_i \in [-600, 600], i=1,...,n",
            r"$x_i \in [-600, 600]$ for $i = 1, ..., n$",
        latex=
            r"f_{\text{Griewank}}(\mathbf{x}) = \frac{1}{4000}\sum_{i=1}^n x_i^2 - \prod_{i=1}^n\cos\left(\frac{x_i}{\sqrt{i}}\right) + 1",
            r"$$f(\textbf{x}) = f(x_1, ..., x_n) = 1 + \sum_{i=1}^{n} \frac{x_i^{2}}{4000} - \prod_{i=1}^{n}cos(\frac{x_i}{\sqrt{i}})$$",
        links=[
            "https://www.sfu.ca/~ssurjano/griewank.html",
            "http://infinity77.net/global_optimization/test_functions_nd_G.html#go_benchmark.Griewank",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/griewankfcn.markdown",
        ],
        method=benchmarknd.Functions()._griewank__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"$f(\textbf{x}^{\ast}) = 0$ at $\textbf{x}^{\ast} = (0, ..., 0)$",
        name="Griewank",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.', 'Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June 2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf.'],
            ['ttp://www.sfu.ca/~ssurjan'],
        tags=TODO,
    ),
    # Happy Cat
    dict(
        dimensions="TODO",
        domain=[-2, 2],
        domain_latex=r"$x_i \in [-2, 2]$ for $i=1, ..., n$",
        latex=r"$$f(\textbf{x})=\left[\left(||\textbf{x}||^2 - n\right)^2\right]^\alpha + \frac{1}{n}\left(\frac{1}{2}||\textbf{x}||^2+\sum_{i=1}^{n}x_i\right)+\frac{1}{2}$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/happycatfcn.markdown",
        ],
        method=benchmarknd.Functions()._happy_cat__,
        minima=None,
        minima_latex=r"The function has one global minimum at $f(\textbf{x}^{\ast}) = 0$ located at $\mathbf{x^\ast}=(-1, ..., -1)$.",
        name="Happy Cat",
        references=
            ['ans-Georg Beyer and Steffen Finck, HappyCat – A Simple Function Class Where Well-Known Direct Search Algorithms Do Fail, Parallel Problem Solving from Nature - PPSN XII, pp. 367--376 (2012), [https://doi.org/10.1007/978-3-642-32937-1_37'],
        tags=TODO,
    ),
    # Himmelblau
    dict(
        dimensions="TODO",
        domain=[-6, 6],
        domain_latex=
            r"x_i \in [-6, 6], i=1,2",
            r"$x_i \in [-6, 6]$ for $i = 1, 2$",
        latex=
            r"f_{\text{HimmelBlau}}(\mathbf{x}) = (x_1^2 + x_2 - 11)^2 + (x_1 + x_2^2 -7)^2",
            r"$$f(x, y) = (x^{2} + y - 11)^{2} + (x + y^{2} - 7)^{2}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_H.html#go_benchmark.HimmelBlau",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/himmelblaufcn.markdown",
        ],
        method=benchmark2d.Functions()._himmelblau__,
        minima=dict("f(x_i)"=0, "\mathbf{x}"=[0, 0]),
        minima_latex=
            r"f(x_i) = 0 for \mathbf{x} = [0, 0]",
            r"The function has four local minima at: ",
        name=
            "HimmelBlau",
            "Himmelblau",
        references=
            ['ttps://en.wikipedia.org/wiki/Himmelblau%27s_functio'],
        tags=TODO,
    ),
    # Holder Table
    dict(
        dimensions=2,
        domain=[-10, 10],
        domain_latex=
            r"xi ∈ [-10, 10], for all i = 1, 2",
            r"x_i \in [-10, 10], i=1,2",
            r"$x \in [-10, 10]$ and $y \in [-10, 10]$ ",
        latex=
            r"f_{\text{HolderTable}}(\mathbf{x}) = - \left|{e^{\left|{1 - \frac{\sqrt{x_{1}^{2} + x_{2}^{2}}}{\pi} }\right|} \sin\left(x_{1}\right) \cos\left(x_{2}\right)}\right|",
            r"$$f(x,y)=-|sin(x)cos(y)exp(|1-\frac{\sqrt{x^2+y^2}}{\pi}|)|$$",
        links=[
            "https://www.sfu.ca/~ssurjano/holder.html",
            "http://infinity77.net/global_optimization/test_functions_nd_H.html#go_benchmark.HolderTable",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/holdertablefcn.markdown",
        ],
        method=benchmark2d.Functions()._holder_table__,
        minima=dict("f(x_i)"=-19.20850256788675, "x_i"=r"\pm 9.664590028909654"),
        minima_latex=
            r"f(x_i) = -19.20850256788675 for x_i = \pm 9.664590028909654 for i=1,2",
            r"The function has four global minima $f(\textbf{x}^{\ast})=-19.2085$ at $\textbf{x}^{\ast} = (\pm 8.05502,\pm 9.66459)$.",
        name=
            "Holder Table",
            "Holder-Table",
            "HolderTable",
        references=
            ['Global Optimization Test Functions Index. Retrieved June 2013, from http://infinity77.net/global_optimization/test_functions.html#test-functions-index.', 'Test functions for optimization. In Wikipedia. Retrieved June 2013, from https://en.wikipedia.org/wiki/Test_functions_for_optimization.'],
            ['http://www.sfu.ca/~ssurjano/holder.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization'],
        tags=TODO,
    ),
    # Keane
    dict(
        dimensions="TODO",
        domain=[0, 10],
        domain_latex=
            r"x_i \in [0, 10], i=1,2",
            r"$x_i \in [0, 10]$ for $i=1, 2$",
        latex=
            r"f_{\text{Keane}}(\mathbf{x}) = \frac{\sin^2(x_1 - x_2)\sin^2(x_1 + x_2)}{\sqrt{x_1^2 + x_2^2}}",
            r"$$f(x,y)=-\frac{\sin^2(x-y)\sin^2(x+y)}{\sqrt{x^2+y^2}}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_K.html#go_benchmark.Keane",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/kealefcn.markdown",
        ],
        method=benchmark2d.Functions()._keane__,
        minima=dict("f(x_i)"=0.673668, "\mathbf{x}"=[0.0, 1.39325]),
        minima_latex=
            r"f(x_i) = 0.673668 for \mathbf{x} = [0.0, 1.39325].",
            r"The function has two global minima $f(\textbf{x}^{\ast})=0.673667521146855$ at ",
        name="Keane",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', 'http://al-roomi.org/benchmarks/unconstrained/2-dimensions/135-keane-s-function'],
        tags=TODO,
    ),
    # Leon
    dict(
        dimensions="TODO",
        domain=
            [-1.2, 1.2],
            [0, 10],
        domain_latex=
            r"x_i \in [-1.2, 1.2], i=1,2",
            r"$x_i \in [0, 10]$ for $i=1, 2$",
        latex=
            r"f_{\text{Leon}}(\mathbf{x}) = \left(1 - x_{1}\right)^{2} + 100 \left(x_{2} - x_{1}^{2} \right)^{2}",
            r"$$f(x, y) = 100(y − x^{3})^2 + (1 − x)^2$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_L.html#go_benchmark.Leon",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/leonfcn.markdown",
        ],
        method=benchmark2d.Functions()._leon__,
        minima=dict("f(x_i)"=0, "x_i"=1),
        minima_latex=
            r"f(x_i) = 0 for x_i = 1 for i=1,2",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (1,1)$.",
        name="Leon",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. Lavi, T. P. Vogel (eds), “Recent Advances in Optimization Techniques,” John Wiley & Sons, 196', 'http://al-roomi.org/benchmarks/unconstrained/2-dimensions/125-leon-s-function'],
        tags=TODO,
    ),
    # Levi N13
    dict(
        dimensions=2,
        domain=[-10, 10],
        domain_latex=
            r"xi ∈ [-10, 10], for all i = 1, 2",
            r"x_i \in [-10, 10], i=1,...,n",
            r"$x \in [-10, 10]$ and $y \in [-10, 10]$ ",
        latex=
            r"f_{\text{Levy03}}(\mathbf{x}) = \sin^2(\pi y_1)+\sum_{i=1}^{n-1}(y_i-1)^2[1+10\sin^2(\pi y_{i+1})]+(y_n-1)^2",
            r"$$f(x, y) = sin^2(3\pi x)+(x-1)^2(1+sin^2(3\pi y))+(y-1)^2(1+sin^2(2\pi y))$$",
        links=[
            "https://www.sfu.ca/~ssurjano/levy13.html",
            "http://infinity77.net/global_optimization/test_functions_nd_L.html#go_benchmark.Levy03",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/levin13fcn.markdown",
        ],
        method=benchmark2d.Functions()._levi_n13__,
        minima=dict("f(x_i)"=0, "x_i"=1),
        minima_latex=
            r"f(x_i) = 0 for x_i = 1 for i=1,...,n",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (1, 1)$.",
        name=
            "Levi N. 13",
            "Levy 3",
            "Levy Function N. 13",
        references=
            ['Global Optimization Test Functions Index. Retrieved June 2013, from http://infinity77.net/global_optimization/test_functions.html#test-functions-index.'],
            ['http://www.sfu.ca/~ssurjano/levy13.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization'],
        tags=TODO,
    ),
    # Matyas
    dict(
        dimensions=2,
        domain=[-10, 10],
        domain_latex=
            r"xi ∈ [-10, 10], for all i = 1, 2",
            r"x_i \in [-10, 10], i=1,2",
            r"$x \in [-10, 10]$ and $y \in [-10, 10]$ ",
        latex=
            r"f_{\text{Matyas}}(\mathbf{x}) = 0.26(x_1^2 + x_2^2) - 0.48x_1x_2",
            r"$$f(x, y)=0.26(x^2+y^2) -0.48xy$$",
        links=[
            "https://www.sfu.ca/~ssurjano/matya.html",
            "http://infinity77.net/global_optimization/test_functions_nd_M.html#go_benchmark.Matyas",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/matyasfcn.markdown",
        ],
        method=benchmark2d.Functions()._matyas__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,2",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, 0)$.",
        name="Matyas",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.'],
            ['http://www.sfu.ca/~ssurjano/matya.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Mc Cormick
    dict(
        dimensions=2,
        domain=[-1.5, 4],
        domain_latex=
            r"x1 ∈ [-1.5, 4], x2 ∈ [-3, 4]",
            r"x_1 \in [-1.5, 4], x_2 \in [-3, 4]",
            r"$x \in [-1.5, 4]$ and $y \in [-3, 3]$ ",
        latex=
            r"f_{\text{McCormick}}(\mathbf{x}) = - x_{1} + 2 x_{2} + \left(x_{1} - x_{2}\right)^{2} + \sin\left(x_{1} + x_{2}\right) + 1",
            r"$$f(x, y)=sin(x + y) + (x - y) ^2 - 1.5x + 2.5 y + 1$$",
        links=[
            "https://www.sfu.ca/~ssurjano/mccorm.html",
            "http://infinity77.net/global_optimization/test_functions_nd_M.html#go_benchmark.McCormick",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/mccormickfcn.markdown",
        ],
        method=benchmark2d.Functions()._mc_cormick__,
        minima=dict("f(x_i)"=-1.913222954981037, "\mathbf{x}"=[-0.5471975602214493, -1.547197559268372]),
        minima_latex=
            r"f(x_i) = -1.913222954981037 for \mathbf{x} = [-0.5471975602214493, -1.547197559268372]",
            r"The function has one global minimum $f(\textbf{x}^{\ast})\approx −1.9133$ at $\textbf{x}^{\ast} = (−0.547,−1.547)$.",
        name="McCormick",
        references=
            ['Adorio, E. P., & Diliman, U. P. MVF - Multivariate Test Functions Library in C for Unconstrained Global Optimization (2005). Retrieved June 2013, from http://http://www.geocities.ws/eadorio/mvf.pdf.'],
            ['http://www.sfu.ca/~ssurjano/mccorm.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Periodic
    dict(
        dimensions="TODO",
        domain=[-10 10],
        domain_latex=r"$x_i \in [-10 10]$ for $i=1 ... n$",
        latex=r"$$f(\mathbf{x})=f(x_1 ... x_n)=1 + \sum_{i=1}^{n}{sin^2(x_i)}-0.1e^{(\sum_{i=1}^{n}x_i^2)}$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/periodicfcn.markdown",
        ],
        method=benchmarknd.Functions()._periodic__,
        minima=None,
        minima_latex=r"The function has on global minimum $f(\mathbf{x}^{\ast})=0.9$ at $\mathbf{x}^{\ast}=(0 ... 0)$.",
        name="Periodic",
        references=
            ['omin Jamil and Xin-She Yang A literature survey of benchmark functions for global optimization problems Int. Journal of Mathematical Modelling and Numerical Optimisation} Vol. 4 No. 2 pp. 150--194 (2013) [arXiv:1308.4008', '. M. Ali C. Khompatraporn Z. B. Zabinsky “A Numerical Evaluation of Several Stochastic Algorithms on Selected Continuous Global Optimization Test Problems,” Journal of Global Optimization vol. 31 pp. 635-672 2005'],
        tags=TODO,
    ),
    # Powell Sum
    dict(
        dimensions="TODO",
        domain=
            [-4, 5],
            [-1, 1],
        domain_latex=
            r"x_i \in [-4, 5], i=1,...,4",
            r"$x_i \in [-1, 1]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Powell}}(\mathbf{x}) = (x_3+10x_1)^2+5(x_2-x_4)^2+(x_1-2x_2)^4+10(x_3-x_4)^4",
            r"$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}|x_i|^{i+1}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_P.html#go_benchmark.Powell",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/powellsumfcn.markdown",
        ],
        method=benchmarknd.Functions()._powell_sum__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,4",
            r"The function has one global minimum $f(\mathbf{x}^{\ast})=0$ at $\mathbf{x}^{\ast} = 0$.",
        name=
            "Powell",
            "Powell Sum",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. Rahnamyan, H. R. Tizhoosh, N. M. M. Salama, “A Novel Population Initialization Method for Accelerating Evolutionary Algorithms,” Computers and Mathematics with Applications, vol. 53, no. 10, pp. 1605-1614, 2007', 'ukhopadhyay, Sumitra; Das, Soumyadip, (2016), A System on Chip Development of Customizable GA Architecture for Real Parameter Optimization Problem, in Handbook of Research on Natural Computing for Optimization Problems, IGI Global'],
        tags=TODO,
    ),
    # Qing
    dict(
        dimensions="TODO",
        domain=[-500, 500],
        domain_latex=
            r"x_i \in [-500, 500], i=1,...,n",
            r"$x_i \in [-500, 500]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Qing}}(\mathbf{x}) = \sum_{i=1}^{n} (x_i^2 - i)^2",
            r"$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}(x^2-i)^2$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_Q.html#go_benchmark.Qing",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/qingfcn.markdown",
        ],
        method=benchmarknd.Functions()._qing__,
        minima=dict("f(x_i)"=0, "x_i"=r"\pm \sqrt(i)"),
        minima_latex=
            r"f(x_i) = 0 for x_i = \pm \sqrt(i) for i=1,...,n",
            r"The global minima $f(\textbf{x}^{\ast})=0$ are located at $\mathbf{x^\ast}=(\pm\sqrt{i}, ..., \pm\sqrt{i})$.",
        name="Qing",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. Qing, “Dynamic Differential Evolution Strategy and Applications in Electromagnetic Inverse Scattering Problems,” IEEE Transactions on Geoscience and remote Sensing, vol. 44, no. 1, pp. 116-125, 2006'],
        tags=TODO,
    ),
    # Quartic
    dict(
        dimensions="TODO",
        domain=[-1.28, 1.28],
        domain_latex=r"$x_i \in [-1.28, 1.28]$ for $i=1, ..., n$",
        latex=r"$$f(\mathbf{x})=f(x_1,...,x_n)=\sum_{i=1}^{n}ix_i^4+\text{random}[0,1)$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/quarticfcn.markdown",
        ],
        method=benchmarknd.Functions()._quartic__,
        minima=None,
        minima_latex=r"The function has one global minimum $f(\textbf{x}^{\ast})=0 + \it\text{random noise}$ at $\textbf{x}^{\ast} = (0, ..., 0)$.",
        name="Quartic",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', 'http://www.cs.unm.edu/~neal.holts/dga/benchmarkFunction/quartic.html', '. Storn, K. Price, “Differntial Evolution - A Simple and Efficient Adaptive Scheme for Global Optimization over Continuous Spaces,” Technical Report no. TR-95-012, International Computer Science Institute, Berkeley, CA, 1996. [Available Online'],
        tags=TODO,
    ),
    # Rastrigin
    dict(
        dimensions="d",
        domain=[-5.12, 5.12],
        domain_latex=
            r"xi ∈ [-5.12, 5.12], for all i = 1, …, d",
            r"x_i \in [-5.12, 5.12], i=1,...,n",
            r"$x_i \in [-5.12, 5.12]$ for $i = 1, ..., n$ ",
        latex=
            r"f_{\text{Rastrigin}}(\mathbf{x}) = 10n \sum_{i=1}^n \left[ x_i^2 - 10 \cos(2\pi x_i) \right]",
            r"$$f(\textbf{x})=f(x_1, ..., x_n)=10n + \sum_{i=1}^{n}(x_i^2 - 10cos(2\pi x_i))$$",
        links=[
            "https://www.sfu.ca/~ssurjano/rastr.html",
            "http://infinity77.net/global_optimization/test_functions_nd_R.html#go_benchmark.Rastrigin",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/rastriginfcn.markdown",
        ],
        method=benchmarknd.Functions()._rastrigin__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0 at $\textbf{x}^{\ast} = (0, 0)$.",
        name="Rastrigin",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.', 'Pohlheim, H. GEATbx Examples: Examples of Objective Functions (2005). Retrieved June 2013, from http://www.geatbx.com/download/GEATbx_ObjFunExpl_v37.pdf.'],
            ['http://www.sfu.ca/~ssurjano/rastr.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization'],
        tags=TODO,
    ),
    # Ridge
    dict(
        dimensions="TODO",
        domain=[-5, 5],
        domain_latex=r"$x_i \in [-5, 5]$ for $i=1, 2$",
        latex=r"$$f(\textbf{x}) = x_1 + d\left(\sum_{i=2}^{n}x_i^2\right)^\alpha$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/ridgefcn.markdown",
        ],
        method=benchmarknd.Functions()._ridge__,
        minima=None,
        minima_latex=r"The global minimum of the function depends on the hypercube it is defined on. On the hypercube $$[-\gamma, \gamma]^n$$, $f(\textbf{x}^{\ast})= -\gamma$ located at $\mathbf{x^\ast}=(-\gamma, 0, ..., 0)$.",
        name="Ridge",
        references=
            ['eyer HG., Finck S. (2012) HappyCat – A Simple Function Class Where Well-Known Direct Search Algorithms Do Fail. In: Coello C.A.C., Cutello V., Deb K., Forrest S., Nicosia G., Pavone M. (eds) Parallel Problem Solving from Nature - PPSN XII. PPSN 2012. Lecture Notes in Computer Science, vol 7491. Springer, Berlin, Heidelberg, [https://doi.org/10.1007/978-3-642-32937-1_37', 'yman, A.I.: Convergence Behavior of Evolution Strategies on Ridge Functions. Ph.D. Thesis, University of Dortmund, Department of Computer Science (1999'],
        tags=TODO,
    ),
    # Rosenbrock
    dict(
        dimensions="d",
        domain=[-5, 10],
        domain_latex=
            r"xi ∈ [-5, 10], for all i = 1, …, d, although it may be restricted to the hypercube xi ∈ [-2.048, 2.048], for all i = 1, …, d",
            r"x_i \in [-5, 10], i=1,...,n",
            r"$x_i \in [-5, 10]$ for $i=1, ..., n$ ",
        latex=
            r"f_{\text{Rosenbrock}}(\mathbf{x}) = \sum_{i=1}^{n-1} [100(x_i^2 - x_{i+1})^2 + (x_i - 1)^2]",
            r"$$f(\textbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n-1}[b (x_{i+1} - x_i^2)^ 2 + (a - x_i)^2]$$",
        links=[
            "https://www.sfu.ca/~ssurjano/rosen.html",
            "http://infinity77.net/global_optimization/test_functions_nd_R.html#go_benchmark.Rosenbrock",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/rosenbrockfcn.markdown",
        ],
        method=benchmarknd.Functions()._rosenbrock__,
        minima=dict("f(x_i)"=0, "x_i"=1),
        minima_latex=
            r"f(x_i) = 0 for x_i = 1 for i=1,...,n",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (1, ..., 1)$.",
        name="Rosenbrock",
        references=
            ['Dixon, L. C. W., & Szego, G. P. (1978). The global optimization problem: an introduction. Towards global optimization, 2, 1-15.', 'Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.', 'Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June 2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf.', 'Picheny, V., Wagner, T., & Ginsbourger, D. (2012). A benchmark of kriging-based infill criteria for noisy optimization.'],
            ['http://www.sfu.ca/~ssurjano/rosen.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Salomon
    dict(
        dimensions="TODO",
        domain=[-100, 100],
        domain_latex=
            r"x_i \in [-100, 100], i=1,...,n",
            r"$x_i \in [-100, 100]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Salomon}}(\mathbf{x}) = 1 - \cos \left (2 \pi \sqrt{\sum_{i=1}^{n} x_i^2} \right) + 0.1 \sqrt{\sum_{i=1}^n x_i^2}",
            r"$$f(\mathbf x)=f(x_1, ..., x_n)=1-cos(2\pi\sqrt{\sum_{i=1}^{D}x_i^2})+0.1\sqrt{\sum_{i=1}^{D}x_i^2}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Salomon",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/salomonfcn.markdown",
        ],
        method=benchmarknd.Functions()._salomon__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, ..., 0)$.",
        name="Salomon",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', 'http://profesores.elo.utfsm.cl/~tarredondo/info/soft-comp/functions/node12.html', '. Salomon, “Re-evaluating Genetic Algorithm Performance Under Corodinate Rotation of Benchmark Functions: A Survey of Some Theoretical and Practical Aspects of Genetic Algorithms,” BioSystems, vol. 39, no. 3, pp. 263-278, 1996'],
        tags=TODO,
    ),
    # Schaffer N1
    dict(
        dimensions="TODO",
        domain=[-100, 100],
        domain_latex=
            r"x_i \in [-100, 100], i=1,2",
            r"$x_i \in [-100, 100]$ for $i=1, 2$",
        latex=
            r"f_{\text{Schaffer01}}(\mathbf{x}) = 0.5 + \frac{\sin^2 (x_1^2 + x_2^2)^2 - 0.5}{1 + 0.001(x_1^2 + x_2^2)^2}",
            r"$$f(x, y)=0.5 + \frac{sin^2(x^2+y^2)^2-0.5}{(1+0.001(x^2+y^2))^2}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Schaffer01",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schaffern1fcn.markdown",
        ],
        method=benchmark2d.Functions()._schaffer_n1__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,2",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, 0)$.",
        name=
            "Schaffer 1",
            "Schaffer N. 1",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. K. Mishra, “Some New Test Functions For Global Optimization And Performance of Repulsive Particle Swarm Method,” [Available Online'],
        tags=TODO,
    ),
    # Schaffer N2
    dict(
        dimensions=2,
        domain=[-100, 100],
        domain_latex=
            r"xi ∈ [-100, 100], for all i = 1, 2",
            r"x_i \in [-100, 100], i=1,2",
            r"$x_i \in [-100, 100]$ for $i=1, 2$",
        latex=
            r"f_{\text{Schaffer02}}(\mathbf{x}) = 0.5 + \frac{\sin^2 (x_1^2 - x_2^2)^2 - 0.5}{1 + 0.001(x_1^2 + x_2^2)^2}",
            r"$$f(x, y)=0.5 + \frac{sin^2(x^2-y^2)-0.5}{(1+0.001(x^2+y^2))^2}$$",
        links=[
            "https://www.sfu.ca/~ssurjano/schaffer2.html",
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Schaffer02",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schaffern2fcn.markdown",
        ],
        method=benchmark2d.Functions()._schaffer_n2__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,2",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0.0$ at $\textbf{x}^{\ast} = (0, 0)$.",
        name=
            "Schaffer 2",
            "Schaffer Function N. 2",
            "Schaffer N. 2",
        references=
            ['Test functions for optimization. In Wikipedia. Retrieved June 2013, from https://en.wikipedia.org/wiki/Test_functions_for_optimization.'],
            ['http://www.sfu.ca/~ssurjano/schaffer2.html', 'https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. K. Mishra, “Some New Test Functions For Global Optimization And Performance of Repulsive Particle Swarm Method,” [Available Online'],
        tags=TODO,
    ),
    # Schaffer N3
    dict(
        dimensions="TODO",
        domain=[-100, 100],
        domain_latex=
            r"x_i \in [-100, 100], i=1,2",
            r"$x_i \in [-100, 100]$ for $i=1, 2$",
        latex=
            r"f_{\text{Schaffer03}}(\mathbf{x}) = 0.5 + \frac{\sin^2 \left( \cos \lvert x_1^2 - x_2^2 \rvert \right ) - 0.5}{1 + 0.001(x_1^2 + x_2^2)^2}",
            r"$$f(x, y)=0.5 + \frac{sin^2(cos(|x^2-y^2|))-0.5}{(1+0.001(x^2+y^2))^2}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Schaffer03",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schaffern3fcn.markdown",
        ],
        method=benchmark2d.Functions()._schaffer_n3__,
        minima=dict("f(x_i)"=0.00156685, "\mathbf{x}"=[0, 1.253115]),
        minima_latex=
            r"f(x_i) = 0.00156685 for \mathbf{x} = [0, 1.253115]",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0.00156685$ at $\textbf{x}^{\ast} = (0, 1.253115)$.",
        name=
            "Schaffer 3",
            "Schaffer N. 3",
        references=
            ['. K. Mishra, “Some New Test Functions For Global Optimization And Performance of Repulsive Particle Swarm Method,” [Available Online', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008'],
        tags=TODO,
    ),
    # Schaffer N4
    dict(
        dimensions=2,
        domain=[-100, 100],
        domain_latex=
            r"xi ∈ [-100, 100], for all i = 1, 2",
            r"x_i \in [-100, 100], i=1,2",
            r"$x_i \in [-100, 100]$ for $i=1, 2$",
        latex=
            r"f_{\text{Schaffer04}}(\mathbf{x}) = 0.5 + \frac{\cos^2 \left( \sin(x_1^2 - x_2^2) \right ) - 0.5}{1 + 0.001(x_1^2 + x_2^2)^2}",
            r"$$f(x, y)=0.5 + \frac{cos^2(sin(|x^2-y^2|))-0.5}{(1+0.001(x^2+y^2))^2}$$",
        links=[
            "https://www.sfu.ca/~ssurjano/schaffer4.html",
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Schaffer04",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schaffern4fcn.markdown",
        ],
        method=benchmark2d.Functions()._schaffer_n4__,
        minima=dict("f(x_i)"=0.292579, "\mathbf{x}"=[0, 1.253115]),
        minima_latex=
            r"f(x_i) = 0.292579 for \mathbf{x} = [0, 1.253115]",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0.292579$ at $\textbf{x}^{\ast} = (0, 1.253115)$.",
        name=
            "Schaffer 4",
            "Schaffer Function N. 4",
            "Schaffer N. 4",
        references=
            ['Test functions for optimization. In Wikipedia. Retrieved June 2013, from https://en.wikipedia.org/wiki/Test_functions_for_optimization.'],
            ['https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'rpackages.ianhowson.com/cran/smoof/man/makeSchafferN4Function.html', 'omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. K. Mishra, “Some New Test Functions For Global Optimization And Performance of Repulsive Particle Swarm Method,” [Available Online'],
        tags=TODO,
    ),
    # Schwefel
    dict(
        dimensions="d",
        domain=
            [-100, 100],
            [-500, 500],
        domain_latex=
            r"xi ∈ [-500, 500], for all i = 1, …, d",
            r"x_i \in [-100, 100], i=1,...,n",
            r"$x_i \in [-500, 500]$ for $i = 1..n$",
        latex=
            r"f_{\text{Schwefel01}}(\mathbf{x}) = \left(\sum_{i=1}^n x_i^2 \right)^{\alpha}",
            r"$$f(\textbf{x}) = f(x_1, x_2, ..., x_n) = 418.9829d -{\sum_{i=1}^{n} x_i sin(\sqrt{|x_i|})}.$$",
        links=[
            "https://www.sfu.ca/~ssurjano/schwef.html",
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Schwefel01",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schwefelfcn.markdown",
        ],
        method=benchmarknd.Functions()._schwefel__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"$f(\textbf{x}^{\ast}) = 0$ at $\textbf{x}^{\ast} = (420.9687, ..., 420.9687)$",
        name=
            "Schwefel",
            "Schwefel 1",
        references=
            ['GEATbx: Examples of Objective Functions. Retrieved September 2014, from http://www.pg.gda.pl/~mkwies/dyd/geadocu/fcnfun7.html.', 'Global Optimization Test Functions Index. Retrieved June 2013, from http://infinity77.net/global_optimization/test_functions.html#test-functions-index.', 'Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.', 'Laguna, M., & Marti, R. Experimental Testing of Advanced Scatter Search Designs for Global Optimization of Multimodal Functions (2002). Retrieved June 2013, from http://www.uv.es/rmarti/paper/docs/global1.pdf.'],
            ['ttp://www.sfu.ca/~ssurjan'],
        tags=TODO,
    ),
    # Schwefel 2 20
    dict(
        dimensions="TODO",
        domain=[-100, 100],
        domain_latex=
            r"x_i \in [-100, 100], i=1,...,n",
            r"$x_i \in [-100, 100]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Schwefel20}}(\mathbf{x}) = \sum_{i=1}^n \lvert x_i \rvert",
            r"$$f(\mathbf x)=f(x_1, ..., x_n)=\sum_{i=1}^n |x_i|$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Schwefel20",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schwefel220fcn.markdown",
        ],
        method=benchmarknd.Functions()._schwefel_2_20__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, ..., 0)$.",
        name=
            "Schwefel 2.20",
            "Schwefel 20",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. P. Schwefel, “Numerical Optimization for Computer Models,” John Wiley Sons, 1981'],
        tags=TODO,
    ),
    # Schwefel 2 21
    dict(
        dimensions="TODO",
        domain=[-100, 100],
        domain_latex=
            r"x_i \in [-100, 100], i=1,...,n",
            r"$x_i \in [-100, 100]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Schwefel21}}(\mathbf{x}) = \smash{\displaystyle\max_{1 \leq i \leq n}} \lvert x_i \rvert",
            r"$$f(\mathbf{x})=f(x_1, ..., x_n)=\max_{i=1,...,n}|x_i| $$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Schwefel21",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schwefel221fcn.markdown",
        ],
        method=benchmarknd.Functions()._schwefel_2_21__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, ..., 0)$.",
        name=
            "Schwefel 2.21",
            "Schwefel 21",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. P. Schwefel, “Numerical Optimization for Computer Models,” John Wiley Sons, 1981'],
        tags=TODO,
    ),
    # Schwefel 2 22
    dict(
        dimensions="TODO",
        domain=[-100, 100],
        domain_latex=r"$x_i \in [-100, 100]$ for $i=1, ..., n$",
        latex=r"$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}|x_i|+\prod_{i=1}^{n}|x_i| $$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schwefel222fcn.markdown",
        ],
        method=benchmarknd.Functions()._schwefel_2_22__,
        minima=None,
        minima_latex=r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, ..., 0)$.",
        name="Schwefel 2.22",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. P. Schwefel, “Numerical Optimization for Computer Models,” John Wiley Sons, 1981', 'http://www.cs.unm.edu/~neal.holts/dga/benchmarkFunction/schwefel222.html', 'http://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/190-schwefel-s-function-2-22'],
        tags=TODO,
    ),
    # Schwefel 2 23
    dict(
        dimensions="TODO",
        domain=[-10, 10],
        domain_latex=r"$x_i \in [-10, 10]$ for $i=1, ..., n$",
        latex=r"$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}x_i^{10}$$",
        links=[
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/schwefel223fcn.markdown",
        ],
        method=benchmarknd.Functions()._schwefel_2_23__,
        minima=None,
        minima_latex=r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, ..., 0)$.",
        name="Schwefel 2.23",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. P. Schwefel, “Numerical Optimization for Computer Models,” John Wiley Sons, 1981'],
        tags=TODO,
    ),
    # Shubert
    dict(
        dimensions=2,
        domain=[-10, 10],
        domain_latex=
            r"xi ∈ [-10, 10], for all i = 1, 2, although this may be restricted to the square xi ∈ [-5.12, 5.12], for all i = 1, 2",
            r"$x_i \in [-10, 10]$ for $i=1, ..., n$",
        latex=r"$$f(\mathbf{x})=f(x_1, ...,x_n)=\prod_{i=1}^{n}{\left(\sum_{j=1}^5{ cos((j+1)x_i+j)}\right)}$$",
        links=[
            "https://www.sfu.ca/~ssurjano/shubert.html",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/shubertfcn.markdown",
        ],
        method=benchmarknd.Functions()._shubert__,
        minima=None,
        minima_latex=r"The function has 18 global minima $f(\textbf{x}^{\ast})\approx-186.7309$.",
        name="Shubert",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.'],
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. P. Adorio, U. P. Dilman, “MVF - Multivariate Test Function Library in C for Unconstrained Global Optimization Methods,” [Available Online'],
        tags=TODO,
    ),
    # Shubert 3
    dict(
        dimensions="TODO",
        domain=[-10, 10],
        domain_latex=
            r"x_i \in [-10, 10], i=1,...,n",
            r"$x_i \in [-10, 10]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{Shubert03}}(\mathbf{x}) = \sum_{i=1}^n \sum_{j=1}^5 j \sin \left[(j+1)x_i \right] + j",
            r"$$f(\mathbf{x})=f(x_1, ...,x_n)=\sum_{i=1}^{n}{\sum_{j=1}^5{j sin((j+1)x_i+j)}}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Shubert03",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/shubert3fcn.markdown",
        ],
        method=benchmarknd.Functions()._shubert_3__,
        minima=dict("f(x_i)"=-24.062499, "\mathbf{x}"=[5.791794, 5.791794]),
        minima_latex=
            r"f(x_i) = -24.062499 for \mathbf{x} = [5.791794, 5.791794] (and many others).",
            r"The function has one global minimum $f(\textbf{x}^{\ast})\approx-29.6733337$.",
        name="Shubert 3",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. P. Adorio, U. P. Dilman, “MVF - Multivariate Test Function Library in C for Unconstrained Global Optimization Methods,” [Available Online'],
        tags=TODO,
    ),
    # Shubert 4
    dict(
        dimensions="TODO",
        domain=[-10, 10],
        domain_latex=r"x_i \in [-10, 10], i=1,...,n",
        latex=r"f_{\text{Shubert04}}(\mathbf{x}) = \sum_{i=1}^n \sum_{j=1}^5 j \cos \left[(j+1)x_i \right] + j",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Shubert04",
        ],
        method=benchmarknd.Functions()._shubert_4__,
        minima=dict("f(x_i)"=-29.016015, "\mathbf{x}"=[-0.80032121, -7.08350592]),
        minima_latex=r"f(x_i) = -29.016015 for \mathbf{x} = [-0.80032121, -7.08350592] (and many others).",
        name="Shubert 4",
        tags=TODO,
    ),
    # Sphere
    dict(
        dimensions="d",
        domain=
            [-1, 1],
            [-5.12, 5.12],
        domain_latex=
            r"xi ∈ [-5.12, 5.12], for all i = 1, …, d",
            r"x_i \in [-1, 1], i=1,...,n",
            r"$x_i \in [-5.12, 5.12]$ for $i = 1..n$",
        latex=
            r"f_{\text{Sphere}}(\mathbf{x}) = \sum_{i=1}^{n} x_i^2",
            r"$$f(\textbf{x}) = f(x_1, x_2, ..., x_n) = {\sum_{i=1}^{n} x_i^{2}}.$$",
        links=[
            "https://www.sfu.ca/~ssurjano/spheref.html",
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.Sphere",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/spherefcn.markdown",
        ],
        method=benchmarknd.Functions()._sphere__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"$f(\textbf{x}^{\ast}) = 0$ at $\textbf{x}^{\ast} = (0, ..., 0)$",
        name="Sphere",
        references=
            ['Dixon, L. C. W., & Szego, G. P. (1978). The global optimization problem: an introduction. Towards global optimization, 2, 1-15.', 'Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June 2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf.', 'Picheny, V., Wagner, T., & Ginsbourger, D. (2012). A benchmark of kriging-based infill criteria for noisy optimization.'],
            ['ttp://www.sfu.ca/~ssurjano/spheref.htm', 'ttps://en.wikipedia.org/wiki/Test_functions_for_optimizatio'],
        tags=TODO,
    ),
    # Styblinski
    dict(
        dimensions="d",
        domain=[-5, 5],
        domain_latex=
            r"xi ∈ [-5, 5], for all i = 1, …, d",
            r"x_i \in [-5, 5], i=1,...,n",
            r"$x \in [-5, 5]$ for all $i = 1,...,n$",
        latex=
            r"f_{\text{StyblinskiTang}}(\mathbf{x}) = \sum_{i=1}^{n} \left(x_i^4 - 16x_i^2 + 5x_i \right)",
            r"$$f(\textbf{x}) = f(x_1, ..., x_n)= \frac{1}{2}\sum_{i=1}^{n} (x_i^4 -16x_i^2+5x_i)$$",
        links=[
            "https://www.sfu.ca/~ssurjano/stybtang.html",
            "http://infinity77.net/global_optimization/test_functions_nd_S.html#go_benchmark.StyblinskiTang",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/styblinskitankfcn.markdown",
        ],
        method=benchmarknd.Functions()._styblinski__,
        minima=dict("f(x_i)"=r"-39.16616570377142n", "x_i"=-2.903534018185960),
        minima_latex=
            r"f(x_i) = -39.16616570377142n for x_i = -2.903534018185960 for i=1,...,n",
            r"The function has one global minimum at: $f(x^*)=-39.16599\textbf{n}$ at $\textbf{x}^{\ast} = (-2.903534, ..., -2.903534)$.",
        name=
            "Styblinski-Tang",
            "Styblinski-Tank",
            "StyblinskiTang",
        references=
            ['Global Optimization Test Functions Index. Retrieved June 2013, from http://infinity77.net/global_optimization/test_functions.html#test-functions-index.'],
            ['http://www.sfu.ca/~ssurjano/stybtang.html'],
        tags=TODO,
    ),
    # Sum Squres
    dict(
        dimensions="d",
        domain=[-10, 10],
        domain_latex=
            r"xi ∈ [-10, 10], for all i = 1, …, d, although this may be restricted to the hypercube xi ∈ [-5.12, 5.12], for all i = 1, …, d",
            r"$x_i \in [-10, 10]$ for $i=1, ..., n$",
        latex=r"$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}{ix_i^2}$$",
        links=[
            "https://www.sfu.ca/~ssurjano/sumsqu.html",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/sumsquaresfcn.markdown",
        ],
        method=benchmarknd.Functions()._sum_squres__,
        minima=None,
        minima_latex=r"The function has one global minimum $f(\mathbf{x}^{\ast})=0$ at $\mathbf{x}^{\ast}=0$.",
        name="Sum Squares",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.', 'Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June 2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf.'],
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', 'http://www.sfu.ca/~ssurjano/sumsqu.html', '.-R. Hedar, “Global Optimization Test Problems,” [Available Online'],
        tags=TODO,
    ),
    # Three Hump Camel
    dict(
        dimensions=2,
        domain=[-5, 5],
        domain_latex=
            r"xi ∈ [-5, 5], for all i = 1, 2",
            r"x_i \in [-5, 5], i=1,2",
            r"$x_i \in [-5, 5]$ for $i=1, 2$",
        latex=
            r"f_{\text{ThreeHumpCamel}}(\mathbf{x}) = 2x_1^2 - 1.05x_1^4 + \frac{x_1^6}{6} + x_1x_2 + x_2^2",
            r"$$f(x,y)=2x^2-1.05x^4+\frac{x^6}{6}+xy+y^2$$",
        links=[
            "https://www.sfu.ca/~ssurjano/camel3.html",
            "http://infinity77.net/global_optimization/test_functions_nd_T.html#go_benchmark.ThreeHumpCamel",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/threehumpcamelfcn.markdown",
        ],
        method=benchmark2d.Functions()._three_hump_camel__,
        minima=dict("f(x_i)"=0, "\mathbf{x}"=[0, 0]),
        minima_latex=
            r"f(x_i) = 0 for \mathbf{x} = [0, 0]",
            r"The function has one global minimum $f(\textbf{x}^{\ast})=0$ at $\textbf{x}^{\ast} = (0, 0)$.",
        name=
            "Three Hump Camel",
            "Three-Hump Camel",
        references=
            ['Test functions for optimization. In Wikipedia. Retrieved June 2013, from https://en.wikipedia.org/wiki/Test_functions_for_optimization.'],
            ['https://en.wikipedia.org/wiki/Test_functions_for_optimization', 'http://www.sfu.ca/~ssurjano/camel3.html'],
        tags=TODO,
    ),
    # Wolfe
    dict(
        dimensions="TODO",
        domain=[0, 2],
        domain_latex=
            r"x_i \in [0, 2], i=1,2,3",
            r"$x_i \in [0, 2]$ for $i=1, ..., 3$",
        latex=
            r"f_{\text{Wolfe}}(\mathbf{x}) = \frac{4}{3}(x_1^2 + x_2^2 - x_1x_2)^{0.75} + x_3",
            r"$$f(x, y, z) = \frac{4}{3}(x^2 + y^2 - xy)^{0.75} + z$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_W.html#go_benchmark.Wolfe",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/wolfefcn.markdown",
        ],
        method=benchmark3d.Functions()._wolfe__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,2,3",
            r"The global minima $f(\textbf{x}^{\ast})=0$ are located at $\mathbf{x^\ast}=(0, 0, 0)$.",
        name="Wolfe",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. P. Schwefel, “Numerical Optimization for Computer Models,” John Wiley Sons, 1981'],
        tags=TODO,
    ),
    # Xin She Yang
    dict(
        dimensions="TODO",
        domain=[-5, 5],
        domain_latex=
            r"x_i \in [-5, 5], i=1,...,n",
            r"$x_i \in [-5, 5]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{XinSheYang01}}(\mathbf{x}) = \sum_{i=1}^{n} \epsilon_i \lvert x_i \rvert^i",
            r"$$f(\mathbf x)=f(x_1, ...,x_n)=\sum_{i=1}^{n}\epsilon_i|x_i|^i$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_X.html#go_benchmark.XinSheYang01",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/xinsheyangn1fcn.markdown",
        ],
        method=benchmarknd.Functions()._xin_she_yang__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The global minima $f(\textbf{x}^{\ast})=0$ are located at $\mathbf{x^\ast}=(0, ..., 0)$.",
        name=
            "Xin-She Yang",
            "Xin-She Yang 1",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. S. Yang, “Test Problems in Optimization,” Engineering Optimization: An Introduction with Metaheuristic Applications John Wliey & Sons, 2010. [Available Online'],
        tags=TODO,
    ),
    # Xin She Yang N2
    dict(
        dimensions="TODO",
        domain=
            [-2np.pi, 2np.pi],
            [-2*np.pi, 2*np.pi],
        domain_latex=
            r"x_i \in [-2\pi, 2\pi], i=1,...,n",
            r"$x_i \in [-2\pi, 2\pi]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{XinSheYang02}}(\mathbf{x}) = \frac{\sum_{i=1}^{n} \lvert{x_{i}}\rvert}{e^{\sum_{i=1}^{n} \sin\left(x_{i}^{2.0}\right)}}",
            r"$$f(\mathbf{x})=f(x_1, ..., x_n)=(\sum_{i=1}^{n}|x_i|)exp(-\sum_{i=1}^{n}sin(x_i^2))$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_X.html#go_benchmark.XinSheYang02",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/xinsheyangn2fcn.markdown",
        ],
        method=benchmarknd.Functions()._xin_she_yang_n2__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"The global minimum $f(\textbf{x}^{\ast})=0$ are located at $\mathbf{x^\ast}=(0, ..., 0)$.",
        name=
            "Xin-She Yang 2",
            "Xin-She Yang N. 2",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. S. Yang, “Test Problems in Optimization,” Engineering Optimization: An Introduction with Metaheuristic Applications John Wliey & Sons, 2010. [Available Online'],
        tags=TODO,
    ),
    # Xin She Yang N3
    dict(
        dimensions="TODO",
        domain=
            [-20, 20],
            [-2*np.pi, 2*np.pi],
        domain_latex=
            r"x_i \in [-20, 20], i=1,...,n",
            r"$x_i \in [-2\pi, 2\pi]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{XinSheYang03}}(\mathbf{x}) = e^{-\sum_{i=1}^{n} (x_i/\beta)^{2m}} - 2e^{-\sum_{i=1}^{n} x_i^2} \prod_{i=1}^{n} \cos^2(x_i)",
            r"$$f(\mathbf x)=f(x_1, ..., x_n) =exp(-\sum_{i=1}^{n}(x_i / \beta)^{2m}) - 2exp(-\sum_{i=1}^{n}x_i^2) \prod_{i=1}^{n}cos^ 2(x_i) $$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_X.html#go_benchmark.XinSheYang03",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/xinsheyangn3fcn.markdown",
        ],
        method=benchmarknd.Functions()._xin_she_yang_n3__,
        minima=dict("f(x_i)"=-1, "x_i"=0),
        minima_latex=
            r"f(x_i) = -1 for x_i = 0 for i=1,...,n",
            r"The global minimum $f(\textbf{x}^{\ast})=-1$ are located at $\mathbf{x^\ast}=(0, ..., 0)$ for $m=5$ and $\beta = 15$.",
        name=
            "Xin-She Yang 3",
            "Xin-She Yang N. 3",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. S. Yang, “Test Problems in Optimization,” Engineering Optimization: An Introduction with Metaheuristic Applications John Wliey & Sons, 2010. [Available Online'],
        tags=TODO,
    ),
    # Xin She Yang N4
    dict(
        dimensions="TODO",
        domain=[-10, 10],
        domain_latex=
            r"x_i \in [-10, 10], i=1,...,n",
            r"$x_i \in [-10, 10]$ for $i=1, ..., n$",
        latex=
            r"f_{\text{XinSheYang04}}(\mathbf{x}) = \left[ \sum_{i=1}^{n} \sin^2(x_i) - e^{-\sum_{i=1}^{n} x_i^2} \right ] e^{-\sum_{i=1}^{n} \sin^2 \sqrt{ \lvert x_i \rvert }}",
            r"$$f(\mathbf x)=f(x_1, ..., x_n)=\left(\sum_{i=1}^{n}sin^2(x_i)-e^{-\sum_{i=1}^{n}x_i^2}\right)e^{-\sum_{i=1}^{n}{sin^2\sqrt{|x_i|}}}$$",
        links=[
            "http://infinity77.net/global_optimization/test_functions_nd_X.html#go_benchmark.XinSheYang04",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/xinsheyangn4fcn.markdown",
        ],
        method=benchmarknd.Functions()._xin_she_yang_n4__,
        minima=dict("f(x_i)"=-1, "x_i"=0),
        minima_latex=
            r"f(x_i) = -1 for x_i = 0 for i=1,...,n",
            r"The global minimum $f(\textbf{x}^{\ast})=-1$ are located at $\mathbf{x^\ast}=(0, ..., 0)$.",
        name=
            "Xin-She Yang 4",
            "Xin-She Yang N. 4",
        references=
            ['omin Jamil and Xin-She Yang, A literature survey of benchmark functions for global optimization problems, Int. Journal of Mathematical Modelling and Numerical Optimisation}, Vol. 4, No. 2, pp. 150--194 (2013), [arXiv:1308.4008', '. S. Yang, “Test Problems in Optimization,” Engineering Optimization: An Introduction with Metaheuristic Applications John Wliey & Sons, 2010. [Available Online'],
        tags=TODO,
    ),
    # Zakharov
    dict(
        dimensions="d",
        domain=[-5, 10],
        domain_latex=
            r"xi ∈ [-5, 10], for all i = 1, …, d",
            r"x_i \in [-5, 10], i=1,...,n",
            r"$x_i \in [-5, 10]$ for $i = 1..n$",
        latex=
            r"f_{\text{Zacharov}}(\mathbf{x}) = \sum_{i=1}^{n} x_i^2 + \left ( \frac{1}{2} \sum_{i=1}^{n} i x_i \right )^2 + \left ( \frac{1}{2} \sum_{i=1}^{n} i x_i \right )^4",
            r"$$f(\textbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^n x_i^{2}+(\sum_{i=1}^n 0.5ix_i)^2 + (\sum_{i=1}^n 0.5ix_i)^4$$",
        links=[
            "https://www.sfu.ca/~ssurjano/zakharov.html",
            "http://infinity77.net/global_optimization/test_functions_nd_Z.html#go_benchmark.Zacharov",
            "https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/zakharov.markdown",
        ],
        method=benchmarknd.Functions()._zakharov__,
        minima=dict("f(x_i)"=0, "x_i"=0),
        minima_latex=
            r"f(x_i) = 0 for x_i = 0 for i=1,...,n",
            r"$f(\textbf{x}^{\ast}) = 0$ at $\textbf{x}^{\ast} = (0, ..., 0)$",
        name=
            "Zacharov",
            "Zakharov",
        references=
            ['Global Optimization Test Problems. Retrieved June 2013, from\nhttp://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.'],
            ['ttp://www.sfu.ca/~ssurjano/zakharov.htm'],
        tags=TODO,
    ),
]