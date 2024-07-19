# Match Cellar (Temporal, Numeric, ICE)

## Domain Description

This domain is based on the [Match Cellar (Temporal, Numeric)](../match-cellar-temporal-numeric/).
The difference is that the LIGHT_MATCH action is shorter and have intermediate effects to turn on the light.

This behavior cannot be represented in PDDL and is fully modeled using [UPF](https://github.com/aiplan4eu/unified-planning).
A compiled version is available that split the LIGHT_MATCH action into two actions STRIKE_MATCH and LIT_MATCH, in order to have the intermediate effects between both.
Moreover, the LIGHT_MATCH action is kept and is constrained to overlap the two actions STRIKE_MATCH and LIT_MATCH:

```
conditions    a                b
              +--------------+ +-----------+
actions       | STRIKE_MATCH | | LIT_MATCH |
              +--------------+ +-----------+
effects       not(a)         b not(b)      c

                                           c
              +----------------------------+
              |         LIGHT_MATCH        |
              +----------------------------+
              a                        not(c)
```

## Authors

Roland Godet
