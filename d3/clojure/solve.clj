(ns itsbth.aoc-2021.d3
  (:require [clojure.string :as str]))


(def numbers
  (->> (slurp "../sample")
       (str/split-lines)))

(def width (count (nth numbers 0)))

; only handling five (sample) and twelve (input) bits
(def full-mask (if (= width 12) 2r111111111111 2r11111))

(defn parse-int [ns]
  (Integer/parseInt ns 2))

(defn count-n-bits [numbers n]
  (->> numbers
       (map #(nth % n))
       (filter (partial = \1))
       (count)))

(->> (range width)
     (map #(count-n-bits numbers %))
     (map #(>= % (/ (count numbers) 2)))
     (map #(if % \1 \0))
     (str/join)
     (parse-int)
     (#(* % (bit-xor % full-mask)))
     (printf "Part 1: %d\n"))

(loop [candidates numbers bit 0])


