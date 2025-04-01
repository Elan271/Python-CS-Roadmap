import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from "@/components/ui/accordion";
import { Badge } from "@/components/ui/badge";

const phases = [
  {
    title: "Foundations",
    color: "green",
    topics: [
      "Python basics: lists, dicts, sets, tuples",
      "Functions, recursion fundamentals",
      "Bubble, Selection, Insertion sort",
      "Linear & Binary Search"
    ]
  },
  {
    title: "Data Structures & Problem Solving",
    color: "blue",
    topics: [
      "Sliding window, Two pointers",
      "Hashmaps and frequency counts",
      "Linked Lists (basic operations, reversal, cycle detection)",
      "Stacks & Queues: Valid Parentheses, Min Stack"
    ]
  },
  {
    title: "Recursion & Backtracking",
    color: "purple",
    topics: [
      "Subsets, Permutations, Combinations",
      "N-Queens, Sudoku Solver",
      "Word Search"
    ]
  },
  {
    title: "Trees & Graphs",
    color: "orange",
    topics: [
      "Tree Traversals: Inorder, Preorder, Postorder",
      "BST operations: Insert, Delete, Search",
      "DFS, BFS, Topological Sort",
      "Union-Find, Cycle detection"
    ]
  },
  {
    title: "Advanced Techniques",
    color: "red",
    topics: [
      "Dynamic Programming: LCS, LIS, 0/1 Knapsack",
      "Greedy: Huffman Coding, Activity Selection",
      "Bit Manipulation: XOR tricks, Bitmask DP"
    ]
  },
  {
    title: "Competitive & Real-World Focus",
    color: "black",
    topics: [
      "Sieve of Eratosthenes, Modular Arithmetic",
      "Heaps with heapq",
      "Trie (Prefix Tree)",
      "Dijkstra, A* Search",
      "System design: LRU Cache, URL Shortener"
    ]
  }
];

export default function CSAlgorithmsRoadmap() {
  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">🧠 CS Algorithms Roadmap (Python)</h1>
      <Accordion type="multiple">
        {phases.map((phase, index) => (
          <AccordionItem key={index} value={`phase-${index}`}>
            <AccordionTrigger>
              <div className="flex items-center gap-2">
                <Badge variant="outline" className={`text-${phase.color}-600 border-${phase.color}-600`}>{phase.title}</Badge>
              </div>
            </AccordionTrigger>
            <AccordionContent>
              <Card className="bg-muted shadow-sm">
                <CardContent className="p-4 space-y-2">
                  {phase.topics.map((topic, i) => (
                    <div key={i} className="text-base">• {topic}</div>
                  ))}
                </CardContent>
              </Card>
            </AccordionContent>
          </AccordionItem>
        ))}
      </Accordion>
    </div>
  );
}
