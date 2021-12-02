(ns itsbth.aoc-2021.d1)
(require '[clojure.string :as str])


(defn parse-int [ns]
    (Integer/parseInt ns 10))

; part 1, solved at a repl
(->> (slurp "../input")
    (str/split-lines)
    (map parse-int)
    (partition 2 1)
    (filter (partial reduce <))
    (count)
    (printf "Part 1: %d\n"))

; part 2
(->> (slurp "../input")
    (str/split-lines)
    (map parse-int)
    (partition 3 1)
    (map (partial reduce +))
    (partition 2 1)
    (filter (partial reduce <))
    (count)
    (printf "Part 2: %d\n"))

;; REMARKS: Not very DRY. Part 2 is a copy of part 1 with two lines added and two lines changed, even reading the file again.
;;          Varying parameter order forced me to use as->, making it significantly less clean. Would probably have been worth
;;          it to define helper functions, but all in all not that interesting of a problem that I want to spend more time.
