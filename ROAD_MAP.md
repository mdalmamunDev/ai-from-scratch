# AI Model From Scratch — Practice-Driven Roadmap

**22+ Week Challenge-Based Learning Plan**

Goal: understand how AI models work internally by learning the mathematics, implementing algorithms from scratch, solving progressively harder problems, and finally building a small GPT-style language model. Every phase contains exercises, implementation challenges, and a project.

## How to Use This Roadmap

- Complete the core challenges before moving to the next phase.
- For major algorithms follow: **Learn → Practice → Challenge → Build → Review → Refactor**.
- Attempt every implementation yourself before looking at a solution; use hints first.
- Keep all work in one Git repository with a folder per phase.
- Write short notes on what you implemented and why it works.
- Compare your implementation with NumPy, scikit-learn, or PyTorch afterward.
- Target 1–2 hours per day, 5–6 days per week.

## Phase Overview

| # | Phase | Weeks | Project |
| --- | --- | --- | --- |
| 1 | Python Fundamentals | 1 | Dataset Analyzer CLI |
| 2 | Mathematics for ML | 2–4 | Mini Math Library |
| 3 | ML Fundamentals | 5–6 | ML Experiment Notebook |
| 4 | ML From Scratch | 7–8 | From-Scratch ML Library |
| 5 | NumPy, Pandas, Matplotlib, scikit-learn | 9–10 | End-to-End Classical ML Project |
| 6 | Neural Networks From Scratch | 11–13 | NumPy Neural Network Library |
| 7 | PyTorch | 14–15 | PyTorch Training Pipeline |
| 8 | NLP & Language Modeling | 16–17 | Character-Level Language Model |
| 9 | Transformers & Mini GPT | 18–20 | Mini GPT |
| 10 | Evaluation, Deployment & Engineering | 21–22+ | Final AI System |

---

## Phase 1 — Python Fundamentals (Week 1)

### Learn
- Python syntax, variables, types and type hints
- Conditions, loops and comprehensions
- Lists, tuples, sets and dictionaries
- Functions, parameters, return values and scope
- Modules, imports and virtual environments
- Files, exceptions and debugging
- Basic OOP and reusable code

### Practice
- 10+ basic Python problems: calculator, temperature conversion, validation, statistics
- 10+ data-structure problems using lists/dictionaries/sets
- 5 function-design problems
- Read and process a small CSV/text dataset

### Challenges
1. **Easy:** build a student score analyzer
2. **Medium:** clean and group nested student records
3. **Hard:** implement a reusable `DatasetAnalyzer` class
4. **Engineering:** add validation, exceptions and a CLI interface

### Project
**Dataset Analyzer CLI** — load data, validate it, calculate statistics, filter records and generate a summary.

---

## Phase 2 — Mathematics for Machine Learning (Weeks 2–4)

### Learn
- Vectors, matrices, dimensions and shapes
- Dot product and matrix multiplication
- Vector transformations and geometric intuition
- Mean, variance and standard deviation
- Probability and conditional probability
- Random variables and distributions
- Functions and derivatives
- Partial derivatives, gradients and chain rule

### Practice
- 20+ vector and matrix calculation problems
- Implement vector addition, dot product and matrix multiplication manually
- 10+ statistics/probability exercises
- 10+ derivative and gradient exercises

### Challenges
1. **Easy:** implement vector operations without NumPy
2. **Medium:** build a `Matrix` class with multiplication
3. **Hard:** calculate gradients for multivariable functions
4. **AI:** explain mathematically how a weight changes during training

### Project
**Mini Math Library** — vectors, matrices, statistics and basic gradient calculations from scratch.

---

## Phase 3 — Machine Learning Fundamentals (Weeks 5–6)

### Learn
- What machine learning is and is not
- Supervised vs. unsupervised learning
- Features, targets, labels and datasets
- Training, validation and test sets
- Prediction and loss functions
- Overfitting and underfitting
- Bias/variance intuition
- Model evaluation and generalization

### Practice
- 15+ ML concept and reasoning problems
- Manually split datasets into train/validation/test sets
- Calculate MAE, MSE, accuracy and precision/recall manually
- Analyze examples of overfitting and underfitting

### Challenges
1. **Easy:** identify features and targets from real-world problems
2. **Medium:** design a train/validation/test strategy
3. **Hard:** diagnose an intentionally overfit model
4. **Engineering:** create a reusable experiment/evaluation structure

### Project
**ML Experiment Notebook** — load a dataset, define features/target, split data, create a baseline and evaluate it.

