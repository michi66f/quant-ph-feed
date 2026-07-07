- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02616v1
- Title: MLIR for Quantum Beyond Gate Cancellation: Quantum Circuit Mapping Reimagined
- Authors: Matthias Reumann, Yannick Stade, Robert Wille, Lukas Burgholzer
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2607.02616v1  pdf=https://arxiv.org/pdf/2607.02616v1.pdf

Abstract:
The Multi-Level Intermediate Representation (MLIR) framework has become a cornerstone for building extensible, domain-specific compilers, with the quantum computing community already leveraging it to model quantum programs and implement basic optimizations. However, computationally intensive tasks in the quantum compilation pipeline, such as quantum circuit mapping, remain underexplored within the MLIR ecosystem. This paper proposes an MLIR-native blueprint for these non-local, quantum-specific optimization routines by reimplementing a well-established, state-of-the-art mapping A* search algorithm for qubit routing and SWAP insertion. Our evaluation demonstrates that this approach not only integrates seamlessly into an MLIR-based quantum compiler collection but also surpasses previous non-MLIR solutions in both solution quality and runtime. The implementation is open-source and publicly available at https://github.com/munich-quantum-toolkit/core.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02620v1
- Title: Comparing the Performance of Leading VQE Algorithms for Computing Ground-State Energies of Amino Acids
- Authors: Sanskriti Shindadkar, Clyde Villacrusis, Jasper Andrews, Brandon Yan
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2607.02620v1  pdf=https://arxiv.org/pdf/2607.02620v1.pdf

Abstract:
Simulating molecules is a major application of quantum computing, with the potential to overcome exponential scaling constraints of classical computation. Researchers use different methods in order to evaluate the readiness of NISQ computers in order to test current simulation capabilities. We present an integrated repository with reproducible benchmarks of over 10 different ansatzes from published papers and two different truncation methods, applicable to any set of mapped hamiltonians, providing a single pipeline for comparing performance along multiple axes, including variance and computational time, among others. We apply them to simulate different amino acids, using hamiltonians taken from the QMProt Dataset. We then ran four separate experiments. First, we quantified noise resilience by optimizing the same hardware-efficient ansatzes under identical initialization while sweeping PennyLane noise channels and strengths, and measuring parameter drift, cosine similarity of optimal parameters, and energies evaluated on noiseless versus noisy backends. We then studied barren-plateau-related trainability via gradient-variance diagnostics and optimization trajectories across initialization strategies and ansatzes depth on small systems. We then compared adaptive versus fixed ansatzes at matched parameter budgets, reporting outer-loop iterations, wall time, and especially total cost-function evaluations to fairly contrast greedy adaptive growth with layered hardware-efficient circuits. Lastly, we mapped accuracy versus expressive capacity by sweeping the number of retained adaptive operators and recording ground-state energy error relative to classical references.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02622v1
- Title: COMET: Combinatorial Optimization for Multiplex Editing Targets Via Constraint-Preserving QAOA
- Authors: Priyansh Singhal, Sumit Maheshwari, Piyush Joshi
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2607.02622v1  pdf=https://arxiv.org/pdf/2607.02622v1.pdf

Abstract:
Multiplex CRISPR-Cas9 gene editing requires selecting one guide RNA per target gene subject to cross-gene interactions: a constrained combinatorial problem that can be formulated as a Quadratic Unconstrained Binary Optimization (QUBO) and solved via the Quantum Approximate Optimization Algorithm (QAOA). The one-hot per-gene constraint is conventionally enforced by adding quadratic penalty terms to the cost Hamiltonian, but penalty coefficient selection is heuristic and penalties amplify hardware noise. An alternative is to enforce the constraint structurally via the XY-mixer, which preserves feasibility by construction. We present COMET, a systematic comparison of penalty-based and XY-mixer QAOA on a three-gene, twelve-qubit multiplex editing instance targeting the immune-checkpoint genes PDCD1, LAG3, and HAVCR2. In simulation, the XY-mixer exceeds 95% probability of the optimum by QAOA depth p=3, while three penalty variants spanning an order of magnitude in penalty coefficient remain below 6% at every depth. On IBM's ibm_kingston (Heron r2) processor, the XY-mixer's simulator-hardware energy gap stays within |0.8| across all depths, while the worst-tuned penalty variant's gap reaches +53.9. We provide an honest account of where the structural guarantee partially breaks under gate-level noise. The twelve-qubit instance is classically trivial; our contribution is a methodological comparison of constraint-enforcement strategies in a biologically motivated domain, with real-hardware validation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02626v1
- Title: Krylov-Lie Algebras for Variational Quantum Algorithms: Geometric, Depth-Aware Insights into Expressivity and Trainability
- Authors: Anžej Margeta-Cacace
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.02626v1  pdf=https://arxiv.org/pdf/2607.02626v1.pdf

Abstract:
Variational quantum algorithms (VQAs) are a leading approach to near-term quantum computation, but their utility is limited by barren plateaus and other pathologies in their loss landscapes. Existing landscape theories based on dynamical Lie algebras, Jordan-algebraic Wishart systems, approximate t-designs, and Haar-random circuits are foundational, but they often neglect the finite-depth geometry of realistic ansätze and are therefore poorly suited to the shallow-depth regime, where VQAs are poor approximators of 2-designs and trainability is most feasible. This thesis introduces Krylov algebras, algebraic structures induced by the Krylov span of a finite generator set acting on one or more seed vectors, as a framework for VQA landscape theory. We show that VQA reachable manifolds can be approximated in a numerically robust, geometrically faithful way by Krylov-Lie algebras and groups, and that these structures induce canonical invariant measures for computing expectation values and variances under general sampling measures. In particular, we derive weighted non-Haar variance formulas that recover the usual Lie-algebraic Haar formulas as a special case while isolating non-Haar effects into explicit correction terms. We also show that the common heuristic that sufficiently deep circuit ensembles must converge to Haar fails in general without additional hypotheses, identify concrete obstructions to naive Haar convergence, and recover convergence under natural necessary and sufficient ergodic conditions. Lastly, our formulas further imply that non-Haar contributions may mitigate barren plateaus by reweighting the visible sectors of the loss landscape, suggesting that VQAs may be more trainable than recent literature has posited.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02652v1
- Title: Minimally invasive measurement of work in coherent quantum systems
- Authors: Cyril Elouard, Karen Hovhannisyan, Giulia Rubino
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02652v1  pdf=https://arxiv.org/pdf/2607.02652v1.pdf

Abstract:
A central challenge in quantum thermodynamics is to access work fluctuations in coherent processes without distorting the energetics of the unmeasured evolution. In standard two-point schemes, the initial energy measurement dephases coherent inputs, causing the measured average work to differ from that of the unmeasured evolution. Here, we develop an operational scheme for accessing work statistics for closed quantum systems based on the abstract notion of variation in the Heisenberg picture Hamiltonian. This scheme preserves energetically relevant coherences, thereby faithfully reproducing unmeasured work, while still producing positive probabilities. We derive modified Jarzynski and Crooks relations, as well as a thermodynamic uncertainty relation, identifying coherence-induced correction terms. Furthermore, we show that this scheme can reliably quantify the performance of a coherent engine in situations where the two-point energy measurement would suppress work output. In addition, the scheme requires only a single measurement and can predict the work associated with a subsequent unitary transformation. We exploit this feature to construct a Maxwell-demon protocol that can outperform energy-based feedback engines for coherent work extraction. Our results establish this scheme as a framework for accessing coherent work fluctuations without erasing the coherence that drives quantum thermodynamic performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02673v1
- Title: Quench Spectroscopy of Magnetic Excitations on a Superconducting Quantum Processor
- Authors: D. A. Millar, G. W. Pennington, N. T. M. Siow, S. Brandhofer, J. Crain, F. H. L. Essler, A. G. Green, S. J. Thomson
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2607.02673v1  pdf=https://arxiv.org/pdf/2607.02673v1.pdf

Abstract:
The elementary excitation spectrum of a many-body quantum system encodes many key properties, including phenomena as diverse as transport, thermalisation and ground state structure. Excitation spectra of strongly correlated systems are typically encoded in dynamical structure factors, which are demanding to measure experimentally and challenging to compute classically. Here we use quench spectroscopy on a superconducting quantum processor to extract excitation spectra of spin chains of $L=101$ spins. By tailoring the combination of quench protocol and observable, we selectively access distinct excitation sectors across several phases of the spin-$1/2$ XXZ chain, resolving free magnons, multi-magnon bound states, and two-spinon continua. Notably, we demonstrate that the protocol does not rely on ground state preparation: in the classically challenging gapless regime, we extract spectra directly from the quench dynamics of easily prepared product states, a procedure that is natural and straightforward on quantum hardware. Our work establishes quench spectroscopy as a fast and flexible probe of many-body excitation spectra on digital quantum hardware, introduces a novel quench protocol that does not require costly state preparation routines, and provides a scalable route towards regimes where classical simulation may become intractable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02696v1
- Title: Parametrized-circuit-free quantum regression with variance regularization
- Authors: Yerassyl Balkybek, Andrey Kardashin, Vladimir V. Palyulin, Konstantin Antipin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02696v1  pdf=https://arxiv.org/pdf/2607.02696v1.pdf

Abstract:
Quantum regression tasks for predicting properties of quantum states are commonly addressed using variational quantum algorithms. While variational quantum circuits are highly expressive and allow to achieve reasonable accuracy, training these circuits may demand a considerable amount of time and resources. In this work, we propose an approach of constructing problem-specific quantum regression models with encoding relevant symmetries and regularizing the variance. The proposed method is based on finding the coefficients of the linear combination of suitably chosen observables. Although it requires the knowledge of the symmetries of the problem in question, the method does not involve parameterized quantum circuits, and the training is done efficiently once the observables are measured. We demonstrate this method on two examples: Prediction of the transverse field strength in the Ising model, and quantification of entanglement in bipartite qubit systems. Our approach is accurate and less resource-intensive than conventional variational methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02736v1
- Title: Encoding matroids into quantum states
- Authors: Nathan Ferreira, Alison A. Silva, Giuliano G. La Guardia, Fabiano M. Andrade
- Categories: quant-ph (primary); quant-ph; math-ph; math.CO
- Links: abs=https://arxiv.org/abs/2607.02736v1  pdf=https://arxiv.org/pdf/2607.02736v1.pdf

Abstract:
Efficient representations of multipartite quantum states play a fundamental role in quantum information theory, providing both conceptual insight and practical tools for characterizing entanglement. Motivated by the axiomatic framework for graph states [Phys. Rev. A 85, 062313 (2012)] and its subsequent extension to hypergraph states [Phys. Rev. A 87, 022311 (2013)], we introduce an axiomatic construction of \emph{matroid states}, a new family of multipartite quantum states associated with matroids. Our constructions are based on a set of axioms analogous to those that define graph and hypergraph states, yielding a consistent quantum representation of arbitrary matroids. Two ways of constructing matroid states are proposed: the first is defined in terms of circuits, and the second in terms of independent sets. In both approaches, we establish the existence of universal global operators that satisfy desirable properties such as locality, symmetry, commutativity, and are associated with the combinatorial structure of matroids. Furthermore, we establish a hierarchy connecting graph, matroid, and hypergraph states within a unified framework. Additionally, we show how to obtain an arbitrary graph state by applying suitable families of matroid states, whose corresponding operators are the generators of the stabilizer subgroup of the graph state. These results identify matroid theory as a natural combinatorial language for the efficient description of multipartite quantum states and open new perspectives for the investigation of quantum entanglement and related combinatorial structures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02767v1
- Title: Self-Attention for Quantum Entanglement Prediction
- Authors: Anuj Gore, Roopayan Ghosh, Dylan Lewis, Sougato Bose
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02767v1  pdf=https://arxiv.org/pdf/2607.02767v1.pdf

Abstract:
Quantum entanglement is a powerful resource for quantum-enhanced technologies. However, its reliable quantification remains challenging due to the exponential scaling of the Hilbert space with system size, which renders full state tomography infeasible. Moreover, experimentally estimating entanglement typically requires a large number of measurement samples leading to a significant overhead. In this work, we present two models, a feed-forward neural network and an attention-based model, to accurately predict the bipartite second Renyi from projective measurements of quantum states. We benchmark their performance against standard classical shadow estimators and find that the machine-learning approaches achieve higher accuracy and improved sample efficiency across a range of system sizes. Our results demonstrate the potential of machine learning for scalable and efficient estimation of quantum correlations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02794v1
- Title: Reducing quantum measurements in qubit-based overlapping grouping methods for quantum energy estimation through better initializations
- Authors: Isaac L. Huidobro-Meezs, Rodrigo A. Vargas-Hernández
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02794v1  pdf=https://arxiv.org/pdf/2607.02794v1.pdf

Abstract:
The measurement cost for estimating expectation values of Hamiltonians is a central bottleneck in variational quantum algorithms. Grouping strategies significantly reduce this cost, with overlapping techniques being the state of the art in the field. Overlapping grouping methods require i) a non-overlapping grouping of the Hamiltonian, typically obtained from the Sorted Insertion (SI) algorithm as initialization, and ii) the construction of covariance dictionaries from approximate wavefunctions to guide the optimization. It was recently shown that different initializations can potentially reduce measurement costs for overlapping methods. Motivated by these findings, we introduce variance-aware SI (VarSI), a family of covariance-informed non-overlapping Pauli grouping heuristics to reduce measurement counts. VarSI grouping leverages the covariance dictionaries, already required by overlapping methods, to construct better non-overlapping groups. We propose three variants: a global greedy grouping insertion rule, a variance-informed SI analog, and a local refinement step initialized from SI or our variance-informed variant. We showcase the use of groupings generated by our VarSI heuristic algorithms to initialize overlapping methods using the iterative coefficient-splitting (ICS) algorithm. Molecular benchmarks with 130 Hamiltonians demonstrate consistent, non-overlapping measurement improvements over SI of 38\% and enhanced downstream ICS results when initialized from VarSI groups. We find that the initializations considered here achieve up to 70\% measurement reductions for ICS, compared to the standard SI initialization with mean reductions of 9--15.3\% depending on qubit mappings and covariance dictionaries used. These results show that non-overlapping grouping remains a consequential design step even when the final estimator uses overlapping fragments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02804v1
- Title: Fault-tolerant quantum computation with static atomic buses
- Authors: Matteo Bergonzoni, Laura Pecorari, Sam Norrell, Cody Poole, Guido Pupillo, Mark Saffman
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02804v1  pdf=https://arxiv.org/pdf/2607.02804v1.pdf

Abstract:
Efficient quantum error correction and fault-tolerant quantum computing require scalable, high-fidelity long-range connectivity. In neutral-atom quantum computers, this is commonly achieved through atom transport, but shuttling introduces latency and motional heating that worsen with system size. Here, we introduce a neutral-atom architecture based on static atomic buses, in which auxiliary mediator atoms enable long-range entangling operations without qubit transport. The architecture naturally supports long-range stabilizer measurements in high-rate LDPC codes and transversal logical gates between neighboring surface-code patches, enabling a modular framework for efficient logical memories, Clifford computation, and magic-state distillation. To realize these capabilities, we co-design optimal-control protocols for bus-mediated controlled-Z gates that incorporate both microscopic neutral-atom dynamics and architectural constraints. We obtain smooth bus-mediated gates with fidelities approaching 99.9% and durations of a few hundred nanoseconds by combining time-optimal control with interaction-flatness and robustness constraints. Large-scale simulations of quantum error correction and logical entangling operations between neighboring surface-code patches predict more than an order-of-magnitude improvement in logical error rates compared with atom-shuttling architectures under realistic noise. The architecture achieves logical gate times of approximately 100 us and quantum-error-correction cycle times of about 1 ms for code distances d<12. These results establish static atomic buses as a practical alternative to atom shuttling for scalable fault-tolerant neutral-atom quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02810v1
- Title: Locally Passive, Globally Charged Quantum Batteries: Coherence-Controlled Work and the Robustness of the Stored Charge
- Authors: Asad Ali, Saif Al-kuwari, James Q. Quach
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02810v1  pdf=https://arxiv.org/pdf/2607.02810v1.pdf

Abstract:
A solvable charger--battery model is introduced in which quantum coherence controls both where a quantum battery's charge is stored and how robustly it survives noise. Charging converts the charger's coherence into charger--battery entanglement and splits the deposited work between a locally extractable part and a correlation-locked part accessible only through joint operations; for a qubit, the split obeys an exact complementarity, and at maximal coherence, the battery is locally passive with the entire charge locked in correlations. Robustness follows local accessibility: the stored energy and locally extractable work are population-based, immune to pure dephasing, and limited only by relaxation, with an energy half-life, whereas the correlation-locked work is fragile to both dephasing and relaxation. Dephasing, global and local depolarization, and amplitude damping are treated through a single gain--loss competition algebra, and the resulting storage lifetimes are made concrete with superconducting-transmon parameters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02811v1
- Title: An approach for calculating astrophysical opacities on quantum computers
- Authors: Shivesh Pathak, Alina Kononov, Andrew D. Baczewski
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02811v1  pdf=https://arxiv.org/pdf/2607.02811v1.pdf

Abstract:
We propose a quantum algorithmic protocol for calculating astrophysical opacities. Our implementation uses first- and second-quantized representations of interacting electronic and photonic subsystems and Hamiltonian simulation via the interaction picture. Inferring opacity from momentum-resolved measurements of the photonic register yields a direct relationship between qubit count and spectral range/resolution. Logical resource estimates for the classically challenging problem of solar iron opacity are comparable to another high-energy-density physics problem (Rubin et al., PNAS 121(3) (2024)).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02858v1
- Title: Tunable M-Ary Quantum Secure Direct Communication via Correlation-Histogram Modulation
- Authors: Todd M. W. Hodges
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02858v1  pdf=https://arxiv.org/pdf/2607.02858v1.pdf

Abstract:
We propose a two-way entanglement-based quantum secure direct communication (QSDC) protocol in which information is encoded as the value of a continuously tunable parameter and decoded from empirically estimated joint-outcome histograms over windows of detected pairs. The protocol uses a fixed two-qubit polarization Hilbert space and only standard coincidence-based polarization measurement at the receiver, with the symbol alphabet enlarged not by increasing the carrier Hilbert-space dimension but by exploiting temporal integration over a window of pairs to resolve distinguishable joint-outcome probability distributions. Under an idealized model in which the source is maximally entangled, the encoding operation is strictly local, and the channel imprints no parameter-dependent signature on the traveling photon, the reduced state of the traveling photon is maximally mixed and independent of the encoded parameter. Consequently, passive interception of the in-flight subsystem alone yields no information about the encoded message. We further develop a quantitative trace-distance framework for bounding any parameter-dependent leakage that may arise from non-ideal channel and device effects in practical implementations. The protocol introduces protocol-level design parameters not available in fixed-alphabet two-way QSDC, specifically a runtime-tunable alphabet size and native support for continuous-time analog modulation, which may be advantageous in operating environments where channel conditions vary on protocol-relevant timescales.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02868v1
- Title: Photon Squeezing and Its Signatures of Quantum Phase Transitions in the Open Quantum Rabi-Stark Model
- Authors: Tian Ye, Xinghan Chen, Chen Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02868v1  pdf=https://arxiv.org/pdf/2607.02868v1.pdf

Abstract:
As a hallmark of nonclassical light, squeezed light is of profound theoretical interest and holds broad practical promise for emerging quantum technologies. In this work, we investigate steady-state optical quadrature squeezing in the open quantum Rabi-Stark model by employing the quantum dressed master equation. Both numerically and analytically, we find that positive (negative) Stark coupling tends to enhance (suppress) the squeezing effect. The quadrature squeezing exhibits distinct signatures associated with both first- and second-order quantum phase transitions (QPTs). Notably, a sharp vanishing of squeezing is observed across the first-order QPT, suggesting its potential as a sensitive probe of such transitions. In the vicinity of the second-order QPT, we further demonstrate that the squeezing factor displays finite-size scaling behavior, indicating a promising route toward the realization of near-perfect squeezing. Moreover, we establish a quantitative criterion for the disruption of quantum criticality induced by thermal fluctuations, which may offer valuable guidance for future experiments. These findings contribute to a deep understanding of nonclassical light in light-matter interacting systems and provide useful insights for the design of strong optical squeezing states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02888v1
- Title: Decision Kernels for Quantum Error Mitigation: Why Accuracy Gains Need Not Improve Downstream Decisions
- Authors: Vicenzo Scavino
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02888v1  pdf=https://arxiv.org/pdf/2607.02888v1.pdf

Abstract:
Quantum error mitigation (QEM) is usually benchmarked by expectation-value accuracy, but many near-term workflows use those values only to make downstream choices such as argmin selection, ranking, top-k filtering, optimizer-step acceptance, or phase labeling. This creates a structural mismatch: accuracy is measured in the ambient landscape space, whereas shift-invariant decisions depend only on gaps. We develop a quotient-space theory of finite-shot QEM for downstream decisions. The minimal decision-complete object is the residual gap law; in Gaussian finite-shot regimes it is summarized by effective margins and a decision kernel. The QEM-specific point is that this kernel is not free: it is the pullback of shared physical device noise through the mitigation map. We prove quotient factorization, gap-law minimality, a marginal no-go theorem, a QEM pullback theorem, Gaussian decision-risk formulas, and a fixed-allocation shot-level converse. Finite-shot Qiskit Aer simulations demonstrate the predicted divergence in the evaluated regimes. Clifford-data regression can be decision-flat while improving mean-squared error, and probabilistic error cancellation can improve accuracy while worsening decision risk through sampling overhead. Decision-aware selection modestly reduces static held-out failure relative to accuracy-based selection, often by retaining Raw, but the dynamic success target is not reached. Pre-registered stress tests under a calibrated device-noise model and on a hardware micro-cell probe robustness beyond these regimes. The operational implication in the evaluated regimes is to select QEM methods through residual gap geometry, not from expectation-value accuracy alone.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02906v1
- Title: Coherent Control of Three-Level System Using Shaped Free Electrons
- Authors: Dixuan Wu, Jing Li, Yuhan Jiang, Yunquan Liu
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2607.02906v1  pdf=https://arxiv.org/pdf/2607.02906v1.pdf

Abstract:
Three-level systems exhibit quantum interference effects absent in two-level systems, making them important for quantum optics. Here, we study the coherent interaction of a Lambda-type three-level system with free electrons shaped by optical near fields. By treating the electron train as a quantum drive, we show that the interplay between electron modulation and the three-level system's transition pathways induces tunable interference patterns. This interaction effectively realizes electron-mediated coherent population trapping (CPT). We identify a regime that enables complete population transfer between the two lower states and the preparation of a high-coherence superposition, manifested as dark states. In particular, these driven-dissipative steady states are independent of the initial state. Our work proposes shaped free electrons as a platform for steady-state coherent control of three-level systems, enabling atomic-scale state engineering.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02960v1
- Title: Full-Period Optical Phase Estimation with Heisenberg Scaling Using Displaced Squeezed States and Gaussian Measurements
- Authors: Marco A. Rodríguez-García, Luis Medina-Dozal, Francisco E. Becerra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02960v1  pdf=https://arxiv.org/pdf/2607.02960v1.pdf

Abstract:
We propose two-stage optimized strategies for full-period optical phase estimation with single-mode Gaussian states and Gaussian measurements under a fixed energy constraint. In the first stage (Stage I), displaced squeezed probes and heterodyne measurements provide coarse localization of the phase to a window on the circle. In the second stage (Stage II), squeezed-vacuum probes with adaptive homodyne measurements perform efficient phase estimation inside the selected window. We derive a generalized Cramér-Rao bound for this family of two-stage Gaussian strategies, which contains the contribution from local parameter estimation in Stage II plus an overshoot penalty from coarse localization errors in Stage I. For E <= 25 photons and squeezing limited to 12 dB, protocols using displaced squeezed states in Stage I reduce the optimized two-stage bound relative to protocols using coherent states in Stage I, and remain within a factor of 3 to 30 of the idealized local squeezed-vacuum quantum Cramér-Rao bound.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02962v1
- Title: Higher-order noise statistics restore Heisenberg scaling under collective dephasing
- Authors: Jiaxin Liu, Xing Heng, Zuoxian Wang, Danyue Ma
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02962v1  pdf=https://arxiv.org/pdf/2607.02962v1.pdf

Abstract:
Noisy-metrology theory characterizes decoherence by its two-point correlation function, equivalently the single-atom coherence time or noise spectrum. We show this is insufficient for entangled probes: two collective baths with identical single-atom $T_2$ but different higher-order statistics yield opposite entanglement-enhanced scaling. Under Gaussian Markovian collective dephasing a Greenberger--Horne--Zeilinger (GHZ) probe reaches an atom-number-independent sensitivity floor. For a fully Markovian compound-Poisson bath, in which collective dephasing is generated by a finite-rate sequence of unitary phase kicks, a Dicke coherence of order $q$ (a difference of $J_z$ eigenvalues) decays at $Γ_q=Γ[1-\mathrm{Re}\,\varphi(q)]$, with $\varphi$ the kick characteristic function; for any absolutely continuous kick law this rate saturates at large $q$ instead of growing as $q^2$, and a GHZ probe recovers Heisenberg scaling $δω\propto1/N$ over the window in which collective finite-rate noise dominates residual independent decoherence. We prove that the Gaussian floor is the exact worst case: at fixed single-atom coherence time every finite-rate kick statistics strictly beats it, and for arbitrary Lévy phase noise the asymptotic entangled-probe sensitivity is set exclusively by the diffusive component. A converse bound shows that no input state, ancilla, or measurement improves on the GHZ scaling. The mechanism is purely exponential and CP-divisible, distinct from the Zeno, non-Markovian, nonlinear-generator, and error-correction routes. A dissipative analogue caps the Dicke superradiant burst. The full counting statistics of common noise thus emerge as a control axis for noisy quantum metrology, beyond the spectrum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02984v1
- Title: Robust phase sensitivity in Mach-Zehnder interferometer using photon added and subtracted squeezed coherent state
- Authors: Shivani Singh, Priya Malpani, Anirban Pathak
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02984v1  pdf=https://arxiv.org/pdf/2607.02984v1.pdf

Abstract:
For the precision-based measurements, Mach-Zehnder interferometry is a widely used technique. There are various ways to enhance the precision of Mach-Zehnder interferometer (MZI), e.g., having a non-classical input state is one of the ways to enhance the precision of the phase estimation performed by MZI. The phase estimation performed by MZI is investigated here by considering that the input states of MZI are different combinations of photon added and subtracted squeezed coherent states (PASCS and PSSCS). Using quantum Fisher information, it is shown that the use of PASCS in both the input modes of MZI, provides the most precise estimate of the unknown phase. This system is also analyzed in two different measurement scenarios -- single intensity detection (SID) and intensity difference detection (IDD). Systematic analysis has established that the intensity measurement might not be an optimal measurement scheme for phase estimation in MZI as phase and intensity correspond to non-commuting observables. The impact of the photon loss on the MZI-based phase estimation setup is also studied and it is found that PASCS is robust against photon loss, when the loss in MZI is low.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02987v1
- Title: Time-dependent multiparameter estimation for quantum experiments via online-offline sequential Monte-Carlo method
- Authors: Chattamas Manoworakul, Jason F. Ralph, Nattaphong Wonglakhon, Areeya Chantasri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02987v1  pdf=https://arxiv.org/pdf/2607.02987v1.pdf

Abstract:
While typical online estimation methods can estimate the multiparameter dynamics of many systems, they may not be sufficient for a system with highly noisy measurement and rapid detection rate. In this paper, we create a hybrid estimation method by augmenting the sequential Monte Carlo (SMC) sampler, an online estimation method with an offline technique known as the time-batch estimation technique. By continuously monitoring the system, we may divide signals into batches and average them into an averaged trajectory. The system dynamics is then evolved with batch-averaged Kraus maps, for which we derive a highly efficient approximation. To facilitate the adoption of our algorithm, we present a modular derivation of the SMC methods and showcase our algorithm as an explicit example. We then implement our algorithm on the measurement signals obtained from superconducting-qubit experiments under two types of measurement setting: a fluorescence measurement and a dispersive $z$-measurement. The algorithm's hyperparameter values are chosen from independent numerical simulation, while the accuracy of our estimation is validated by a signal reconstruction method. Our results show that, for the fluorescence case, our algorithm can estimate the system's parameters better than the standard calibration method, and, for the dispersive case, our estimation is capable of finding an unexpected jump in parameter values that the standard calibration method could not find.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02989v1
- Title: Error-tolerant secure key leasing for quantum decryption keys in public-key encryption
- Authors: Duo Xu, Yuki Takeuchi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02989v1  pdf=https://arxiv.org/pdf/2607.02989v1.pdf

Abstract:
We propose the first error-tolerant secure key leasing (SKL) for public-key encryption. As with SKL in prior works, our protocol consists of a lessor and lessee. In the protocol, the lessor encodes its secret key into quantum states and leases the key to the lessee. Then, the lessor can ask the lessee to return the secret key at a later point. The lessor is able to check whether the lessee has returned its key honestly. However, our protocol works even when the leased secret key is subject to noise. The lessee decrypts the ciphertext correctly, and the lessor verifies the return of the secret key correctly when the amount of error is below a certain threshold. Our improved protocol does not change the encoding of the secret key, and thus adds no overhead to the quantum information processing. Our most significant result is a framework to analyze the trade-off between robustness against error and security. We bridge the security of the error-tolerant SKL and that of the error-tolerant certified deletion with shortened codes, which is a relatively less explored concept in coding theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02997v1
- Title: Symmetry-Resolved Parent Hamiltonians for Entangled Bosonic Cat Resources
- Authors: Šimon Bräuer, Klaus Mølmer
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.02997v1  pdf=https://arxiv.org/pdf/2607.02997v1.pdf

Abstract:
We derive parent Hamiltonians in terms of oscillator operators for multimode bosonic cat resource states. The construction separates a universal branch Hamiltonian, which confines each mode to the coherent-state support $ |\pmα\rangle$, and state-dependent constraint Hamiltonians, which select the desired correlations and symmetry sectors inside the resulting branch manifold. This framework progressively removes degeneracies in the low-energy manifold and yields explicit parent Hamiltonians for GHZ-, cluster-, and W-type cat states. In the large-$|α|$ limit, the bosonic parent Hamiltonians reduce to stabilizer or exchange Hamiltonians acting on an effective logical-qubit basis. The present construction provides a direct bridge between coherent-state bosonic engineering and stabilizer-based quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03002v1
- Title: Fringe field induced spin-OAM mixing of twisted electrons
- Authors: S. V. Gatalina, S. S. Baturin
- Categories: quant-ph (primary); quant-ph; physics.acc-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2607.03002v1  pdf=https://arxiv.org/pdf/2607.03002v1.pdf

Abstract:
We study spin effects in twisted-electron propagation through the entrance or exit region of an axially symmetric magnetic coil. Starting from the Foldy-Wouthuysen reduction of the Dirac equation, we derive a paraxial spinor equation in which the longitudinally varying solenoidal field produces, in addition to the usual diagonal Zeeman term, a transverse Pauli coupling proportional to the fringe-field gradient. The scalar transverse dynamics is treated exactly by the Ermakov mapping, which absorbs the longitudinally dependent focusing into a metaplectic scaling transformation and reduces the orbital evolution to that of a stationary two-dimensional oscillator. On this background, the transverse Pauli term is treated perturbatively and yields an explicit first-order correction for arbitrary realistic solenoidal profiles. Axial symmetry implies conservation of the total projection of angular momentum, so each spin flip is accompanied by a compensating one-quantum change of orbital angular momentum. In addition, the linear coordinate structure of the perturbation restricts the first-order dynamics to at most two neighboring radial sidebands for each incoming oscillator component. We derive the corresponding transition amplitudes and show how their phases are governed jointly by the Ermakov accumulation and the diagonal spin-orbital rotation. The resulting framework provides a direct way to quantify spin-orbit mixing of twisted electrons in realistic magnetic lenses and solenoidal beam-line elements, and it identifies a route toward controlled spin-OAM conversion in engineered sequences of magnetic-field edges.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03052v1
- Title: Single-acquisition tomography of photonic qubits with structured media
- Authors: Francesco Di Colandrea, Yingwen Zhang, John Grace, Dilip Paneru, Alessio D'Errico, Ebrahim Karimi
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2607.03052v1  pdf=https://arxiv.org/pdf/2607.03052v1.pdf

Abstract:
Quantum state tomography is an essential tool for characterizing quantum systems and underpins nearly every experimental realization of quantum technologies. Conventional tomography relies on performing a sequence of projective measurements on many identical copies of a quantum state, requiring the measurement apparatus to be reconfigured between successive acquisitions. As the Hilbert-space dimension increases, the number of required measurements grows rapidly; in practice, additional overcomplete measurements are often performed to improve robustness to experimental imperfections. Here, we introduce a tomography platform based on structured anisotropic media that performs informationally complete measurements of photonic polarization qubits within a single acquisition. The approach employs three liquid-crystal metasurfaces with spatially varying optic-axis orientations that transform the input polarization into a far-field distribution of discrete transverse-momentum modes. Each diffraction pattern uniquely determines the polarization state, enabling its reconstruction without sequential changes to the measurement apparatus. Unlike previous implementations, our scheme is intrinsically photon-number independent: the same optical device operates identically for arbitrary photon numbers, while the desired photon-number sector can be selected afterwards through post-selection of the corresponding $n$-fold coincidence events. We experimentally demonstrate single-frame quantum state tomography of both single- and two-photon polarization states, providing a simple and scalable route toward efficient quantum-state characterization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03105v1
- Title: ORBIT-Q: Dual-axis benchmarking of autonomous agents in scientific quantum programming
- Authors: Shi-Xin Zhang, Yu-Qin Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03105v1  pdf=https://arxiv.org/pdf/2607.03105v1.pdf

Abstract:
Autonomous coding agents perform well on many conventional programming tasks, but scientific computing demands a rigorous validation paradigm that extends beyond simple functional test completion: generated code must preserve physical fidelity, differentiable workflows, framework-native semantics, and scalable representations. We introduce Open Research Benchmark for Integrated Tasks in Quantum Computing (ORBIT-Q) to address this gap. At its core, ORBIT-Q contributes a carefully curated suite of complex, research-level quantum workflows that serves as a challenging testbed for modern scientific programming. ORBIT-Q combines a rigorous multi-tier verification pipeline to support two orthogonal comparisons: different agent harness and model configurations at a fixed quantum software framework, and different quantum software frameworks at a fixed agent. In our systematic evaluations, TensorCircuit-NG (TC) exhibits the highest capability and performance efficiency among the evaluated quantum software frameworks under agent-driven programming, and Codex with GPT-5.5 is the strongest tested agent configuration on TC. However, a significant performance and design gap remains between frontier autonomous agents and human expert reference implementations. We further evaluate two efficiency dimensions: agent-side resource use and artifact-side runtime. Together, these results establish ORBIT-Q as a rigorous benchmark for autonomous scientific programming, framework-agent synergy, and quantum software performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03164v1
- Title: Geometric modulation of transition and survival intensities in non-Hermitian systems
- Authors: Ryu Frieson, Takashi Oka, Hideaki Obuse
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.optics
- Links: abs=https://arxiv.org/abs/2607.03164v1  pdf=https://arxiv.org/pdf/2607.03164v1.pdf

Abstract:
The time evolution of non-Hermitian systems is generally nonunitary. Dynamics governed by time-dependent non-Hermitian Hamiltonians lead to a variety of novel phenomena, one of which is state amplification or suppression induced by the complex Berry phase. Here, we extend the framework of geometric modulation to multi-level systems and show that both transition and survival intensities can be modulated. We apply our theory to the non-Hermitian Landau-Zener (LZ) problem. First, we show that, in the half-LZ problem, both the transition and survival probabilities exhibit nonreciprocity due to the complex Berry phase. In the non-Hermitian standard LZ problem, only the survival intensity is known to exhibit nonreciprocity, whereas the transition intensity does not. However, the physical origin of this nonreciprocal behavior remains unclear. In this work, we show that the nonreciprocity originates from the complex Berry phase.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03187v1
- Title: Quantum Kolmogorov--Arnold representation theorem for continuous unitary-valued maps
- Authors: Sviatoslav V. Dzhenzher
- Categories: quant-ph (primary); quant-ph; cs.LG; math.FA
- Links: abs=https://arxiv.org/abs/2607.03187v1  pdf=https://arxiv.org/pdf/2607.03187v1.pdf

Abstract:
The classical Kolmogorov--Arnold representation theorem states that any continuous multivariate function can be exactly decomposed into a finite composition of univariate continuous functions and addition operations.   This foundational result has recently inspired the development of Kolmogorov--Arnold Networks (KANs) in classical machine learning, as well as their extensions into the quantum domain (QKANs). In this paper, we establish two quantum analogues of the Kolmogorov--Arnold representation theorem for continuous unitary-valued maps of several variables within an open $1$-neighbourhood of the identity matrix \(O_1(\mathbf{I}) \subset \mathcal{U}(n)\).   First, we prove a representation theorem that yields an exact additive decomposition inside the matrix exponent of anti-Hermitian-valued maps.   Second, due to the non-commutative nature of quantum operators, we derive a factorised version expressing the target unitary map as a finite sequential product of univariate matrix exponentials. Finally, we provide a concrete topological counterexample based on the lifting property of \(\mathcal{SU}(2)\) to demonstrate that these local representation theorems cannot be globally extended to the entire unitary group \(\mathcal{U}(n)\) without encountering fundamental structural obstructions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03193v1
- Title: Self-Specializing Vision-Language Transmon Chip Calibration in a Physics-Grounded Environment
- Authors: Animesh Tripathy, Aswanth Krishnan
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.LG
- Links: abs=https://arxiv.org/abs/2607.03193v1  pdf=https://arxiv.org/pdf/2607.03193v1.pdf

Abstract:
Calibrating a superconducting transmon chip is a sequential decision problem under noise, drift, and a finite budget: an expert must choose experiments, read ambiguous plots, judge fit quality, and revise stale beliefs as the chip drifts. We study whether a vision-language agent can close this loop and specialize itself to one physical device without weight updates, via three co-designed artifacts. The first is a physics-grounded simulation environment for transmon chips: calibration observables derive from circuit-quantized parameters via scqubits, with realistic flux-line distortion, wall-time-scaled and mid-scan drift, and gate leakage, concerns a toy simulator would omit; each tool call advances a modeled clock so drift accrues by wall time, not call count. The second is a vision-language agent that runs the loop end to end, calling tools, reading plots, maintaining a structured notebook, and submitting parameters without hidden truth, scored against hidden parameters and gate fidelities measured on the device. The third is gradient-free online adaptation: a reflector reads truth-free anomaly signatures from past attempts and grows a small, human-readable device note appended to the prompt, admitted by a paired-snapshot accept gate that isolates strategy improvement from drift. On a hard-tier chip under budget pressure, six iterations raised the worst-case CZ fidelity from 0.678 to 0.787 and cut its variance, reproducing at four-qubit scale; a single accepted note raised CZ fidelity from 0.678 to 0.913 on its paired snapshot. A planted-fault study confirms the note is causal, diagnosing a hardware fault truth-free, its principal value raising the failure floor and cutting variance. The agent, scoring, and reward transfer to real hardware via a measurement-backend swap; only the accept gate is a simulation affordance, reducing to a held-out-slice or repeat-and-average form.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03202v1
- Title: Broadband Characterization of Polarization Mode Dispersion for Quantum Communication Channels
- Authors: Vadim Rodimin, Konstantin Kravtsov, Rui Ming Chua, Xingjian Zhang, Aleksei Ponasenko, Yury Kurochkin, Alexander Ling, James A. Grieve
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2607.03202v1  pdf=https://arxiv.org/pdf/2607.03202v1.pdf

Abstract:
We present a method for characterizing polarization fiber channels carrying broadband quantum signals, where narrowband filtering would waste photon flux. Wavelength-dependent polarization mode dispersion (PMD) maps each input state to a trajectory on the Poincaré sphere; we show that the singular value decomposition of the band-averaged rotation matrix yields, in closed form, the optimal input states, the mutually unbiased measurement bases, and their infidelities. The three singular values provide a compact, bandwidth-dependent channel signature that separates first- from higher-order PMD, and the resulting 5%-infidelity bandwidth gives a practical filtering budget. We characterize deployed fiber links in Masdar City and demonstrate PMD mitigation by concatenating two channels through a single polarization controller.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03218v1
- Title: Quantum Annealing for Dynamic Portfolio Optimization under Realistic Transaction Costs
- Authors: Escolástico Sánchez-Martínez, Senaida Hernandez Santana, Ventura Sarasa Laborda, Pablo Serrano Molinero, Guillermo Botella Juan, Alberto del Barrio García
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03218v1  pdf=https://arxiv.org/pdf/2607.03218v1.pdf

Abstract:
This paper investigates and compares quantum and classical investment strategies for portfolio construction under realistic trading and allocation constraints. The study considers a multi-period portfolio re-balancing setting in which asset weights are subject to lower and upper bounds, class-level exposure restrictions, and turnover limitations. On the quantum side, the portfolio selection problem is reformulated as a quadratic unconstrained binary optimization (QUBO) model through a finite binary encoding of asset weights, and subsequently embedded into a constrained quadratic model (CQM) solved by a hybrid quantum-classical optimization workflow. On the classical side, benchmark allocation strategies are introduced to provide an economically meaningful reference for performance assessment. The proposed framework jointly evaluates portfolio efficiency from two complementary perspectives: business performance, measured through return, volatility, and a measure of the trade-off between them, the Sharpe ratio; and computational performance, assessed through solver structure, constraint handling, and hardware execution characteristics. The resulting comparison provides a rigorous basis for understanding the practical role of quantum annealing in constrained portfolio optimization, while clarifying both its modeling advantages and its current implementation limitations relative to established classical approaches.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03235v1
- Title: A Galton-Watson estimate for Dyson series
- Authors: Hans Maassen, Dmitri Botvich
- Categories: quant-ph (primary); quant-ph; math.PR
- Links: abs=https://arxiv.org/abs/2607.03235v1  pdf=https://arxiv.org/pdf/2607.03235v1.pdf

Abstract:
We consider the question of convergence of particular series of integrals, which are labeled by rooted trees. Necessary and sufficient criteria for convergence are obtained, together with an explicit expression for the sum. The technique used is strongly reminiscent of the generating function approach of Galton and Watson to branching processes. The interest in these series derives from the Dyson series expansion for the perturbation of a free quantum dynamics by a local potential: the convergence of the series imlies that the perturbed dynamics exists and is unitarily equivalent with the free one.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03250v1
- Title: Generating one-way computations with flow: flow-preserving rewriting that ignores the interpretation
- Authors: Miriam Backens
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03250v1  pdf=https://arxiv.org/pdf/2607.03250v1.pdf

Abstract:
The one-way model is a universal model of quantum computation, driven by successive adaptive single-qubit measurements on an entangled resource state. Measurements are non-deterministic, yet if the computation satisfies one of several related families of conditions known as 'flows', the computation can be made deterministic overall by modifying later measurements depending on the outcomes of earlier ones. Flow properties also enable efficient translation from one-way computations to circuits, motivating research into rewriting one-way computations while preserving the existence of flow. Existing approaches to flow-preserving rewriting are used for compilation or optimisation and preserve both the interpretation and the existence of flow.   Here, we broaden our perspective to consider flow-preserving rewriting that does not necessarily preserve the interpretation, with applications to creating test instances for software that works with flow, as well as to generating ansätze for quantum machine learning. We show that a family of just three flow-preserving rewrite rules suffices to generate any diagram with flow from a trivial diagram with the desired number of inputs and outputs. This rule set is nearly the same as the complete set of flow- and interpretation-preserving rewrite rules for one-way computations in which all measurements are Pauli; and just a small subset of the flow- and interpretation-preserving rewrite rules for arbitrary measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03274v1
- Title: False vacuum decay in long-range interacting quantum systems
- Authors: Valerio Pagni, Laura Batini, Nicolò Defenu
- Categories: quant-ph (primary); quant-ph; gr-qc; hep-th
- Links: abs=https://arxiv.org/abs/2607.03274v1  pdf=https://arxiv.org/pdf/2607.03274v1.pdf

Abstract:
We formulate false-vacuum decay in a mixed-field Ising chain with $1/r^α$ interactions as a spatially nonlocal Euclidean $φ^4$ theory featuring a fractional spatial kinetic term $\sim |q|^σ$, where $σ=α-1$. The nonlocal bounce is anisotropic in space-time and develops algebraic spatial tails, challenging the standard thin-wall picture of a compact droplet. Combining thin-wall arguments with numerical solutions of the full nonlocal saddle, we show that these tails preserve the leading thin-wall exponents, manifesting instead in subleading corrections. For $0<σ<1$, the lifetime exponent scales with the energy bias $h$ of the metastable state as $B\sim h^{-1/σ}$; for $1<σ<2$, the leading Coleman scaling $B\sim h^{-1}$ is recovered, while long-range effects are retained in the subdominant term $\sim h^{σ-2}$. Our results show that tunable long-range interactions fundamentally reshape bubble nucleation and alter false-vacuum decay in quantum simulators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03275v1
- Title: Comparing and learning figures of merit for quantum circuit compilation
- Authors: Harshdeep Singh, Marvin Richter, Mats Granath, Anton Frisk Kockum
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03275v1  pdf=https://arxiv.org/pdf/2607.03275v1.pdf

Abstract:
To make quantum algorithms executable on a particular quantum device, they need to be compiled into circuits that respect constraints of the quantum hardware. This compilation usually involves multiple steps, where many hardware-compatible circuits are generated, and the best circuit is selected. To say which circuit is best, the quality of a circuit is generally quantified by a $\textit{figure of merit}$ (FoM). For FoMs, there is a trade-off between ease of calculation and accuracy in predicted execution quality. Commonly used FoMs, e.g., the number of gates, circuit depth, etc., are easy to evaluate, but do not directly capture the effects of circuit structure and noise. On the other end of the spectrum are FoMs that require full circuit execution and take a prohibitively long time to evaluate. One example is the probability of successful trials (PST), i.e., the probability of obtaining the initial state after running the quantum circuit followed by its inverse. Here, we investigate advantages and disadvantages of different FoMs, and formulate the properties of an ideal FoM. Based on our results, we propose wPST, a weighted version of the PST that accounts for individual qubits, not just the whole state. To quickly predict PST and wPST, we design machine learning models that take into account both the quantum circuit and quantum hardware data. In numerical simulations and experiments on quantum processors, we find that our machine learning-predicted FoMs outperform commonly used FoMs, increasing the correlation with the true PST or wPST by over 50%. To make our model useful for quantum compilers, we devise a two-step process to predict the wPST for non-transpiled quantum circuits: first, we predict the additional quantum gates required for the given quantum circuit, and then we predict the wPST, accounting for coherence times in the quantum device.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03278v1
- Title: Complexity of Normalized Persistence Problems for Topological Data Analysis and Local Hamiltonians
- Authors: Dominic Lowe, M. S. Kim, Roberto Bondesan, Ryu Hayakawa
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.LG
- Links: abs=https://arxiv.org/abs/2607.03278v1  pdf=https://arxiv.org/pdf/2607.03278v1.pdf

Abstract:
Topological data analysis (TDA) is a machine learning technique that uses topology to extract patterns from data and has shown the potential to exhibit quantum advantage. A key concept in TDA is persistent homology, which measures the robustness of topological information at different lengthscales. In this paper, we introduce and study the problem of normalized persistence, a practically motivated and easily interpretable version of persistent homology that counts the fraction of holes that persist at different lengthscales. We prove that a variant of normalized persistence is $\mathsf{DQC}_1$-hard and contained in $\mathsf{BQP}$, giving evidence of an exponential quantum speedup for TDA under the standard assumption that $\mathsf{DQC}_1 \not\subseteq \mathsf{BPP}$. These are the first $\mathsf{DQC}_1$-hardness results that are directly applicable to TDA instances. We also find a close connection between normalized persistence and the complexity of estimating spectral quantities in the low-energy subspace of local Hamiltonians. We study a family of such problems, including a low-energy normalized subtrace and spectral density. We show that these are $\mathsf{DQC}_1$-hard for $O(1)$-local Hamiltonians, strengthening previous results that required log-local interactions. We also introduce a variant of $\mathsf{DQC}_1$ with perfect completeness ($\mathsf{SDQC}_1$) to characterize the hardness of problems normalized by an exact kernel. This includes normalized persistence for $O(1)$-local Hamiltonians, which we show is $\mathsf{SDQC}_1$-hard.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03295v1
- Title: Quantum Probability and Quantum Information Theory
- Authors: Hans Maassen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03295v1  pdf=https://arxiv.org/pdf/2607.03295v1.pdf

Abstract:
This is an introductory course on quantum probability and quantum information, based on matrix algebras.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03302v1
- Title: Dissipative preparation and stabilization of d-mode multinomial cat states
- Authors: S. Zhao, A. Metelmann
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2607.03302v1  pdf=https://arxiv.org/pdf/2607.03302v1.pdf

Abstract:
Engineering dissipation with tailored steady states has become a powerful approach for preparing and stabilizing quantum states. In this framework, engineered dissipative processes continuously steer a system towards desired target states while suppressing unwanted noise. However, extending this idea to multimode systems is challenging and remains largely unexplored, although this class of states is a powerful resource for quantum sensing and quantum information processing applications. Here, we propose a general method to design the required dissipative processes for the generation of multimode cat states in bosonic systems. We show that the engineered dissipation prepares such states from the vacuum with high fidelity and robustly stabilizes them against decoherence. As a result, their lifetime is extended by several orders of magnitude compared to natural decay times, which in turn enhances their applications in quantum techonologies. We specifically focus on the preparation and stabilization of two-mode binomial cat states and discuss a pathway for the implementation in superconducting circuit. However, our scheme can also scale up to arbitrary d-mode multinomial cat states associated to $\mathfrak{su}(d\ge2)$ algebras, and thus, our scalable framework provides a feasible route towards stabilizing compact nonclassical states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03313v1
- Title: High Success Probability, Fidelity, and Purity Nonlinear Optical Two-Qubit Gates on Chip
- Authors: Minghao Shang, Hua-Ying Liu, Ying Wei, Xiaoyi Liu, Qianhao Ning, Lijian Zhang, Shi-Ning Zhu, Zhenda Xie
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2607.03313v1  pdf=https://arxiv.org/pdf/2607.03313v1.pdf

Abstract:
Optical two-qubit gate with high success probability, fault-tolerant fidelity, and high-purity outputs is a fundamental yet unsolved challenge, essential for large-scale optical quantum computing toward quantum advantage. Here, we propose a feasible scheme for such gate using thin-film lithium niobate platform, enabling \c{hi}(2) nonlinear photon-photon interaction with 100% efficiency. By decoupling photon interaction and qubit flip operations, fidelity ceiling is removed, and output state purity is recovered by spectral-phase pre-compensation based on a full-spectral photon interaction model, yielding a CNOT gate with 84% success probability, 93% purity, and unity fidelity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03337v1
- Title: An End-to-End Multi-Stage Kill-Chain Attack on Quantum Neural Networks: Demonstration on Trapped-Ion Hardware
- Authors: Cedric Brügmann, Daniel Herr, Daniel Ohl de Mello, Pascal Debus, Maximilian Wendlinger, Kilian Tscharke, Juris Ulmanis, Alexander Erhard, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03337v1  pdf=https://arxiv.org/pdf/2607.03337v1.pdf

Abstract:
We demonstrate an end-to-end, multi-stage attack against a quantum neural network (QNN) model that is executed on a trapped-ion quantum computer. Our chain combines side-channel reconnaissance, crosstalk characterization, adversarial example generation, and a physical crosstalk attack that realizes the adversarial perturbation on the device. We cover the full attack chain on ion traps and report the corresponding superconducting-hardware experiments in the appendix. We discuss implications for QaaS providers and hardware mitigations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03340v1
- Title: Measurements Number Scaling in the Quantum Approximate Optimization Algorithm for MaxCut: A Statistical Analysis
- Authors: Inbar Chefer, Uri Shaham, Adi Makmal
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03340v1  pdf=https://arxiv.org/pdf/2607.03340v1.pdf

Abstract:
We provide a statistical analysis of the measurement (shot) requirements of the quantum approximate optimization algorithm (QAOA) for the MaxCut problem. We derive sufficient conditions on the number of shots per cost operator evaluation to: (a) estimate the expected cost to within a relative error $δ$ and a confidence $1-ε$, and (b) ensure SGD-based parameter optimization converges to a target relative suboptimality level with high probability. In addition, we provide an explicit bound on the number of SGD iterations required to reach the target accuracy. Our analysis reveals an unexpected scaling phenomenon: for specific graph classes, which we formally characterize, the total shot budget needed to achieve a fixed relative-performance metric decreases as the instance size grows. This result complements earlier cost function concentration arguments regarding parameter optimization redundancy, thereby highlighting the potential for high-performance, low-overhead QAOA implementations for large-scale MaxCut instances. To assist practitioners, we translate our analytical findings into practical rules of thumb for shot-budget allocation and validate these results with numerical simulations, offering new insights into the interplay between graph size, structural complexity, and resource requirements in QAOA.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03361v1
- Title: Nested-Loop Trajectory-Informed Variational Quantum Solver for Interior-Point OPF
- Authors: Farshad Amani, Amin Kargarian
- Categories: quant-ph (primary); quant-ph; eess.SY; math.OC
- Links: abs=https://arxiv.org/abs/2607.03361v1  pdf=https://arxiv.org/pdf/2607.03361v1.pdf

Abstract:
Optimal power flow (OPF) solved by an interior-point method (IPM) requires repeatedly solving Newton linear systems. When variational quantum linear solvers (VQLS) are used, each IPM iteration involves an additional nested inner variational optimization loop, which can significantly slow the overall quantum-assisted IPM convergence. To address this challenge, this paper proposes a dual-level trainable quantum IPM framework for OPF that leverages early solver-generated trajectories rather than relying on single-point prediction. The key observation is that early IPM iterates provide informative primal-dual, slack, and barrier-variable evolution about the path to optimality, while early VQLS parameter updates provide useful information about the later variational search. At the quantum-solver level, a trainable parameter model uses a short prefix of the VQLS parameter trajectory to project the remaining variational search toward a lower-cost region. At the OPF-solver level, a second trainable model uses early primal-dual IPM iterates to project a later central path state, which is restored to an admissible point before IPM refinement continues. Simulation studies show that the proposed approach reduces the number of variational updates by up to $95\%$ while maintaining OPF objective values close to the classical IPM reference. A 2-bus demonstration on real quantum hardware is also included to validate the implementation of the proposed workflow.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03409v1
- Title: Symmetry-Protected Quantum Synchronization in Squeezed-Bath-Engineered Superradiance
- Authors: Juan David Álvarez-Cuartas, Joakim Bergli, John H. Reina
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03409v1  pdf=https://arxiv.org/pdf/2607.03409v1.pdf

Abstract:
A squeezed dissipative bath converts the coupling phase of a bipartite unconventional Dicke model into a control parameter that suppresses both static superradiant thresholds, opening a window where only a Hopf instability survives and the two spin ensembles synchronize completely via the shared cavity mode. The squeezed bath preserves a $\mathbb{Z}_2$ parity symmetry, so conventional broken-symmetry diagnostics vanish identically. We certify the synchronized state instead through parity-even, information-theoretic witnesses: a 30\% photon-number suppression, a Husimi-$Q$ lobe-count change, a 64\% suppression of spin--spin mutual information, and a robust discord-to-mutual-information ratio $D/I = 0.50 \pm 0.05$, confirmed by full quantum master-equation simulations. These results establish parity-even witnesses as a general, entanglement-free route to certifying quantum synchronization in symmetry-protected driven-dissipative systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03417v1
- Title: Specifying the operational meaning of quantum reference frames
- Authors: Augustin Vanrietvelde
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03417v1  pdf=https://arxiv.org/pdf/2607.03417v1.pdf

Abstract:
In their strongest usage, quantum reference frames have been described as referring to "the measurements performed by a superposed lab", "the perspective of a quantum particle", "the point of view of a superposed observer", etc. While exciting, these operational proposals have remained brief and ambiguous, leading to misinterpretations and criticism. Here, we provide a detailed specification and defense of the notion of a position-superposed lab or observer. We argue that this requires no exotic claims about quantum physics and raises no greater interpretive difficulty than ordinary quantum measurements. We then derive several consequences of taking this operational meaning seriously. We stress that the position-superposed observers that define quantum references frames are different from, and considerably less problematic than, the outcome-superposed observers considered in Wigners' friend scenarios. In particular, we show that outcomes obtained by a position-superposed observer may (without decohering the superposition) be broadcast to a well-localised one, in contrast with Wigner's friend scenarios, which require the outcomes to remain internal to the system at hand. Finally, we defend the possibility to roleplay a quantum reference frame from a classical reference frame.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03429v1
- Title: Matter-Field Exchange Generates Entanglement, Not Classical Gravity
- Authors: Nicetu Tibau Vidal, Aditya Varna Iyer
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2607.03429v1  pdf=https://arxiv.org/pdf/2607.03429v1.pdf

Abstract:
Aziz and Howl have argued that a hybrid theory with quantum matter and a classical gravitational field can generate entanglement between two massive systems. In their construction, the branch-dependent contribution appears at fourth order through propagators of the quantum matter field in a fixed classical gravitational potential. We analyse this mechanism within the same perturbative QFT framework and show that the effect should not be interpreted as classical gravity mediating entanglement in the sense relevant to BMV-type witnesses. The non-separable term relies on a quantum-matter exchange channel between the two interferometers and is present only when the two systems are modelled as excitations of the same matter field. If distinct, non-interconverting matter fields describe the systems, the corresponding cross-propagator is absent and the Aziz-Howl entangling diagram vanishes. The effect relies on coherent propagation amplitudes of the quantum matter field between the two interferometers, together with postselection onto the original localised branch subspace. Moreover, the inference of entanglement is made after projecting the full QFT evolution onto a restricted final subspace containing the original localised $N$-particle branch states. This projection removes precisely the sectors that would record matter-field contamination, mode deformation, or exchange between the two interferometers. We therefore argue that the Aziz-Howl mechanism is a matter-sector cross-talk effect in a classical background, not entanglement mediated by classical gravitational degrees of freedom. Having identified the channel responsible for the Aziz-Howl contribution, we predict that it can be eliminated by using distinct, non-interconverting matter species in the two interferometers, or by inserting a barrier that suppresses matter-field propagation between them.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03437v1
- Title: Design of an Electrically Tunable Microtoroid for Frequency Selection of Polarization-Entangled Photons
- Authors: Yichi Zhang, Enqi Ke, Judith Su
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2607.03437v1  pdf=https://arxiv.org/pdf/2607.03437v1.pdf

Abstract:
Encoding quantum information into discrete optical frequencies, or "frequency bins," uses different colors of light as additional information channels, allowing each photon to carry more information than polarization alone. We present a computational design for an electrically tunable silica microtoroid that selects desired frequency channels after a polarization-entangled photon pair has been generated without disturbing the photons' polarization entanglement. In the proposed architecture, the 750 nm signal photon passes through the microtoroid, while its entangled 880 nm partner bypasses the resonator and serves as a reference for the selected frequency channel. The principal challenge is resonator birefringence: because horizontally and vertically polarized light resonate at slightly different frequencies, the selected frequency can reveal the photon's polarization state and weaken the quantum correlation between the photon pair. We solve this problem by adding a small lithium-niobate tuning element controlled with a single applied voltage. The voltage shifts the resonator so that it responds almost identically to horizontally and vertically polarized light, reducing the remaining mismatch to only 0.286 optical linewidths across nine frequency channels. The photons remain strongly entangled after passing through the device, with a concurrence of C = 0.969, a Bell-state fidelity of F = 0.981, and a Bell parameter of S_max = 2.785. If the relative timing between the frequency channels is also controlled, the same device can generate a nine-channel polarization-frequency hyperentangled state with an effective dimension of K = 8.97. This computational design provides a compact, electrically tunable bridge between polarization-entangled photon sources and future high-capacity quantum photonic systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03438v1
- Title: Dynamical zero modes, boundary dependence, and numerical instability in dynamical quantum phase transitions
- Authors: Siyan Lin, Xu Feng, Xiuhua Tian, Shu Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03438v1  pdf=https://arxiv.org/pdf/2607.03438v1.pdf

Abstract:
Boundary conditions are usually expected to cause only finite-size corrections to bulk quantities, but this expectation can fail for dynamical quantum phase transitions. In this work, we show that such boundary dependence is encoded in dynamical zero modes (DZMs) of the Loschmidt matrix, which are defined as singular vectors whose singular values vanish in the thermodynamic limit. Using the Su-Schrieffer-Heeger (SSH) and extended SSH models as examples, we find that the time interval where the Loschmidt rate functions (LRFs) under periodic and open boundary conditions differ coincides with the emergence of DZMs in the open-boundary Loschmidt matrix. These modes carry the boundary-dependent contribution: removing them from the open-boundary LRF recovers the periodic-boundary result. We further show that these DZMs lead to finite-precision numerical instability, since their finite-size singular values decay exponentially with system size and eventually become unresolved in fixed-precision arithmetic. A reliable small-size branch before this loss of precision can be used to estimate the thermodynamic LRF by linear extrapolation. Our results identify DZMs as both a diagnostic of boundary-dependent LRFs and the origin of the associated numerical instability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03468v1
- Title: Superposed circular motion Unruh effect in (3+1) dimensions
- Authors: Taylor Cey, Cisco Gooding, Robert Mann
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.03468v1  pdf=https://arxiv.org/pdf/2607.03468v1.pdf

Abstract:
Using a recently-introduced quantum control model for Unruh-DeWitt detectors in superpositions of classical trajectories, we investigate the response of a detector interacting with a massless scalar quantum field in (3+1) dimensions along a superposition of circular trajectories. We present numerical results for the transition probability and effective temperature of such a detector in four distinct geometric scenarios: (a) concentric, vertically-stacked trajectories, (b) planar, horizontally-displaced trajectories, (c) static central point and surrounding circular trajectory, and (d) concentric, planar circular trajectories. For Gaussian switching functions that are much broader than the acceleration timescale, in case (a) we find only minor deviations from the well-known, effectively thermal response of a single circular trajectory, whereas in case (c) we find a significant reduction in the effective temperature and greater variation with energy gap. We conclude with a discussion of a potential analogue implementation in ultracold atom systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03486v1
- Title: Semiclassical Langevin dynamics of long-range dissipative time crystals
- Authors: Reyhaneh Khasseh, Rosario Fazio, Angelo Russomanno
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2607.03486v1  pdf=https://arxiv.org/pdf/2607.03486v1.pdf

Abstract:
We develop a semiclassical Langevin approach to study finite-size effects in dissipative time-crystalline spin systems. For a spin-$1/2$ model with power-law Lindblad operators, we find finite-size oscillations exponentially decaying in time, and their decay rate decreases algebraically with system size in the long-range regime. The scaling exponent of this decay time provides a direct diagnostic of the robustness of the time-crystalline, and we find that this robustness extends beyond the range of power-law dissipation exponents where the system dynamics is mean-field in the thermodynamic limit. We also apply our approach to a spin-one model with local dissipation and long-range Hamiltonian interactions, formulating it in terms of Gell-Mann variables. In this case, finite-size stability is quantified through the deviation time from the mean-field behavior and the behavior of the dominant Fourier peak. We find that both quantities scale as a power law with the system size -- marking thereby a time-crystal behavior -- when the exponent of the power-law interaction is below a certain threshold, that turns out to be in agreement with previous cumulant-expansion findings. Our results show that semiclassical Langevin dynamics provides a useful finite-size probe of dissipative time crystals in regimes beyond exact Lindblad simulations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03493v1
- Title: Driving collective RPA modes by a time-dependent Dyson map
- Authors: Andreas Fring, Marta Reboiro
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.03493v1  pdf=https://arxiv.org/pdf/2607.03493v1.pdf

Abstract:
We study a time-dependent non-Hermitian generalisation of the Schütte-Da~Providência model describing a bosonic mode coupled to collective particle-hole excitations. Using a time-dependent Dyson map, we construct a Hermitian counterpart and reduce the collective fermionic sector by means of the random phase approximation (RPA). The resulting dynamics is mapped to two time-dependent harmonic-oscillator branches with instantaneous RPA frequencies $W_\pm(t)$. We determine the corresponding stability regions and compute transition probabilities between instantaneous oscillator states. In first-order instantaneous-basis perturbation theory the leading transition $n\to n+2$ is proportional to $\dot W_j/W_j$, showing that it is purely nonadiabatic and absent in the time-independent case. We compare this result with exact Lewis-Riesenfeld transition amplitudes within the RPA approximation. Numerical examples show that different components of the Dyson map provide distinct driving mechanisms: the scaling parameter modulates the effective coupling, while the squeezing parameter acts through a moving-boundary contribution. In both cases the induced collective transitions exhibit parametric-resonance peaks and sideband structures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03527v1
- Title: Daylight quantum keyless private communication for free-space links
- Authors: Pedro Neto Mendes, Preeti Yadav, Lourenço Sumares, Hugo Zbinden, Davide Rusca, Emmanuel Zambrini Cruzeiro
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03527v1  pdf=https://arxiv.org/pdf/2607.03527v1.pdf

Abstract:
Quantum key distribution (QKD) is the most established approach in quantum communication. However, long-distance free-space implementations, particularly satellite links, remain challenging, especially during the day due to daylight background noise. Quantum keyless private communication (QKPC) is a quantum communication protocol that enables information-theoretic security with simpler system requirements, improved robustness against noise, and without the need for secret key distribution. QKPC and QKD are complementary, with QKPC enabling free-space links where QKD is impractical, while QKD provides channel monitoring for applications that require eavesdropping detection. Here, we report a complete implementation of QKPC in a daylight free-space experiment over a 90 m rooftop link, using an experimentally simple setup. Our demonstration includes all stages of the protocol, from encoding and synchronization to message decoding, operates entirely without auxiliary classical synchronization channels, and is implemented offline through post-processing. This work demonstrates the feasibility of practical and scalable quantum communication over high-noise daylight links and highlights the potential of QKPC as a complementary solution to QKD for future ground-based and space-based communication systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03535v1
- Title: Thermalization hierarchy from irreducible degrees of freedom
- Authors: Pedro Fittipaldi de Castro, Wladimir A. Benalcazar
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2607.03535v1  pdf=https://arxiv.org/pdf/2607.03535v1.pdf

Abstract:
The decomposition of the Hilbert space of a quantum many-body system into the irreducible representations of its bond and commutant algebras yields a finer structure of dynamically isolated subspaces than the mere decomposition into symmetry sectors. While it has been recognized that subspaces associated with low bond-irrep dimensions $D_λ$ tend to violate the eigenstate thermalization hypothesis (ETH), here we show that $D_λ$ controls thermalization continuously across the full spectrum of dynamical subspaces. Using SU(2)-symmetric spin-1/2 chains as a paradigmatic example, we demonstrate that $\mathrm{log} \ D_λ$ quantitatively accounts for the average eigenstate entanglement entropy within each sector, establishing a thermalization hierarchy that interpolates from exact quantum many-body scars at $D_λ=1$ to volume-law ergodic states at large $D_λ$. To make this concrete, we introduce the notion of irreducible degrees of freedom (IDOF), defined as the number of independently-varying spatial coordinates parametrizing a many-body state within a given bond-algebra sector, which provides a microscopic interpretation of $D_λ$ and of the resulting thermalization hierarchy. Finally, we show that by selectively breaking symmetries while preserving chosen bond-algebra sectors, one can embed families of nonthermal eigenstates at prescribed entanglement levels into an otherwise ergodic spectrum, generalizing restricted spectrum-generating algebras from towers of individual states to entire dynamical subspaces.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03538v1
- Title: The arrival position problem in quantum mechanics
- Authors: Ali Ayatollah Rafsanjani, Will Cavendish
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2607.03538v1  pdf=https://arxiv.org/pdf/2607.03538v1.pdf

Abstract:
The problem of making unambiguous probabilistic predictions about experiments involving waiting "always on" detectors remains a challenge for quantum theory. While most research on this problem studies arrival time, i.e., predicting the distribution of when detection events occur, this paper studies the arrival position problem, which is the complementary challenge of predicting the distribution of where detection events occur. Despite the widespread recognition of the arrival time problem, the inability of standard quantum theory to address the arrival position problem remains a pervasive theoretical blind spot. In this paper, we compare quantitative arrival position predictions derived from prominent proposed solutions to the screen problem. As we show, these models yield distinguishable predictions even in relatively simple experiments achievable with current technology. Notably, many of these discrepancies persist even in the far-field limit, where standard semiclassical approximations are typically assumed to be valid.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03552v1
- Title: A Pulsed Live-Cell Quantum Microscope for Entangled Solid State and Biological Qubits
- Authors: Javier Noé Ramos-Silva, Sangjun Noh, Minghao Jiang, Parisa Aghaei, Ayla Hazrathosseini, Jocelyn Leon, Philip Hemmer, Peter J. Burke
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03552v1  pdf=https://arxiv.org/pdf/2607.03552v1.pdf

Abstract:
Two revolutions in quantum sensing are converging on the same microscope stage. Biological qubits have emerged as genetically encoded, optically addressable quantum systems inside live cells. Solid state spin based qubits have been entangled and used as nanoscale correlator magnetometers, delivering sensitivity and spatial-resolution gains that single-spin probes cannot reach. Here we report a pulsed quantum microscope that enables simultaneous quantum state manipulation of both qubit technologies in live cells. The platform combines nanosecond-gated optical excitation at 450 nm and 520 nm, three-dimensional diffraction-limited addressing by galvo beam scanning and piezo objective focus, rapidly switched static and radio-frequency magnetic fields, single-photon timing with picosecond resolution, and microwave control for frequencies from DC to 5 GHz, including the 2.87 GHz resonance of solid state spins, the 500 MHz to 800 MHz resonance of radical pairs in biological qubits, and any future qubit resonance in the GHz range. Live cell imaging with simultaneous biological and solid state nanoparticle qubits in the same cell demonstrates the power of this technique for multiplexed quantum sensing. We anticipate this approach will open new opportunities for researchers to explore quantum sensing in live cells, and, ultimately, entanglement between a solid-state qubit and a protein-hosted spin qubit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03579v1
- Title: Device-independent Quantum Key Distribution in the commuting operator framework
- Authors: Gereon Koßmann, René Schwonnek, Po-Chieh Liu, Hao-Chung Cheng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03579v1  pdf=https://arxiv.org/pdf/2607.03579v1.pdf

Abstract:
Device-independent quantum key distribution (DIQKD) is arguably the gold standard for secure quantum communication, as it aims to rely only on observed input-output statistics of an uncharacterized device which is only assumption to obey the laws of quantum physics. A corresponding security analysis hence demands a description of a quantum experiment from a most general perspective. Under close inspection, existing proof techniques do not always meet this goal as they tend to rely on subtile assumptions on a tensor product structure of the underlying Hilbert space and a 'hidden but finite' dimensionality. In this work, we collect the tools needed for a full analysis of DIQKD in the commuting operator framework, which avoids these subtilities and provides the arguably most general view on a quantum experiment. We rigorously proof the common assumption that in DIQKD measurements can be w.l.o.g. assumed to be projective. Furthermore, we show that task of computing key rates can be casted as a non-commutative polynomial optimization (NPO) problem to which the Navascués-Pironio-Acín (NPA) hierarchy gives a correct and converging relaxation.   As a tool, we generalize the integral representation for the relative entropy by Frenkel [Quantum 7, 1102 (2023)] to general von Neumann algebras and apply techniques from Kossmann and Schwonnek [arXiv: 2411.04858] for the approximation in an NPO program.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03622v1
- Title: Macroscopic Quantum Interference of the Center-of-Mass Motion of Levitated Superconducting Microparticles enabled by Magnetic Higher-Order Traps
- Authors: Jaume Cunill-Subiranas, Fabian Resare, Suocheng Zhao, Sofia Qvarfort, A. Metelmann, Carles Navau, Witlef Wieczorek
- Categories: quant-ph (primary); quant-ph; physics.app-ph
- Links: abs=https://arxiv.org/abs/2607.03622v1  pdf=https://arxiv.org/pdf/2607.03622v1.pdf

Abstract:
We show how magnetostatic higher-order multipole traps can be used to generate macroscopic quantum interference of the motion of levitated superconducting microparticles. An appropriate combination of multipolar magnetic fields offers great versatility in constructing various trap potentials, including anharmonic trap potentials such as Duffing or double-well types. Crucially, the anharmonic trap potentials realize a nonlinearity on the order of hundred times the zero-point motion, i.e., on a length scale below nanometers. These anharmonic potentials allow for the generation of quantum features of the center-of-mass motion of a magnetically levitated superconducting microparticle. Importantly, they can be easily generated with a static arrangement of coils, requiring only that the current running through them is tunable. We propose protocols exploiting the versatility of the magnetic trap landscape to generate non-Gaussian motional states. We solve the dynamics of the center-of-mass motion of the particle in phase space and analyze its parameter dependence. Furthermore, we give a recipe to distinguish classical from quantum behavior in a statistically meaningful way through measurement of the position of the particle. Our results open a path to accessing the quantum regime of the center-of-mass motion of objects with masses larger than picogram, i.e., $10^{13}$ atomic mass units. This will enable fundamental physics experiments for studying the transition between quantum and classical behavior, exploring the intersection between quantum physics and gravity as well as probing of certain types of dark matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03636v1
- Title: From the Hong-Ou-Mandel Effect to Quantum Sensing: Interference of Nonclassical Light with Partial Distinguishability and Noise
- Authors: Matheus Eiji Ohno Bezerra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03636v1  pdf=https://arxiv.org/pdf/2607.03636v1.pdf

Abstract:
This thesis explores the interference of nonclassical states of light, particularly Fock and Gaussian states, in noisy linear interferometers, with applications to quantum information and quantum sensing. Using the phase-space formalism, analytical tools based on generating functions are developed to describe quantum optical interference in a unified way. For multiphoton Fock states, new zero probability events (suppression laws) are identified beyond the previously derived symmetry permutation principle, revealing rich interference structures that is degraded with photon distinguishability. For Gaussian states, the Hafnian-based description of Gaussian Boson Sampling is extended to include partial distinguishability via the overlap matrix of the internal state of the photons. Finally, the link between these interference effects and quantum multiparameter estimation is examined for the simultaneous estimation of phase and loss. This study shows that while probe incompatibility can vanish for optimized non-Gaussian states and some two-mode Gaussian states, at high photon number, measurement incompatibility remains a fundamental constraint even in this limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03747v1
- Title: The influence of the transverse electric field on accelerating vortex state in the axisymmetric electric field
- Authors: Ziyang Ding, Ziqiang Huang, Qi Meng, Alexander J. Silenko, Pengming Zhang, Liping Zou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03747v1  pdf=https://arxiv.org/pdf/2607.03747v1.pdf

Abstract:
The relativistic vortex states of massive charged particles propagating in non-uniform axisymmetric electric field are studied. Starting from the stationary-state equation after the relativistic Foldy-Wouthuysen (FW) transformation and employing the paraxial approximation, the coupled evolution equations for the beam width, wavefront curvature, and Gouy phase are derived. The equations are solved numerically for a quadratic electrostatic potential, an immersion lens, and an einzel lens. The essential influence of the transverse field on beam evolution is demonstrated. The results provide a relativistic quantum framework for controlling accelerated vortex particle beams using electrostatic fields.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03757v1
- Title: Entanglement-Assisted Timing Optimization for Discriminating Amplitude-Damping Dynamics
- Authors: Massimiliano F. Sacchi, Milajiguli Rexiti, Stefano Mancini
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03757v1  pdf=https://arxiv.org/pdf/2607.03757v1.pdf

Abstract:
We analyze minimum-error discrimination of two qubit dynamical processes generated by phase-covariant amplitude-damping Lindbladians in a single-use scenario. The optimization involves both the input probe, possibly entangled with an isolated ancilla, and the interrogation time. For unassisted probes we obtain a closed expression for the optimal trace-norm distinguishability at fixed time, with distinct interior and boundary branches. For entanglement-assisted probes, the common phase covariance of the two channels reduces the diamond-norm optimization to a one-parameter Schmidt family. The resulting formula gives transparent sufficient conditions for fixed-time entanglement advantage and separates this local advantage from advantage after global optimization over time. We exhibit examples in which the best unassisted strategy is approached only asymptotically, whereas an entangled probe achieves a strictly smaller error probability at finite time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03779v1
- Title: Gorini-Kossakowski-Sudarshan-Lindblad equation in different bases: application to driven-dissipative two- and multilevel systems
- Authors: O. A. Ilinskaya, O. V. Ivakhnenko, A. I. Ryzhov, O. Yu. Kitsenko, S. N. Shevchenko
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03779v1  pdf=https://arxiv.org/pdf/2607.03779v1.pdf

Abstract:
An open quantum system can be described by a master equation, of which one of the most popular is the Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) equation. We revisit description of driven-dissipative quantum systems focusing on the appropriate choice of the system's basis and the respective transformations. We consider the GKSL equation in different bases and calculate the dynamics for a qubit and for a qudit. An appropriate choice of the basis is a fundamental problem for theoretical consideration of open quantum systems and provides an opportunity to obtain the desired evolution in practice.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03786v1
- Title: Perturbed quantum billiards on the hyperbolic plane
- Authors: Matic Orel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03786v1  pdf=https://arxiv.org/pdf/2607.03786v1.pdf

Abstract:
We study the emergence of generic quantum chaos from an arithmetic billiard in the hyperbolic plane. Starting from an arithmetic triangle, we introduce small area-preserving geometric perturbations and compute long consecutive sequences of eigenvalues and eigenstates. The spectral statistics show a perturbation-dependent crossover from Poisson-like arithmetic behaviour to the Gaussian orthogonal ensemble (GOE), with the crossover scale moving to higher wavenumbers as the perturbation decreases. To characterize the nearest-neighbour spacing distribution, we compare the data with Brody and generalized-gamma fits. The generalized-gamma form is used only as a two-parameter diagnostic, allowing the small- and intermediate-spacing structure to vary independently from the large-spacing tail, rather than as a universal crossover law. For the weakest perturbation, we also compare the data with an effective block-GOE model, which diagnoses residual block-like structure deep into the computed spectral range. We complement the spectral analysis with Poincaré-Husimi representations of the eigenstates and quantify phase-space localization using an entropy-based measure. Its distribution is well described by Beta distributions whose width decays as a power law in the wavenumber. Before the spectral crossover, the localization statistics retain memory of the near-arithmetic regime. After the GOE regime is reached, the localization-fluctuation widths collapse onto a common decay law, sigma(Beta) ~ k^{-eta}, with eta approximately 0.37--0.38. These results provide a combined spectral and eigenfunction-level picture of the arithmetic-to-GOE crossover in hyperbolic quantum billiards.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03805v1
- Title: A regularization method for quantum neural networks using data symmetry
- Authors: Hiroshi Ohno
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03805v1  pdf=https://arxiv.org/pdf/2607.03805v1.pdf

Abstract:
Leveraging data symmetries has recently become a key strategy in quantum neural networks (QNNs) to improve generalization and training efficiency. In this study, we propose a novel regularization method for QNNs based on input data symmetry. By introducing a penalty term that encourages the model to align with data symmetry, our method enables improved training speed and generalization. This symmetry-based regularization is simple to implement and does not require prior knowledge of the symmetry group. We validate its effectiveness through numerical experiments on both classification tasks and quantum generative adversarial networks. Empirical results demonstrate faster convergence and lower test errors. Furthermore, we provide a theoretical generalization bound using Rademacher complexity and conjecture a condition under which models with symmetry exhibit better generalization. Our findings highlight the potential of symmetry-aware regularization in enhancing the performance of QML models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03820v1
- Title: Matter-wave Induced Transparenc
- Authors: Tongkang wang, Yuqi Liu, Wenlan Chen, Zhendong Zhang, Jiazhong Hu
- Categories: quant-ph (primary); quant-ph; physics.atm-clus; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2607.03820v1  pdf=https://arxiv.org/pdf/2607.03820v1.pdf

Abstract:
Electromagnetically induced transparency suppresses optical absorption through destructive interference, playing a central role in light-matter interaction and quantum information science. We report matter-wave induced transparency, where atomic collisional interactions induce transmission through a lossy molecular potential for the incident atomic scattering waves. Using cesium Bose-Einstein condensates and modulation-induced Feshbach resonances, we realize a three-level atom-molecule coupled system with unprecedented flexibility. Under the dark state condition, a narrow and tunable transparency window appears within a broad dissipative collisional resonance. The transparency window linewidth is controlled by modulation-induced coupling. And scattering pathways are selectable via multifrequency Floquet modulation. These results establish an interference-based route for exploring programmable nonequilibrium and non-Hermitian physics, steering quantum chemistry and precision measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03897v1
- Title: Algebra of quantum mechanics via classical phonons. I: The Schrodinger equation as the Newtonian equation of motion and quantum observables as classical averages
- Authors: Emmanuel Giner
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.03897v1  pdf=https://arxiv.org/pdf/2607.03897v1.pdf

Abstract:
The Schrodinger equation for a single spinless particle is formally obtained via a classical phonon model, namely the Frenkel-Kontorova model. Starting from a one-dimensional lattice of coupled harmonic oscillators, we show that the continuous limit of the corresponding Newtonian equation of motion yields the Klein-Gordon equation for a real-valued field. By introducing a complex-valued change of variables mixing the real-valued displacement and velocity fields, and by separating fast and slow time scales, the Klein-Gordon equation is written as the Schrodinger equation within the non-relativistic limit. This complex change of variable also allows to rewrite classical global observables of the phonon field, such as the total energy or momentum, as the corresponding quantum observables. Additionally, we show that when a friction force is incorporated into the classical model, the corresponding Klein-Gordon equation can be rewritten as a Schrodinger equation with a non-Hermitian Hamiltonian. While the global approach is limited here to the non-relativistic regime and does not address the measurement problem, quantization or relativistic effects, it nonetheless illustrates how quantum algebra and complex-valued wave functions can be exactly reproduced using classical dynamics. The relativistic regime for a spinless particle and the link between commutators and Poisson brackets is addressed in the second part of this series.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03905v1
- Title: On estimating operator norm distance, with optimal trace distance estimation when one state is pure
- Authors: Yupan Liu, Qisheng Wang, Zhan Yu
- Categories: quant-ph (primary); quant-ph; cs.DS; cs.IT
- Links: abs=https://arxiv.org/abs/2607.03905v1  pdf=https://arxiv.org/pdf/2607.03905v1.pdf

Abstract:
We investigate the computational complexity of estimating the operator norm distance ${\rm T}_{\infty}(ρ_0,ρ_1)$, defined via the operator norm $\|A\|_{\infty} = σ_{\max}(A)$, given ${\rm poly}(n)$-size state-preparation circuits of $n$-qubit quantum states $ρ_0$ and $ρ_1$. We provide efficient quantum estimators for the operator norm distance whose complexity is independent of the rank (and thus the dimension) of the states:   1. When one state is pure, we establish an optimal quantum estimator using $Θ(1/ε)$ queries to the state-preparation circuits. Consequently, for constant additive error, say $ε=1/5$, our estimator runs in ${\rm poly}(n)$ time. Since the operator norm distance ${\rm T}_{\infty}(|ψ\rangle\!\langleψ|,ρ)$ is exactly half of the trace distance ${\rm T}(|ψ\rangle\!\langleψ|,ρ)$, our result also gives rank-independent query complexity for estimating both quantities, whereas the approaches due to van Apeldoorn, Cornelissen, Gily{é}n, and Nannicini (SODA 2023) and Wang and Zhang (TIT 2024) have query complexity scaling at least linearly with ${\rm rank}(ρ)$, which can be $\exp(n)$ in general.   2. For general quantum states, we also provide a quantum estimator using $\widetilde{O}(1/ε^{3/2})$ queries to the state-preparation circuits, which shows that the corresponding promise problem is ${\sf BQP}$-complete and improves the ${\sf QMA}$ upper bound sketched by Liu and Wang (ESA 2025). Together with an $Ω(1/ε)$ quantum query complexity lower bound, this leaves only square-root room for improvement.   The key intuition behind our estimators is that, when one state is pure, the pure state $|ψ\rangle$ has overlap at least $1/2$ with the top unit eigenvector of $|ψ\rangle\!\langleψ|-ρ$, reflecting a structural feature specific to the operator norm distance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03909v1
- Title: Algebra of quantum mechanics \textit{via} classical phonons. II: Klein-Gordon dynamics, the Heisenberg formalism, the Dirac canonical commutation rule and the Poincaré algebra through the continuous Poisson bracket formalism
- Authors: Emmanuel Giner
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.03909v1  pdf=https://arxiv.org/pdf/2607.03909v1.pdf

Abstract:
In the first part of this series we have shown how the Schrodinger equation for a single particle and the corresponding non relativistic quantum observables can be obtained from a purely classical phonon model through the Newtonian equations of motion. In this work we focus instead on how the classical Hamiltonian formalism applied to the same phonon system allows to recover the feature of relativistic quantum mechanics for a single spinless particle. Using the classical nature of the phonon model, we naturally define continuous Poisson brackets between classical observables, which allows to recover the dynamics of such observables, i.e. the Ehrenfest relations associated to real-valued Klein-Gordon fields. The Poisson brackets also permits to obtain the generic form of constants of motions, thus generalizing the concept of inner products and momentum on Klein-Gordon fields. We then connect the formalism of real-valued classical functionals with that of hermitian operators and complex-valued wave functions. This is done through the introduction of a non-local complex-valued change of variables which allows to rewrite the real-valued Klein-Gordon equation in a form akin to the Schrodinger equation, and the classical observables as quantum expectation values. Then, we show how this change of variables allows to rewrite the classical Poisson brackets as commutators of hermitian operators. This points out the strict equivalence between the Heisenberg formalism and the formalism of classical Poisson bracket. Eventually, we illustrate how the Poisson brackets allows to recover the transformations of Poincaré group in 1+1 dimension together with its algebra. The latter makes the link between the Lorentz invariant inner product of Mostafazadeh and the Casimir invariant associated to the mass of particle.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03939v1
- Title: Disentangling Haldane Phase by Generalized Clifford Circuits
- Authors: Minsoo Kim, Changhun Oh, Donghoon Kim
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2607.03939v1  pdf=https://arxiv.org/pdf/2607.03939v1.pdf

Abstract:
Disentangling transformations play a central role in the classical simulation of quantum many-body systems, yet their analytic structure and underlying mechanism remain largely unexplored. Here, we study the structure of the disentangler in the Haldane phase of spin-1 systems using generalized Clifford circuits. To this end, we extend the Clifford-circuit-augmented matrix product states (CAMPS)-based density-matrix renormalization group (DMRG) method to spin-1 systems. Within this framework, we find that the local disentanglers optimized for the Haldane phase implement the generalized Kramers--Wannier (KW) transformation, and we analytically verify its optimality for the Affleck--Kennedy--Lieb--Tasaki (AKLT) state. Beyond reducing entanglement, the KW transformation maps the Haldane phase to a phase with spontaneously broken $\mathbb{Z}_{2}$ symmetry. This mapping is distinct from the Kennedy--Tasaki transformation and provides a new unitary route from symmetry-protected topological order to symmetry breaking.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03950v1
- Title: Orthogonality Edges in Strong-Coupling Quantum Work Statistics
- Authors: Atta ur Rahman, Muhammad Noman, S. M. Zangi, Saeed Haddadi
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; physics.app-ph
- Links: abs=https://arxiv.org/abs/2607.03950v1  pdf=https://arxiv.org/pdf/2607.03950v1.pdf

Abstract:
Strong coupling to a reservoir can do more than shift, broaden, or dress the work peaks of a driven quantum system. When the reservoir is infrared singular, a sudden change of a local control parameter can alter the boundary condition seen by infinitely many low-energy modes, converting a quasiparticle-like threshold line into a many-body edge. We demonstrate this mechanism for the inclusive work distribution of the biased spin-boson model under a sudden bias inversion. In the independent-boson limit, the problem is exactly solvable and gives a sharp infrared classification: a super-Ohmic bath can retain a finite elastic threshold weight, whereas Ohmic and sub-Ohmic baths extinguish the elastic line through boundary orthogonality. At the Ohmic fixed point, the same exponent controls both the vanishing elastic residue and the low-work continuum. We then ask how this edge is resolved away from the static-boundary limit. Using displaced-basis exact diagonalization of logarithmically discretized baths, we find that finite tunnelling leaves an edge-like continuum over the accessible energy window, while separating two operational diagnostics of the threshold: the cumulative-continuum exponent extracted from $z$-interleaved spectra lies above the elastic-overlap exponent extracted from $z$-averaged overlaps, $θ_C>θ_Z$. We interpret this separation as a finite-energy crossover away from the static-boundary fixed point, not as evidence for a new asymptotic fixed point. The separation survives fitting-window variation, oscillator-cutoff checks, spectrum-size checks, and leave-one-$z$-out tests, while time-domain characteristic functions provide a compatible but non-decisive diagnostic. Finally, the same threshold edge controls the sampling cost of Jarzynski-type exponential averages, making rare low-work events increasingly important at low temperature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03982v1
- Title: A Semantic Framework for Reproducible Variational Quantum Algorithm Execution Records
- Authors: Silvie Illésová, Martin Beseda
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03982v1  pdf=https://arxiv.org/pdf/2607.03982v1.pdf

Abstract:
Variational quantum algorithms are hybrid quantum-classical workflows whose results depend on many interacting choices, including the ansatz, Hamiltonian, optimizer, backend, shot count, noise model, mitigation method, random seed, stopping criteria, and software versions. In current practice, this information is often scattered across code, configuration files, logs, backend metadata, and paper descriptions, making executions difficult to reproduce, compare, debug, and reuse. This paper proposes an ontology-supported framework for representing Variational Quantum Algorithm (VQA) execution records as structured and machine-readable software engineering artifacts. The framework defines a Web Ontology Language (OWL) ontology for modeling the main entities involved in VQA experimentation, including algorithms, circuits, ansatzes, Hamiltonians, optimizers, backends, noise models, mitigation techniques, execution steps, software environments, measurement outcomes, and results. It further combines the ontology with Shapes Constraint Language (SHACL) constraints for validating completeness and consistency, and SPARQL Protocol and RDF Query Language (SPARQL) competency queries for retrieving reproducibility-relevant information. We demonstrate the approach using Variational Quantum Eigensolver (VQE) execution records, including a valid record and intentionally incomplete or inconsistent examples. The results show that the framework can represent complete VQA execution contexts, detect missing or malformed metadata, and support query-based inspection of information needed for reproducible quantum software experimentation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03983v1
- Title: Verification of Quantum Computations: Hardware-Efficient Security Proofs
- Authors: Harold Ollivier
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.03983v1  pdf=https://arxiv.org/pdf/2607.03983v1.pdf

Abstract:
How can a user with limited quantum resources verify the output of an untrusted, fully quantum server? This manuscript provides a conceptual synthesis of some recent developments toward answering this question under statistical (information-theoretic) security. Rather than duplicating the dense technical proofs of the underlying publications, our focus here is on the physical motivations, the structural connections between different protocols, and the path toward hardware-efficient implementation.   We begin by introducing a modular, composable framework that partitions verification into three distinct, independent primitives: remote state preparation, trap-based deviation detection, and error-correcting embedding. Using this framework, we show how the demanding hardware requirements of early protocols can be systematically relaxed. We review schemes that eliminate the spatial overhead, remove the need to prepare computational-basis dummy states, and replace single-photon sources with trusted local rotations or weak coherent pulses. Finally, we examine how these techniques scale, both to asymmetric multi-party settings and to the delegation of fully fault-tolerant computations in the presence of gate-level noise. This document is intended as a guide to the architectural principles of practical quantum verification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04007v1
- Title: Stellar Braid Monodromy of Finite-Rank Non-Gaussian Photonic States
- Authors: Arnaud Coatanhay, Angelique Dremeau
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04007v1  pdf=https://arxiv.org/pdf/2607.04007v1.pdf

Abstract:
Finite-rank non-Gaussian bosonic states admit a holomorphic description in the Bargmann representation: after a zero-free Gaussian factor is separated off, their non-Gaussian structure is encoded by a finite stellar divisor. This article introduces a topological refinement of stellar rank for regular parameterized families of such states. Rather than only counting the zeros of the stellar divisor, we follow their motion under deformations of the state and record the associated braid monodromy. In the finite-Fock chart, a regular degree-r stellar state is represented by a monic polynomial with r simple zeros. The regular stratum is biholomorphic to the unordered configuration space of r points in the complex plane, and its fundamental group is the Artin braid group on r strands. Thus braid monodromy is an intrinsic invariant of loops in the regular finite-rank stellar state space. We then extend the construction to admissible finite stellar divisors of the form E_tau,mu(z) P(z); the zero-free Gaussian parameters form a contractible fiber over the same configuration-space base. Experimentally motivated finite-Fock families, especially the cubic subspace spanned by the first four Fock states, provide concrete laboratories, while trinomial slices yield explicit discriminants and local half-twists. The resulting invariant is post-tomographic and applies to preparation loops and parameterized families; it complements Wigner negativity, stellar rank, approximate stellar rank, and other scalar diagnostics of non-Gaussianity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04015v1
- Title: The Delayed Stabilizer ZX-Calculus
- Authors: Cole Comfort, Giovanni de Felice
- Categories: quant-ph (primary); quant-ph; cs.LO; math.CT; math.SG
- Links: abs=https://arxiv.org/abs/2607.04015v1  pdf=https://arxiv.org/pdf/2607.04015v1.pdf

Abstract:
Many stabilizer quantum error-correcting codes are built from a finite pattern repeated across space or time, such as lattice codes, translation-invariant graph states, and quantum convolutional codes. Ordinary stabilizer ZX-diagrams capture only finite truncations of such systems, obscuring the repeated structure that defines them. We introduce the delayed stabilizer ZX-calculus, a finite graphical language for these infinite, translation-invariant processes. It extends the odd-prime-dimensional stabilizer ZX-calculus with a single new generator, the delay, which feeds data from one time step to the next. We equip the calculus with two semantics. In the first semantics, we interpret the behaviour of a delayed ZX-diagram as an equivalence class of sequences of quantum channels; where two sequences are identified if they have the same information content. We show that the behaviour of a delayed ZX-diagram uniquely determines an infinite stabilizer group. In the second semantics, we interpret the delay as a formal variable, encoding the translation-invariant families of Pauli operators as generating functions. This allows us to represent a delayed ZX-diagram in terms of a tableau of generating functions, from which the infinite stabilizer group can be recovered. Finally, we give a complete axiomatization of the delayed stabilizer ZX-calculus, featuring generalised Euler decomposition and colour change rules. Using generalised forms of local complementation and pivoting, we reduce every diagram to a unique normal form. This establishes soundness, universality, and completeness for the generating tableau semantics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04021v1
- Title: Detection methods for optimal target reflectivity estimation with two-mode squeezed vacuum probes
- Authors: Harel Radia, Tuvia Gefen, Nadav Katz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04021v1  pdf=https://arxiv.org/pdf/2607.04021v1.pdf

Abstract:
Target reflectivity estimation using a two-mode squeezed vacuum (TMSV) probe offers a theoretical advantage over classical schemes, but realizing this potential under the measurement constraints of microwave platforms remains a central challenge. In this work, we study the precision limits for target reflectivity estimation across different energy and loss regimes, while accounting for realistic measurement restrictions. We characterize the optimal measurements and identify a transition in their structure: above a specific reflectivity threshold, a parametric amplifier receiver is optimal, whereas below it, the optimal observables are two-mode squeezing generators. We then study the performance of Gaussian measurements. When restricted to standard local homodyne detection, the TMSV probe is highly non-optimal. However, we show that suitable non-local Gaussian measurements can closely approach the quantum Cramér-Rao bound at the large noise limit. These results demonstrate that near-optimal quantum target reflectivity estimation is achievable in various relevant noisy regimes, even under the restriction of Gaussian measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04035v1
- Title: Robust self-test of the maximally entangled state of two-qubits without assuming unitary observables
- Authors: Alexandre C. Orthey, Magdalena Stobińska-Moretto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04035v1  pdf=https://arxiv.org/pdf/2607.04035v1.pdf

Abstract:
Standard device-independent self-testing uses Naimark dilation to assume projective measurements, masking the operational limitations of realistic non-unitary observables. We establish a robust pure self-test for the singlet and Pauli observables that entirely circumvents dilation of the measurement apparatus. Assuming a pure state to model an untrusted source, we regularize the physical non-projective operators and derive an analytic $\mathcal{O}(\sqrtε)$ robustness bound. Our results suggest that device-independent certification of real implementations is significantly more demanding than standard projective models imply.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04040v1
- Title: Quantum simulation of gauge theories on dynamical spacetimes via Floquet-induced matrix models
- Authors: Samuel Buckley-Bonanno, Noah Eckstein, Susanne F. Yelin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04040v1  pdf=https://arxiv.org/pdf/2607.04040v1.pdf

Abstract:
Quantum simulations of gauge theories are typically built on spatial lattices, an approach that has enabled major progress at the cost of requiring fixed background geometries and obscuring the treatment of curved and dynamical spacetimes. Large-$N$ matrix models offer an alternative, encoding spacetime geometry and gauge fields in the commutation structure of a set of Hermitian matrices, with the classical continuum emerging smoothly at large matrix dimensions. Here we introduce a Floquet framework that makes these models directly accessible to programmable quantum platforms. We show that Euclidean path integral weights of a Yang-Mills matrix models are reproduced, at leading order in the coupling, by the ensemble-averaged fidelities of Haar-random states evolved under periodic sequences of matrix operators. The observables for the simulated matrix model can then be accessed through established randomized benchmarking protocols in terms of the Loschmidt echo. The encoding requires exponentially fewer qubits than canonically quantized approaches. Numerically, we validate the fidelity-weight correspondence, demonstrate parallelized quantum circuits that sample the path-integral measure, and identify the deconfinement transition of an $SU(2)$ gauge field on both flat and expanding cosmological backgrounds. By avoiding a fixed spacetime lattice, the framework preserves continuous symmetries and unitarity on dynamical geometries, opening quantum simulation to field and spacetime dynamics beyond the reach of conventional lattice methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04052v1
- Title: A Lie-Jordan Geometric Formulation of Lindblad Dynamics
- Authors: Leonel Bixano, Victor Alberto Cruz-Barriguete, Guillermo López-Alvarez, V. G. Ibarra-Sierra, José Luis Cardoso, Alejandro Kunold
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.04052v1  pdf=https://arxiv.org/pdf/2607.04052v1.pdf

Abstract:
We develop a Lie-Jordan geometric formulation of finite-dimensional open quantum dynamics, building on the algebraic framework introduced in our previous work (arXiv:2606.26477). The Hilbert-Schmidt operator space is endowed with an orthonormal Hermitian basis, in which the commutator and anticommutator are encoded by the structure tensors \(C_{μν}{}^λ\) and \(B_{μν}{}^λ\). Within this formulation, the von Neumann and Gorini-Kossakowski-Lindblad-Sudarshan equations admit a direct component representation. Our central result is the identification of a basis-independent universal trilinear dissipative map, \( \mathcal D(X,Y)Z=XZY-\frac12\{YX,Z\}, \) whose components define a universal operator-space tensor depending only on the Lie-Jordan structure tensors. The physical dissipator is obtained by contracting this tensor with the expansion coefficients of the Lindblad operators and the Kossakowski matrix, thereby separating the universal algebraic structure from the model-dependent physical information. We further show that the combinations \((B+C)\) and \((B-C)\) generate internal left and right transports, allowing the elementary dissipative map to be expressed as a left-right bimodule action corrected by an ordered Jordan contribution. The universal map satisfies basis-independent trace and Hermitian-conjugation identities, from which trace preservation, Hermiticity preservation of the complete dissipator, and the reality of its component representation in a Hermitian Hilbert-Schmidt basis follow. We also derive its Hilbert-Schmidt adjoint and illustrate the formalism for a qubit with pure dephasing and amplitude-damping channels. This construction provides a tensorial and affine-geometric interpretation of the universal superoperator structure derived in arXiv:2606.26477 while keeping the algebraic and model-dependent sectors explicitly separated.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04054v1
- Title: Frozen-Tree Sampling Refutes Quantum Advantage of Random Circuit Sampling
- Authors: Sangchul Oh
- Categories: quant-ph (primary); quant-ph; cs.CC; math-ph
- Links: abs=https://arxiv.org/abs/2607.04054v1  pdf=https://arxiv.org/pdf/2607.04054v1.pdf

Abstract:
Random circuit sampling of bitstrings from a Haar-random quantum state is widely believed to be classically intractable, and has therefore been implemented as a primary benchmark for demonstrating quantum advantage. Here, we challenge this premise by proposing an efficient classical frozen-tree sampling algorithm that exploits the conditional scale invariance of Haar-random quantum states [Oh, arXiv:2602.19448]. The frozen-tree sampler draws bitstrings of $n$ qubits in $O(n)$ time per sample. Moreover, its output probability $p_F(x)$ is statistically identical to the probability $p_C(x)$ of a random quantum circuit, since both are independent instances of the same Dirichlet distribution. Consequently, no statistical test acting on samples alone can distinguish the classical frozen-tree sampler from a quantum random circuit. The claimed quantum advantage of random circuit sampling therefore does not withstand scrutiny: its hardness lies not in sampling from the Dirichlet distribution, which is classically efficient, but in identifying a specific circuit realization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04075v1
- Title: Wei-Norman approach for non-Hermitian driven spin-$S$ systems and its application to defect freezing
- Authors: Mingwei Meng, Chen Sun
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; math-ph; nlin.SI
- Links: abs=https://arxiv.org/abs/2607.04075v1  pdf=https://arxiv.org/pdf/2607.04075v1.pdf

Abstract:
In the theoretical study of nonequilibrium non-Hermitian systems, obtaining exact analytical solutions for their nonadiabatic dynamics is highly desirable yet often challenging. In this work, we identify a class of non-Hermitian quantum systems where this difficulty can be substantially reduced. Employing the Wei-Norman approach, we show that for a spin-$S$ subject to a general non-Hermitian time-dependent drive, the matrix elements of the evolution operator can be expressed in closed analytical forms (via Jacobi polynomials) in terms of the corresponding spin-$1/2$ model. This approach is straightforward and accessible to nonspecialists in Lie algebra. As an application, we investigate a specific nonequilibrium non-Hermitian phenomenon known as defect freezing, i.e., the existence of excitations in the adiabatic limit, in spin-$S$ extensions of the $\mathcal{PT}$-symmetric Su-Schrieffer-Heeger model under linear quenches. We derive exact analytical expressions for the momentum-resolved excitation probabilities and the total excitation densities. Our results reveal that defect freezing occurs exclusively in momentum sectors that traverse the $\mathcal{PT}$-symmetry-broken region -- and thus pass through a pair of higher-order exceptional points (EPs) -- during the quench; notably, the excitation density exhibits a singularity at a critical value of the non-Hermiticity parameter. This work enriches the analytical toolkit for nonadiabatic dynamics in multi-level non-Hermitian systems and provides quantitative, testable predictions for defect freezing across higher-order EPs, possibly accessible on platforms such as electric circuit networks and photonic lattices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04080v1
- Title: Coherent quantum control of dark excitons in hybrid metal organic chalchogenolates
- Authors: Christian L. McCoy, Tobias Saule, Mariya Aleksich, Maggie C. Willson, J. Nathan Hohman, Thomas Weinacht, George N. Gibson, Carlos A. Trallero-Herrero
- Categories: quant-ph (primary); quant-ph; cond-mat.other; cond-mat.soft; physics.optics
- Links: abs=https://arxiv.org/abs/2607.04080v1  pdf=https://arxiv.org/pdf/2607.04080v1.pdf

Abstract:
Artificial atom-like systems are a promising candidate for next generation quantum processing. Among them, dark excitons exhibit one of the longest lifetimes at high temperatures. Here, we demonstrate coherent control of dark excitonic states in metal-organic chalcogenolates (MOChas) by using an ultrafast pulse shaper at room temperature. These dark exciton states are optically accessed via two-photon absorption and directly read out with a four-wave mixing process. The system is described by a non-perturbative, two-photon Hamiltonian based on well-known atomic physics and applied to a three level system comprised of two dark excitons. Empirical and theoretical state specific optical access is shown via a simple optical pulse shape. The developed Hamiltonian-based description is a first step towards a quantum processing platform using three-level systems and two photon transitions, one example being dark excitons in the MOCha silver benzeneselenolate (mithrene). Simple conditions for gate operations are laid out and described.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04082v1
- Title: A Cross-Platform Analysis of High-Performance Quantum Error Correction Codes
- Authors: Bryan Pan, Yufeng Xin
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2607.04082v1  pdf=https://arxiv.org/pdf/2607.04082v1.pdf

Abstract:
The theory of quantum error correction was established decades ago. Yet the limitation of the quantum computing platforms in terms of noise level and available physical qubit count persists, which greatly hinders the development of scalable quantum computing systems. In this paper, we present analytical estimates of logical error rates of advanced QEC codes across leading hardware platforms and distributed quantum computing systems using a simple but unified framework. The analysis captures two dominant contributors to logical error: code structure and two-qubit gate overhead. The framework provides a fast estimate of logical error rates and identification of dominating factors in different hardware platforms, such as circuit volume, routing overhead, inter-QPU operations, or asymmetric noise protection. We show that several qualitative trends observed in larger-scale simulations can be reproduced and interpreted analytically within this framework. We further demonstrate that the framework can be used to find the sweet spot design region of distributed QEC, which is critical for the design of distributed quantum computing systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04090v1
- Title: Controlling Atom Array in an Ultra-high-cooperativity Optical Cavity
- Authors: Jilai Ye, Zhihao Chi, Ye Tian, Shuyao Mei, Xiaoyu Li, Wenjun Zhang, Yajuan Zhao, Jiazhong Hu, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04090v1  pdf=https://arxiv.org/pdf/2607.04090v1.pdf

Abstract:
Neutral-atom array and cavity quantum electrodynamics offer complementary strengths for quantum science: scalable, reconfigurable qubit architectures and strong coherent light-matter coupling. Combining them in a single platform requires an optical cavity with simultaneously high cooperativity, sufficient mode volume to accommodate atom array, and ample side optical access for atom trapping, imaging, cooling, and rearrangement, a combination that is challenging to achieve. Here we realize an atomic array integrated with a millimeter-scale Fabry--Pérot cavity whose optically-characterized single-atom cooperativity reaches $η_{\mathrm{cav}}=125\pm13$. Atom-cavity transmission spectra of trapped atoms yield an effective spectroscopic cooperativity $η_{\mathrm{spec}}=112.3\pm3.3$, providing an in-situ verification of strong coupling in the integrated platform, and we demonstrate simultaneous coupling of up to 16 individually trapped atoms to the antinode of the cavity mode. The key technical advance is a two-step mirror-fabrication method combining precision mechanical shaping and carbon-dioxide laser polishing, which produces concave fused-silica mirrors with sub-millimeter radii of curvature and residual roughness below 2 Å. Our results establish a regime of cavity-integrated atomic array that simultaneously provides high cooperativity, large mode volume, and flexible manipulation of individual atoms, opening opportunities for cavity-assisted quantum state readout and long-range entanglement-engineering in atom-array platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04110v1
- Title: Circuit Design Informed Adaptive Variational Quantum Algorithms
- Authors: Muhammad Umer, Dimitris G. Angelakis
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04110v1  pdf=https://arxiv.org/pdf/2607.04110v1.pdf

Abstract:
Resource-efficient computation is of central importance in the noisy intermediate-scale quantum (NISQ) era, where decoherence, gate errors, and restricted qubit connectivity severely limit the reliable execution of quantum algorithms. In this work, we demonstrate that incorporating circuit design considerations is crucial for developing resource-efficient variational quantum algorithms. By focusing on the Hadamard test circuit architecture, hardware-aware qubit connectivity, and problem-specific adaptive framework, we analyze how circuit design constraints can systematically reduce the measurement overhead associated with repeated evaluations of the candidate gate pool in adaptive algorithms. Specifically, we demonstrate reductions in the required measurement resources ranging from at least 25% to as high as 50% - 55%. To assess the effectiveness of our approach, we investigate the ground state problem of the nonlinear Schrödinger equation. Overall, our work contributes to resource-friendly strategies for quantum computation and underscores that algorithmic frameworks should systematically integrate circuit design constraints with hardware-aware and problem-specific structures to enhance the practical feasibility of quantum devices in the NISQ era.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04175v1
- Title: Realizing Next-Nearest-Neighbor Coupling and Peierls Phase in Circuits
- Authors: Xin-Sheng Zhang, Wen-Jie Xu, Hang-Yu Gu, Chuan-Xun Du, Yong-Long Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04175v1  pdf=https://arxiv.org/pdf/2607.04175v1.pdf

Abstract:
We really design the trimerized circuits for the non-Hermitian one-dimensional Su-Schrieffer-Heeger models. There are three models, the initial one just considers the nearest neighbor coupling, the enhanced one is extended to contain the next-nearest-neighbor coupling, and the final one is reenhanced by introducing the Peierls phase. We investigate the dynamics of the circuit Laplacians with respect to the models, find that the topological states appear in the initial model and the response intervals are substantially affected by the next-nearest-neighbor coupling channels and the Peierls phase. These results are practically demonstrated by numerical simulations and experimental measurements. As a conclusion, the trimerized circuits can provide an adjustable and simple platform to investigate new topological physical states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04186v1
- Title: Analytic properties of cross-click operators in passive multi-basis photodetection: monotonicity, exact convergence rates, and dimension reduction for quantum key distribution
- Authors: Zhangdong Ye
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04186v1  pdf=https://arxiv.org/pdf/2607.04186v1.pdf

Abstract:
Cross-click operators, the POVM elements for simultaneous clicks in detectors assigned to different measurement bases, are used in QKD and entanglement-verification analyses with realistic threshold detectors to bound multiphoton contributions. Earlier applications verified the needed growth of the minimum eigenvalue $f^{(n)}$ on the $n$-photon subspace only numerically over finite sectors. This work gives an analytic characterization for passive linear-optical analyzers with arbitrary efficiency mismatch and dark counts. The key observation is that every silence operator is the second quantization $Γ(A)$ of an explicit single-photon contraction $A$, whose $n$-photon restriction is $A^{\otimes n}$ on $\mathrm{Sym}^n$. This yields: (i) monotonicity $f^{(n+1)}\ge f^{(n)}$; (ii) two-sided exponential bounds $\max_b γ_b|A_b|^n \le 1-f^{(n)} \le \sum_b γ_b|A_b|^n$, which determine the exact asymptotic convergence rate from single-photon spectral data; (iii) for ideal detectors and $n\ge1$, the exact formula $f^{(n)}=1-\sum_b p_b^n$; and (iv) an exact factorization $1-f^{(n_A,n_B)}=(1-f_A^{(n_A)})(1-f_B^{(n_B)})$ for the two-party cross-click operator. The results apply to polarization, time-bin, and spatial-mode analyzers within the stated threshold-detector model. As an application, we obtain closed-form photon-number weight bounds used in detection-efficiency-mismatch analyses, replacing finite-sector Fock-space numerics by formulas valid for all photon numbers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04227v1
- Title: Genuine Multipartite Entanglement between Logical Qubits via Cross-Code Lattice Surgery
- Authors: Alex Steiner, Tomasz Andrzejewski, Phila Rembold, Hendrik Poulsen Nautrup, Christian D. Marciniak, Robert Freund, Ivan Pogorelov, Thomas Monz, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04227v1  pdf=https://arxiv.org/pdf/2607.04227v1.pdf

Abstract:
Universal quantum computers are expected to generate arbitrary complex quantum states of logical qubits encoded in many physical qubits. This capability hinges on a fault-tolerantly implemented universal gate set, which no single quantum error-correction code admits transversally but which becomes accessible by joining complementary codes via lattice surgery. Here we report on the experimental generation and certification of logical genuine multipartite entanglement in a trapped-ion quantum processor using a transversally implemented universal logical gate set. The gate set is accessed via lattice surgery across two different codes and comprises a Hadamard gate on a four-qubit surface code and a doubly controlled Pauli-$Z$ ($\overline{\mathrm{CCZ}}$) gate on an eight-qubit 3D colour code. To showcase this lattice-surgery toolbox, we generate both stabiliser (Greenberger-Horne-Zeilinger) and non-stabiliser ($|\overline{\mathrm{CCZ}}\rangle$) states of three logical qubits and verify their genuine multipartite entanglement--a form of correlation beyond statistical mixtures of bipartite entanglement across any bipartition. We further use these cross-code primitives to demonstrate arbitrary rotations of single logical qubits via a $\overline{\mathrm{CCZ}}$-based resource gadget accessing the full universal gate set through lattice surgery. Together, these demonstrations showcase the core building blocks of an architecture for fault-tolerant quantum computation and its ability to generate complex logical quantum states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04279v1
- Title: Weak ergodicity breaking without nonthermal eigenstates
- Authors: Boning Huang, Yongguan Ke, Li Zhang, Lin Ling, Chaohong Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04279v1  pdf=https://arxiv.org/pdf/2607.04279v1.pdf

Abstract:
The typical mechanisms of ergodicity breaking in isolated interacting quantum systems, such as many-body localization and quantum many-body scars, originate from the nonthermal nature of the underlying eigenstates. Here, in the absence of nonthermal eigenstates, we identify a mechanism for collective revivals of multiparticle Wannier states (MWSs) associated with nearly linear bands in a spatially modulated Bose-Hubbard lattice. The MWSs, as superpositions of multiparticle Bloch states within individual energy bands, give rise to band-resolved Wannier-sector fragmentation. The key idea is that spatially periodic modulation folds and separates energy bands of a simple lattice into several sub-bands, among which nearly linear sub-bands inherit the linear segments of the original bands. Although multiparticle Bloch states satisfy the eigenstate thermalization hypothesis (ETH), the MWSs in the nearly linear band still exhibit long-lived collective revivals, due to emergent equally spaced energy levels. Our work provides a route to weak ergodicity breaking in which long-lived revivals arise from spectral phase coherence among ETH-satisfying eigenstates rather than from scar-like nonthermal eigenstates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04289v1
- Title: Chromatic Completeness and the Independence of Geometric Obstruction
- Authors: Karl Svozil
- Categories: quant-ph (primary); quant-ph; math.CO
- Links: abs=https://arxiv.org/abs/2607.04289v1  pdf=https://arxiv.org/pdf/2607.04289v1.pdf

Abstract:
We establish a strict logical separation between two distinct phenomena in orthogonality hypergraphs: chromatic completeness, the possibility of assigning a single globally consistent nondegenerate spectrum to all contexts, and geometric coordinatizability, the existence of a faithful orthogonal representation by rays. A strong chromatic number larger than the Hilbert-space dimension obstructs only the former. It does not, by itself, obstruct the existence of a faithful orthogonal representation. We make this separation explicit by comparing two three-dimensional examples with the same strong chromatic number. A completed 25-ray version of the Yu-Oh configuration has strong chromatic number four and nevertheless possesses an explicit faithful orthogonal representation in R^3. Conversely, Greechie's G_{32} hypergraph also has strong chromatic number four, and has a separating and unital set of two-valued states, but we give an elementary algebraic proof that it admits no faithful orthogonal representation in C^3. The obstruction in G_{32} is therefore not chromatic but projective-geometric: the incidence relations force two distinct atoms to collapse onto the same ray.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04295v1
- Title: Optimal estimation of quantum boundary effect in cosmic string space-time
- Authors: Yao Jin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04295v1  pdf=https://arxiv.org/pdf/2607.04295v1.pdf

Abstract:
The presence of a cosmic string modifies vacuum fluctuations, making the evolution of a two-level polarizable atom position dependent. Such modifications produce effects on the atomic dynamics analogous to those induced by a reflecting boundary. We show that these quantum boundary effects can be estimated by performing a sequence of $N$ measurements on a single probe atom. For a fixed total probe time, the precision limit is attained by preparing each probe in its optimal initial state, performing the corresponding optimal measurement, and shortening the probe time of each probe. The optimal measurement is uniquely determined by the probe's initial state, and the precision limit obtained with the atom initially in the excited state is four times higher than that for an equal-weight superposition state. The estimation precision displays damped oscillatory behavior as the atom-boundary or atom-string separation increases. While polarization parallel to the reflecting boundary is always optimal in the boundary case, the optimal polarization in cosmic-string space-time depends on both the atom-string separation and the deficit angle. For small deficit angles and sufficiently large separations, polarization along the cosmic-string direction becomes inferior to the other polarization directions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04298v1
- Title: Incompatibility assisted Zeno-like confinement enables unbounded sharing of nonlocality
- Authors: Prerna Rao, Som Kanjilal
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04298v1  pdf=https://arxiv.org/pdf/2607.04298v1.pdf

Abstract:
To enable sequential sharing of Bell-nonlocality by an unbounded number of copies, each copy must satisfy two requirements. First, the measurements must be incompatible to extract nonlocality. Second, the post-processsed state, obtained as an equal mixture of the two post-measurement states, must remain nonlocal. We show that the incompatibility requirements impose nontrivial constraints on the choice of the initial nonlocal state and the amount of measurement noise required to ensure that the post-processed state remains nonlocal for an unbounded number of copies. We establish this result for two measurement scenarios, namely, when each copy performs unsharp measurements corresponding to a pair of anti-commuting Pauli observables, and when each copy performs probabilistic projective measurements (PPMs) of a pair of anti-commuting Pauli observables. Furthermore, we show that, in the asymptotic limit, the nonlocal post-processed states of all the copies are almost identical, leading to a quantum Zeno-like confinement within the nonlocal region.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04320v1
- Title: Fundamental limits on state preparation for an open qubit
- Authors: D. A. Abraamian, L. V. Lokutsievskiy, A. N. Pechen
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2607.04320v1  pdf=https://arxiv.org/pdf/2607.04320v1.pdf

Abstract:
We analytically determine the ultimate limits of state preparation in two-level open quantum systems driven by coherent control. For a dissipative qubit governed by a GKSL master equation, we give an exact characterization of the reachable set in the Bloch ball. Dissipation excludes a region of states in the Bloch ball which cannot be approached even under arbitrarily strong coherent driving, and we prove that this region has a nontrivial geometry whose boundary is a surface of revolution around the $x$-axis which is analytic except for two conical singularities. We derive a closed-form control protocol for moving on this boundary, and construct an explicit protocol that steers the system arbitrarily close to any prescribed boundary state. These results provide a complete geometric constructive description of reachable qubit states in the standard dissipative environment, establishing fundamental bounds on controllability and state-preparation fidelity for open two-level quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04348v1
- Title: Supersymmetry and Entanglement in the Generalized Dirac Oscillator
- Authors: H. P. Laba, V. M. Tkachuk
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04348v1  pdf=https://arxiv.org/pdf/2607.04348v1.pdf

Abstract:
The supersymmetric properties of the generalized Dirac oscillator allow us to determine the entanglement entropy between the spin and the continuous variable in a purely algebraic manner. The entanglement has a relativistic origin and disappears in the nonrelativistic limit. The entanglement entropy attains its maximal value in the limit of infinite energy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04363v1
- Title: Purcell effect and quantum Zeno effect suppressed self-discharging of quantum battery
- Authors: Da-Wei Liu, Guoqing Tian, Zi-Hao Li, Shi-Qi Gan, Ying Wu, Liu-Gang Si
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04363v1  pdf=https://arxiv.org/pdf/2607.04363v1.pdf

Abstract:
Quantum batteries (QB), as an energy storage and transfer device, not only show obvious advantages compared to classical electrochemical batteries, but also have important applications in quantum information. Self-discharging is a central obstacle to storing useful work in open QB, especially when the charger itself provides an unavoidable loss channel. Here we show that such charger-induced loss can be converted into a protection mechanism by combining Purcell effect with quantum Zeno effect. We reveal that the virtual photon process and the Purcell effect can induce the strong coupling regime to the quantum Zeno regime, in which the stronger the dissipation of the charger, the weaker the self-discharging effect of the QB. As a result, the dissipation caused by the charger to the QB can be suppressed four orders of magnitude in our scheme. Meanwhile, the quantum Zeno effect induced by the Purcell effect can also avoid the energy backflow between the QB and the charger. Owing to the significantly suppressed dissipation, the stored energy of QB can be charged to a nearly full state and the stored energy is almost converted into extractable work, which greatly improves the energy conversion efficiency.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04399v1
- Title: Topological properties and Majorana Multiplicity in Zigzag Kitaev Chain
- Authors: Rajiv Kumar, Panch Ram, Levan Chotorlishvili, Sunil Kumar Mishra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04399v1  pdf=https://arxiv.org/pdf/2607.04399v1.pdf

Abstract:
We investigate the spectral and topological properties of a zigzag Kitaev chain constructed from two diagonally coupled one dimensional Kitaev chains with a zero and finite superconducting pairing phase difference. Using a Bogoliubov-de Gennes formulation, we analyze the energy spectrum, distribution of Majorana zero modes (MZMs), the quasi-particle dispersion, and the winding number, respectively. For a zero phase difference, the resulting energy spectrum shows topological phases with two, four MZMs, and trivial regions. The phases of gap closure determine the topological phase boundaries. In particular, for the phase difference between $φ=π$, the degeneracy of MZMs is partially lifted, leading to modified topological phases compared to the case $φ=0$. The topological and trivial phase boundaries are further confirmed by evaluating the quasi-particle dispersion and the topological invariant, namely the winding number. We show that the zigzag Kitaev chain contributes independently to the total winding number $ν= 1$ and $2$, giving rise to distinct topological phases that support two and four MZMs. The $ν= 0$ gives rise to a trivial region. The energy spectrum of systems corroborates the analytical phase boundaries and reveals characteristics associated with hybridization, enabling us to obtain the complete phase diagram of the zigzag model. Our results establish the zigzag Kitaev chain as a minimal platform for engineering MZM quantum computations, with potential applications in the study of topological phases and Majorana based qubit physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04455v1
- Title: Controlling many-body quantum chaos in a dissipative optical cavity
- Authors: Filippo Ferrari, Francesca Orsi, Ekaterina Fedotova, Óscar Rios Alves, Michał Zdziennicki, Jean-Philippe Brantut, Vincenzo Savona
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2607.04455v1  pdf=https://arxiv.org/pdf/2607.04455v1.pdf

Abstract:
Cavity quantum electrodynamics (QED) with ultracold fermions provides a promising platform for realizing many-body quantum chaos through disordered, photon-mediated long-range interactions. Such setups are inherently open and are therefore subject to dissipation arising from cavity photon loss and atomic spontaneous emission. In this article, we study the driven-dissipative dynamics of a typical cavity QED setting including controllable disorder and long-range interactions. We find that the two dissipation sources have qualitatively different structures. Cavity loss reduces to a single dephasing channel, whereas spontaneous emission in the experimentally relevant regime generates a collection of nonlocal dephasing channels. Cavity-induced dephasing preserves signatures distinguishing integrable from chaotic Hamiltonian dynamics in observables that depend linearly on the density matrix, while spontaneous emission suppresses these signatures. By contrast, quantities that probe the structure of the many-body state, such as the entanglement entropy, are strongly affected by both dissipation mechanisms. Assuming experimentally realistic parameters, we derive quantitative constraints for the observation and control of many-body quantum chaos in cavity-QED platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04462v1
- Title: Noise-Aware Synthesis of Quantum LDPC Encoder Circuits via Two-Sided Hamming Descent
- Authors: Aditya Sodhani, Keshab K. Parhi
- Categories: quant-ph (primary); quant-ph; cs.ET; cs.IT
- Links: abs=https://arxiv.org/abs/2607.04462v1  pdf=https://arxiv.org/pdf/2607.04462v1.pdf

Abstract:
Quantum low-density parity-check (LDPC) codes are a promising route to fault-tolerant quantum computation, but their use requires efficient preparation of encoded states. Standard encoder constructions generate circuits through fixed algebraic procedures, yet the resulting circuit can contain substantial redundancy. We formulate LDPC encoder preparation as a circuit-resynthesis problem: given the linear-reversible matrix implemented by the encoder's CNOT block, we seek a lower-cost equivalent circuit that can be routed efficiently on the target hardware and which mitigates noise. We propose a novel optimization approach referred as two-sided Hamming descent and a noise-aware optimization pipeline for this task.   Across several families of Calderbank-Shor-Steane (CSS) LDPC encoders, including Bivariate Bicycle, hypergraph-product, and entanglement-assisted codes, the proposed pipeline produces substantially smaller and shallower encoder circuits than the standard constructions and the synthesis baselines considered, cutting gate counts by 53.8% in aggregate across the benchmark and by up to 68% on the Bivariate Bicycle family. The gains remain visible after routing, where the two-qubit depth is reduced by up to 71% and translate into higher-fidelity state preparation under circuit-level noise. On the Bivariate Bicycle family, live-range scheduling further reduces routed preparation failure by up to 13.7% without adding two-qubit gates to the selected circuit. These results indicate that encoder-matrix resynthesis, combined with hardware-calibrated selection and scheduling, is an effective compiler-level tool for preparing quantum LDPC code states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04488v1
- Title: Trace-to-Hilbert-Schmidt Speed Ratio in Quantum Dynamics: Universal Bounds and Effective Rank
- Authors: Hossein Rangani Jahromi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04488v1  pdf=https://arxiv.org/pdf/2607.04488v1.pdf

Abstract:
We study the ratio between the trace speed and the Hilbert-Schmidt speed for differentiable finite-dimensional quantum states, $\mathcal R(φ)=\|\partial_φρ(φ)\|_1/\|\partial_φρ(φ)\|_2$. Because $\partial_φρ(φ)$ is always Hermitian and traceless, this ratio is constrained more strongly than for a generic operator. For any nonzero tangent operator $X=\partial_φρ$ of rank $r$, we prove the sharp bounds $\sqrt{2}\le \|X\|_1/\|X\|_2\le \sqrt r$. The lower bound is attained exactly for rank-two tangents, while the upper bound is attained exactly when all nonzero singular values are equal, which in the traceless Hermitian setting requires even rank. At every nonstationary point of a pure-state family, the tangent has rank two, implying $\mathcal R=\sqrt2$. For odd Hilbert-space dimension $d$, we further prove the sharp global maximum $\mathcal R\le \sqrt{d-1/d}$, with equality characterized by full-rank spectra whose positive and negative eigenvalues are separately degenerate and have multiplicities differing by one. We identify $\mathcal R^2$ as the inverse participation ratio of the singular-value distribution of the tangent operator, giving $\mathcal R$ a natural interpretation as an effective-rank diagnostic for local quantum dynamics. Furthermore, we decompose the effective rank into classical (eigenvalue) and quantum (eigenvector) contributions and prove the bound $r_{\mathrm{eff}}\le r_C + r_Q$, with equality guaranteed when either component vanishes. We establish a direct inequality linking the effective rank to the quantum Fisher information (QFI), which forces a large number of active singular modes when the QFI is small relative to the squared trace speed. Finally, we derive a hierarchy of quantum speed limits in which the effective rank controls the tightness of bounds expressed through the Hilbert-Schmidt speed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04519v1
- Title: Schrodinger Oscillator and its Thermal Properties in a Dynamical Noncommutative Space
- Authors: Ilyas Haouam
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.04519v1  pdf=https://arxiv.org/pdf/2607.04519v1.pdf

Abstract:
In this paper, we study the two-dimensional Schrodinger oscillator within a dynamical noncommutative (DNC) space. By leveraging perturbation theory, we derive the energy eigenvalues and eigenvectors and systematically analyze the effects of both dynamical and non-dynamical noncommutative settings. First-order corrections to the eigensystem are obtained, revealing that the energy shift explicitly depends on the DNC parameter tau. Furthermore, we explore the thermal properties of the system by employing the partition function. Numerical results are presented to provide a comprehensive analysis of the system behavior under the considered effects. Notably, in the DNC framework, the commutation relations and the deformation parameter are position-dependent. Using the two-dimensional Bopp-shift, we effectively map the noncommutative problem to its commutative counterpart.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04538v1
- Title: Security of Quantum Conference Key Agreement with Two-Way Classical Communication
- Authors: Shun Kawakami, Mori Watanabe, Takuya Ikuta, Koichi Takasugi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04538v1  pdf=https://arxiv.org/pdf/2607.04538v1.pdf

Abstract:
Quantum conference key agreement (QCKA) enables multiple users to establish a common secret key with information-theoretic security and is regarded as a key primitive for secure communication in future quantum networks. However, practical implementations of QCKA typically suffer from higher noise levels than conventional bipartite quantum key distribution (QKD), making the improvement of the tolerable error threshold an important challenge. Gottesman and Lo proposed two preprocessing procedures for QKD with two-way classical communication, known as the B-step and the P-step, which enhance the tolerable error threshold. In this paper, we analyze the asymptotic security of QCKA with tripartite GHZ states and two measurement bases using two-way classical communication, including multiple B-steps and P-steps. We derive the corresponding secure key rate analytically and demonstrate that iterative B-steps can increase the tolerable error threshold beyond 20%, significantly improving upon the approximately 11% threshold achievable without two-way classical communication and the approximately 15% threshold obtained with only a single B-step. Our results show that two-way classical communication can substantially enhance the robustness of practical QCKA protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04555v1
- Title: Equiangular weighted frames and conical 2-designs with unequal traces
- Authors: Katarzyna Siudzińska
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04555v1  pdf=https://arxiv.org/pdf/2607.04555v1.pdf

Abstract:
Conical 2-designs are families of positive operators possessing crucial symmetry properties that allow them to efficiently characterize important quantum measures. However, little is known about their general structures and properties. We propose a construction method of conical 2-designs whose elements are not of equal traces, based on a generalization of equiangular weighted frames to non-projective operators. We provide a detailed analysis of their properties, relations to quantum measurements, and applications, together with examples that go beyond the known classes. This constitutes a major step toward a full characterization of informationally overcomplete quantum measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04584v1
- Title: Quantum random walks on d-regular graphs with Haar-random coin operators
- Authors: Alice C. Quillen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04584v1  pdf=https://arxiv.org/pdf/2607.04584v1.pdf

Abstract:
With unitary coin operator that is a random matrix drawn from a uniform distribution with respect to the Haar measure, we construct a variant of a discrete quantum random walk using a d-regular undirected connected simple graph. With each step of the walk, the coin operator random matrix is drawn independently from the distribution. The expectation value over the distribution of random unitaries for the associated quantum channel gives a depolarization channel for the coin subspace and resembles the associated classical random walk where the direction a walker steps depends upon the outcome of a fair coin or balanced d-sided dice. Remarkably, despite the fact that the averaged channel depolarizes the coin subspace, measurements in the vertex subspace can be designed that would reveal information about the initial quantum state, even after many iterations of the channel. We illustrate with examples of quantum walks on Cayley graphs of Abelian groups, such as the cycle and hypercube graphs. These quantum walks are examples of bipartite strongly interacting systems, where one subsystem is strongly perturbed, yet information about the initial state in the other subsystem is potentially measurable forever. Due to its decoherence, a quantum random walk with a Haar-random coin would not be useful in search algorithms but could aid in understanding quantum systems with strongly perturbed subsystems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04586v1
- Title: QuTuner: Feature- and Learning-Guided Optimization Pass Tuning for Quantum Compilers
- Authors: Ming Zhong, Xiangyu Ren, Jinglei Cheng, Shaohua Li, Zhiding Liang
- Categories: quant-ph (primary); quant-ph; cs.SE
- Links: abs=https://arxiv.org/abs/2607.04586v1  pdf=https://arxiv.org/pdf/2607.04586v1.pdf

Abstract:
Quantum compilers play a key role in transforming quantum circuits into lower-cost implementations with improved execution fidelity. This process is commonly guided by circuit-level metrics, such as gate counts and circuit depth. Although compiler pass tuning has been widely studied in classical compilation, directly transferring these techniques to quantum compilers is challenging, because quantum programs are expressed as circuits and exhibit optimization behaviors that are shaped by quantum-specific structures. Prior quantum compiler tuning approaches have begun to use circuit features to guide pass selection, but they remain limited in two aspects: they search only a small portion of the optimization-pass space, and they mainly rely on static features that do not explicitly reflect how a circuit reacts to compiler optimizations.   We present QuTuner, a feature-guided quantum compiler pass tuning framework that generalizes across compilers and tuning objectives. QuTuner first builds a large optimization dataset. It then characterizes each circuit from two complementary views: static circuit features that describe circuit structure, and optimization-aware pass embeddings that summarize the circuit's responses to individual optimization passes. Using these representations, QuTuner trains two offline models to retrieve and rank candidate pass sequences for unseen circuits, followed by lightweight refinement. We evaluate QuTuner on Qiskit and PyTKET using two benchmark suites. On Qiskit, QuTuner improves the evaluation-metric reduction by up to 84.85% over the strongest baseline while reducing tuning time by 73.59%. On PyTKET, it improves metric reduction by up to 18.68% with a 64.49% reduction in tuning time. These results show that QuTuner provides an effective approach to adaptive pass tuning for quantum compilers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04598v1
- Title: Breaking the One-Dimensional Expressibility-Trainability Tradeoff
- Authors: Kyoungho Cho, Yu-Seong Jeon, Jinhyoung Lee, Jeongho Bang
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2607.04598v1  pdf=https://arxiv.org/pdf/2607.04598v1.pdf

Abstract:
Expressive parameterized quantum circuits (PQCs) are often designed under a dilemma: the growth of expressibility and entangling power (EP) that improves Hilbert-space coverage is also expected to randomize an ansatz and activate barren-plateau (BP) conditions. We show that this dilemma is not a one-dimensional tradeoff. The usual picture collapses three inequivalent objects -- parameter-ensemble coverage, fixed-circuit entangling response, and local gradient moments -- into one scalar narrative. For a fixed circuit probed by Haar-product inputs, EP is a global two-copy mean of the output-entanglement distribution, whereas entangling-power deviation (EPD) is a global four-copy fluctuation descriptor. Gradient variance, however, is a local two-copy contraction selected by a parameter light cone and a cost observable. This moment hierarchy yields an analytic separation: equal EP need not imply equal trainability, as witnessed by equal-EP circuits with different EPDs and different gradient variances. These separations turn EP and EPD into a two-dial design rule for PQC ansatzes: EP measures how far the circuit has moved along the coverage dial, while EPD monitors whether input-dependent variability remains. We find that ansatz routes can reach high, Haar-like coverage before EPD and gradient variance collapse, showing that coverage and BP activation are distinct crossover events. The EP/EPD framework thus breaks the apparent one-dimensional expressibility-trainability tradeoff into a practical design rule: search for highly expressive PQCs in the window where coverage is high but BP-like homogenization has not yet erased trainable structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04656v1
- Title: Measurement Geometry as a Resource for Certifying Network Nonlocality
- Authors: Leon Adachi, Le Bin Ho
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04656v1  pdf=https://arxiv.org/pdf/2607.04656v1.pdf

Abstract:
Quantum networks can exhibit nonclassical correlations that cannot be explained by classical models with independent sources. While the role of entanglement is well understood, the impact of measurement design remains largely unexplored. Here we develop an operational framework for certifying network nonlocality in the bilocal Alice--Bob--Charlie network using ancilla-assisted meters to evaluate the nonlocal observables required for bilocal and fully network nonlocal (FNN) witnesses. The approach successfully reproduces both bilocal and FNN correlations in simulation. On the 156-qubit superconducting processor \textit{ibm\_kingston}, we observe bilocal nonlocality with $\mathcal{S}_{\rm BLHV}=1.067(6)>1$ after readout-error mitigation, while the FNN witnesses reach $99\%$ and $96\%$ of their certification thresholds, implying the substantially stronger requirements for FNN certification. We further show that Bob's joint measurement determines the accessible level of network nonlocality: bilocal and FNN certification are optimized by different measurement settings, while both violations can disappear even for maximally entangled states. These results identify measurement geometry as an independent resource for network nonlocality and provide a practical route toward its certification on programmable quantum processors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04659v1
- Title: Krylov complexity, mode-resolved complexity and entanglement entropy across phase transitions in the non-Hermitian extended Su-Schrieffer-Heeger model
- Authors: Ling-Feng Zhang, Wing Chi Yu
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2607.04659v1  pdf=https://arxiv.org/pdf/2607.04659v1.pdf

Abstract:
We investigate phase transitions in the extended Su-Schrieffer-Heeger (SSH) model with next-nearest-neighbor hoppings and an imaginary staggered chemical potential. In the presence of small non-Hermiticity, exceptional points emerge in pairs from the gap-closing momenta near the topological phase boundaries of the Hermitian limit. Utilizing the Krylov spread complexity and entanglement entropy, we analyze two dynamical protocols: (i) preparing the non-Hermitian ground state via a unitary transformation, and (ii) evolving the system under the non-Hermitian Hamiltonian. We show that the spread complexity, and long-time spread complexity as well as entanglement entropy can effectively signal phase transitions in the first and second protocols, respectively. To unravel the detailed structure of the transitions, we introduce the momentum-resolved complexity that identifies the characteristic modes and tracks their evolution with the driving parameter. In the regime where the system possesses a purely imaginary spectrum, we further identify dynamical phases based on the saturation behavior of the spread complexity. The entanglement entropy is also found to exhibit similar saturation behavior, thereby providing a more experimentally accessible probe of the dynamical phases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04669v1
- Title: Estimation of a sparse multi-qubit Hamiltonian via compressed sensing
- Authors: Juntao Tu, Yuanlong Wang, Shuming Cheng, Shuixin Xiao, Zhibo Hou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04669v1  pdf=https://arxiv.org/pdf/2607.04669v1.pdf

Abstract:
Hamiltonian estimation is an effective approach in studying the structure and dynamical evolution of quantum systems. The difficulty in estimating the Hamiltonian is that an $N$-qubit Hamiltonian has $4^N-1$ unknown parameters, requiring exponentially many equations for information extraction. In this paper we develop a method based on compressed sensing to estimate the Hamiltonian of a multi-qubit system. We identify a problem where as $N$ increases, the common sufficient condition (Restricted Isometry Property) for compressed sensing often fails, obstructing the application of compressed sensing in ($N\geq 3$)-qubit Hamiltonian estimation. To solve this problem, we propose a ``scale transformation" technique to restore RIP and ensure a compressive estimation of a $k$-sparse Hamiltonian using only $O(k\log(4^N/k))$ equations. In the numerical examples, we estimate the Hamiltonians of two 6- and 30-qubit systems, demonstrating the effectiveness of the method.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04672v1
- Title: A Path-Superposition Framework for Quantum Gate Teleportation
- Authors: Santiago Ávila, Marco Enríquez
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04672v1  pdf=https://arxiv.org/pdf/2607.04672v1.pdf

Abstract:
Quantum gate teleportation enables distant parties to implement nonlocal quantum operations without physically transferring the participating qubits, making it a promising primitive for distributed quantum computing. We introduce a general framework for deterministic quantum gate teleportation based on path superposition, in which the target nonlocal operation is specified through the phase of a preshared maximally entangled resource and a suitable family of path-dependent local unitary operators. The framework establishes general design conditions that guarantee deterministic teleportation after measurement of the control qubits and the application of local correction operations. As representative realizations, we construct teleportation protocols for controlled-NOT (CNOT) and controlled-Z (CZ) gates, demonstrating that different nonlocal operations can be implemented within the same protocol architecture through appropriate choices of the design parameters. We further outline a proof-of-concept photonic realization based on spatial-path and polarization degrees of freedom. The proposed framework identifies path superposition as a versatile resource for quantum gate teleportation and distributed quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04721v1
- Title: Mapping open quantum dynamics onto graphs
- Authors: Kyuho Kim, Dayeong Lee, Seungkyun Park, Xianji Piao, Namkyoo Park, Sunkyu Yu
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2607.04721v1  pdf=https://arxiv.org/pdf/2607.04721v1.pdf

Abstract:
Graph-theoretic frameworks have been widely employed in quantum physics to address the high-dimensional complexity of quantum systems. Although open quantum dynamics incorporates system-bath coupling via numerous interacting operators, it has been formulated algebraically with a partial set of jump operators or statistically universal reservoirs, leaving the underlying connectivity structure largely unexplored. Here, we propose a universal graph-theoretic framework for Markovian quantum dynamics. The framework maps open quantum dynamics onto two uniquely defined graphs, where the quantum master equation is rigorously interpreted as the average wave characteristic of operator-valued signals across the graphs. Applying this framework to the open quantum Rabi model, we demonstrate an open-system generalization of Fock-state lattices, characterize graph-topological signatures of dissipation, and classify the weak-to-ultrastrong coupling transition. Building on these representations, graph pruning reveals the backbone of open quantum dynamics, which enables superior graph neural-network learning. Our results bridge graph theory and open quantum dynamics, achieving efficient data-driven analysis of high-dimensional complexity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04736v1
- Title: Magnetic graphs for cavity quantum electrodynamics
- Authors: Sunkyu Yu, Xianji Piao, Namkyoo Park
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04736v1  pdf=https://arxiv.org/pdf/2607.04736v1.pdf

Abstract:
Strengthening light-matter coupling has become a central challenge in cavity quantum electrodynamics (QED), enabling ultrafast gate operations, qubit protection, and deterministic nonlinear optics. As the coupling increases, even the simplest configuration, a two-level atom interacting with a quantized field, requires careful treatment, as exemplified by the gauge-invariant quantum Rabi model (QRM). Here we propose a magnetic graph model for single-atom cavity QED, which enables the interpretation of quantum dynamics across the ultrastrong coupling regime through graph connectivity. We demonstrate that the generalized QRM maps onto a complex bipartite graph of identical sites under Floquet boundary conditions. This framework captures the crossover from weak to deep-strong coupling via a single metric: the cost of disconnecting a nonmagnetic subgraph. We examine the mechanism underlying this connectivity transition, establishing phase frustration induced by subgraph topology as the primary driver. Scalable to many-body systems, this approach bridges graph theory and cavity QED, revealing highly complex-graph dynamics even in the simplest setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04742v1
- Title: Quantum-Optical Bound States in the Continuum
- Authors: Ruo Kun Cai, Zhi Jiao Deng, Chun Wang Wu, Ping Xing Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04742v1  pdf=https://arxiv.org/pdf/2607.04742v1.pdf

Abstract:
Bound states in the continuum (BICs) are counterintuitive localized states that lie within the continuum of extended states. While extensively realized and utilized in classical wave systems, it is still unclear what a close analog of BICs would be, and how to extract their experimental signature in quantum-optical settings -- where the wave field itself is quantized into bosonic excitations. Here, we present a paradigmatic quantum-optical model consisting of a driven multi-level Jaynes-Cummings (JC) system, featuring few quantum degrees of freedom yet capable of hosting a BIC. Using the concept of a Fock-state lattice (FSL), this model can be mapped to an extended structure comprising two semi-infinite inhomogeneous Su-Schrieffer-Heeger (SSH) chains coupled to a common continuum. An appropriate quantum superposition of two topological zero modes from the separate chains forms a BIC that remains perfectly localized in the Fock-state dimension within the continuum spectrum, due to complete decoupling from the common continuum via destructive quantum interference. We further develop a method to extract the spectroscopic signature of the BIC -- a discrete peak embedded in a continuous background -- by Fourier-transforming the time-dependent dynamics of the system's chiral-symmetry operator. A highly feasible experimental proposal using a single trapped ion is provided. Our work bridges BIC physics with quantum optics, opening a pathway to harnessing such exotic states at the quantum limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04791v1
- Title: Sector-memory obstruction to probe-level bath emergence in finite programmable qubit environments
- Authors: Gaurav Sarmah, Ramakrishna Podila
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2607.04791v1  pdf=https://arxiv.org/pdf/2607.04791v1.pdf

Abstract:
Finite quantum environments can relax local probes without acting as canonical baths. We study this distinction for a probe qubit coupled to a programmable bath of ($N$) qubits under excitation-number-conserving dynamics. The conserved charge partitions the Hilbert space into sectors. We characterize probe-level bath emergence using the sector-resolved late-time population ($p_e^{(q)}$), the sector-memory variance ($M_N$), and a global Gibbs-fit error ($Δ_G^{\mathrm{global}}$). Exact simulations with Haar-random pure states in each complete fixed-charge sector yield sector-dependent populations close to the maximally mixed-sector benchmark ($p_e^{(q)}=q/(N+1)$), producing a nonzero Gibbs obstruction. We then construct charge-preserving Floquet circuits using ($R_z$) phases and ($XX+YY$) exchange gates, validate them with ideal and noisy Qiskit simulations, and implement finite-depth experiments on IBM Fez. For ($N=4$) and ($ε=0$), the hardware data give ($M_N \simeq 0.044$), ($Δ_G^{\mathrm{global}} \simeq 0.558$), and charge preservation near 0.90 after readout mitigation. A paired symmetry-breaking scan using bath ($R_x(ε)$) rotations reduces both diagnostics while increasing charge leakage, but does not erase sector ordering over the accessible depths. These results show that equilibration within constrained sectors is insufficient to produce a single sector-independent Gibbs state for the probe.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04845v1
- Title: HamQASBench: A Hamiltonian-Informed Diagnostic Benchmark for Evaluating Quantum Architecture Search
- Authors: Jiayang Niu, Akib Karim, Yan Wang, Jie Li, Ke Deng, Azadeh Alavi, Muhammad Usman, Yongli Ren
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2607.04845v1  pdf=https://arxiv.org/pdf/2607.04845v1.pdf

Abstract:
Quantum Architecture Search (QAS) automates the design of parameterized quantum circuits for variational quantum algorithms, yet existing benchmarks organize instances by molecular identity or qubit count -- criteria agnostic to Hamiltonian structure -- and rely solely on energy accuracy, which cannot detect structural failures such as over-parameterization on near-product ground states. We introduce HamQASBench, a Hamiltonian-informed diagnostic benchmark organizing 11 molecules into five structural tiers via fingerprints derived from the Pauli operator basis, computational basis representation, and ground-state entanglement. A post-hoc critical-structure extraction procedure identifies minimal circuits consistent with each tier's requirements, complementing energy-based evaluation with per-qubit entanglement analysis and pairwise state fidelity. Benchmarking five QAS methods across four paradigms reveals failure modes invisible to conventional metrics: over-parameterization in the minimalism regime, eigenstate commitment under degeneracy, a representation bottleneck in strongly correlated systems, topology-induced routing failure, and circuit search space growth as a scalability bottleneck.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04864v1
- Title: Emergence of the Scrooge Ensemble in the Sachdev-Ye-Kitaev Model
- Authors: Zeyu Liu, Pengfei Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04864v1  pdf=https://arxiv.org/pdf/2607.04864v1.pdf

Abstract:
The probabilistic nature of quantum measurement provides a direct window into the structure and complexity of many-body wave functions. When only part of a system is measured, the remaining degrees of freedom form an ensemble of post-measurement states whose statistical structure can reveal a stronger form of thermalization, known as deep thermalization. Recent numerical evidence suggests that this phenomenon is characterized by convergence of the projected ensemble to the Scrooge ensemble, a maximally random ensemble compatible with a given density matrix. In this Letter, we use the solvable Sachdev-Ye-Kitaev (SYK) model to unveil the mechanism by which the Scrooge ensemble emerges in many-body systems. By formulating measurement probabilities and post-measurement states in terms of path integrals, we analytically characterize all moments of the projected ensemble and show that they exactly match those of the Scrooge ensemble, even at short evolution times. We further connect this result to the saddle-point structure of the measurement path integral, which naturally generates the replica permutations underlying Scrooge statistics. Our results establish the solvable SYK model as a tractable setting for exploring universal statistics of quantum measurements in chaotic many-body dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04896v1
- Title: Photonic Cluster State Generation from a Quantum Dot Emitting in the Telecom C-band
- Authors: Giora Peniakov, Reza Hekmati, Johannes Michl, Mohamed Helal, Moritz Meinecke, Jochen Kaupp, Yorick Reum, Martin Kamp, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04896v1  pdf=https://arxiv.org/pdf/2607.04896v1.pdf

Abstract:
Photonic cluster states are a key resource for photonic quantum information processing. So far, deterministic generation of these states has been limited to the near-infrared wavelength range. To achieve quantum advantage in communication while maintaining compatibility with silicon photonics, operation in the telecom wavelength range is required. In this work, we demonstrate deterministic cluster state generation directly in the telecom C-band. This is achieved through repetitive excitation of a hole spin confined in an indium-arsenide quantum dot subjected to an external magnetic field. We characterize the quantum process that generates the cluster state by measuring its process map, obtaining a fidelity of $\mathrm{F} = 0.71 \pm 0.01$ to the ideal case. As part of this characterization, we observe spin--photon polarization entanglement with a negativity of $\mathrm{N} = 0.27 \pm 0.02$. The emitted photons exhibit indistinguishability of at least 83%, demonstrating the potential for future fusion gates necessary for photonic cluster state generation beyond linear connectivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04899v1
- Title: Quantum orientation, Noether structure, composition of systems and operations
- Authors: Heinz-Jürgen Schmidt
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04899v1  pdf=https://arxiv.org/pdf/2607.04899v1.pdf

Abstract:
In this paper we argue that, in addition to the statistical structure of quantum theory, another structure, referred to here as the ``Noether structure," is necessary to describe the composition of systems and to define completely positive operations. A Noether structure reflects the dual role of Hermitian operators as observables on the one hand and as generators of symmetry transformations on the other. This idea has been expressed in a similar form in the works of Alfsen and Shultz, who investigated the conditions under which the Jordan product can be extended to an associative product of operator algebras. Our investigations into the Noether structure and the composition of systems are limited to the finite-dimensional case and establish a connection to completely positive operations. In the case of pure operations, the latter can be characterized as orientation-preserving maps.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04914v1
- Title: Error Mitigation in Bosonic Systems via Virtual Distillation
- Authors: Leonardo Finocchiaro, Marco Robbio, Diogo Gomes, David Gunn, Adithi Udupa, Axel M. Eriksson, Leonardo Novo, Giulia Ferrini
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04914v1  pdf=https://arxiv.org/pdf/2607.04914v1.pdf

Abstract:
Virtual distillation is a promising error-mitigation technique that exploits multiple copies of a noisy quantum state to estimate observables as if measured on a purified state. Although originally introduced in the context of bosonic many-body systems under the name of virtual cooling, its development and applications have largely focused on qubit-based quantum computation. Here, we establish a framework for virtual distillation in bosonic quantum information processing and continuous-variable quantum computing. Building on a diagonalization of cyclic shift operators implemented with passive linear-optical interferometers, we derive experimentally accessible protocols for estimating virtually distilled expectation values of observables relevant to bosonic architectures. In particular, we show how to recover noise-mitigated expectation values of number operators, phase-shift operators, and arbitrary quadratures from multi-copy measurements. For number operators, we further demonstrate the estimation of virtually distilled correlators of arbitrary order through the characteristic function of the photon-number distribution. We apply the framework to states affected by photon loss and dephasing, two of the dominant noise mechanisms in bosonic quantum computation, and quantify the resulting suppression of noise contributions. Our results extend virtual distillation beyond its original setting and provide a practical route toward error-mitigated measurements in bosonic quantum processors using experimentally available linear-optical resources.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04915v1
- Title: How Hard Is Quantum Advantage? A Cloud Microphysics Stress Test for Variational Quantum Models
- Authors: Felix Herbort, Ellen Sarauer, Daniel Ohl de Mello, Paul Christiansen, Steffen Hien, Cedric Brügmann, Dieter Jaksch, Veronika Eyring, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04915v1  pdf=https://arxiv.org/pdf/2607.04915v1.pdf

Abstract:
Quantum machine learning (QML) could have the potential to leverage advantages of quantum over classical computing but still lacks strong evidence of actual improvements and scalability, partly due to phenomena such as barren plateaus. In this paper, we employ a hybrid quantum neural network (QNN) on a dataset on cloud microphysics, containing processes for phase transitions of water in the atmosphere and its related temperature changes, which are highly relevant for accurate climate predictions and projections. To reach optimal performance of our QNNs, we employ a rich and trainable frequency spectrum together with expressivity enhancing classical postprocessing. We find that our QNNs strongly benefit from extensive hyperparameter optimization and thereby demonstrate the feasibility of applying QNNs to complex physical systems. At the same time, the QNNs are outperformed by classical baselines in the form of simple fully-connected neural networks. We discuss identified bottlenecks of this class of quantum models to learn the full complexity of the cloud microphysics dataset to show that there is a need to further understand and improve variational quantum models for machine learning such that they might fill the gap where classical models fail or are inefficient.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04936v1
- Title: Noise-limited secret key agreement with twin optical physically unclonable functions
- Authors: Georgios M. Nikolopoulos
- Categories: quant-ph (primary); quant-ph; cs.CR; physics.optics
- Links: abs=https://arxiv.org/abs/2607.04936v1  pdf=https://arxiv.org/pdf/2607.04936v1.pdf

Abstract:
We investigate the use of twin optical fingerprints derived from correlated physical unclonable functions (PUFs), as a hardware-based platform for cryptographic key generation and distribution. Each fingerprint is associated with a random, yet reproducible speckle pattern, generated when coherent light is scattered by a disordered optical structure. We consider a pair of correlated optical PUFs, and study the conditions under which two honest parties can establish a common secret key, despite fabrication-induced variability and environmental noise. An explicit information-theoretic key-agreement protocol is developed, incorporating secure sketches, error reconciliation, and privacy amplification. We quantify information leakage due to public helper data, and derive lower bounds on the length of the final secret key. The analysis identifies the noise regimes in which secure key agreement is feasible, and examines the performance of both practical and near-capacity reconciliation schemes. Finally, we discuss how twin optical PUFs could be integrated into quantum key distribution (QKD) networks, as a mechanism for establishing an initial pre-shared secret key between two honest users, without relying on computational assumptions or trusted third parties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04950v1
- Title: Contraction and Expansion Values of Quantum Channels
- Authors: Ruben Ibarrondo, Mikel Sanz
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.04950v1  pdf=https://arxiv.org/pdf/2607.04950v1.pdf

Abstract:
The contraction coefficient of the trace distance is a central tool in quantum information, quantifying how strongly a quantum channel degrades the distinguishability of states. However, being an extremal ratio, it captures only the most optimistic behaviour of the channel and is often trivial, even for very noisy channels. Moreover, a single scalar is poorly suited to describe how contraction accumulates under channel composition. In this work we introduce the \emph{contraction and expansion values}, two monotone sequences that refine the contraction and expansion coefficients in the same way singular values refine the operator norm. They arise from a min--max variational principle over subspaces of traceless Hermitian operators, admit an operational interpretation in terms of two state-discrimination games, and are shown to coincide with the Gel'fand or Bernstein numbers of the channel restricted to traceless operators. This identification places the sequences within Pietsch's theory of $s$-numbers and yields, in particular, bounds under channel composition that the contraction coefficient alone cannot provide. We establish their main structural properties and compute or estimate them for single-qubit channels, $d$-dimensional amplitude damping channels, and direct-sum channels.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04979v1
- Title: Extending the Bloch sphere model to an N-qubit system
- Authors: Francisco Piñero, Cristian Franco, Hernán I. de la Cruz, Fernando L. Pelayo, Vicente Pascual, Mauro Mezzini, Jose Javier Paulet, Fernando Cuartero
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04979v1  pdf=https://arxiv.org/pdf/2607.04979v1.pdf

Abstract:
The Bloch sphere is an elegant tool for representing single-qubit states. However, a widely accepted generalization for multi-qubit systems with entanglement remains absent. We propose a novel geometric model extending the Bloch sphere representation to arbitrary $N$-qubit systems using $2^N-1$ spheres. We demonstrate that any pure 2-qubit state is uniquely described by three spheres: two for individual qubits and a third encapsulating bipartite entanglement. Generalizing this, we establish an $N$-qubit parameterization through the hierarchical application of controlled rotation gates along the $Z$ and $Y$ axes. We formally prove a strict bijection between the standard state vector representation and our model's angular parameters. This framework provides an intuitive visualization of multiple entanglement, offering potential computational advantages for quantum simulators and new analytical perspectives on quantum gates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04991v1
- Title: Quantum Hashing via Constrained Rydberg Many-Body Dynamics
- Authors: Han-Chao Chen, Xin Liu, Zheng-Yuan Zhang, Dong-Sheng Ding, Bao-Sen Shi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.04991v1  pdf=https://arxiv.org/pdf/2607.04991v1.pdf

Abstract:
In this Letter, we show that constrained many-body dynamics in Rydberg atom arrays naturally gives rise to a quantum hashing mechanism. By encoding ternary strings into deterministic trajectories in the state space, the classical information space is mapped onto a quantum state ensemble in the Hilbert space with an induced geometric structure. Statistical analysis reveals that this ensemble exhibits high probability near-orthogonality, random-like distribution, and broad geometric coverage. These geometric features naturally give rise to the essential cryptographic properties of quantum hashing, including low collision probability, one-wayness, tamper sensitivity, and privacy preservation. Our results demonstrate that the cryptographic functionality of quantum hashing need not rely on deliberately engineered algorithms, but can instead emerge naturally from constrained many-body dynamics, identifying quantum dynamics itself as a physical resource for cryptographic information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05000v1
- Title: Canonical quantization of neurons
- Authors: Alexander He, Nana Liu, Mark M. Wilde
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cs.LG
- Links: abs=https://arxiv.org/abs/2607.05000v1  pdf=https://arxiv.org/pdf/2607.05000v1.pdf

Abstract:
Canonical quantization provides a systematic procedure for constructing quantum models from classical Hamiltonians. Here, we apply this principle to a fundamental computational primitive of machine learning: the neuron. Specifically, by viewing a neuron as a composition of an energy function and an activation function, we quantize this model by replacing the energy function with a quantum Hamiltonian and applying the activation function to it through matrix functional calculus. This results in an activation observable that can be measured on an input quantum state. We investigate the use of these quantized neurons for function approximation, where the objective is to learn an unknown observable from labeled quantum data. For this purpose, we develop hybrid quantum-classical algorithms for training and evaluation, including procedures for measuring the activation observable and estimating gradients of the squared loss error. Our algorithms for gradient estimation rely on basic primitives like classical random sampling, the Hadamard test, and Hamiltonian simulation, and those for measuring an activation observable rely on quantum algorithms known as the power of one qumode and Schroedingerization. Numerical experiments demonstrate that our quantized neurons exhibit enhanced expressive capabilities relative to corresponding classical neurons on representative learning tasks. Our work establishes canonical quantization as a principled framework for constructing quantum machine learning primitives and provides a foundation for developing neural architectures tailored to quantum data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05072v1
- Title: Transmon Phase Gates Controlled by Superconducting Soliton DAC
- Authors: Derek Reitz, Tony X. Zhou, Aditya Sharma, Ryan Bilotta, John McFarland, Aref Fouladi, Jacob Glasby, Aruna Ramanayaka, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.05072v1  pdf=https://arxiv.org/pdf/2607.05072v1.pdf

Abstract:
We introduce a superconducting digital-to-analog converter (DAC) that filters control noise, provides native multiplexing, performs quantum gates in nanoseconds, and can be controlled by CMOS. This is achieved by transducing a trapezoidal drive pulse into a superconducting soliton, which is then held in the DAC load loop, applying flux to a mutually-coupled superconducting qubit or gate coupler. The analog flux output by the DAC can be easily controlled by varying the soliton hold time, or with a DC-biased tunable DAC-qubit coupler, allowing the DAC to perform a fixed-time, high-fidelity gate that's robust to fabrication variance or flux offsets in the quantum circuit. Our initial demonstration shows that the DAC can successfully perform 5.6 ns S-gates on transmons. We measure the DAC-induced quantum state excitation probability per gate to be 0.05%, and find that the DAC-induced relaxation rate from the qubit 1 state is below the intrinsic T1 rate limit of the transmon. Quantum simulations show qualitative agreement with the measured data, and predict that the DAC excitation rate can be lowered 10 times further by overdamping the Josephson junction (JJ) in the DAC load loop. may be limited by a Interleaved Randomized Benchmarking (IRB) sequences on an observer qubit reveal that, when scaling to many qubits, the DAC's performance may be limited by a non-local, DAC-induced phase error of 1.6% per gate, appearing in ancilla qubits that are not directly coupled to any of the 30 DACs on the chip. We discuss strategies for future layouts of multi-DAC chips that focus on mitigating the source of these non-local, high-frequency electromagnetic interactions (EMI), and how to incorporate a DC-tunable coupler for phase correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05094v1
- Title: Brownian Motion in Orthogonal and Symplectic Groups
- Authors: Zhiyang Tan, Piet W. Brouwer
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; math-ph
- Links: abs=https://arxiv.org/abs/2607.05094v1  pdf=https://arxiv.org/pdf/2607.05094v1.pdf

Abstract:
Matrix Brownian motion provides a powerful framework for studying crossover ensembles in quantum chaos and quantum transport, as well as thermalization and information scrambling in many-body dynamics. Here, we develop a unified diagrammatic framework to characterize Brownian ensembles for orthogonal and symplectic random matrices, which describe systems with particle-hole symmetry. We compute polynomial averages up to fourth order and construct an orthogonally invariant interpolation for the disconnected $\mathrm{SO}^-(q)$ sector of the orthogonal group. We consider applications relating to the fields of quantum information, quantum chaos, and quantum transport.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05107v1
- Title: Complementary 3D color codes for transversal quantum logic
- Authors: Friederike Butt, Luis Colmenarez, Erik Weilandt, Tom Peham, Robert Wille, Markus Müller
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.05107v1  pdf=https://arxiv.org/pdf/2607.05107v1.pdf

Abstract:
Transversal logical gates provide a direct route to fault-tolerant quantum computation, but the Eastin-Knill theorem forbids a universal transversal gate set within a single quantum error-correcting code. We propose a hybrid architecture based on the tetrahedral three-dimensional color code and its Hadamard-transformed counterpart, which we call the H-tetrahedral code. The two encodings support complementary transversal non-Clifford operations. Combined with bitwise Hadamard transformations that switch between the two encodings and a one-way transversal logical CNOT from the tetrahedral code to the H-tetrahedral code, these operations realize an almost-universal transversal logical gate set that enables both the creation of entanglement and logical states with magic. We complete a universal gate set through a pieceably fault-tolerant round-robin construction of a logical controlled-$Z$ gate between two H-tetrahedral codes. This logical entangling gate is interleaved with reduced-overhead Steane-type syndrome extraction using logical two-dimensional color-code auxiliary qubits. Our construction provides a new route toward implementing classically hard-to-simulate quantum algorithms where magic and most entangling operations are transversal while the resource overhead is concentrated in a small number of non-transversal Clifford entangling operations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05109v1
- Title: Characterisation of a satellite-to-ground channel for continuous variable quantum key distribution protocol
- Authors: Emma Tien Hwai Medlock, Vinod N. Roa, Timothy Spiller, Rupesh Kumar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.05109v1  pdf=https://arxiv.org/pdf/2607.05109v1.pdf

Abstract:
In space based quantum key distribution (QKD) protocols, the quantum channel will be dynamic in nature and the channel loss will change with respect to the zenith angle. In the context of continuous variable (CV)-QKD, this will cause issues with parameter estimation and for a transmitted local oscillator in particular it will also fluctuate the shot noise. Therefore, it is vital to characterise this channel loss and the sources of this loss. In this paper the varying channel loss is characterised under practical assumptions. This is shown for various different scenarios, turbulence strengths, as well as wavelengths. This work shows, for the channel parameters considered, it is possible to generate a positive secret key if restricted Eve security assumptions are made.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05112v1
- Title: Fragile single-cone Dirac quantum walks in two dimensions
- Authors: C. W. J. Beenakker, J. Sánchez Férnan, J. Tworzydło
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2607.05112v1  pdf=https://arxiv.org/pdf/2607.05112v1.pdf

Abstract:
It is known that a one-dimensional (1D) quantum walk gives a local space-time discretization of the massless Dirac equation with a single quasi-energy cone (no fermion doubling at low energies), keeping the fundamental symmetries (chiral and time-reversal) of the continuum theory. We show that the analogous 2D construction is fundamentally more fragile. Local two-band quantum walks can have an unpaired Dirac cone, but the protecting symmetries then cease to be ordinary on-site symmetries: they become non-symmorphic, involving half-lattice translations, and are broken by generic spatial inhomogeneities. In particular, we demonstrate that the 2D Dirac quantum walk based on the Ho-Chalker network model can be gapped by potential scattering.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05178v1
- Title: Efficient classical simulation of two-dimensional long-range systems: Rydberg arrays and beyond
- Authors: Jia-Lin Chan, Tao Xiang, Yantao Wu
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2607.05178v1  pdf=https://arxiv.org/pdf/2607.05178v1.pdf

Abstract:
In variational Monte Carlo (VMC) calculations of $N$-site quantum systems with arbitrary all-to-all two-body interactions, evaluating the local energy generally costs $O(N^3)$. We introduce a new framework that reduces this cost to $O(N)$ for tensor network states, capable of scalable and accurate computation of real-time dynamics and ground states. As a result, we obtain accurate simulations of the adiabatic real-time protocol of a $10\times10$ dipolar XY model realized in a Rydberg simulator [C. Chen et al., Nature 616, 691 (2023)], which was previously beyond the reach of classical simulation. Going beyond quantum experiments, we also directly perform ground state VMC to compare with the adiabatic state preparation. Our work demonstrates tensor network VMC as a powerful classical simulator for long-range quantum platforms such as Rydberg and ion-trap simulators, which are currently in urgent need of scalable classical benchmarking tools. As a separate technical contribution, we resolve the pathology of evolving from product states within of tensor network VMC.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05218v1
- Title: Quasi-holonomy in non-adiabatic quantum evolution
- Authors: Erik Sjöqvist, Adam Fredriksson
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.05218v1  pdf=https://arxiv.org/pdf/2607.05218v1.pdf

Abstract:
We develop a framework for quasi-holonomy in non-adiabatic quantum time evolution of subspaces along loops in a complex Grassmannian. By factoring the Schrödinger evolution into dynamical and connection-induced contributions in a moving basis, we obtain an effective geometric generator that depends explicitly on the dynamical propagator. This quasi-connection does not define a genuine connection on the original Grassmann bundle, since its gauge transformation law acquires a history-dependent, nonlocal term. Other ways of factoring the Schrödinger evolution are briefly discussed. All these approaches suffer from the same type of history-dependence, thereby defining transport of subspaces in which geometric and dynamical effects are generally intertwined, just as in the case of the quasi-holonomy. Our work sheds light on the issue of separating quantum evolution of subspaces into holonomic and dynamical parts from an essentially gauge-theoretic perspective.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05281v1
- Title: Routing Anonymity and Identifiability of Noisy Quantum Hardware
- Authors: Ben Priestley, Mina Doosti
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2607.05281v1  pdf=https://arxiv.org/pdf/2607.05281v1.pdf

Abstract:
Present-day quantum computing is cloud-based, where a user submits a circuit to a service provider's proprietary backend hardware. While providers may wish to hide implementation details, scheduling choices, or even which physical device was used, noisy finite-shot outputs can carry backend-specific fingerprints: information imprinted in the classical output distribution that can reveal the backend identity. So far, such fingerprints have mostly been studied from a benchmarking perspective, with limited attention to privacy considerations for users and providers. This work develops the first formal framework for backend identifiability and its privacy implications. We introduce a backend-identifiability game and use it to formalise routing anonymity as a security notion for quantum cloud services. We show that backend identifiability is a hypothesis-testing problem and prove that, under passive i.i.d. access to a single backend, routing anonymity decays exponentially at the Chernoff rate. We also establish a utility-anonymity trade-off, imposing fundamental limits on how much backend-specific information can be removed from classical outputs without degrading their usefulness. In addition, we observe that, for noisy quantum hardware, identifying fingerprints are inherently an intermediate-depth phenomenon, and establish a depth principle using Pauli-transfer-matrix tools. We complement the theory with experiments on Amazon Braket on AWS, using ion-trap and superconducting quantum processors. We observe 87-90% classification between superconducting backends and 96-100% classification across physical platforms, and find that identifiability can survive natural forms of post-processing. Overall, these results establish routing anonymity as a distinct security requirement for quantum cloud computing, and provide a framework for quantifying and controlling the utility-anonymity trade-off.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05307v1
- Title: Quantum Spectral Anomaly Detection
- Authors: Yewei Yuan, Michele Minervini, Mark M. Wilde, Nana Liu
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2607.05307v1  pdf=https://arxiv.org/pdf/2607.05307v1.pdf

Abstract:
A core task in quantum anomaly detection is to compute an anomaly score that quantifies how strongly a test quantum state deviates from a given quantum dataset assumed to be normal. Classically, principal component analysis (PCA) for centered data computes the anomaly score by evaluating the test sample relative to the subspace spanned by the selected leading eigenvectors. However, for quantum data that lack a standard centering, explicitly recovering principal eigenvectors, constructing full Gram matrices, or loading quantum-random-access-memory-style data can be more costly than estimating the anomaly score itself. To avoid these costs, we propose Quantum Spectral Anomaly Detection (QSPADE), which computes PCA-like anomaly scores directly from the spectrum of the average state of the normal dataset. By replacing hard PCA rank selection with a smooth, temperature-controlled spectral threshold, QSPADE makes near-threshold spectral components contribute partially to the anomaly score. This makes the score vary continuously rather than jump when a borderline component is included or excluded, and makes it less sensitive to noise or arbitrary hard cutoffs near the threshold. In the zero-temperature limit, QSPADE recovers the hard-projector PCA score. The proposed measurement-based quantum detector can be calibrated with a sample complexity independent of the data dimension. Numerical simulations show that QSPADE behaves like kernel-PCA on encoded classical data and detects changes across a transverse-field Ising transition without predefined order parameters. Consequently, QSPADE gives an efficient framework for both quantum-kernel anomaly detection on encoded classical data and the monitoring of quantum-native systems where diagnostic observables are unknown.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05343v1
- Title: Quantum Computational Resources and Conformal Field Theory: Unifying Spins, Bosons, and Fermions
- Authors: Ryota Matsuda, Masahiro Hoshino, Yuto Ashida
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2607.05343v1  pdf=https://arxiv.org/pdf/2607.05343v1.pdf

Abstract:
Characterizing a quantum state through the lens of quantum resources provides an information-theoretic perspective on many-body systems. While quantum entanglement serves as the paradigmatic example of a quantum resource, recent studies have shown that quantum magic, a resource for universal quantum computation, can capture aspects of many-body states complementary to those described by entanglement. For instance, in spin systems, conformal field theory (CFT) analysis of the stabilizer Rényi entropy has revealed universal features of nonstabilizerness that are qualitatively distinct from entanglement. In bosonic and fermionic systems, however, a comparable formulation for their computational resource, non-Gaussianity, has yet to be established. In this work, we introduce a unified measure, the magic Rényi entropy (MRE), to quantify computational resources in spins, bosons, and fermions on an equal footing. This allows us to reveal common universal aspects of nonstabilizerness and non-Gaussianity in critical many-body states. In particular, our CFT analysis shows that the universal contribution to the MRE appears as the size-independent term determined by the Affleck-Ludwig boundary entropy. We find that non-Gaussianity can continuously renormalize this universal contribution or drive a boundary phase transition through bulk-induced boundary renormalization-group flows. As a concrete demonstration, we present a detailed CFT analysis of non-Gaussianity in interacting spinless fermions described by the Tomonaga-Luttinger liquid, showing boundary transitions at the Luttinger parameters $K=1/3$ and $K=3$. We perform numerical calculations that confirm our field-theoretical predictions. These results provide a unified field-theoretical understanding of many-body magic across spins, bosons, and fermions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05361v1
- Title: Coherent Control of Energy Transport at Room Temperature in a Noisy Bath
- Authors: Davinder Singh, Paul Brumer
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.05361v1  pdf=https://arxiv.org/pdf/2607.05361v1.pdf

Abstract:
Coherent control of energy transport in a non-equilibrium steady-state (NESS) in a reaction-center-connected donor-acceptor pair is proposed. The pigments are considered to be continuously interacting with incoherent radiation and a phonon bath while being driven by phase-controlled coherent fields. Coherent excitation of the donor-acceptor pair is shown to induce interference between excitation pathways, resulting in phase dependent modulation of the flux. As a consequence one can enhance or suppress energy transfer via interference, e.g. an optical energy switch. The persistence of such interference enables coherent control at a NESS in dissipative regime suggests an extension of the operational scope of quantum control from traditional transient domain with low dissiaption to noisy environment NESS at room temperature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05386v1
- Title: Logical Spectroscopy: Lifted-Product Codes with Addressable Bases
- Authors: Jong Yeon Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.05386v1  pdf=https://arxiv.org/pdf/2607.05386v1.pdf

Abstract:
Quantum LDPC memories can encode many logical qubits, but dimension alone does not make them usable: applications need explicit conjugate logical operators with structured labels and physical representatives. For hypergraph-product (HGP) codes this structure is transparent, since the input matrices are binary and can be row-reduced over $\mathbb{F}_2$. Abelian lifted-product codes are subtler. Their seed entries are shifts, or sparse sums of shifts, in a group-algebra ring rather than a field, so pivot blocks need not be invertible and global row reduction can fail.   We address this with \emph{logical spectroscopy}, a spectral construction that replaces global row reduction by finite-field computations in the Frobenius character packets of the Abelian lift group. The Chinese remainder theorem (CRT) decomposes the group algebra into these packets. In each packet, we compute kernels, quotients, and product-complex homology; we then lift the resulting representatives back with CRT idempotents and pair $X$ and $Z$ logicals through reciprocal trace-dual packets. This gives complete addressable conjugate logical bases for finite Abelian lifted products $\mathsf{LP}(A,B)$.   The same packet data also gives design diagnostics. Packet ranks show how logical sectors split, the lifted representatives give certified upper bounds on the width of the constructed conjugate basis, and whole-orbit erasures decompose into packet-attributed erased-logical dimensions. Thus, CRT packets also serve as working coordinates: they label logical sectors, certify the constructed basis width, and attribute structured erasure failures. Under bounded seed-shape and group-basis-support assumptions, this construction gives Abelian lifted-product qLDPC families an HGP-like feature while preserving the layout freedom of group-algebra lifts.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02754v1
- Title: Possibilistic collapse and extremality of simplicial distributions
- Authors: Aziz Kharoof, Cihan Okay
- Categories: math.CT (primary); math.CT; math.AT; quant-ph
- Links: abs=https://arxiv.org/abs/2607.02754v1  pdf=https://arxiv.org/pdf/2607.02754v1.pdf

Abstract:
Consistent families of locally defined probability distributions that do not admit a joint global distribution are known as contextual, with primary examples arising in quantum theory. In this paper, we study such families of distributions using the theory of simplicial distributions, and further develop the theory for possibilistic distributions defined over the Boolean semiring. We characterize possibilistic collapses of simplicial distributions geometrically using bundle scenarios. Using this characterization together with a new connectivity condition on the total space of a bundle scenario, we provide a criterion for detecting extremal simplicial distributions. In parallel, we develop an analogous theory for presheaves on simplicial complexes, describe possibilistic collapses of empirical models on them using event scenarios together with a categorical extremality condition, and relate the two frameworks via a comparison result. We provide examples of contextual simplicial distributions that arise from our criteria on scenarios of interest in quantum foundations, such as Bell scenarios and boundaries of standard simplices, the latter connecting to Vorob'ev's classical theorem on acyclic complexes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02894v1
- Title: Digital Quantum Simulation of Nonequilibrium Dynamics in the Schwinger Model under a Strong External Electric Field
- Authors: Haobin Chen, Lin Cheng, Xingyu Guo
- Categories: hep-lat (primary); hep-lat; hep-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.02894v1  pdf=https://arxiv.org/pdf/2607.02894v1.pdf

Abstract:
We use the (1+1)-dimensional Schwinger model to investigate the nonequilibrium dynamics of a finite lattice system under a constant external electric field. The lattice Hamiltonian is constructed under open boundary conditions. The vacuum state is prepared using the variational quantum eigensolver (VQE). Scans over the external field strength show the flip of the vacuum state at several field strengths. The critical field strengths agree with theoretical predictions. We further investigate the real-time evolution of the zero-field vacuum under an external electric field using a second-order Trotter-Suzuki decomposition. By comparison with exact diagonalization (ED), we verify that the quantum-simulation protocol reproduces the main features of field-induced boundary charge separation, decay of the vacuum-state fidelity, and quasiperiodic energy redistribution between the electric-field energy term and the fermionic sector. Our results indicate that combining VQE-based state preparation with digital real-time evolution provides a useful approach for studying nonequilibrium dynamics in strong-field lattice gauge theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.02935v1
- Title: Decoherence Effects on Primordial Black Holes and Scalar-Induced Gravitational Waves
- Authors: Waqas Ahmed
- Categories: gr-qc (primary); gr-qc; hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.02935v1  pdf=https://arxiv.org/pdf/2607.02935v1.pdf

Abstract:
Primordial black holes (PBHs) form when large primordial curvature perturbations re-enter the Hubble radius and exceed the classical collapse threshold. These perturbations originate as quantum fluctuations of the inflationary vacuum, motivating a quantum-information description of the PBH-producing scalar sector. We develop a conservative extension of the standard PBH and scalar-induced gravitational-wave (SIGW) framework in which Gaussian quantum discord is used as a diagnostic of residual quantum correlations, not as a new PBH-formation criterion. We describe each \((\bm k,-\bm k)\) pair as a two-mode Gaussian state and show that, in the pure squeezed limit, discord grows rapidly with the squeezing parameter, so low discord thresholds are automatically satisfied for strongly squeezed modes. The nontrivial regime is the mixed state produced by decoherence. Using a Lindblad open-system description, we motivate a Gaussian loss channel for the scalar covariance matrix and distinguish the discord from a covariance-survival factor \(Q_{\rm dec}(k)\). If the decoherence channel suppresses the scalar two-point covariance, PBH abundance can be affected through the classical collapse variance, while the SIGW spectrum is modified more directly by the factors \(Q_{\rm dec}(ku)Q_{\rm dec}(kv)\) inside the radiation-era convolution. For a narrow scalar peak and slowly varying \(Q_{\rm dec}\), this gives the benchmark scaling \(Ω_{\rm GW}^{\rm eff}\simeq Q_{\rm dec}^2Ω_{\rm GW}^{\rm class}\). Thus quantum discord and decoherence provide a controlled way to characterize the quantum-to-classical transition of PBH-producing perturbations, with the clearest imprint appearing in scalar-induced gravitational waves.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03205v1
- Title: Griffiths Anomalous Absorption in Sparse-Loss Photonic Lattices
- Authors: Stefano Longhi
- Categories: physics.optics (primary); physics.optics; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03205v1  pdf=https://arxiv.org/pdf/2607.03205v1.pdf

Abstract:
Light absorption in photonic lattices with sparsely distributed loss sites exhibits behavior analogous to Griffiths physics. Under uniform excitation, the transmitted power shows a stretched-exponential decay and a non-monotonic dependence on the loss strength, with an optimal loss rate that maximizes absorption. This behavior arises from rare, long loss-free segments that act as weakly coupled, long-lived photonic channels, rather than from exceptional point physics or interference effects. Using a minimal tight-binding model with binary quenched dissipation, we show that rare regions produce a universal Griffiths-type subexponential decay. Sparse-loss photonic lattices thus provide an accessible platform to observe disorder-induced anomalous absorption and rare-region Griffiths physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03208v1
- Title: Data-driven multi-objective optimization for alloy recycling using factorization machines and quantum annealing
- Authors: Thomas Plehn, Katrin Bugelnig, Silvana Tumminello, Daniel Barragan-Yani, David Melching
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03208v1  pdf=https://arxiv.org/pdf/2607.03208v1.pdf

Abstract:
Quantum annealing has the potential to provide practical quantum advantage for complex optimization tasks. Here, we present a systematic assessment of an integrated factorization-machine and quantum-annealing workflow (FM+QA) for a technologically relevant application: multi-objective Pareto optimization in metal up-cycling through alloy design. To address the non-convex nature of the Pareto front, we employ the recently proposed data-driven Tchebycheff scalarization (DDTS) scheme. Our results show that FM+QA extends the applicability of QUBO-based optimization to data-driven materials discovery problems with multiple competing objectives. In particular, we analyze the scaling behavior of the approach and compare quantum annealing with classical simulated annealing using both regular binary encoding and one-hot encoding. Finally, we provide a critical perspective on the problem sizes and encoding strategies for which quantum-annealing-based optimization may become practically beneficial in the near future.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03471v1
- Title: Analytic Theory of Phase Transitions in Optical Metamaterials
- Authors: Jiahao Yan, Xiaoshui Lin, Junpeng Hou, Qing Gu, Chuanwei Zhang
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03471v1  pdf=https://arxiv.org/pdf/2607.03471v1.pdf

Abstract:
Optical metamaterials provide a versatile platform for engineering homogeneous electromagnetic media whose distinct phases are characterized by phase diagrams in constitutive-parameter space. However, existing studies of hyperbolicity, topological properties, and exceptional-point formation often rely on highly symmetric models or case-by-case numerical parameter scans, leaving a unified analytic framework that identifies phases and phase transitions directly from the constitutive tensors lacking. Here, we develop a general theory that yields exact analytic criteria for topological transitions, exceptional-point transitions, pinch-off Lifshitz transitions, and optical Lifshitz transitions in homogeneous media. Applying this framework to a tractable example of a gyroelectric medium with anisotropic chirality, we uncover exceptional rings and negative refraction induced by gyroelectric-chiral coupling. By enabling the exact determination of phase boundaries, our theory provides a predictive framework for discovering previously unexplored electromagnetic phases and offers new principles for the systematic design of optical metamaterials.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03474v1
- Title: Non-Diffractive Topological Spin Textures of Relativistic Twisted Fermion Beams
- Authors: Andrei Afanasev, Carl E. Carlson
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03474v1  pdf=https://arxiv.org/pdf/2607.03474v1.pdf

Abstract:
In optics and acoustics, in structured beams, non-diffracting polarization measures in clearly diffracting beams, and spin direction distributions in the core of these waves that have Skyrmionic behavior have been found. We here study the equivalents of these for fermions and show that in corresponding circumstances the non-diffractive spin textures persist independently of spin, statistics, or kinematics (or propagation speed of the structured wave). As a part of the study, we present LG solutions for Dirac particles valid for both relativistic and non-relativistic kinematics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03605v1
- Title: Minimal Proper Time and Deterministic Microstates: Emergent Quantum Fields and Relativistic Spacetime
- Authors: Alessio Maiezza
- Categories: hep-th (primary); hep-th; gr-qc; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03605v1  pdf=https://arxiv.org/pdf/2607.03605v1.pdf

Abstract:
We develop a top-down counterpart of the minimal proper-time formulation of quantum field theory previously introduced as an effective bottom-up framework. Starting from a deterministic pre-geometric substrate of causally ordered events, we show how coarse-graining over microscopic histories leads, at low energies, to an effective Nambu-like quantum dynamics. The elementary deterministic update is identified with the minimal proper-time step, while the growth of coarse-grained equivalence classes controls both the ultraviolet dissipative correction and the scale dependence of the effective quantization strength, encoded in a running Planck constant. In this way, the proper-time cutoff kernel of the bottom-up formulation acquires a microscopic interpretation as the inverse growth of unresolved deterministic histories. In the infrared limit, the dissipative term vanishes and standard unitary quantum field theory is recovered. The same coarse-grained structure also provides a natural setting for an emergent relativistic spacetime geometry, compatible in the macroscopic limit with Einstein gravity. The resulting picture suggests a common deterministic origin for minimal-scale structure, quantum behavior, and relativistic spacetime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03753v1
- Title: Efficient Analysis of Carrier Transport and TM-TE Emission in AlGaN UVC LEDs via Multi-band Localization Landscape Theory
- Authors: Yu-Ming Chang, Ping-Jie Zhuang, Marcel Filoche, Claude Weisbuch, James S. Speck, Yuh-Renn Wu
- Categories: physics.app-ph (primary); physics.app-ph; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03753v1  pdf=https://arxiv.org/pdf/2607.03753v1.pdf

Abstract:
AlGaN-based UVC LEDs (220-250 nm) suffer from poor hole confinement and strain-induced |Z>-band dominance at high Al content (>60%), leading to increased TM emission and reduced external quantum efficiency (EQE). While conventional k.p models combined with Schrodinger, Poisson, and drift-diffusion solvers are widely used to study optical transitions, they are computationally expensive. In this work, we apply the multiband Localization Landscape (LL) model, including the effect of strain, as an alternative that replaces the eigenvalue problem to efficiently capture quantum effects and carrier localization. Using the 3D multi-band LL model with the Wigner-Weyl formalism, we reproduce emission and absorption spectra trends similar to the results in 3D k.p calculations, but with significantly reduced simulation time. The polarization ratio also agrees well with published experimental results across a wide spectral range. Furthermore, we analyze electrical characteristics such as band structure, polarization switching, and carrier confinement under alloy fluctuations and strain. This multi-band LL-based approach provides a fast and reliable solution for understanding and optimizing UVC LED performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03799v1
- Title: Measurement-induced spatially nonuniform fluctuations of the local particle number and their crossover in a quasiperiodic free-fermion chain
- Authors: Toranosuke Matsubara, Kazuki Yamamoto
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.dis-nn; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03799v1  pdf=https://arxiv.org/pdf/2607.03799v1.pdf

Abstract:
We study continuously monitored dynamics of a quasiperiodic free-fermion chain defined on a Fibonacci lattice. We focus on fluctuations of the local particle number, which exhibit a spatially uniform distribution in the unitary limit. Remarkably, we demonstrate that they exhibit a nonuniform spatial pattern originating from the quasiperiodic long-range order under continuous measurement. Furthermore, employing both physicaland perpendicular-space analyses, we elucidate that measurement-induced crossover emerges in fluctuations due to the interplay between the incommensurate modulation and the continuous measurement. While weak measurement yields a distribution reflecting the long-range spatial structure of the quasiperiodic system, an increase in measurement strength alters the distribution into one dominated by the local environment of each site. We also elucidate that the measurement-induced crossover emerges in other physical quantities such as connected correlation functions. These findings offer insights into nonequilibrium quasiperiodic phenomena emerging in continuously monitored dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03845v1
- Title: Quantum tunneling Mpemba effect
- Authors: Hisao Hayakawa, Satoshi Takada
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03845v1  pdf=https://arxiv.org/pdf/2607.03845v1.pdf

Abstract:
The quantum tunneling Mpemba effect is investigated within a continuous one-dimensional symmetric double-well potential open to external environmental sinks at the boundaries ($x=\pm L$). Using a non-Hermitian spectral decomposition of the effective Hamiltonian, we characterize the open-system relaxation dynamics without relying on abstract state-space quenches. We mathematically prove that the non-monotonic behavior of the first non-trivial even-parity spectral coefficient, $a_{2}(T_{i})$, with respect to the initial preparation temperature $T_{i}$ is a universal topological property born from quantum statistical mechanics. Crucially, we demonstrate that this intermediate thermal peak is governed by the Sturm-Liouville oscillation theorem and remains completely invariant with respect to the global system size $L$, contrasting sharply with the boundary-driven classical Mpemba effect. This universal peak arises from the geometric and nodal alignment between highly localized unperturbed states and extended non-Hermitian decay channels. Furthermore, we clarify that while this mechanism is robust, the actual observation of anomalous crossings in the total survival probability trace $S(t,T_{i})$ and the trace distance $\mathcal{D}(t,T_i)$ demand a strict separation of timescales, requiring the over-barrier escape rate to vastly exceed the decay rate of the deep-well tunneling doublet ($Γ_{2}\gg Γ_{0}$ and $Γ_2\gg Γ_1$). Our continuous formulation successfully bridges real-space classical boundary-driven dissipation with open quantum dynamics, providing novel insights for engineering non-equilibrium states via tailored boundary loss.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.03937v1
- Title: Evidence of the Cooper-Pair Field with Gaussian Memory Kernel in Unconventional Superconductors
- Authors: Udomsilp Pinsook
- Categories: cond-mat.supr-con (primary); cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2607.03937v1  pdf=https://arxiv.org/pdf/2607.03937v1.pdf

Abstract:
We develop a dynamical description of the superconducting pair field in which the Cooper-channel Hubbard--Stratonovich field $Δ$ is treated as a memory-dressed Bogoliubov pair field rather than as a purely static order parameter. Starting from the standard pair-field effective action, we couple $Δ$ to antinode-selected collective or self-generated fields. An ensemble of such modes produces a distribution of local Bogoliubov frequencies; when this distribution is approximately Gaussian, ensemble averaging gives the memory factor $\exp[-t^2/(2τ_g^2)]$. In cuprate superconductors, the antinodal gap or pseudogap restricts the active electronic phase space and acts as a momentum-space spectral cavity. It selects fluctuation wavevectors $\mathbf Q_a$ that may become charge-density-wave-like instabilities in an ordered limit, but behave as a reservoir of local collective fields in the fluctuating regime. The same framework admits resonant algebraic prefactors, so that threshold and forced-oscillator responses generate the hierarchy $p=-1/2,1/2,1,3/2,\ldots$, while the Gaussian envelope cuts off secular growth and converts these branches into finite spectral components. The resulting picture contains a robust pseudogap memory channel and, below $T_c$, an additional condensate-assisted coherent channel proportional to $|Δ_0(T)|^2$. Thus the superconducting transition primarily reorganizes pair-field spectral weight between incoherent pseudogap memory and coherent Bogoliubov memory. The frequency-domain response is expressed in terms of parabolic-cylinder functions, and comparisons with Raman, ARPES, tunneling, and doping-dependent ARPES scaling suggest that these probes are complementary projections of the same Gaussian-memory pair continuum. We compare our numerical results with the recent experimental data on Bi$_2$Sr$_2$CaCu$_2$O$_{8+δ}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04065v1
- Title: The Normalised Wigner Negativity Rate as a Second-Moment Probe of Infall in AdS$_3$
- Authors: Ritam Basu
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04065v1  pdf=https://arxiv.org/pdf/2607.04065v1.pdf

Abstract:
In spread complexity, the average position of an operator along its Krylov chain, recovers the right radial momentum of an infalling particle in AdS, yet it is a measure of the first moment, irrespective of the spread of the wavepacket away from its classical trajectory. The rate of a normalized Krylov-Wigner negativity can be proposed as a diagnostic of the second moment of the boundary state that captures this spreading. Starting with the \emph{seed-normalized} Krylov-Wigner distribution -- that is, the Wigner transform of the descendant cloud, with the decaying return amplitude divided out -- we obtain an analytic Bessel form in the macroscopic limit and compute its total negativity explicitly. Retaining the Bessel variable all the way through, we find that the negativity goes as $\sinh^{4Δ}(πt/β)$, while the raw, seed-normalized state negativity saturates, as dictated by the $O(\sqrt{D})$ bound. Using the exact negative binomial statistics of the Krylov chain and the momentum dictionary of Caputa et al.~\cite{Caputa:2024}, the rate of the negativity scales as the growth rate of the Krylov variance at late time asymptotics \emph{if and only if} $Δ=1$, the Breitenlohner-Freedman saturating dimension in $AdS_3$. This dimensionality is special in that the negativity rate is the product of the proper radial position and momentum, $\mathcal{R} \propto \mathcal{C} P_ρ$, i.e., the rate of the tidal stretch of nearby geodesic falling into the horizon. We comment on the direction for future research, in particular the interpretation of the transverse string size operator in terms of the Krylov number operator through the common $SU(1,1)$ discrete series.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04072v1
- Title: Benchmarking API Drift in LLM-Generated Quantum Code Across Successive SDK Versions
- Authors: Mohammad Arif Rasyidi, Syahirul Faiz
- Categories: cs.SE (primary); cs.SE; cs.AI; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04072v1  pdf=https://arxiv.org/pdf/2607.04072v1.pdf

Abstract:
Large language models can generate plausible quantum code, but it is unclear whether they can reliably target the specific software development kit (SDK) version requested by the user. We study this problem as API drift and introduce quantum-api-drift, a benchmark for measuring version fidelity, defined here as execution success on the requested SDK version, cross-version compatibility, failure modes, and documentation-guided repair in LLM-generated quantum SDK code. We instantiate the benchmark with Qiskit, a representative quantum SDK that underwent substantial interface changes across v0.43, v1.3, and v2.0. We evaluate 17 models on 50 tasks with 3 samples per prompt, yielding 450 generated samples and 1,350 executions per model. Sixteen models are tested in a matched REST API setting with a 1024-token output cap, while GPT-5.4 (Codex CLI) is reported separately as a reference configuration. Across the 16 matched REST models, diagonal Pass@1 ranges from 0.02 to 0.85. Claude Opus 4.7 is strongest on v0.43 and v2.0, while Grok 4.20 is strongest on v1.3 at 0.513. Error profiles differ systematically by model strength: weaker models fail mainly with broken imports, while stronger models more often reach deprecation-level failures. Documentation-guided repair succeeds for 0.19 to 0.59 of repair attempts overall and is consistently much more effective for migration to v2.0 than to v1.3. The benchmark artifacts are publicly available at https://github.com/arasyi/quantum-api-drift. These results show that version alignment is a distinct evaluation axis for quantum code generation and that API drift remains only partly recoverable even with migration guidance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04095v1
- Title: ML and AI for density functional theory: different priorities for Kohn-Sham and orbital-free DFT, for electronic and nuclear DFT
- Authors: Xin-Hui Wu, Sergei Manzhos
- Categories: physics.chem-ph (primary); physics.chem-ph; cond-mat.mtrl-sci; nucl-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04095v1  pdf=https://arxiv.org/pdf/2607.04095v1.pdf

Abstract:
We overview similarities and, importantly, differences in computational bottlenecks and accuracy requirements that can be addressed with machine learning (ML) and artificial intelligence (AI) techniques in electronic and nuclear DFT. From these follow different promising methodological and algorithmic choices depending on whether one machine learns the exchange correlation (XC) functional, the kinetic energy functional (KEF), the density or the basis functions. In particular, while the popular deep neural networks remain a potent choice in the context of KS DFT, we highlight their disadvantages when building KEFs and highlight conceptual advantages - yet to be fully realized - of symbolic regression for both electronic and nuclear DFT. We point out promising approaches that can be carried from the more extensively investigated ML-enhanced electronic DFT to nuclear DFT.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04115v1
- Title: Infrared Divergences as Itinerant Vacua
- Authors: Masahiro Morikawa
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04115v1  pdf=https://arxiv.org/pdf/2607.04115v1.pdf

Abstract:
Infrared divergences (IRDs) are usually treated as pathologies to be cancelled, regularized, or hidden in dressed asymptotic states. This paper develops a complementary and constructive viewpoint: an IRD is the signature of an \emph{itinerant vacuum} -- a quantum vacuum that wanders continuously through a family of inequivalent states as a classical order parameter evolves. Each value of the order parameter carries its own coherent vacuum, so moving the order parameter means traversing a succession of orthogonal vacua. The IRD is the field-theoretic cost of this wandering, and the $1/f$ noise, gravitational memory, and non-Gaussian fluctuations that emerge from it are its observable classical remnants.   The technical core is an exact separation in the real-time closed-time-path (CTP) effective action. The infrared-divergent imaginary part of the influence functional must not be left as a divergent coefficient in a deterministic equation of motion; it is instead converted, by a Hubbard--Stratonovich identity, into a classical stochastic source. This step is an algebraic identity of the generating functional and requires no prior coarse graining or decoherence assumption: the retarded kernel encodes the memory of past vacuum transitions, while the noise kernel encodes the quantum uncertainty of the next one. We apply this construction to four parallel arenas -- soft QED, scalar fields in de Sitter space, soft gravitons, and non-equilibrium phase transitions -- and show that the same itinerant-vacuum mechanism underlies $1/f$ current noise, the primordial power spectrum, gravitational memory, and order-parameter dynamics. A geometric formulation in terms of a Hilbert-space bundle over the vacuum manifold is outlined as an outlook.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04207v1
- Title: Uniform mixing and $ε$-uniform mixing on cycles
- Authors: Xiwang Cao, Cuiwen Zhu
- Categories: math.CO (primary); math.CO; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04207v1  pdf=https://arxiv.org/pdf/2607.04207v1.pdf

Abstract:
We study continuous-time quantum walks on cycles. We prove two complementary results. Firstly, the cycle $C_9$ does not admit uniform mixing at any time. Using the similar idea and Dickson polynomials, we prove that $C_{15}$ does not admit uniform mixing at any time neither. Secondly, for every prime $p$, we show that the cycle $C_{p^2}$ admits $ε$-uniform mixing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04393v1
- Title: Atomic oven with rapid thermal response for atom experiments
- Authors: Weilong Huang, Congjun Zou, Feiyu Dong, Huirong Xiao, Zejian Ren, Shanchao Zhang
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04393v1  pdf=https://arxiv.org/pdf/2607.04393v1.pdf

Abstract:
Atomic oven generating controllable atomic beam flux plays a fundmental role in quantum gas experiments. Here, we report a new heater design that can heat up an high temperature atomic oven with fast thermal response. The new heater shows a heating rate improved by 7.65 times comparing to that of the onventional resistive heater while the crucible temperature can heated up to 1200K. With this oven, we generated a collimated ytterbium beam with flux exceeding $10^{14} \text{ atoms/s}$ at 823 K. We believe that our design offers a promising solution for shortening experimental dead time and improve the experiment efficiency in cold atom researches.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04483v1
- Title: Topological effects in the polarization of the Fulling-Rindler vacuum
- Authors: A. A. Saharian, G. V. Mirzoyan, V. S. Torosyan
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04483v1  pdf=https://arxiv.org/pdf/2607.04483v1.pdf

Abstract:
We investigate how the compactification of some spatial dimensions in Rindler spacetime affects the vacuum expectation values (VEVs) of the field squared and the energy-momentum tensor for a charged scalar field prepared in the Fulling-Rindler vacuum state. A toral compactification is considered with quasi-periodicity conditions on the field operator along the compact dimensions. The phases of these conditions are interpreted in terms of the magnetic flux enclosed by the compact dimensions. For a general number of spatial dimensions, the components of the VEVs are explicitly separated, corresponding to the expectation values in the Minkowski vacuum. As a limiting case, the VEVs are retrieved in Rindler spacetime with trivial topology. We demonstrate that, for non-zero phases in the periodicity conditions, the vacuum energy-momentum tensor exhibits off-diagonal components with indices in the compact subspace. Near the Rindler horizon, the leading terms in the asymptotic expansions of the field squared and the diagonal components of the energy-momentum tensor coincide with the corresponding VEVs in Rindler spacetime with trivial topology. The off-diagonal components of the energy-momentum tensor vanish on the Rindler horizon. For small accelerations, the difference between the VEVs in the Fulling-Rindler and Minkowski vacua is exponentially small. The exception to this is a massless field with zero phases in the periodicity conditions. In this special case, the difference decays according to a power law as a function of acceleration. As an application, we consider the VEVs near the horizon of cylindrical black holes and topological black holes with toroidal horizons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04682v1
- Title: All-optical control of coherent perfect absorption via frequency conversion
- Authors: Rikizo Ikuta, Hirokazu Kobayashi, Hiroki Takahashi
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04682v1  pdf=https://arxiv.org/pdf/2607.04682v1.pdf

Abstract:
Coherent perfect absorption (CPA) extinguishes optical fields through interference and dissipation, but conventional implementations rely on material loss that is largely fixed after fabrication. Here we demonstrate all-optically controllable CPA based on frequency conversion in a periodically poled lithium niobate waveguide resonator. Pump-driven frequency conversion couples a resonant signal field at 1581 nm in the main system to a non-resonant environmental mode at 780 nm, creating a dynamically tunable effective loss channel. The nonlinear cavity acts as a tunable lossy beamsplitter without intrinsic material absorption. Under coherent two-sided signal injection, we observe up to 92 % absorption. We further introduce environment-assisted CPA by injecting an external field into the frequency-converted environmental mode, turning the environment from a passive loss reservoir into an addressable coherent control port. Our results establish a frequency-conversion-based platform for all-optical control of dissipation in CPA, combining pump-tunable loss with environment-assisted coherent control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04766v1
- Title: Strain- and potential-controlled tunneling in monolayer MoS$_2$
- Authors: Hasna Chnafa, Rachid El Aitouni, Clarence Cortes, David Laroze, Ahmed Jellal
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04766v1  pdf=https://arxiv.org/pdf/2607.04766v1.pdf

Abstract:
We present a theoretical study of spin- and valley-resolved quantum transport in monolayer MoS$_2$ under the combined influence of mechanical strain and an external scalar potential, a combination whose simultaneous unexplored. Within an effective massive Dirac Hamiltonian that incorporates intrinsic spin--orbit coupling, strain induces valley-dependent momentum shifts that lift the degeneracy between the $K$ and $K'$ valleys and strongly modify the transport characteristics. The scalar potential modifies the tunneling spectrum, leading to pronounced changes in resonant transmission, Fabry--Pérot interference, and conductance. We show that the interplay between strain and electrostatic potential enables efficient control of both valley and spin polarization of the transmitted current. In particular, we identify a dual-knob control scheme in which the barrier width governs the frequency of conductance oscillations while strain independently controls their phase and amplitude. Furthermore, we predict electrostatic spin inversion -- a sign reversal of spin polarization achievable purely by gate tuning at finite strain, requiring no geometric reconfiguration. Depending on the strain orientation, the transmission probability and conductance can be selectively suppressed or enhanced, resulting in highly tunable valley- and spin-polarized transport. These findings demonstrate that strain and potential engineering provide orthogonal and independently operable mechanisms for controlling conductance as well as spin and valley degrees of freedom in monolayer MoS$_2$, offering promising prospects for spintronic and valleytronic device applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04834v1
- Title: Hidden Gauge Freedom in Complex-Pole Hierarchical Equations of Motion
- Authors: Tianchu Li, Andrés Montoya-Castillo
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04834v1  pdf=https://arxiv.org/pdf/2607.04834v1.pdf

Abstract:
While complex-pole hierarchical equations of motion (HEOM) have dramatically expanded the reach of numerically exact quantum dynamics simulations of open quantum systems, they suffer from numerical instabilities rooted in the non-Hermitian structure of their Liouvillian. Yet, the origin of this structure remains obscure. Here, we report a previously unknown gauge freedom in complex-pole HEOM: a continuous family of analytically equivalent Liouvillians, all encoding the same bath correlation function, whose numerical properties vary dramatically. This gauge controls both the eigenspectrum and non-normality of the hierarchy generator, revealing spectral divergence and non-normal error amplification as two distinct instability mechanisms. By optimizing this gauge, we introduce GO--HEOM, which eliminates divergences in strongly coupled Brownian oscillator environments and extends numerically exact simulations of sub-Ohmic dynamics -- including through the delocalized-to-localized quantum phase transition -- to previously inaccessible coupling strengths. Because this gauge transformation is independent of the bath-correlation decomposition scheme, our GO--HEOM becomes a general, broadly compatible strategy for accessing numerically exact quantum dynamics of open quantum systems over arbitrary coupling and highly non-Markovian regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04876v1
- Title: A Unified Electrostatic-to-Spin Framework for Asymmetric Multi-Gate CMOS Quantum Devices
- Authors: Zeheng Wang, Yan Liu, Yue Hao, Genquan Han
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04876v1  pdf=https://arxiv.org/pdf/2607.04876v1.pdf

Abstract:
In advanced complementary metal-oxide-semiconductor (CMOS) quantum chips, compact gate stacks make it difficult to connect lithographic geometry, electrostatic confinement and many-electron spin filling in one transparent model. This connection is central to design-technology co-optimization (DTCO). Here we develop a reduced-order analytical framework for asymmetric multigate silicon quantum-dot devices. Its electrostatic core, the Poisson-kernel coupled-interface Green-function (PK-GF) model, agrees with an independent finite-volume solution at the millivolt scale for the matched two-dimensional problem, without fitting to that solution. We then pass the gate-derived confinement, rather than a harmonic or fitted potential, to a spin-valley many-body calculation for a jellybean quantum dot with N = 2-17 electrons at B = 5 T. The unrestricted Hartree-Fock (UHF) solution supports occupation-dependent, Wigner-molecule-like charge localization but likely overestimates spin polarization. Complete active-space configuration interaction (CASCI) supports a low-spin branch within the tested active spaces, which aligns with the experiments. The workflow therefore connects CMOS layout, device electrostatics, and potential-determined quantum observables, providing an auditable modelling layer for CMOS-based qubit design and DTCO.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.04966v1
- Title: Super-molasses returns: All optical near-resonance laser cooling and trapping of neutral atoms from background vapor
- Authors: Matt Himsworth, Chester Camm, Max Carey, Jack Saywell, Jonathan Woods, Vilius Atkoucius, Florence Concepcion, Konstantinos Karakostas, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04966v1  pdf=https://arxiv.org/pdf/2607.04966v1.pdf

Abstract:
Laser cooled and trapped atoms have been the workhorse of atomic physics for the past four decades. The predominant method has been the highly versatile Magneto-Optical Trap. We describe an alternative laser trap involving a simple geometry of collimated laser beams that provides both a velocity and position dependent restoring force such that a dense cloud of cold atoms is formed. This technique produces similar atom number ($>10^6$) and density ($10^{10}$\,atoms/cm$^{3}$) to the Magneto-Optical Trap, albeit with \emph{no magnetic field}. The beam geometry is compatible with conventional sub-Doppler cooling techniques, allowing the trapped cloud to be cooled to $< 10~μ$K. We demonstrate the validity and robustness of the trap by capturing $^{87}$Rb atoms directly from the background vapor and provide a theoretical discussion of the underlying principles. This trap has many unique properties that make it highly suitable for quantum sensing, timing, and computing applications as well as a new tool in fundamental science and metrology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05012v1
- Title: Investigating Role of Electron Correlation Effects via Triple Excitations for Precise Evaluation of Energies and Hyperfine Structure Constants in $^{23}$Na
- Authors: Vaibhav Katyal, B. K. Sahoo
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05012v1  pdf=https://arxiv.org/pdf/2607.05012v1.pdf

Abstract:
Accurate determination of hyperfine structure constants in atomic systems provides important insight into the interplay of electron correlation and relativistic effects in the nuclear region. Although sodium (Na) is a relatively light atom, previous all-order relativistic many-body calculations of the magnetic dipole hyperfine constants for the low-lying states of $^{23}$Na show noticeable discrepancies with experiment. To address this, we calculate the ionization potentials and hyperfine structure constants of $^{23}$Na using relativistic coupled-cluster theory with explicit inclusion of triple excitations. We further incorporate corrections from the Breit interaction, quantum electrodynamics, and the Bohr-Weisskopf (BW) effect. Results from lower-order methods are also presented to assess the importance of different physical contributions across states. Our calculations demonstrate that contributions from the lower-order relativistic and BW effects play almost similar roles with the electron correlation effects, including triple excitations, and are essential for reconciling theoretical predictions with experimental observations. This study can also serve as a useful guide for understanding the role of triples in heavier alkali systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05014v1
- Title: Geometric Characteristics of Subproblems in Ising-Machine-Assisted Large Neighborhood Search
- Authors: Masashi Yamashita, Shu Tanaka
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.dis-nn; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05014v1  pdf=https://arxiv.org/pdf/2607.05014v1.pdf

Abstract:
Large-scale quadratic unconstrained binary optimization (QUBO) formulations of constrained combinatorial optimization problems often exceed the input-size limit of present Ising machines or suffer from degraded solution quality as the number of binary variables increases. Large neighborhood search (LNS) mitigates this difficulty by sequentially optimizing restricted subproblems, but the structural factors that distinguish subproblems beyond the number of binary variables remain insufficiently characterized. In this study, we examine vehicle routing problems and compare a construction based on the vehicle routes of the current solution, denoted by LNS-K, with a construction based on QUBO variables and constraint relations, denoted by LNS-Q, while controlling the number of binary variables in the subproblems. Under the tested conditions, LNS-K obtained shorter total distances than LNS-Q in the matched-size comparisons, and the position variance, a measure of the spatial spread of the selected customers, decreased during the iterations in LNS-K. These observations suggest that subproblem design for sequential optimization with Ising machines should consider not only subproblem size but also semantic and geometric structures inherited from the current solution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05020v1
- Title: Emergent cosmology and gravity from quantum time?
- Authors: Ovidiu Cristinel Stoica
- Categories: gr-qc (primary); gr-qc; math-ph; physics.hist-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05020v1  pdf=https://arxiv.org/pdf/2607.05020v1.pdf

Abstract:
Macroscopic observables allow the recovery of intrinsic dynamics from stationary quantum states. I show that, by interpreting the squared amplitude as the probability density for each definite value of intrinsic time, a curvature emerges in the time direction. For example, from the perspective of intrinsic quantum time, the Friedmann-Lemaître-Robertson-Walker cosmological model emerges from spherically symmetric stationary solutions in four-dimensional Euclidean space, without presupposing gravity. If there is no unique direction of time, curvature emerges in all spacetime dimensions, without presupposing gravity, from the variable amplitude of the stationary wavefunction alone. This opens a new possibility that general relativity or some modification of it emerges from intrinsic time observables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05190v1
- Title: Spectral-topology-induced criticality in non-Hermitian fermionic metals
- Authors: Ayan Banerjee, Julius T. Gohsrich, Flore K. Kunst
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05190v1  pdf=https://arxiv.org/pdf/2607.05190v1.pdf

Abstract:
Quantum matter emerges from the interplay of fluctuations, topology, and entanglement, which - in equilibrium - governs quantized transport, universal criticality, and topological classification. Non-Hermitian systems, widely explored in platforms ranging from electric circuits to photonics, are intrinsically out-of-equilibrium, and display fundamentally new phenomena, including complex spectra, spectral winding, exceptional topology, and non-unitary dynamics. A central challenge is understanding how the complex single-particle spectrum governs universal many-body behavior. We introduce a symmetry-protected dynamical topological index derived directly from the complex spectrum. Through the lens of algebraic topology, more specifically Morse theory, we identify critical points in the spectrum with topological defects, whose curvature and stability are protected under continuous deformations. This links spectral geometry to many-body observables, unifying non-Hermitian band topology, entanglement, and transport. We demonstrate that non-Hermitian quantum criticality in non-interacting systems is controlled by gain-and-loss-selected non-equilibrium steady states, which dynamically generate an emergent imaginary Fermi surface whose Fermi points host scale-invariant gapless modes with logarithmic entanglement scaling and algebraic correlations. Our work establishes a unified framework for non-Hermitian quantum matter, connecting spectral topology to Morse theory, revealing a topological foundation of non-equilibrium quantum criticality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05195v1
- Title: Integral representations of $f$-divergences for general von Neumann algebras
- Authors: Ricardo Correa da Silva, Markus B. Fröb, Gandalf Lechner, Leonardo Sangaletti
- Categories: math.OA (primary); math.OA; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05195v1  pdf=https://arxiv.org/pdf/2607.05195v1.pdf

Abstract:
We define and analyze hockeystick divergences and $f$-divergences for normal positive functionals on general von Neumann algebras, generalizing and unifying previous work in classical probability and finite-dimensional von Neumann algebras. All the main properties of these state distinguishability measures (including in particular monotonicity, convexity, semicontinuity, bounds, state discrimination, data processing inequality) are derived from properties of the Jordan decomposition of selfadjoint normal functionals. This is done by representing the $f$-divergences as integrals over hockeystick divergences, and their significance in quantum hypothesis testing is reviewed. The $f_0$-divergence given by the information function $f_0(t) = t \ln t$ is shown to coincide with Araki's relative entropy, extending results of Frenkel to general von Neumann algebras.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05216v1
- Title: Fast Pulses for High-Fidelity Circularization of Interacting Rydberg atoms
- Authors: Matthias Hüls, Aurore A. Young, Clément Sayrin, Michel Brune, Jean-Michel Raimond, Tommaso Calarco, Felix Motzoi, Robert Zeier, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05216v1  pdf=https://arxiv.org/pdf/2607.05216v1.pdf

Abstract:
Circular states in Rydberg atoms offer a promising platform for quantum computation, quantum simulation and quantum sensing. However, the final step of their preparation - termed as circularization, a process that involves the transfer of a large amount of angular momentum quanta to the valence electron by means of radio-frequency (RF) pulses - remains as a major bottleneck for all technological applications based on interacting circular Rydberg atoms. Even though successfully implemented to circularize an atom cloud in the dilute regime, previous efforts to speed up the circularization process have focused on the single-atom case, thereby neglecting the interactions which constitute one of the main resources for quantum simulation and computation. In this theoretical work we show how interactions between two atoms disturb the efficiency of pulses designed for single atoms and identify shifts induced by the interactions on relevant transition energies as the dominant disturbance. We demonstrate that the initial efficiency of single-atom pulses can be restored by adapting them to these shifts. Our approach is based on a simple functional form depending only on two linear parameters, which we derive analytically. The adapted pulses prepare two $^{87}$Rb atoms after $65 \,$ns in a $n=52$ circular state with a fidelity of at least $95\,\%$ for interatomic distances down to $6.5\,μ$m and for all angular configurations, while also complying experimental amplitude and frequency constraints. Finally, we show that when combining our adapted pulses with Krotov's pulse-shaping algorithm we obtain high-fidelity pulses for any pair arrangement with interatomic distances larger than $5.9\,μ$m. This work demonstrates that fast RF pulses can circularize interacting Rydberg atoms, paving the way toward their technological application.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05269v1
- Title: Excitation spectra and rank tomography of linear matrix product tangent spaces
- Authors: Otto T. P. Schmidt, Iacopo Carusotto
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05269v1  pdf=https://arxiv.org/pdf/2607.05269v1.pdf

Abstract:
We formulate a tangent-space method for algebraic varieties of matrix product states (MPS) to study excitation spectra of non-uniform quantum many-body systems with open boundary conditions. We further introduce a rank tomography of the MPS tangent space, which characterizes its expressivity in terms of particle-sector rank profiles of the underlying MPS variety. Using the Bose--Hubbard model as a benchmark, we illustrate that the method reproduces low-lying excitations and captures finite-size precursors of the Mott-insulator to superfluid transition.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05294v1
- Title: Polynomial Initial-State Jumps and Christoffel Transforms in Krylov Complexity
- Authors: Abhishek Chowdhury, Ajit Prasad Mahapatra
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05294v1  pdf=https://arxiv.org/pdf/2607.05294v1.pdf

Abstract:
State Krylov, or spread, complexity is a property of a pair $(H,\ket{K_0})$ rather than of the Hamiltonian alone. Thus, changing the initial state at fixed $H$ generally changes the Lanczos coefficients and the ordered Krylov basis. We solve this relative initial-state problem for normalized polynomial filters, $\ket{ψ_Q}=Q(H)\ket{K_0}/\sqrt{N_Q}$ with $N_Q=\langle K_0|Q(H)^\dagger Q(H)|K_0\rangle$. The filtered spectral measure is the positive polynomial modification $|Q(E)|^2\mathrm dμ(E)/N_Q$, and orthogonality turns this measure change into a finite-band transfer from reference Fourier-orthogonal-polynomial moments to shifted Krylov amplitudes. We derive exact finite sums for individual amplitudes and projected Christoffel-Darboux kernels for cumulative probabilities and spread complexity. The formulae cover confluent roots, complex seed coefficients, support loss, and terminal quotients in finite dimensions. We evaluate the construction in three canonical Jacobi families, the Heisenberg--Weyl/Charlier oscillator, the compact $SU(2)$/Krawtchouk spin, and the constant-coefficient tight-binding/Chebyshev chain, with a Hermite central-limit scaling of Charlier as a continuous-spectrum check of this Christoffel jump machinery. Finite seed families are organized by a matrix-valued parent measure whose scalar compressions recover the individual shifted problems. The fixed-inner-product construction carries over to operator Krylov complexity after the replacement \(H\mapsto\mathcal L\) and \(\ket{K_0}\mapsto O\); polynomial seeds then become nested-commutator descendants \(Q(\mathcal L)O\). The result is an exact relative calculus in which a solved cyclic problem generates a family of polynomially related initial-state dynamics without repeating Lanczos in the original Hilbert space.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.05385v1
- Title: Charge-Sector Construction of the Type-IIB Axion--Dilaton Wormhole Partition Function
- Authors: Soo-Jong Rey
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2607.05385v1  pdf=https://arxiv.org/pdf/2607.05385v1.pdf

Abstract:
I construct the Type-IIB axion--dilaton wormhole partition function from charge-sector data. In a chosen axion charge, equivalently form-field flux sector, the long-distance saddle calculation supplies a two-end operator term with coefficient matrix \(C^{ij}_ν\). The labels \(i,j\) label end-insertion operators; the labels \(A,B\) label parent universes. Reduction data \(b\) convert this matrix into scalar coefficients \(W_ν[b]\). The wormhole partition function in the theta variable is \(Z_{\rm wh}(θ;b)=\sum_νW_ν[b]\e^{iνθ}\). I analyze properties and constraints this coefficients satisfy: discrete-symmetry covariance, phase, absolute bounds, moment positivity, Cauchy--Schwarz inequalities for the unreduced coefficient matrix, complex-\(θ\) domains, charge-lattice tails, and the dilute Bessel/Skellam limit. The \(θ\)-dependence of the wormhole partition function is the Fourier transform of the charge-sector scalar coefficients.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2009.08021v4
- Title: Tutorial: Gate-based superconducting quantum computing
- Authors: Sangil Kwon, Akiyoshi Tomonaga, Gopika Lakshmi Bhai, Simon J. Devitt, Jaw-Shen Tsai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2009.08021v4  pdf=https://arxiv.org/pdf/2009.08021v4.pdf

Abstract:
In this tutorial, we introduce basic conceptual elements to understand and build a gate-based superconducting quantum computing system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2207.09368v5
- Title: Shadow Pauli Flow: Characterising Determinism in MBQCs involving Pauli Measurements
- Authors: Mehdi Mhalla, Simon Perdrix, Luc Sanselme
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2207.09368v5  pdf=https://arxiv.org/pdf/2207.09368v5.pdf

Abstract:
We introduce a new characterisation of determinism in Measurement-Based Quantum Computing (MBQC). The one-way model consists in performing local measurements over a large entangled state represented by a graph. The ability to perform an overall deterministic computation requires a correction strategy because of the non-determinism of each measurement. The existence of such a correction strategy depends on the underlying open graph, which is a description of the resource state together with the basis of the performed measurements. GFlow is a well-known graphical characterisation of robust determinism in MBQC when every measurement is performed in some specific planes of the Bloch sphere. While Pauli measurements are ubiquitous in MBQC, GFlow fails to be necessary for determinism when a measurement-based quantum computation involves Pauli measurements. Pauli Flow was designed as a generalisation of GFlow to handle MBQC with Pauli measurements, and guarantees robust determinism, however, it has been shown more recently that it fails to be a necessary condition. Our contribution is twofold. First, we demonstrate that Pauli flow is actually necessary for robust determinism in a weaker sense: given an open graph, i.e. a resource state, a deterministic computation can be driven iff it has a Pauli flow. However, the Pauli flows do not reflect all the possible correction strategies over a particular resource state, and properties like measurement order or computational depth are not necessarily reflected by a Pauli flow. Thus, to characterise determinism in full generality, we introduce a further extension called Shadow Pauli Flow that we prove necessary and sufficient for robust determinism: An MBQC is robustly deterministic if and only if its correction strategy is consistent with a Shadow Pauli flow. Furthermore, we show that Shadow Pauli flow can be computed in polynomial time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2212.03850v2
- Title: SupercheQ: Quantum Advantage for Distributed Databases
- Authors: E. R. Anschuetz, P. Gokhale, B. Tonekaboni, C. Campbell, F. T. Chong, E. D. Dahl, P. Frederick, E. B. Jones, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2212.03850v2  pdf=https://arxiv.org/pdf/2212.03850v2.pdf

Abstract:
We introduce Supercheq, a family of quantum protocols that achieves asymptotic advantage over classical protocols for checking the equivalence of files, a task also known as fingerprinting. The first variant, Supercheq-EE (Efficient Encoding), uses $n$ qubits to verify files with $2^{O(n)}$ bits -- an exponential advantage in communication complexity (i.e.~bandwidth, often the limiting factor in networked applications) over the best possible classical protocol in the simultaneous message passing setting. Moreover, Supercheq-EE can be gracefully scaled down for implementation on circuits with $\mathrm{poly}(n^\ell)$ depth to enable verification for files with $O(n^\ell)$ bits for arbitrary constant $\ell$. The quantum advantage is achieved by random circuit sampling, thereby potentially endowing circuits from recent quantum supremacy and quantum volume experiments with a practical application. We validate Supercheq-EE's performance at scale through GPU simulation motivated by Infleqtion's Sqale neutral atom QPU gateset. The second variant, Supercheq-IE (Incremental Encoding), also achieves arbitrary-polynomial advantage in fingerprint size ($n$ qubits to verify files with size $O(n^{\ell})$ bits), while supporting incremental updates to the fingerprint using only a constant number of $(\ell-1)$-qubit gates. Moreover, Supercheq-IE at $\ell=2$ ($\geq 3$) only requires Clifford gates (gates in the $\ell-1$ level of the Clifford hierarchy), ensuring relatively modest overheads for error-corrected implementation. We experimentally demonstrate proof-of-concepts on quantum hardware from Diraq (spin qubit) and IBM (superconducting). We envision Supercheq could be deployed in distributed data settings, accompanying replicas of important databases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2309.15863v4
- Title: Relativistic entanglement in muon decay
- Authors: S. Carneiro, F. C. Sobrinho
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2309.15863v4  pdf=https://arxiv.org/pdf/2309.15863v4.pdf

Abstract:
We discuss the time evolution of quantum entanglement in the presence of non-collapsing interactions. In particular, the entanglement between the products of a muon decay in a magnetic field is revisited. It results from angular momentum conservation and leads to an anomaly in the measured muon g-factor in precise agreement with that reported by the Brookhaven and Fermilab experiments, alleviating the present tension between data-driven and lattice theoretical values.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2401.03090v3
- Title: Generalized Stein's lemma and asymptotic equipartition property for subalgebra entropies
- Authors: Li Gao, Mizanur Rahaman
- Categories: quant-ph (primary); quant-ph; math-ph; math.FA; math.OA
- Links: abs=https://arxiv.org/abs/2401.03090v3  pdf=https://arxiv.org/pdf/2401.03090v3.pdf

Abstract:
The quantum Stein's lemma is a fundamental result of quantum hypothesis testing in the context of distinguishing two quantum states. The ``generalized quantum Stein's lemma'' asserts that this result is true in a general framework where one of the states is replaced by convex sets of quantum states. Formulated in 2008, the generalized Stein's lemma is one of the most influential results in quantum information theory that links resource convertibility to quantum hypothesis testing. However, in 2023 a logical gap was found in the original proof of the generalized Stein's lemma and since then there has been an enormous effort in resolving this issue. In this work, we show that the assertion of the generalized Stein's lemma is true for the setting where the second hypothesis is the state space of any finite-dimensional subalgebra. This is obtained through a strong asymptotic equipartition property for smooth subalgebra entropies that applies to any fixed smoothing parameter. In fact, we obtain a stronger second-order analysis for the hypothesis-testing relative entropy in this setting. As an application in resource theory, we show that the relative entropy of a subalgebra is the asymptotic dilution cost under suitable operations. This provides a possible route to establishing a connection between different quantum resources based on subalgebras.   After finishing this article, we learned that there are two independent works (by Hayashi-Yamasaki, and Lami) that finally resolve the generalized Stein's lemma in its full generality. However, we provide an alternative proof in a special case using different operator-algebraic techniques that may be of independent interest.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2405.20381v2
- Title: Classical and Quantum Properties of the Spin-Boson Dicke Model: Chaos, Localization, and Scarring
- Authors: David Villaseñor, Saúl Pilatowsky-Cameo, Jorge Chávez-Carlos, Miguel A. Bastarrachea-Magnani, Sergio Lerma-Hernández, Lea F. Santos, Jorge G. Hirsch
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; nlin.CD
- Links: abs=https://arxiv.org/abs/2405.20381v2  pdf=https://arxiv.org/pdf/2405.20381v2.pdf

Abstract:
This review article describes major developments associated with the Dicke model, from its introduction in the 1950s to explain the transition from a normal to a superradiant phase to its modern applications in quantum many-body physics. Over the decades, this interacting spin-boson model has played a central role in the study of collective light-matter interactions, chaos, and quantum phase transitions. We focus on properties and phenomena that are best understood when seen from both the classical and quantum perspectives, with particular emphasis on the emergence of chaos, localization, and scarring. While our primary emphasis is on the isolated model, we also discuss recent advances in the open Dicke model, where environmental couplings are needed for describing realistic experimental platforms and exploring new regimes of quantum dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2410.21201v2
- Title: Sample-Optimal Quantum Estimators for Pure-State Trace Distance and Fidelity via Samplizer
- Authors: Qisheng Wang, Zhicheng Zhang
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.DS; cs.IT
- Links: abs=https://arxiv.org/abs/2410.21201v2  pdf=https://arxiv.org/pdf/2410.21201v2.pdf

Abstract:
We settle the problem of estimating the trace distance and (square root) fidelity between $n$-qubit pure quantum states to within additive error $\varepsilon$, given their independent samples, which was raised as an open question by Wang (IEEE Trans. Inf. Theory 2024). This is achieved by a quantum algorithm with optimal sample complexity $Θ(1/\varepsilon^2)$, improving the long-standing folklore with sample complexity $O(1/\varepsilon^4)$. At the heart of our algorithm is a samplized phase estimation of the product of two Householder reflections. This is realized by an improved (multi-)samplizer for pure states, through which any quantum query algorithm using $Q$ queries to the reflection operator $I - 2|ψ\rangle\!\langleψ|$ can be converted to a $δ$-close (in the diamond norm distance) quantum sample algorithm using $Θ(Q^2/δ)$ samples of the state $|ψ\rangle$. This samplizer for pure states is also shown to be optimal.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2411.04730v4
- Title: Cloning Games, Black Holes and Cryptography
- Authors: Alexander Poremba, Seyoon Ragavan, Vinod Vaikuntanathan
- Categories: quant-ph (primary); quant-ph; cs.CR; hep-th
- Links: abs=https://arxiv.org/abs/2411.04730v4  pdf=https://arxiv.org/pdf/2411.04730v4.pdf

Abstract:
In this work, we introduce a new toolkit for analyzing cloning games, a notion that captures stronger and more quantitative versions of the celebrated quantum no-cloning theorem. This framework allows us to analyze a new cloning game based on binary phase states. Our results provide evidence that these games may be able to overcome important limitations of previous candidates based on BB84 states and subspace coset states: in a model where the adversaries are restricted to making a single oracle query, we show that the binary phase variant is $t$-copy secure when $t=o(n/\log n)$. Moreover, for constant $t$, we obtain the first optimal bounds of $O(2^{-n})$, asymptotically matching the value attained by a trivial adversarial strategy. We also show a worst-case to average-case reduction which allows us to show the same quantitative results for the new and natural notion of Haar cloning games.   Our analytic toolkit, which we believe will find further applications, is based on binary subtypes and uses novel bounds on the operator norms of block-wise tensor products of matrices. To illustrate the effectiveness of these new techniques, we present two applications: first, in black-hole physics, where our asymptotically optimal bound offers quantitative insights into information scrambling in idealized models of black holes; and second, in unclonable cryptography, where we (a) construct succinct unclonable encryption schemes from the existence of pseudorandom unitaries, and (b) propose and provide evidence for the security of multi-copy unclonable encryption schemes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2411.06822v4
- Title: Efficient Classical Computation of Single-Qubit Marginal Measurement Probabilities to Simulate Certain Classes of Quantum Algorithms
- Authors: Santana Yuda Pradata, Muhammad 'Anin Nabail 'Azhiim, Hendry Minfui Lim, Wiwit Suryanto, Ahmad Ridwan Tresna Nugraha, Muhammad Alfian Amrizal, Hiroyuki Takizawa
- Categories: quant-ph (primary); quant-ph; cs.DM; cs.DS
- Links: abs=https://arxiv.org/abs/2411.06822v4  pdf=https://arxiv.org/pdf/2411.06822v4.pdf

Abstract:
Classical simulations of quantum circuits are essential for verifying and benchmarking quantum algorithms, particularly for large circuits, where computational demands increase exponentially with the number of qubits. Among available methods, the classical simulation of quantum circuits inspired by density functional theory -- the so-called QC-DFT method, shows promise for large circuit simulations as it approximates the quantum circuits using single-qubit reduced density matrices to model multi-qubit systems. However, the QC-DFT method performs very poorly when dealing with multi-qubit gates. In this work, we introduce a novel CNOT "functional" that leverages neural networks to generate unitary transformations, effectively mitigating the simulation errors observed in the original QC-DFT method. For random circuit simulations, our modified QC-DFT enables efficient computation of single-qubit marginal measurement probabilities, or single-qubit probability (SQPs), and achieves lower SQP errors and higher fidelities than the original QC-DFT method. Despite some limitations in capturing full entanglement and joint probability distributions, we find potential applications of SQPs in simulating Shor's and Grover's algorithms for specific solution classes. These findings advance the capabilities of classical simulations for some quantum problems and provide insights into managing entanglement and gate errors in practical quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2411.10638v2
- Title: Nonlinear optical charge state switching and pumping to a diamond NV center dark state
- Authors: Prasoon K. Shandilya, Vinaya K. Kavatamane, Sigurd Flågan, David P. Lake, Denis Sukachev, Paul E. Barclay
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.optics
- Links: abs=https://arxiv.org/abs/2411.10638v2  pdf=https://arxiv.org/pdf/2411.10638v2.pdf

Abstract:
The photodynamics of diamond nitrogen-vacancy (NV) centers limits their performance in many quantum technologies. Quenching of photoluminescence, which degrades NV readout, is commonly ascribed to a dark state that is not fully understood. Using a nanoscale cavity to generate intense infrared fields that quench NV emission nonlinearly with field intensity, we show that the dark state is accessed by two-photon pumping into the $^4\!A_2$ quartet state of the neutrally charged NV (NV$^0$). We constrain this state's energy relative to the NV$^0$ ground-state ($^2\!E$) to ${<}0.58$\,eV and the recombination energy threshold to the NV$^-$ ground state ($^3\!A_2$) to $\leq2.33\,\text{eV}$. Furthermore, we estimate the intrinsic lifetime of $^4\!A_2$ state to be $1.78-6.06\,μ\text{s}$ and show that accessing this state allows sensing of local infrared fields. This new understanding will allow predictions of the limits of NV technologies reliant upon intense fields, including levitated systems, spin--optomechanical devices, and absorption--based magnetometers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2411.11954v2
- Title: Learning complexity gradually in quantum machine learning models
- Authors: Erik Recio-Armengol, Franz J. Schreiber, Jens Eisert, Carlos Bravo-Prieto
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2411.11954v2  pdf=https://arxiv.org/pdf/2411.11954v2.pdf

Abstract:
Quantum machine learning is an emergent field that continues to draw significant interest for its potential to offer improvements over classical algorithms in certain areas. However, training quantum models remains a challenging task, largely because of the difficulty in establishing an effective inductive bias when solving high-dimensional problems. In this work, we propose a training framework that prioritizes informative data points over the entire training set. This approach draws inspiration from classical techniques such as curriculum learning and hard example mining to introduce an additional inductive bias through the training data itself. By selectively focusing on informative samples, we aim to steer the optimization process toward more favorable regions of the parameter space. This data-centric approach complements existing strategies such as warm-start initialization methods, providing an additional pathway to address performance challenges in quantum machine learning. We provide theoretical insights into the benefits of prioritizing informative data for quantum models, and we validate our methodology with numerical experiments on selected recognition tasks of quantum phases of matter. Our findings indicate that this strategy could be a valuable approach for improving the performance of quantum machine learning models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2412.12558v4
- Title: The Jacobi Factoring Circuit: Quantum Factoring with Near-Linear Gates and Sublinear Space and Depth
- Authors: Gregory D. Kahanamoku-Meyer, Seyoon Ragavan, Vinod Vaikuntanathan, Katherine Van Kirk
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2412.12558v4  pdf=https://arxiv.org/pdf/2412.12558v4.pdf

Abstract:
We present a compact quantum circuit for factoring a large class of integers, including some whose classical hardness is expected to be equivalent to RSA (but not including RSA integers themselves). Most notably, we factor $n$-bit integers of the form $P^2 Q$ with $\log Q = Θ(n^a)$ for $a \in (2/3, 1)$ in space and depth sublinear in n (specifically, $\tilde{O}(\log Q)$) using $\tilde{O}(n)$ quantum gates; for these integers, no known classical algorithms exploit the relatively small size of $Q$ to run asymptotically faster than general-purpose factoring algorithms. To our knowledge, this is the first polynomial-time circuit to achieve sublinear qubit count for a classically-hard factoring problem.   Our circuit builds on the quantum algorithm for squarefree decomposition discovered by Li, Peng, Du, and Suter (Nature Scientific Reports 2012), which relies on computing the Jacobi symbol in quantum superposition. The technical core of our contribution is a new space-efficient quantum algorithm to compute the Jacobi symbol of $A$ mod $B$, in the regime where $B$ is classical and much larger than $A$. Our circuit for computing the Jacobi symbol generalizes to related problems such as computing the greatest common divisor and modular inverses, and thus could be of independent interest.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2412.19176v3
- Title: Variational Quantum Eigensolver: A Comparative Analysis of Classical and Quantum Optimizer Methods
- Authors: Duc-Truyen Le, Vu-Linh Nguyen, Cong-Ha Nguyen, Quoc-Hung Nguyen, Van-Duy Nguyen
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2412.19176v3  pdf=https://arxiv.org/pdf/2412.19176v3.pdf

Abstract:
In this study, we investigated the Variational Quantum Eigensolver (VQE) application for the Ising model as a testbed model, in which we thoroughly delved into several optimizers, both classical and quantum, and analyzed the extent to which each of these methods would offer a benefit. We then investigated a new combinatorial optimization scheme, termed QN-SPSA+PSR, in which the Fubini-Study metric is approximated within the Quantum Natural Gradient (QN) framework, with its inner gradient estimated by the Simultaneous Perturbation Stochastic Approximation (SPSA), while the outer gradient of the cost function is evaluated exactly by the Parameter-Shift Rule (PSR). The QN-SPSA+PSR method integrates the QN-SPSA computational efficiency with the precise gradient computation of the PSR, improving the stability of QN-SPSA-based and convergence speed per parameter update while maintaining low computational consumption. Our results provide a potential performance improvement in the VQAs' optimization subroutine, even in Quantum Machine Learning's optimization section, and enhance viable paths toward efficient quantum simulations on Noisy Intermediate-Scale Quantum Computing (NISQ) devices. Additionally, we also conducted a detailed study of quantum circuit ansatz structures in order to find the one that would work best with the Ising model and NISQ, in which we utilized the properties of the investigated model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2501.16419v4
- Title: Near-Optimal Parameter Tuning of Level-1 QAOA for Ising Models
- Authors: V Vijendran, Dax Enshan Koh, Eunok Bae, Hyukjoon Kwon, Ping Koy Lam, Syed M Assad
- Categories: quant-ph (primary); quant-ph; cs.DS; cs.ET; math.OC
- Links: abs=https://arxiv.org/abs/2501.16419v4  pdf=https://arxiv.org/pdf/2501.16419v4.pdf

Abstract:
The Quantum Approximate Optimisation Algorithm (QAOA) tackles combinatorial optimisation problems by encoding their solutions into the ground state of an Ising Hamiltonian prepared by a $p$-level parameterised circuit, with the angles tuned classically. Parameter optimisation is widely regarded as a central bottleneck, even for the shallowest circuits. Focusing on QAOA at $p=1$ (QAOA$_1$), we show that tuning the two angles $(γ, β)$ for weighted Ising models is not a black-box search but a structured signal-processing problem. We prove that the QAOA$_1$ expectation value is a partial Fourier series in $γ$ whose frequencies are determined explicitly by the problem's couplings and fields, giving instance-wise bandwidth bounds and, via the Nyquist--Shannon theorem, the sampling resolution needed to avoid the aliasing that causes coarse-grid searches to return spurious optima. We then eliminate the mixer angle analytically, computing $β^*(γ)$ in closed form to reduce the search to one dimension, and apply a subdivision algorithm that locates the globally optimal $γ$ in polynomial time with a certificate of optimality when the weights are commensurable and bounded. For regular weighted graphs, we further prove the conventional wisdom that the globally optimal $γ^* \in \mathbb{R}^+$ concentrates near zero and coincides with the first local optimum, giving a rigorous account of the empirical success of small-angle initialisation and allowing gradient descent to replace exhaustive line searches. Validated within Recursive QAOA (RQAOA) on weighted instances of 128 and 256 qubits, our method consistently outperforms both coarsely optimised RQAOA and semidefinite programming.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2504.14499v3
- Title: Limitation of maximally entangled probes for single-shot distinguishability of unitaries
- Authors: Satyaki Manna, Anandamay Das Bhowmik, Debashis Saha
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.14499v3  pdf=https://arxiv.org/pdf/2504.14499v3.pdf

Abstract:
There have been many instances where the maximally entangled state as a probe acts better than the product and the non-maximally entangled states in the task of distinguishing quantum channels. We provide a proof that for single-shot discrimination of two unitary channels, entangled and product states are operationally equivalent. But we identify pairs of unitaries that are perfectly distinguishable using a non-maximally entangled state, but not with a maximally entangled one. This contrast becomes more pronounced when the number of unitaries exceeds two. In every dimension $\geqslant 3$, we show that there exists a class of unitaries that are indistinguishable under maximally entangled probes, yet perfectly distinguishable using product or non-maximally entangled inputs. Another interesting set of unitaries in every dimension $\geqslant 3$ has been presented where only non-maximally entangled state acts as the successful probe, while product states and maximally entangled states cannot.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2504.15698v3
- Title: Shallow randomized measurement in noisy quantum devices
- Authors: Gyungmin Cho, Dohun Kim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.15698v3  pdf=https://arxiv.org/pdf/2504.15698v3.pdf

Abstract:
Quantum hardware is steadily improving, but near-term quantum devices remain limited by noise and circuit depth. This motivates measurement protocols that can use shallow-depth circuits while remaining robust to experimental errors. In this work, we study the advantages of shallow randomized measurements over non-entangling single-qubit measurements for learning properties of quantum states. Although shallow measurements have shown advantages in selected applications, their usefulness across different learning tasks has not been systematically understood. Here, we develop a theoretical framework based on Clifford ensembles that incorporates shallow measurements into derandomized measurements, multi-shot protocols, common randomized measurements, error-mitigated estimators, and hybrid quantum-classical learning. Finally, we validate these results on IBM quantum hardware in experiments with up to 40 qubits and 46 layers of two-qubit gates. These results indicate that shallow-depth measurements can provide practical benefits on noisy quantum devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2504.18426v2
- Title: PT-symmetry breaking phase transitions in an LMG dimer
- Authors: Simon Kothe, Christopher Oliver, Peter Kirton
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2504.18426v2  pdf=https://arxiv.org/pdf/2504.18426v2.pdf

Abstract:
The open Lipkin-Meshkov-Glick (LMG) model provides a prototype of a dissipative phase transition which can be analyzed using mean-field theory. By combining the physics of this model with those of a quantum analogue of a parity-time reversal symmetry breaking transition we analyze the steady state phase diagram of a pair of coupled LMG models. Their competition generates a complex phase diagram with multiple steady-state phases and emergent dynamical regimes absent from either constituent model, including chaos characterized by the maximum Lyapunov exponent. We show that the effects predicted from mean-field theory survive in the full quantum model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2505.08460v3
- Title: Landau levels in a time-dependent magnetic field: the Madelung fluid perspective
- Authors: Nicolas Perez, Eyal Heifetz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.08460v3  pdf=https://arxiv.org/pdf/2505.08460v3.pdf

Abstract:
We revisit the quantum dynamics of a charged particle in a time-dependent magnetic field, a fundamental problem exhibiting rich non-adiabatic behaviour, from the complementary perspective of the Madelung fluid formulation. We first analyse the system within standard quantum mechanics using perturbation theory around the Landau levels, and then address the same problem through the Madelung perspective. We show that the hydrodynamic formulation not only yields an intuitive derivation of the exact solution, it also provides a clear physical interpretation of non-adiabatic quantum evolution in terms of mechanical energy transfers. In this picture, the sloshing oscillations of the wave function arise from deviations from the force balance between the magnetic Lorentz force and the gradient of the Bohm potential within the Landau levels. More broadly, our study illustrates how the Madelung approach reveals unexpected analogies between quantum dynamics and phenomena familiar from geophysical fluid dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2505.13599v4
- Title: Decoding across transversal Clifford gates in the surface code
- Authors: Marc Serra-Peralta, Mackenzie H. Shaw, Barbara M. Terhal
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.13599v4  pdf=https://arxiv.org/pdf/2505.13599v4.pdf

Abstract:
Transversal logical gates offer the opportunity for fast and low-noise logic, particularly when interspersed by a single round of parity check measurements of the underlying code. Using such circuits for the surface code requires decoding across logical gates, complicating the decoding task. We show how one can decode across an arbitrary sequence of transversal gates for the unrotated surface code, using a fast "logical observable" minimum-weight-perfect-matching (MWPM) based decoder, and benchmark its performance in Clifford circuits under circuit-level noise. We propose windowed logical observable matching decoders to address the problem of fully efficient decoding: our basic windowed decoder is computationally efficient under the restriction of quiescent (slow) resets. Our 'advanced' two-step windowed decoder can be computationally inefficient but allows fast resets. For both windowed decoders we identify errors which scale sublinearly in $d$ - depending on the structure of the circuit - which can lead to logical failure, and we propose methods to adapt the decoding to remove such failures. Our work highlights the complexity and interest in efficient decoding of fast logic for the surface code.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2506.04687v2
- Title: Joint Optimization of Electric Vehicle Routes and Charging Locations through Learning Charge Constraints Using QUBO Solvers
- Authors: Akihisa Okada, Keisuke Otaki, Hiroaki Yoshida
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.04687v2  pdf=https://arxiv.org/pdf/2506.04687v2.pdf

Abstract:
Optimal routing problems of electric vehicles (EVs) have attracted much attention in recent years, and installation of charging stations is an important issue for EVs. Hence, we focus on the joint optimization of the location of charging stations and the routing of EVs. When routing problems are formulated in the form of quadratic unconstrained binary optimization (QUBO), specialized solvers such as quantum annealers are expected to provide optimal solutions with high speed and accuracy. However, battery capacity constraints make it hard to formulate into QUBO form without a large number of auxiliary qubits. Here, we propose a sequential optimization method utilizing the Bayesian inference and QUBO solvers, in which the battery capacity constraints are automatically learned. This method enables us to optimize the number and location of charging stations and the routing of EVs with a small number of searches. Applying this method to a routing problem of 20 locations, we observed consistent convergence toward battery-feasible solutions across independent runs, demonstrating stable learning behavior of the proposed framework. Small-scale validation experiments using exhaustive enumeration show that the framework reliably discovers feasible configurations close to the global optimum, while runtime and QUBO-size analyses clarify its computational characteristics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2507.19801v2
- Title: Fringe visibility and which-way information in Young's double slit experiments with light scattered from single atoms
- Authors: Hanzhen Lin, Yu-Kun Lu, Vitaly Fedoseev, Yoo Kyung Lee, Jiahao Lyu, Wolfgang Ketterle
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2507.19801v2  pdf=https://arxiv.org/pdf/2507.19801v2.pdf

Abstract:
Young's double slit experiment has often been used to illustrate the concept of complementarity in quantum mechanics. If information can in principle be obtained about the path of the photon, then the visibility of the interference fringes is reduced or even destroyed. This Gedanken experiment discussed by Bohr and Einstein can be realized when the slit is replaced by individual atoms sensitive to the transferred recoil momentum of a photon which "passes through the slit". Early pioneering experiments were done with trapped ions and atom pairs created via photo-dissociation. Recently, it became possible to perform interference experiments with single neutral atoms cooled to the absolute ground state of a harmonic oscillator potential. The slits are now single atoms representing a two-level system, and the excitation in the harmonic oscillator potential is the which-way marker. In this note, we analyze and generalize two recent experiments performed with single atoms and emphasize the different ways they record which-way information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2507.21036v3
- Title: Quantum optical shallow networks
- Authors: Simone Roncallo, Angela Rosy Morgillo, Seth Lloyd, Chiara Macchiavello, Lorenzo Maccone
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.21036v3  pdf=https://arxiv.org/pdf/2507.21036v3.pdf

Abstract:
Classical shallow networks are universal approximators. Given a sufficient number of neurons, they can reproduce any continuous function to arbitrary precision, with a resource cost that scales linearly in both the input size and the number of trainable parameters. In this work, we present a quantum optical protocol that implements a shallow network with an arbitrary number of neurons. Both the input data and the parameters are encoded into single-photon states. Leveraging the Hong-Ou-Mandel effect, the network output is determined by the coincidence rates measured when the photons interfere at a beam splitter, with multiple neurons prepared as a mixture of single-photon states. Remarkably, once trained, our model requires constant optical resources regardless of the number of input features and neurons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2507.23005v3
- Title: Detecting quantum non-Gaussianity with a single quadrature
- Authors: Clara Wassner, Jack Davis, Sacha Cerf, Ulysse Chabaud, Francesco Arzani
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.23005v3  pdf=https://arxiv.org/pdf/2507.23005v3.pdf

Abstract:
Full reconstruction of quantum states from measurement samples is often a prohibitively complex task, both in terms of the experimental setup and the scaling of the sample size with the system. This motivates the relatively easier task of certifying application-specific quantities using measurements that are not tomographically complete, i.e. that provide only partial information about the state related to the application of interest. Here, we focus on simplifying the measurements needed to certify non-Gaussianity in bosonic systems, a resource related to quantum advantage in various information processing tasks. We show that the statistics of a single quadrature measurement, corresponding to standard homodyne detection in quantum optics, can witness arbitrary degrees of non-Gaussianity as quantified by stellar rank. Our results are based on a version of Hudson's theorem for wavefunctions, proved in a companion paper [arXiv:2507.23468], revealing that the zeros in a homodyne distribution are signatures of quantum non-Gaussianity and higher stellar ranks. The validity of our witnesses is supported by a technical result showing that sets of states with bounded energy and finite stellar rank are compact. We provide an analysis of sample complexity, noise robustness, and experimental prospects. Our work drastically simplifies the setup required to detect quantum non-Gaussianity in bosonic quantum states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2508.01362v2
- Title: Proof of quantum to classical transition for the center of mass of quantum many body systems
- Authors: Marco Bilardello
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.01362v2  pdf=https://arxiv.org/pdf/2508.01362v2.pdf

Abstract:
The classical limit of quantum mechanics is investigated, by focusing on the study of the center of mass of a many-body system where each particle is described by quantum mechanics. We study how, in the limit when the number of particles diverges and under quite general assumptions, the center of mass of the system is not anymore described by quantum mechanics but by classical mechanics: the center of mass of the system becomes with a well-defined position and momentum, the state of the center of mass is fully determined by its position and by its momentum, and its dynamics is given by the classical law of dynamics. In order to get this result, three assumptions on the many-body system are necessary: the total mass of the system must be much larger than the mass of each particle composing the system; at most a finite number of particles has non-zero correlation in position with an infinite number of particles; finally, when the number of particles composing the system diverge, the variance in position of each particle converges to a finite value. These assumptions are commonly realized for a macroscopic solid and liquid systems. The results obtained in this paper show how the classical limit of quantum mechanics can be naturally achieved without the need to modify quantum mechanics, without the need to have an external environment and without the need of changing the interpretations of quantum mechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2508.17471v3
- Title: Two-stage Distributed Variational Quantum Eigensolver Software for QUBO and Quadratic Programming
- Authors: Milad Hasanzadeh, Amin Kargarian
- Categories: quant-ph (primary); quant-ph; eess.SY; math.OC
- Links: abs=https://arxiv.org/abs/2508.17471v3  pdf=https://arxiv.org/pdf/2508.17471v3.pdf

Abstract:
This paper proposes a two-stage distributed variational quantum eigensolver (DVQE) software for solving quadratic unconstrained binary optimization (QUBO) problems and bounded constrained quadratic programming (QP) problems. The proposed DVQE solver supports both monolithic and distributed quantum-circuit execution and evaluates QUBO objectives directly from measured bitstrings. To improve variational training, DVQE uses a two-stage procedure that combines metaheuristic warm-start initialization with sampling-based variational refinement. The software supports several metaheuristic approaches as warm-start strategies. To extend QUBO-based quantum optimization to constrained continuous problems, this paper also develops a sequential QP to QUBO framework, called QQP. QQP first scales the bounded continuous variables to a normalized box and then handles equality and inequality constraints using a Powell-Hestenes-Rockafellar (PHR) augmented-Lagrangian formulation. Under a fixed PHR active region, the constrained augmented-Lagrangian subproblem becomes an ordinary bounded quadratic problem. QQP then solves this bounded quadratic problem through repeated local one-bit QUBO reformulations, where each binary variable represents a local up/down move of one continuous variable inside a trust region. In this way, QQP converts a constrained continuous QP into a sequence of QUBO subproblems without introducing slack variables. Each local QUBO subproblem can be solved using either a classical QUBO backend or the proposed DVQE solver. Numerical experiments evaluate the proposed software on QUBO and QP test problems. The results show that the distributed DVQE framework can recover high-quality QUBO solutions, and that the QQP framework can solve bounded constrained QP instances with small optimality, feasibility, and solution gaps.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2509.14026v2
- Title: Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks
- Authors: Jiun-Cheng Jiang, Morris Yu-Chao Huang, Tianlong Chen, Hsi-Sheng Goan
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2509.14026v2  pdf=https://arxiv.org/pdf/2509.14026v2.pdf

Abstract:
Variational quantum circuits (VQCs) are central to quantum machine learning, while recent progress in Kolmogorov-Arnold networks (KANs) highlights the power of learnable activation functions. We unify these directions by introducing the quantum variational activation function (QVAF), a general framework in which parameterized quantum circuits serve as learnable activation functions; in this work we study an efficient single-qubit instantiation called DatA Re-Uploading ActivatioN (DARUAN). We show that DARUAN with trainable data-preprocessing weights can realize an exponentially growing accessible frequency support with the number of re-uploading repetitions; for an explicit geometric choice of these weights, this gives a capacity-level exponential parameter reduction relative to independently parameterized Fourier activations. Embedding DARUAN into KAN yields the quantum-inspired Kolmogorov-Arnold Network (QKAN), which retains the interpretability of the KAN architecture while improving parameter efficiency, expressivity, and generalization. We further introduce layer extension and the hybrid QKAN (HQKAN) architecture to improve scalability and computational efficiency, enabling QKAN modules to act as compact replacements for multi-layer perceptrons (MLPs) in large-scale models. We provide theoretical analysis and extensive experiments on function regression, image classification, and autoregressive generative language modeling, demonstrating the efficiency and scalability of QKANs. Because the single-qubit circuits are efficiently simulable on classical quantum simulators, QKANs have quantum-inspired advantage in parameter efficiency and training stability; DARUANs and QKANs serve as present-day validation of the QVAF concept, and the trained DARUANs are directly executable and feasible on current noisy intermediate-scale quantum (NISQ) hardware for inference validation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2509.24028v2
- Title: The gauge freedom in the Aharonov-Casher theorem: The problem in two and one dimensions
- Authors: Lucas Sourrouille
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.24028v2  pdf=https://arxiv.org/pdf/2509.24028v2.pdf

Abstract:
In this note, we investigate the role of gauge freedom in the Aharonov-Casher theorem in one and two dimensions. In particular, we analyze the asymptotic behavior of the gauge freedom. We show that in two dimensional space the gauge field is uniquely determined, whereas in one dimensional space there exists a gauge freedom that enables an infinite family of equivalent gauges. This freedom is determined by a constant k. However, the number $k$ must be restricted in order to guarantee the existence of a normalizable zero mode. This restriction is determined by the inequaly $|k| < \frac{1}{2} \int dx B(x)$, where $B(x)$ is a scalar field localized in a finite region of space. We show that this condition is equivalent to the gauge field taking opposite-sign values at $+\infty$ and $-\infty$. Finally, we illustrate these results with an explicit example.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2509.25345v2
- Title: Fast quantum computation with all-to-all Hamiltonians
- Authors: Chao Yin
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2509.25345v2  pdf=https://arxiv.org/pdf/2509.25345v2.pdf

Abstract:
All-to-all interactions arise naturally in many areas of theoretical physics and across diverse experimental quantum platforms, motivating a systematic study of their information-processing power. Assuming each pair of qubits interacts with $\mathrm{O}(1)$ strength, programmable time-dependent all-to-all Hamiltonians can simulate arbitrary all-to-all quantum circuits, performing quantum computation in time proportional to the circuit depth. We show that this naive correspondence is far from optimal: all-to-all Hamiltonians can process information on much shorter timescales.   First, we prove that any two-qubit gate can be simulated by all-to-all Hamiltonians on $N$ qubits in time $\mathrm{O}(1/N)$ (up to factor $N^δ$ with an arbitrarily small constant $δ>0$), with polynomially small error $1/\mathrm{poly}(N)$. Immediate consequences include: 1) Certain $\mathrm{O}(N)$-qubit unitaries and entangled states, such as the multiply-controlled Toffoli gate and the GHZ and W states, can be generated in $\mathrm{O}(1/N)$ time; 2) Information could propagate in a fast way that saturates known Lieb-Robinson bounds in strongly power-law interacting systems.   Our second main result proves that any depth-$D$ quantum circuit can be simulated by a randomized Hamiltonian protocol in time $T=\mathrm{O}(D/\sqrt{N})$, with constant space overhead and polynomially small error. Applied to circuit ensembles forming unitary designs and pseudorandom unitaries, this simulation gives an operational proof of the fast scrambling conjecture for dense Hamiltonians.   The techniques underlying our results depart fundamentally from the existing literature on parallelizing commuting gates: We rely crucially on non-commuting Hamiltonians and draw on diverse physical ideas.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2510.08432v3
- Title: Parallel Spooky Pebbling Makes Regev Factoring More Practical
- Authors: Gregory D. Kahanamoku-Meyer, Seyoon Ragavan, Katherine Van Kirk
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2510.08432v3  pdf=https://arxiv.org/pdf/2510.08432v3.pdf

Abstract:
Pebble games, an abstraction from classical reversible computing, have found use in the design of quantum circuits for inherently sequential tasks. Gidney showed that allowing Hadamard basis measurements during pebble games can dramatically improve costs -- an extension termed "spooky pebble games" because the measurements leave temporary phase errors called ghosts. Separately, previous work by Blocki et al. studied the benefits of parallelism in pebble games. In this work we define and study parallel spooky pebble games, showing that parallelism and spookiness can yield impressive gains when used together. First, we show by construction that a line graph of length $\ell$ can be pebbled in depth $2\ell$ (exactly optimal) using space $\leq 2.47\log \ell$. Then, to explore pebbling schemes using even less space, we use a highly optimized $A^*$ search implemented in Julia to find the lowest-depth parallel spooky pebbling possible for a range of concrete line graph lengths $\ell$ given a constant number of pebbles $s$.   We then show that these techniques can significantly reduce the cost of the arithmetic in Regev's factoring algorithm. For example, we find that 4096-bit integers $N$ can be factored in multiplication depth 193, which outperforms the 680 required of previous variants of Regev and the 444 reported by Ekerå and Gärtner for Shor's algorithm. While the space required for Shor's algorithm is considerably less than any variant of Regev's algorithm including ours, and thus Shor likely remains the best candidate for the first quantum factorization of large integers, our results show that implementations of Regev's algorithm are far from fully optimized, and Regev's algorithm may have practical importance in the future. We also believe our pebbling techniques are applicable in quantum cryptanalysis beyond integer factorization, and in quantum circuit compilation more broadly.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2510.12887v3
- Title: Many-body post-processing of density functional calculations using the variational quantum eigensolver for Bader charge analysis
- Authors: Erik Schultheis, Alexander Rehn, Gabriel Breuil
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2510.12887v3  pdf=https://arxiv.org/pdf/2510.12887v3.pdf

Abstract:
Quantum chemistry and condensed matter physics are among the most promising applications of quantum computers. Further, estimating properties of a material is crucial to evaluate its industrial applications. To investigate charge distributions of weakly and strongly correlated systems we calculate Bader charges for various periodic systems by solving many-body Hamiltonians using the variational quantum eigensolver. The Hamiltonians are computed from Kohn-Sham orbitals obtained from a prior DFT calculation. We first demonstrate the accuracy of our method on various doped MgH2 supercells. Further, we show that our approach, compared to standard DFT, significantly improves the Bader charge values for strongly correlated transition metal oxides, where we take DFT+U results as a reference. The computational framework behind our many-body calculations, called Dopyqo, is made openly available as a software package.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2510.15223v5
- Title: Game-Theoretic Discovery of Quantum Error-Correcting Codes Through Nash Equilibria
- Authors: Rubén Darío Guerrero
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.15223v5  pdf=https://arxiv.org/pdf/2510.15223v5.pdf

Abstract:
Quantum error correction code discovery has relied on algebraic constructions with predetermined structure or computational search lacking equilibrium-topology analysis. We introduce a game-theoretic framework recasting code optimization as strategic interactions between competing objectives, where Nash equilibria systematically generate codes with desired properties. We validate the framework by demonstrating it rediscovers the optimal $[\![15,7,3]\!]$ quantum Hamming code in 20\% of independent runs (Calderbank-Shor-Steane 1996) from competing objectives without predetermined algebraic structure, with equilibrium analysis providing transparent mechanistic insights into why this topology emerges. Applied across seven objectives -- distance maximization, hardware adaptation, rate-distance optimization, cluster-state generation, surface-like topologies, connectivity enhancement, and maximization of the quantum Fisher information $\mathcal{F}_Q$ (which quantifies, via the Cramér--Rao bound, the metrological sensitivity of the encoded codespace) -- the framework generates distinct code families through objective reconfiguration rather than algorithm redesign. Scalability to hardware-relevant sizes is demonstrated at $n=100$ qubits, discovering codes including $[\![100,50,4]\!]$ with distance-4 protection and 50\% encoding rate, with tractable $O(n^3)$ per-iteration complexity enabling discovery in under one hour. This work opens research avenues at the intersection of game theory and quantum information, providing systematic, interpretable frameworks for quantum system design.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2510.21692v3
- Title: Can Bose-Einstein condensates enhance radioactive decay?
- Authors: Hanzhen Lin, Yukun Lu, Wolfgang Ketterle
- Categories: quant-ph (primary); quant-ph; hep-ph; nucl-ex; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2510.21692v3  pdf=https://arxiv.org/pdf/2510.21692v3.pdf

Abstract:
This paper lays out the principles of how Bose-Einstein condensates can modify radioactive decay. We highlight the challenges of many modes and short coherence times due to the $\approx$ MeV energies of the emitted radiation. Recent proposals for gamma ray and neutrino lasers claim that using a Bose-Einstein condensate as a source would solve these issues. We show that this is not the case, and the proposed experiments would have a gain of only $10^{-16}$ or smaller. We also analyze proposals for gamma ray lasers based on stimulated annihilation of positronium Bose-Einstein condensates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2510.27661v2
- Title: Teleportation-based squeezer for bosonic cluster states
- Authors: Michal Matulík, Radim Filip, Petr Marek
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.27661v2  pdf=https://arxiv.org/pdf/2510.27661v2.pdf

Abstract:
The one-way quantum computation utilizing bosonic modes of light offers unmatched scalability of light modes, and it has seen rapid experimental development recently. Scalability requires robust and low-error gates and measurements. Squeezing gate is one of the necessary Gaussian operations. We find the optimal squeezing gate in cluster state architecture. Our approach newly uses amplitude transmission coefficients of unbalanced beam splitters and homodyne detection with subsequent unity-gain feed-forward to squeeze the input state. The approach outperforms the current method based on optimally rotated homodyne detection, but with fixed balanced beam splitters. The performance of both cluster state squeezers is evaluated for Gaussian and non-Gaussian input states. We use different metrics to benchmark the quality of squeezed output states. The result opens a road to low-noise squeezing gates in experimentally achievable cluster states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2512.19806v2
- Title: Local Operations and Field Mediated Entanglement without a Local Tensor Product Structure
- Authors: Alberto Spalvieri, Sébastien Christophe Garmier, Flaminia Giacomini
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2512.19806v2  pdf=https://arxiv.org/pdf/2512.19806v2.pdf

Abstract:
Quantum information has become a powerful tool for probing the structure of quantum field theories, yet its application to gauge theories remains subtle. On the one hand, quantum information theory assumes subsystem locality, i.e.~the factorization of the total Hilbert space into subsystems. On the other hand, gauge constraints prevent the total Hilbert space to decompose into a spacetime-local tensor product structure. Because the Hilbert space structure of gauge theories does not accommodate the subsystem decomposition used in quantum information theory, standard information-theoretic results, such as the Local Operations and Classical Communication (LOCC) theorem, cannot be used straightforwardly in the context of gauge theories. In this work, we bridge this gap in the case of a two-dimensional lattice gauge model that captures key features of electromagnetism. In particular, we construct gauge-invariant local algebras and derive a physically meaningful decomposition of the Hilbert space, providing an operationally consistent notion of locality in the absence of a local tensor-product structure. We apply this framework to field-mediated entanglement protocols relevant to proposed tests of the quantum nature of gravity. We show that the discretized version of electromagnetism satisfies an analogue of the LOCC theorem: entanglement cannot be generated without genuine quantum field interactions, even in the absence of a spacetime-local tensor product factorization of the Hilbert space. This may point towards an operational way to define a subsystem structure for gauge theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2512.19896v2
- Title: Gate-Based Microwave Quantum Repeater Via Grid-State Encoding
- Authors: Hany Khalifa, Matti Silveri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.19896v2  pdf=https://arxiv.org/pdf/2512.19896v2.pdf

Abstract:
In autonomous quantum error correction the lifetime of a logical bosonic qubit can be extended beyond its physical constituents without feedback measurements. Leveraging autonomous error correction, we propose a gate-based microwave quantum repeater (GBMQR) with encoded bosonic grid states. Each repeater station comprises a transmon and two bosonic resonators: one resonator serving as a stationary quantum memory utilizing autonomous error correction, and the other as an information bus for entanglement generation. Entanglement is generated sequentially through the successful absorption of a microwave photon wavepacket. This method enables deterministic entanglement generation, in contrast to a probabilistic mixing of two heralding signals on a balanced beamsplitter. Furthermore, our GBMQR employs an all-bosonic entanglement swapping Bell-state measurement. This is implemented via a bosonic controlled-Z gate and two separate X-basis projective homodyne measurements on the stationary stored codewords. Our approach circumvents mode-mismatch losses associated with routing and interfering of heralding modes on a beamsplitter, and confines losses to those arising from stationary storage. We evaluate the performance of the proposed quantum repeater by calculating its secret key rate under realistic lab environments. Moreover, we explicitly demonstrate that at stationary damping rate of $κ^{-1}_{\text{damp}}=$~\SI{40}{\milli\second}, GBMQR can achieve entanglement generation and swapping success probabilities approx.~$0.75$, and $0.58$ respectively, surpassing the hallmark success probability of $1/2$ set by ideal linear beamsplitter-based Bell-state measurements. The proposed device can be implemented using currently available superconducting microwave technology and is suited for secure chip-to-chip communication and distributed quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2512.20106v2
- Title: Finite-size Effects on The Edge Loss Probability in Non-Hermitian Quantum Walks
- Authors: Shuaixian Liu, Yulan Dong, Bowen Zeng, Mengqiu Long
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.20106v2  pdf=https://arxiv.org/pdf/2512.20106v2.pdf

Abstract:
A dynamical bulk-edge relation in quantum walks has been theoretically proposed and experimentally observed, in which a power-law dependence of the bulk loss probability is associated with a pronounced peak of loss probability at the edge. This behavior has been proven to arise from imaginary gap closing and the non-Hermitian skin effect in the infinite limit without boundary effects. However, in a finite-size chain, we find that boundary scattering can suppress this edge burst. Meanwhile, imaginary gap opening, together with the non-Hermitian skin effect, can also induce a large loss probability at the edge. Our results provide insights into finite-size quantum dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2512.20142v2
- Title: Highly Tunable Two-Qubit Interactions in Si/SiGe Quantum Dots by Interchanging the Roles of Qubit-Defining Gates
- Authors: Jaemin Park, Hyeongyu Jang, Hanseo Sohn, Younguk Song, Lucas E. A. Stehouwer, Davide Degli Esposti, Giordano Scappucci, Dohun Kim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.20142v2  pdf=https://arxiv.org/pdf/2512.20142v2.pdf

Abstract:
Silicon quantum dot spin qubits have become a promising platform for scalable quantum computing because of their small size and compatibility with industrial semiconductor manufacturing processes. Although Si/SiGe heterostructures are commonly used to host spin qubits due to their high mobility and low percolation density, the SiGe spacer creates a gap between the qubits and control electrodes, which limits the ability to tune exchange coupling. As a result, residual coupling leads to unwanted single-qubit phase shifts, making multi-qubit control more difficult. In this work, we explore swapping the roles of overlapping nanogates to overcome this issue. By reconfiguring the gate voltages, we demonstrate in situ role switching while maintaining multi-qubit control. Additionally, this method significantly improves the tunability of exchange coupling by several orders of magnitude over the traditional approach. This strategy reduces unintended single-qubit phase shifts and minimizes the complexity of multi-qubit control, supporting scalable growth with minimal experimental overhead.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2512.22767v3
- Title: An asymmetric and fast Rydberg gate protocol for entanglement outside of the blockade regime
- Authors: Daniel C. Cole, Vikas Buchemmavari, Mark Saffman
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2512.22767v3  pdf=https://arxiv.org/pdf/2512.22767v3.pdf

Abstract:
We analyze a new Rydberg gate design based on the original $π-2π-π$ protocol [Jaksch, et. al. Phys. Rev. Lett. {\bf 85}, 2208 (2000)] that is modified to enable high fidelity operation without requiring a strong Rydberg interaction. The gate retains the $π-2π-π$ structure with an additional detuning added to the $2π$ pulse on the target qubit. The protocol reaches within a factor of 2.39 (1.68) of the fundamental fidelity limit set by Rydberg lifetime for equal (asymmetric) Rabi frequencies on the control and target qubits. We generalize the gate protocol to arbitrary controlled phases. We design optimal target-qubit phase waveforms to generalize the gate across a range of interaction strengths and we find that, within this family of gates, the constant-phase protocol is time-optimal for a fixed laser Rabi frequency and tunable interaction strength. Quantum control techniques are used to design gates that are robust against variations in Rydberg Rabi frequency or interaction strength.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2601.02925v2
- Title: Violation of Bell Monogamy Relations
- Authors: Abhisek Panda, Chandan Datta, Pankaj Agrawal
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.02925v2  pdf=https://arxiv.org/pdf/2601.02925v2.pdf

Abstract:
The entangled multipartite systems, specially in pure states, exhibit the phenomenon of entanglement monogamy. Such systems also display the phenomenon of Bell nonlocality. Like entanglement monogamy relations, there are Bell monogamy relations. These relations suggest a sharing of nonlocality across the subsystems. The nonlocality, as characterized by Bell inequalities, of one subsystem limits the nonlocality exhibited by another subsystem. We show that the Bell monogamy relations can be violated by using local filtering operations. We consider permutation-symmetric multipartite pure states, in particular $W$ states, to demonstrate the violation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2604.09002v2
- Title: Loss-Tolerant Quantum Communication via Bosonic-GKP-Parity-Encoding
- Authors: S. Nibedita Swain, Timothy C. Ralph
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.09002v2  pdf=https://arxiv.org/pdf/2604.09002v2.pdf

Abstract:
Quantum repeaters constitute a promising platform for enabling long-distance quantum communication and may ultimately serve as the backbone of a secure quantum internet, a scalable quantum network, or a distributed quantum computer. An efficient approach to encoding qubits within an error correcting code is provided by bosonic codes, in which even a single oscillator mode can function as a sufficiently large physical system. In this work, we initially investigate the bosonic Gottesman Kitaev Preskill (GKP) code as a promising platform for loss correcting quantum repeaters, compatible with room temperature implementation, and analyse how loss and other noise sources propagate through the circuit using Heisenberg evolution. We analyse three quantum repeater protocols in which transmission loss is suppressed at the cost of logical errors, identifying a relay-like teleamplifier as the optimal scheme. This enables long distance quantum communication via densely packed nodes without higher-level encoding, and we evaluate the resulting secure key rates exploiting analog syndrome information. Furthermore, we propose a concatenated Bell-state measurement (CBSM) scheme with a modified parity encoding based on GKP qubits, CV measurement with teleamplifier and a clipping method that corrects transmission loss without introducing logical errors. This significantly enhances the possible secure key distance. We find that GKP based repeaters can achieve performance comparable to approaches relying on photonic qubits, while requiring orders of magnitude fewer qubits. Our parity encoded GKP repeater protocol achieves a substantially higher secret key rate than existing GKP based repeater schemes while maintaining a comparable resource overhead.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2604.09257v2
- Title: Quadratic Quantum Polarimetry with Entangled Photon Pairs
- Authors: Jinliang Ren, Vira Besaga, Ivan Lopushenko, Jinyong Ma, Alexander Bykov, Igor Meglinski, Frank Setzpfandt, Andrey A. Sukhorukov
- Categories: quant-ph (primary); quant-ph; physics.bio-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.09257v2  pdf=https://arxiv.org/pdf/2604.09257v2.pdf

Abstract:
Conventional polarimetry, including schemes leveraging entangled light, characterizes optical samples through linear transformations of polarization states. We introduce a two-photon probing approach in which both photons of an entangled pair interact with the same depolarizing medium simultaneously. In this regime, the transformation of the two-photon polarization correlations becomes quadratic in the Mueller matrix, enabling access to second-order polarization information beyond conventional polarimetry. We develop a theoretical framework linking the Mueller matrix to the evolution of the two-photon polarization correlation tensor and show that depolarization induces quadratic degradation of entanglement and state purity. Experiments using polarization-entangled photon pairs transmitted through controlled scattering media confirm the predicted response and reveal enhanced sensitivity to polarization scrambling compared with single-photon probing. These results establish two-photon probing as a higher-order quantum polarimetric modality for characterizing polarization channels.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2604.24633v2
- Title: Optimization Using Locally-Quantum Decoders
- Authors: Noah Shutty, Avijit Mandal, Seyoon Ragavan, Quentin Buzet, André Chailloux, Nicholas C. Rubin, Abid Khan, Sami Boulebnane, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.24633v2  pdf=https://arxiv.org/pdf/2604.24633v2.pdf

Abstract:
It was pointed out in [JSW+25] that widely-studied optimization problems such as D-regular max-k-XORSAT can be reduced to decoding of LDPC codes, using quantum algorithms related to Regev's reduction. LDPC codes have very good decoders, such as Belief Propagation (BP), and this therefore makes D-regular max-k-XORSAT an enticing target for this class of quantum algorithms. However, BP was found insufficient to achieve quantum advantage. Here, we develop an intrinsically quantum decoding technique, which decodes classical LDPC codes subject to coherent superpositions of bit flip errors. For average-case instances of D-regular max-k-XORSAT drawn from Gallager's ensemble, this quantum decoder strongly outperforms classical belief propagation at many values of k and D. For some (k,D) the approximate optima achievable using this decoder surpass both Prange's algorithm and simulated annealing. However, we stop short of achieving quantum advantage because we identify an enhancement to Prange's algorithm that recovers a precise tie, much as a precise tie was observed between the standard version of Prange's algorithm and a more limited version of locally-quantum decoding in [CT24].

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2604.27049v2
- Title: Non-Local Magic Resources for Fermionic Gaussian States
- Authors: Daniele Iannotti, Beatrice Magni, Riccardo Cioli, Alioscia Hamma, Xhek Turkeshi
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2604.27049v2  pdf=https://arxiv.org/pdf/2604.27049v2.pdf

Abstract:
Entanglement and magic are fundamental resources that capture the complexity of quantum many-body systems. Non-local magic isolates the irreducible nonstabilizerness intrinsically tied to entanglement. However, evaluating this quantity generally requires a prohibitive minimization over the full Hilbert space, making it computationally inaccessible beyond a few qubits. Here, we overcome this bottleneck by suggesting a closed-form expression for the non-local stabilizer entropies of fermionic Gaussian states over local Gaussian unitaries, which can be evaluated in polynomial time directly from the eigenvalues of the reduced Majorana covariance matrix. We apply this framework to characterize fermionic non-local magic across diverse physical regimes: we derive an exact Page-like curve for typical random states, reveal logarithmic scaling at the quantum critical point of the XY model, and establish a quasiparticle picture for magic generation during out-of-equilibrium quantum quenches. Crucially, because our result relies solely on two-point correlation functions, it provides a scalable route for the experimental estimation of fermionic non-local magic in large-scale quantum processors via fermionic shadow tomography.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.01103v3
- Title: On Quantum Indeterminacy and the Uncertainty Principle
- Authors: Maurice de Gosson
- Categories: quant-ph (primary); quant-ph; math-ph; math.GT; math.SG
- Links: abs=https://arxiv.org/abs/2605.01103v3  pdf=https://arxiv.org/pdf/2605.01103v3.pdf

Abstract:
We propose a geometric formulation of quantum indeterminacy based on polar duality between convex bodies representing position and momentum data. A pair (X,P) of centrally symmetric convex bodies is said to satisfy the indeterminacy condition when the h-polar of X is included in P. We show that this condition naturally arises from the geometry of quantum blobs and is closely related to Hardy's uncertainty principle and the Donoho--Stark inequalities. Using symplectic capacities and John ellipsoids, we associate a canonical covariance ellipsoid with every quantum polar pair and prove that it satisfies the quantum condition. The Robertson--Schrödinger inequalities follow as a consequence. This provides a non-statistical formulation of quantum indeterminacy from which the usual uncertainty relations emerge. which the usual uncertainty relations emerge.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.06848v2
- Title: Quantum Darwinism and the quality of Petz recovery
- Authors: Juha Torvinen, Esko Keski-Vakkuri, Nicola Pranzini
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.06848v2  pdf=https://arxiv.org/pdf/2605.06848v2.pdf

Abstract:
According to Quantum Darwinism, system-environment interactions both einselect particular system properties and encode them redundantly in many independent subsets of the environment, called fragments. This redundancy implies that an observer can recover the einselected information by accessing just one such fragment. However, the protocol by which such reconstruction should occur is often left unspecified. Considering a system $Γ$ interacting with a multipartite environment $Ξ$, we investigate whether, and under what conditions, the einselected state of $Γ$ can be recovered from environmental fragments using the Petz recovery map. We show that the fidelity between the system's initial state and the state reconstructed via Petz recovery develops a plateau as a function of the fragment size. Our results are supported by both analytical arguments and numerical simulations of large but tractable models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.07753v2
- Title: Universal Symmetry-Breaking Dynamics at Continuous Phase Transitions: Evidence for a New Dynamical Critical Exponent
- Authors: Tobias Wiener, Laurin Brunner, Markus Heyl
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2605.07753v2  pdf=https://arxiv.org/pdf/2605.07753v2.pdf

Abstract:
Uncovering and understanding universal dynamics in matter far from equilibrium remains a key challenge. In this work, we identify a so far unrecognized form of universal behavior that emerges after a sudden symmetry-breaking quench at continuous phase transitions. Our key observation is that the order-parameter fluctuations in Ising models exhibit a compelling temporal collapse across a wide range of system sizes and quench strengths, indicative of an emergent single-variable scaling form. This phenomenon can be explained by introducing a so far unknown dynamical critical exponent for the underlying continuous phase transition. We find evidence for a lower critical effective dimension of this universal regime: it is observed in the 2D quantum and 3D and 4D classical Ising models, but not in the 1D quantum or 2D classical cases. Our results suggest that our observed universal far-from-equilibrium scaling may extend beyond the Ising models studied here and could more broadly characterize systems with non-conserved order parameters, opening new avenues for exploring universal dynamics both theoretically and in current experimental platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.09872v3
- Title: Multi-Prover Interactive Proof Systems with Leakage
- Authors: Vahid R. Asadi, Atsuya Hasegawa, François Le Gall
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2605.09872v3  pdf=https://arxiv.org/pdf/2605.09872v3.pdf

Abstract:
It is known that there exist multi-prover interactive protocols ($\mathsf{MIP}$ protocols) for the complexity class $\mathsf{NEXP}$, succinct $\mathsf{MIP}$ protocols for $\mathsf{NP}$ and multi-prover interactive protocols with shared entanglement ($\mathsf{MIP}^\ast$ protocols) for $\mathsf{RE}$. This extraordinary power of multi-prover interactive proof systems comes from the assumption that provers do not communicate with each other during the protocols. If they are allowed to communicate freely, the setting is the same as in the single-prover case, and the computational power of the system becomes significantly weaker.   In this paper, we investigate for the first time the setting where communication (i.e., leakage of information) between provers is allowed but bounded. We introduce two techniques to approach this question and show that multi-prover interactive proof systems are robust against some amount of leakage. Our first technique is based on parallel repetition theorems. We apply it to show that for any polynomial $p$, we can construct two-prover one-round $\mathsf{MIP}$ and $\mathsf{MIP}^\ast$ protocols for $\mathsf{NEXP}$ and $\mathsf{RE}$, respectively, that are robust against $p(n)$ bits of leakage. We further derive our second technique to convert any low-soundness PCP construction to a two-prover one-round $\mathsf{MIP}$ protocol for $\mathsf{NP}$ robust against leakage. We also discuss the relation between robustness against leakage in multi-prover interactive proof systems and the Sliding Scale Conjecture in the PCP literature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.19917v3
- Title: Spin-Induced Non-Markovian Time-Crystal-Like Dynamics and Fractal Scaling in the Bateman Dual Oscillator
- Authors: Partha Nandi, Giuseppe Vitiello
- Categories: quant-ph (primary); quant-ph; hep-th; physics.soc-ph
- Links: abs=https://arxiv.org/abs/2605.19917v3  pdf=https://arxiv.org/pdf/2605.19917v3.pdf

Abstract:
Can a closed quantum system generate persistent time-crystal-like dynamics without external driving? Within the Bateman dual oscillator framework, we show that the answer is affirmative. We consider a nonrelativistic (2+1)-dimensional system in which spin-induced spatial deformation generates an effective Bateman oscillator structure. After quantization, the system is governed by a time-independent Hermitian Hamiltonian describing coherent coupling between damped and amplified oscillator sectors while preserving the total energy of the global doubled system. Tracing over the amplified sector, we derive an effective non-Markovian reduced dynamics for the observable subsystem. The resulting memory effects sustain persistent oscillations of subsystem observables and generate emergent time-crystal-like temporal ordering without external periodic driving or equilibrium spontaneous symmetry breaking. Since the oscillatory behavior originates from nonequilibrium reduced subsystem dynamics rather than equilibrium expectation values of the full Hamiltonian, the mechanism lies outside the assumptions of conventional no-go theorems for equilibrium time crystals. The same dynamics further exhibits logarithmic-spiral trajectories and self-similar fractal scaling, revealing a direct connection between coherent dissipative dynamics, non-Markovian memory effects, and emergent temporal ordering in a globally unitary quantum system. In this specific sense, "watching the growth" of these self-similar structures corresponds to observing the gradual formation of time-crystal-like ordering.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.30798v2
- Title: Eigenstate chaos in the presence of non-Abelian symmetries
- Authors: Siddharth Jindal, Pavan Hosur
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2605.30798v2  pdf=https://arxiv.org/pdf/2605.30798v2.pdf

Abstract:
The eigenstate thermalization hypothesis (ETH) posits that energy eigenstates encode local properties of the microcanonical ensemble. Motivated by recent interest in the physics of non-commuting conserved charges and the non-Abelian ETH, we study chaotic eigenstates in the presence of symmetries described by general compact Lie groups, such as SU(2). By applying non-Abelian symmetry resolution, we develop a non-Abelian microcanonical entropy and relate this entropy to the entanglement entropy of chaotic eigenstates. We find that microcanonical entropy is closely related to the symmetry-resolved entanglement entropy, which differs from conventional entanglement entropy by a universal logarithmic correction. Our results depend on the global Casimir charge, e.g. total spin. At finite charge density, we find a logarithmic enhancement to conventional entanglement entropy. At zero density, we find no such correction to entanglement entropy, but a logarithmic reduction to microcanonical entropy and symmetry-resolved entanglement entropy. We discuss the implications of our approach for non-Abelian eigenstate thermalization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.01341v2
- Title: Generating Fock state exceeding 10000 excitations with near unit fidelity by adaptive generalized-parity measurement
- Authors: Chen-yi Zhang, Jun Jing
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.01341v2  pdf=https://arxiv.org/pdf/2606.01341v2.pdf

Abstract:
Fock states are fundamental quantum states with a precisely defined integer number of excitations, serving as the core basis for describing bosonic modes. Large Fock states provide irreplaceable non-classical resources for quantum information processing and quantum metrology. The deterministic generation of macroscopic photon-number Fock states has long been a difficult problem in the field of quantum optics. We propose an adaptive generalized parity measurement (GPM) protocol for generating Fock states with more than $10000$ excitations, avoiding low success probability subject to postselection and high cost under complex coherent controls. For general discrete-spectrum systems, e.g., a bosonic mode coupled to an ancillary qubit, we derive a construction rule in which the intervals between repeated measurements on qubit are updated adaptively based on the last outcome. It means that our protocol does not discard any measurement trajectory, dramatically different from the probabilistic protocols that retain only one prescribed trajectory of postselection. In the resonant Jaynes-Cummings model, a large coherent state can be almost deterministically transformed to a large Fock state of $n_t=\mathcal{O}(10^4)$ excitations by $10$ rounds of measurements, the average fidelity of which is about $87\%$. The success probability for obtaining $|20000-\sqrt{20000}\leq n_t\leq20000+\sqrt{20000}\rangle$ with a fidelity above $99\%$ is about $35\%$ with respect to the ensemble sampling. Our protocol is fault-tolerant in the presence of moderate measurement error and parametric imperfection. Also it remains effective when the system is prepared as displaced thermal states, showing reliable performance regardless of initial state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.22071v2
- Title: Hardware-native quantum phase estimation with circuit QED
- Authors: Changchun Zhong
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.22071v2  pdf=https://arxiv.org/pdf/2606.22071v2.pdf

Abstract:
Quantum phase estimation is a cornerstone algorithm for determining eigenvalues of unitary operators with Heisenberg-limited precision. Conventional implementations rely on digital controlled-unitary operations together with phase-extraction circuits, which generally results in substantial circuit depth and hardware overhead. Here, we propose a hardware-native alternative that replaces digital controlled-unitary operations by analog bosonic interactions, naturally available in circuit quantum electrodynamics. The protocol extracts the phase through a sequence of binary threshold tests. A bosonic mode serves as an efficient quantum memory where the binary digits of the phase are encoded into the direction of phase-space rotations. These digits are then read out sequentially via high-fidelity homodyne measurements. We show that the protocol preserves Heisenberg scaling in estimation precision while simultaneously providing exponentially suppressed failure probability. By exploiting bosonic degrees of freedom and analog dispersive interactions, the scheme provides a hardware-efficient realization of quantum phase estimation and establishes a natural route toward implementing high-precision phase estimation on circuit quantum electrodynamics platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.22127v2
- Title: Emergence of Boolean Facts from Markovian Coarse-Graining in Relational Quantum Causal Processes
- Authors: Yipeng Xu
- Categories: quant-ph (primary); quant-ph; gr-qc; math-ph
- Links: abs=https://arxiv.org/abs/2606.22127v2  pdf=https://arxiv.org/pdf/2606.22127v2.pdf

Abstract:
We formulate an operator-algebraic mechanism by which exact Boolean records can arise from local completely positive quantum operations without being imposed as microscopic structure. The kinematic input is an algebraic process functional assigning probabilities to local normal completely positive operations in a finite operational context. From the predual response of a target algebra to source interventions, relative to a background strategy class, we define an influence algebra; exact events are then, by definition, the projections in its center. The dynamical question is whether nontrivial centers can be generated by coarse-graining rather than inserted through split-record laboratories. We address this question using state-preserving normal unital completely positive coarse-graining channels. If the Cesaro means of such a channel converge to a Choi-Effros infrared range and the range is asymptotically abelian in the GNS seminorm, then the represented infrared algebra is a commutative von Neumann algebra. Its projection lattice is therefore a complete Boolean algebra. We also give a finite-sector block-primitive criterion, motivated by locality and scrambling, which implies this asymptotic abelianness with exponential suppression of off-sector coherences and intra-sector fluctuations. The result is a conservative mathematical statement: classical facts are not identified with arbitrary projections of a Type-III local algebra, but with central projections selected by an asymptotically abelian completely positive infrared limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.23577v2
- Title: Genuine Global Kochen-Specker Contextuality as Classical Coordination Cost
- Authors: Ming Yang
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2606.23577v2  pdf=https://arxiv.org/pdf/2606.23577v2.pdf

Abstract:
Classical simulations of quantum correlations can fail because no low-communication local hidden-variable model exists, or because no single noncontextual hidden state can explain all compatible measurement contexts. This manuscript studies a third regime: genuine global Kochen-Specker contextuality, where local subsystems are noncontextual and the tested multipartite blocks are generalized-Bell-local, but the whole empirical model admits no global noncontextual hidden-variable explanation. We propose a coordination-cost framework in which communication, memory, and local computation are treated as different ways for a classical simulator to maintain a global classical explanation from locally available information. We introduce coordination bits, global contextual covering numbers, scaling laws for task families, and an abstract lifting theorem showing how classical simulation lower bounds for KS-contextual seed families can be transferred to genuinely global-KS models. As worked examples, we analyze a polarization-path Hardy obstruction and postselected KCBS-type tasks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.28866v3
- Title: Quantum Variational Approaches to the Maximum Independent Set Problem at Utility Scale
- Authors: Kalyan Dasgupta, Sumanta Mukherjee, Dhriti Verma, Surya Shravan Kumar Sajja, Abhishek Singh, Dzung Phan, Jayant Kalagnanam
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.28866v3  pdf=https://arxiv.org/pdf/2606.28866v3.pdf

Abstract:
We study variational quantum algorithms for the Maximum Independent Set (MIS) problem on benchmark graphs of 64, 99, and 180 vertices. The Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA) are compared across SPSA and COBYLA optimizers at multiple circuit depths. A preprocessing pipeline comprising spectral graph reordering (via the Fiedler vector) and distance-based sparsification reduces circuit depth while preserving energy fidelity. Classical post-processing via history-guided bitstring correction and stepwise maximality extension recovers the exact MIS across all instances. With CVaR optimization, VQE with SPSArecovers up to 6 distinct MIS per run for the 64-node instance and up to 10 distinct MIS per run for the 99-node instance, sampling broadly from the optimal solution population. Repeated runs with different SPSA trajectories collectively enumerate a larger fraction of all MIS for each instance. For the 180-node instance, where standard approaches stall at size 14 (MIS is 15), we introduce ancilla-assisted superposition initialization: ancilla qubits prepare a uniform superposition over classically-found near-optimal solutions, and an excitation-preserving ansatz evolves this state while conserving Hamming weight. This novel construction enables quantum-parallel variational search over multiple seeds simultaneously, discovering the exact MIS where single-seed methods fail. The 180-qubit simulation represents, to our knowledge, the largest scale at which gate-based variational algorithms have solved MIS to optimality. Hardware validation on IBM Quantum hardware ibm_marrakesh confirms that converged simulator parameters transfer effectively to noisy quantum execution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.29293v2
- Title: Private training in quantum machine learning
- Authors: Tigran Sedrakyan, Frédéric Grosshans, Elham Kashefi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.29293v2  pdf=https://arxiv.org/pdf/2606.29293v2.pdf

Abstract:
With the emergence of machine learning (ML) models trained on large datasets containing potentially sensitive data, a major question in AI safety is how to make learning private with respect to the training data. Similar to classical machine learning, quantum machine learning (QML) models are not devoid of privacy vulnerabilities. Differential privacy (DP) is a standard tool for training ML models on sensitive data, but its impact in QML remains poorly understood. In this work we study private training in hybrid variational QML models using a classical private DP-SGD optimizer applied to pipelines with classical inputs and outputs. We analyze the interplay between gradient clipping and calibrated noise addition in DP-SGD, and its impact on optimization and accuracy for noisy and noiseless quantum models. We first explain why quantum noise does not provide a satisfactory replacement for the calibrated noise in DP-SGD for ensuring privacy. We then show how the deterministic bounds on gradient norms for a wide class of quantum models translate into explicit control of the detrimental clipping bias introduced by DP-SGD. Finally, we formulate a numerical comparison protocol under fixed clipping threshold and privacy budget and evaluate it on synthetic and image-classification tasks for equivalent quantum and classical models. Our results suggest that quantum models can retain higher accuracy in private-training regimes where the formal privacy guarantee is ensured by a classical DP-SGD mechanism.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.29304v2
- Title: Volume Law and Universality of Entanglement Entropy in Random Graph Fermi Systems
- Authors: Saikat Sur
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2606.29304v2  pdf=https://arxiv.org/pdf/2606.29304v2.pdf

Abstract:
We study the ground-state entanglement entropy of free fermions on random graphs. We first establish a general criterion for the volume law on random graphs, based on the spectral characteristics of the Hamiltonian. We then apply this criterion to the Erdős--Rényi random graph, where each of the possible edges is present independently with some probability. Using random matrix theory and asymptotic freeness, we show that the ground-state entanglement entropy obeys an exact volume law in Erdős--Rényi graphs in the thermodynamic limit, with a universal coefficient that is independent of the edge probability of the graph. This coefficient is confirmed numerically to take the value approximately $0.3863$ nats, strictly below the Page value. The volume law therefore reflects the absence of geometric locality in the random graph.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.29610v2
- Title: Physics-Informed Neural Quantum Control for Rovibrational Photoassociation in a Morse Molecular System
- Authors: Murilo D. Forlevesi, Emanuel Fernandes de Lima, Edson Denis Leonel
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2606.29610v2  pdf=https://arxiv.org/pdf/2606.29610v2.pdf

Abstract:
We present a Physics-Informed Neural Quantum Control (PINQC) framework for rovibrational photoassociation in a Morse molecular system. The proposed method combines neural-network-based laser-field generation with differentiable quantum propagation, allowing optimized laser pulses to be obtained directly from the underlying quantum dynamics without requiring external training data. The optimized control fields efficiently transfer an initially continuum-like Gaussian wave packet into the vibrational ground-state level, promoting continuum-to-bound population transfer through coherent rovibrational dynamics. The resulting photoassociation process involves both vibrational stabilization and rotational redistribution arising naturally from dipole-induced couplings between neighboring rotational channels. A central result of the present work is the successful application of the PINQC framework to extended rovibrational models containing larger rotational levels than those previously accessible in our conventional photoassociation calculations. The optimization remains numerically stable despite the increased complexity of the molecular system, demonstrating that differentiable optimization provides an effective strategy for treating rovibrational models of increased dimensionality. These results establish the PINQC framework as a promising computational tool for molecular photoassociation and motivate future investigations of increasingly complex rovibrational quantum-control problems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.31243v2
- Title: Absorption capacity of separable noise: Bell-mixing thresholds on separability and teleportation
- Authors: Xuan Du Trinh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.31243v2  pdf=https://arxiv.org/pdf/2606.31243v2.pdf

Abstract:
We study Bell-mixing lines $ρ_λ=λΦ^+ +(1-λ)σ$, where $Φ^+$ is a fixed Bell reference and $σ$ is a separable two-qubit noise state. Along this line there are two operational crossings: the state becomes entangled, and it reaches quantum teleportation advantage over classical strategies. We package these crossings as capacities of the noise state. The entanglement absorption capacity $C_{\rm abs}(σ)$ is the largest amount of Bell reference that $σ$ can absorb while the partial transpose remains positive. The fidelity absorption capacity $C_F(σ)$ is the largest amount of Bell reference that $σ$ can absorb while keeping the maximal teleportation fidelity at or below the classical bound $2/3$. The thresholds corresponding to the two crossing points are obtained from the same Möbius map, $λ_* = C_{\rm abs}/(1+C_{\rm abs})$ and $λ_F = C_F/(1+C_F)$. We derive closed-form capacities and thresholds for product noise states and separable complex $X$ noise states. For product noise, $C_{\rm abs}$ depends only on local marginal purities, while $C_F$ also depends on orientation relative to the maximally entangled reference. For $X$ noise states, both capacities are explicit in all four Bell frames. We also study three extensions: arbitrary pure-state references, the evolution of $X$ noise states and their capacities under local amplitude-damping and dephasing channels, and decomposition certificates that give lower bounds on the capacities, hence on the thresholds, for general separable noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.31753v2
- Title: Distributed Property Testing with (Quantum) Carrier Pigeons: Tight Bounds on State Certification
- Authors: Kenny Chen
- Categories: quant-ph (primary); quant-ph; cs.DS
- Links: abs=https://arxiv.org/abs/2606.31753v2  pdf=https://arxiv.org/pdf/2606.31753v2.pdf

Abstract:
Recently, Doosti et al. introduced the problem of distributed quantum state verification, where $m$ distributed nodes are given a copy of an unknown state $ρ$, and can send limited one way communication to a central node, who has a complete description of a known state $σ$. They ask how many distributed nodes $m$ are required, before the central node can succeed at distinguishing whether $ρ=σ$ or $\|ρ-σ\|_1\geq\varepsilon$ with high probability. In the setting where only quantum communication is allowed, Doosti et al. exhibit conditional lower bounds in both the public and private-coin settings, and a matching upper bound in the public-coin setting. We extend these results, and show unconditional lower bounds for when both classical and quantum communication are permitted. We show the public-coin lower bound is tight by giving an algorithm with a matching upper bound. We also show an almost tight upper bound in the private-coin setting when only quantum communication is permitted.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.00210v2
- Title: Classification and Exact Local Masking in Finite-Field Clifford Dual-Unitary Circuits
- Authors: Basanta R Pahari
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.00210v2  pdf=https://arxiv.org/pdf/2607.00210v2.pdf

Abstract:
We classify two-qudit Clifford dual-unitary gates over the finite field $\mathbb{F}_q$, where the local dimension $q$ is a prime power, and apply the classification to exact local masking and operator transport in homogeneous brickwork circuits. Under ordered one-qudit Clifford equivalence, the dual-unitary locus contains $q-2$ perfect-tensor cores, one rank-one core, and one SWAP core. Homogeneous repetition separates these cores into five distinct transport phases.   The one-site Weyl edge channels determine exact local-masking distances. Writing $d_r(t)$ for the masking distance against output observers controlling at most $r$ sites, perfect-tensor circuits attain \[ d_1(t)=4t, \qquad d_2(t)=4t-2, \] whereas delayed erasers satisfy \[ d_1(t)=4t-2, \qquad d_2(t)=4t-4 \] for $t\geq 2$. Consequently, sufficiently short quantum messages are completely hidden from every one- or two-qudit output subsystem, even when the input is entangled with a reference, while remaining exactly recoverable from the full output.   For $q=3$, we construct an explicit perfect-tensor Clifford gate from two inverse SUM gates. Exhaustive Weyl-support searches for $t=1,2,3$ reproduce the predicted masking distances. For a coherent perturbation of this gate, local leakage scales linearly with the perturbation strength, whereas the infidelity of recovery using the ideal inverse scales quadratically near the perfect point.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2607.01158v2
- Title: Continuous Observation of Quantum Systems
- Authors: Hans Maassen
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.01158v2  pdf=https://arxiv.org/pdf/2607.01158v2.pdf

Abstract:
In a series of papers in the 1980's Alexander Holevo proved a classification theorem for continuous quantum measurement processes, or, as they would today be called, stationary quantum trajectories in continuous time. His main tools were functional analytic in character: starting from a Bochner-type inequality he employed dilation techniques for positive definite kernels. Here we give an alternative, more probabilistic proof: we use weak convergence of measures and employ Levy's Continuity Theorem. We clarify the boundedness conditions in Holevo's theorem, and supply a simple example from quantum optics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2306.12166v3
- Title: Elusive phase transition in the replica limit of monitored systems
- Authors: Guido Giachetti, Andrea De Luca
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.dis-nn; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2306.12166v3  pdf=https://arxiv.org/pdf/2306.12166v3.pdf

Abstract:
We study an exactly solvable model of monitored dynamics in a system of $N$ spin-$1/2$ particles with pairwise all-to-all noisy interactions, where each spin is continuously weakly measured along a random direction. Using the replica trick to incorporate the Born-rule weighting of measurement outcomes, we obtain an exact large-$N$ description of purification and of the statistics of local observables. We find that the nature of the phase transition strongly depends on the number $n$ of replicas: non-perturbative logarithmic corrections appear in the physically relevant $n\to1$ limit and destroy the purifying phase present at finite integer $n$. As a consequence, the purification time of an initially mixed state is always exponentially long in the system size, even at arbitrarily large measurement rate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2407.21764v3
- Title: Energy Transport Among Highly-Polarized Atoms
- Authors: Catherine D. Opsahl, Yuan Jiang, Samantha A. Grubb, Alan T. Okinaka, Nicolaus A. Chlanda, Hannah S. Conley, Aidan D. Kirk, Sarah E. Spielman, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2407.21764v3  pdf=https://arxiv.org/pdf/2407.21764v3.pdf

Abstract:
We measure the transport of energy among the internal states of ultracold rubidium Rydberg atoms coupled by dipole-dipole exchange. In a magneto-optical trap, a static electric field of a few V/cm shifts the energy levels of the atoms. For a particular principal quantum number, $n$, the angular momentum eigenstates $\ell > 4$ are nearly degenerate at zero electric field. At nonzero field, a manifold of equally spaced clusters form a ladder with each rung consisting of a set of closely spaced $m$ energy eigenstates. We excite Rydberg atoms to energy levels near the center of the manifold and allow them to exchange energy via resonant dipole-dipole interactions. We measure the time evolution as energy spreads away from the center of the manifold, which reveals that the system may fail to thermalize for long interaction times. A computational model that includes only a few essential features of the system qualitatively agrees with this result.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2411.14406v3
- Title: Full counting statistics after quantum quenches as hydrodynamic fluctuations
- Authors: David X. Horvath, Benjamin Doyon, Paola Ruggiero
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2411.14406v3  pdf=https://arxiv.org/pdf/2411.14406v3.pdf

Abstract:
The statistics of fluctuations on large regions of space encodes universal properties of many-body systems. At equilibrium, it is described by thermodynamics. However, away from equilibrium such as after quantum quenches, the fundamental principles are more nebulous. In particular, although exact results have been conjectured in integrable models, a correct understanding of the physics is largely missing. In this letter, we explain these principles, taking the example of the number of particles lying on a large interval in one-dimensional interacting systems. These are based on simple hydrodynamic arguments from the theory of ballistically transported fluctuations, and in particular the Euler-scale transport of long-range correlations. Using these principles, we obtain the full counting statistics in terms of thermodynamic and hydrodynamic quantities, whose validity depends on the structure of hydrodynamic modes and on the fluctuations in the initial state. In fermionic-statistics interacting integrable models with a continuum of hydrodynamic modes, such as the Lieb-Liniger model for cold atomic gases, the formula reproduces previous conjectures, but is in fact not exact: it gives the correct cumulants up to, including, order 5, while long-range correlations modify higher cumulants. In integrable and non-integrable models with two or less hydrodynamic modes, the formula is expected to give all cumulants.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2412.06792v3
- Title: Optical Switching of $χ^{(2)}$ in Diamond Photonics
- Authors: Sigurd Flågan, Joe Itoi, Prasoon K. Shandilya, Vinaya K. Kavatamane, Matthew Mitchell, David P. Lake, Paul E. Barclay
- Categories: physics.optics (primary); physics.optics; cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2412.06792v3  pdf=https://arxiv.org/pdf/2412.06792v3.pdf

Abstract:
Diamond's unique physical properties make it a versatile material for a wide range of nonlinear and quantum photonic technologies. However, unlocking diamond's full potential as a nonlinear photonic material with non-zero second-order susceptibility $χ^{(2)}\neq0$ requires symmetry breaking. In this work, we use a nanoscale cavity to demonstrate second-harmonic generation (SHG) in diamond, and demonstrate, for the first time, that the magnitude of the diamond's effective $χ^{(2)}$ strongly depends on the electronic configuration of defects in the diamond crystal, such as nitrogen-vacancy centres. The modification of $χ^{(2)}$ arises from photoionisation from the negative to neutral charge-state, and is manifested by quenching of SHG upon green illumination. Toggling the green illumination allows for optical switching of the device's $χ^{(2)}$. Optical control of $χ^{(2)}$ by defect engineering opens the door for second-order nonlinear processes in diamond.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2502.09697v2
- Title: Spacetime Supersymmetry in the Truncated Lattice Schwinger Model
- Authors: Yanting Cheng, Shang Liu
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.str-el; hep-lat; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2502.09697v2  pdf=https://arxiv.org/pdf/2502.09697v2.pdf

Abstract:
Gauge theories in (1+1)D have attracted renewed attention partially due to their experimental realizations in quantum simulation platforms. In this work, we revisit the truncated lattice massive Schwinger model and the truncated lattice Abelian-Higgs model in (1+1)D, where to facilitate quantum simulation, the electric field eigenvalues are truncated to a finite subset while preserving the exact gauge and global symmetries. We uncover previously overlooked universal features in these models, including the emergence of a supersymmetric quantum critical point when the Maxwell term's coefficient changes sign. Our primary focus is the truncated lattice Schwinger model at $θ=0$, a model not equivalent to familiar spin models. We find that upon reversing the sign of the Maxwell term, the second-order charge conjugation symmetry breaking transition (or confinement-deconfinement transition in a sense) can become first-order. Furthermore, the two types of transitions are connected by a supersymmetric critical point in the tricritical Ising universality class. In the case of truncated Abelian-Higgs model at $θ=0$, which we find to be equivalent to the quantum Blume-Capel model, the very existence of a symmetry-breaking phase requires a negative-sign Maxwell term. Similarly, there is a tricritical Ising point separating first-order and second-order phase transitions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2503.24362v5
- Title: Recursion method for quench dynamics: strengths and limitations
- Authors: Ilya Shirokov, Viacheslav Khrushchev, Filipp Uskov, Ivan Dudinets, Igor Ermakov, Oleg Lychkovskiy
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2503.24362v5  pdf=https://arxiv.org/pdf/2503.24362v5.pdf

Abstract:
The recursion method, which solves coupled Heisenberg equations in a Lanczos operator basis, has recently emerged as a powerful nonperturbative tool for computing dynamical correlation functions in strongly correlated two- and three-dimensional quantum many-body systems. Motivated by this success, we investigate whether the method can be extended to expectation values of observables following a quantum quench. We find that such an extension encounters an obstacle absent in the computation of dynamical correlation functions. The latter are fully determined by the Lanczos coefficients $b_n$, which in generic systems exhibit universal behavior, enabling reliable extrapolation from the first few dozens of explicitly computed coefficients. In contrast, quench dynamics additionally requires "quench coefficients" $c_n$, defined as overlaps of Lanczos basis operators with the initial state. We show that, unlike the Lanczos coefficients, the quench coefficients exhibit no universal structure and cannot be reliably extrapolated, thereby limiting the time up to which the method yields accurate results. The behavior of quench coefficients is highly state-dependent, ranging from decaying to irregular or even growing sequences; typically, the less regular the sequence $c_n$, the shorter the accessible timescale. Nevertheless, for favorable initial states, the method remains competitive with state-of-the-art approaches. Moreover, its symbolic implementation allows a single computation to be reused across different Hamiltonian parameters and initial states, making it particularly advantageous in studies requiring extensive scans over Hamiltonian parameters or initial states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2504.18747v2
- Title: Covert Communication Over a Quantum MAC with a Helper
- Authors: Hassan ZivariFard, Rémi A. Chou, Xiaodong Wang
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2504.18747v2  pdf=https://arxiv.org/pdf/2504.18747v2.pdf

Abstract:
We study covert classical communication over a quantum multiple-access channel (MAC) with a helper. Specifically, we consider three transmitters, where one transmitter helps the other two transmitters communicate covertly with a receiver. We demonstrate the feasibility of achieving a positive covert rate over this channel and establish an achievable rate region. Our result recovers as a special case known results for classical communication over classical MACs with a degraded message set, classical communication over quantum MACs, and classical communication over MACs with a helper. To the best of our knowledge, our result is the first to achieve covert communication with positive rates over both classical and quantum MACs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2507.05954v2
- Title: A Hydrodynamic Theory for Non-Equilibrium Full Counting Statistics in One-Dimensional Quantum Systems
- Authors: David X. Horvath, Benjamin Doyon, Paola Ruggiero
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.quant-gas; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2507.05954v2  pdf=https://arxiv.org/pdf/2507.05954v2.pdf

Abstract:
We study the dynamics of charge fluctuations after homogeneous quantum quenches in one-dimensional systems with ballistic transport. For short but macroscopic times where the non-trivial dynamics is largely dominated by long-range correlations, a simple expression for the associated full counting statistics can be obtained by hydrodynamic arguments. This formula links the non-equilibrium charge fluctuation after the quench to the fluctuations of the associated current after a charge-biased inhomogeneous modification of the original quench which corresponds to the paradigmatic partitioning protocol. Under certain assumptions, the fluctuations in the latter case can be expressed by explicit closed form formulas in terms of thermodynamic and hydrodynamic quantities via the Ballistic Fluctuations Theory. In this work, we identify precise physical conditions for the applicability of a fully hydrodynamic theory, and provide a detailed analysis explicitly demonstrating how such conditions are met and how this leads to such hydrodynamic treatment. We discuss these conditions at length in non-relativistic free fermions, where calculations become feasible and allow for cross-checks against exact results. In physically relevant cases, strong long-range correlations can complicate the hydrodynamic picture, but our formula still correctly reproduces the first cumulants.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2507.07195v3
- Title: Theory of Strongly Correlated Systems: An Introduction to Sachdev-Ye-Kitaev Model
- Authors: Rishabh Jha
- Categories: hep-th (primary); hep-th; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2507.07195v3  pdf=https://arxiv.org/pdf/2507.07195v3.pdf

Abstract:
The Sachdev-Ye-Kitaev (SYK) model provides an analytically tractable framework for exotic strongly correlated phases where conventional paradigms like Landau's Fermi liquid theory collapse. This review offers a pedagogical introduction to the SYK physics, highlighting its unique capacity to model \textit{strange metals} -- systems exhibiting linear-in-temperature resistivity, Planckian dissipation, and quasiparticle breakdown. We systematically construct both Majorana and complex fermion variants, transforming them into training grounds for modern many-body physics techniques, for instance, (1) large-$N$ formulations via disorder averaging and replica symmetry, (2) Schwinger-Dyson and Kadanoff-Baym equations, (3) imaginary time Matsubara formulation, (4) real-time dynamics via Keldysh formalism, and the associated (5) non-perturbative Keldysh contour deformations. These tools lay the foundation for equilibrium thermodynamics, quantum chaos, quench dynamics, and transport in the thermodynamic limit, all within a solvable, chaotic quantum system. Intended as a self-contained resource, the review bridges advanced technical machinery to physical insights, with computational implementations provided. Though principally treating the SYK model as a condensed matter laboratory, we also highlight its profound connection to quantum gravity, woven throughout this work, underscoring how this solvable chaotic fermionic model serves as a lens onto black hole thermodynamics and holographic duality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2509.16747v2
- Title: $Δ_T$ Noise as a Robust Diagnostic for Chiral, Helical and Trivial Edge Modes
- Authors: Sachiraj Mishra, Colin Benjamin
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; math-ph; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2509.16747v2  pdf=https://arxiv.org/pdf/2509.16747v2.pdf

Abstract:
In this article, we demonstrate that $Δ_T$ noise provides a sensitive, practical probe for distinguishing chiral edge modes from topological helical and trivial (non-topological) helical edge transport. Measured under zero-current conditions, $Δ_T$ noise reveals contrasts that conventional conductance measurements typically miss. Crucially, $Δ_T$ noise requires no external energy input in the form of an applied voltage bias, yet encodes the same intrinsic information that shot noise yields in the zero-temperature, finite-bias limit, without the distorting effects of Joule heating. This absence of bias-induced heating makes $Δ_T$ noise both more precise and more reliable than conventional shot-noise approaches.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2510.08031v2
- Title: Bypassing Spin-Analyzing Power Dependence for Quantum Entanglement at Colliders: A Case Study of $Λ\barΛ$
- Authors: Junle Pei, Tianjun Li, Lina Wu, Xiqing Hao, Xiaochuan Wang
- Categories: hep-ph (primary); hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2510.08031v2  pdf=https://arxiv.org/pdf/2510.08031v2.pdf

Abstract:
We study, as a concrete case study using the $Λ(\to pπ^-)\barΛ(\to \bar{p}π^+)$ system, whether quantum entanglement in fermion pairs produced at colliders can be certified solely using angular information from final-state decays, while remaining independent of the parity-violating decay parameters $α_Λ$ and $α_{\barΛ}$. Building on a general decomposition of any angular observable in terms of Wigner d-functions, we show that the expectation value must take the form $\mathcal{O}_0+\mathcal{O}_1α_Λ+\mathcal{O}_2α_{\barΛ}+\mathcal{O}_3α_Λα_{\barΛ}$, with coefficients $\mathcal{O}_i$ ($i=0,1,2,3$) linear in the spin-density matrix elements $α_{k,j}α^*_{m,n}$. We obtain the value ranges of observables over the general and separable spaces of $α_{k,j}$, and demonstrate a sufficient entanglement condition for pure states, extending it to mixed states by convexity. In constructing an $α_Λ$- and $α_{\barΛ}$-independent witness from angular observables alone, we find that there are obstacles to probe quantum entanglement via the inequality-type and ratio-type ways. In particular, for the ratio-type criterion ${\langle A\rangle}/{\langle B\rangle}$, the presence of zeros of $\langle B\rangle$ in both the general and separable spaces of $α_{k,j}(k,j=\pm\frac{1}{2})$ results in identical value ranges of ${\langle A\rangle}/{\langle B\rangle}$ in the two spaces (covering the entire real line), thereby precluding any effective criterion. Finally, for this specific system, we present the successful constructions with additional spin information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2510.25056v2
- Title: Generalized Dynamical Duality of Quantum Particles in One Dimension
- Authors: Yu Chen, Xiaoling Cui
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2510.25056v2  pdf=https://arxiv.org/pdf/2510.25056v2.pdf

Abstract:
We prove a generalized dynamical duality for identical particles in one dimension (1D). Namely, 1D systems with arbitrary statistics -- including bosons, fermions and anyons -- approach the same momentum distribution after long-time expansion from a trap, provided they share the same scattering length for short-range interactions. This momentum distribution is uniquely given by the rapidities, or quasi-momenta, of the initial trapped state. Our results can be readily detected in quasi-1D ultracold gases with tunable s- and p-wave interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2511.09560v2
- Title: Resolving the phase of a Dirac topological state via interferometric photoemission
- Authors: Shiri Gvishi, Ittai Sidilkover, Yun Yen, Shaked Rosenstein, Nir Hen Levin, Adi Perelmuter, Omer Pasternak, Costel R. Rotundu, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2511.09560v2  pdf=https://arxiv.org/pdf/2511.09560v2.pdf

Abstract:
The electronic wavefunction is at the heart of physical phenomena, defining the frontiers of quantum materials research. While the amplitude of the electron wavefunction in crystals can be measured with state-of-the-art probes in unprecedented resolution, its phase has remained largely inaccessible, obscuring rich electronic information. Here we develop a quantum-path electron interferometer based on time- and angle-resolved photoemission spectroscopy, that enables the reconstruction of phase information associated with electronic states, as encoded in the photoemission transition amplitudes - with energy and momentum resolution. We demonstrate the scheme by resolving the phase along the Dirac electronic band of a prototypical topological insulator and observe a resonance-associated phase jump as well as a momentum and phase synchronized inversion revealing the helicity of the Dirac cone. We show the interferometer can be optically controlled by the polarization of the absorbed light, allowing a differential measurement of the phase - a crucial component for extracting phase information from an interferogram. This photo-electron-interferometer provides direct experimental access to the phase of electronic transition amplitudes. Its implementation relies on experimentally accessible conditions - such as the presence of a suitable intermediate state and polarization-selective coupling - and can therefore be extended to a wide class of materials.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2604.03569v2
- Title: Impure codes exceeding the pure bounds for quantum local recovery
- Authors: Carlos Galindo, Fernando Hernando, Helena Martín-Cruz, Ryutaroh Matsumoto
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2604.03569v2  pdf=https://arxiv.org/pdf/2604.03569v2.pdf

Abstract:
Existing literature provides several bounds for quantum local recovery, which essentially consider the number of message qudits, the distance, the length, and the locality of the involved codes. We give a family of $J$-affine variety codes that result in impure CSS codes. These quantum codes exceed several of the above mentioned bounds that apply to pure quantum locally recoverable codes. We also discuss a connection between bounds on quantum local recovery and on weight-constrained stabilizer codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2604.06288v2
- Title: Experimental predictions of the $E_8 \times ωE_8$ octonionic unification program : A falsification-oriented catalogue for quantum foundations, particle physics, gravitation, and cosmology
- Authors: Tejinder P. Singh
- Categories: hep-ph (primary); hep-ph; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2604.06288v2  pdf=https://arxiv.org/pdf/2604.06288v2.pdf

Abstract:
The $E_8\timesωE_8$ octonionic unification programme makes empirical claims across quantum foundations, particle physics, gravitation, and cosmology. This catalogue assembles them as possible failure modes rather than a success list, classified by logical strength and distinctiveness. Standing entries include collapse in time with an attosecond cutoff, $m_τ/m_μ=m_s/m_d$, the first-generation $1{:}4{:}9$ pattern, and $α_s(M_Z)/α_{\rm em}(0)=16$. Version~2 upgrades every sector to the dedicated 2026 papers. Neutrinos: the v1 maximal leptonic phase, a removable-rephasing artifact, is corrected to conditional CP conservation, $δ_{CP}^{\ell}\in\{0,π\}$; the minimal Majorana branch commits to inverted ordering with masses $(49.1,\,49.8,\,0.76)$~meV, $Σm_ν\simeq0.10$~eV, $m_{ββ}=18.2\pm1.2$~meV; the three right-handed neutrinos become diluted $\sim\!40$~eV relics closing the matter budget, with a two-epoch dark-radiation fingerprint ($ΔN_{\rm eff}\simeq0.19$ at BBN, $0.05$ at recombination). The second Higgs becomes a full electroweak quartet in a CP-conserving 2HDM near alignment, mass undetermined. Gravitational parity-blindness is derived via three screening theorems, residual violation confined to a quantified operator basket, with CMB TB/EB correlations observable if $r\gtrsim\text{few}\times10^{-3}$ and a Galactic-supernova triple-timing test at $3\times10^{-9}$. CKM: two of four degrees of freedom parameter-free ($|V_{us}|=0.237$, $|V_{cb}|=0.042$), the remainder one complex bridge element, fragilities disclosed. The Tsirelson-bound violation is recorded as mechanism-and-sign with magnitude underived, hence not yet falsifiable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2604.22600v2
- Title: Anomalous Mean-Squared Displacement in Quantum Active Matter from a Wigner Phase-Space Framework
- Authors: Sangyun Lee, Yehor Tuchkov, Alexander P. Antonov, Benno Liebchen, Hartmut Löwen, Giovanna Morigi, Michael te Vrugt
- Categories: cond-mat.soft (primary); cond-mat.soft; quant-ph
- Links: abs=https://arxiv.org/abs/2604.22600v2  pdf=https://arxiv.org/pdf/2604.22600v2.pdf

Abstract:
Active matter is driven out of equilibrium by a local influx of energy. While classical active matter has been extensively studied, the extension of active matter concepts to quantum systems has been explored far less. In this work we develop a full quantum description based on the Wigner function. By introducing a hybrid Wigner master equation that incorporates classical active motion and quantum degrees of freedom, we compute the quantum mean-squared displacement (MSD) using established techniques from classical active matter. We analytically derive the time dependence of the MSD and clarify the conditions under which the characteristic scaling with time $\mathrm{MSD}\sim t^{6}$ emerges, namely the regime of long persistence time and large active noise strength. We also show that, for certain parameter and initial conditions, the MSD can exhibit an even steeper scaling regime $\mathrm{MSD}\sim t^{7}$. In addition, explicit expressions are derived that precisely predict the onset times of $t^6$ and $t^7$ scaling behaviors. Finally, we examine the robustness of these behaviors against quantum fluctuations of the initial state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.04353v2
- Title: Scattering-Induced Loss in Ferroelectric Photonic Devices
- Authors: Jonah Townsend, Enzo Conceição Picinini, Rogério de Sousa
- Categories: physics.optics (primary); physics.optics; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2605.04353v2  pdf=https://arxiv.org/pdf/2605.04353v2.pdf

Abstract:
Ferroelectric materials have colossal optical nonlinearities, but their integration into quantum photonic chips is made challenging by the additional loss mechanisms that they introduce. Here we present a perturbative theory that expresses non-absorptive (elastic) photon scattering-induced loss as a functional of a general spectral density for spatial fluctuations of electric permittivity. We apply the theory to calculations of attenuation coefficients $α$ in slab waveguides in order to compare two distinct loss mechanisms: Interface roughness and ferroelectric domain disorder. Our theory can account for realistic roughness without special symmetry considerations, and it demonstrates how to use electron microscopy images of ferroelectric domains to obtain explicit numerical predictions for $α$. Loss is maximum when the mean domain length is comparable to the wavelength of light (Mie regime), indicating that, for telecom wavelengths, sub-micron domains (Rayleigh regime) or single domain waveguides provide equivalent strategies for reducing loss.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.08307v2
- Title: Chiral-Induced Spin Selectivity Regulates Triplet formation in Heliobacterial Photosynthesis
- Authors: Parul Raghuvanshi, Vishvendra Singh Poonia
- Categories: physics.bio-ph (primary); physics.bio-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2605.08307v2  pdf=https://arxiv.org/pdf/2605.08307v2.pdf

Abstract:
Triplet formation and its regulation have always been of central interest in understanding the photophysical behavior of living systems. In organic systems, excessive triplet formation poses significant challenges, as it can promote photochemical damage and reduce the efficiency of charge separation processes, making its regulation critically important.Here, we present a theoretical investigation of the intrinsic quantum spin dynamics governing triplet formation in the heliobacterial reaction center, a system that operates without any internal magnetic field. Using an open quantum systems approach based on the Lindblad formalism, we simulate the spin-correlated radical pair dynamics occurring during charge separation in the heliobacterial reaction center. The study systematically examines how triplet formation is regulated by variations in two key parameters, hyperfine coupling strengths and recombination rates, and how this regulation is further influenced by the inclusion of chirality-induced spin selectivity (CISS) in conjunction with the radical pair mechanism (RPM). Our results demonstrate that the CISS effect significantly suppresses triplet formation across the parameter space relevant to the heliobacterial molecular environment, revealing an intrinsic quantum protective mechanism operating through spin control in heliobacterial photosynthesis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.09249v2
- Title: Bound-State Spectra of a Lifshitz-Type Dirac Equation in (2+1) Dimensions
- Authors: Lucas K. R. Queiroz, Van Sérgio Alves, Nilberto Bezerra, Luis Fernández, Francisco Peña
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2605.09249v2  pdf=https://arxiv.org/pdf/2605.09249v2.pdf

Abstract:
We investigate a Dirac-type equation in $(2+1)$ dimensions modified by Lifshitz spatial derivatives with dynamical exponent $z=2$, focusing on the spectral properties of bound-states under radial confinement. Analytical solutions are obtained for constant backgrounds, hard-wall confinement, and harmonic potentials, while logarithmic confinement is treated numerically via the Numerov method and complemented by a semiclassical WKB analysis. The resulting spectra exhibit characteristic scaling laws governed by the Lifshitz parameter $b$, including $E - M \propto b/R_0^2$ for hard-wall confinement, $E - M \propto \sqrt{2b}\,ω$ for harmonic trapping, and $E - M \sim α\ln\sqrt{b}$ in the semiclassical regime of logarithmic confinement, where $M$ is a mass scale. These results provide a consistent characterization of how higher-order spatial derivatives modify the energy spectra in two-dimensional Dirac systems and may be relevant for effective descriptions of materials with quadratic low-energy dispersion, such as bilayer graphene and related anisotropic 2D systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.13774v2
- Title: Affiliated operators for classical and quantum control
- Authors: Dimitrios Giannakis, Gage Hoefer
- Categories: math.OC (primary); math.OC; math.DS; math.OA; quant-ph
- Links: abs=https://arxiv.org/abs/2605.13774v2  pdf=https://arxiv.org/pdf/2605.13774v2.pdf

Abstract:
Using techniques from the theory of von Neumann algebras, we propose a framework for addressing questions of controllability of bilinear systems on infinite dimensional Hilbert spaces. In the setup, we assume only that the drift and control terms arising in a bilinear control system are affiliated with a von Neumann algebra of finite type acting on the same Hilbert space. When the control terms satisfy basic norm bound conditions, we prove existence of time-optimal controls. In the more general setting where all operators may be unbounded, we show how the dynamical Lie algebra for the system is still well-defined and may be used to check approximate controllability of the system in question. We discuss how this approach can be applied to classical dynamical systems through the Koopman operator formalism, and investigate potential candidates for the von Neumann algebra which may guide the choice of controls. We illustrate how an affiliation relation naturally arises in both classical and quantum control systems with a few examples.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.19820v2
- Title: Geometric curvature driven by many-body collective fluctuations
- Authors: Alejandro S. Miñarro, Gervasi Herranz
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2605.19820v2  pdf=https://arxiv.org/pdf/2605.19820v2.pdf

Abstract:
Quantum geometry characterizes the variation of wavefunctions in momentum space through their overlaps and relative phases, providing a general framework for understanding many transport and optical properties. It is generally formulated in terms of interband matrix elements, which, entering the response functions, allow obtaining experimental access to the quantum geometric tensor. Recently, it has been emphasized that quantum geometry can also be interpreted in terms of quantum dipole fluctuations in the ground state driven by interband mixing. Here, we extend this picture to include contributions from many-body collective fluctuations, in which propagators and response vertices are dressed dynamically by the interaction with collective modes. Focusing on the Berry curvature, we show that contributions from collective fluctuations can be experimentally distinguished from bare band-geometric contributions, via specific antisymmetric channels in inelastic scattering spectra. We further identify the non-commutative properties of transverse quantum fluctuations as well as non-local-time interactions as the generators of this dynamical curvature in the susceptibility response.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2605.31601v2
- Title: Twin Phases: Intrinsic Deconfined Quantum Criticality
- Authors: Alison Warman, Yuhan Gai, Sakura Schafer-Nameki
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; math.CT; quant-ph
- Links: abs=https://arxiv.org/abs/2605.31601v2  pdf=https://arxiv.org/pdf/2605.31601v2.pdf

Abstract:
We introduce the concept of twin phases for a symmetry $\mathcal{S}$, defined as inequivalent phases, whose order parameters are part of the same generalized charge under $\mathcal{S}$. Stable, direct transitions between such twin phases are never spontaneous-symmetry-breaking transitions, even after (partially) gauging the initial symmetry $\mathcal{S}$: they are phase transitions without hidden symmetry breaking. We illustrate this with an (anomalous) finite group symmetry in 1+1d, which exhibits such intrinsically beyond Landau transition, i.e. an intrinsically Deconfined Quantum Critical Point (DQCP).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-07 13:31
- arXiv: 2606.29944v2
- Title: Soft-Radiation-Induced Decoherence of Heavy-Quark Spin Entanglement at the Electron-Ion Collider
- Authors: Sanskriti Agrawal, Muneeb Zahoor, Raktim Abir
- Categories: hep-ph (primary); hep-ph; hep-ex; hep-th; nucl-th; quant-ph
- Links: abs=https://arxiv.org/abs/2606.29944v2  pdf=https://arxiv.org/pdf/2606.29944v2.pdf

Abstract:
Using the soft-gluon theorem, we identify a soft-recoil mechanism by which unresolved gluon radiation induces decoherence in the spin correlations of heavy quark-antiquark pairs produced in deep-inelastic scattering. We show the eikonal soft contribution preserves the Born spin structure, whereas the subleading soft term generates stochastic recoil-induced rotations of the spin-correlation plane. Upon tracing over the unresolved gluon, these rotations produce an effective dephasing channel: the normal-axis correlation remains unchanged at this order, while the in-plane spin coherences are suppressed. We estimate the resulting reduction of concurrence and Bell-CHSH violation, and propose a radiation-binned EIC observable based on the ratio of in-plane to normal spin correlations. This observable isolates the characteristic anisotropic suppression predicted by the soft-recoil mechanism and provides a measurable handle on radiation-induced spin decoherence of an entangled quark-antiquark pair produced in a deep-inelastic scattering process.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

