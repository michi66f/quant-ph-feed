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

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06602v1
- Title: Real-Time VPN Traffic over ETSI GS QKD 014 Key Delivery with a LuxQuanta NOVA QKD Platform
- Authors: Felipe Paixão, Anderson Altair Tomkelski, Marcus Elias Silva Freire, Isys Nogueira de Sant'Anna, Adriano Humberto de Oliveira Maia, Reinan da Silva Salazar, Ney Ricardo Lopez Junior, João Marcelo Silva Souza
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2607.06602v1  pdf=https://arxiv.org/pdf/2607.06602v1.pdf

Abstract:
This report presents a prototype VPN that uses QKD-derived keys delivered through the ETSI GS QKD 014 API. The VPN encrypts IP traffic with AES-256-GCM, transports ETSI key identifiers in-band, and retrieves matching keys from local KMEs. After validation with a controlled KME simulator, the system was tested on two Jetson Xavier NX devices connected to a LuxQuanta NOVA QKD platform. The experiment successfully transmitted bidirectional real-time audio and video traffic through the VPN for eight continuous hours, demonstrating the feasibility of integrating classical VPN applications with QKD infrastructure through a standardized key-delivery interface.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06654v1
- Title: Localized control of large ion crystals in a Penning trap using a spatial light modulator
- Authors: Allison L. Carter, Jennifer F. Lilieholm, Bryce B. Bullock, Kurt Thompson, Diep Nguyen, John J. Bollinger
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2607.06654v1  pdf=https://arxiv.org/pdf/2607.06654v1.pdf

Abstract:
Penning ion traps as quantum platforms have primarily utilized global control and symmetric Dicke states for quantum simulation and sensing experiments. The introduction of local control greatly increases the power of the platform as a quantum simulator but is technically challenging due to the rapid rotation of the ion crystals. Here we use an ultraviolet-compatible spatial light modulator (SLM) to imprint programmable AC Stark shift patterns with different azimuthal symmetries and gradients that co-rotate with the ion crystals, demonstrating localized coherent control of single plane crystals with greater than 100 ions. Comparisons of the measured ion qubit populations with calculations from independent measurements of the applied AC Stark shift patterns show good agreement, validating the technique and providing a path, with a higher format SLM, for parallelizable, coherent individual ion addressing in Penning traps.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06670v1
- Title: Localized Thermometry via Dayem Bridges Integrated on Superconducting Qubit Chips
- Authors: Ella O. Lachman, Dave P. Pappas, Jayss Marshall, Josh Y. Mutus
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2607.06670v1  pdf=https://arxiv.org/pdf/2607.06670v1.pdf