---

## Phase 4 — Machine Learning From Scratch (Weeks 7–8)

### Learn
- Linear regression
- Mean Squared Error
- Gradient descent
- Learning rate and convergence
- Logistic regression
- Sigmoid function
- Binary classification
- Training loops and parameter updates

### Practice
- Calculate predictions and MSE manually
- Implement prediction, loss, gradient and parameter update functions
- Implement gradient descent without ML libraries
- Implement logistic regression and sigmoid
- Create 15+ regression/classification experiments

### Challenges
1. **Easy:** fit a line to a tiny dataset
2. **Medium:** implement `LinearRegression` from scratch
3. **Hard:** implement `LogisticRegression` from scratch
4. **Engineering:** create a reusable fit/predict/score API
5. **Comparison:** compare with scikit-learn and explain differences

### Project
**From-Scratch ML Library** — `LinearRegression` and `LogisticRegression` with training, prediction and evaluation.

---

## Phase 5 — NumPy, Pandas, Matplotlib & scikit-learn (Weeks 9–10)

### Learn
- NumPy arrays and vectorized operations
- Broadcasting and matrix operations
- Pandas DataFrames and data cleaning
- Missing values and feature preparation
- Matplotlib visualization
- scikit-learn workflows
- Preprocessing, splitting and evaluation

### Practice
- 20+ NumPy array/vectorization challenges
- 10+ Pandas data-cleaning challenges
- Build 5+ meaningful visualizations
- Train several baseline models using scikit-learn

### Challenges
1. Rewrite a slow Python loop using NumPy vectorization
2. Clean a deliberately messy dataset
3. Find and visualize correlations
4. Build a complete preprocessing → training → evaluation pipeline

### Project
**End-to-End Classical ML Project** — clean a real dataset, visualize it, train multiple models and compare results.

---

## Phase 6 — Neural Networks From Scratch (Weeks 11–13)

### Learn
- Neuron and perceptron
- Weights and bias
- Activation functions
- Forward propagation
- Loss calculation
- Backpropagation
- Chain rule in neural networks
- Stochastic Gradient Descent
- Multi-layer neural networks

### Practice
- Implement a single neuron with NumPy
- Implement ReLU, sigmoid and tanh
- Implement forward propagation
- Implement loss functions
- Derive and implement backpropagation
- Train a network on a small classification dataset

### Challenges
1. **Easy:** build one neuron manually
2. **Medium:** build a single-layer classifier
3. **Hard:** build a multi-layer network with backpropagation
4. **Debug:** diagnose exploding/vanishing gradients
5. **Engineering:** create reusable `Layer` and `NeuralNetwork` abstractions

### Project
**Neural Network From Scratch** — a trainable NumPy library with forward/backward passes and SGD.

---

## Phase 7 — PyTorch (Weeks 14–15)

### Learn
- Tensors
- Autograd and computational graphs
- `nn.Module`
- Loss functions and optimizers
- Datasets and DataLoaders
- Training and validation loops
- CPU/GPU execution
- Saving and loading checkpoints

### Practice
- 15+ tensor manipulation challenges
- Rebuild the NumPy neural network using PyTorch
- Write custom training and validation loops
- Train models with multiple optimizers and learning rates
- Save, load and resume a checkpoint

### Challenges
1. Implement a custom `Dataset`
2. Write a training loop without high-level trainer APIs
3. Move a model between CPU and GPU
4. Investigate why a model is not learning

### Project
**Production-Style PyTorch Training Pipeline** — dataset, model, training loop, validation, checkpointing and metrics.

---

## Phase 8 — NLP & Language Modeling (Weeks 16–17)

### Learn
- Text preprocessing
- Character-level and token-level tokenization
- Vocabulary and token IDs
- Embeddings
- Sequences and context windows
- Next-token prediction
- Cross-entropy loss
- Language-model training

### Practice
- Build a character tokenizer
- Build encode/decode functions
- Create vocabulary mappings
- Generate context-target training pairs
- Implement embeddings
- Train a tiny next-token predictor

### Challenges
1. **Easy:** tokenize a text corpus
2. **Medium:** implement a character-level language model
3. **Hard:** implement batching of context windows
4. **AI:** explain why embeddings are better than raw token IDs

### Project
**Character-Level Language Model** — train a small model that generates text from a custom corpus.

---

## Phase 9 — Transformers & Mini GPT (Weeks 18–20)

