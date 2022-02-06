# Hi!

The idea of this repo/package is to simulate some stochastic processes. So far not so much is possible, but let's see what the future brings.

### Installation:

Clone this repo:

`git clone https://github.com/k-mundinger/stochproc.git`

I would recommend to use a conda env.

`conda create --name stochproc-env python=3.9`

I set up a `Makefile` to make life easier. Change to the folder you cloned the repo to and type:

```
make install
make requirements
```

You can also (for now) skip the `make requirements` part and just install plotly, numpy and matplotlib manually.

Check out the `demo.ipynb` notebook to see what you can use this package for!