Abstract:
Accurate knowledge of the on-chip temperature is essential for understanding and optimizing the performance of superconducting qubits, yet direct thermometry at millikelvin temperatures remains challenging. While qubits themselves are sensitive to the temperature of their environment, other factors may affect the qubits` effective temperature, and using them as thermometers with any accuracy requires specialized measurement protocols and qubit designs, limiting their practicality for routine diagnostics and adding complex infrastructure to any hardware testing apparatus. Here we demonstrate a complementary on-chip thermometry method based on superconducting Dayem bridges that are integrated on the same chip as transmon qubits. By extracting the critical current of the Dayem bridge from I-V measurements, we obtain a local, quantitative measure of the chip temperature without the need for microwave calibration or qubit-specific control sequences. To demonstrate the utility of the Dayem bridges as thermometers, we fabricate them in-situ with qubits on the same chip, calibrate the Dayem bridge critical current as a function of temperature, and characterize its resolution and stability at cryogenic temperatures. We additionally perform simultaneous measurements of the Dayem bridge thermometer and qubit excited-state population, and show agreement over the relevant temperature range, validating the method against established qubit thermometry. Furthermore, we correlate the independently measured chip temperature with qubit energy relaxation and dephasing times, demonstrating the utility of this approach for diagnosing temperature-dependent decoherence mechanisms. These results establish integrated Dayem bridges as a simple, non-invasive, and scalable tool for cryogenic hardware development, and on chip thermometry in superconducting quantum circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06672v1
- Title: Spin singlets are useful
- Authors: Silas Hoffman, Edward H. Chen, Matthew Brooks, Stephen Carr, Daniel Volya, Alan Tran, Tyler Keating, Thaddeus D. Ladd, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2607.06672v1  pdf=https://arxiv.org/pdf/2607.06672v1.pdf

Abstract:
We evaluate the utility of the spin-zero manifold of an exchange-coupled array of $N$ spins for tasks in quantum computation and quantum simulation. Since pairs of electrons can be readily initialized into a product state of singlets in semiconducting quantum dot arrays, the full spin-zero manifold is available with exchange-only control, providing a Hilbert space of approximate dimension $2^N/(N/2)^{3/2}$, asymptotically close to the $2^N$ dimension of the full spin Hilbert space. Leveraging the spin-zero manifold enables larger computational space in a given array compared to traditional exchange-only control, in which spin arrays are organized into modular units of $n$ spins comprising $N/n$ encoded qubits, limiting to the exponentially smaller Hilbert dimension $2^{N/n}$. Here we focus on benchmarking metrics for this resource utilization by generalizing cross-entropy benchmarking, mirror benchmarking, and out-of-time-ordered correlators to this system. We show that operating in the spin-zero manifold can accelerate the realization of computational quantum advantage applications in semiconductor-based spin qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06675v1
- Title: Spectral Born machines: classically trainable quantum generative models for discrete data
- Authors: Austin Huang, William Maxwell, Vasilis Belis, Evan Peters, Jason Pye, Soran Jahangiri, Joseph Bowles
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06675v1  pdf=https://arxiv.org/pdf/2607.06675v1.pdf

Abstract:
We present \emph{spectral Born machines}, a class of quantum generative models that results from viewing and generalizing the class of IQP Born machines through the lens of group Fourier analysis. These quantum models exploit the quantum Fourier transform to create an inductive bias that make them naturally suited to learning integer-structured data, while remaining classically hard to sample from in general. Similar to IQP Born machines, spectral Born machines can be trained efficiently at scale on classical hardware via a maximum mean discrepancy loss based on graph spectral analysis, which we make available in a new \emph{tcdq} module of the PennyLane software platform. In numerical experiments, we show how the spectral bias of the model leads to significantly reduced parameter counts compared to unstructured approaches, and demonstrate the scalability of the software by training a 190-qubit model with over 1 million parameters to successfully learn a distribution of 93 nucleotide-long ribosomal RNA. Our results suggest that highly over-parameterized spectral Born machines may be immune to overfitting, even in strongly data-scarce regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06682v1
- Title: Semi-Device-Independent Quantum Key Distribution from Operational Assumptions
- Authors: Anubhav Chaturvedi, Giuseppe Viola, Ekta Panwar, Tushita Prasad, Debashis Saha
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06682v1  pdf=https://arxiv.org/pdf/2607.06682v1.pdf

Abstract:
Semi-device-independent quantum key distribution leaves the measurement devices uncharacterized while placing a trusted assumption on Alice's source. We formulate this source assumption operationally on Alice's four-preparation ensemble as a scalar bound on one of four physically motivated source tasks: full-label guessing, parity guessing, or their normalized composites with label exclusion. For the two-bit random-access code, we derive the exact classical frontier for each of the four source assumptions. Numerically, the BB84 strategy attains the maximal quantum deviation from all four frontiers, while the preparation-depolarized BB84 family and the direct-sum label-leakage family trace complementary branches of the arbitrary-dimensional quantum boundary for the two exclusion-assisted assumptions. Because all four task values are monotone under input-independent quantum channels, the same scalar source bound constrains every Bob--Eve extension compatible with the complete observed behavior. Using a three-setting extension that separates RAC testing from key generation, we obtain two dimension-independent security certificates over this feasible set: lower bounds on the conditional min-entropy and conditional von Neumann entropy, obtained respectively by direct optimization of Eve's key-guessing probability and by prepare-and-measure semidefinite relaxations based on the Brown--Fawzi--Fawzi variational bound. The exclusion-assisted assumptions certify positive key rates down to nearly vanishing preparation visibility, far beyond full-label or parity guessing alone. Under direct-sum label leakage, all four independently optimized rate bounds remain positive at every sampled incomplete-leakage point and vanish only at complete label revelation. These results show that robust semi-device-independent security depends not only on what Eve can identify, but also on what she can exclude.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06683v1
- Title: Universal purification dynamics of monitored Clifford circuits
- Authors: Beatrice Magni, Federico Gerbino, Xhek Turkeshi, Andrea De Luca
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2607.06683v1  pdf=https://arxiv.org/pdf/2607.06683v1.pdf

Abstract:
Quantum circuits under sufficiently weak monitoring purify on a timescale $T_P$ exponentially long in the system size. This slowness underlies a universal purification dynamics, whose quantitative description has so far required the replica trick, with a delicate analytic continuation. We show that monitored Clifford circuits on $L$ qudits of prime dimension $q$ bypass this construction entirely: in the scaling limit at fixed $x = t/T_P(L)$, purification reduces to the Markovian decay of the density-matrix rank, an exactly solvable death process descending from infinity. We compute the full scaling functions in compact form: all Rényi entropies collapse onto a universal curve $\langle S(x) \rangle$. Exact stabilizer simulations at $q=2,3,5$ confirm the predictions, with no fitting parameter for the global model and $T_P$ as the only fitted scale for local brick-wall circuits. Also, the replica problem amounts to a tilted version of the same Markov process, in agreement with exact computations from the Clifford commutant. Finally, the quantization of the rank leaves two hallmarks that distinguish Clifford dynamics from generic monitored circuits: the entropy fluctuations saturate at short scaled times $x\to0$ to an $O(1)$ variance, instead of vanishing, and observables develop a temporal modulation periodic in $\log_q x$, which cannot be captured by the replica approach.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06718v1
- Title: Quantum error correction of a grid-state qubit with state preparation and measurement errors below $10^{-3}$
- Authors: Sara Turcotte, Lucas St-Jean, Amélie L. Pessonneaux, Ross Shillito, Bohdan Kulchytskyy, Eliott Ouellet, Jean Olivier Simoneau, Florian Hopfmueller, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06718v1  pdf=https://arxiv.org/pdf/2607.06718v1.pdf

Abstract:
Grid state qubits offer a hardware-efficient approach to large-scale fault-tolerant quantum computing. They access the information redundancy required for quantum error correction by exploiting the large Hilbert space naturally available in harmonic oscillators. Superconducting architectures are particularly suitable to implement grid state qubits due to their fast and high-fidelity operations. Grid states in superconducting circuits enable quantum error correction (QEC) with performance beyond break-even. However, the state preparation and measurements (SPAM) errors of grid states has been a significant limitation to computational performances. In this work, we leverage high-performance QEC to enable repeat-until-success state preparation of both cardinal and magic states of the single-mode grid-state qubit. We combine this with an improved measurement protocol that corrects for both finite-energy envelope and auxiliary qubit readout errors, and increases robustness to photon loss. Our experiments, using both techniques, achieve a combined state-preparation and measurement error below $10^{-3}$. This represents two orders-of-magnitude improvement over the state of the art, bringing this platform on par with standard SPAM error levels measured in transmon qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06752v1
- Title: Feynman's clock and hierarchy-informed sampling for quantum error mitigation
- Authors: Theo Saporiti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06752v1  pdf=https://arxiv.org/pdf/2607.06752v1.pdf

Abstract:
Near-term physical implementations of quantum algorithms require efficient quantum error mitigation schemes to reduce quantum noise. In this letter we propose a new mitigation technique, by extending the applicability of our BBGKY-ISM scheme from quantum simulations of spin chains to arbitrary quantum circuits. We map executions of quantum circuits using Feynman's clock Hamiltonian to the Hamiltonian dynamics of a corresponding quantum system, whose time evolution obeys a BBGKY-like hierarchy of equations informing the BBGKY-ISM mitigation. We show that the method's classical and quantum overheads are polynomial in the circuit size and in the number of qubits. We apply our method to numerical simulations of tunable Bell state preparation circuits under state-of-the-art quantum noise, and numerically demonstrate its systematic and controllable quantum error reduction capability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06783v1
- Title: Secret Key Rate Analysis of Distribution Matching Algorithms for Discrete-Modulated CV-QKD
- Authors: Micael Dias, Caroline Alves, Gabrielly Roman, Søren Forchhammer
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2607.06783v1  pdf=https://arxiv.org/pdf/2607.06783v1.pdf

Abstract:
Continuous variable quantum key distribution protocols (CV-QKD) with discrete modulation have been intensively investigated to bridge the gap between ideal Gaussian modulation and modern coherent optical communication systems. To mitigate the penalty of discrete modulation, probabilistic constellation shaping (PCS) is applied to the modulation format and is typically performed by distribution matching (DM) algorithms. In this paper, we address the application of DM algorithms to perform PCS in CV-QKD protocols. We investigate the impact of approximating optimized Maxwell-Boltzman distributions with DM algorithms based on Huffman (HDM) and constant composition (CCDM) codes on the protocol's secret key rate (SKR) and tolerance to excess noise. Our results show that specifically symbol-by-symbol HDM degrades the SKR by at least 30\%, whereas CCDM matches the optimal SKR with code length of $10^3$ or more symbols. Furthermore, we also provide a statistical analysis of symbol dependence for both approaches, showing that CCDM must operate with blocks of at least $10^5$ symbols for the correlations become negligible. Finally, we propose an algorithm to generate independent symbols following near-optimal distributions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06837v1
- Title: Entanglement-assisted remote energy transfer
- Authors: Bashir Mojaveri, Rasoul Jafarzadeh Bahrbeig, Mohammad Ali Fasihi, Nasrin Abdi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06837v1  pdf=https://arxiv.org/pdf/2607.06837v1.pdf

Abstract:
Currently, remote energy transfer and immunity to dissipation are hot topics in quantum batteries (QBs). In this work, we propose a protocol to realize energy transfer between two remote atoms (a quantum charger and a quantum battery) each coupled to a separate optical cavity with the cavities connected by a fiber. The cavities and fiber are coupled to their individual baths. After optimizing inter-system couplings to achieve an efficient transfer, we uncover the effect of suppressing dissipation by introducing parity deformation of the cavities fields. We also prove that the charger-battery entanglement is a consumable resource for energy storage: it is initially stored until the charger and battery reach energy balance, and then subsequently consumed to maintain the increase in energy stored in the battery. The present scheme is the first execution of energy transfer to a distant battery assisted by entanglement, which may help better understand quantum thermodynamics and open new possibilities toward harnessing decoherence as a resource to improve the charging performance of QBs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06842v1
- Title: Universal spin-squeezing dynamics in spinor condensates
- Authors: Nikolaos Giovanoudis, Navid Kazemiseresht, Fabio Mezzacapo, Emilia Witkowska, Tommaso Roscilde
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2607.06842v1  pdf=https://arxiv.org/pdf/2607.06842v1.pdf

Abstract:
The production of large-scale entangled states is one of the main goals of next-generation quantum technologies, with an immediate potential for applications in the context of entanglement-assisted quantum sensing. A very promising platform to achieve this goal is offered by ultracold spinor gases, made of atoms with a large internal spin sensitive to magnetic fields. Here we show that the native spin-changing collisions in a spinor Bose-Einstein condensate, combined with an arbitrary quadratic Zeeman shift, can generate scalable spin squeezing in the collective spin of the ensemble, following the universal paradigm of the celebrated one-axis-twisting model. Squeezing dynamics is driven by the quadratic Zeeman shift when this shift is small; and by the spin-changing collisions for large shifts, in the form of stroboscopic squeezing. Turning off the Zeeman shift freezes out the collective-spin dynamics, so that the ensuing collective spin dynamics can be uniquely governed by an external field to be sensed. Our theoretical results pave the way for the use of spinor Bose gases with a large spin in fundamental studies of entanglement, as well as in advanced metrological applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06847v1
- Title: How thermal is a filtered state?
- Authors: Yilun Yang, J. Ignacio Cirac, Mari Carmen Bañuls
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06847v1  pdf=https://arxiv.org/pdf/2607.06847v1.pdf

Abstract:
Quantum many-body states with sufficiently low energy variance can serve as approximations to thermal states, and they may be prepared by energy filtering simple pure states. In this work, we examine how narrow the filter width must be to guarantee thermal behavior. To this end, we analyze the problem in the Floquet regime, where filtered states are found to be equivalent to time averages. This equivalence allows us to reproduce the distinct Rényi-$α$ entropy scalings as reported in [Morettini et al., Physical Review Letters 133, 240401 (2024)]. Crucially, we show that under the Floquet eigenstate thermalization hypothesis, the trace distance between Floquet-filtered states and thermal states is bounded by the square root of filter width. We further demonstrate that these results extend naturally to the conventional Hamiltonian setting by mapping Hamiltonian-filtered states to their Floquet counterparts.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06850v1
- Title: A "squeezed polaron" variational wavefunction for the spin boson model
- Authors: Diego Barberena, Nigel Cooper
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2607.06850v1  pdf=https://arxiv.org/pdf/2607.06850v1.pdf

Abstract:
The localization transition of the sub-Ohmic spin-boson model generates boson bath correlations that are, at low frequencies, analytically inaccessible to standard coherent-state-polaron variational ansatzes. In this paper, we introduce a ``squeezed polaron'' wavefunction incorporating generic Gaussian boson-boson correlations induced by the spin impurity. This gives the correct critical power-law scaling of bath observables near the localization transition together with a systematically improved ground state energy and a more accurate determination of the critical coupling. Our wavefunction captures the correct mean-field nature of the transition in the deep sub-Ohmic region. It also displays non-mean-field critical exponents in the shallow sub-Ohmic regime. Using the squeezed polaron as a starting point, we derive scattering phase shifts for bosons, and show how they encode the emergent energy scale that vanishes at the localization transition.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06858v1
- Title: Explaining the magnitude of Chirality-Induced Spin Selectivity via electron-electron exchange
- Authors: Bence Csakany, Alex J. W. Thom
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2607.06858v1  pdf=https://arxiv.org/pdf/2607.06858v1.pdf

Abstract:
Chiral molecular structure can couple to electron spin, leading to unexpected spin polarization effects. This Chirality-Induced Spin Selectivity (CISS) was first reported for DNA molecules adsorbed on gold but its microscopic origin remains unclear. We demonstrated though simulation that the exchange arising from electron-electron Coulomb interactions within the self-consistent mean field (Hartree--Fock) approximation can yield significant ($\sim 2\%$) spin polarisation for $3$-methylcyclohexanone adsorbed on Cu(111) amplifying a much smaller ($\sim 0.0014\%$) initial bias, consistent with experiment. Symmetry considerations ensure the result is physically meaningful, while its ab-initio nature ensures all parameters are physically realistic. This amplification is connected to existing studies on spin-symmetry breaking in Hartree--Fock, providing a new pathway for understanding the magnitude of CISS as an emergent phenomenon of interacting electrons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06876v1
- Title: XOR Games at Full Tilt: The Hardness of Binary Nonlocal Games
- Authors: Richard Cleve, Eric Culf, Aviv Taller
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2607.06876v1  pdf=https://arxiv.org/pdf/2607.06876v1.pdf

Abstract:
It is well known that the quantum value of an XOR nonlocal game, where the winning condition depends only on the XOR of the two players' output bits, may be approximated in polynomial time. We study a variant of the XOR game model, which we call tilted XOR games, where the winning condition can additionally depend on only one of the output bits. We show that this dramatically increases the expressive power: the computational complexity of the problem of approximating the quantum value of tilted XOR games to constant precision is RE-complete. Also, our result extends to succinct versions of tilted XOR games, where the questions can be polynomial-length binary strings, generated by a polynomial-time verifier.   For classical strategies, the distinction between XOR games and tilted XOR games is inconsequential. Håstad (J. ACM, 2001) shows that they are both NP-complete to approximate, by using a reduction from linear systems to XOR games. Our approach is to show that this is also quantum-sound, but as a reduction from linear system games to tilted XOR games.   Since titled XOR games are a special case of binary games (where each party outputs a single bit), our result implies that binary games are RE-hard to approximate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06888v1
- Title: Correlation Localization in Waveguide QED with Delayed Interactions
- Authors: N. Vera, F. M. Quinteros, P. Barberis-Blostein, P. Solano
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2607.06888v1  pdf=https://arxiv.org/pdf/2607.06888v1.pdf

Abstract:
We study the atom-atom correlation length in an atomic array coupled to a waveguide under the Bragg condition with delayed non-Markovian interactions caused by a finite photon propagation time. Starting from a single excited atom, the excitation partially spreads among all atoms, reaching a steady state. The remaining excitation localizes near the initially excited atom, and the atom-atom correlation length decreases as a power law with the interaction delay. This localization phenomenon reveals how the delay-induced non-Markovian behavior affects the correlation transport in waveguide QED systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06932v1
- Title: Enhanced two-photon sources in a cavity-coupled two-atom system
- Authors: Zhicai Chen, Jun Xu, Deyi Kong, Xiangming Hu, Fei Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06932v1  pdf=https://arxiv.org/pdf/2607.06932v1.pdf

Abstract:
We propose a component-selective scheme for improving two-photon sources in a cavity-coupled two-atom system, where a single cavity mode interacts with two two-level atoms driven by phase-controlled classical fields of the same frequency. By controlling the atomic detunings and driving phase, the system can be tailored toward optimized cavity-field two-photon blockade or strongly correlated fluorescence photon-pair emission. When the two-cavity-photon component is enhanced, the cavity field exhibits optimized two-photon blockade with simultaneous suppression of unwanted one- and three-photon components at a comparable two-photon population. In another parameter regime, strongly correlated fluorescence photon pairs can also be generated from the two atoms by selecting the double-atomic-excitation component in the same two-excitation manifold. This approach provides a route toward high-quality and versatile two-photon sources, with potential applications in few-photon quantum optics and quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06934v1
- Title: Anyon-induced non-Hermitian topological phases
- Authors: Yi-An Wang, Kun Ding, Linhu Li
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2607.06934v1  pdf=https://arxiv.org/pdf/2607.06934v1.pdf

Abstract:
We show that anyonic exchange statistics can activate non-Hermitian point-gap topology in models that are topologically trivial in its absence. The emergent topology oscillates more rapidly with the statistical phase as the anyon number increases, and exhibits a parity dependence on the particle number. A perturbative analysis reveals the mechanism: fractional statistics induces a mismatch between momentum terms that, combined with sublattice-dependent dissipation, produces particle-number-dependent non-reciprocity and complex spectral winding. As these effects rely on the formation and exchange of interaction-bound anyons, our results establish exchange statistics as a resource for enabling non-Hermitian topology under programmed dissipation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06953v1
- Title: A quantum model for synchronizing finite state transition systems
- Authors: Martin Lukac, Khaled El-Fakih, Uraz Turker
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2607.06953v1  pdf=https://arxiv.org/pdf/2607.06953v1.pdf

Abstract:
We propose a quantum model for finding a resetting input sequence (RS) which can take a finite state transition system (FA), to particular state independent of its current state. The complexity of finding such sequences for various types of FA can be NP-Hard or even PSPACE-Complete. To this end, we represent the FA states, inputs, and transition function in quantum space. Accordingly, we propose a model to represent the execution of an input sequence of a particular length $l$ starting form an initial FA state. The model is extended considering the application in superposition of all input sequences of length $l$ to an initial state of the FA. The model is further extended considering the application of all input sequences to all initial states of the FA capturing for every input sequence the collection (ordered list) of states reached by applying the sequence to all states of the FA. The amplitude amplification algorithm is then used as it combines similar collections of reached states while preserving all input sequences that reach these collections. A Grover search for a reached collection where its elements correspond to the same FA state provides a RS for the FA. Our approach offers a quadratic gain over the exponential complexity of traditional brute-force method, which is the only method that can be applied to a general FA class. As a proof of concept we provide results of several simulated FAs on a quantum simulator.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06967v1
- Title: Tomography of a Macroscopic Quantum State influenced by Classical Self-Gravity
- Authors: Wenjie Zhong, Yubao Liu, Yanbei Chen, Haixing Miao, Yiqiu Ma
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2607.06967v1  pdf=https://arxiv.org/pdf/2607.06967v1.pdf

Abstract:
Macroscopic optomechanical systems offer a promising testbed for distinguishing whether gravity acts as a quantum interaction or as a classical field. Schrodinger-Newton (SN) theory is the nonrelativistic limit of semi-classical gravity where quantum matter couples to classical gravity. Based on SN theory, this work investigates how classical self-gravity affects continuous quantum state tomography of a macroscopic mechanical oscillator monitored by variable-angle homodyne detection. In the Schrodinger-Newton (SN) theory, the measurement record arises from a different conditional test mass dynamics from that in quantum-gravity (QG)/standard quantum mechanics, consequently, applying the QG-optimised reconstruction map introduces an additional state-dependent contribution. We show that this contribution makes the reconstructed covariance depend on the chosen set of tomography angles and can drive the SN covariance--after QG filtering--outside the standard Gaussian-covariance domain set by the Heisenberg uncertainty principle. We quantify the resulting QG-SN distinguishability via the Hellinger distance and analyse its dependence on measurement strength and temperature. We then formulate the same issue in the broader setting of nonlinear quantum mechanics: when the system's conditional dynamics during the readout process depends on the state being inferred, the tomographic map acquires nonlinear, model-dependent corrections to the usual Radon or Gaussian reconstruction map.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06994v1
- Title: Operator-frame geometry of non-compact quantum systems with frame-vacuum phase transitions
- Authors: Satoshi Tanaka, Gonzalo Ordonez, Masatoshi Kubota, Hiroto Nakano, Kazuki Kanki
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06994v1  pdf=https://arxiv.org/pdf/2607.06994v1.pdf

Abstract:
We formulate the geometric structure of non-compact bosonic quantum systems in regimes where vacuum instability renders the relevant quantum states non-normalizable, causing conventional state-space quantum geometry -- described by the Berry connection, curvature, and quantum metric -- to become ill-defined. To overcome this breakdown, we develop a formulation of quantum geometry at the level of canonical operator frames, allowing for complexified Bogoliubov-Valatin transformations that lift the requirement that creation operators be Hermitian conjugates of annihilation operators. Canonical operator frames are defined as choices of bosonic creation and annihilation operators realizing the canonical commutation relations. A natural equivalence relation among such frames generalizes the phase ambiguity of quantum states and determines a parameter space that analytically extends the stable-regime parameter space. The space of canonical operator frames forms a principal bundle over parameter space -- the operator-frame bundle -- equipped with a natural Ehresmann connection that defines parallel transport while preserving the canonical commutation relations. In the stable regime, this construction reduces to the Berry connection, while more generally it yields a well-defined operator-space quantum geometric tensor (QGT) that remains valid across vacuum instabilities. Using the framework of rigged Hilbert spaces, we define a notion of quantum frame vacuum and obtain a consistent state-space QGT. Focusing on a single bosonic mode, we demonstrate analyticity of the QGT across the quantum frame-vacuum phase transition and present the corresponding phase diagram on the complexified squeezing-parameter plane. We further introduce a realistic physical setting that allows continuous paths connecting stable and unstable regimes, along which the QGT evolves smoothly across Stokes lines.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07031v1
- Title: Bayesian Gill-Massar Bound: An Attainable Lower Bound for Qubit Parameter Estimation
- Authors: Ke-Han Zhao, Koichi Yamagata, Jun Suzuki
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07031v1  pdf=https://arxiv.org/pdf/2607.07031v1.pdf

Abstract:
We study lower bounds for Bayesian quantum parameter estimation, with a particular focus on qubit models. While several lower bounds on the Bayes risk have been proposed, including the Bayesian symmetric logarithmic derivative (B-SLD) type bound and the Bayesian Nagaoka-Hayashi (B-NH) bound, there is no definite proof available to show they are attainable except for special cases. Thus, identifying attainable bounds together with their corresponding optimal measurement strategies remains a central open problem in Bayesian quantum estimation. In this work, we introduce a new Bayesian lower bound, referred to as the Bayesian Gill-Massar (B-GM) bound, inspired by the logic of Gill-Massar bound in point estimation. We derive an analytical closed-form expression of the bound and show that it is attainable for any qubit model. In particular, we prove that the optimal Bayesian strategy can be realized by a projection-valued measure associated with a single effective direction determined by the weight matrix and the B-SLD-type Fisher information matrix. We provide numerical comparisons between the B-GM, B-NH, and B-SLD-type bounds in higher-dimensional models. Our results show that the B-GM bound has a limitation in high-dimensional models with few parameters, since it can be negative.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07056v1
- Title: Quantum Recurrence Plot Algorithm Based on Quantum Principal Component Analysis
- Authors: Hanhuai Zhu, Jingjing Huang, Zhi-Xi Wang, Shao-Ming Fei
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07056v1  pdf=https://arxiv.org/pdf/2607.07056v1.pdf

Abstract:
Recurrence Plot (RP) is a method employed to analyze the periodicity, chaoticity, and nonlinear characteristics of complex systems. Quantum Principal Component Analysis (QPCA), on the other hand, achieves dimensionality reduction of sample data using density matrices based on quantum circuits. We improve the distance threshold function of the recurrence plot algorithm using a density operator conceptually equivalent to the covariance matrix, integrate it with quantum circuits, and thereby develop a Quantum Recurrence Plot (QRP) algorithm. This algorithm achieves ultra-high efficiency in parallel computing, reduces computational costs, and simultaneously upgrades the traditional grayscale recurrence plot to colored heatmaps, enabling a better revelation of the system's dynamical characteristics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07081v1
- Title: Spectral Chaos Does Not Determine Quantum Mpemba Crossings
- Authors: Ri-Hua Zheng, Yang Xiao, Yu Wang, Ye-Hong Chen, Yan Xia
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07081v1  pdf=https://arxiv.org/pdf/2607.07081v1.pdf

Abstract:
In a symmetry-restoration quantum Mpemba effect, an initial state with stronger local symmetry breaking can lose that memory faster than a state that starts closer to the symmetric manifold. We test whether this local ordering reversal is organized by chaotic thermalization in a clean U(1)-conserving spin chain, comparing spectral level statistics with crossings of the entanglement asymmetry for the same Hamiltonians. We find that Gaussian orthogonal ensemble (GOE)-like level statistics alone do not determine whether Mpemba crossings occur. Across field textures, GOE-like spectra can occur with or without entanglement-asymmetry crossings, and crossings can also appear away from the GOE reference. A near-staggered detuned control further shows that even an inversion of the total charge-sector coherence need not produce an entanglement-asymmetry crossing. Thus the crossing response is controlled not by spectral chaos alone, but by how local charge-sector coherence enters the reduced density matrix.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07093v1
- Title: Phase-Selected Efficient Single-Photon Frequency Conversion via Local Fano Resonance in a Two-Giant-Atom Waveguide-QED System
- Authors: Qing-Ao Xiang, Yan Liu, Xin-Yuan Yang, Ya-Ju Song
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07093v1  pdf=https://arxiv.org/pdf/2607.07093v1.pdf

Abstract:
Efficient single-photon frequency conversion is investigated in a two-giant-atom waveguide-QED system, where a two-level giant atom and a $Λ$-type three-level giant atom couple to a common one-dimensional waveguide. While the $Λ$-type atom provides the inelastic channel, the two-level atom induces secondary coherent coupling, creating multi-path interference for the converted photon. Using the real-space approach and within the Markovian approximation, we derive analytical four-channel scattering amplitudes and reveal that the inelastic transmission spectrum, governed by three complex resonance poles, exhibits a multi-peak interference pattern. By introducing a local single-pole approximation, we reduce this complex spectrum to a local Fano lineshape, decomposing it into a coherent superposition of a local background term and a single-pole resonant term. The interplay between these two terms-controlled by the photon propagation phase between the giant atoms' coupling points-determines the conversion efficiency, with the background suppression condition leading to a Lorentzian reduction. Based on the single-pole resonance weight, we formulate a phase-selection criterion for highly efficient conversion. Compared with both the small-atom and single $Λ$-type giant-atom models, the two-giant-atom scheme achieves substantially enhanced inelastic transmission over a broader frequency-conversion range. This work reveals how phase-controlled local Fano resonance enables high-efficiency frequency conversion, establishing a general paradigm for engineering resonant light-matter interactions in structured quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07124v1
- Title: Room-temperature inversionless diamond nitrogen-vacancy electronic spin maser
- Authors: Ali Fawaz, Sarath Raman Nair
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07124v1  pdf=https://arxiv.org/pdf/2607.07124v1.pdf

Abstract:
We propose a method to create a room-temperature maser operating at approximately 2.9~GHz frequency using an ensemble of negatively charged nitrogen-vacancy electronic spins (NV) in diamond, without requiring population inversion. Our method considers a DC magnetic field of a few milli-Tesla (mT) applied along the perpendicular direction of an ensemble of NV spins aligned along a common axis. This perpendicular magnetic-field creates superposition states of $|m_{\mathrm{s}}=-1\rangle$ and $|m_{\mathrm{s}}=+1\rangle$ of the NV spin's ground state triplet levels and thereby makes it possible to drive all three transitions in the NV spin ground state. We model the system by including optical pumping of the NV spins, near-resonant driving of two transitions, and coupling the third transition to a near-resonant microwave resonator. Numerical estimates using experimentally realizable parameters show that inversionless masing can be achieved inside the microwave resonator using our method. As an application, we show that the output intensity of an inversionless maser ($1.1\times10^{14}$ spins) can be used for magnetic field sensing with a DC sensitivity on the order of a hundred pT/$\sqrt{\mathrm{Hz}}$. Our study opens a new direction in room-temperature diamond NV maser devices for quantum technological applications without the requirement of a strong bias magnetic field, as in conventional NV diamond masers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07138v1
- Title: Dynamical structure factor with a pumping approach on a trapped-ion quantum computer
- Authors: Etienne Granet, Keisuke Murota, Henrik Dreyer, Kentaro Yamamoto, Juan Pedersen, Hidemaro Suwa
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07138v1  pdf=https://arxiv.org/pdf/2607.07138v1.pdf

Abstract:
Dynamical structure factors (DSF) measured with neutron-scattering experiments provide key insights into the structure of materials. Their computation requires both the preparation of an equilibrium state and the implementation of Hamiltonian dynamics. We demonstrate the feasibility of computing DSF on the Quantinuum Reimei trapped-ion quantum computer, comparing the DSF of 1D Heisenberg model on $20$ sites, and that of the copper sulfate crystal. To that end, we introduce a pumping approach for computing the DSF $S(q,ω)$ on quantum computers that enables targeting specific arbitrary values of frequencies $ω$. This method time-evolves the initial state using a time-dependent Hamiltonian perturbed by a source term oscillating at the target frequency $ω$. When targeting only a few frequency values, this approach provides a significant reduction in shot overhead compared to previous methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07167v1
- Title: Macroscopic position-position entanglement by photon recoil in Rydberg atoms
- Authors: Xiao-Feng Shi
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2607.07167v1  pdf=https://arxiv.org/pdf/2607.07167v1.pdf

Abstract:
Entanglement between two spatially separate matter particles can be generated via many means and often resides in the internal states of particles. Here, via Rydberg blockade in two spatially separate neutral atoms, we find that the photon recoil in Rydberg excitation can push one atom microns away provided the other atom exerts a state-dependent Rydberg-mediated blockade. When the atoms are recaptured by optical traps, a position-position entangled state between two spatially separate atoms can emerge. This realizes a Bell state of two atoms, where the entanglement exists in the position of each atom and the distance between the two possible locations of each atom can be in the hundred-micron regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07197v1
- Title: Analytical Landscape of Maximal Magic for Two-Qutrit States and Beyond
- Authors: Marco Knipfer, Alexander Roman, Katia Matcheva, Konstantin T. Matchev
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2607.07197v1  pdf=https://arxiv.org/pdf/2607.07197v1.pdf

Abstract:
Achieving a genuine quantum advantage relies on two distinct non-classical resources that restrict efficient classical simulation: entanglement and magic (nonstabilizerness). We investigate the interplay between these resources by characterizing the Pareto frontiers of extreme magic at fixed entanglement for systems of two qutrits ($d=3$) and two ququints ($d=5$). Unlike the case of two qubits, the Schmidt spectrum for two qutrits features two independent entanglement parameters, resulting in two-dimensional Pareto surfaces. For the lower frontier, we recast the minimal magic as a compact function of concurrence and negativity, with a maximal value of $\ln 2$. For the upper frontier, we determine the maximal stabilizer Rényi entropy to be $M_2 = \ln(81/17) \approx 1.561$, which tightens the previous theoretical bound of $\ln 5\approx 1.609$ and improves on earlier numerical estimates. The maximum magic is achieved at eighteen distinct maxima categorized into three families of six permutation-equivalent spectra. We provide analytical expressions for the maximal magic in the neighborhood of each maximum and for the corresponding maximally magical states which turn out to be Weyl-Heisenberg-covariant fiducial states for mutually unbiased bases. Finally, numerical analysis of two ququints ($d=5$) reveals six permutation-inequivalent maxima with a peak magic value of $M_2 = \ln(625/49) \approx 2.546$. Based on these findings, we conjecture that the maximal magic for a bipartite system of two qudits with prime dimension $d$ is given by $\ln [ d^4 / (2d^2 - 1) ]$, which reproduces the previously known value for qubits, as well as the values derived here for qutrits and ququints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07222v1
- Title: Quantum Computing : A New Frontier for Science and Society
- Authors: Giuseppe Di Molfetta
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07222v1  pdf=https://arxiv.org/pdf/2607.07222v1.pdf

Abstract:
This short report explores the (non exhaustive) current state of quantum technologies, their potential applications, and the challenges that must be addressed to harness their full potential. In particular we will focus on the quantum computer architecture and its ecosystem. Such architecture represents a complex, multi-layered system that integrates quantum and classical components to enable the execution of quantum algorithms. This manuscript is then organized as follows : first we will introduce the quantum processing unit, the lowest layer of a quantum computer. Then we will progress from the lowest to the higher layer of the system architectures : measurement, circuit control, error correction and mitigation system, the quantum compiler and finally the software stack, with particular emphasis on the interactions between these components

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07223v1
- Title: Non-Abelian Thouless pumping based on the global adiabatic criterion in Rydberg synthetic lattices
- Authors: Jin-Kang Guo, Jin-Lei Wu, Chuan-Cun Shu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07223v1  pdf=https://arxiv.org/pdf/2607.07223v1.pdf

Abstract:
We study a quantum implementation of non-Abelian Thouless pumping in Lieb lattices using Rydberg synthetic dimensions. The lattice is encoded in twelve selected microwave-coupled Rydberg levels, forming a three-cell structure with six degenerate zero-energy states. These zero-energy states define the working subspace for cyclic modulation of the microwave couplings, while the remaining bright states provide the dominant leakage channels at finite evolution time. To choose the relative timing of the Gaussian pulses, we introduce a global adiabatic criterion (GAC), which evaluates the mean value and temporal fluctuation of a nonadiabatic factor obtained from a representative $Λ$-type transfer paradigm. With the resulting timing applied to the full twelve-level pumping dynamics, composing two elementary pumping cycles in opposite temporal orders produces distinct projected population maps. It is exactly consistent with noncommuting matrix-valued adiabatic operations in the zero-energy subspace. We numerically simulate the non-Abelian Thouless pumping using the Lindblad master equation with state-dependent Rydberg loss and representative perturbations. The results show that the GAC-selected timing within the same Gaussian pulse family gives higher target-state population than two literature-adapted Gaussian pulse schedules over the simulated parameter ranges. This quantum implementation of non-Abelian Thouless pumping, enabled by the GAC, marks a major milestone in finite-time geometric control and paves the way for transformative applications in holonomic quantum computing with Rydberg synthetic lattices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07225v1
- Title: Quantum Boomerang Effect in Time-Crystalline Structures
- Authors: Qi-wen Peng, Krzysztof Sacha, Chu-hui Fan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07225v1  pdf=https://arxiv.org/pdf/2607.07225v1.pdf

Abstract:
The quantum boomerang effect (QBE) is a unique dynamical signature of Anderson localization, characterized by a launched wavepacket that initially drifts but ultimately returns to its initial position due to fundamental quantum interference. In this work, we theoretically establish and quantitatively characterize the QBE in a time-crystalline structure using a periodically driven quantum particle in a one-dimensional potential well. By constructing maximally localized Floquet-Wannier states and introducing temporal disorder, we rigorously map the continuous Floquet dynamics onto a discrete disordered tight-binding lattice. By positioning a detector at a fixed spatial coordinate, we monitor the temporal evolution of the wavepacket, to extract the mean temporal center of mass of the probability density in a time-crystalline structure. This mean temporal center of mass exhibits an initial ballistic expansion, followed by a pronounced U-turn, and ultimately returns to its initial temporal position after long-time evolution. These results confirm the existence of the complete QBE in the time domain. They also demonstrate that non-trivial dynamics can be explored within time-crystalline systems, even though these structures already possess an inherent temporal periodicity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07332v1
- Title: Lecture notes on classical and quantum non-Markovianity
- Authors: Graeme Pleasance
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07332v1  pdf=https://arxiv.org/pdf/2607.07332v1.pdf

Abstract:
The study of non-Markovian quantum processes has attracted significant interest in recent decades, giving rise to several competing notions of quantum non-Markovianity. These notes serve as an introduction to the topic for graduate students familiar with quantum mechanics and probability theory. Owing to the vastness of the literature, we focus on two prominent characterizations of quantum Markovianity based on the divisibility of quantum channels and monotonically decreasing state distinguishability. The correspondence between classical concepts (stochastic matrices, Chapman-Kolmogorov equation) and their quantum analogs (dynamical maps, CP-divisibility) is emphasized throughout.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07336v1
- Title: Resource-Efficient Hybrid Quantum Neighborhood Selection for Large-Scale Molecular Diversity Optimization
- Authors: Nicolas Mendes de Araujo, Lester de Abreu Faria
- Categories: quant-ph (primary); quant-ph; cs.ET; math.OC; q-bio.BM
- Links: abs=https://arxiv.org/abs/2607.07336v1  pdf=https://arxiv.org/pdf/2607.07336v1.pdf

Abstract:
Large-scale combinatorial optimization remains demanding for classical heuristics, particularly when dense Quadratic Unconstrained Binary Optimization (QUBO) formulations induce large memory footprints, high CPU utilization, and long execution times. While near-term quantum processors cannot yet deliver unconditional quantum advantage, hybrid architectures can provide practical value by reducing the resource burden. This paper presents a resource-efficiency study of Hybrid Quantum Neighborhood Selection (HQNS), a framework that decomposes large dense QUBO instances into bounded-width quantum subproblems via stochastic frontier selection. We evaluate HQNS on the Maximum Diversity Subset Selection Problem (MDSSP), focusing on the trade-off between solution quality retention and resource consumption. Benchmarks up to N=1000 candidates show that HQNS preserves 99.9908% of the mean diversity score of an 11-restart parallel Simulated Annealing baseline, while reducing wall-clock time by 94.91%, peak CPU utilization by 64.68%, and peak memory usage by 88.61%. The QPU execution time remains bounded within a 6-7 second envelope across scales, indicating that the quantum component is decoupled from the global QUBO dimension when the frontier size is fixed. These results suggest that HQNS provides a resource-aware pathway for deploying hybrid quantum optimization in practical large-scale settings, serving as an efficient architecture for incorporating near-term quantum processors into classical optimization pipelines.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07338v1
- Title: Quantum simulation of real-world nonlinear dynamics via Koopman method
- Authors: Baoyang Zhang, Dong An, Zhaoyuan Meng, Yefei Yu, Xiaoxiao Xiao, Zhen Lu, Yue Yang
- Categories: quant-ph (primary); quant-ph; cs.AI; physics.flu-dyn
- Links: abs=https://arxiv.org/abs/2607.07338v1  pdf=https://arxiv.org/pdf/2607.07338v1.pdf

Abstract:
Nonlinear dynamics is ubiquitous in nature, ranging from chemical pattern formation to ocean circulation, yet its simulation on quantum computers is fundamentally limited by the unitary nature of quantum evolution. We propose the quantum Koopman method, a data-driven framework that embeds nonlinear dynamics into a learned linear representation and implements the resulting evolution using shallow quantum circuits. This method learns Koopman observables from trajectory data, projects the lifted dynamics onto a finite-dimensional subspace, and decomposes the corresponding non-unitary propagator into parallel spectral channels. We utilize the Koopman method on a superconducting processor to simulate three distinct nonlinear systems, comprising reaction-diffusion dynamics, fluid motion on a sphere, and satellite-derived observations of Gulf Stream currents, employing up to 32 parallel circuits of 10 qubits. These quantum simulations capture the dominant multiscale patterns and statistical signatures of the underlying dynamics, and reveal a transition from performance limited by hardware noise in weakly nonlinear systems to performance limited by finite-dimensional Koopman representations as nonlinear scale interactions increase. This transition identifies a practical boundary for quantum-amenable nonlinear dynamics, establishing a hardware-validated route for simulating moderately nonlinear dynamics on near-term quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07389v1
- Title: Circuit Depth Reduction of One-Ancilla Quantum Differential Equation Solver via Extrapolation
- Authors: Di Fang, Justin Park
- Categories: quant-ph (primary); quant-ph; math.NA
- Links: abs=https://arxiv.org/abs/2607.07389v1  pdf=https://arxiv.org/pdf/2607.07389v1.pdf

Abstract:
Solving linear differential equations is a fundamental task in scientific computing and an important primitive for quantum computing. A recent one-ancilla quantum differential equation solver provides a hardware-friendly and locality-preserving approach with provable performance guarantees, making it highly suitable for the early fault-tolerant and near-term regimes. Its simple circuit structure comes with a natural trade-off: the maximum single-run circuit depth scales as $O (1/ε)$ in the target accuracy $ε$. In this work, we reduce this depth by combining the solver with classical step-size postprocessing. By running the one-ancilla solver at a logarithmic number of finite time step sizes and using classical post-processing to cancel leading discretization errors, we reduce the maximum single-run circuit depth to $O(\mathrm{polylog}(1/ε))$ without adding quantum ancillae or sacrificing locality. Technically, extending extrapolation ideas beyond Hamiltonian and Lindbladian dynamics requires regularity estimates for observable maps under nonunitary evolution, which we obtain through a holomorphic extension of the adjoint evolution. Numerical experiments on the Hatano-Nelson model (ODE) and the convection-diffusion equation (PDE) demonstrate the effectiveness of the approach.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07434v1
- Title: Spectral-width limit on non-Hermitian quantum metrology
- Authors: Jiaxin Liu, Zuoxian Wang, Danyue Ma
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07434v1  pdf=https://arxiv.org/pdf/2607.07434v1.pdf

Abstract:
Engineered loss, gain, and non-reciprocity can sharply amplify a sensor's response, and exceptional points and the skin effect are widely proposed as routes to more precise quantum sensors. Some predict an exponentially large quantum Fisher information, the quantity that sets the best achievable precision, yet whether this amplified response is genuine measurement information has remained unsettled. We prove that it is not. For any open sensor whose parameter is imprinted coherently by a Hamiltonian, with loss, gain, non-reciprocity, and readout held fixed, the quantum Fisher information is capped by a single quantity, the spread between the largest and smallest energy the generator can impart, independent of the non-Hermitian dynamics. Amplification enlarges the response but not the information. The reported exponential gains arise only when that spread is unbounded, and any finite spread, such as a photon-number cutoff, restores the cap. The same limit governs dissipative probe preparation and spectral singularities. For photonic sensors the cap takes an operator form in which the information of any probe, classical or entangled, is set by the photon's dwell time at the perturbation, and it contains the recently derived scattering limits as special cases. Non-Hermiticity thus shapes a sensor's dynamics but does not source its precision, and the generator's spread and the attainable dwell time benchmark future non-Hermitian sensing proposals.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07445v1
- Title: Phase-Programmable Free Electron Quantum States in Synthetic Momentum Space
- Authors: Alatz Alvarez-Ahedo, Miriam Lazo, Tian-Niu Xu, Yiming Pan, Mikel Sanz, Yongcheng Ding
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07445v1  pdf=https://arxiv.org/pdf/2607.07445v1.pdf

Abstract:
Light-electron interactions generate synthetic momentum-space dynamics that can be used to engineer free electron quantum states. Here we develop coherent control protocols in which the optical phase acts as the controllable hopping phase of a Floquet-Bloch momentum lattice. Pontryagin optimization designs phase-only waveforms that prepare selected momentum populations and coherent few-sideband superpositions with programmable relative phases. In a complementary Bragg regime protocol, dynamical phase matching selectively couples neighboring sidebands and enables deterministic sequential state synthesis. Full wave-packet simulations based on the minimal-coupling Hamiltonian identify the tolerance window set by phase noise, detuning, and finite momentum spread. The two protocols expose a speed-selectivity tradeoff between ultrafast multilevel interference control and slower resonant engineering, establishing programmable free electron sidebands as a platform for ultrafast quantum state synthesis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07449v1
- Title: Turing mechanisms in a multimode open quantum system
- Authors: Giorgia Comparato, Francesco Gargano, Rosario Lo Franco
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.07449v1  pdf=https://arxiv.org/pdf/2607.07449v1.pdf

Abstract:
We investigate pattern formation in a finite chain of bosonic modes whose dynamics is governed by a Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) master equation. The model combines local parametric driving and nonlinear damping with nonlocal dissipative couplings between modes that work on different discrete spatial scales. In the classical limit, these mechanisms generate a reaction-diffusion-like dynamics, allowing the emergence of Turing-type instabilities. The key aspect of the analysis is the coexistence and competition of different unstable spatial modes. Depending on the range of parameters, the system may select different stationary nonuniform configurations, oscillatory wave-like states, or regimes in which multiple modes interact before a dominant pattern is established, thus providing a mechanism for pattern selection. We compare the deterministic bifurcation scenario, generated by a reaction-diffusion-like system derived from semiclassical drift dynamics, with the quantum dynamics, derived via the GKSL master equation, using phase-space methods and reduced Wigner functions. The results show how Turing instabilities, mode competition, and pattern selection can be extended to multimode open quantum systems, providing a bridge between nonlinear dynamical systems, dissipative quantum mechanics, and spatial self-organization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07502v1
- Title: Spin Textures and Eigenstate Evolution of Isospectrally Patterned Lattices
- Authors: Peter Schmelcher
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.quant-gas; physics.optics
- Links: abs=https://arxiv.org/abs/2607.07502v1  pdf=https://arxiv.org/pdf/2607.07502v1.pdf

Abstract:
Isospectrally patterned lattices exhibit a composite band structure with a tunable ratio of localized versus delocalized eigenstates that is controlled by the underlying phase gradient. We show that the lattice Hamiltonian can be interpreted as that of a single spin exposed to a rotating magnetic field which is allowed to hop with a spin-flip across the lattice. In the low- and high-energy part of the band the localized states show an envelope of oscillatory character separated by quasi-nodes. Spin peaks occur at the locations of these quasi-nodes and provide a unique spin texture to the eigenstates which becomes increasingly complex with increasing degree of excitation. The crossover from localization to delocalization and vice versa leaves its fingerprints in the Fourier spectrum of the eigenstates: the original bimodal frequency distribution widens with increasing degree of excitation, moves across the spectral window and finally culminates in an extremely narrow frequency peak. In the course of this evolution the spin texture undergoes a rearrangement transition involving different characteristic (ir)regular patterns which we quantify by considering the total variation of the local spin fluctuations. Our results demonstrate the variety of the spectral properties of isospectrally patterned lattices which holds great prospect in particular when considering higher lattice or cell dimensions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07530v1
- Title: The NISQ Trap: Eight Years of Demonstrations the Hardware Was Built to Lose
- Authors: Amit Hagar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07530v1  pdf=https://arxiv.org/pdf/2607.07530v1.pdf

Abstract:
With a single contested exception, every NISQ-era flagship demonstration of "quantum advantage" has been classically reproduced, or closed by a simulability theorem, within eighteen months of its announcement. Six theoretical results from 2024 through April 2026 explain the pattern: the regions of circuit-space NISQ hardware can run with sufficient fidelity coincide with the regions classical algorithms compress efficiently, because the features that admit one (low effective depth, strong algebraic structure, geometric locality) are the features that admit the other. This reading dates the NISQ programme from its 2018 articulation as an interim retreat from the unmet conditions of the 1996 threshold theorems, characterises the eight years that followed as a closed loop in which the demonstrations the hardware could run were drawn from the only regions classical methods could already attack, and locates the exit from the loop where the threshold theorems originally located it: in fault tolerance. The empirical pattern could in principle break with a demonstration that escapes the current simulability results. After eight years and more than thirty advantage-class announcements, the burden of producing such a demonstration falls to the defenders of NISQ.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07539v1
- Title: A Dynamic Multiplexing Policy for a Quantum Repeater
- Authors: Jeroen Grimbergen, Sounak Kar, Michal van Hooft, Conor Bradley, Stephanie Wehner
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07539v1  pdf=https://arxiv.org/pdf/2607.07539v1.pdf

Abstract:
We consider a multiplexed quantum repeater that distributes entanglement between two end nodes. Multiplexing is achieved through optical integration of many quantum chips. Each chip hosts an optically addressable communication qubit and a separate memory qubit. The communication qubit serves as an entanglement generation interface between different quantum chips, and the memory qubit can be used to store entanglement. The quantum chips on the repeater are interconnected using a reconfigurable router, which makes it possible to dynamically assign quantum chips for entanglement generation with either of the two end nodes in every end-to-end communication cycle. We propose a dynamic multiplexing policy in which after an entangled link has been established with one of the end nodes, all remaining quantum chips are assigned to the opposite end node. We compare this dynamic policy to a policy in which the assignment of quantum chips to end nodes is fixed. We consider a parameter regime where on average less than one entangled link is generated per end-to-end communication cycle, which is the relevant regime for near-term quantum networks. We show that in this regime, the dynamic multiplexing policy can lead to a significant improvement in fidelity over a fixed policy, while marginally improving the rate. Moreover, even though the dynamic multiplexing policy requires a deeper, and hence, more lossy, router than the fixed policy, it can still achieve higher secret key rates in the parameter regime studied. This makes dynamic multiplexing with a many-quantum-chip repeater especially relevant for the development of near-term quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07540v1
- Title: Towards Minimax Estimation of High-Order Functionals by Quantum Arguments
- Authors: Qisheng Wang
- Categories: quant-ph (primary); quant-ph; cs.IT; math.ST
- Links: abs=https://arxiv.org/abs/2607.07540v1  pdf=https://arxiv.org/pdf/2607.07540v1.pdf

Abstract:
We propose a novel approach to the minimax estimation of high-order functionals from the perspective of quantum computing. Specifically, for any real number $α\gg 1$, we present two estimators, one for the classical functional $\mathrm{F}_α(P) = \sum_{i=1}^S p_i^α$ of a discrete distribution $P$ and the other for the quantum functional $\mathrm{F}_α(ρ) = \operatorname{tr}(ρ^α)$ of a mixed state $ρ$. These functionals have close connections with the Rényi entropy and the Tsallis entropy. We show that both estimators achieve the minimax optimal $L_2$ rate $α\mathsf{n}^{-1}$ in the range $α\lesssim \mathsf{n} \lesssim α^{3-o(1)}$, where the support size $S$ of $P$ or the dimension of $ρ$ can be much larger than the number of samples $\mathsf{n}$. As a result, both estimators achieve the \textit{optimal} sample complexity $\mathsf{n} \asymp α$, improving upon the prior best upper bounds $O(α^2)$ established by Jiao, Venkat, Han, and Weissman (IEEE Trans. Inf. Theory 2017) for classical functionals and Chen and Wang (COLT 2025) for quantum functionals. Our estimators are constructed under a unified framework using quantum primitives and run in linear time on a quantum computer. This work reveals an unexpected path from quantum computing to statistics, suggesting a conceptually new methodology for functional estimation. It adds to the growing list of quantum proofs for classical theorems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07546v1
- Title: An analytical solution of a quantum system with non-Markovian behavior: The Bixon-Jortner system in time domain
- Authors: Osman Cevheroğlu, Arkadaş Özakın
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07546v1  pdf=https://arxiv.org/pdf/2607.07546v1.pdf

Abstract:
Non-Markovian behavior in quantum systems is often studied in the context of bipartite systems consisting of a system of interest and an environment -- tracing over the environment results in non-Markovian behavior for the subsystem of interest. One may get a Markovian limit in certain regimes, which is studied using the Lindblad master equation, and corrections to this behavior can be obtained by techniques such as the Nakajima-Zwanzig formalism. In this paper, we obtain an exact non-Markovian equation for the dynamics of a simple model system that consists of a direct sum rather than a tensor product of two pieces, namely, a discrete state and an infinite ladder. This system, called the Bixon-Jortner model, was first developed in the quantum chemistry literature but has been utilized by the quantum optics community as a model system with interesting behavior, including a Wigner-Weisskopf limit of exponential decay. We attack the time evolution problem of this system directly in time-domain, and start with an integrodifferential equation describing the time evolution of the discrete state. Using tools from mathematical physics, we transform this equation to a delay differential equation, which makes the non-Markovianity completely transparent, and then we solve the delay equation using an intuitive ansatz. This allows us to obtain the analytic form of the dynamics directly in time domain, and demonstrate decay and revival behaviors coming from the aforementioned delay differential equation. We believe the explicit form of the time-domain non-Markovian equation we obtain and the accessibility the solution techniques we use make our results a useful case study of non-Markovianity in quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07547v1
- Title: Variational Learning with Sparse Long-range Entangling Gates
- Authors: Helene M. Lösl, Aydin Deger, Andrew J. Daley
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2607.07547v1  pdf=https://arxiv.org/pdf/2607.07547v1.pdf

Abstract:
The performance of variational quantum algorithms depends in general on the structure of the parametrized quantum circuit, but the most common ansätze are typically based on local couplings. Motivated by the extended connectivity available with neutral atoms and trapped ions, we examine when structured long-range connectivity provides a useful resource, focusing on sparse power-of-two (PWR2) coupling graphs. Using dynamical Lie-algebra analysis, approximate unitary-design diagnostics, and finite-depth measures of expressibility and entanglement, we examine how these geometries enlarge the accessible operator space. This enlarged space alone is not sufficient to ensure trainability of the parameterized circuit for given target problems, and we explore performance across example problems with and without long-range coupling, identifying where sparse coupling graphs are or are not likely to provide an advantage. We also introduce a variational scheme that maps hierarchical long-range Hamiltonians to geometrically local ones that can be optimized with short-range circuits. Together, these results identify circuit geometry and qubit reconfigurability as task-dependent resources for variational algorithms, relevant to ongoing developments in quantum hardware with long-range connectivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07549v1
- Title: Control Protocols for Entangling Gates for Group-IV Color-Centers in Diamond
- Authors: Jurek Frey, Frank K. Wilhelm, Matthias M. Müller
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07549v1  pdf=https://arxiv.org/pdf/2607.07549v1.pdf

Abstract:
Accurately controlling entangling gates remains a major challenge for quantum technology applications with solid-state spin qubits. Here, we study a group-IV color-center with a strongly-coupled nuclear spin and approach the problem from a quantum control perspective. We show that there are three different types of entangling gates where the entanglement is mediated by the parallel hyperfine-coupling component, the orthogonal one or both. We derive the respective quantum speed limits (QSL) and show by means of dynamical decoupling, resonant driving of single- and double-quantum transitions, quantum optimal control and algebraic gate decomposition how these gates can be realized. We finally discuss the experimental applicability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07550v1
- Title: RL-Guided Quantum-ALNS for Constrained VRP
- Authors: Farzan Moosavi, Bilal Farooq
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07550v1  pdf=https://arxiv.org/pdf/2607.07550v1.pdf

Abstract:
This study develops a hybrid quantum-classical framework for constrained vehicle routing problems, focusing on the pickup-and-delivery problem with time windows. Instead of casting the full routing problem as a stand-alone quantum optimization task, we embed shallow quantum samplers inside the repair phase of an Adaptive Large Neighbourhood Search (ALNS) heuristic. A Deep Q-Network controller decides whether each reduced repair subproblem should be handled by a classical repair heuristic or by a quantum sampler, using features that describe the local repair structure and predicted hardware reliability. IBM Heron experiments are used to calibrate an empirical noise-aware model for local quantum repair circuits. Across the tested instances, quantum repair is admissible in only about 16% of reduced repair states and is not superior on average. However, under selected matched repair budgets, quantum-enabled repair reduces the final gap relative to standard ALNS in 29 of 36 tested settings. These results suggest that near-term quantum sampling is most useful as a selective local repair mechanism rather than as a replacement for classical routing heuristics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07554v1
- Title: RubriQ: Rubric-Guided Group Relative Policy Optimization for Constraint-Aware Quantum Circuit Synthesis
- Authors: Ziqing Guo, Ziwen Pan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07554v1  pdf=https://arxiv.org/pdf/2607.07554v1.pdf

Abstract:
Designing fault-tolerant quantum circuits that are both algorithmically correct and hardware compatible remains a major bottleneck in the transition to scalable quantum computing. We introduce RubriQ, a scalable framework that formulates circuit synthesis as a large language model (LLM) code-generation task, optimized via group relative policy optimization (GRPO). Unlike conventional black-box neural critics, RubriQ employs a domain-grounded programmatic rubric as the reinforcement learning reward function, evaluating circuits for T-gate reduction, hardware topology compliance, and unitary fidelity. To support high-throughput training, RubriQ integrates GPU-accelerated CUDA-Q simulation directly into the reinforcement learning (RL) loop and is deployed on NERSC Perlmutter using DeepSpeed ZeRO2 across multinode NVIDIA A100 clusters. On benchmark tasks, RubriQ achieves a mean T-gate compression of 3.31x, significantly outperforming sparse-reward RL baselines (2.05x), converging 2-3x faster, and maintaining less than 1\% hardware-constraint violations. Validated on IBM and IonQ quantum processors, RubriQ establishes an automated, high-performance computing (HPC)-driven pipeline for generating hardware-ready, fault-tolerant quantum circuits at scale.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07560v1
- Title: Does Born Rule Imply Unitarity of Time Evolution in Quantum Mechanics?
- Authors: Ali Mostafazadeh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07560v1  pdf=https://arxiv.org/pdf/2607.07560v1.pdf

Abstract:
The Born rule for computing probabilities of the outcomes of measurements is an indispensable ingredient of quantum mechanics. The standard textbook description of this rule gives the impression that it implies the unitarity of time evolution. This view relies on the argument that unless the dynamics is unitary, the probabilities of finding all possible outcomes of a measurement do not add up to 1, i.e., the total probability is not conserved. We show that this argument is flawed, and that the general expression for the Born rule ensures the conservation of total probabilities even when the dynamics of a quantum system is not unitary. This applies to the dynamics of ensembles of quantum systems in both pure and mixed states. We discuss the status of the local conservation of probabilities and the arguments against the plausibility of non-unitary time evolutions that are based on the identification of the Hamiltonian operator with the energy observable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07562v1
- Title: Relativistic Quantum Thermometry in AdS Spacetime via Non-Markovian Temperature Sensing
- Authors: Anass Hminat, Abdallah Slaoui, Rachid Ahl Laamara
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07562v1  pdf=https://arxiv.org/pdf/2607.07562v1.pdf

Abstract:
Quantum thermometry based on single-qubit sensor configurations enables the precise estimation of the temperature of a cosmological Anti-de Sitter (AdS) spacetime. In this work, we characterize the achievable estimation accuracy using the Quantum Fisher Information (QFI) and the associated quantum signal-to-noise ratio. For the first time, we introduce an ancillary Unruh-DeWitt detector between the sensor and the thermal bath, enhancing thermometric sensitivity by channeling temperature-dependent information into the probe qubit's coherence. We examine how detector acceleration in AdS space and the choice of boundary conditions modify the probe's thermal sensitivity. Despite the differing geometries, a unified phenomenology emerges: we characterize the scaling of the QFI with respect to temperature, detector energy gap, spacetime curvature, and interaction time. Finally, we identify optimal state preparation and measurement strategies that maximize the QFI, thereby establishing the fundamental limits of precision for non-Markovian sensing in curved spacetime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07572v1
- Title: Analysis of the sample complexity for PAC-learning functions defined over quantum states
- Authors: Jordi Pérez-Guijarro
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07572v1  pdf=https://arxiv.org/pdf/2607.07572v1.pdf

Abstract:
A fundamental question in PAC learning is determining the number of labeled examples required to learn a concept class to a desired accuracy and confidence. In classical learning theory, this quantity is characterized by the VC-dimension, while several quantum generalizations have established analogous results when examples are provided in quantum superposition. In this work, we study a distinct quantum PAC-learning model in which concepts are functions acting on quantum states. We demonstrate that the VC-dimension, although still relevant, fails to fully capture the sample complexity of this model. To further characterize this setting, we develop a new lower bound on the required number of samples and establish an upper bound when the states in the domain are linearly independent. Remarkably, this upper bound has a form similar to the classical PAC-learning bound. We further examine a setting in which the learner receives more informative data and show that the limitations of the VC-dimension persist in this extended model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07586v1
- Title: Fidelity Analysis of Adiabatically Driven Donor Spins as Two-Qubit and Ququart Systems
- Authors: Brian Michon, James Keppens, Ashutosh Kinikar, George Simion, Kristof Moors, Bart Sorée
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07586v1  pdf=https://arxiv.org/pdf/2607.07586v1.pdf

Abstract:
Donor spin systems host a native Hilbert space whose dimension exceeds that of a qubit, meaning they can be used as qudits. Here we study a \ce{Si{:}P} donor spin system through leakage-aware randomized benchmarking (RB) of native ququart $\mathcal{C}_4$ and encoded two-qubit $\mathcal{C}_2^{\otimes 2}$ Clifford groups. We implement adiabatic ramps to operate electron dipole spin resonance (EDSR) pulses at the ionization point, where the electron is shared halfway between the donor and the interface, and to operate electron spin resonance (ESR) pulses near the interface, motivated by the sensitivity of the effective magnetic field to charge noise at the ionization point. By placing the electron near the ionization point only during EDSR control and using sufficiently long displacement ramp durations, leakage outside the computational basis is strongly suppressed, which is crucial for optimized qudit control. We find in our analysis based on leakage RB that $\mathcal{C}_4$ consistently achieves $\sim 40$--$50\%$ lower (lower-bound) error rates $\varepsilon^{\mathrm{LB}}_\mathrm{PT}$ with respect to $\mathcal{C}_2^{\otimes 2}$, due to its reduced circuit complexity. These results indicate that donor spin qudits benefit from genuine qudit operation as opposed to imposed encoded qubit operation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07597v1
- Title: Quantum Software Engineering in Practice: FPGA and AI Integration for Quantum Certification
- Authors: Marcos Guillermo Lammers, José Manuel Suárez, Adrián Pousa, Luis Mariano Bibbó, Alejandro Fernández
- Categories: quant-ph (primary); quant-ph; cs.SE; eess.SY
- Links: abs=https://arxiv.org/abs/2607.07597v1  pdf=https://arxiv.org/pdf/2607.07597v1.pdf

Abstract:
The emergence of Quantum Software Engineering (QSE) responds to the need for systematic, disciplined, and quantifiable approaches to the development, operation, and maintenance of quantum software. Within this context, quantum computer certification represents a significant challenge: verifying that quantum devices produce valid entangled states despite hardware imperfections, noise, and decoherence. This paper presents QAccCert, a hybrid certification framework developed following QSE principles, demonstrating how heterogeneous technologies like FPGAs and Artificial Intelligence can be integrated for quantum processing. The framework implements entanglement certification through CHSH inequality violation in ideal quantum simulations using Qiskit AerSimulator. Through LLM-guided optimization, the system achieves 99.94% of the theoretical maximum of $2\sqrt{2}$, evidencing more efficient parameter space exploration than random search. These simulated results illustrate how QSE methodologies, combined with strategic technology interconnection, can be applied for practical and scalable quantum certification on real NISQ hardware in future work. This study provides a concrete case study of systematic quantum software development.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07603v1
- Title: Operational Collapse Region in Repeaterless Loss-Dephasing Quantum Channels
- Authors: Ufuk Korkmaz, S. Elham Mousavigharalari, Deniz Türkpençe
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07603v1  pdf=https://arxiv.org/pdf/2607.07603v1.pdf

Abstract:
The distribution of entangled photon pairs over standard optical fiber is a fundamental requirement for the realization of the quantum internet. However, real-world deployment is severely bottlenecked by the interplay of amplitude damping (photon loss) and phase noise (birefringence). In this paper, we numerically investigate the degradation of dual-rail polarization entanglement in telecom C-band fiber links. We demonstrate a critical disparity between the physical survival of quantum correlations and their practical utility in standard communication protocols. By evaluating the unconditional logarithmic negativity against the post-selected teleportation fidelity, we identify a distinct ``operational collapse region'' -- a distance window where the channel retains true quantum entanglement, yet standard coincidence-based detection architectures fail to provide any advantage over classical strategies. Furthermore, we reveal that the width of this inaccessible region exhibits a non-monotonic dependence on the phase noise rate, implying that simply minimizing fiber dephasing does not necessarily optimize the operational efficiency of the network. These findings provide vital guidelines for the design of practical quantum communication links.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07607v1
- Title: Covariant Approximate Quantum Codes for Protected Analog Computation
- Authors: Mariia Elovenkova, Hong-Ye Hu, Susanne F. Yelin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07607v1  pdf=https://arxiv.org/pdf/2607.07607v1.pdf

Abstract:
Quantum error correction compatible with continuous symmetries is a fundamental problem in quantum information and a possible route to robust analog quantum simulation. Because the Eastin-Knill theorem forbids exact codes with continuous transversal symmetries, we construct explicit $SU(d)$-covariant approximate codes that exploit permutation symmetry to spread logical information uniformly across all physical subsystems. For one-, two-, and three-qudit erasures at known locations, we prove worst-case purified-distance scaling $Θ(1/N)$, matching approximate Eastin-Knill lower bounds up to constants, and we extend the reduced-state analysis to general flagged local noise. For single-qudit erasure, we construct an explicit near-optimal decoder from the Petz recovery map. We then use these codes as building blocks for encoded analog dynamics. Symmetry-preserving Hamiltonians generate block-structured dynamical Lie algebras implementable transversally, while controlled symmetry-breaking terms serve as non-transversal resources for universal dynamics. These results provide explicit non-Abelian covariant codes and a framework for robust analog quantum simulation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07614v1
- Title: Multi-stage Quantum Amplifier Readout Chain
- Authors: Logan Howe, Andrea Giachero, Michael Vissers, Corwin Shiu, Shannon Duff, Jason Austermann, Johannes Hubmayr, Joel Ullom
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07614v1  pdf=https://arxiv.org/pdf/2607.07614v1.pdf

Abstract:
Multi-stage cryogenic readout chains with a wide bandwidth and added noise within a few quanta of the quantum limit are frequently constructed using traveling-wave parametric amplifiers (TWPAs) as the first stage, and a semiconductor amplifier as the second stage. Unfortunately for highly-scaled superconducting detector arrays, or quantum information systems, and space-based observatories, the power dissipation of the semiconductor amplifier becomes problematic from the perspective of available cryogenic cooling power at \mbox{3~K to 4~K}. Here we demonstrate a readout chain based on a two-stage kinetic inductance TWPA (KTWPA). This quantum-amplifier-based-readout-chain (QARC) provides sufficient gain that a cryogenic semiconductor follow-on amplifier can be eliminated without degradation of the system noise. In this way, the QARC dissipates approximately three orders of magnitude less power than readout chains containing semiconductor amplifiers while adding noise of less than 2~quanta over a 1~GHz bandwidth. In addition, by leveraging the high power handling of kinetic inductance technology, the QARC maintains an input compression point of -93~dBm, which exceeds that of many contemporary Josephson-junction-based parametric amplifiers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07629v1
- Title: Analysis of polarization drift of optical signals over deployed aerial-inground fiber connections
- Authors: Aneesh Ramaswamy, Nageswara S. V. Rao, Joseph C. Chapman, Muneer Alshowkan
- Categories: quant-ph (primary); quant-ph; physics.data-an; physics.optics
- Links: abs=https://arxiv.org/abs/2607.07629v1  pdf=https://arxiv.org/pdf/2607.07629v1.pdf

Abstract:
Polarization measurements of a classical 1550-nm signal are collected and analyzed on 15-km hybrid aerial-inground fiber connections over 11 months. The spectral area and spectral moments9 of mHz-resolution Fast-Fourier-Transform (FFT) of these measurements are extracted, and related to temperature, humidity, wind speed, and time of day. Spectral area correlations show a strong11 diurnal structure: daytime maxima align with temperatures/wind speed peaks and humidity dips, with lower levels during the night. These diurnal patterns also show seasonality, with higher13 mean and variance in summer than winter. A random forest regressor is used to estimate FFT features from environmental measurements, informed by a theoretical model

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07634v1
- Title: QCNN with Rough Path Signature Kernels
- Authors: Leonardo Nogueira Falabella, Vasily Sazonov
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2607.07634v1  pdf=https://arxiv.org/pdf/2607.07634v1.pdf

Abstract:
Time series analysis plays a vital role across a wide range of scientific and engineering domains but poses substantial computational challenges. A major difficulty arises from the time reparameterization invariance of time series data, which complicates the extraction of meaningful temporal features. In this work, we address the problem of time series classification by exploring the application of quantum computation techniques. We propose a hybrid quantum-classical architecture that integrates recent advances in quantum neural networks with the mathematical framework of path signatures, mitigating the impact of time reparametrization invariance. The architecture employs feature layers that compute a signature kernel between pairs of input paths, consisting of a reference path and a target path for classification, using either classical or quantum variational linear solvers (VQLS). These feature layers are followed by a Quantum Convolutional Neural Network (QCNN) to perform downstream learning tasks. We evaluate several realizations of the proposed architecture, differing in QCNN configurations, on a binary classification task involving time series representations of handwritten digits. Our experiments demonstrate the potential advantages of implementing path signature kernel layers within quantum circuits and provide an analysis of the computational limitations associated with the VQLS component.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07691v1
- Title: Faster quantum linear system solver beyond the condition number
- Authors: Alexander M. Dalzell, Jianqiang Li, Yuan Su
- Categories: quant-ph (primary); quant-ph; cs.DS; math.NA
- Links: abs=https://arxiv.org/abs/2607.07691v1  pdf=https://arxiv.org/pdf/2607.07691v1.pdf

Abstract:
The spectral condition number is a widely adopted measure of worst-case cost for quantum linear system solvers. Yet it can significantly overestimate the actual runtime for a typical problem instance. We present two quantum algorithms that produce the normalized solution $|x\rangle$ of linear system $Ax=| b \rangle$ to accuracy $ε$ with complexity independent of the condition number $κ=\lVert A^{-1}\rVert$. We focus on the standard input model where $A$ is accessed through a block encoding and $| b \rangle$ is prepared by a unitary. But we also introduce an affine dilation model that encodes $A$ and $| b \rangle$ jointly, allowing further refinements of the query complexity. Our truncation-based solver makes an optimal number of queries to $| b \rangle$ and $\operatorname{\mathbf{O}}\left(κ_{\mathrm{eff}}\operatorname{polylog}\left(\frac{κ_{\mathrm{eff}}}ε\right)\right)$ queries to $A$. We prove a family of upper bounds on the effective condition number, including $κ_{\mathrm{eff}}\leq\frac{\lVert(A^\dagger A)^{-t/2}|x\rangle\rVert^{1/t}}{ε^{1/t}}$ for positive even integer $t$ and $κ_{\mathrm{eff}}\leq\frac{\lVert A^{-1\dagger}(A^\dagger A)^{-(t-1)/2}|x\rangle\rVert^{1/t}}{ε^{1/t}}$ for positive odd $t$, overcoming the $κ$-barrier. Our filtering-based solver is extremely simple with a favorable runtime prefactor. In particular, the solver has query complexity $6\frac{\lVert A^{-1\dagger}|x\rangle\rVert}ε\ln\left(\frac{1}ε\right)$ to leading order when the solution norm is known. We then present a similarly simple solution norm estimator with the same asymptotic cost up to logarithmic factors. Our quantum linear system solvers thus substantially improve a recent algorithm of Li, enabling faster quantum linear system solving beyond the condition number.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07701v1
- Title: Multi-channel collective dissipation via the symmetric irreducible representation of SU(4)
- Authors: M. Lutsukh, M. Bazarsana, T. Begzjav, G. O. Ariunbold
- Categories: quant-ph (primary); quant-ph; math-ph; physics.atm-clus
- Links: abs=https://arxiv.org/abs/2607.07701v1  pdf=https://arxiv.org/pdf/2607.07701v1.pdf

Abstract:
We specialize Agarwal's multi-level collective spontaneous-emission formalism to the four-level case by formulating it in the fully symmetric \SU(4) representation of $N$ identical atoms. In the irreducible representation $(N,0,0)$, the occupation-number basis forms a tetrahedral weight lattice on which the six embedded $\mathfrak{su}(2)$ transition subalgebras act as ladder operators. From these algebraic factors we obtain a compact Pauli-type population-rate equation and a closed-form expression for the total emitted intensity that apply to any combination of open dipole channels. The formalism is then specialized to the seven dipole-allowed four-level topologies -- tripod, inverted tripod, Y, inverted Y, double-$Λ$, closed cascade, and diamond -- and the resulting rate equations are solved numerically for atom numbers up to $N=50$. In every case the emitted intensity develops a delayed cooperative burst whose peak height obeys a power law $I_{\mathrm{peak}}=aN^{p}$ with topology-dependent parameters $(a,p)$; the fitted exponents lie in the range $1.81\lesssim p\lesssim 1.92$, indicating a superlinear. The \SU(4) tetrahedral flow and the seven configuration-dependent transients together provide a unified geometric picture of multi-channel collective dissipation in four-level atomic ensembles.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06584v1
- Title: A Term-Rewriting Semantics for Pure Quantum States
- Authors: Dan-Adrian German
- Categories: physics.pop-ph (primary); physics.pop-ph; cs.ET; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06584v1  pdf=https://arxiv.org/pdf/2607.06584v1.pdf

Abstract:
In 2017, Terry Rudolph introduced an elementary rewriting system that relies on a representation of quantum states as misty states to accurately describe the basics of quantum circuits and quantum computation to high-school and middle-school students. The accessibility and effectiveness of the system are remarkable: every calculation can be done to good-enough accuracy, and perhaps with a small overhead, using just a tiny, universal set of gates chosen to take advantage of a remarkable mathematical result by Yaoyun Shi, leveraging another powerful result by A. Y. Kitaev. The misty formalism greatly simplifies calculations and makes them accessible to first-time learners using only simple arithmetic, and without sacrificing accuracy; it, too, is universal, inasmuch as you can use it to do any quantum calculation with maybe just a small overhead. We don't advocate that we should recast all of quantum theory into this formalism. The misty state picture is a good way of getting people to the heart of some nontrivial quantum theory without having to first absorb a huge amount of (what might initially seem largely) irrelevant math. Our argument is that the misty formalism can effectively be used to facilitate a transition to the full, conventional quantum-mathematical apparatus. To this end, we start by reviewing the original proposal, consider its strengths and limitations, and show it in action via entanglement swapping. We then extend the formalism through a new category of (irreducible) misty states acting as fixed points, and present the GHZ game in this new, general setting and representational semantics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06689v1
- Title: Local Markov Order and Global Inference in Many-Body Dynamics
- Authors: Thomas Iadecola
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; nlin.CG; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06689v1  pdf=https://arxiv.org/pdf/2607.06689v1.pdf

Abstract:
We consider how the presence of conserved charges affects memory in a classical stochastic process, the symmetric exclusion process, with an observer constantly measuring a single site. We find that the observer's measurement record becomes Markovian (i.e., loses memory) on a timescale that depends on their knowledge of the global charge, namely the total particle number. In particular, when the global charge is unknown a priori, the observer's time series Markovianizes on a timescale constrained by their ability to learn it from their measurement record. Augmenting the observer's record with bulk measurements drives a charge-learnability transition between charge-fuzzy and -sharp phases. We show that the memory timescale tracks the learnability timescale, diverging in the fuzzy phase and remaining finite in the sharp phase.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06716v1
- Title: Mesoscopic routers and single-pole double-throw switches for electronic heat
- Authors: José Balduque, Rafael Sánchez
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06716v1  pdf=https://arxiv.org/pdf/2607.06716v1.pdf

Abstract:
The unavoidable dissipation of heat in electronic nanostructures is a crucial problem, specially when their operation requires low temperatures. It demands finding devices able to control and redirect the excess heat, ideally without perturbing the electrostatic environment. We propose three-terminal junctions working either as thermal routers or as thermal single-pole double-throw switches controlled by a single external knob. Two models are discussed based on resonant tunneling energy filters and different couplings to the heat source: (i) Phase-coherent contact via a scanning tip modulates the relative amount of the two output currents via position-dependent quantum interference; (ii) Coupling via a gate voltage tunable filter selectively switches one of the currents in the presence of dephasing. In the later case, we find that the heat flow using ideal filtering is bounded by fourth the open conductor current.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06751v1
- Title: Majorana physics in a Luttinger liquid with attractive interactions
- Authors: Francesco Debortoli, Nitya Cuzzuol, Luca Barbiero, Fabian Grusdt
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06751v1  pdf=https://arxiv.org/pdf/2607.06751v1.pdf

Abstract:
Majorana zero modes are the hallmark of topological superconductivity. In one-dimensional systems, these zero modes are usually introduced in the context of gapped, mean-field models that do not conserve particle number, such as the Kitaev chain. By non-locally encoding a conventional fermion across spatially separated Majorana zero modes, these systems become inherently immune to local decoherence. In this work, we show that signatures of Majorana edge physics persist in a number-conserving, gapless Luttinger liquid of spinless fermions with short-range attractive interactions. We identify the two-point correlator as a sharp diagnostic, revealing an edge-to-edge revival whose sign depends on the fermion-number parity. This revival is robust in the thermodynamic limit, and persists in the excited states of the system and at different fillings. A simple particle-hole ansatz for the ground state of the system with an odd number of fermions captures the physics of the system for a wide range of interaction strengths, interpolating between the free-fermion limit and the strongly interacting Majorana regime. Finally, we propose a concrete protocol to realize this model with ultracold dipolar molecules or atoms in an optical lattice, and to detect the revival via beam-splitter interferometry, opening an experimental route to Majorana physics beyond the conventional gapped-superconductor paradigm.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06760v1
- Title: QANTIS: Hardware-Calibrated Sequential POMDP Belief Updates on IBM Heron
- Authors: Bayram Yuksel Eker, Suayb S. Arslan, Ozgur Nazli, Mustafa Serhat Demirgil, Furkan Deligoz
- Categories: cs.AI (primary); cs.AI; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06760v1  pdf=https://arxiv.org/pdf/2607.06760v1.pdf

Abstract:
Autonomous systems under partial observability act on beliefs, not raw sensor events. QANTIS treats the quantum processor as a calibrated belief-update service in that loop: it receives a prior and an observation model, estimates the rare-event evidence term, and returns an ordinary posterior to a classical planner. This paper asks whether that service can be reused across a sequential Tiger POMDP horizon on present IBM Heron hardware without corrupting the planner-facing posterior. We answer with a controlled hardware case study rather than an end-to-end autonomy or wall-clock speedup claim. The study compares no amplification, guarded Grover amplification, and all-step fixed-point amplification on the same trajectory, then checks whether the returned posterior would change the downstream action. All-step FPAA preserves the Tiger posterior across the reported 8-step and 12-step primary runs, and the 20-step and 32-step controls remain inside the same operating band. In every reported decision check, the hardware posterior and the exact Bayes posterior select the same immediate action. Boundary-aware BIQAE stabilizes amplitude estimation near zero and near one, while a rare-event sweep maps the logical sample-complexity envelope for one-in-a-million evidence. The result is an operating envelope for a hardware-calibrated belief-update primitive, not a standalone hardware-advantage claim.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06870v1
- Title: Phase transitions and uberholography of holographic pure-state geometries
- Authors: Ning Bao, Keiichiro Furuya, Jacob March
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06870v1  pdf=https://arxiv.org/pdf/2607.06870v1.pdf

Abstract:
We study the error-correcting properties of pure-state holographic geometries, in which mixed boundary subregions are replaced, via the surface/state correspondence, by the Ryu--Takayanagi (RT) geodesic bounding their entanglement wedges. In AdS$_3$/CFT$_2$ we derive a cross-ratio threshold relation $η'/η= e^{ΔH/2}$ for the connected/disconnected transition of the entanglement wedge when two holes are punched in such a geometry. The quantity $ΔH$ is sourced entirely by geodesics ending on RT boundaries. It shifts the standard two-interval threshold $η= 1/2$, and we classify when its sign is fixed by the pattern of hole endpoints. Turning to code properties, we show that the recursive hole-punching underlying uberholography cannot start within an RT-boundary, while an untouched asymptotic boundary can still fractalize, and we find numerically that in the configurations we study it does so with the universal fractal dimension $α\approx 0.786$. The resulting upper bounds on price and distance are nevertheless procedure dependent. In the configurations we study, punching holes on the asymptotic boundary while retaining the RT-boundary yields strictly tighter bounds than first tracing out the RT-boundary and then fractalizing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06938v1
- Title: First constraint on Born-rule violations at high-energy colliders
- Authors: Antony Valentini, Mira Varma
- Categories: hep-ph (primary); hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06938v1  pdf=https://arxiv.org/pdf/2607.06938v1.pdf

Abstract:
We obtain an experimental constraint on possible Born-rule violations at high-energy colliders. We model Born-rule violations with differential scattering cross sections $dσ/dΩ$ subject to an angular smearing by a narrow Gaussian of width $\varepsilon$ (with respect to $x=\cosθ$ for scattering angle $θ$). For large-angle Bhabha ($e^{+}e^{-} \rightarrow e^{+}e^{-}$) scattering, at a centre-of-mass energy $\sqrt{s}=29\, \mathrm{GeV}$, data from the PEP collider at SLAC allow us to set an upper bound of $\varepsilon<0.042$ at $95\%$ confidence. This corresponds to a Gaussian smearing over an angular range of twice the experimental bin width, and hence provides a physically meaningful limit on deviations from the Born rule. Future prospects for improving this limit are discussed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06941v1
- Title: Visualizing modified spin-wave wavefronts near magnetic defects and domains using nitrogen-vacancy centers
- Authors: Wenxin Cheng, Chang Liu, Dekun Shen, Jiaxin Li, Shangyuan Wang, Hongyu Wang, Miming Cai, Jihao Xia, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06941v1  pdf=https://arxiv.org/pdf/2607.06941v1.pdf

Abstract:
Direct, real-space imaging of spin-wave propagation and wavefronts in magnetic materials is crucial for advancing both fundamental understanding of spin dynamics and the development of functional devices. This, however, remains a significant challenge, especially in materials with complex magnetic characteristics at the nanoscale. Here, we employ scanning nitrogen-vacancy center spectroscopy to achieve visualization of spin waves in two archetypical magnetic films: yttrium-iron-garnet and lanthanum strontium manganese oxide. We reveal a wavelength-dependent spin-wave filtering effect near point-like magnetic scatterers and a modified spin wavefront in antiferromagnetically coupled stripe domains. The spin-wave characteristics are explained using micromagnetic simulations and analytical calculations. These findings point to possible fine control of spin-wave propagation near complex magnetic structures and extend the scope of spin-wave imaging based on nitrogen-vacancy centers beyond uniform magnets.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07044v1
- Title: Absolute frequency measurement of the $^{176}$Lu$^+\,(^{3}\mathrm{D}_1)$ standard against the NRC-FCs2 fountain with $2.6\times10^{-16}$ uncertainty
- Authors: K. J. Arnold, Bin Jian, Zhao Zhang, Qi Zhao, Qin Qichen, N. Jayjong, M. D. K. Lee, Scott Beattie, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07044v1  pdf=https://arxiv.org/pdf/2607.07044v1.pdf

Abstract:
We report an improved absolute frequency measurement of the $^{176}$Lu$^+\,(^{3}\mathrm{D}_1)$ optical frequency standard, evaluated via a remote link to the NRC-FCs2 caesium fountain primary frequency standard. Operating a single ion clock with 94.2% uptime over 10 days, and using an ambiguity-resolved precise point positioning (PPP-AR) link over the Global Positioning System (GPS), we determine an absolute frequency of $353\,638\,794\,073\,800.33(9)\,$Hz at a fractional uncertainty of $2.6 \times 10^{-16}$. This agrees with our previous result, which underpins the CIPM recommended frequency value, and reduces the uncertainty by a factor of 3.6.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07125v1
- Title: Density effects in precision laser spectroscopy of exotic helium atoms
- Authors: Hubert J. Jóźwiak, Dimitar Bakalov, Michał Przybytek, Michail Stoilov, Piotr Wcisło
- Categories: physics.atom-ph (primary); physics.atom-ph; physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07125v1  pdf=https://arxiv.org/pdf/2607.07125v1.pdf

Abstract:
Exotic helium atoms act as unique atomic traps for heavy, negatively charged particles, protecting them from nuclear annihilation and nuclear capture on timescales long enough to enable high-precision laser spectroscopy. Such measurements serve as stringent tests of three-body quantum electrodynamics and offer a direct route to determining fundamental particle masses. Motivated by upcoming spectroscopic efforts targeting pionic ($π^{-\,4}\mathrm{He}^+$) and kaonic ($K^{-\,4}\mathrm{He}^+$) helium, we present a rigorous theoretical evaluation of the collisional and density effects governing these systems. Using an ab initio potential energy surface and coupled-channel quantum scattering calculations, we study the collisional stability of the candidate metastable states against inelastic quenching in a cryogenic helium buffer gas. Furthermore, we provide theoretical reference values for the pressure broadening and pressure shift coefficients of the targeted transitions. These results establish an essential benchmark for future experiments, paving the way for refined determinations of the pion and kaon masses.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07342v1
- Title: Horizon-Restricted Leading Soft QED as Open Quantum System
- Authors: Soo-Jong Rey
- Categories: hep-th (primary); hep-th; cs.IT; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07342v1  pdf=https://arxiv.org/pdf/2607.07342v1.pdf

Abstract:
I formulate black-hole-horizon-induced decoherence of charged branch codes as the leading-soft QED restricted to an exterior algebra, formulated as an open quantum system. The fixed-history Feynman--Vernon identity ${\cal F}[J,J]=1$ remains exact. Decoherence enters through the unequal-history influence factor that survives exterior monitoring and belongs to the complementary horizon output. In the coherent eikonal regime, I derive the completely positive Schur channel $({\cal E}_H^{(0)}ρ)_{ab}=\langleΦ_b^{H,(0)}|Φ_a^{H,(0)}\rangle \, ρ_{ab}$. The leading soft input is the eikonal factor, projected onto the horizon radiative algebra. The channel yields Gram-positivity constraints, an exterior quantum-eraser bound, finite-time non-Markovianity tests, soft/hard scaling criteria, and a charged-qutrit interferometer measuring a leading-soft Bargmann holonomy. The holonomy phase is the rephasing-invariant symplectic area of a triangle in horizon soft phase space. I show that its orientation, common-mode, triangulation, and completely positive determinant identities render falsifiable tests beyond pairwise two-path visibility.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07372v1
- Title: Vectorizing Quantum Control: A RISC-V Vector Extension Architecture for Scalable Qubit Systems
- Authors: Xiaorang Guo, Kun Qin, Yanbin Chen, Carsten Trinitis, Martin Schulz
- Categories: cs.AR (primary); cs.AR; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07372v1  pdf=https://arxiv.org/pdf/2607.07372v1.pdf

Abstract:
The Quantum Control Processor (QCP) bridges the gap between compiler toolchains and control electronics, and is responsible for translating compiled quantum circuits into executable instructions that directly manipulate qubits and handle measurement feedback. However, existing designs rely primarily on customized instruction sets, limiting design reuse and requiring significant effort to build supporting toolchains. Furthermore, efficiently addressing qubits and scheduling operations in highly scalable scenarios remains a critical challenge. In this work, we present a vectorized quantum control approach built upon the RISC-V Vector (RVV) engine with a quantum-oriented extension. Leveraging the high parallelism of RVV, our approach can address up to 128 qubits in a single instruction. We also embed parameterized rotation information into the instruction set, enabling dynamic tuning of gate rotations in hybrid quantum-classical programs. To support mid-circuit measurements, we design a hardware-based halt-resume protocol that resumes pipeline execution within 80 $ns$ of receiving the measurement result. Comprehensive evaluation using both RISC-V toolchains and FPGA prototypes demonstrates that our design achieves up to 2.52$\times$ speedup over the baseline in program execution time, with excellent scalability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07556v1
- Title: Entanglement Asymmetry in Random Quantum Automata
- Authors: Olalla A. Castro-Alvaredo, Dávid Szász-Schagrin, Michele Mazzoni
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07556v1  pdf=https://arxiv.org/pdf/2607.07556v1.pdf

Abstract:
We investigate the subsystem entanglement asymmetry in random quantum automaton ensembles, which are generated by permuting the basis states in the Hilbert space and applying global phase shifts. We compute the ensemble average of the $U(1)$ subsystem asymmetry in different connectivity geometries, showing that the late-time limit of the ensemble associated to a 2-local circuit geometry coincides with the all-to-all ensemble average. By focusing on different subsystem sizes, we demonstrate that, similarly to Haar-random circuits, the system locally symmetrizes. However, in sharp contrast to the Haar-random setting, the scale at which symmetrization happens depends on the initial state, a phenomenon we associate with the interplay of conservation of the participation entropy and the uniform exploration of charge sectors. Additionally, we connect the growth of the subsystem asymmetry to the subsystem coherence and show that their growth is characterized by the same symmetrization scale.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07583v1
- Title: Vacuum polarization and renormalized stress-energy tensor of spherical thin shells
- Authors: Julio Arrechea, Cormac Breen, Adrian Ottewill, Lorenzo Pisani, Peter Taylor
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07583v1  pdf=https://arxiv.org/pdf/2607.07583v1.pdf

Abstract:
We provide a thorough study of the properties of the Boulware vacuum in the spacetime of a spherical, static thin shell with a Minkowski interior. To this end, we calculate the renormalized vacuum polarization and stress-energy tensor of massless scalar fields via the extended-coordinate prescription, paying particular attention to their scaling as the shell approaches the black hole limit. Near the surface of the thin shell, we obtain the expected leading-order singular behavior of both quantities via two independent methods: a high-frequency approximation for the modes, and a weak-field approximation. At the center of the shell we find non-local, Casimir-like contributions that remain finite in the black hole limit, and whose backreaction effects we compute via the semiclassical Einstein equations. Away from these regions amenable to analytic treatment, we obtain numerical results for a wide range of shell compactnesses and field couplings. In the black hole limit, we show that the vacuum polarization and renormalized stress-energy tensor outside the shell quickly approach the ones generated by a Schwarzschild black hole, suggesting a possible universality in the vacuum outside highly compact horizonless objects. This work addresses the conceptual and technical aspects necessary for computing renormalized expectation values in matter configurations, laying the foundations for future explorations on the subject.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07591v1
- Title: Geometric Interpretation of Sum Photon Blockade
- Authors: Timur Khudaiberganov
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07591v1  pdf=https://arxiv.org/pdf/2607.07591v1.pdf

Abstract:
We present a geometric interpretation of the sum photon blockade effect in multimode quantum optical systems, such as semiconductor microresonators. The blockade condition \(c^{(n)} \cdot v = 0\) reflects the orthogonality of the \(n\)-photon amplitude vector to a target mode vector in an \(N\)-dimensional Hilbert space, visualized as the confinement of the state to a hyperplane.   A key result is the calculation of the maximum probability of the system remaining in the blockade subspace under the influence of decoherence processes (in particular, dephasing), which determines the practical feasibility and robustness of the effect. This approach extends to higher-order correlators \(g^{(2)}_Σ\) and cross-correlations, enabling the design of scalable quantum devices.   We introduce the concept of "dark-state typicality": as the number of modes \(M\) increases, the dark subspace annihilated by the collective mode operator asymptotically occupies a unit fraction of the \(n\)-boson Hilbert space. This allows the transition from fragile, finely tuned mechanisms to macroscopically robust non-classical light in large multimode bosonic architectures.   We consider continuum collective modes, hypotheses on correlation zeros and invariant manifolds, as well as the relationship between blockade and entanglement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07642v1
- Title: Acoustic-phonon-driven spin-lattice relaxation of the hBN boron vacancy in the sub-THz regime
- Authors: Priyo Adhikary, Pramey Upadhyaya
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07642v1  pdf=https://arxiv.org/pdf/2607.07642v1.pdf

Abstract:
The negatively charged boron vacancy center in hexagonal boron nitride is a premier candidate for quantum sensing, yet its performance is critically limited by longitudinal spin-lattice relaxation time ($T_1$). A microscopic understanding of spin relaxation in the high magnetic field regime remains elusive, as the relevant Zeeman transitions lie far below the optical phonon energies typically invoked to describe the relaxation process. Here, we apply an \textit{ab initio} acoustic mode spin-phonon relaxation theory to this problem and quantitatively reproduce the experimental magnetic field and temperature dependence of $T_1$ without empirical fitting parameters. We demonstrate that the relaxation dynamics are driven by a direct one-phonon emission and absorption process resonant with the Zeeman splitting. Furthermore, we identify the out-of-plane flexural phonon branch which is unique to two-dimensional hosts, as the primary source of decoherence, creating a distinct low-energy spectral function that facilitates spin relaxation. Our results provide a microscopic interpretation of the experimentally observed non-monotonic field and temperature dependence in two-dimensional quantum defect centers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.07692v1
- Title: Error bounds for the truncated Baker--Campbell--Hausdorff and Zassenhaus formulas in unitary problems
- Authors: A. Arnal, F. Casas, J. L. Ruiz-Benito
- Categories: math-ph (primary); math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07692v1  pdf=https://arxiv.org/pdf/2607.07692v1.pdf

Abstract:
The Baker--Campbell--Hausdorff (BCH) formula plays a critical role in many branches of mathematics and physics. It expresses the logarithm of the product of exponentials of non-commuting operators as an infinite series of nested commutators of the operators involved. The Zassenhaus formula is the dual of the BCH formula: the exponential of a sum of operators is written as an infinite product of exponentials involving the operators and their commutators. In practical computations, however, one typically has to truncate the expansions, and so understanding the error committed by the resulting approximations and eventually providing suitable bounds for this error is of paramount interest. In this work we present a general strategy to derive rigorous error bounds and explicit error constants for the BCH and Zassenhaus formulas when the operators involved are skew-adjoint, as is the case for quantum evolution problems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2006.11768v5
- Title: Self gravity decoheres quantum systems
- Authors: Alessio Lapponi, Stefano Mancini, Frank K. Wilhelm, David Edward Bruschi
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2006.11768v5  pdf=https://arxiv.org/pdf/2006.11768v5.pdf

Abstract:
We study the effects of self gravity on the quantum state of a massive and static particle that initially contains quantum coherence between two positions. We employ linearized quantum gravity to obtain the self-interacting dynamics of the particle mediated by gravitons, and find that the effective evolution of the particle's state can be viewed as a quantum channel composed of a unitary, dephasing, depolarizing, and erasure part. Depolarization drives the state towards maximal mixedness while depolarization and dephasing decrease its quantum coherence. Crucially, the intrinsic diffusion and dephasing timescales of the problem determine a relation between the mass and size of the particle that naturally identifies the transition between its classical and quantum regime. Our work therefore provides an explanation for the observational difference between the quantum behavior of small and light systems and the classical behavior of larger and heavier ones.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2212.09794v2
- Title: Quantum max-flow in the bridge graph
- Authors: Fulvio Gesmundo, Vladimir Lysikov, Vincent Steffan
- Categories: quant-ph (primary); quant-ph; math.AG; math.RT
- Links: abs=https://arxiv.org/abs/2212.09794v2  pdf=https://arxiv.org/pdf/2212.09794v2.pdf

Abstract:
The quantum max-flow is a linear algebraic version of the classical max-flow of a graph, used in quantum many-body physics to quantify the maximal possible entanglement between two regions of a tensor network state. In this work, we calculate the quantum max-flow exactly in the case of the bridge graph. The result is achieved by drawing connections to the theory of prehomogenous tensor spaces and the representation theory of quivers. Further, we highlight relations to invariant theory and to algebraic statistics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2302.00821v2
- Title: Designing a Hybrid Digital / Analog Quantum Physics Emulator as Open Hardware
- Authors: Marcus Edwards
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2302.00821v2  pdf=https://arxiv.org/pdf/2302.00821v2.pdf

Abstract:
Existing approaches to emulating quantum computing algorithms using classical electronic hardware are limited by exponential scaling limitations in space, such as circuit size, or time, such as runtime or bandwidth. We introduce a scheme for representing quantum information using analog signals that lessens the bandwidth limitation problem seen in existing approaches [1, 2] by taking full advantage of the ability of analog signals to encode information using RMS voltage as well as frequency and phase. We introduce the mathematical framework for this representation, which separates the information relevant for measurement in the computational basis from information that is not relevant to it. We introduce circuits that take advantage of this separation of concerns to achieve simplifications, for working with quantum information in this representation. We argue that it is comparatively very inexpensive (as low as ~$5.00 / qubit) to outmatch the computing capabilities of existing FPGA based emulators [4], though scaling beyond tens of qubits is still impractical due to constraints of analog hardware module precision. However, our approach opens the door to a new avenue by which classical emulators can hope to improve: by improving on analog electronic circuit performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2304.10144v2
- Title: Kernel Learning by quantum annealer
- Authors: Yasushi Hasegawa, Hiroki Oshiyama, Masayuki Ohzeki
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2304.10144v2  pdf=https://arxiv.org/pdf/2304.10144v2.pdf

Abstract:
The Boltzmann machine is one of the various applications using quantum annealer. We propose an application of the Boltzmann machine to the kernel matrix used in various machine-learning techniques. We focus on the fact that shift-invariant kernel functions can be expressed in terms of the expected value of a spectral distribution by the Fourier transformation. Using this transformation, random Fourier feature (RFF) samples the frequencies and approximates the kernel function. In this paper, furthermore, we propose a method to obtain a spectral distribution suitable for the data using a Boltzmann machine. As a result, we show that the prediction accuracy is comparable to that of the method using the Gaussian distribution. We also show that it is possible to create a spectral distribution that could not be feasible with the Gaussian distribution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2408.03665v3
- Title: When Quantum Nonlocality Does Not Play Dice
- Authors: Ravishankar Ramanathan, Yuan Liu, Stefano Pironio
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2408.03665v3  pdf=https://arxiv.org/pdf/2408.03665v3.pdf

Abstract:
Bell inequality violations are often taken as evidence that quantum nonlocality guarantees intrinsic randomness, effectively playing the role of a "dice" at the heart of many device-independent cryptographic protocols. We show that there exist nontrivial Bell inequalities that are maximally violated by quantum correlations yet fail to certify randomness for any fixed input pair, rendering them useless for a large class of standard device-independent schemes. This is achieved through a systematic construction based on symmetric deterministic extensions of nonlocal games. We further construct maximally nonlocal quantum correlations that are deterministic for every fixed input pair, in the sense that for any chosen inputs they admit a convex decomposition into strategies with fixed outputs for those inputs. In the no-signalling framework, this property corresponds to the "bound randomness" of [Acín et al., PRA 93, 012319 (2016)], where an adversary-once learning the inputs-can steer the correlations into a decomposition that makes the outputs fully predictable, thereby making them useless in most existing device-independent protocols. In contrast, bound randomness is impossible in quantum theory: any quantum correlations that become deterministic once the inputs are revealed must in fact be local. Our results pinpoint the precise limits of determinism compatible with quantum nonlocality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2501.13030v3
- Title: Probing the Quantum Nature of Gravity through Classical Diffusion
- Authors: Oliviero Angeli, Sandro Donadi, Giovanni Di Bartolomeo, José Luis Gaona-Reyes, Andrea Vinante, Angelo Bassi
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2501.13030v3  pdf=https://arxiv.org/pdf/2501.13030v3.pdf

Abstract:
The question of whether gravity is fundamentally quantum remains one of the deepest open problems in modern physics. A recently explored approach consists of testing gravity's ability to entangle quantum systems, which requires preparing and controlling massive quantum states - a formidable experimental challenge. We propose an alternative strategy that circumvents the need for quantum state engineering. We show that, if gravity is classical, it must necessarily modify momentum statistics in a non-unitary way. We consider the corresponding linearized master equation for two harmonically trapped objects interacting gravitationally and establish a lower bound on the noise that any classical gravitational interaction must induce. We then outline an experimental protocol based on a high-precision torsion pendulum at millikelvin temperatures, showing that the predicted diffusion, if present, is in principle detectable with near-term technology. Our approach offers a novel route to testing the classical versus quantum nature of gravity without requiring macroscopic quantum superpositions or precise control of the system's quantum state, thereby significantly reducing the experimental complexity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2502.00037v4
- Title: Superstate Quantum Mechanics
- Authors: Mikhail Gennadievich Belov, Victor Victorovich Dubov, Vadim Konstantinovich Ivanov, Alexander Yurievich Maslov, Olga Vladimirovna Proshina, Vladislav Gennadievich Malyshkin
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2502.00037v4  pdf=https://arxiv.org/pdf/2502.00037v4.pdf

Abstract:
We introduce Superstate Quantum Mechanics (SQM), a theory that considers states in Hilbert space subject to multiple quadratic constraints, with ``energy'' also expressed as a quadratic function of these states. Traditional quantum mechanics corresponds to a single quadratic constraint of wavefunction normalization with energy expressed as a quadratic form involving the Hamiltonian. When SQM represents states as unitary operators, the stationary problem becomes a quantum inverse problem with multiple applications in physics, machine learning, and artificial intelligence. Any stationary SQM problem is equivalent to a new algebraic problem that we address in this paper. The non-stationary SQM problem considers the evolution of the system itself, involving the same ``energy'' operator as in the stationary case. Two possible options for the SQM dynamic equation are considered: (1) within the framework of linear maps from higher-order quantum theory, where 2D-type quantum circuits transform one quantum system into another; and (2) in the form of a Gross-Pitaevskii-type nonlinear map. Although no known physical process currently describes such 2D dynamics, this approach naturally bridges direct and inverse quantum mechanics problems, allowing for the development of a new type of computer algorithms. As an immediately available practical application of the theory, we consider using a quantum channel as a classical computational model; this type of computation can be performed on a classical computer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2502.03524v2
- Title: Sharp Page transitions in generic Hamiltonian dynamics
- Authors: Lauren H. Li, Stefan Kehrein, Sarang Gopalakrishnan
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2502.03524v2  pdf=https://arxiv.org/pdf/2502.03524v2.pdf

Abstract:
We consider the entanglement dynamics of a subsystem initialized in a pure state at high energy density (corresponding to negative temperature) and coupled to a cold bath. The subsystem's Rényi entropies $S_α$ first rise as the subsystem gets entangled with the bath and then fall as the subsystem cools. We find that the peak of the min-entropy, $\lim_{α\to \infty} S_α$, sharpens to a cusp in the thermodynamic limit at a well-defined time we call the Page time. We construct a hydrodynamic ansatz for the evolution of the entanglement Hamiltonian, which accounts for the sharp Page transition as well as the intricate dynamics of the entanglement spectrum before the Page time. Our results hold both when the bath has the same Hamiltonian as the system and when the bath is taken to be Markovian. Our ansatz suggests conditions under which the Page transition should remain sharp even for Rényi entropies of finite index $α$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2505.12974v2
- Title: Countermeasure against detector-blinding attack with estimation of secret-key leakage
- Authors: Dmitry M. Melkonian, Daniil S. Bulavkin, Kirill E. Bugai, Kirill A. Balygin, Dmitriy A. Dvoretskiy
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.12974v2  pdf=https://arxiv.org/pdf/2505.12974v2.pdf

Abstract:
We present a countermeasure against the detector blinding attack (DBA) utilizing statistical analysis of error and double-click events accumulated during a quantum key distribution session under randomized modulation of single-photon avalanche diode (SPAD) detection probabilities via gate voltage manipulation. Building upon prior work demonstrating the ineffectiveness of this countermeasure against continuous-wave (CW) DBA, we extend the analysis to evaluate its performance against pulsed DBA. Our findings reveal an approximately 13 dB increase in the trigger pulse energies difference between default and reduced gate voltage applied under pulsed DBA conditions compared to CW DBA. This heightened difference enables a re-evaluation of the feasibility of utilizing SPAD detection probability variations as a countermeasure and makes it possible to estimate the fraction of bits compromised by an adversary during pulsed DBA.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2508.13150v2
- Title: Driven-Dissipative Dynamics of Measurement-Induced State Transitions
- Authors: Bo-Syun Pan, Yen-Hsiang Lin, Chiao-Hsuan Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.13150v2  pdf=https://arxiv.org/pdf/2508.13150v2.pdf

Abstract:
Dispersive readout plays a central role in superconducting quantum computing, enabling quantum nondemolition measurements through a coupled microwave resonator. While stronger resonator drives can improve measurement speed and fidelity, they can also activate multi-photon resonances that trigger measurement-induced state transitions (MIST) out of the computational subspace. We develop a driven-dissipative framework for MIST that retains the quantum resonator response absent in semiclassical treatments and yields analytically derived transition-rate expressions. The upward and downward transition-rate profiles determine the steady-state populations and finite-time dynamics, enabling quantitative exploration across drive strength and detuning, while capturing the crossover between quantum-resolved and semiclassical-like dynamics. This framework reproduces the quantum dynamics and identifies a strongly driven regime beyond semiclassical Landau--Zener predictions, where delayed population transfer opens a finite-time readout window with high resonator photon population. These results establish MIST as a predictive driven-dissipative process and characterize strongly driven regimes that can be leveraged for measurement optimization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2508.14262v2
- Title: High-temperature limit penalizing high-frequency quantum fluctuations
- Authors: Graeme Pleasance, Erik Aurell, Francesco Petruccione
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.14262v2  pdf=https://arxiv.org/pdf/2508.14262v2.pdf

Abstract:
We revisit the Caldeira-Leggett model of quantum Brownian motion with Ohmic spectral density, and derive an additional contribution to the decoherence kernel in a new high-temperature limit at arbitrarily large cut-off frequency. This contribution reveals a novel mechanism for the classicalization of high-frequency quantum fluctuations. We further demonstrate that it leads to a Markovian master equation that is in guaranteed Lindblad form, and argue that this master equation describes the correct Markovian limit of quantum Brownian motion. Our approach considers in detail the behavior of the decoherence kernel at both the initial and final times of the process on the time scale of the bath memory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2509.16752v2
- Title: Characterizing Phase Fragility via Algorithmically Prepared Ancillas in Repeated-Interaction Models
- Authors: S. Elham Mousavigharalari, Deniz Türkpençe
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.16752v2  pdf=https://arxiv.org/pdf/2509.16752v2.pdf

Abstract:
We study how a phase parameter $φ$, encoded through a single-qubit $H\,\varphi\,H$ gate sequence, is reflected in the quantum Fisher information (QFI) under realistic noisy dynamics. Within a collision-model framework, a probe qubit interacts sequentially with algorithmically prepared reservoir ancillas, leading to a $φ$-dependent steady state from which $\mathcal{F}_φ$ can be evaluated in closed form. In parallel, we perform pulse-resolved open-system simulations of the same gate sequence, using Gaussian-driven control motivated by transmon hardware, to obtain the corresponding pre-measurement density matrix. Despite the distinct physical descriptions, both approaches yield QFI profiles with similar phase dependence on the encoded phase. A quantitative comparison using profile-level similarity metrics further shows that the two descriptions identify the same phase-sensitive regions, although their absolute QFI contrasts differ. This consistency indicates that the steady state of a probe qubit interacting with algorithmically prepared ancillas can capture key features of the phase response observed in noisy device-level implementations. The underlying physical mechanism is the persistence of finite steady coherence in the asymptotic probe state, which retains the phase imprint of the prepared ancillas. Beyond conceptual insight, the steady-state framework provides a model-based, tomography-free diagnostic route for characterizing phase sensitivity. Possible uses in biased-noise error correction, hardware-aware compilation, and pulse-level optimization are therefore presented as future outlook directions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2510.08344v2
- Title: Entanglement Growth from Entangled States: A Unified Perspective on Entanglement Generation and Transport
- Authors: Chun-Yue Zhang, Zi-Xiang Li, Shi-Xin Zhang
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2510.08344v2  pdf=https://arxiv.org/pdf/2510.08344v2.pdf

Abstract:
Studies of entanglement dynamics in quantum many-body systems have focused largely on initial product states. Here, we investigate the far richer dynamics from initial entangled states, uncovering universal patterns across diverse systems ranging from many-body localization (MBL) to random quantum circuits. Our central finding is that the growth of entanglement entropy can exhibit a counter-intuitive non-monotonic dependence on the initial entanglement in many non-ergodic systems, peaking for moderately entangled initial states. To understand this phenomenon, we introduce a conceptual framework that decomposes entanglement growth into two mechanisms: ``build'' and ``move''. The ``build'' mechanism creates new entanglement, while the ``move'' mechanism redistributes pre-existing entanglement throughout the system. Specifically, we demonstrate that MBL dynamics are ``move-dominated'', exhibiting a quantitative agreement with a random SWAP circuit that serves as a model of pure ``move'' dynamics by uniformly distributing pre-existing entanglement. This implies that MBL acts as a redistributor of a hidden entanglement reservoir quantified by the bipartition-averaged entropy. This ``build-move'' framework offers a unified perspective for classifying diverse physical dynamics, deepening our understanding of entanglement propagation and information processing in quantum many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2510.08695v2
- Title: Degeneracy Cutting: A Local and Efficient Post-Processing for Belief Propagation Decoding of Quantum Low-Density Parity-Check Codes
- Authors: Kento Tsubouchi, Hayata Yamasaki, Shiro Tamiya
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.08695v2  pdf=https://arxiv.org/pdf/2510.08695v2.pdf

Abstract:
Quantum low-density parity-check (qLDPC) codes are promising for realizing scalable fault-tolerant quantum computation due to their potential for low-overhead protocols. A common approach to decoding qLDPC codes is to use the belief propagation (BP) decoder, followed by a post-processing step to enhance decoding accuracy. For fast decoding, the post-processing algorithm is desirable to have a small computational cost and rely only on local operations on the Tanner graph to facilitate parallel implementation. To address this requirement, we propose degeneracy cutting (DC), an efficient post-processing technique for the BP decoder that operates on information restricted to the support of each stabilizer generator. DC selectively removes one variable node with the lowest error probability for each stabilizer generator, significantly improving decoding performance while retaining the favorable computational scaling and structure amenable to parallelization inherent to BP. We further extend our method to realistic noise models, including phenomenological and circuit-level noise models, by introducing the detector degeneracy matrix, which generalizes the notion of stabilizer-induced degeneracy to these settings. Numerical simulations demonstrate that BP+DC achieves decoding performance approaching that of BP followed by ordered statistics decoding (BP+OSD) in several settings, while requiring significantly less computational cost. Our results present BP+DC as a promising decoder for fault-tolerant quantum computing, offering a valuable balance of accuracy, efficiency, and suitability for parallel implementation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2511.04446v2
- Title: Robust certification of non-projective measurements: theory and experiment
- Authors: Raphael Brinster, Peter Tirler, Shishir Khandelwal, Michael Meth, Hermann Kampermann, Dagmar Bruß, Rainer Blatt, Martin Ringbauer, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.04446v2  pdf=https://arxiv.org/pdf/2511.04446v2.pdf

Abstract:
Determining the conditions under which positive operator-valued measures (POVMs), the most general class of quantum measurements, outperform projective measurements remains a challenging and largely unresolved problem. Of particular interest are projectively simulable POVMs, which can be realized through probabilistic mixtures of projective measurements, and therefore offer no advantage over projective schemes. Characterizing the boundary between simulable and non-simulable POVMs is, however, a difficult task, and existing tools either fail to scale efficiently, provide limited experimental feasibility or work only for specific POVMs. Here, we introduce and demonstrate a general method to certify non-simulability of a POVM by introducing a complete hierarchy of semidefinite programs. It provides upper bounds on the non-simulability measure of critical visibility of arbitrary POVMs which are tight in many cases and outperform previously known criteria. We experimentally certify the non-simulability of two- and three-dimensional POVMs using a trapped-ion qudit quantum processor by constructing non-simulability witnesses and introduce a modification of our framework that makes them robust against state preparation errors. Finally, we extend our results to the setting where an additional ancilla system is available.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2511.06488v2
- Title: Generalized State Discrimination for Tunable Quantum Key Distribution
- Authors: Animesh Banik, Md. Shihab Khan, Rafid Masrur Khan, Syed Emad Uddin Shubha, Quazi Muhammad Rashed Nizam
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.06488v2  pdf=https://arxiv.org/pdf/2511.06488v2.pdf

Abstract:
We introduce a tunable framework for generalized quantum state discrimination (GSD) and apply it to quantum key distribution (QKD) through a protocol we call phiQKD. Building upon the two-state B92 protocol, phiQKD replaces the traditional unambiguous state discrimination (USD) measurement with a one-parameter family of hybrid POVMs characterized by a tilting angle $φ$. This allows for continuous control over the trade-off among correct, incorrect, and inconclusive outcomes. While offering improvement in key rate over B92, the primary practical advantage of phiQKD lies in its adaptability to noise and channel imperfections via measurement tunability. By evaluating the protocol under asymptotic, finite-key, and composable security models, we show that, treating quantum measurement as a tunable design parameter, rather than a fixed operation, enables flexible protocol optimization and improved performance under realistic constraints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2512.07561v3
- Title: Exponentially accelerated relaxation and quantum Mpemba effect in open quantum systems
- Authors: Emerson Lima Caldas, Diego Paiva Pires
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.07561v3  pdf=https://arxiv.org/pdf/2512.07561v3.pdf

Abstract:
We investigate the quantum Mpemba effect in the relaxation of open quantum systems whose effective dynamics is described by Davies maps. We introduce a class of unitary transformations constructed from permutation matrices that, when applied to an initial state, (i) suppress the slowest decaying modes of the nonunitary dynamics and (ii) maximize the state's distinguishability from the steady state. The first condition ensures exponentially faster convergence to equilibrium, while the second implies that a quantum system initially further from equilibrium can approach it more rapidly than one that starts closer. This protocol thus realizes a genuine Mpemba effect, and its simulation requires low computational effort. We prove that, for any initial state, there exists a permutation matrix that maximizes its distance from equilibrium with respect to a chosen information-theoretic distinguishability measure. We illustrate our findings for a two-level system, as well as for the nonunitary dynamics of the transverse-field Ising chain and the XXZ chain, each weakly coupled to a bosonic thermal bath. In these cases, the quantum Mpemba effect is demonstrated using the Hilbert-Schmidt distance, quantum relative entropy, and trace distance. Overall, our results provide a versatile framework for engineering a genuine quantum Mpemba effect in Markovian open quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2601.04364v2
- Title: Quantum sensing with critical systems: impact of symmetry, imperfections, and decoherence
- Authors: Yinan Chen, Sara Murciano, Pablo Sala, Jason Alicea
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2601.04364v2  pdf=https://arxiv.org/pdf/2601.04364v2.pdf

Abstract:
Entangled many-body states enable high-precision quantum sensing beyond the standard quantum limit. We develop interferometric sensing protocols based on quantum critical wavefunctions and compare their performance with Greenberger-Horne-Zeilinger (GHZ) and spin-squeezed states. Building on the idea of symmetries as a metrological resource, we introduce a symmetry-based algorithm to identify optimal measurement strategies. We illustrate this algorithm both for magnetic systems with internal symmetries and Rydberg-atom arrays with spatial symmetries. We study the robustness of criticality for quantum sensing under non-unitary deformations, symmetry-preserving and symmetry-breaking decoherence, and qubit loss -- identifying regimes where critical systems outperform GHZ states and showing that non-unitary deformation can even enhance sensing precision. Combined with recent results on log-depth preparation of critical wavefunctions, interferometric sensing in this setting appears increasingly promising.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2604.10592v2
- Title: Post-Cut Metadata Inference Attacks on Quantum Circuit Cutting Pipelines
- Authors: Samuel Punch, Krishnendu Guha, Utz Roedig
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2604.10592v2  pdf=https://arxiv.org/pdf/2604.10592v2.pdf

Abstract:
Quantum cloud providers can identify a user's algorithm and secret problem structure without ever seeing actual quantum data, simply by analyzing routine metadata collected for billing and system management. Existing confidentiality tools such as blind quantum computation and quantum homomorphic encryption protect the quantum payload itself, but they do not protect this classical orchestration metadata. This leaves an unexplored security risk in the logs generated when a large quantum program is split into smaller pieces to fit onto limited hardware, a process known as circuit cutting. These fragments leak sensitive information through what we term the topological transpilation penalty: the unavoidable depth and gate inflation added when a compiler reorganizes a program for a restricted hardware topology. Tests on a 156-qubit production Quantum Processing Unit (QPU) show that traditional timing side-channels fail in this setting, since hardware control-plane delays mask actual quantum execution time. The unique shape of the transpilation penalty acts instead as a persistent structural fingerprint for the hidden workload. Using 12,000 circuit fragments across eight algorithm families, our attack recovers algorithm family and Hamiltonian k-locality with near-perfect accuracy, achieving instance-disjoint AUC = 1.000 for both. This leakage persists under size-holdout evaluation on unseen circuit scales, with AUC = 0.987 and 0.986 respectively. The cutting mechanism is inferred with AUC = 0.991, and hardware topology is recovered well above chance with AUC = 0.818. These results show that circuit cutting exposes algorithmic intent, and potentially proprietary problem structure, through metadata alone, without any need to observe quantum data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2605.05343v2
- Title: Kinetically constrained superradiance
- Authors: Luis Fernando dos Prazeres, Hossein Hosseinabadi, Jamir Marino
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.05343v2  pdf=https://arxiv.org/pdf/2605.05343v2.pdf

Abstract:
We introduce kinetically constrained superradiance, a form of cooperative emission in which interactions imprint configuration-dependent energy shifts on optical transitions, splitting Dicke superradiance into multiple, frequency-resolved collective decay channels. Each channel selectively radiates from distinct many-body spin configurations, generating a hierarchy of dissipative time scales and sequential relaxation dynamics. Unlike conventional superradiance, where permutation symmetry enforces relaxation to a trivial steady state, configuration-selective emission can trap finite-momentum spin-wave excitations and stabilize long-lived entanglement. Remarkably, these correlations are generated purely by dissipation in the absence of entangling coherent dynamics. Our results point to modern superradiant experiments as scalable resources for dissipative engineering of correlated quantum states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2605.08332v2
- Title: Optimal FALQON for Quantum Approximate Optimization via Layer-wise Parameter Tuning
- Authors: Michael Mancini, Shabnam Sodagari
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2605.08332v2  pdf=https://arxiv.org/pdf/2605.08332v2.pdf

Abstract:
Feedback-based adaptive quantum optimization (FALQON) is a promising approach for solving combinatorial problems on noisy intermediate-scale quantum (NISQ) devices, requiring only single circuit evaluations per layer. However, standard FALQON relies on fixed hyperparameters that severely limit convergence speed, requiring hundreds to thousands of layers for acceptable solutions. This paper proposes Optimal FALQON, an optimization-based formulation that treats the per-layer time step ($δ_k$) and scaling factor ($M_k$) as decision variables optimized via classical methods. We present a comprehensive empirical study on all 94 non-isomorphic 3-regular graphs with 12 vertices, comparing Optimal FALQON with standard FALQON and multiple QAOA variants. Results demonstrate statistically significant improvements in success probability, evaluation efficiency, and depth-normalized cost across the evaluated benchmarks. Furthermore, initializing QAOA with parameters from Optimal FALQON yields superior warm-start performance compared to fixed initialization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2605.23862v3
- Title: Indefinite probabilities in quantum spacetime: A deepening of unpredictability
- Authors: Vittorio D'Esposito, Giuseppe Fabiano, Domenico Frattulillo
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2605.23862v3  pdf=https://arxiv.org/pdf/2605.23862v3.pdf

Abstract:
Non-commutative spacetime and quantum groups have been argued to capture non-classical features of spacetime and its symmetries in quantum gravity. In this letter, we show that employing the $SU_q(2)$ quantum group to describe rotational symmetry for spin-$\frac{1}{2}$ systems and Stern-Gerlach apparatuses leads to the description of probabilities of outcomes of spin measurements in terms of non-commuting operators. As a result, we obtain an uncertainty principle between different probability operators, realising a notion of indefinite probabilities. This is then reflected in the non-commutativity of the entries of the rotation matrix relating the reference frames of two observers, hence fundamentally preventing them from sharply measuring their relative orientation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.00795v2
- Title: Three-qubit nonlocality paradoxes: beyond GHZ
- Authors: Nadish de Silva, Santanil Jana, Ming Yin
- Categories: quant-ph (primary); quant-ph; cs.LO; math-ph
- Links: abs=https://arxiv.org/abs/2607.00795v2  pdf=https://arxiv.org/pdf/2607.00795v2.pdf

Abstract:
Quantum nonlocality paradoxes, such as that of GHZ, provide maximally sharp logical obstructions to classical probabilistic models of quantum correlations. They are key resources in a broad variety of information-theoretic tasks that exhibit unconditional quantum advantage. For example, in nonlocal games, which are communication tasks that serve as core technical tools in recent landmark results in quantum computational complexity theory.   Their role in establishing quantum advantage motivated their study by Abramsky et al. who introduced an infinite family of three-qubit paradoxes exhibiting novel conditional structure. This was later extended by the present authors into a full classification program.   In this work, we completely classify all three-qubit nonlocality paradoxes established via a biconditional parity proof; this is a very large class of paradoxes that encompasses all earlier-known examples. We do this by introducing a suite of new structural and combinatorial techniques. We find that the landscape of nonlocality paradoxes is far richer than previously understood, violating regularity conditions underlying all prior constructions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.05814v2
- Title: Latency-Constrained Hardware-Aware Quantum Error Correction Co-Design with Adaptive Confidence-Gated Neural Decoding for the Rotated Surface Code
- Authors: Sumit Chongder
- Categories: quant-ph (primary); quant-ph; cs.ET; cs.LG
- Links: abs=https://arxiv.org/abs/2607.05814v2  pdf=https://arxiv.org/pdf/2607.05814v2.pdf

Abstract:
Real-time decoding is a major bottleneck in scaling quantum error correction (QEC) from noisy intermediate-scale quantum (NISQ) devices to fault-tolerant quantum computing. We present an adaptive confidence-gated decoding framework for the rotated surface code that treats decoding as a two-stage inference problem. A lightweight feed-forward neural network performs fast-path decoding for the majority of syndrome measurements, while only low-confidence predictions are escalated to a minimum-weight perfect matching (MWPM) refinement stage. We benchmark the framework on rotated surface codes with distances $d \in \{3,5,7,9,11\}$ under circuit-level depolarising noise using the Stim stabiliser simulator. The evaluation characterises logical accuracy, confidence-controlled accuracy-latency trade-offs, decoding throughput, per-shot latency, and decoding-graph resource scaling. Routing only 3.3%-6.2% of syndromes to the refinement stage improves logical accuracy from 99.21% for the neural-only baseline to 99.81% at a confidence threshold of 0.95 while incurring only a bounded increase in average decoding cost. Neural-decoder throughput saturates near $4.6 \times 10^{5}$ samples s$^{-1}$ at batch size 512 on commodity CPU hardware, indicating that the neural fast path is not the dominant throughput bottleneck beyond code distance $d=7$. We release the complete benchmarking pipeline, trained models, raw benchmark data, and source code, and explicitly distinguish the experimentally validated contributions from the broader hardware-aware QEC co-design roadmap, including hardware-constrained code discovery, GPU-accelerated inference, and multi-noise optimisation, which remain directions for future work.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2607.06488v2
- Title: Design and Benchmarking of a Quantum Photonic Chip
- Authors: Gabriele De Angelis, Nicolò Leone, Alessandro Luongo, Alberto Montanaro, Matteo Sanna, Roberto Siagri, Vito Sorianello, Luigi Tallone, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.06488v2  pdf=https://arxiv.org/pdf/2607.06488v2.pdf

Abstract:
We present the design and benchmarking of RP000, a quantum photonic processor capable of encoding a quantum system in the degrees of freedom of single photons, based on standard CMOS-compatible manufacturing processes, and working at room temperature. We benchmark it against machine learning tasks, evaluating three quantum-classical architectures of increasing complexity. Our experimental results and simulations show that RP000 achieves higher accuracy than classical networks of comparable size in multiple use cases. Compared to a superconducting quantum processor, RP000 exhibits superior noise tolerance. These findings demonstrate that RP000 can provide a scalable route toward efficient quantum applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2303.10069v4
- Title: Bounds on eigenstate thermalization
- Authors: Shoki Sugimoto, Ryusuke Hamazaki, Masahito Ueda
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2303.10069v4  pdf=https://arxiv.org/pdf/2303.10069v4.pdf

Abstract:
The eigenstate thermalization hypothesis (ETH), which asserts that every eigenstate of a many-body quantum system is indistinguishable from a thermal ensemble, plays a pivotal role in understanding thermalization of isolated quantum systems. Yet, no evidence has been obtained as to whether the ETH holds for all few-body operators in a chaotic system; such few-body operators include key quantities in statistical mechanics, such as the total magnetization, the momentum distributions, and their low-order thermal and quantum fluctuations. Here, we formulate a conjecture that for a generic nonintegrable system the ETH holds simultaneously for all $m$-body operators with $m < α_{\ast} N$ in the thermodynamic limit for some nonzero constant $α_{\ast} > 0$. We first show the existence of such nontrivial constants for idealized (pseudo) random-matrix descriptions of many-body eigenstates. We then verify the conjecture for generic spin, Bose, and Fermi systems with local and few-body interactions by large-scale numerical calculations. Our results imply that generic systems satisfy the ETH simultaneously for all few-body operators, including their thermal and quantum fluctuations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2412.01571v3
- Title: Bose-Hubbard model with power-law hopping in one dimension
- Authors: Tanul Gupta, Nikolay V. Prokof'ev, Guido Pupillo
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2412.01571v3  pdf=https://arxiv.org/pdf/2412.01571v3.pdf

Abstract:
We investigate the zero-temperature phase diagram of the one-dimensional Bose-Hubbard model with power-law hopping decaying with distance as $1/r^α$ using exact large scale quantum Monte Carlo simulations. For all $1<α\leq 3$ the quantum phase transition from a superfluid and a Mott insulator at unit filling is found to be continuous and scale invariant, in marked contrast with the Berezinskii-Kosterlitz-Thouless (BKT) scenario that is recovered only for $α>3$. By performing finite-size scaling collapses of the superfluid stiffness and extracting dynamical and correlation-length exponents from the low-energy spectrum, we establish that these transitions define a distinct universality class throughout the long-range regime $1<α\le 3$. Analysis of the single-particle correlation functions and grand canonical phase diagram further reveals a sequence of ordering regimes within the superfluid phase: true long-range order for $α\le 2$, anomalous quasi-long-range order for $2<α\le 3$, and conventional algebraic decay for $α>3$. Our exact numerical results provide a benchmark to compare theories of long-range quantum models and are relevant for experiments with cold neutral atom, molecules and ion chains.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2509.04234v4
- Title: Simple harmonic oscillators from non-semisimple walled Brauer algebras
- Authors: Sanjaye Ramgoolam, Michał Studziński
- Categories: hep-th (primary); hep-th; math.CO; math.RT; quant-ph
- Links: abs=https://arxiv.org/abs/2509.04234v4  pdf=https://arxiv.org/pdf/2509.04234v4.pdf

Abstract:
Walled Brauer algebras $B_N ( m , n ) $ illuminate the combinatorics of mixed tensor representations of $U(N)$, with $m$ copies of the fundamental and $n$ copies of the anti-fundamental representation. They lie at the intersection of research in representation theory, AdS/CFT and quantum information theory. They have been used to study of correlators in multi-matrix models motivated by brane-anti-brane physics in AdS/CFT. They have been applied in computing and optimising fidelities of port-based quantum teleportation. There is a large $N$ regime, specifically $ N \ge (m+n)$ where the algebras are semi-simple and their representation theory more tractable. There are known combinatorial formulae for dimensions of irreducible representations and associated reduction multiplicities. The large $N$ regime has a stability property whereby these formulae are independent of $N$. In this paper we initiate a systematic study of the combinatorics in the non-semisimple regime of $ N = m +n - l $, with positive $l$. We introduce restricted Bratteli diagrams (RBD) which are useful as an instrument to process known data from the large $N$ regime to calculate representation theory data in the non-semisimple regime. We identify within the non-semisimple regime, a region of $(m,n)$-stability, where $ \min ( m, n ) \ge ( 2l -3) $ and the RBD take a stable form depending on $l$ only and not the choice of $ m,n$ within the region. In this regime, several aspects of the combinatorics of the RBD are controlled by a universal partition function for an infinite tower of simple harmonic oscillators closely related, but not identical, to the partition function of 2D non-chiral free scalar field theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2509.18248v2
- Title: Localization and topological signatures under periodic twisting
- Authors: James Walkling, Antonio Štrkalj, F. Nur Ünal
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.dis-nn; cond-mat.mes-hall; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2509.18248v2  pdf=https://arxiv.org/pdf/2509.18248v2.pdf

Abstract:
We theoretically explore a dynamical generalization of the Aubry-André model in two dimensions formed by superimposing two square-lattice potentials. Motivated by the rich physics emerging at different twist angles between the two lattices at equilibrium, we introduce periodic twisting by continuously rotating one of the lattices with respect to the other in the plane. We demonstrate that the distinct time-dependent twisting in this system gives rise to an intricate form of periodic multi-frequency driving that changes with the distance from the rotation axis. We find that the incommensurate nature of the potential no longer plays the pivotal role as it does in the static case. Rather, the tunneling can be understood in terms of a local, spatially varying dynamical localization effect, which we show to yield ring-shaped states localized within the bulk that have interesting transport signatures. Quantifying the eigenstates with the Bott index and local Chern marker, we find that there is a zoo of states with non-trivial topological signatures, the most ubiquitous of which result in relatively uniform ring-shaped regions of the Chern marker. We investigate the origin of these effects from various angles and identify that hybridization between different delocalized ring states plays a vital role. Lastly, we discuss possible experimental realizations in quantum simulation settings. Our results open a new avenue of investigation with periodic twisting inducing a spatially varying multi-frequency drive.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-09 13:32
- arXiv: 2606.30762v2
- Title: Athermality of generalized Gibbs ensembles
- Authors: Riccardo Senese, Bruno Bertini, Katja Klobas, Pasquale Calabrese
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2606.30762v2  pdf=https://arxiv.org/pdf/2606.30762v2.pdf

Abstract:
Integrable quantum systems evolving from non-equilibrium initial states do not thermalize to conventional Gibbs ensembles (GE). Instead, at long times they relax to generalized Gibbs ensembles (GGEs), which incorporate the full set of local and quasi-local conserved quantities. While GGEs have been extensively studied in the literature, a quantitative analytic characterization of how different they are from ordinary GEs is still lacking. In this work, we address this question by employing the concept of athermality, which we define within quantum resource theory as the relative entropy between a given state and the closest thermal state. By means of integrability techniques we compute the athermality for several quantum quenches in paradigmatic integrable models, including the free XY spin chain, the interacting Lieb-Liniger model, the XXZ spin chain, and the harmonic chain. We find that often the athermality becomes anomalously small when the post-quench Hamiltonian is critical in its ground state, despite probing physics at a finite energy density. We also prove that it systematically develops a singularity at criticality, which is inherited from the entropy of the GGE.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07764v1
- Title: Comment on 'Quantum Monge-Kantorovich Problem and Transport Distance between Density Matrices'
- Authors: Tomasz Miller
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.07764v1  pdf=https://arxiv.org/pdf/2607.07764v1.pdf

Abstract:
Friedland et al. [PRL 129, 110402 (2022)] proposed and studied a quantum analogue of the $p$-Wasserstein distance based on quantum cost matrices and quantum couplings. They conjectured that, despite being only a semidistance in general, this quantity is a true distance for a particular quantum cost matrix and for cost matrices in a small neighborhood of it. We disprove these conjectures by exhibiting an explicit family of triples of states for which the triangle inequality fails.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07798v1
- Title: Observation of coherent flux-charge interaction in a gate-tunable fluxonium
- Authors: Brian D. Isakov, Shikhar Singh, Adrian Parra-Rodriguez, David Feldstein-Bofill, Zhenhai Sun, Anders Kringhøj, Svend Krøjer, Alexandre Blais, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2607.07798v1  pdf=https://arxiv.org/pdf/2607.07798v1.pdf

Abstract:
Interactions that mix conjugate variables, such as the flux through a circuit element and the charge across it, lie outside the reach of the elementary couplings of superconducting circuits. Capacitors connect charge to charge, and inductors connect flux to flux, while no two-terminal element couples flux to charge directly. A native flux-charge coupling would thus serve as a circuit primitive in its own right, opening direct routes to non-reciprocity, protected modes, and unconventional readout. In this work, we demonstrate a flux-charge coupling by harnessing a voltage-tunable Josephson junction with parametrically modulated critical current, which mediates the interaction between a classical charge variable and a quantum flux operator. Relying on parity-selection rules in a hybrid superconducting-semiconductor fluxonium, we isolate the flux-charge coupling from other parasitic capacitive contributions and perform cross-quadrature-activated coherent control of states. Critically, we realize a flux-charge coupling that scales linearly with driving amplitude while keeping the transition energy first-order-insensitive to gate voltage. Such unconventional interaction broadens the toolbox of superconducting circuits with a critical missing component that enables the coherent coupling of conjugate variables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07801v1
- Title: Topology from Decoherence
- Authors: Alexandre Chaduteau, Derek Lee, Frank Schindler, Abhinav Prem
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2607.07801v1  pdf=https://arxiv.org/pdf/2607.07801v1.pdf

Abstract:
Decoherence is conventionally regarded as an obstacle to realizing topological quantum phases. This has motivated extensive efforts to suppress noise in candidate topological materials and devices. Here, we show that decoherence can instead induce topological phenomena. We demonstrate this in a lattice system subject to environment-induced dephasing. The noise-averaged dynamics, governed by an interacting quantum master equation, realize a topological phase characterized by a winding number and the non-Hermitian skin effect. The dynamical consequence is striking: the correlated nature of the stochastic noise yields asymmetric diffusion, whose direction is fixed by the winding number and is reversible only through a topological phase transition. This effect is induced purely by interactions, distinguishing it from previous studies of free, effectively single-particle systems. It also disappears upon postselecting measurement outcomes, confirming that it is a genuinely open-system phenomenon with no effective Hamiltonian description. Remarkably, the model remains analytically tractable. Our results establish correlated quantum noise as a route to topology in open many-body systems, beyond free-particle and non-Hermitian Hamiltonian paradigms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07802v1
- Title: Shortcuts to Adiabaticity for non-Hermitian systems in Krylov Space
- Authors: Ankit W. Shrestha, Budhaditya Bhattacharjee, Adolfo del Campo
- Categories: quant-ph (primary); quant-ph; cond-mat.other; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2607.07802v1  pdf=https://arxiv.org/pdf/2607.07802v1.pdf

Abstract:
Shortcuts to adiabaticity (STA) reproduce adiabatic dynamics in finite time, but their counterdiabatic implementation relies on the adiabatic gauge potential (AGP), which is difficult to compute and implement in many-body systems and whose extension to open and non-Hermitian settings has remained largely model-specific. Here, we develop a general, diagonalization-free framework for engineering STA in non-Hermitian systems by representing the AGP in Krylov space. Starting from an integral representation of the counterdiabatic control, we recast the AGP as a nested-commutator series with controlled locality and generate the associated Krylov basis using the bi-Lanczos and Arnoldi algorithms. This reduces the exact or truncated AGP to a sparse tridiagonal or upper-Hessenberg matrix equation that generalizes the Hermitian construction. We demonstrate the method on a decaying two-level atom, where it recovers the exact drive and signals the exceptional point; on the interacting Hatano-Nelson model, where truncated controls rapidly suppress nonadiabatic excitations; and on a PT-symmetric Heisenberg chain, whose AGP norm detects the PT-symmetry-breaking transition. Throughout, the expansion converges with only a small fraction of the full Krylov space, offering a practical route to fast, accurate control of many-body non-Hermitian systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07805v1
- Title: Robust Ion-Photon Entanglement via Polarization-to-Time-Bin Conversion
- Authors: Ana Luiza Ferrari, Denton Wu, Mika A. Zalewski, Norbert M. Linke
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07805v1  pdf=https://arxiv.org/pdf/2607.07805v1.pdf

Abstract:
Time-bin photonic qubits are well-suited for quantum network applications due to their robustness to polarization instability in fiber links and potential for heterogeneous networks. In this work, we implement the first entanglement-preserving polarization-to-time-bin conversion of a photon qubit in an entangled state with a matter qubit. Photons initially generated with polarization encoding are converted to the time-bin basis through a polarization-discriminating asymmetric Mach-Zehnder interferometer. The photonic qubits are generated via the $1092$ nm transition of a $^{88}$Sr$^{+}$ ion. We measure state fidelity bounds of $0.906 \pm 0.011 \le \mathcal{F} \le 0.934\pm 0.011$, with conversion error $< 0.028$, and find this fidelity is unaffected by depolarizing noise even at full depolarization strength.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07808v1
- Title: Non-Local Magic from the Entanglement Spectrum
- Authors: Gianpaolo Torre, Fabio Franchini, Salvatore Marco Giampaolo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07808v1  pdf=https://arxiv.org/pdf/2607.07808v1.pdf

Abstract:
Non-local magic has recently emerged as a fundamental resource for characterizing genuinely non-local non-stabilizer correlations. However, its direct calculation is an intractable numerical problem, except for small systems, and its understanding remains limited. We derive a representation of non-local magic in terms of the Walsh--Hadamard autocorrelations of the entanglement spectrum. Our representation makes the underlying harmonic structure explicit and enables a systematic analysis of its behaviors for various scenarios. We prove that non-local magic can be upper-bounded by an entanglement entropy and we derive exact analytical results for broad classes of quantum states, characterizing the scaling of non-local magic for volume-law states, as well as ground states of one-dimensional gapped and critical systems. Our results identify the spectral organization of the entanglement spectrum as the key ingredient governing non-local magic and provide a framework for further systematic analytical investigation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07816v1
- Title: A Sparse and Truncated State Vector Simulator for Peaked Circuits
- Authors: Diogo R. Ferreira
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2607.07816v1  pdf=https://arxiv.org/pdf/2607.07816v1.pdf

Abstract:
In a class of quantum circuits known as peaked circuits, the goal is to predict the most probable bit string at the output of the circuit. Since these circuits are designed to have a sharp peak in their output distribution, in principle it should be possible to simulate them using a truncated state vector with a limited number of terms, or a fraction of the total probability mass. This approximate simulation can be carried out on a classical computer with a sparse representation that stores only the nonzero amplitudes of the state vector, in contrast to the dense representations that are common in most quantum simulators. For efficiency, all operations on the state vector should be vectorized to the furthest possible extent and, if available, hardware acceleration can also be used. This work describes how these requirements were met in an open-source implementation, and discusses its performance and limitations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07822v1
- Title: Routing Techniques for Error Corrected Silicon Spin Qubit Quantum Architectures
- Authors: Julian Shen, Ludwig Schmid, Robert Wille
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07822v1  pdf=https://arxiv.org/pdf/2607.07822v1.pdf

Abstract:
Silicon spin qubits have emerged as a promising qubit technology due to their favorable scaling and fabrication properties. However, efficiently compiling quantum circuits onto spin qubit platforms remains challenging, particularly when accounting for hardware constraints and the high sensitivity to static defects. Existing compilation approaches for spin qubits either largely ignore error correction, despite its critical role for large-scale quantum computation, or focus on low-level schedule constructions, missing a high-level compilation and routing for logical, error-corrected algorithms. To address this gap, we introduce a compilation framework for spin qubits based on the recent snakes on a plane model, which utilizes a 2D surface code and qubit teleportation to mitigate errors. Building on this model, we propose shortest-path and rotation-based algorithms as two novel classes of qubit-routing techniques, along with additional defect-handling and initial-mapping strategies. We evaluate both algorithms across diverse architectural settings and problem sizes, demonstrating that shortest-path methods excel in sparse, low-defect scenarios, while rotation-based approaches perform better in high-density environments. The implementation is publicly available on GitHub as open source.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07833v1
- Title: Improved GKP magic states from error-corrected non-Gaussian quantum states
- Authors: Sharon David, Jack Davis, Ulysse Chabaud, Francesco Arzani
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07833v1  pdf=https://arxiv.org/pdf/2607.07833v1.pdf

Abstract:
Gate teleportation, together with magic state distillation, is a promising route towards fault-tolerant, universal computation. In the context of bosonic quantum computation, Baragiola et al. PRL 123(20).200502 (2019) showed that within the framework of Gottesman--Kitaev--Preskill codes, encoded magic states suitable for distillation can be produced by error correcting Gaussian states, such as the vacuum. Here, we show that applying the same framework to simple non-Gaussian input states can significantly improve the quality of the magic states obtained, reducing the overall resources for the complete distillation procedure. We focus on superpositions of coherent states or Fock states, showing that many can lead to improvements in the generation of high-quality encoded magic states, which in some cases reduces the resources required for magic state distillation by about a factor $3$. We also investigate the primary source of these improvements and find that, unlike what was previously conjectured, the suitability of input states is not fully explained by symmetry arguments. Instead, the best states seem to avoid projection near stabilizer states as a result of the error correction procedure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07835v1
- Title: Super-Logarithmic Entanglement Scaling in a Monitored Superconducting Chain
- Authors: Rui-Jing Guo, Zhi-Yuan Wei
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2607.07835v1  pdf=https://arxiv.org/pdf/2607.07835v1.pdf

Abstract:
We develop a Keldysh-replica non-linear sigma model (NLSM) for the entanglement dynamics of a monitored one-dimensional spinful $s$-wave BCS chain in the rare-measurement regime, $γ\ll J,Δ$. Although the clean spinful $s$-wave BCS Hamiltonian belongs to symmetry class CI, spin-resolved measurements and projection to a conserved $f$-sector reduce the effective problem to class C. Starting from the corresponding parent symplectic saddle, we show that measurement backaction and the pairing amplitude impose complementary mass constraints that gap out different fluctuation channels. Their interplay dynamically projects the surviving massless modes onto an $\textrm{SO(R)}$ target manifold in replica space. A one-loop renormalization group analysis of this $\textrm{SO(R)}$ NLSM shows that, in the replica limit $R\to1$, the beta function becomes negative, producing a weak-anti-localization flow. This flow yields a super-logarithmic steady-state entanglement scaling $S(L)\sim \ln^2 L$ in the rare-measurement regime. Our field-theoretic result explains the numerical evidence reported in the companion Letter [arXiv:2604.04375] and shows that a topologically trivial monitored $s$-wave superconductor can realize an $\textrm{SO(R)}$ weak-anti-localizing critical phase without relying on a Wess-Zumino-Witten term.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07848v1
- Title: Quantum Sensors for Chemistry and Materials Science
- Authors: Piotr Put, Arjun Pillai, Xuan Hoang Le, Mikhail D. Lukin, Hongkun Park
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2607.07848v1  pdf=https://arxiv.org/pdf/2607.07848v1.pdf

Abstract:
The advancement of chemistry and materials science relies on transformative analytical tools which can overcome the sensitivity, spatial resolution, and throughput limitations of conventional techniques. This review explores the application of quantum sensors - specifically optically pumped magnetometers (OPMs) and nitrogen-vacancy (NV) centers in diamond - as robust platforms for molecular and materials analysis. We contrast the extreme magnetic sensitivity of macroscopic OPM ensembles with the atomic-scale resolution and multimodal capabilities of solid-state NV centers. We highlight their deployment in zero- to ultralow-field and nanoscale NMR spectroscopy, real-time reaction monitoring, and transient radical and pH detection. Furthermore, we discuss their integration into high-throughput chemical assays and non-destructive materials diagnostics, such as operando battery monitoring. With the ongoing commercialization of these technologies and advances in quantum-enhanced sensitivities, quantum sensors are poised to routinely address complex real-world analytical challenges.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07857v1
- Title: Multi-agent Autoformalization of Tensor Network Theory
- Authors: Sirui Lu, Erickson Tjoa, J. Ignacio Cirac
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2607.07857v1  pdf=https://arxiv.org/pdf/2607.07857v1.pdf

Abstract:
We build a team of specialized large language-model agents and present an agent-driven workflow for research-level formalization in theoretical physics, with the autoformalization of the fundamental theorem of matrix-product states as a demonstration. The agents, coordinated through a structured mathematical blueprint and periodic human review, orchestrated and executed the full formalization autonomously. For some statements, the agents were able to explore new proof routes that are not part of the standard literature. Along the way the agents produced extensive tensor-network and quantum-information libraries not previously available in Mathlib, Lean's mathematical library. As a physical application, the formalization also extends towards symmetry-protected topological phases in one dimension. We find that the main bottleneck in large-scale autoformalization is enforcing mathematical intent and we provide a detailed study of the full process and various subtleties involved. We release the codebase as the library \href{https://github.com/LionSR/TNLean}{TNLean}, together with a \nChapters{}-chapter \href{https://lionsr.github.io/TNLean/blueprint/}{blueprint} of the formalization effort.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07874v1
- Title: Unveiling Semiclassical Structures in Quantum Chaotic Eigenstates Using Neural Networks
- Authors: J. Montes, F. Borondo, Gabriel G. Carlo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07874v1  pdf=https://arxiv.org/pdf/2607.07874v1.pdf

Abstract:
Physics-informed neural networks and neural quantum states have consolidated a new paradigm to analyze and discover physical phenomena through constrained neural parametrizations. In this context, we investigate whether the semiclassical structure of the eigenfunctions of a quantum chaotic system can be unveiled through unsupervised learning. To this end, we train a "quantum dictionary", formulated as an overcomplete autoencoder, that sparsely represents the eigenstates of the system, using as an illustration the quantum baker map. The only explicit physical information imposed on the dictionary atoms is their localization in phase space, without providing any kind of information about the periodic orbits of the corresponding classical system. The model achieves high fidelity in reconstructing eigenstates not used during training. By comparing the learned atoms with an independently constructed "semiclassical dictionary", we find that they spontaneously localize on the periodic orbits and develop scar-like structures. This result is interesting in two ways: a localization constraint is sufficient to recover nontrivial semiclassical organization from spectral data and at the same time periodic orbits confirm their fundamental role in the structure of quantum chaotic eigenfunctions. More generally, our proposed architecture opens a new route to learning representations whose atoms optimize other chosen physical properties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07878v1
- Title: Complex spacing ratio statistics in the partially open asymmetric quantum baker map
- Authors: Leonardo Ermann, Pablo Sesin, Alejandro M. F. Rivas, Pablo D. Bergamasco, Gabriel G. Carlo
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; nlin.CD
- Links: abs=https://arxiv.org/abs/2607.07878v1  pdf=https://arxiv.org/pdf/2607.07878v1.pdf

Abstract:
We study the complex eigenvalue statistics of the asymmetric quantum baker map with partial projective openings. The classical asymmetric baker map, with its discontinuity at $q=2/3$, is fully chaotic, has no reflection symmetry, and provides a clean setting with tunable escape rate and fractal repeller dimension. We consider three distinct opening geometries in position space: localized (contiguous channels), random, and uniform (equispaced channels), all controlled by a tunable amplitude reflectivity parameter $ρ$ that interpolates between the fully open ($ρ=0$) and the closed ($ρ=1$) limits. We use the partially truncated circular unitary ensemble (PTCUE) as the random matrix theory benchmark. The main focus is on the joint distribution of the complex spacing ratio $z$, defined as the ratio of the distances from an eigenvalue to its nearest and next-nearest neighbors in the complex plane. We find a smooth crossover from a quasi-1D spectral regime, where eigenvalues cluster near the unit circle and the phase distribution of $z$ is peaked, to a two-dimensional Ginibre-like regime, where the distribution becomes nearly uniform and level repulsion is fully developed. Both the number of open channels $M$ and the reflectivity $ρ$ modulate this crossover, and $ρ$ provides an additional continuous control even at fixed opening size. All three opening models converge to PTCUE statistics at large $M$, while differences are most pronounced for the localized model at small $M$. No evidence of an abrupt transition is found. This crossover which suggests a universal behavior, has deep consequences for open quantum and wave-chaotic experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07890v1
- Title: Measurement-Based Quantum Computing on a Photonic Chip
- Authors: Jeldrik Huster, Louis L. Hohmann, Kevin Edelmann, Stefanie Barz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07890v1  pdf=https://arxiv.org/pdf/2607.07890v1.pdf

Abstract:
Integrated photonics provides a scalable platform for quantum information processing. In this context, measurement-based quantum computing (MBQC) offers an attractive approach in which quantum computation is realised by adaptive measurements on highly entangled graph states, circumventing the need for deterministic photon-photon interactions. Here, we demonstrate MBQC on an integrated silicon photonic chip capable of generating photonic graph states with up to four qubits. We achieve fidelities of $F_{Star} = (83.5 \pm 1.8)\,\%$ and $F_{Lin} = (75.6 \pm 1.1)\,\%$ for four-photon star and linear graph states, respectively. We use these resource states to implement MBQC-based single- and two-qubit gates and to demonstrate Grover's search algorithm and the Deutsch-Jozsa algorithm. These results establish the feasibility of reconfigurable four-photon MBQC on an integrated photonic platform and provide a foundation for future larger-scale implementations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07902v1
- Title: Environmental Memory Effects and Quantum Resource Hierarchies in Polarized Hyperon--Antihyperon Systems
- Authors: Omar Bachain, Mohamed Amazioug, Rachid Ahl Laamara
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07902v1  pdf=https://arxiv.org/pdf/2607.07902v1.pdf

Abstract:
Hyperon--antihyperon pairs produced in $e^{+}e^{-}\rightarrow J/ψ\rightarrow Y\bar{Y}$ ($Y=Λ,Σ^{+},Ξ^{-},Ξ^{0}$) constitute a unique high-energy platform for probing quantum correlations through experimentally accessible spin observables. We investigate the impact of correlated dephasing environments on the stationary and dynamical properties of logarithmic negativity, geometric quantum discord, and $l_{1}$-norm quantum coherence under both longitudinal and transverse beam polarizations. Our analysis reveals that environmental memory plays a crucial role in preserving quantum resources. In the non-Markovian regime, information backflow generates recurrent revivals of quantum correlations and significantly delays decoherence, whereas Markovian evolution drives the system toward asymptotic stationary states through an irreversible loss of quantum information. The influence of beam polarization is found to be strongly channel dependent and can substantially enhance the amount of accessible quantum correlations. A comparative investigation of different quantifiers uncovers a clear hierarchy of quantum resources. Quantum coherence remains robust over the widest parameter range, geometric quantum discord survives even in regions where entanglement is strongly reduced, while logarithmic negativity is the most sensitive to environmental degradation. This hierarchy persists for all considered hyperon channels and under both polarization configurations. The dependence of quantum resources on the production angle, azimuthal angle, polarization degree, and memory parameter is examined using experimental inputs from BESIII. The predicted effects are found to be compatible with the precision expected at BESIII and future high-luminosity facilities such as STCF and CEPC.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07927v1
- Title: Invariance Audits for Quantum Kernels and Variational Rewinding: A Real-to-Hermitian Taxonomy of Projector, Flag, Anchor, and Density Geometry
- Authors: Azadeh Alavi, Fatemeh Kouchmeshki, Hossein Akhoundi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07927v1  pdf=https://arxiv.org/pdf/2607.07927v1.pdf

Abstract:
Machine-learning models often replace vectors by normalized directions, projectors, covariances, subspaces, ordered flags, quantum states, or density operators before any classifier is fitted. This replacement is an invariance decision: it determines which distinctions are kept and which are quotiented out. We develop a self-contained real-to-Hermitian taxonomy for auditing such representations in quantum machine learning. On the real side, we formalize Grassmann and flag projector kernels, prove positive semidefiniteness and block-gauge invariance of a weighted flag kernel, and give a same-span block-swap witness showing when whole-span Grassmann geometry must fail while ordered flags succeed. On the quantum side, we prove that a noiseless fidelity kernel is exactly the Hilbert--Schmidt inner product between the associated rank-one Hermitian projectors, and that a QVR-style return probability is exactly an overlap score between the input projector and a learned anchor operator. Rank-constrained returns correspond to complex Grassmann anchors, while mixed or multimodal class models are naturally represented by density or positive-semidefinite anchors. Controlled vector, subspace, statevector, anomaly, finite-shot, and quotient-witness experiments support the same conclusion: quantum and geometric lifts are useful when their invariances match the task, and fail correctly when discarded information is label-bearing. The paper makes no hardware-speedup or quantum-advantage claim.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07942v1
- Title: A hardware-efficient variational ansatz with an exact diagonal metric for real- and imaginary-time evolution and Haar sampling
- Authors: Dario Picozzi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07942v1  pdf=https://arxiv.org/pdf/2607.07942v1.pdf

Abstract:
Variational quantum algorithms depend on the geometry of their parametrised circuits: metric-aware optimisation and time evolution require the Fubini-Study metric, which has hitherto demanded costly auxiliary measurements and ill-conditioned inversions. This work introduces a hardware-efficient $n$-qubit ansatz, which parametrises states by a binary tree and whose Fubini-Study pullback metric is diagonal in closed form. Quantum natural gradient on the tree parameters, variational imaginary- and real-time evolution, and exact unitary-invariant (Haar) sampling on a symmetry sector run with no auxiliary metric circuits or matrix inversion. When the target state is supported on a subspace of $k$ computational-basis states, the redundant tree parameters carry a gauge freedom a pruning compiler converts into circuits whose two-qubit count provably grows linearly in $k$; a variant reaches near-optimal $O(nk/\log n)$ scaling with the closed-form metric intact. On electronic-structure calculations for small molecules and half-filled Hubbard quench dynamics, the method reaches reference-level accuracy with one to three orders of magnitude fewer two-qubit gates than leading alternatives. Interchangeable constructions (a Schur-transform dressing or internal reparameterisations) make the ansatz exactly spin-adapted, with fixed total spin at every parameter and no penalty terms. The bare ansatz is an exactly controllable, well-conditioned and barren-plateau-free primitive for preparing and sampling sector states: on its own, it is classically simulable in $k$ (a boundary proved for a general class of sector-sparse ansätze); composed with a classically hard dressing, it yields molecular ground states, sector-Haar benchmarking, thermal correlators, and exact effective Hamiltonians trained from energy measurements alone, with the composed circuit carrying the potential for quantum advantage.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07970v1
- Title: Associating Trajectories with Quantum Processes by Equivalent Spectra
- Authors: Elliott Tammaro, Sriram Gundla, Arunabh Pratik, Shyla Rathore
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07970v1  pdf=https://arxiv.org/pdf/2607.07970v1.pdf

Abstract:
Quantum mechanics abandoned the classical notion of a particle trajectory, yet trajectories remain conceptually appealing for resolving foundational issues in quantum mechanics. Bohmian mechanics offers one route to associating trajectories with quantum processes, but it requires explicit non-locality to remain consistent with EPR-type experiments, placing it in tension with special relativity. We propose an alternative approach: rather than deriving trajectories from a quantum guidance equation, we search for classical trajectories whose radiated frequency spectra match those of quantum processes such as atomic transitions. Using the Liénard-Wiechert potentials, we compute the electric and magnetic fields generated by a point charge along a given trajectory, numerically solving the retarded-time and from these fields obtain the power spectrum of emitted radiation. By fitting the parameters of a chosen family of trajectories, we identify "equivalent spectrum" trajectories that reproduce a target frequency distribution, including ones of quantum mechanical origin. We discuss the implications of this method and propose future work to determine whether equivalent spectrum trajectories belong to a family governed by a differential equation, which would constitute a quantum-equivalent equation of motion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07978v1
- Title: A Quantum Reservoir Architecture for Chaotic Forecasting and a Test of Whether Its High Dimension Helps
- Authors: Tushar Pandey
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2607.07978v1  pdf=https://arxiv.org/pdf/2607.07978v1.pdf

Abstract:
Quantum reservoir computing uses a fixed quantum circuit as a feature generator and trains only a simple linear readout on top of it. This makes it cheap to train and free of the optimisation problems that affect many quantum machine-learning models. A natural worry is that the very large feature space the circuit produces might inflate apparent performance without adding anything real. This paper provides two things. First, it gives a complete, reproducible recipe for one such reservoir applied to forecasting chaotic systems, including how data is fed in, how the circuit is built, and how the readout is trained. Second, it gives a way to tell whether the reservoir's high dimension is actually doing useful work. We grow the size of the prediction problem and the size of the quantum reservoir together, so that extra capacity cannot be the explanation for any improvement, and we track a single stability number that measures how well behaved the readout fit is. On two chaotic test systems, a spatiotemporal chain and a shallow-water fluid model, the quantum reservoir keeps a flat, stable error as both sizes grow, while a matched classical reservoir does not. We report where the classical baseline is in fact stronger, so the comparison is honest. The result is a clean specification plus a diagnostic that other groups can apply to any reservoir whose features have a known scale.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07988v1
- Title: Procrustes Tomography -- reconstructing noisy quantum channels made easy
- Authors: Josey Stevens, Reece Robertson, Sebastian Deffner
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.07988v1  pdf=https://arxiv.org/pdf/2607.07988v1.pdf

Abstract:
What is the most expensive part of quantum device characterization? Clearly, the answer is quantum process tomography. However, especially for noisy intermediate-scale quantum (NISQ) computers, a comprehensive understanding of the noisy quantum dynamics is essential in interpreting the computational output. In this work, we introduce an efficient method -- Procrustes tomography -- that outperforms established methods in a number of aspects. After a pedagogical and constructive introduction, we demonstrate the utility of the method for representative examples of noisy quantum channels.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07999v1
- Title: Optimizing LZSM protocol for high-fidelity gates in open-system fluxonium
- Authors: Santiago Ferreyra, Valentın Reparaz, Maria Jose Sanchez, Leandro Tosi, Daniel Dominguez
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2607.07999v1  pdf=https://arxiv.org/pdf/2607.07999v1.pdf

Abstract:
Quantum gates based on resonant Rabi oscillations are inherently slow for small-frequency qubits. They are also prone to errors due to counter-rotating terms. However, when the anharmonicity is sufficiently high, as in the fluxonium architecture, alternative manipulation protocols can outperform standard resonant driving. In this work, we implement fast, high-fidelity quantum gates based on a one-period Landau-Zener-Stückelberg-Majorana (LZSM) driving protocol. We derive analytical expressions that simplify the exploration of the parameter space while accounting for the multi-level structure of the circuit. Furthermore, we analyze the role of leakage, discussing strategies to mitigate it and identifying regimes in which it becomes the dominant source of error. Finally, to evaluate the impact of dissipation on gate fidelity, we develop a robust formalism suitable for analyzing the open-system performance of quantum gates in the strong driving regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08037v1
- Title: Robust Quantum Learning through Hamiltonian Reservoir Computing
- Authors: Youya Xu, Chengyong Yu, Sanjib Ghosh
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; physics.app-ph
- Links: abs=https://arxiv.org/abs/2607.08037v1  pdf=https://arxiv.org/pdf/2607.08037v1.pdf

Abstract:
Quantum learning provides a versatile paradigm for information processing by exploiting the intrinsic representational capacity of high-dimensional Hilbert spaces. Here, we investigate a Hamiltonian-encoding framework for quantum reservoir computing that simultaneously addresses three key challenges in quantum learning: trainability, hardware efficiency, and information stability. In this framework, input data are directly mapped onto a fixed Hamiltonian and transformed into expressive nonlinear features through quantum dynamical evolution. By employing the reservoir-computing paradigm, the approach naturally circumvents the barren plateau problem in quantum learning landscapes. We validate the framework across two complementary platforms: an analog superconducting array processor and a digital gate-based quantum circuit implementation. Despite their fundamentally different realizations, both platforms exhibit comparable representational power and achieve competitive learning performance, establishing a unified framework for cross-platform quantum learning. While both implementations achieve comparable performance, the analog processor may offer a more hardware-efficient realization by bypassing the temporal overhead of gate-based decomposition and thereby making more effective use of finite coherence times, albeit at the expense of universality. Furthermore, we find that finite dissipation suppresses quantum-scrambling-induced instabilities at long evolution times and can enhance learning performance, revealing a constructive role for environmental coupling in stabilizing quantum learning dynamics. Collectively, these results establish Hamiltonian-encoded reservoir computing as a compact, expressive, and hardware-efficient paradigm for quantum learning on current-generation quantum platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08047v1
- Title: Nuclear Many-Body Systems as Benchmarks for Quantum Computing
- Authors: Sota Yoshida, Alessandro Baroni, Takayuki Miyagi, Ermal Rrapaj
- Categories: quant-ph (primary); quant-ph; nucl-th
- Links: abs=https://arxiv.org/abs/2607.08047v1  pdf=https://arxiv.org/pdf/2607.08047v1.pdf

Abstract:
We present a framework for benchmarking quantum algorithms for nuclear many-body systems based on realistic nuclear Hamiltonians such as chiral effective field theory. To this effect we introduce a workflow that maps nuclear interactions in second quantization formalism to qubit Hamiltonians. This enables the systematic construction of benchmark instances spanning no-core and valence-space formulations with two-body (NN) and selected three-body (3N) interactions. Then, we proceed to provide resource estimates for three representative eigenvalue algorithms: Quantum Phase Estimation, Quantum Krylov methods, and Observable Dynamic Mode Decomposition. We compare their resource requirements in terms of T-gate counts and system size, and examine the impact of model-space choices and many-body interactions. The primitives included in our analysis are Trotterization, Qubitization, and Quantum Singular Value Transformation. Our results quantify scaling trends across algorithms and problem classes, and provide a basis for consistent comparisons of quantum approaches to nuclear many-body problems. The implementation is provided by the NuQuLib software stack.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08070v1
- Title: (2,m)-threshold quantum data hiding
- Authors: Donghoon Ha, Jeong San Kim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08070v1  pdf=https://arxiv.org/pdf/2607.08070v1.pdf

Abstract:
We consider multiparty quantum state discrimination and present a multiparty quantum data-hiding scheme for one classical bit to be shared among multiple parties. In the proposed scheme, any pair of parties can collaborate to perfectly recover the hidden bit through a joint measurement, whereas measurements based on local operations and classical communication(LOCC) performed even by all parties reveal only an arbitrarily small amount of information. We further provide bounds on the optimal LOCC discrimination of multiparty quantum states. The proposed scheme can be implemented using only separable states of low-dimensional quantum systems, enhancing its practical feasibility.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08078v1
- Title: Experimental demonstration of entanglement sudden death induced by natural dissipation
- Authors: Yan Wang, Hao-Long Zhang, Jia-Hao Lü, Ken Chen, Wen Ning, Li-Hua Lin, Zhen-Biao Yang, Shi-Biao Zheng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08078v1  pdf=https://arxiv.org/pdf/2607.08078v1.pdf

Abstract:
Any quantum system inevitably interacts with its natural environment, which can be modeled as a Markovian reservoir consisting of a continuum of electromagnetic field modes. The quantum coherence of qubits in a zero-temperature natural reservoir decays asymptotically, whereas the quantum entanglement of two qubits coupled to such reservoirs may disappear in a finite time. This phenomenon, referred to as entanglement sudden death (ESD), has been simulated with artificially engineered dissipative channels, but ESD induced by natural dissipative channels has not been confirmed. We here present the first demonstration of natural-dissipation-induced ESD for two photonic qubits, each stored in a leaky resonator of a superconducting circuit. The disentanglement dynamics of the two photonic qubits is monitored with two ancilla superconducting qubits, which can be controllably coupled to the corresponding leaky resonators. The techniques developed in our experiment pave the way for experimental exploration of entanglement dynamics in natural environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08092v1
- Title: Equivariant Quantum Clustering with Differential Privacy: Parameter-Efficient Privacy-Preserving Analysis Across Heterogeneous Sensitive Datasets
- Authors: B. M. Taslimul Haq, Md Arifur Rahman, Tawfiq Al Islam Foysal, Abdullah Al Noman, Abir Ahmed
- Categories: quant-ph (primary); quant-ph; cs.CV
- Links: abs=https://arxiv.org/abs/2607.08092v1  pdf=https://arxiv.org/pdf/2607.08092v1.pdf

Abstract:
Privacy-preserving clustering is critical for analyzing sensitive data in healthcare, cybersecurity, and enterprise applications, where maintaining data confidentiality must be balanced with analytical performance. This paper presents Equivariant Quantum Clustering (EQC), a parameter-efficient framework that integrates symmetry-aware quantum circuits with differential privacy to improve the privacy-utility tradeoff. EQC employs p4m equivariant parameter sharing to reduce circuit complexity while preserving informative feature representations. The framework is evaluated on three privacy-sensitive datasets: NSL-KDD, CERT Insider Threat v6.2, and a synthetic MIMIC-III clinical dataset. On the NSL-KDD benchmark, EQC achieves 79.3% clustering accuracy while reducing membership inference attack success to 38.3% under a privacy budget of ε = 1.0 and δ = 10^-5, outperforming representative classical and quantum baselines. Ablation studies indicate that the performance gains primarily arise from parameter-efficient circuit design combined with differential privacy. The results demonstrate that EQC provides a practical quantum-ready framework for secure and privacy-preserving clustering across heterogeneous sensitive datasets.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08096v1
- Title: Center-of-Mass Bounds and Harmonic Extremality
- Authors: Arseny Pantsialei
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08096v1  pdf=https://arxiv.org/pdf/2607.08096v1.pdf

Abstract:
We study the center-of-mass observable in one-dimensional many-body systems with translation-invariant interactions and extend the harmonic-rigidity mechanism from the one-body setting to an interacting many-body problem. We prove a sharp upper bound on the ground-state center-of-mass fluctuation in terms of the active spectral gap associated with the center-of-mass probe, and show that this bound does not require any positivity assumption on the ground state. In the positivity class, we characterize the equality case completely. Exact saturation occurs if and only if the external one-body traps are harmonic with a common frequency, while the interaction may remain arbitrary within the translation-invariant class. We also identify a natural rigidity defect measuring deviation from the harmonic extremal situation and prove quantitative near-saturation estimates controlling both the variance deficit and the spectral weight outside the first active shell. In this way, the paper establishes harmonic confinement as the unique static extremizer for the rigid interacting center-of-mass mode at fixed active gap.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08102v1
- Title: Decomposition-Based QAOA for Maximum Coverage Location Problem in Satellite Constellation Design
- Authors: Divya Sisodiya, Amiratabak Bahengam, Hang Woon Lee, Hao Chen
- Categories: quant-ph (primary); quant-ph; eess.SY
- Links: abs=https://arxiv.org/abs/2607.08102v1  pdf=https://arxiv.org/pdf/2607.08102v1.pdf

Abstract:
An increase in earth observation missions has increased the demand of efficient design and optimization of satellite constellations. Maximizing coverage of the target while effectively utilizing the limited orbital resources is one of the critical design challenges for complex combinatorial optimization problems. The maximal covering location problem (MCLP), serves as a base for orbital coverage modeling, is NP-hard and computationally intractable for large-constellation instances. Using heuristics, metaheuristics, and mixed-integer linear programming, classical solvers have achieved optimal or near-optimal results, yet their scalability is limited as the problem size increases. Quantum computing advancements, including the quantum approximate optimization algorithms, offer a potential solution to NP-hard combinatorial optimization problems. Current quantum hardware limitations, such as low qubit counts and circuit depth, restrict solutions for small-scale instance problems. To address this challenge, this paper proposes a scalable quantum optimization framework for MCLP in satellite constellation design. A decomposition-based quantum methodology is proposed, in which large MCLP instances are partitioned into subgraphs by classical decomposition, optimized independently via quantum optimization circuits, and combined using quantum reconstruction strategies. Computational results across different constellation sizes reveal better scalability in less time while maintaining competitive coverage performance compared to classical solvers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08133v1
- Title: Communication Advantages from Quantum Dense Network Coding
- Authors: Ian George, Brian Doolittle
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2607.08133v1  pdf=https://arxiv.org/pdf/2607.08133v1.pdf

Abstract:
A central problem in quantum information theory is understanding how quantum resources can be used to communicate information more efficiently than classical resources. We introduce quantum dense network coding -- a protocol that transmits the output of a non-Boolean function to a receiver using provably half as many qubits as bits for each sender by not transmitting the entirety of the function inputs. We show this advantage requires both shared entanglement and quantum communication, is robust to noise, and the gap in success probability between quantum and classical communication can be amplified exponentially in the number of senders. Finally, we show that dense network coding gives rise to a novel, information-theoretically secure, quantum cryptographic protocol, which we call measurement-device-independent quantum key growing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08138v1
- Title: Adaptive Qubit Freezing Enables Robust Graph Partitioning for Divide-and-Conquer QAOA
- Authors: Sokea Sang, Leanghok Hour, Dongmin Kim, Youngsun Han
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08138v1  pdf=https://arxiv.org/pdf/2607.08138v1.pdf

Abstract:
Divide-and-conquer variants of the Quantum Approximate Optimization Algorithm (QAOA) provide a promising route for executing combinatorial optimization problems beyond the qubit capacity of near-term quantum devices. However, existing approaches rely on the existence of small vertex separators and fail entirely on dense or highly connected graphs where such decompositions do not exist. We introduce Frozen Large Graph Partitioning (FrozenLGP), an adaptive decomposition framework that transforms partitionability from an assumption into an enforceable property. When standard partitioning fails, FrozenLGP identifies the minimum set of obstructing vertices through a minimum-vertex-cut computation based on max-flow and classically freezes their spin assignments. The energetic contributions of the removed interactions are rigorously preserved by folding them into linear bias terms in the Ising Hamiltonian of neighboring active qubits. Across graph sizes up to 10,000 vertices and multiple topology families, FrozenLGP achieves 100\% decomposition coverage, compared with 4.6\% for the standard divide-and-conquer baseline on high-connectivity instances. End-to-end MaxCut experiments demonstrate that FrozenLGP preserves approximation quality on instances already solvable by conventional divide-and-conquer QAOA while extending applicability to previously unsupported graphs, and outperforming alternative full-coverage decomposition strategies. Noise simulations further show improved robustness arising from reduced entangling-gate requirements. These results establish FrozenLGP as a topology-robust front end for distributed QAOA on near-term quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08158v1
- Title: Continuous-Variable MIMO THz Quantum Secret Sharing: Gaussian-modulation and Passive-modulation
- Authors: Leixin Wu, Jiayu Pan, Fangzhe Chen, Lingtao Zhang, Bowen Zheng, Tie Qiu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08158v1  pdf=https://arxiv.org/pdf/2607.08158v1.pdf

Abstract:
Although quantum key distribution (QKD) enables information-theoretically secure key distribution, it is mainly designed for point-to-point communication and cannot directly support multi-user collaborative scenarios. To address this limitation, quantum secret sharing (QSS) has been proposed to enable secure multiparty key sharing. However, most existing QSS protocols rely on a single-input single-output (SISO) channel, which limits the achievable secret key rate (SKR) and transmission distance. This paper proposes a continuous-variable (CV) QSS protocol based on a multiple-input multiple-output (MIMO) architecture operating in the terahertz (THz) band. In the proposed scheme, transmit-receive beamforming decomposes the MIMO channel into multiple parallel SISO subchannels, thereby improving both the SKR and transmission distance. We describe the QSS transmission procedure and derive the SKR expressions for eight protocol variants under Gaussian collective attacks. Specifically, Gaussian modulation and passive modulation are considered at the transmitter, while homodyne and heterodyne detection are considered at the receiver. Both asymptotic and composable finite-size SKR formulas are derived to characterize the ideal upper-bound performance and the achievable performance under finite resources, respectively. Simulation results show that, under ideal assumptions including perfect channel state information, perfect phase synchronization, and ideal beamforming, the Gaussian-modulation protocol with a 32 x 32 antenna configuration and the passive-modulation protocol with a 1024 x 1024 antenna configuration achieve transmission distances of 14.99 m and 160 m in the atmospheric channel, respectively. These results provide an idealized theoretical benchmark for evaluating the potential performance gains of MIMO-assisted THz CV-QSS in indoor and short-range outdoor wireless networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08166v1
- Title: Efficient Pauli-decomposition and multistage state-refinement for tensor network based differential equation solver
- Authors: Vishwabhushan Suresh Gholap, Himadri Shekhar Dhar, Siddhartha Santra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08166v1  pdf=https://arxiv.org/pdf/2607.08166v1.pdf

Abstract:
Classical numerical techniques for solving partial differential equations (PDEs) become computationally expensive as the dimension of the discretized differential operator increases. For PDEs giving rise to Sturm--Liouville problems, tensor network (TN) methods can be highly productive: an operator of dimension $N\times N$ can be represented as a matrix product operator (MPO) using only $n=\log_2(N)$ qubits, enabling computation of eigenvalues and eigenvectors via imaginary time evolution (ITE). However, this remains computationally challenging. First, most methods for generating MPOs of large operators without explicit tensor-product structure require prohibitively large memory. Second, the number of Trotterization steps for convergence in conventional ITE increases rapidly with $n$. We present techniques to mitigate both challenges for certain sparse, structured differential operators. To address the first, we construct the MPO by expanding the operator in the Pauli-string basis, enabled by an analytical expression for the Pauli basis coefficients that reduces the memory requirement from $\mathcal{O}(2^{n+1})$ to $\mathcal{O}(2n)$. To address the second, we propose a multistage state-refinement heuristic that accelerates ITE convergence, reducing convergence time by up to two orders of magnitude. Using this TN framework, we compute the first 32 eigenstates of a Laplacian of dimension exceeding $10^6$ with fidelity above $0.95$ using a 20-qubit MPO. We further validate the method on the 2D anharmonic oscillator and investigate disordered systems, where increasing random potential strength degrades accuracy and limits the approach.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08200v1
- Title: Efficient High-Dimensional Quantum Circuit Synthesis: From Multi-Controlled Gates to Isometries and Quantum Channels
- Authors: Gui-Long Jiang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08200v1  pdf=https://arxiv.org/pdf/2607.08200v1.pdf

Abstract:
Circuit synthesis of multi-controlled gates is crucial for qudit ($d$-level) quantum computing. This paper presents efficient synthesis schemes that reduce the elementary gate count for multi-controlled single-qudit gates. For synthesizing general $(n-1)$-controlled unitaries on $n$ qudits, we reduce the controlled-increment (CINC) and generalized controlled-$X$ (GCX) gate counts to $O(n^2)$, improving upon existing $O(n^{2+\log_2 d})$ CINC and $O(n^3)$ GCX bounds. For $(n-1)$-controlled special unitaries, this complexity is further reduced to $O(n)$. By utilizing the proposed circuit, we present qudit-based circuit constructions for isometries and quantum channels from $n$ to $m$ qudits. When specialized to general $n$-qudit unitaries, our construction requires fewer CINC gates than previous results. Moreover, for the first time, we present a circuit synthesis scheme for single-controlled gates using SUM gates and single-qudit gates when $d$ is prime. This enables all CINC-based circuits for various quantum operations to be converted into SUM-gate circuits while preserving the same asymptotic complexity. Finally, we establish a theoretical lower bound on the number of SUM and CINC gates required to synthesize general $n$-qudit unitaries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08212v1
- Title: Möbius-Guided Diagonal-Gate Compilation with Native Multiqubit Controlled-Phase Gates on Neutral-Atom Processors
- Authors: Hairuo Huang, Yanwu Gu, Chen Huang, Xi Zhao, Meng-Jun Hu, Dong E. Liu, Jingbo Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08212v1  pdf=https://arxiv.org/pdf/2607.08212v1.pdf

Abstract:
Diagonal gates are ubiquitous primitives in quantum algorithms, from phase oracles, hypergraph-state preparation, and multi-control logic to Hamiltonian simulation of spin models and digitized lattice field theories, where Ising interactions and local potential terms are diagonal in the encoded basis. Standard compilers, however, often lower diagonal structure into one- and two-qubit gates before neutral-atom hardware can exploit native Rydberg-mediated multiqubit controlled-phase operations. We propose a Möbius-guided compiler that maps a diagonal phase function to a phase hypergraph via subset-lattice Möbius inversion. The hypergraph retains the support and angle of each many-body phase term, allowing sparse or local high-order structure to be routed as native multiqubit controlled-phase candidates when feasible and decomposed otherwise. The neutral-atom scheduler accounts for atom motion, interaction-zone constraints, blockade feasibility, and error costs, enabling a direct comparison between native high-order execution and decomposed alternatives. Benchmarks against routed ZAP and ZX-calculus baselines show improved estimated success for algorithmic instances with exploitable three- and four-body phase terms, and comparable performance on predominantly two-body instances. These results provide a feasible compilation strategy for more fully exploiting the native capabilities of neutral-atom hardware, using atom reconfigurability and Rydberg-mediated multiqubit phase operations as practical resources for more efficient quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08220v1
- Title: Quantum linear solvers for quantum chemistry: prospects of exponential quantum advantage
- Authors: Peniel Bertrand Tsemo, Kenji Sugisaki, Ishita Bhattacharjee, V. S. Prasannaa
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2607.08220v1  pdf=https://arxiv.org/pdf/2607.08220v1.pdf

Abstract:
Quantum linear solvers (QLSs) can offer the potential for exponential quantum advantage in solving quantum chemical problems, but its assessment hinges on determining the condition number ($κ$) scaling, which itself is computationally challenging. While a recent work applied the Harrow-Hassidim-Lloyd (HHL) algorithm to single-reference linearized coupled cluster equations (SRLCC), the validity of the HHL-SRLCC framework is restricted to weakly correlated regimes. A general treatment requires a formulation that can access strongly correlated regions. We thus begin by extending the QLS-SRLCC framework to its multi-reference form, which is based on the internally contracted multi-reference LCC method (QLS-icMRLCC). We then analyze $κ$ scaling using three complementary diagnostics that range from explicit computations to use of indirect structural indicators: (i) direct calculations of $κ$, (ii) scaling of the ratio of maximum to minimum diagonal entries of an A matrix, and (iii) structural analyses of the A matrices based on a recently proposed conjecture, which we adapt to the QLS-LCC problem. The three approaches yield consistent predictions, indicating a polylogarithmic $κ$ scaling in system size. This finding, when combined with our arguments on sub-linear scaling of sparsity, supports the prospects of exponential advantage using QLSs for the LCC problem. Finally, numerical calculations on potential energy curves of model systems containing up to four atoms recover the ground state energies with errors relative to benchmark classical methods not exceeding 0.009$\%$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08275v1
- Title: Engineering Nonclassical States via the Dynamical Casimir Effect
- Authors: Maristella Crotti, Luca Razzoli, Giacomo Guarnieri, Luigi Giannelli, Giuseppe A. Falci, Giuliano Benenti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08275v1  pdf=https://arxiv.org/pdf/2607.08275v1.pdf

Abstract:
Nonadiabatic driving in ultrastrongly coupled light--matter systems is commonly regarded as a source of errors, as counter-rotating interactions convert vacuum fluctuations into real excitations through the dynamical Casimir effect (DCE). Here we show that, instead, the DCE can be harnessed as a resource for engineering nonclassical states of light. Considering a cavity mode ultrastrongly coupled to a frequency-tunable qubit, we employ optimal quantum control to design driving protocols that convert vacuum fluctuations into targeted states. Numerical optimization reveals a versatile and robust approach for the deterministic preparation of a broad class of nonclassical states, illustrated here through Fock states, squeezed states, and Schrödinger-cat-state superpositions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08348v1
- Title: Works on My QPU: Reproducibility in Quantum Computing Research
- Authors: Dominik Köster, Maja Franz, Benjamin Zec, Nicole Hoess, Ralf Ramsauer, Wolfgang Mauerer
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08348v1  pdf=https://arxiv.org/pdf/2607.08348v1.pdf

Abstract:
Quantum computing research increasingly depends on complex software stacks, yet the reproducibility of published results does not receive the priority and longevity mandated by recommendations of large international scientific bodies and best practices in software-centric systems research. In this paper, we present a combined manual and automated large-scale analysis of the reproducibility landscape in quantum computing research, quantify shortcomings, and derive actionable steps forward.   We manually evaluate a curated sample of 127 papers using a five-question framework that covers code availability, environment specification, documentation, hardware description, and executability. To place these findings in a broader context, we conduct an automated large-scale screening of nearly 5000 quantum computing papers for the same reproducibility indicators. Our manual analysis reveals that only 24.4% of the sampled papers provide code artefacts, and among those, 64.5% fail to execute successfully in a clean environment. This assessment is corroborated by a large-scale automated analysis that yields a consistent code availability rate of 26.8%. Further, it shows that approximately one-third of the papers with accessible code lack machine-readable environment specifications.   The results in this paper indicate that reproducibility is not yet consistently achieved in quantum computing research. In response, we outline a set of practical recommendations that address the observed failure modes and illustrate how reproducibility can be improved in practice.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08350v1
- Title: Grokking and epoch-wise double descent in quantum neural networks
- Authors: Daniel Pranjić, Marco Roth, Christian Tutschku
- Categories: quant-ph (primary); quant-ph; physics.data-an
- Links: abs=https://arxiv.org/abs/2607.08350v1  pdf=https://arxiv.org/pdf/2607.08350v1.pdf

Abstract:
Grokking, the delayed transition from memorization to generalization, is a fundamental phenomenon in gradient-based learning, yet its dynamics within variational quantum machine learning (QML) remain largely unexamined. In this work, we report the empirical observation of both the grokking transition and epoch-wise double descent in a two-qubit quantum neural network (QNN) under a complete parameterization of the SU(4) manifold. We demonstrate that overparameterization via increased circuit depth improves the probability of successful generalization. Notably, these architectures frequently exhibit an epoch-wise double descent in test error, degrading at a critical epoch before recovering into a generalizing state. Crucially, we identify a generalization decay in late-stage training, where the test error increases significantly despite a stagnant training loss. Bridging this behavior with algorithmic stability theory, our analysis reveals that this decay correlates with an unconstrained increase of the weight-norm, drifting away from sparse, phase-aligned harmonic solutions toward overfitted solutions in the Hilbert space. We analyze the underlying temporal dynamics of this transition, demonstrating how the onset of generalization is linked to optimization hyperparameters such as learning rate and weight decay. Finally, to mitigate late-stage decay, we introduce a weak explicit weight-norm regularization into the loss function. We demonstrate that this structural anchor stabilizes the post-grokking phase and permanently preserves generalization gains, providing a robust framework for training overparameterized quantum circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08363v1
- Title: Stroboscopic Stabilization of Cat Qubits
- Authors: Timo Hillmann, Franco Nori, Fernando Quijandría
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08363v1  pdf=https://arxiv.org/pdf/2607.08363v1.pdf

Abstract:
Dissipatively stabilized cat qubits provide a promising route toward fault-tolerant quantum computation, exhibiting exponential suppression of bit-flip errors with increasing phase-space separation of the logical states, while incurring only a linear increase in phase-flip errors. Existing implementations rely on engineered two-photon dissipation via nonlinear coupling to a lossy environment, an approach largely confined to superconducting platforms and limited by spurious decay channels and finite dissipation rates. Here, we propose a fundamentally different stabilization paradigm based on repeated interactions with an auxiliary two-level system mediated by a quadratic Hamiltonian, enabling dissipative stabilization without reservoir engineering. Our approach overcomes key limitations of existing schemes and is compatible with a wider class of experimental platforms. Furthermore, it preserves the noise bias and extends to squeezed cat qubits, rendering single-photon loss errors partially correctable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08386v1
- Title: Parallel QEC Decoding Applied to Distributed Quantum Computing
- Authors: Gabriele Incardona, Davide Ferrari, Michele Amoretti
- Categories: quant-ph (primary); quant-ph; cs.DC; cs.PF
- Links: abs=https://arxiv.org/abs/2607.08386v1  pdf=https://arxiv.org/pdf/2607.08386v1.pdf

Abstract:
A novel parallel approach is proposed for QEC decoding based on Belief Propagation with Ordered Statistics Decoding. The main idea is to pre-process the error vectors obtained from Belief Propagation by applying Singular Value Decomposition locally to sub-regions of the lattice. The proposed approach is applied to distributed quantum computers and evaluated in terms of complexity, accuracy, and scalability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08396v1
- Title: Efficiently simulable quantum circuits with large entanglement, magic, and non-Gaussianity via code-compiled tensor networks
- Authors: Aydin Deger, Stergios Koutsioumpas, Mark Webster, Hasan Sayginel, Joschka Roffe, Dan E. Browne
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08396v1  pdf=https://arxiv.org/pdf/2607.08396v1.pdf

Abstract:
We introduce a family of quantum circuits that possess standard indicators of classical simulation hardness including high entanglement entropy, magic, and non-Gaussianity, yet admit efficient classical simulation via matrix product states (MPS). Our construction uses logical circuits of high-rate Calderbank-Shor-Steane (CSS) codes with enhanced symmetries. Using code automorphisms and transversal diagonal gates from higher levels of the Clifford hierarchy, we realize nonlocal logical Clifford and non-Clifford gates, showing how error-correcting codes can compile complex logical circuits into simple physical operations. Simulation efficiency rests on two properties: (i) diagonal transversal gates do not increase bond dimension, and (ii) permutations are tracked classically via on-the-fly relabeling, avoiding costly SWAP networks. Unlike Clifford or matchgate simulation, our method accepts a broad class of initial states, including dense entangled, magic, and non-Gaussian inputs, provided the encoded state retains an efficient MPS representation. We also release an exact phase-polynomial backend for monomial subfamilies, whose cost is set by higher-degree phase terms rather than entanglement growth. We demonstrate the method on an infinite polar CSS code family, showing bond dimension stays bounded by the encoding cost regardless of circuit depth. These results show that for some circuit families, standard resource measures are individually insufficient to indicate simulation hardness. As a near-term application, we use the compiled MPS as a classical reference for direct fidelity estimation of a quantum device running nontrivial logical circuits. Pauli sampling on the encoded reference, with a Clifford pushback through the known encoder, provides the ideal expectation values, so the logical output fidelity can be estimated from local Pauli readout alone, without costly state tomography.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08411v1
- Title: The Geometry of Quantum Complexity in Open Systems
- Authors: Ezra Acalapati, Kausik Ghosh, Giuseppe Policastro
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2607.08411v1  pdf=https://arxiv.org/pdf/2607.08411v1.pdf

Abstract:
We extend Nielsen's geometric approach for quantum complexity from closed to open quantum systems, whose dynamics is governed by Lindbladian evolution. In this framework, complexity is defined through an optimal-control problem on the space of mixed states, with a cost assigned to both unitary and non-unitary generators. We show that the resulting geometric structure differs fundamentally from the Riemannian geometry that emerges in the case of unitary evolution. In the open-system setting, the natural geometry is typically sub-Finslerian. Dissipation makes the geodesics non-reversible, while the admissible tangent directions are restricted by the physically allowed controls. We analyze several physically motivated examples, including a single qubit subject to depolarizing and amplitude-damping channels, as well as the damped harmonic oscillator. We show that, similarly to the unitary case, varying the penalty factors in the cost functional modifies the geometric properties through changes in the flag curvature, the Finslerian analog of sectional curvature. Our results provide a geometric framework for quantifying the abstract notion of complexity in dissipative quantum systems, with potential connections to experimentally realizable setups.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08425v1
- Title: Quantum and Classical Potts Criticality in Driven-Dissipative Bosonic Lattices
- Authors: Jacopo Tosca, Zejian Li, Cristiano Ciuti
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2607.08425v1  pdf=https://arxiv.org/pdf/2607.08425v1.pdf

Abstract:
The emergence of equilibrium universality from intrinsically nonequilibrium dynamics is a fundamental open problem. Bose-Hubbard lattices realized in photonic and circuit-QED platforms provide a versatile setting to engineer nonlinear interactions, dissipation, and multiphoton processes. Here we investigate a Bose-Hubbard lattice subject to three-photon parametric driving, whose nonequilibrium steady state spontaneously breaks a $\mathbb Z_3$ symmetry and realizes the criticality of the three-state Potts model, a three-state generalization of the Ising model. Using a variational phase-space approach with systematically controllable accuracy based on a Variational Multi-Gaussian ansatz, we perform finite-size scaling analyses in one and two spatial dimensions. We find that, in two-dimensional lattices with single-photon losses, the nonequilibrium steady-state transition belongs to the universality class of the 2D classical three-state Potts model. In contrast, in one-dimensional lattices with three-photon losses, the transition is governed by the one-dimensional quantum three-state Potts universality class. These results establish driven-dissipative bosonic lattices as a platform for emergent Potts criticality and identify multiphoton dissipation as a mechanism that promotes nonequilibrium critical behavior from classical to quantum universality classes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08431v1
- Title: Global Precision Limits in Critical Quantum Metrology: From Cramér-Rao to Ziv-Zakai
- Authors: Neng Zeng, Tao Liu, Yu-Ran Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08431v1  pdf=https://arxiv.org/pdf/2607.08431v1.pdf

Abstract:
Critical quantum metrology with equilibrium states predicts quantum-enhanced sensitivity only in the vicinity of criticality, where large prior information about the parameter is required. By employing quantum Ziv-Zakai bounds, we derive a limit on the mean-square error in critical quantum metrology. For second-order quantum phase transitions, we show that the precision predicted by the Cramér-Rao bound offers no substantial improvement over the prior standard deviation. Thus, the critical quantum sensor's precision can only achieve a constant gain compared to the prior standard deviation, even without performing any measurement. We elucidate the fundamental limitation on the achievable precision in critical quantum metrology in the context of local sensing, even without considering state-preparation costs or noise. Thus, the super-Heisenberg-limited sensitivity at criticality arises from precise prior knowledge rather than a genuine gain due to criticality. Our work provides a practical framework for assessing critical quantum metrology and a routine for studying quantum sensing with many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08447v1
- Title: Simulation of exchange coupling effects in double quantum dot FinFET-like structures
- Authors: Ilan Bouquet, Alexander Maeder, Mathieu Luisier
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08447v1  pdf=https://arxiv.org/pdf/2607.08447v1.pdf

Abstract:
By leveraging a GPU-accelerated Schrödinger-Poisson (SP) solver, we characterize exchange coupling in a hole spin double-qubit device involving a double quantum dot (DQD) system formed inside a 5-gate silicon fin field-effect transistor (FinFET) similar to real experimental structures. The self-consistent SP simulations rely on a finite difference discretization of the 3D volume and on a Luttinger-Kohn 6x6 kp Hamiltonian accounting for magnetic fields and strain distribution. They return the gate-induced confined electronic states and the corresponding electrostatic potential hosting the DQD. These quantities serve as inputs to a two-particle Hamiltonian that is constructed from single-particle Slater determinants through the configuration interaction (CI) method. By diagonalizing this two-particle Hamiltonian, the eigenstates and eigenenergies of the DQD system are obtained, together with their exchange coupling. We show that our simulation framework, using a reduced number of basis states, is capable of reproducing the magneto-electrostatic behavior of the devices of interest, as predicted from theory and observed experimentally. We finally leverage our approach to determine the optimal operating conditions of a two-qubit quantum logic gate implemented in a Si FinFET structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08450v1
- Title: Exactly solved Schrödinger equations with time-dependent Hamiltonians
- Authors: Michael Warnock, Antônio Francisco Neto, Pierre-Louis Giscard, Omid Faizy, Christian Joachim
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2607.08450v1  pdf=https://arxiv.org/pdf/2607.08450v1.pdf

Abstract:
We present the analytical, exact, explicit, and assumption free formulas for the evolution operators corresponding to four instances of time-dependent Hamiltonians relevant to quantum spin batteries including two stochastic cases. We demonstrate how to recover and go beyond existing expansions and approximations directly from the exact solutions giving, for example, an explicit exact formula for Floquet Hamiltonians at all orders. The exact solutions are obtained through a completely novel combination of three mathematical techniques, the $\star$-algebra, path-sums and Omega calculus, which we briefly overview. These are widely applicable to other non-autonomous differential systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08462v1
- Title: Optimizing and Certifying Multipartite Permutationally Invariant Bell Inequalities
- Authors: Jin-Fu Chen, Mengyao Hu, Jordi Tura
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08462v1  pdf=https://arxiv.org/pdf/2607.08462v1.pdf

Abstract:
Multipartite Bell nonlocality provides a device-independent probe of many-body quantum correlations, but its characterization is limited by the rapid growth of the underlying classical and quantum optimization problems. We develop a scalable method for constructing and certifying permutationally invariant Bell inequalities using only one- and two-body correlators. The construction gives families of inequalities with robust quantum violations for general $m$ measurements as the number of parties $N$ becomes large. To improve robustness against noise, we optimize the ratio of the quantum value to the classical bound for these families in the large-$N$ limit. We then certify the resulting quantum violation using semidefinite programming. For the broad class of Bell inequalities studied here, the infinite-$N$ ratios take simple rational values for finite $m$ and converge to $\coth(1)$ as $m\to\infty$. The optimized inequalities efficiently detect many-body Bell nonlocality with collective measurements, with more measurement settings leading to stronger violations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08469v1
- Title: Non-Hermitian topology driven by an identity term: An exactly solvable paradigm
- Authors: Lingfang Li, Yating Wei, Yang Ruan, Gangzhou Wu, Jun Wang, Shihua Chen, Tong Lin, Ching Hua Lee, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.other
- Links: abs=https://arxiv.org/abs/2607.08469v1  pdf=https://arxiv.org/pdf/2607.08469v1.pdf

Abstract:
An identity term in the Hamiltonian is conventionally regarded as spectrally inert-it shifts energies but does not alter eigenstate topology. We show that under non-Hermitian skin pumping, this paradigm fails: a momentum-dependent identity term actively deforms the generalized Brillouin zone, thereby challenging established topological criteria that rely on fixed complex contours. Here, by introducing spin-orbit coupling into a Hatano-Nelson chain, we present an exact analytical solution for the entire non-Hermitian eigensystem under open boundary conditions. Our solution reveals how inter-cell spin-orbit coupling, synergizing with this non-trivial identity term, induces topological edge states and robust zero modes in the complete absence of chiral symmetry. This work establishes an exactly solvable paradigm for non-Hermitian topology beyond symmetry protection, and provides a rigorous benchmark for testing topological invariants in systems with momentum-dependent identity terms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08508v1
- Title: Magic Gate Teleportation: Structure, Useful Resource States, and Simpler Feedforward
- Authors: Yunzhe Zheng, Allen Zang, Aleksander Kubica
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08508v1  pdf=https://arxiv.org/pdf/2607.08508v1.pdf

Abstract:
Quantum gate teleportation is a key technique in fault-tolerant quantum computation that uses resource states to implement logical gates. Here, we develop a theory of quantum gate teleportation protocols that implement non-Clifford gates on arbitrary input states without revealing any information about them; we refer to these protocols as magic gate teleportation (MGT). We uncover a hidden structure within MGT -- after backpropagating the Pauli measurements, MGT protocols can be viewed as encoding the input state into a stabilizer code heralded by the measurement outcomes, followed by a logical non-Clifford gate. Using this structure, we construct MGT protocols for any resource state obtained by applying commuting Pauli rotations to a stabilizer state, and provide an efficient algorithm for synthesizing their circuit implementations. Conversely, we prove that useful resource states for MGT, i.e., states that can be used for non-Clifford gates through MGT protocols, are necessarily Clifford-equivalent to diagonal states; in particular, the output state distilled from the $[\![5, 1, 3]\!]$ protocol is not useful for MGT. Finally, we identify conditions under which the feedforward operators can be implemented by Pauli operators, shedding light on the paradigm of algorithmic fault tolerance and simplifying the feedforward operations needed for quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08513v1
- Title: Metropolitan entanglement distribution between an atom and a near-visible photon
- Authors: Maya Büki, Pooja Malik, Florian Fertig, Tobias Frank, Marvin Scholz, Tommy Block, Gianvito Chiarella, Yiru Zhou, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08513v1  pdf=https://arxiv.org/pdf/2607.08513v1.pdf

Abstract:
Entanglement distribution is the overarching purpose of quantum networks. While communication over long distances can use deployed fiber infrastructure, it requires photons in the telecom band. However, advanced quantum network nodes do not operate at such wavelengths. Here we overcome this limitation with two tailor-made low-noise quantum-frequency converters to distribute entanglement between a single atom and a resonant photon over 14km line-of-sight via 24km of a deployed commercial fiber. The photon at wavelength 780nm is first entangled with the atom, then converted to the telecom S-band, and finally back-converted after propagation through the fiber. This link enables a photon transfer efficiency of 1.7% while affecting the atom-photon entanglement fidelity by less than 1%. This brings integration of atomic quantum nodes with existing long-distance fiber networks into reach, enabling novel applications in quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08517v1
- Title: Quantum Communication Lower Bounds for Search Problems via Matrix Discrepancy
- Authors: Minbo Gao, Chenghua Liu, Guangxu Yang, Tianyi Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08517v1  pdf=https://arxiv.org/pdf/2607.08517v1.pdf

Abstract:
We study one-way quantum communication lower bounds for search problems. Unlike decision problems, search problems can have many valid outputs, which pose a fundamental barrier to standard quantum lower-bound techniques. We overcome this by developing a novel method based on matrix discrepancy, which allows us to bound the output measurements of a quantum protocol jointly.   As applications of our method, we establish the first tight quantum lower bounds for two fundamental search problems in some natural parameter regimes: collision finding and triangle finding. For collision finding, we prove a tight $Ω(N^{1/4})$ one-way quantum communication lower bound. Previously, the best-known quantum communication lower bound for collision finding was $Ω(N^{1/12})$ due to Göös and Jain (RANDOM 2022), and no stronger bound was known even under the one-way restriction. For triangle finding in graph streams, we prove a one-pass quantum streaming space lower bound of $Ω\left(\sqrt{Δ_V}\right)$ for graphs with $m$ edges, $Θ(m)$ triangles, and constant $Δ_E$, where $Δ_V$ and $Δ_E$ denote the maximum number of triangles sharing a common vertex and edge, respectively, under the condition that $1\le Δ_V\le m^{2/3}$. This constitutes the first nontrivial quantum space lower bound in this regime, matching the classical upper bound of Jayaram and Kallaugher (RANDOM 2021) up to logarithmic factors. Notably, our method also recovers the classical lower bound of Kallaugher and Price (SODA 2017) through an entirely different argument, avoiding their Boolean-Hidden-Matching reduction that breaks down for quantum protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08530v1
- Title: The Langevin-equation description of optomechanics with the dispersive and dissipative optomechanical coupling
- Authors: Alexander K. Tagantsev
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08530v1  pdf=https://arxiv.org/pdf/2607.08530v1.pdf

Abstract:
The description of the optomechanical system is commonly based on the quantum Langevin equation formalism. This framework is introduced phenomenologically or based on a model Hamiltonian. However, once dealing with the optomechanical Fabry-Perot cavity or the modified Michelson-Sagnac interferometer with a semitransparent mechanically active membrane inside, a model-free consideration is also possible by using an alternative approach. Such an approach, which is based on the classical wave equations in the systems, is popular in the gravitational-wave community where it is termed as input-output relations approach. In this work, using the aforementioned approach, we derived the equations for the ladder operator of the intracavity field, stochastic back-action force, and the relation between the fields at the input mirror. Then we simplified the obtained results down to the range of applicability of the Langevin equation formalism and compared these with the corresponding predictions of the latter formalism. This enabled us to critically assess the validity of the Langevin equation formalism and rectify its range of applicability. In the case where the dissipative optomechanical coupling is involved we identified appreciable problems with this formalism. We found that, disregarding the fact that decay rate of the optomechanical Fabry-Perot cavity depends on its length, no dissipative optomechanical coupling is generated. This is in contrast with the prediction of the standard Langevin-equation based treatment. We found that, staying inside the range of applicability of the Langevin equation formalism, the relation between the fields at the input mirror may not be correct. We found that the Langevin equation formalism misses a phase factor at the input field, this factor turns out to be important for the situation involving the dissipative optomechanical coupling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08548v1
- Title: An Effective Quantum Hoare Logic for Hybrid Quantum Programs with Unbounded Loops
- Authors: Christophe Chareton, Jad Issa, Romain Péchoux
- Categories: quant-ph (primary); quant-ph; cs.PL
- Links: abs=https://arxiv.org/abs/2607.08548v1  pdf=https://arxiv.org/pdf/2607.08548v1.pdf

Abstract:
While quantum hardware remains limited, hybrid quantum-classical algorithms with complex control structures, including unbounded loops, are emerging, posing new challenges for quantum program analysis, including the accurate estimation of the resource consumption of a given program. Meanwhile, precise analysis techniques such as symbolic execution have largely left out hybridization and unbounded recursion. On the other hand, current quantum Hoare logics that generally support them are lacking in expressiveness and miss out on efficient computational equational reasoning that could be implemented in a semi-automated tool. This leaves a gap awaiting to be filled. In this work, we answer this challenge with the first semi-automated static analysis solution combining effective functional verification and resource (termination or cost) estimation for hybrid quantum programs with unbounded loops. Towards that end, we introduce integer hybrid path-sums (IHPS), extending path-sums to handle unbounded while loops, as a representation of possible executions of a program. A generic strategy for determining termination and expected resource consumption via loop invariants is also proposed and illustrated on several examples. Finally, the solution is implemented as a semi-automatic Haskell program. This work is the first step toward the design of a complete static resource analysis tool for hybrid quantum programs, essential for the development of real-world quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08560v1
- Title: QSCOUT's Qubit-Boson Gate Set
- Authors: Edward C. Tortorici, Ethan C. McGarrigle, Brian K. McFarland, Wes L. Johnson, Daniel S. Lobser, Melissa C. Revelle, Brandon P. Ruzic, Susan M. Clark, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08560v1  pdf=https://arxiv.org/pdf/2607.08560v1.pdf

Abstract:
The Quantum Scientific Computing Open User Testbed (QSCOUT) has developed a qubit-boson gate set for hybrid continuous-discrete variable (CV-DV) quantum computing. This document outlines how to utilize these gates on QSCOUT using Just Another Quantum Assembly Language, Jaqal\textsuperscript{TM}.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08591v1
- Title: Distributed Monogamy of Entanglement limits Quantum Channel Simulation
- Authors: Rabsan Galib Ahmed, Graeme Smith
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08591v1  pdf=https://arxiv.org/pdf/2607.08591v1.pdf

Abstract:
Entanglement is monogamous: if it is shared among more than two parties, the entanglement between any pair cannot be very strong. For an integer $k\geq 2$, $k$-extendibility of a state $ρ_{AB}$ quantifies this as the number of copies of $B$ that can be simulated by the state's environment. We introduce fractional extendibility, which gives a finer characterization of the quantum correlation that is leaked to the environment, and prove that it is invariant under tensor products and monotonic under local processing. We also establish the distributed monogamy of entanglement: for any state on $AB_1B_2\dots B_n$, the maximum average probability of extracting an EPR pair from a random subset of $k \leq n/2$ systems among the $B_i$'s is the fraction $k/n$. With these tools we show that any quantum erasure channel with erasure probability more than a half cannot simulate a less noisy erasure channel, even with asymptotically many uses of the more noisy channel.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08615v1
- Title: Operational meaning of Markov gap in tripartite entanglement of quantum dynamics
- Authors: Zongsheng Zhou, Riqiang Zhang, Yu-Xiang Zhang
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2607.08615v1  pdf=https://arxiv.org/pdf/2607.08615v1.pdf

Abstract:
We investigate how irreducible multipartite entanglement, a long-range correlation by nature, can emerge from short-range dynamics far from equilibrium. Focusing on the Markov gap as a probe of irreducible tripartite entanglement (IrTE) in free-fermion chains, we uncover qualitatively distinct dynamical behaviors: the Markov gap grows either quasi-linearly or in staircase-like jumps depending on the initial state. We also propose attainable upper and lower bounds for the onset time of IrTE based on the Lieb-Robinson bound. Strikingly, the Markov gap saturates to a volume-law value on a timescale $t\sim\! L^2$, much slower than the ballistic spreading of bipartite correlations. To understand what information about the wavefunctions is revealed by the Markov gap calculation, we introduce the concept of essential tripartite fermion (ETF) and an associated tripartite null matrix. The value of Markov gap closely tracks the number of small singular values of this tripartite null matrix, yielding a transparent, operational physical interpretation of the measure. We further demonstrate that several dynamical signatures persist in the interacting XXZ chain.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08626v1
- Title: A Nonstabilizerness Resource Law for Universal Quantum State Purification
- Authors: Keming He, Enji Xiong, Xin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08626v1  pdf=https://arxiv.org/pdf/2607.08626v1.pdf

Abstract:
Quantum state purification aims to recover higher-fidelity quantum states from multiple noisy copies and is a fundamental primitive for quantum information processing. Magic resources enable operations beyond classically simulable dynamics and are central to universal fault-tolerant quantum computation. Recent no-go results show that classically simulable operations cannot achieve a nontrivial universal fidelity gain. This motivates a quantitative theory of the magic required for purification at prescribed success probability and target fidelity. For universal purification with two input copies, we prove an exact linear mana law in odd dimensions and a two-sided linear robustness law for multi-qubit systems, which becomes exact for a single qubit. We also identify an explicit successful purification map that makes the tradeoff transparent. These results establish universal purification as a task obeying a quantitative magic-fidelity law and link magic resources to error mitigation and fault-tolerant quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08634v1
- Title: Triangulene-based diradicals as a blueprint for molecular quantum platforms with optical addressability and long spin coherence times
- Authors: Arup Sarkar, Cathal Hogan, Conor Ryan, Lorenzo A. Mariano, Alessandro Lunghi
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2607.08634v1  pdf=https://arxiv.org/pdf/2607.08634v1.pdf

Abstract:
The identification of molecules that combine long spin coherence times and efficient spin-optical interfaces, ideally at room temperature, is pivotal towards the development of molecular quantum technology. By means of advanced first-principles methods, we here unravel the electronic structure for triangulene (1), its aza-cation derivative (2), and the crystal of 2,6,10-tri-tert-butyl-4,8,12-trimesityl-triangulene (3), and show that these organic diradicals possess a triplet ground state well separated from the first singlet excited state approaching 0.5 eV, closely resembling solid-state defects like nitrogen vacancy centers. In addition, we compute spin decoherence times due to the interaction with phonons and surrounding nuclear spins, showing that a deuterated molecule of 3 in a nuclear spin-free environment would support $T_2 = 0.21$ ms at 10 K. Importantly, we show that the engineering of specific low-energy vibrations could significantly improve $T_2$ toward the limit imposed by the molecular core spin relaxation, here estimated to be as long as $T_1=27$ ms at 300 K for 2. Finally, we compute two-phonon contributions to inter-system crossing at 300 K for2 as a luminescent prototype, and find that it is highly spin-selective, supporting the possibility to engineer optical read out and spin initialization. These results advance a unified first-principles theoretical foundation of spin decoherence and spin-selective excited-state processes and point to novel chemical design strategies for optically addressable, highly coherent molecular qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08636v1
- Title: GroverFigureOfMerit: An Agnostic Figure of Merit for Quantum Backend Characterization in the NISQ Era
- Authors: Tiago Restucha, Marcos Guillermo Lammers, Alejandro Fernández
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08636v1  pdf=https://arxiv.org/pdf/2607.08636v1.pdf

Abstract:
The Noisy Intermediate-Scale Quantum (NISQ) era poses a challenge for developers: hardware providers expose capabilities through heterogeneous interfaces with proprietary metrics varying widely across providers, hindering informed backend selection. Static characterization metrics - coherence times T1/T2, gate error rates - exhibit limitations: they fail to capture dynamic variability across successive executions, overlook the impact of transpilation, and lack architectural comparability across physically distinct technologies. We propose a Figure of Merit (FoM) based on Grover's algorithm as an algorithmic stress test evaluating quantum backend performance holistically. The metric combines success probability on target states with penalties for non-uniform amplification and leakage to non-marked states, yielding a unified score across hardware architectures. Implemented via the Qonscious framework - a conditional execution platform using polymorphic adapters, it executes agnostically on IBM, IonQ backends, and simulators. Main contributions: (1) proposal and validation of GroverFigureOfMerit, incorporating uniformity and leakage penalties (adapted from GRADE) with emphasis on noise, transpilation, and topological constraints; (2) systematic analysis of heterogeneity across nine quantum providers motivating agnostic metrics; and (3) experimental demonstration via ideal simulators and real-processor noise models, confirming sensitivity to noise, topology, and transpilation overhead. Results confirm the metric distinguishes backend performance under a unified score, capturing intrinsic algorithmic limits. Validation on physical QPUs is identified as a natural next step.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08638v1
- Title: Symmetry as a route to generalized bosonic Kitaev chains
- Authors: Gideon Lee, Tony Jin, Aashish A. Clerk
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2607.08638v1  pdf=https://arxiv.org/pdf/2607.08638v1.pdf

Abstract:
The bosonic Kitaev chain (BKC) model is a deceptively simple looking quadratic pairing Hamiltonian. Despite being purely Hermitian, it exhibits a number of striking non-Hermitian topological phenomena, including skin effects. We show here how symmetries play a key role in this model, and how identifying these allows one to develop generalized BKC-like models. We emphasize the surprising fact that any quadratic bosonic pairing Hamiltonian with a sublattice (chiral) symmetry necessarily has a dynamical matrix with an effective time reversal symmetry. This symmetry is unrelated to physical time-reversal, but enables non-trivial topological invariants. We also discuss how this symmetry is unrelated to another key property of the BKC, the decoupling of quadrature dynamics. This feature can instead be connected to a distinct symmetry, namely an effective particle-hole symmetry of the dynamical matrix. We discuss non-trivial generalized BKC models that only keep one of these two effective symmetries intact. We also provide a classification of all translationally-invariant 1D pairing Hamiltonians, and show connections between the BKC and a well-studied non-Hermitian fermionic system, the symplectic Hatano-Nelson model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08649v1
- Title: Extracting conformal data from Loschmidt echoes after critical quenches
- Authors: Aleix Bou-Comas, Stefano Carignano, Sergio Cerezo-Roquebrún, Esperanza Lopez, Luca Tagliacozzo
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; hep-th
- Links: abs=https://arxiv.org/abs/2607.08649v1  pdf=https://arxiv.org/pdf/2607.08649v1.pdf

Abstract:
Conformal field theory provides universal predictions for Loschmidt amplitudes following quenches from product states to critical Hamiltonians. Building on this observation, we develop a route to extracting conformal data from real-time dynamics without preparing critical low-energy states. After analytic continuation, the Loschmidt amplitude is described by a boundary-CFT partition function on a strip, whose transverse transfer matrix encodes both the boundary operator spectrum and the central charge. Local space-time perturbations of the amplitude are governed by equilibrium correlation functions, and therefore provide access to critical exponents. In parallel, generalized temporal entropies exhibit scaling with time analogous to the equilibrium scaling of spatial entanglement entropy. We show that the low-lying boundary spectrum can be reconstructed from the system-size dependence of finite-chain Loschmidt echoes, whose damped oscillations encode differences of boundary scaling dimensions. Finally, we propose a finite-size scaling protocol that can extract these quantities from simulations or experiments on state-of-the-art quantum platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08655v1
- Title: Temperature Beyond Equilibrium in Isolated Quantum Many-Body Systems and Their Subsystems
- Authors: Maurizio Fagotti
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; math-ph
- Links: abs=https://arxiv.org/abs/2607.08655v1  pdf=https://arxiv.org/pdf/2607.08655v1.pdf

Abstract:
Temperature is one of the central concepts of thermodynamics, yet its meaning away from equilibrium remains elusive. This problem is particularly acute in isolated quantum many-body systems: their states evolve unitarily, need not be close to equilibrium, and can retain energy coherence, a feature with no classical thermodynamic analogue. A non-stationary quantum state contains two kinds of energy fluctuations. One is associated with energy populations and has the usual thermodynamic interpretation; the other arises from coherence between energy sectors and drives time dependence. We propose that temperature, also out of equilibrium, locates the state within the family of regular states compatible with its energy-coherence structure. This leads to a natural definition of temperature for regular nonequilibrium states. The resulting inverse temperature is not generally the derivative of thermodynamic entropy with respect to energy. Indeed the principle of maximum entropy does not extend in its usual form; it is replaced by a principle of minimum discrimination information. We also develop the corresponding theory for subsystems, where temperature cannot in general be inferred from the reduced state alone. Instead, it is determined by the induced local thermodynamic structure, with boundary ambiguities removed in the thermodynamic limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08686v1
- Title: Instability of the undecidable behavior of the spectral gap in 1D
- Authors: Laura Castilla-Castellano, Angelo Lucia
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08686v1  pdf=https://arxiv.org/pdf/2607.08686v1.pdf

Abstract:
The problem of determining the existence of a spectral gap in a lattice quantum spin system was previously shown to be undecidable for one [J. Bausch et al., "Undecidability of the spectral gap in one dimension", Physical Review X 10 (2020)] or more dimensions [T. S. Cubitt et al., "Undecidability of the spectral gap", Nature 528 (2015) and Forum of Mathematics Pi, 10 (2022)]. In this work, we focus on the 1-dimensional result, showing that the constructed family with undecidable behavior is extremely sensitive to perturbations. In particular, for any $\varepsilon > 0$, there exists a 1-local, rank 1, perturbation with norm $O(\varepsilon)$, such that the spectral gap problem for the family in [J. Bausch et al., "Undecidability of the spectral gap in one dimension", Physical Review X 10 (2020)] now becomes decidable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08687v1
- Title: Low-latency FPGA-based electronic control system for fast preparation of defect-free atom arrays
- Authors: Ya-Dong Hu, Dong-Qi Ma, Tian-Yang Zhang, Liang Chen, Yi-Chen Zhang, Xiao-Kang Zhong, Wen-Yi Zhu, Hong-Jie Fan, et al.
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2607.08687v1  pdf=https://arxiv.org/pdf/2607.08687v1.pdf

Abstract:
The scalability of neutral atom quantum computing demands integrated electronic control systems with low latency, modular architecture, and real-time feedback capability. Here, we present an FPGA-based electronic control system that eliminates the PC from the feedback loop, integrating photon counting, real-time decision-making, and waveform generation within a unified PXIe architecture. The system achieves a total feedback latency of $282\,\mathrm{μs}$ and is validated in practical experiments by assembling defect-free atom arrays from 24 stochastically loaded optical tweezers. A single-round rearrangement achieves a filling fraction of $\sim96\%$, while feedback-controlled iterative rearrangement over five rounds boosts the success probability for generating a 10-atom defect-free array from $65.7\%$ to $95.4\%$. This system establishes the electronic infrastructure necessary for mid-circuit measurement and real-time quantum error correction on neutral-atom platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08697v1
- Title: Quantifying randomness with measurement incompatibility
- Authors: Sebastian Schlösser, Pauli Jokinen, Martin Plávala, Leevi Leppäjärvi, Leonardo S. V. Santos, Roope Uola
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08697v1  pdf=https://arxiv.org/pdf/2607.08697v1.pdf

Abstract:
We present a trade-off between the amount of observed measurement incompatibility and the capabilities of a classical Eavesdropper in a prepare-and-measure scenario. The result is based on a qualitative connection between measurement incompatibility and randomness generation together with the utilization of incompatibility witnesses as randomness certificates. This allows one to use a geometric measure of incompatibility, the generalised robustness, to bound Eve's strategies through a semi-definite program, while providing an explicit protocol for generating randomness from any set of incompatible measurements. By translating the result to quantum steering, we find a tight connection between steerability and randomness generation in a setting using any finite number of measurement inputs. We further show how our techniques can be generalised to scenarios where Eve has a quantum memory by using a dimensional generalisation of joint measurability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08708v1
- Title: Absence of quantum advantage for approximate spin glass optimization
- Authors: Dries Sels, Flaviano Morone
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2607.08708v1  pdf=https://arxiv.org/pdf/2607.08708v1.pdf

Abstract:
We perform a semiclassical, large-spin S, analysis of the quantum approximate optimization algorithm (QAOA) on the Sherrington-Kirkpatrick (SK) model, using the truncated Wigner approximation. Fixing the QAOA angles to their previously determined optimal S=1/2 values, we observe a non-monotonic dependence of the final energy on the spin. At small S the semiclassics is dominated by noise, while the large-S limit is constrained by the exponential growth of the initial fluctuations. For a depth-p QAOA one achieves the optimal balance at S of order p, resulting in a convergence of the final energy to the Parisi value like log(p)/p. We find that the semiclassics slightly outperforms the true spin-1/2 QAOA, and thus suggest they both converge to the Parisi value in the same way. Finally, removing all the initial noise, and re-optimizing the parameters to account for that change, results in superior performance with 1/p convergence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08709v1
- Title: Robust One-Sided Device-Independent Quantum Key Distribution via High-Dimensional Steering
- Authors: Monika Mothsara, Suraj Goel, Bohnishikha Ghosh, Vatshal Srivastav, Will McCutcheon, Mehul Malik, Gláucia Murta
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08709v1  pdf=https://arxiv.org/pdf/2607.08709v1.pdf

Abstract:
Quantum key distribution (QKD) brings the promise of communication with information-theoretic security but is limited in practice due to its susceptibility to noise, losses, and device imperfections. To address these challenges, we propose a robust high-dimensional (HD) one-sided device-independent QKD (1sDI-QKD) protocol and present a proof-of-principle experimental implementation using photons entangled in the transverse-spatial degree-of-freedom. We develop a systematic security analysis of HD 1sDI-QKD protocols, leveraging quantum steering to certify security, and evaluate achievable secret key rates for different measurement configurations and system dimensions using reverse reconciliation. Our analysis shows that increasing the dimension enhances robustness against both noise and loss. We then demonstrate the key experimental building blocks required for implementing the protocol: (a) a high-quality source of high-dimensional photonic entanglement, and (b) a fully programmable, high-dimensional multi-outcome measurement device operating in up to dimension 11. Using these components, we obtain positive key rates for all investigated dimensions under the fair-sampling assumption, with the highest key rates achieved for dimension d=7. Finally, we discuss the steps required for a practical, loophole-free implementation of 1sDI-QKD in realistic regimes of loss and noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08713v1
- Title: Approaching Carnot Efficiency at Finite Power in an Experimentally Feasible Quantum Heat Engine
- Authors: Shogo Toma, Atsushi Noguchi, Ken Funo, Hiroyasu Tajima
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2607.08713v1  pdf=https://arxiv.org/pdf/2607.08713v1.pdf

Abstract:
Whether a heat engine can approach Carnot efficiency while maintaining finite power is a fundamental question in finite-time thermodynamics. For classical Markovian heat engines with local interactions, the power-efficiency trade-off forbids an asymptotic approach to Carnot efficiency at finite power. In quantum systems, by contrast, degeneracy, symmetry, and collective jumps have been theoretically predicted to enable such an asymptotic attainment by enhancing activity. It has remained open, however, whether this mechanism can be realized in an experimentally implementable heat engine. In this Letter, we propose a superconducting-circuit heat engine that emulates the collective enhancement, thereby enabling an asymptotic approach to Carnot efficiency at finite power. This result demonstrates that, in an implementable model, such an enhanced dissipative mechanism circumvents the power-efficiency trade-off of classical Markovian engines. Our work connects abstract bounds in finite-time thermodynamics to a concrete circuit-QED platform and suggests a route toward quantum-device design based on collectively enhanced dissipative processes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08760v1
- Title: Hockey stick $f$-divergences
- Authors: Fumio Hiai, Milán Mosonyi, Marco Tomamichel
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2607.08760v1  pdf=https://arxiv.org/pdf/2607.08760v1.pdf

Abstract:
In this paper we give a systematic and unified treatment and extensions of various results on a new notion of quantum $f$-divergences defined from quantum hockey stick divergences, the theory of which has been developed recently in \cite{BHT_fdiv,HircheTomamichel_integral,LiuHircheCheng2025}. In particular, we consider non-normalized states and hockey stick $f$-divergences defined from more general notions of quantum hockey stick divergences, as well as a somewhat more general form of the integral representation defined in terms of an additional real parameter. We also consider the extension of the theory to general von Neumann algebras, and extend various results from \cite{HircheTomamichel_integral,LiuHircheCheng2025} to this setting. Our main results here are the representation of the hockey stick $f$-divergences in terms of Neyman-Pearson error probabilities, which was given in the finite-dimensional case in \cite{LiuHircheCheng2025}, an extension of Jen\v cová's result \cite{Jencova2023} on the detection of reversibility of a quantum channel on a pair of states in terms of the hockey stick divergences, and an extension of a result in \cite{HircheTomamichel_integral} showing that the regularized hockey stick Rényi $α$-divergences coincide with the Petz-type Rényi divergences for $α\in(0,1)$ and with the sandwiched Rényi divergences for $α>1$. Moreover, we give some partial results on the characterization of when different notions of quantum $f$-divergences give the same value on a pair of quantum states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08761v1
- Title: Irreducible Geometry of Higher-Order Correlator Families
- Authors: Kaito Kobayashi
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2607.08761v1  pdf=https://arxiv.org/pdf/2607.08761v1.pdf

Abstract:
Programmable quantum simulators are beginning to access correlators of increasing complexity, ranging from four-point out-of-time-ordered correlators to even higher-order many-body correlators. The theoretical framework for interpreting such data, however, remains comparatively underdeveloped. Although a variety of higher-order correlators can be constructed straightforwardly, their physical meaning is often difficult to infer. A further complication is that different correlators are generally not independent: some may be mutually redundant, while others may encode genuinely distinct information. These features make it necessary to analyze correlators not as isolated quantities, but as a structured family. In this work, we develop a geometric framework for the collective analysis of higher-order correlator families. By representing correlators as inner products between operator words, we recast each family as a geometry in operator space. The key idea is to introduce conditioning subspaces that separate this geometry into reducible information, already explained by a chosen resolved sector, and irreducible information, encoded in the residual correlator geometry. Focusing on the latter component, we define irreducible volume profiles that quantify how broadly the unexplained part of a correlator family spreads over independent geometric directions. This perspective leads to several complementary forms of conditioning. Canonical conditioning optimally explains a correlator family. Targeted conditioning fixes the resolved sector to isolate a chosen physical feature. Krylov and cross conditioning extend the framework from a single correlator family to comparisons among correlator geometries. Our framework reveals irreducible structures hidden at the level of individual correlator values and establishes correlator geometry as a higher-level description of quantum many-body dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08762v1
- Title: Typicality of Steering for Two-qubit States
- Authors: Gerard Anglès Munné, Paweł Cieśliński, Tamás Vértesi, Wiesław Laskowski
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08762v1  pdf=https://arxiv.org/pdf/2607.08762v1.pdf

Abstract:
Phenomena that slip beyond the grasp of our classical intuition reveal uniquely quantum effects that deepen our understanding of the physical world and enable advances in information processing, particularly in quantum communication and computation. One such phenomenon is quantum steering, whereby measurements performed by one party influence the conditional states of another when the two share an entangled quantum system. If the observed correlations cannot be explained by a local hidden state model, the state is said to be steerable. In this work, we investigate the typicality of this behavior: given a generic two-qubit state and $m$ Haar-random projective measurements, what is the probability of observing steering? We derive analytical expressions for the steering probability $\mathcal{P}_S$ of Werner states in two- and three-setting scenarios, the latter restricted to coplanar projective measurements on the Bloch sphere. For larger numbers of settings and various random states ensembles, we perform numerical analyses showing that $\mathcal{P}_S$ increases systematically with the number of measurements and substantially exceeds the corresponding probabilities associated with Bell nonlocality. Our results demonstrate that random states with minimal environmental coupling exhibit a high probability of steering for finite $m$ and approach genuine typicality, $\mathcal{P}_S=100\%$, as the number of settings increases. We provide a detailed characterization of $\mathcal{P}_S$ across different state ensembles and specific families, including Bell-diagonal and Werner states, identifying those with the greatest non-classical potential and highlighting their relevance for protocols in which steering serves as a key resource.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08767v1
- Title: Plaquette: A hardware-aware design platform for fault-tolerant quantum computers
- Authors: Raul Conchello Vendrell, Carlos Díaz López, Ish Dhand, Kshitij Kapoor, Davide Laureti, Marcello Massaro, Pranjal Nayak, Ivan Ogloblin, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2607.08767v1  pdf=https://arxiv.org/pdf/2607.08767v1.pdf

Abstract:
Hardware teams building fault-tolerant quantum computers (FTQCs) must decide which imperfections to suppress, and that decision requires the logical performance of the architecture under the device's actual noise. Hardware noise often departs from the stochastic Pauli models used by scalable stabilizer simulators: superconducting transmons leak out of the computational subspace, neutral atoms scatter through intermediate states, trapped ions heat as their motional modes absorb phonons, and miscalibrated controls over-rotate coherently. We present Plaquette, a theoretical framework and software suite that computes the logical performance of fault-tolerant architectures directly from the physics of such imperfections. In Plaquette, a hardware error model is specified once, as Kraus operators, Hamiltonian-Lindblad dynamics, or an experimentally reconstructed quantum channel, and is compiled automatically into the exact or approximate representation required by each of four sampler classes: stabilizer sampling for Pauli noise, the new XPauli sampler for leakage and environment sectors, near-Clifford samplers for coherent errors, and full-state simulation for exact reference calculations. We validate the XPauli and near-Clifford samplers against full-state simulation, which they can match within statistical uncertainty while Pauli twirling can fall short depending on the error model. We demonstrate the framework on three error models: leakage in superconducting qubits, intermediate-state scattering in neutral atoms, and heating in trapped ions. The size of the discrepancy between Plaquette and Clifford-only simulations varies with platform and noise process, so reliable thresholds, error budgets, and overhead estimates require the most accurate simulation available. Plaquette provides a direct path from the open-system physics of a device to the logical performance of the FTQC built on it.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.04905v2
- Title: Entropy bounds, Geroch process, and the sign of deformation parameter
- Authors: Bijan Bagchi, Akshat Pandey, Parmest Roy, Sauvik Sen
- Categories: hep-th (primary); hep-th; gr-qc; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.04905v2  pdf=https://arxiv.org/pdf/2607.04905v2.pdf

Abstract:
Based on Geroch's process of dropping a system into a black hole from the vicinity of the horizon, we investigate in this paper the influence of deformation on the Bekenstein entropy bound both for (3+1) and (2+1) dimensions in the context of a generalized uncertainty principle (GUP). While providing a coherent framework that sets an upper limit on the entropy across dimensions we show, within a semiclassical treatment, that while a negative GUP deformation yields a universal relaxation of the bound, a positive deformation tightens it. Our results may be interpreted as a response to Planck-scale modifications of the near-horizon redshift.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07747v1
- Title: Second-harmonic signal in electric-field-modulated EPR spectra of Fe3 spin triangles
- Authors: Jason S. R. McCoombs, Jorge I. Hilari, Jérôme Robert, Balwant Singh Chauhan, Ratnamala Chatterjee, Filippo Troiani, Athanassios K. Boudalis
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07747v1  pdf=https://arxiv.org/pdf/2607.07747v1.pdf

Abstract:
We present electric-field-modulated electron paramagnetic resonance (EFM-EPR) measurements on centrosymmetric single crystals of the molecular spin triangle $\mathrm{[{Fe_3}O({O_2}CPh){_6}(py){_3}]ClO{_4}{\cdot}py}$ ($\bf{Fe_3}$). We provide the first observation of second harmonic EFM-EPR signal in polynuclear magnetic molecules. This signal is simulated and explained in terms of an electric-field induced modulation of the isotropic exchange in the molecule, and of their symmetry lowering resulting from a Jahn-Teller effect. Additionally, an unexpected first harmonic EFM-EPR signal is observed. Various plausible symmetry-breaking mechanisms are discussed in an attempt to explain this feature, whose observation is unexpected in a nominally centrosymmetric crystal.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07754v1
- Title: Image classification via a quantum-inspired strategy involving a mixture of experts
- Authors: Kumari Jyoti, Rohith Babu, Apoorva D. Patel
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07754v1  pdf=https://arxiv.org/pdf/2607.07754v1.pdf

Abstract:
Pattern recognition problems arise in a variety of physical image processing situations, and convolutional neural networks are a popular scheme for the required feature extraction and classification tasks. The classical networks use diffusion-based smearing and block-wise pooling to downsample the image data and capture important structural features. In this work, we propose and demonstrate a more efficient quantum-inspired strategy involving a mixture of experts. It is a hybrid classical-quantum framework. The quantum part consists of amplitude encoding of the images, convolution using local unitary operations, multiple experts processing the same image with different parameters, and feature extraction using quantum stabiliser codes. The classical part then jointly processes the features extracted by different experts using a standard fully connected neural network for image class prediction. Using MNIST and Fashion-MNIST datasets as benchmarks, we demonstrate that the joint expert analysis outperforms the individual expert one, as well as reduces the failure rate of image class prediction by around a factor of two. The overhead of our quantum-inspired strategy is only moderate on GPU workstations, which makes our proposal a practical alternative to existing classical schemes. We also point out how the quantum part of our framework can be executed on a quantum processor.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07799v1
- Title: No off-diagonal quantum focusing for Rényi divergences
- Authors: Tanay Kibe, Pratik Roy
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07799v1  pdf=https://arxiv.org/pdf/2607.07799v1.pdf

Abstract:
The quantum focusing conjecture is a mathematical expression of the idea that semiclassical gravity remains universally attractive. Its off-diagonal part is a monotonicity condition on the double null shape variation of relative entropy on distinct null generators, and has been argued to follow from strong subadditivity of entanglement entropy. Recent proof of a diagonal Rényi quantum null energy condition raises the question: does a full Rényi focusing statement also hold? We answer this question negatively for any Rényi-type divergence satisfying data processing, tensor additivity, and matched classical--quantum conditioning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07871v1
- Title: Quantum Dot Moiré from Crossed MoS2 Nanoribbons
- Authors: Xinting Shuai, Hao Zhang, Wenjing Wu, Chongning Wu, Maryam Amiri, T. A. M. Ragib Shahriar, Dian Pan, Zhi Kai Ng, et al.
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; cond-mat.mes-hall; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07871v1  pdf=https://arxiv.org/pdf/2607.07871v1.pdf

Abstract:
Twisted atomically thin layers have attracted much attention for Moiré potential and correlated quantum phenomena. However, existing Moiré superlattices have largely been limited to extensive wavefunction without lateral confinement. Here we introduce a new platform where 1D nanoribbons of 2D MoS2 grown by vapor deposition can be easily superposed at various angles from stacking and transferring, to form Moiré quantum dots at their intersections with unique exciton physics. Angle-dependent Moiré intersections show enhanced exciton emission at commensurate angle 22 deg, which demonstrates faster relaxation at the cryogenic temperature. A size-dependent study further exhibits a reduced exciton energy and soften out-of-plane interlayer coupling for smaller Moiré areas. Our results reveal exciton physics turnability via precise overlapping of 1D nanoribbons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07913v1
- Title: A majorization relation for a sum of two tensor products of positive semidefinite operators
- Authors: Mohammad A. Alhejji, Cole Kelson-Packer
- Categories: math.RA (primary); math.RA; math-ph; math.CO; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07913v1  pdf=https://arxiv.org/pdf/2607.07913v1.pdf

Abstract:
We use linear programming to prove a separable version of Ky Fan's majorization relation for a sum of two operators that are each a tensor product of $n$ positive semidefinite operators. We give an example showing that such a relation does not hold in general for sums of three or more tensor products of three or more positive semidefinite operators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07929v1
- Title: Dual-Platform Precision Measurement of the $3^2D_{5/2}$ to $4^2S_{1/2}$ $g$-Factor Ratio in $^{40}\text{Ca}^+$
- Authors: Brian J. McMahon, Vikram S. Sandhu, John M. Gray, Creston D. Herold, Kenton R. Brown, Brian C. Sawyer
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07929v1  pdf=https://arxiv.org/pdf/2607.07929v1.pdf

Abstract:
We report precision measurements of the ratio of Landé $g$ factors between the $3^2D_{5/2}$ and $4^2S_{1/2}$ states of a single trapped $^{40}\text{Ca}^+$ ion. The measurements are performed in two distinct ion trap apparatus: a cryogenic surface electrode radiofrequency Paul trap and a room-temperature permanent magnet Penning trap. The Penning trap measurements yield a ratio of $0.599~488~813~3(2)$, which represents a more than 40-fold uncertainty reduction compared to previous work. The radiofrequency trap measurement yields a concurring value of $0.599~488~813(6)$. We estimate that systematic shifts for each system are well below the respective statistical uncertainty.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07932v1
- Title: Gate induced strain on a two-dimensional hole gas in silicon
- Authors: D. van der Bovenkamp, C. S. A. Müller, B. D. Pantiru, I. Bošnjak, M. Cignoni, Q. Torrent Nicolau, M. E. Bal, S. Wiedmann, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07932v1  pdf=https://arxiv.org/pdf/2607.07932v1.pdf

Abstract:
We show the effect of gate-induced strain on the valence band of a silicon (Si) metal oxide semiconductor (MOS) confined two-dimensional hole gas (2DHG). Increasing aluminum gate thickness, and thereby the strain in the channel, results in the onset of a second subband contributing to Shubnikov-de Haas oscillations. Temperature-dependent magnetotransport measurements reveal distinct cyclotron masses of $m_c^*=(0.36\pm0.04)m_0$ and $m_c^*=(0.49\pm0.02)m_0$. The measured cyclotron masses differ from those expected for an idealized heavy-hole (HH)/light-hole (LH) picture, reflecting the combined influence of quantum confinement, strain, and HH-LH mixing on the valence band.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07983v1
- Title: Theoretical ab initio Evolution of Satellite Intensity near Threshold for Cu K-shell transitions
- Authors: Daniel Pinheiro, Gonçalo Baptista, César Godinho, André Fernandes, Jorge Machado, Pedro Amaro, Nancy Paul, Martino Trassinelli, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07983v1  pdf=https://arxiv.org/pdf/2607.07983v1.pdf

Abstract:
In this work, we have investigated the evolution of satellite intensity near the ionization threshold for Cu K-shell transitions through theoretical methods. Employing standard state-of-the-art ab initio methods, we have calculated all Cu K-shell transitions and simulated the full K$α_1$ and K$α_2$ spectrum where all transition parameters, as well as shake probabilities were determined theoretically. Through these calculations we show that standard state-of-the-art ab initio methods achieve good agreement with experiment and enable us to simulate the intensity evolution near ionization thresholds within a good margin of error. Below-threshold satellite intensity was found to originate from resonant 1s$\rightarrow$3d and 1s$\rightarrow$4p excitations in Cu(I) and Cu(II) oxide phases respectively, which were included in our simulations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.07997v1
- Title: Smoothing Exponents and Decoupling in Semifinite von Neumann Algebras
- Authors: Zhiwen Lin, Hongsen Qiu, Xinyu Zhang
- Categories: cs.IT (primary); cs.IT; math.OA; quant-ph
- Links: abs=https://arxiv.org/abs/2607.07997v1  pdf=https://arxiv.org/pdf/2607.07997v1.pdf

Abstract:
We study the smoothing exponent of the max-relative entropy in semifinite von Neumann algebras. Our main result gives an exact exponent formula in this setting. The proof develops operator-algebraic replacements for the dimension-dependent tools used in finite-dimensional arguments. These ingredients show that the smoothing exponent is governed by the underlying von Neumann algebraic structure rather than by matrix dimension estimates. As an application, we formulate catalytic quantum information decoupling with a semifinite von Neumann algebraic reference system. We prove an intrinsic layer-cake lemma for von Neumann algebras, which removes the countable spectrum assumption in the finite-dimensional proof and yields the corresponding semifinite estimate. Consequently, the decoupling reliability exponent is described by the same sandwiched Rényi mutual information formula as in the finite-dimensional theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08023v1
- Title: Interfacial chirality-induced magnetic-field-free switching with high energy efficiency in all-vdW heterostructures
- Authors: Kai-Xuan Zhang, Suik Cheon, Seungbok Lee, Joonyoung Choi, Jihoon Keum, Hyuncheol Kim, Yeochan An, Woonghee Cho, et al.
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08023v1  pdf=https://arxiv.org/pdf/2607.08023v1.pdf

Abstract:
Chirality, a central concept across many scientific disciplines, continues to inspire the discovery of novel physical phenomena. In condensed matter physics, structural chirality - defined by the absence of mirror plane symmetries - has primarily been explored in bulk materials. However, new chiral phenomena can emerge uniquely at the interface, distinct from their bulk counterparts, when a chiral material forms a heterostructure. Here, we demonstrate that all van-der-Waals (vdW) heterostructure composed of the chiral Co1/3TaS2 and the achiral vdW ferromagnet Fe3GeTe2 exhibits two distinct and unconventional spin-orbit torques originating from the interfacial chirality. These torques enable magnetic-field-free switching of perpendicular magnetization with ultralow current density ~ 10^6 A/cm^2 and minimal power dissipation < 10^15 W/m^3. Moreover, by replacing Fe3GeTe2 with a similar vdW ferromagnet, Fe3GaTe2, but of higher Curie temperature, we achieved the magnetic-field-free switching at room temperature in the Fe3GaTe2/Co1/3TaS2 vdW heterostructure. Our findings establish interfacial chirality as a powerful new handle for spintronic control, opening a new pathway to explore chirality-induced phenomena beyond the bulk symmetry constraints - and paving the way toward highly efficient, low-power spintronic devices based on all-vdW heterostructures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08169v1
- Title: Overview of Applications of Quantum Computing in QCD
- Authors: Germán Rodrigo
- Categories: hep-ph (primary); hep-ph; hep-ex; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08169v1  pdf=https://arxiv.org/pdf/2607.08169v1.pdf

Abstract:
Quantum computing has emerged as a promising framework for addressing computationally demanding problems in collider physics. In recent years, a growing number of quantum algorithms have been proposed for applications ranging from event generation and parton shower simulation to the evaluation of scattering amplitudes, loop and phase-space integration, and optimization problems relevant to experimental analysis. We provide a concise overview of the main ideas behind these developments, with emphasis on the potential advantages of quantum approaches in comparison with classical methods, as well as on the current limitations imposed by noisy intermediate-scale quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08235v1
- Title: Full-Spectrum Quantum Simulation for the Nuclear Shell Model
- Authors: B. Maheshwari, P. Stevenson, P. Van Isacker
- Categories: nucl-th (primary); nucl-th; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08235v1  pdf=https://arxiv.org/pdf/2607.08235v1.pdf

Abstract:
The nuclear shell model is a general way of expressing the many-body nuclear Hamiltonian and deciphering the underlying nuclear structure. In today's era of modern and high-power computation, the primary limitation of the nuclear shell model is the enormous dimensionality of its Hilbert space, which far exceeds available storage capacity and prevents the diagonalization of the full Hamiltonian matrix in that space. Quantum computing offers a scalable solution to bypass this curse of dimensionality. In this work, we introduce a single-run quantum simulation capable of obtaining multiple shell-model eigenstates simultaneously. The nuclear Hamiltonian is transformed from a bit to a qubit basis using the Jordan-Wigner transformation, explicitly preserving fermionic anti-commutation. We employ a Subspace Search Variational Quantum Eigensolver (SSVQE) along with an Adaptive Derivative-Assembled Pseudo-Trotter (ADAPT) ansatz to construct the quantum circuit required to solve the shell-model problem. The ADAPT-SSVQE algorithm uses a symmetry-preserving single and double-excitation operator pool and optimizes a weighted energy sum to obtain the simultaneous convergence of all eigenstates within a targeted MJ subspace, eliminating the need for post-processing efforts to extract excited spectra. We benchmark this approach by solving the problem for two and three identical nucleons in a j = 9/2 orbital, successfully extracting five and ten mutually orthogonal states, respectively, within a 10-qubit active space. The algorithm achieves spectroscopic accuracy, in simulation, relative to exact diagonalization and intrinsically restores total angular momentum (\hat{J}^2) symmetry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08294v1
- Title: Interplay of Quasiperiodic Criticality and the Non-Hermitian Skin Effect
- Authors: Zhangyuan Chen, Xianqi Tong, Xiaosen Yang
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08294v1  pdf=https://arxiv.org/pdf/2607.08294v1.pdf

Abstract:
Quasiperiodic lattices can host critical eigenstates, whereas nonreciprocal hopping in non-Hermitian lattices can induce non-Hermitian skin effect. In this work, we investigate localization phenomena in a Hatano--Nelson model with quasiperiodically modulated hopping amplitudes, where nonreciprocity arises from unequal modulation strengths of the right and left hoppings. Using a non-unitary gauge transformation, we map the non-Hermitian system into a Hermitian quasiperiodic system and obtain an exact analytical expression for the Lyapunov exponent in the thermodynamic limit. Under periodic boundary conditions, inverse participation ratios and finite-size scaling analysis are used to identify the quasiperiodic critical regimes. The comparison shows that parameter regimes hosting quasiperiodic critical states under periodic boundary conditions can exhibit the non-Hermitian skin effect under open boundary conditions. Furthermore, the non-Hermitian skin effect associated with quasiperiodic critical regimes is also observed in representative long-range hopping models and multiband extensions. Our results provide an analytically controlled perspective on how quasiperiodicity, modulated nonreciprocity, and boundary conditions jointly shape the non-Hermitian skin effect in critical regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08298v1
- Title: Wigner symmetries single out symmetric Wasserstein distances in all finite dimensions
- Authors: Gergely Bunth
- Categories: math-ph (primary); math-ph; math.OA; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08298v1  pdf=https://arxiv.org/pdf/2607.08298v1.pdf

Abstract:
We study the quantum Wasserstein distances introduced by De Palma and Trevisan associated with quadratic cost operators generated by families of self-adjoint observables. We first show that an arbitrary positive semidefinite cost operator is completely determined by the restriction of the corresponding Wasserstein distance to pairs of pure states. This allows geometric invariance of the pure-state distance to be translated directly into invariance of the cost operator.   Within the class of nonzero quadratic costs generated by at most $d^2-1$ observables on a $d$-dimensional Hilbert space, we prove that the Wasserstein isometry monoid consists exactly of the Wigner symmetries, that is, unitary and antiunitary conjugations, if and only if the distance is invariant under unitary conjugations on pure states. Equivalently, the cost operator intertwines the adjoint representation of the unitary group and is a positive scalar multiple of the identity on the traceless subspace.   We further construct explicit mutually inverse maps between quadratic cost operators generated by observables and Hilbert--Schmidt frame-type operators formed from their traceless parts. Under this correspondence, isotropy of the cost is equivalent to the tight frame property of the associated Hilbert--Schmidt operator. Consequently, a nonzero isotropic cost requires at least $d^2-1$ self-adjoint generators, and equality holds precisely when their traceless parts form, up to a common scale, a Hilbert--Schmidt orthonormal basis. Thus the geometric, representation-theoretic, operator-theoretic, and frame-theoretic notions of symmetry all determine the same one-parameter family of quantum Wasserstein distances.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08315v1
- Title: Magnetic control of Goos-Hänchen shifts and group delay time in monolayer WSe$_2$
- Authors: Youssef Fattasse, Rachid El Aitouni, Miloud Mekkaoui, Pablo Díaz, David Laroze, Ahmed Jellal
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08315v1  pdf=https://arxiv.org/pdf/2607.08315v1.pdf

Abstract:
We study the influence of an external magnetic field on the Goos-Hänchen (GH) shift and the group delay time (GDT) in monolayer WSe$_2$ in the presence of a magnetic barrier. The transport properties of Dirac-like carriers are obtained by solving the effective low-energy Hamiltonian and evaluating the corresponding transmission amplitudes. The GH shift and the GDT are subsequently extracted from the phase of the transmission coefficient. We systematically analyze their dependence on the magnetic field strength, incident energy, angle of incidence, and barrier width, with particular emphasis on the spin and valley degrees of freedom associated with the $K$ and $K'$ valleys. Our results show that the magnetic barrier strongly modulates both the GH shift and the GDT, leading to oscillatory behavior and pronounced spin-valley-dependent transport characteristics. Remarkably, the magnetic field enables selective control of the lateral shift and traversal time of carriers for each spin and valley channel, allowing for tunable spatial and temporal separation of electronic wave packets. This provides a mechanism for manipulating fermionic trajectories after transmission through the barrier in a highly controllable manner. Such tunability opens promising avenues for designing nanoscale devices based on spin and valley filtering, as well as for potential applications in information storage and processing within spintronic and valleytronic platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08320v1
- Title: Approximate eigenfunctions for some aperiodic crystals
- Authors: Long Meng
- Categories: math-ph (primary); math-ph; cond-mat.mes-hall; math.FA; math.SP; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08320v1  pdf=https://arxiv.org/pdf/2607.08320v1.pdf

Abstract:
In this paper, we consider Hamiltonians for aperiodic crystals of the form \begin{align*}   H_\varepsilon:=T(-i\nabla_x+{\mathbf A}(x,\varepsilon x))+V(x,\varepsilon x),\qquad x\in {\mathbb R}^d \end{align*} where $T$ represents either a Dirac operators or a Schrödinger operator, and $x\mapsto {\mathbf A}(x,X)$ and $x\mapsto V(x,X)$ are $\mathbb L$-periodic with respect to some lattice $\mathbb L\subset{\mathbb R}^d$.   Let \begin{align*}   (k,X)\ni {\mathbb R}^d\times {\mathbb R}^d\mapsto h(k,X):=T(-i\nabla_x+k+{\mathbf A}(x,X))+V(x,X) \end{align*} be a family of operators acting on $L^2_{\rm per}(\mathbb{R}^d/\mathbb{L})$ with periodic boundary conditions. We show that, under some suitable assumptions on the family of operators $ (h(k,X))_{k,X}$ around an energy level $e_0\in {\mathbb R}$ and some points $(k_0,X_0)\in {\mathbb R}^d\times {\mathbb R}^d$, one can construct localized approximate eigenfunctions $Φ_\varepsilon\in L^2({\mathbb R}^d)$ of the operator $H_\varepsilon$ such that for $\varepsilon$ small enough and for some $m\in \{1,2\}$ and $μ\in {\mathbb R}$, \begin{align}\label{eq:abstract}   \|(H_\varepsilon-e_0-\varepsilon^{\frac{m}{2}}μ)Φ_\varepsilon\|_{L^2({\mathbb R}^d)}={\mathcal O}(\varepsilon^{\frac{m}{2}+\frac{1}{4}}). \end{align} with \begin{align*}   \|Φ_\varepsilon\|_{L^2({\mathbb R}^d)}=\frac{1}{|{\mathbb R}^d/\mathbb L|^{1/2}}+{\mathcal O}(\sqrt{\varepsilon}). \end{align*}

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08418v1
- Title: Efficient photo-ionizing elimination of detrimental electric fields for Rydberg atoms
- Authors: Zhou-Chen Deng, Hao-Nan Lin, Yu-Cheng Duan, Qi Zhang, Xiang-Can Cheng, Yang Liu, Zhao-Yang Yuan, Jie Li, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08418v1  pdf=https://arxiv.org/pdf/2607.08418v1.pdf

Abstract:
Rydberg atoms are highly sensitive to external electric fields due to their exaggerated electronic properties. This unique feature lays the foundation for many of their applications in quantum science. However, an uncontrolled stray electric field can be detrimental, severely degrading their quantum control. In this work, we demonstrate a universal scheme that relies on the efficient creation of an in-vacuum plasma source by photo-ionizing laser-cooled atoms to eliminate detrimental electric fields in a Rydberg-atom tweezer array platform, requiring only readily available resources. With this method, we began with a Stark-ionized Rydberg continuum spectrum caused by a large, unknown stray electric field and ultimately recovered stable, coherent excitation of an individual Rydberg state after fully eliminating the field. Our method is directly applicable to existing Rydberg-atom platforms and can also be useful in other experiments sensitive to stray electric fields.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08421v1
- Title: Fourier imaging of collective spontaneous emission modes in superradiant cold atomic clouds
- Authors: Adrien Gavalda, Guillaume Tremblier, Martin Poitrinal, Sara Pancaldi, Antoine Browaeys, Igor Ferrier-Barbut
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08421v1  pdf=https://arxiv.org/pdf/2607.08421v1.pdf

Abstract:
We measure the spatial pattern associated with the superradiant emission from a cloud of cold 87Rb atoms using Fourier imaging. We observe a highly directional, ring-shaped emission structure, which corresponds to a single collective jump operator associated to the most superradiant mode of the ensemble. Using spatial filtering, we isolate this channel and find the typical superradiant burst with superlinear scaling of the intensity with atom number. We compare our results to two models that describe the competition between the various decay channels, finding good agreement. Our work shows that the collective jump operators introduced by Carmichael et al. [Optics Communications 179, 417 (2000)] can be measured and manipulated.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08568v1
- Title: Renormalization flows for 1D mixed states and a quantum Goursat lemma
- Authors: Léo Le-Nestour, David Pérez-García, Alberto Ruiz-de-Alarcón
- Categories: math-ph (primary); math-ph; cond-mat.str-el; math.QA; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08568v1  pdf=https://arxiv.org/pdf/2607.08568v1.pdf

Abstract:
Renormalization provides a framework for relating microscopic models of physical systems to effective descriptions at larger length scales. This procedure is studied for the boundary states of non-chiral two-dimensional topologically ordered models. The initial data consist of renormalization fixed points built from representations of finite-dimensional $C^*$-Hopf algebras, which are then perturbed by uniform on-site noise quantum channels and repeatedly coarse-grained. The resulting flows admit an intrinsic algebraic description in terms of completely positive maps on the $C^*$-Hopf algebra or, equivalently, positive linear functionals on its enveloping $C^*$-Hopf algebra. Their iteration is governed by convolution powers, and convergent trajectories yield new matrix product density operator fixed points, described by finite $*$-quantum hypergroups. This provides a concrete physical interpretation of such structures. For finite group algebras and their duals, we provide explicit classifications via Goursat's lemma for groups. Finally, we formulate and prove a quantum generalization of Goursat's lemma for finite-dimensional $C^*$-Hopf algebras, a result of independent interest, which gives an explicit structural description of all convergent renormalization trajectories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08583v1
- Title: Holographic Theory of Mixed-Dimensional Statistics and Conservation-Encoding Hopping-Operator Algebras
- Authors: Hanyu Xue, Xiao-Gang Wen
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08583v1  pdf=https://arxiv.org/pdf/2607.08583v1.pdf

Abstract:
We develop a general framework for the statistics of mixed-dimensional excitations subject to intertwined conservation laws, extending the familiar Fermi statistics with conserved particle number. We define statistics microscopically through a \emph{hopping-operator algebra}: a local operator subalgebra (LOsA) generated by operators that locally move or deform excitations while preserving the conservation law. Nontrivial statistics arise when this subalgebra is nontrivial.   We first focus on LOsAs that encode \emph{pointed} conservation laws. These give rise to invertible excitations, whose fusion rules are exactly those of the symmetry defects of a higher group $\cG$. For such $\cG$-conserved excitations in $d$-dimensional space, we show that the corresponding LOsA -- and hence the statistics it defines -- is classified by a cohomology class $[ω] \in H^{d+2}(B\cG;\R/\Z)$, where changing $[ω]$ by a coboundary corresponds merely to a rephasing of the local operators. We further provide a holographic realization: excitations with this prescribed conservation law and statistics live on the boundary of a $\cG$ higher-group gauge theory in $(d+1)$-dimensional space, twisted by $[ω]$.   More generally, non-pointed conservation laws and the associated statistics of non-invertible excitations are defined by a pair: a LOsA together with its excitation-complex representation. This is equivalent to the pair consisting of a LOsA and its Hilbert-space representation, which is the data defining a generalized symmetry. Consequently, non-pointed conservation laws and their statistics in $d$-dimensional space are classified by fusion $d$-categories, just as generalized symmetries are. The higher-group results above are the fully-pointed special cases of this more general classification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08589v1
- Title: Universality of Measurement-Induced Criticality under Symmetry-Breaking Measurements
- Authors: Angelo Russotto, Filiberto Ares, Pasquale Calabrese
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08589v1  pdf=https://arxiv.org/pdf/2607.08589v1.pdf

Abstract:
We study the critical properties of random quantum circuits with a $U(1)$ symmetry subject to local projective measurements that explicitly break this symmetry. We find that, at the measurement-induced phase transition, symmetry-breaking measurements act as a relevant perturbation at large scales, leading to the same universal critical properties as the corresponding monitored random circuit with non-symmetric unitary dynamics. In particular, we consider monitored $U(1)$-symmetric Haar-random circuits in the limit of large local Hilbert-space dimension, where the trajectory-averaged entanglement entropy can be exactly obtained in terms of a classical statistical mechanics model. In this model, the charge associated with the conservation law follows a symmetric simple exclusion process, in which symmetry-breaking measurements correspond to disordered defects that create and destroy charges. We prove that the charge correlation length remains finite for any measurement rate, ruling out a charge-sharpening transition, in contrast to the case of symmetry-preserving measurements. We further support our predictions at finite local Hilbert-space dimension through numerical finite-size scaling analyses of the entanglement transition in monitored $U(1)$-symmetric Haar and stabilizer random circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.08684v1
- Title: Entanglement Wedge Reconstruction without Holographic Quantum Error Correction
- Authors: Seiji Terashima
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2607.08684v1  pdf=https://arxiv.org/pdf/2607.08684v1.pdf

Abstract:
Bulk reconstruction is a central problem in AdS/CFT, and entanglement wedge reconstruction is its subregion version. We argue that this subregion statement should be separated from the stronger holographic quantum error correction interpretation, in which one region-independent logical bulk operator has code-preserving representatives in several boundary regions. A simple locality argument shows that such a common reconstruction must commute with the code-preserving local algebras in the complementary regions. This is the mechanism realized in HaPPY-type codes: the erased regions are blind to a protected logical algebra. An ordinary finite $N$ holographic CFT does not have such a protected invisible sector for supergravity fields. Its low-energy local observables, in particular, suitably smeared stress tensors, detect the physical support and gravitational dressing of ordinary bulk operators, up to possible center or superselection data. Thus, there is no such holographic quantum error correction and the $N=\infty$ agreement of global and subregion HKLL formulae is a free-theory statement. What remains is entanglement wedge reconstruction without holographic quantum error correction, or subregion complementarity: each boundary region has its own code-preserving low-energy algebra and its own region-adapted bulk interpretation, rather than a shared logical operator.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2305.02439v2
- Title: Machine learning of measurement schemes for efficient quantum observable estimation
- Authors: Zi-Jian Zhang, Kouhei Nakaji, Matthew Choi, Alán Aspuru-Guzik
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2305.02439v2  pdf=https://arxiv.org/pdf/2305.02439v2.pdf

Abstract:
Estimation of the expectation value of observables is a key subroutine in quantum computing and is also the bottleneck of the performance of many near-term quantum algorithms. Many methods have been proposed to reduce the number of measurements needed for this task by designing measurement schemes that decide the measurements to perform; however, these schemes are usually constructed from hand-crafted heuristics, which limits the measurement efficiency they can achieve. In this paper, we propose a framework for learning measurement schemes directly from the observable, using machine learning techniques including stochastic gradient descent and a two time-scale update rule. As a concrete realization of this framework, we introduce Composite-Locally Biased Classical Shadow (C-LBCS), which learns a mixture of locally-biased classical shadows and their mixing weights end-to-end. We numerically demonstrate C-LBCS on molecular systems up to $\mathrm{CO}_2$ (30 qubits) and show that C-LBCS outperforms the previous state-of-the-art methods despite its simplicity. We believe our approach opens up a reliable and scalable path toward efficient observable estimation on large quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2412.19918v5
- Title: Revisiting the Bohr Model of the Atom through Brownian Motion of the Electron
- Authors: Vasil Yordanov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2412.19918v5  pdf=https://arxiv.org/pdf/2412.19918v5.pdf

Abstract:
We revisit the Bohr model through Brownian motion of the electron and the principles of stochastic optimal control. The electron is assumed to have a definite but random position, represented by a single real-valued stochastic process in physical space whose probability density obeys the Fokker-Planck equation. Because Brownian paths are not differentiable, the process carries two mean drifts, one for each direction of time. We treat the forward drift as the control field, while the backward drift is fixed by the density of the same process. The running cost combines the two drifts into a time-symmetric kinetic term, and through the backward drift it inherits a dependence on the density, so the value becomes a functional on density space. Bellman's dynamic-programming principle requires the control to minimize the expected action from every intermediate time and density onward. The drift therefore emerges as a feedback law on position and density, rather than from the global stationarity of a stochastic action. The resulting law-dependent HJB-Fokker-Planck system reduces to the Schrödinger equation. For stationary hydrogen states the theory yields explicit drift fields in spherical coordinates and reproduces the standard radial and angular kinetic-energy averages of the quantum operator formalism. Direct trajectory-level simulations show the coordinate distributions converging to the Born marginals and the time-averaged energies reproducing the quantum expectation values. For the 2p eigenstates with magnetic quantum number $m=\pm1$, a phase-driven azimuthal drift makes the simulated trajectories circulate at the analytically predicted rate, and the angular momentum accumulated from the raw trajectory increments converges to exactly $L_z=m\hbar$. The angular-momentum quantization postulated in the Bohr model thus reappears as a property of the simulated stochastic motion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2503.13775v3
- Title: Quantum dots for quantum repeaters
- Authors: Joanna M Zajac, Reza Hekmati, Tobias Huber-Loyola, Sven Höfling
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.13775v3  pdf=https://arxiv.org/pdf/2503.13775v3.pdf

Abstract:
This review surveys recent progress in III--V semiconductor quantum dots (QDs) as a platform for quantum repeaters. We start by discussing the state of the art in QD-based non-classical light sources. Specifically, we report on on single-photon and entangled-pair sources operating across near-infrared and telecom wavelengths, with emphasis on the key metrics-multi-photon suppression g2(0), photon indistinguishability, extraction efficiency, and spin coherence time-while discussing frequency conversion, excitation schemes, cavity engineering, remote indistinguishability, and spin coherence.   We then examine the two principal repeater architectures. For all-photonic repeaters we review linear cluster- and graph-state generation using QD spins, recent experimental milestones, and the critical role of spin dephasing time. For memory-based repeaters we focus on heterogeneous implementations combining deterministic QD photon sources with room-temperature alkali-vapor memories, providing rate benchmarking against other platforms, discussion of storage protocols, wavelength compatibility, and early demonstrations. Enabling technologies such as cryogenic cooling, on-chip photonic integration, network synchronization and multiplexing are also presented.   The review highlights the strength of QD-based architectures and identifies the remaining milestones required for their deployment in practical fiber-based quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2506.18061v2
- Title: Planar fault-tolerant logical measurements with low qubit overhead
- Authors: Yingli Yang, Guo Zhang, Ying Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.18061v2  pdf=https://arxiv.org/pdf/2506.18061v2.pdf

Abstract:
Fault-tolerant quantum computation critically depends on architectures uniting high encoding rates with physical implementability. Quantum low-density parity-check (qLDPC) codes, including bivariate bicycle (BB) codes, achieve dramatic reductions in qubit overhead, yet their logical operations remain a key challenge under planar hardware constraints. Here, we introduce code craft, a framework for designing fault-tolerant logical operations on planar BB codes within a translationally invariant, two-dimensional qubit lattice. By systematically deforming codes through local modifications-stretching, cutting, and painting-we enable the manipulation of logical qubits using strictly planar operations. We establish fault tolerance through numerical optimization of code distances and show that logical operations, including controlled-NOT gates, state transfers, and Pauli measurements, can be efficiently implemented within this framework to assemble an individually addressable logical qubit network. Universal quantum computation can then be realized by coupling just one BB-code logical qubit to a surface-code block. By combining the high encoding efficiency of qLDPC codes with geometric locality, our approach offers a practical and resource-efficient path to fault-tolerant quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2506.22346v3
- Title: Making Non-Markovian master equations accessible with approximate environments
- Authors: Gerardo Suárez, Michał Horodecki
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.22346v3  pdf=https://arxiv.org/pdf/2506.22346v3.pdf

Abstract:
Accurate and efficient simulation of open quantum systems remains a significant challenge, particularly for Non-Markovian dynamics. We demonstrate the profound utility of expressing the environmental correlation function as a sum of damped sinusoidals within master equations. While not strictly required, this decomposition offers substantial benefits, crucially reducing the cost of Lamb-shift and decay rates calculations without sacrificing accuracy. Furthermore, this approach enables straightforward calculation of Lamb-shift corrections, bypassing the need for complex principal value integration. We show that these Lamb-shift effects are demonstrably non-negligible in heat transport scenarios, and are needed for an accurate description. Unlike in the Gorini-Kossakowski-Lindblad-Sudarshan(GKLS) master equation, the non-commuting nature of the Lamb-shift with the Hamiltonian in non-Markovian descriptions, coupled with GKLS's inaccuracies at early times, brings the necessity of Non-Markovian descriptions for finite-time thermodynamics. In the weak coupling regime, our Master Equation formulations with exponential decomposition achieve accuracy comparable to numerically exact methods. This methodology significantly simplifies and accelerates the simulation of non-Markovian dynamics in open quantum systems, offering a more reliable and computationally tractable alternative akin to a Global Master Equation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2507.04500v3
- Title: Fast quantum measurement tomography with optimal error bounds
- Authors: Leonardo Zambrano, Sergi Ramos-Calderer, Richard Kueng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.04500v3  pdf=https://arxiv.org/pdf/2507.04500v3.pdf

Abstract:
We present a two-step protocol for quantum measurement tomography that is light on classical co-processing cost and still achieves optimal sample complexity. Given measurement data from a known probe state ensemble, we first apply least-squares estimation to produce an unconstrained approximation of the POVM, and then project this estimate onto the set of valid quantum measurements. For a POVM with $L$ outcomes acting on a $d$-dimensional system, we show that the protocol requires $\mathcal{O}\left((d^3+d^2L)/ε^2\right)$ samples to achieve error $ε$ in worst-case distance, and $\mathcal{O}(d^2 L/ε^2)$ samples in average-case distance. We further establish two matching sample complexity lower bounds of $Ω((d^3 + d^2 L) /ε^2)$ and $Ω(d^2 L/ε^2)$ for any non-adaptive, single-copy POVM tomography protocol. Hence, our projected least squares POVM tomography is sample-optimal in both the dimension and the number of outcomes for both distances. Our method admits an analytic form when using global or local 2-designs as probe ensembles and enables rigorous non-asymptotic error guarantees. Finally, we also complement our findings with empirical performance studies carried out on a noisy superconducting quantum computer with flux-tunable transmon qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2507.06954v2
- Title: Towards relativistic generalization of collapse models
- Authors: Anirudh Gundhi, Lajos Diósi, Matteo Carlesso
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.06954v2  pdf=https://arxiv.org/pdf/2507.06954v2.pdf

Abstract:
Spontaneous collapse models provide a possible, testable solution to the quantum measurement problem. While experiments are providing increasingly stronger bounds on their parameters, a full-fledged relativistic extension is still missing. Previous attempts have encountered different obstacles, such as violation of microcausality, infinite energy rate, and particle production from vacuum. Here, we propose a generalization of the collapse master equation that is characterized by a local field collapse operator and a non-Markovian noise with a Lorentz invariant correlation. Our construction is able to overcome previously encountered problems and has the desirable properties in the non relativistic limit. A specific choice of the noise correlation function is also introduced and discussed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2509.17876v2
- Title: Quantum Portfolio Optimization: An Extensive Benchmark
- Authors: Eric Stopfer, Friedrich Wagner
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2509.17876v2  pdf=https://arxiv.org/pdf/2509.17876v2.pdf

Abstract:
Recently, several researchers proposed portfolio optimization as a potential use case for quantum optimization. However, the literature is lacking an extensive benchmark quantifying the potential of quantum computers for portfolio optimization. In this work, we contribute to closing this gap. We provide a computational study, comparing quantum approaches against state-of-the-art classical methods on a meaningful, real-world instance set. In particular, we compare quantum annealing and the quantum approximate optimization algorithm against classical mixed-integer programming, simulated annealing, steepest descent local search, tabu search and a problem-tailored heuristic. We consider a volatility-minimizing variant of portfolio optimization which we show to be more difficult to solve for classical optimizers than return-maximizing or multi-objective formulations. Our benchmark data set comprises 250 instances with up to 1,000 assets from actual stock data. Due to hardware limitation, quantum methods could only be tested for instances with at most 30 assets. The results show that all instances can be solved to proven optimality by mixed-integer programming in the order of seconds. Moreover, the problem-tailored heuristic consistently outperforms quantum approaches in terms of solution quality for fixed runtime. Thus, we conclude that there is only very limited room for a potential quantum advantage for the considered variant of portfolio optimization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2510.17974v2
- Title: Experimental preparation of $W$ states through frustration on a programmable quantum simulator
- Authors: Alberto Giuseppe Catalano, Ceren Dağ, Gianpaolo Torre, Salvatore Marco Giampaolo, Fabio Franchini
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2510.17974v2  pdf=https://arxiv.org/pdf/2510.17974v2.pdf

Abstract:
$W$ states are a central class of multipartite entangled states with applications in quantum information processing, yet their scalable and deterministic preparation remains challenging. Here we propose a protocol based on {\it topological ring frustration}, where an antiferromagnetic ring with an odd number of sites hosts a delocalized excitation corresponding to a $W$ state. We implement this protocol on a Rydberg atom array -- a programmable quantum simulator -- generating $W$ states of up to 11 atoms. Our results demonstrate a fidelity of $\mathcal{F} \approx 0.77$, and numerical simulations indicate scalability to larger system sizes accessible with near-term hardware improvements. To enable certification of these many-body entangled states, we introduce a novel and efficient Bayesian tomography method that, leveraging on classical simulations, enables their certification with a cost that avoids the exponential scaling of full tomography. These results establish topological frustration as a practical mechanism for engineering multipartite entanglement and provide a scalable route toward the certification of correlated quantum many-body states in quantum simulators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2511.12138v2
- Title: Application of optical squeezing to microresonator based optical sensors
- Authors: Dariya Salykina, Daniil Shakhbaziants, Igor Bilenko, Farid Khalili
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.12138v2  pdf=https://arxiv.org/pdf/2511.12138v2.pdf

Abstract:
High-Q optical microresonators combine low losses and high optical energy concentration in a small effective mode volume, making them an attractive platform for optical sensors. While light is confined in the microresonator by total internal reflection, a portion of the optical field, known as the evanescent field, extends outside. This makes the mode's resonant frequency sensitive to changes in the surrounding environment.   In this work, we explore the quantum sensitivity limits of this type of sensors. We show that using the intracavity squeezing of the light in the microresonator, it is possible to suppress the influence of the optical losses and cancel the undesirable self phase modulation effect, originating from the cubic non-linearity of the microresonators media. As a result, the sensitivity surpassing the shot noise limit can be achieved. An additional sensitivity gain can be obtained by preparing the input light in a squeezed quantum state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2511.20569v2
- Title: Reservoir-Engineered Low-Threshold Quantum Energy Storage
- Authors: Borhan Ahmadi, André H. A. Malavazi, Paweł Mazurek, Paweł Horodecki, Shabir Barzanjeh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.20569v2  pdf=https://arxiv.org/pdf/2511.20569v2.pdf

Abstract:
Fast charging of quantum batteries requires amplification of the energy transferred to a storage mode without uncontrolled gain or phenomenological non-Hermitian dynamics. Inspired by broken/unbroken dynamical regimes, we introduce a reservoir-engineered quantum battery in which a two-photon-driven charger and a battery mode are coupled through a lossy dissipative mediator. Eliminating the fast mediator yields a reduced two-mode Lindblad model with a complex dissipative coupling and renormalized damping rates. Its drift matrix has a pump-induced stability threshold: below threshold the seeded response is bounded, whereas above threshold a weak seed excites a growing mode and the battery occupation increases exponentially. Compared with a coherent beam-splitter charger--battery benchmark at equal effective coupling, the dissipative architecture reaches this broken regime at a lower pump amplitude. For the parameters studied here, this corresponds to about \(61\%\) less critical pump power and opens a pump-power window in which dissipative charging is exponential while the coherent benchmark remains below threshold. In the broken dissipative regime, the growth is dominated by a seed-selected coherent battery displacement rather than incoherent fluctuation buildup, so a large fraction of the stored energy is directly extractable by a displacement operation. The broken-regime boundary is a dynamical stability threshold, not generally an exceptional point, and the full three-mode Lindblad model confirms the reduced description in the fast-mediator regime. Our results give a completely positive route to pump-efficient, low-threshold, and coherently addressable quantum energy storage using engineered reservoirs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2512.20613v2
- Title: Variational matrix product states for combinatorial optimization
- Authors: Guillermo Preisser, Conor Mc Keever, Michael Lubasch
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2512.20613v2  pdf=https://arxiv.org/pdf/2512.20613v2.pdf

Abstract:
To compute approximate solutions for combinatorial optimization problems, we describe variational methods based on the product state (PS) and matrix product state (MPS) ansätze. We perform variational energy minimization with respect to a quantum annealing Hamiltonian and utilize randomness by embedding the approaches in the metaheuristic iterated local search (ILS). The resulting quantum-inspired ILS algorithms are benchmarked on maximum cut problems of up to 50000 variables. We show that they can outperform traditional (M)PS methods, classical ILS, the quantum approximate optimization algorithm and other variational quantum-inspired solvers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2601.02471v2
- Title: Gaussian time-translation covariant operations: structure, implementation, and thermodynamics
- Authors: Xueyuan Hu, Lea Lautenbacher, Giovanni Spaventa, Martin B. Plenio, Nelly H. Y. Ng, Jeongrak Son
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.02471v2  pdf=https://arxiv.org/pdf/2601.02471v2.pdf

Abstract:
Time-translation symmetry strongly constrains physical dynamics, yet systematic characterization for continuous-variable systems lags behind its discrete-variable counterpart. We close this gap by providing a rigorous classification of Gaussian quantum operations that are covariant under time translations, termed Gaussian covariant operations. We show that several key results known for discrete-variable covariant operations break down in the Gaussian optical setting: discrepancies arise in physical and thermodynamic implementation, in the extensivity of asymmetry, and in catalytic advantages. Our results provide comprehensive mathematical and operational toolkits for Gaussian covariant operations, including a peculiar pair of asymmetry measures that are completely non-extensive. Our findings also reveal surprising consequences of the interplay among symmetry, Gaussianity, and thermodynamic constraints, suggesting that real-world scenarios with multiple constraints have a rich structure not accessible from examining individual constraints separately.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2603.27063v2
- Title: Pattern Formation in Quantum Hierarchical Cellular Neural Networks
- Authors: W. A. Zúñiga-Galindo, B. A. Zambrano-Luna, Chayapuntika Indoung
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.27063v2  pdf=https://arxiv.org/pdf/2603.27063v2.pdf

Abstract:
We present a new class of quantum neural networks (QNNs) whose states are solutions of $p$-adic Schrödinger equations with a non-local potential that controls the interaction between the neurons. These equations are obtained as Wick rotations of the state equations of $p$-adic cellular neural networks (CNNs). The CNNs are continuous limits of discrete hierarchical neural networks (NNs). The CNNs are bio-inspired by the Wilson-Cowan model, which describes the macroscopic dynamics of large populations of neurons. We provide a detailed study of the discretization of the new $p$-adic Schrödinger equations, which allows the construction of new QNNs on simple graphs. We also conduct detailed numerical simulations, offering a clear insight into the functioning of the new QNNs. At a mathematical level, we show the existence of local solutions for the new $p$ -adic Schrödinger equations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2604.02420v2
- Title: Bounding the entanglement of a state from its spectrum
- Authors: Jofre Abellanet-Vidal, Guillem Müller-Rigat, Albert Rico, Anna Sanpera
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02420v2  pdf=https://arxiv.org/pdf/2604.02420v2.pdf

Abstract:
We introduce a framework to upper bound the entanglement content of a bipartite quantum state from its spectrum alone. Using linear maps and their inverses, we derive rigorous constraints on the maximal entanglement that can be activated under global unitary transformations. We use as entanglement quantifiers the negativity and the Schmidt number; however, our framework is general and applies to any other entanglement measure. Our approach yields compact analytical sufficient criteria for bounding the entanglement of full-rank states in arbitrary dimensions and reveals new spectral constraints on Schmidt number witnesses.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2604.08763v2
- Title: Weak Adversarial Neural Pushforward Method for the Wigner Transport Equation
- Authors: Andrew Qing He, Wei Cai, Sihong Shao
- Categories: quant-ph (primary); quant-ph; cs.LG; math.NA
- Links: abs=https://arxiv.org/abs/2604.08763v2  pdf=https://arxiv.org/pdf/2604.08763v2.pdf

Abstract:
We extend the Weak Adversarial Neural Pushforward Method to the Wigner transport equation governing the phase-space dynamics of quantum systems. The central contribution is a structural observation: integrating the nonlocal pseudo-differential potential operator against plane-wave test functions produces a Dirac delta that exactly inverts the Fourier transform defining the Wigner potential kernel, reducing the operator to a pointwise finite difference of the potential at two shifted arguments. This holds in arbitrary dimension, requires no truncation of the Moyal series, and treats the potential as a black-box function oracle with no derivative information. To handle the negativity of the Wigner quasi-probability distribution, we introduce a signed pushforward architecture that decomposes the solution into two non-negative phase-space distributions mixed with a learnable weight. The resulting method inherits the mesh-free, Jacobian-free, and scalable properties of the original framework while extending it to the quantum setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2604.17369v2
- Title: Quantum channel tomography: optimal bounds and a Heisenberg-to-classical phase transition
- Authors: Kean Chen, Filippo Girardi, Aadil Oufkir, Nengkun Yu, Zhicheng Zhang
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2604.17369v2  pdf=https://arxiv.org/pdf/2604.17369v2.pdf

Abstract:
How many black-box queries to a quantum channel are needed to learn its full classical description? This question lies at the heart of quantum channel tomography (also known as quantum process tomography), a fundamental task in the characterization and validation of quantum hardware. Despite extensive prior work, the optimal query complexity for quantum channel tomography is far from fully understood.   In this paper, we study tomography of an unknown quantum channel with input dimension $d_1$, output dimension $d_2$, and Kraus rank at most $r$, to within error $\varepsilon$. We identify the dilation rate $τ= r d_2 / d_1$ (which always satisfies $τ\geq 1$ due to the trace preservation of quantum channels) as a key parameter, and establish that the optimal query complexity of channel tomography exhibits distinct scaling laws across three regimes of $τ$.   - In the boundary regime ($τ= 1$): we show that the query complexity is $Θ(r d_1 d_2/\varepsilon)$ for Choi trace norm error $\varepsilon$, and is upper bounded by $O(\min\{r d_1^{1.5} d_2/\varepsilon, r d_1 d_2/\varepsilon^2\})$ and lower bounded by $Ω(r d_1 d_2/\varepsilon)$ for diamond norm error $\varepsilon$.   - In the away-from-boundary regime ($τ\geq 1+Ω(1)$): we show that the query complexity is $Θ(r d_1 d_2/\varepsilon^2)$ for both Choi trace norm and diamond norm errors $\varepsilon$.   Our results uncover a sharp Heisenberg-to-classical phase transition in the query complexity of quantum channel tomography: at $τ=1$, the optimal query complexity exhibits Heisenberg scaling $1/\varepsilon$, whereas for $τ\geq 1+Ω(1)$, it exhibits classical scaling $1/\varepsilon^2$. In addition, we show that in the near-boundary regime ($1< τ< 1+o(1)$), the query complexity exhibits a mixture of Heisenberg and classical scaling behaviors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2606.29235v2
- Title: Imaginary pseudo entropy encodes temporal orientation
- Authors: Tatsuhiro Misumi
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2606.29235v2  pdf=https://arxiv.org/pdf/2606.29235v2.pdf

Abstract:
Pseudo entropy between quantum states at different times is generally complex, yet its imaginary part has lacked a bounded operational meaning. We show that a calibrated replica interferometer converts the pseudo-Rényi phase into a directly measurable record of transition orientation. Together with replica visibility, it exactly determines the trace distance between forward and backward ancilla outputs and hence the Helstrom-optimal single-shot success probability. At short times, the symmetrized covariance of the modular and physical Hamiltonians sets the initial distinguishability response. Under any common quantum channel, the corresponding orientation information can only decrease, with equality characterized by Petz recovery. Imaginary pseudo entropy therefore records a reversible distinction between temporal orientations, while coarse graining can make the loss of that record irreversible.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2504.15264v2
- Title: Sunflowers and Ramsey problems for restricted intersections
- Authors: Barnabás Janzer, Zhihan Jin, Benny Sudakov, Kewen Wu
- Categories: math.CO (primary); math.CO; cs.DM; quant-ph
- Links: abs=https://arxiv.org/abs/2504.15264v2  pdf=https://arxiv.org/pdf/2504.15264v2.pdf

Abstract:
Extremal problems on set systems with restricted intersections have been an important part of combinatorics in the last 70 years. In this paper, we study the following Ramsey version of these problems. Given a set $L\subseteq \{0,\dots,k-1\}$ and a family $\mathcal{F}$ of $k$-element sets which does not contain a sunflower with $m$ petals whose kernel size is in $L$, how large a subfamily of $\mathcal{F}$ can we find in which no pair has intersection size in $L$? We give matching upper and lower bounds, determining the dependence on $m$ for all $k$ and $L$. This problem also finds applications in quantum computing.   As an application of our techniques, we also obtain a variant of Füredi's celebrated semilattice lemma, which is a key tool in the powerful delta-system method. We prove that one cannot remove the double-exponential dependency on the uniformity in Füredi's result, however, we provide an alternative with significantly better, single-exponential dependency on the parameters, which is still strong enough for most applications of the delta-system method.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2508.02819v3
- Title: Signatures of quantum chaos and complexity in the Ising model on random graphs
- Authors: GJ Sreejith, Sandipan Manna
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2508.02819v3  pdf=https://arxiv.org/pdf/2508.02819v3.pdf

Abstract:
We investigate signatures of quantum chaos in the mixed-field quantum Ising model on finite-size Erdős-Rényi graphs using probes scalable on near-term quantum devices. Upon tuning the graph connectivity, the system exhibits a crossover from a localized regime at low connectivity, through a chaotic regime at intermediate connectivity, to a permutation-symmetric integrable limit near all-to-all connectivity. This crossover has possible implications for the performance and trainability of variational algorithms such as QAOA. We characterize this crossover in finite-size systems using complementary probes. First, deep thermalization of a projected ensemble starting from a product state reveals slow (fast) convergence to the Haar ensemble at extremal (intermediate) connectivities. Second, we analyze eigenstate and eigenvalue correlations using the partial spectral form factor, an experimentally scalable proxy for the spectral form factor with reduced resource overhead, and observe characteristic chaos signatures at intermediate connectivities and distinct deviations at extremal connectivities. Finally, we explore the Krylov complexity of operators, a locality-independent diagnostic that, although not directly experimentally accessible, serves as a tool for quantifying scrambling. We show that it is maximized deep in the chaotic regime, corroborating the signatures observed through the experimentally scalable probes. Our results provide finite-size benchmarks demonstrating robust signatures of chaos in scalable probes and suggest that these diagnostics can be implemented in current quantum platforms to access regimes beyond classical simulation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2601.02199v2
- Title: Topological States Enabled by Non-local Nonlinearity in Synthetic Dimensions
- Authors: Chong-Xiao Chen, Zheng-Wei Zhou, Han Pu, Xi-Wang Luo
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2601.02199v2  pdf=https://arxiv.org/pdf/2601.02199v2.pdf

Abstract:
The interplay between topology and nonlinearity represents a central challenge in modern physics. Here, we investigate this interplay by considering a synthetic Su-Schrieffer-Heeger lattice with all-to-all nonlocal interactions. We find that the distinctive nonlinearity maintains an effective chiral symmetry and leads to a quantized nonlinear winding and Berry phase, as corroborated by the developed Bogoliubov nonlinear adiabatic theory. Increasing nonlinearity drives a sequence of topological transitions signaled by the appearance of characteristic swallowtail band structures at intermediate interaction strengths and band swapping in the strong nonlinear regime. The band swapping results in quantized fractional windings and double-period Bloch oscillations that are closely related to discrete time crystals. Remarkably, even starting from a topologically trivial linear system, nonlocal nonlinearity can induce an emergent topological phase with fractional windings. Experimentally, our model can be realized using photons in a degenerate optical cavity with Rydberg-mediated interactions. Our results establish a rigorous framework and pave the way for exploring nonlinear topological phenomena and their applications in synthetic quantum platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2604.17700v2
- Title: Dynamical spin-nematic correlation in a transverse field Ising chain with non-Hermitian Gamma interaction
- Authors: Yu-Hong Yan, Ran Wang, Kun-Liang Zhang
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2604.17700v2  pdf=https://arxiv.org/pdf/2604.17700v2.pdf

Abstract:
We investigate the effect of non-Hermitian Gamma interaction on the phase transitions and magnetic correlations for the transverse field Ising chain. We demonstrate that apart from the gapped antiferromagnetic and paramagnetic phases, there is a gapless phase induced by parity-time symmetry breaking, where the system exhibits long-range and short-range spin-nematic correlations in different regions divided by the quantum critical line determined from the correlation function and the subsystem entanglement entropy. Furthermore, we reveal that the parity-time symmetry breaking leads to the emergence of dynamical spin-nematic correlation, which also suggests a way of characterizing the spin-nematic phase diagram through non-equilibrium dynamics. Our findings show rich quantum phases stem from the competition among the Ising interaction, transverse field and non-Hermitian Gamma interaction, as well as providing a scheme for generating spin-nematic correlation in the spin chain.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2605.03910v2
- Title: Inverse-designed release-free optomechanical crystal with high photon-phonon coupling
- Authors: David Hambraeus, Paul Burger, Johan Kolvik, Philippe Tassin, Raphaël Van Laer
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2605.03910v2  pdf=https://arxiv.org/pdf/2605.03910v2.pdf

Abstract:
Interactions between light and mechanics provide a powerful interface between optical and microwave-frequency signals, with applications spanning classical signal processing and quantum technologies. High-performance optomechanical devices require both strong photon-phonon coupling and tolerance to parasitic laser heating. Release-free optomechanical crystals provide improved thermal anchoring compared to suspended nanobeams, but have so far exhibited weaker vacuum optomechanical coupling rates, leaving a trade-off between coupling strength and thermal robustness. Here, we largely close this gap: we design and experimentally demonstrate a release-free silicon optomechanical crystal with a record vacuum optomechanical coupling rate of about $g_\text{OM} / (2 π) = 800$ kHz, comparable to suspended state-of-the-art devices. The resulting optomechanical scattering rate $Γ_\text{OM}/(2 π)= 1.1$ kHz is nearly twice that of previous release-free implementations. This performance is achieved by combining physics-guided human intuition with a multiphysics inverse-design algorithm introduced here for resonant optomechanical structures. Beyond the specific device demonstrated, the inverse-design framework is applicable to co-optimizing optical and mechanical resonances and eigenmodes more broadly. These results strengthen release-free optomechanical crystals as a platform for fast, low-noise classical and quantum optomechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2606.31117v2
- Title: Radical-Fragment Many-Body Expansion for Linear Alkane Quantum Chemistry
- Authors: Daniel Sierra-Sosa, Jorge Saavedra, Santiago Solares, Gregorio Toscano-Pulido
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.31117v2  pdf=https://arxiv.org/pdf/2606.31117v2.pdf

Abstract:
We introduce a radical-fragment many-body expansion at the two-body level (MBE2) for quantum chemistry of linear alkanes. Instead of heterolytic bond cleavage with hydrogen capping atoms and electrostatic embedding like in Fragment Molecular Orbital (FMO), we perform homolytic C-C bond cleavage to produce open-shell radical fragments (CH3, CH2) treated with restricted open-shell Hartree-Fock (ROHF) in isolation. The two-body MBE2 assembly formula reconstructs total alkane energies from only four unique fragment calculations regardless of chain length, reducing the maximum qubit requirement. We benchmark this framework against five energy solvers (RHF, CCSD, VQE, ADAPT-VQE, and SQD) across 11 linear alkanes from butane (C4H10) to hexacosane (C26H54). The MBE2 decomposition achieves a 12.3x qubit reduction for C26H54 (from 368 to 30 qubits) and a 12.8x reduction in unique calculations via symmetry exploitation. MBE2-VQE and MBE2-SQD (executed on IBM quantum hardware) closely track their respective classical MBE2 references, demonstrating that fragmentation-based quantum chemistry is viable for scaling quantum solvers to large molecular systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-07-10 13:30
- arXiv: 2607.06219v2
- Title: Classical Reversible Computation by Quantum Coherence
- Authors: Daniel Loss
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2607.06219v2  pdf=https://arxiv.org/pdf/2607.06219v2.pdf

Abstract:
Rising energy demand from data-centre and AI applications has renewed interest in reversible computation, where logic need not dissipate heat at every step if information is uncomputed. Implementations have so far been classical: adiabatic CMOS reduces dissipation by slowing charge motion but is still limited by the threshold physics of transistors. Here we propose classical reversible logic implemented by coherent spin dynamics in a spin quantum-dot array, with inputs and outputs in classical basis states and no algorithmic use of superposition. The same spin stores, transports, and computes, with unitary rotation replacing irreversible switching. The universal building block is an iToffoli gate driven by DC voltage pulses and anisotropic exchange in Ge/Si hole spins. Simulations with experimental parameters reproduce the Toffoli truth table and yield a testable error landscape. Because shuttling transports the bit without measurement, logic and data movement remain reversible until readout. Millivolt pulses on femtofarad gates yield a gate energy below the 4~K Landauer scale, about five (eight) orders of magnitude below a room-temperature CMOS Toffoli with (without) 4 K cooling overhead. The same semiconductor hardware is therefore dual-use, supporting quantum algorithms when superposition is used and classical reversible logic otherwise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