### Learn
- Attention intuition
- Query, Key and Value
- Scaled dot-product attention
- Causal/masked attention
- Multi-head attention
- Positional embeddings
- Feed-forward networks
- Residual connections
- Layer normalization
- Transformer decoder block

### Practice
- Implement dot-product similarity
- Implement softmax
- Calculate attention scores manually
- Implement scaled dot-product attention
- Implement causal masking
- Implement a single attention head
- Combine heads into multi-head attention
- Implement a Transformer block

### Challenges
1. Implement attention using only PyTorch tensor operations
2. Add causal masking and verify future tokens cannot leak
3. Implement multi-head self-attention
4. Build a decoder-only Transformer
5. Add training and text generation
6. **Final:** build and train Mini GPT

### Project
**Mini GPT** — a decoder-only Transformer trained for next-token prediction and capable of generating text.

---

## Phase 10 — Evaluation, Deployment & Final Engineering (Weeks 21–22+)

### Learn
- Language-model evaluation
- Training/validation loss analysis
- Inference
- Temperature and sampling
- Top-k/top-p concepts
- Checkpointing
- FastAPI inference service
- Node.js/Express integration
- Deployment and monitoring basics

### Practice
- Compare generated text at different temperatures
- Implement basic sampling strategies
- Measure inference latency
- Build an inference endpoint
- Create a Node.js client for the model API
- Load model checkpoints safely

### Challenges
1. Optimize inference latency
2. Add request validation and error handling
3. Implement streaming-style token generation
4. Containerize the inference service
5. Connect the model to an existing Node.js application

### Project
**Final AI System** — trained model + FastAPI inference service + Node.js integration + evaluation and deployment.

---

## Challenge Rules

- Do not copy the solution before attempting the problem.
- Solve with plain Python first where practical, then optimize with NumPy/PyTorch when the phase calls for it.
- After solving, test edge cases and try to break your implementation.
- Keep a record of failed attempts and what you learned.
- For every major project, write a README covering architecture, mathematics, implementation and results.
- Refactor successful challenge code into reusable components.
- A phase is complete when you can explain the concept, implement it, debug it and use it in a small project.

## Difficulty Progression

| Level | Focus | Expected Work | Rule |
| --- | --- | --- | --- |
| Level 1 — Easy | Understand | Small focused problems | Solve independently |
| Level 2 — Medium | Implement | Algorithms/components | Minimal hints |
| Level 3 — Hard | Combine | Multiple concepts | No solution until attempted |
| Level 4 — Engineering | Build | Reusable/production-style code | Test and refactor |
| Level 5 — Project | Integrate | Complete working system | Explain every major decision |

## Major Milestones

- [ ] 1. Python Dataset Analyzer
- [ ] 2. Mathematical toolkit from scratch
- [ ] 3. Linear and Logistic Regression from scratch
- [ ] 4. End-to-end classical ML project
- [ ] 5. Neural Network using only NumPy
- [ ] 6. PyTorch training pipeline
- [ ] 7. Character-level language model
- [ ] 8. Attention and Transformer implementation
- [ ] 9. Mini GPT
- [ ] 10. Deployed AI model integrated with Node.js

## Recommended Resources

**Python:** [Python Tutorial](https://docs.python.org/3/tutorial/) · [Kaggle Python](https://www.kaggle.com/learn/python) · [Google Colab](https://colab.research.google.com/)

**Math:** [3Blue1Brown Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) · [3Blue1Brown Calculus](https://www.3blue1brown.com/topics/calculus) · [Khan Academy Statistics & Probability](https://www.khanacademy.org/math/statistics-probability)

**ML:** [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) · [StatQuest](https://www.youtube.com/@statquest) · [Kaggle Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning)

**Data tools:** [NumPy Beginner Guide](https://numpy.org/doc/stable/user/absolute_beginners.html) · [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html) · [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html) · [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html)

**Neural nets & PyTorch:** [Karpathy Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) · [Micrograd Lecture](https://www.youtube.com/watch?v=VMj-3S1tku0) · [PyTorch Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) · [PyTorch Examples](https://docs.pytorch.org/tutorials/beginner/pytorch_with_examples.html) · [PyTorch Installation](https://pytorch.org/get-started/locally/)

**Transformers & LLMs:** [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) · [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) · [nanoGPT](https://github.com/karpathy/nanoGPT)

## Completion Target

The goal is not familiarity with AI terminology. You should be able to explain the mathematics behind training, implement core algorithms yourself, build a neural network, implement attention/Transformer components, train a small GPT-style model, evaluate it, expose inference through an API, and integrate it into a real application.