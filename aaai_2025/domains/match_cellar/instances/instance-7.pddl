(define (problem instance7)
    (:domain matchcellar)

    (:init
        (handfree)
        (= (num-matches) 9)
        (= (num-fuses) 18)
        (= (num-lit-matches) 0)
        (= (num-mended-fuses) 0)
    )
    (:goal
        (and
            (= (num-mended-fuses) 18)
        )
    )
    (:metric minimize
        (total-time)
    )
)