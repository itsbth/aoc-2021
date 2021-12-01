(require '[clojure.string :as str])

; part 1, solved at a repl
(as-> (slurp "../input") t
    (str/split t #"\n")
    (map #(Integer/parseInt % 10) t)
    (partition 2 1 t)
    (filter #(reduce < %) t)
    (count t)
    (partial printf "Part 1: %d\n"))

; part 2
(as-> (slurp "../input") t
    (str/split t #"\n")
    (map #(Integer/parseInt % 10) t)
    (partition 3 1 t)
    (map (partial reduce +) t)
    (partition 2 1 t)
    (filter #(reduce < %) t)
    (count t)
    (partial printf "Part 2: %d\n"))

;; REMARKS: Not very DRY. Part 2 is a copy of part 1 with two lines added and two lines changed, even reading the file again.
;;          Varying parameter order forced me to use as->, making it significantly less clean. Would probably have been worth
;;          it to define helper functions, but all in all not that interesting of a problem that I want to spend more time.
