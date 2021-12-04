(ns itsbth.aoc-2021.d2
  (:require [clojure.string :as str]
            [clojure.core.match :refer [match]]))

(defn parse-int [ns]
  (Integer/parseInt ns 10))

(defn move [[x y] [cmd n]]
  (match cmd
    "forward" [(+ x n) y]
    "up" [x (- y n)]
    "down" [x (+ y n)]))

(->> (slurp "../input")
     (str/split-lines)
     (map #(str/split % #" "))
     (map (fn [[c n]] [c (parse-int n)]))
     (reduce move [0 0])
     (reduce * 1)
     (printf "Part 1: %d\n"))

(defn move2 [[x y aim] [cmd n]]
  (match cmd
    "forward" [(+ x n) (+ y (* aim n)) aim]
    "up" [x y (- aim n)]
    "down" [x y (+ aim n)]))

(->> (slurp "../input")
     (str/split-lines)
     (map #(str/split % #" "))
     (map (fn [[c n]] [c (parse-int n)]))
     (reduce move2 [0 0 0])
     (take 2)
     (reduce * 1)
     (printf "Part 2: %d\n"))

(defn project [fns values]
  (map #(% values) fns))

(defn flip [fv]
  (fn [& xs]
    (apply fv (reverse xs))))

(->> (slurp "../input")
     (str/split-lines)
     (map #(str/split % #" "))
     (map (fn [[c n]] [c (parse-int n)]))
     (reduce move2 [0 0 0])
     (project [comp (partial reduce * 1)])
     (apply (partial printf "Part 2: %d\n")))
