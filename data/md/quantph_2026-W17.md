- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15381v1
- Title: Hydration Monitoring Using Urinary Biomarkers: A Hybrid Classical Quantum Predictive Modeling Framework
- Authors: Saul Gonzalez-Bermejo, Tommaso Albrigi, Borja Vazquez-Morado, Urko Regueiro-Ramos, Daniel Casado-Fauli, Sergi Consul-Pacareu, Laia Alentorn, Jordi Ferre, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15381v1  pdf=https://arxiv.org/pdf/2604.15381v1.pdf

Abstract:
Hydration status is a key physiological indicator associated with cellular homeostasis, renal function, and overall health. Recent advances in smart sensing environments enable passive monitoring of urinary biomarkers that can provide continuous insight into hydration dynamics. In this work, we investigate predictive modeling approaches for hydration monitoring using biomarker data collected through the Predict Health Toilet (PHT) system. The problem is formulated as a regression task using urinary indicators such as urine specific gravity, conductivity, and volume. We evaluate classical machine learning models and quantum machine learning architectures based on variational quantum circuits. In particular, we introduce a modular Quantum Sequential Model (QSM) designed to construct flexible hybrid quantum classical predictive pipelines. Experimental results compare classical regression models, symmetry-constrained quantum regressors, and QSM architectures. The results provide insights into the potential role of quantum machine learning in digital health monitoring systems and highlight the opportunities and current limitations of near-term quantum computing for physiological data analysis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15382v1
- Title: Classical and Quantum Machine Learning for Population-Level Prediction of Heat-Related Physiological Events
- Authors: Saul Gonzalez-Bermejo, Tommaso Albrigi, Borja Vazquez-Morado, Urko Regueiro-Ramos, Daniel Casado-Faulı, Sergi Consul-Pacareu, Parfait Atchade-Adelomou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15382v1  pdf=https://arxiv.org/pdf/2604.15382v1.pdf

Abstract:
Predicting heat-related physiological events at the population level is challenging due to the complex interactions among climatic, demographic, and socioeconomic factors, as well as the strong sparsity and seasonality of observational data. In this work, we propose a unified predictive framework that integrates heterogeneous environmental and public-health datasets and evaluates two learning paradigms within a common pipeline: classical machine learning and quantum machine learning. The methodology combines data harmonization, temporal aggregation, feature engineering, and dimensionality reduction to construct a weekly county-level population dataset. On this unified representation, we train both a classical regression baseline and a variational quantum model based on parameterized quantum circuits with angle embedding and data re-uploading. Experimental evaluation on datasets from the United States and Catalonia shows that classical models currently achieve higher predictive accuracy, particularly under conditions of strong class imbalance and sparse targets. Nevertheless, the quantum models demonstrate non-trivial learning capability and capture meaningful predictive structure in several scenarios. These results provide an empirical comparison between classical and quantum learning approaches for population-level physiological prediction and establish a methodological foundation for future hybrid health modeling as quantum hardware continues to evolve.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15389v1
- Title: A Unified Hardware-to-Decoder Architecture for Hybrid Continuous-Variable and Discrete-Variable Quantum Error Correction in LiDMaS+
- Authors: Dennis Delali Kwesi Wayo, Chinonso Onah, Leonardo Goliatt, Sven Groppe
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15389v1  pdf=https://arxiv.org/pdf/2604.15389v1.pdf

Abstract:
We present an architecture-level hardware-to-logical-to-decoder execution stack for hybrid continuous-variable and discrete-variable quantum error correction in LiDMaS+. Provider-native records are normalized into a single decoder IO contract and replayed under fixed controls across MWPM, UF, BP, and neural-MWPM. In a Xanadu case study using fixture inputs and sampled public datasets, replay integrity was complete: 108/108 fixture and 4000/4000 real-slice request-response lines, with zero request-parse errors, zero response-parse errors, and zero decoder-name mismatches. Under matched inputs, decoder behavior is clearly regime-dependent. For weighted fixture summaries, average flip count was 1.296 (MWPM), 1.296 (UF), 0.667 (BP), and 1.296 (neural-MWPM). For weighted real-data summaries, average flip count was 0.641 (MWPM), 0.741 (UF), 0.318 (BP), and 0.641 (neural-MWPM); corresponding nonempty-flip rates were 0.490, 0.490, 0.318, and 0.490. Across fixture data, BP reduced weighted correction volume by 48.6\% versus MWPM; across real slices, BP reduced weighted correction volume by 50.4\% versus MWPM and 57.1\% versus UF. Quality controls show the central interpretability tradeoff: BP is intervention-conservative but leaves higher residual burden, while MWPM-family decoders intervene more aggressively and clear more syndrome. Warning-no-syndrome rates remained decoder-invariant and dataset-driven (fixture weighted 0.259; real weighted 0.510), confirming preserved sparsity semantics from hardware input to logical correction. Re-running analysis stages reproduced identical SHA-256 artifacts, enabling deterministic study iteration. These results establish a practical benchmarking foundation for photonic GKP-oriented hardware programs where decoder policy must be selected as a function of operating regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15393v1
- Title: Projected Dynamic Programming for Sequential Quantum State Discrimination
- Authors: Jaehun Jeong, Donghwa Ji, Hyunjun Jang, Kabgyun Jeong
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15393v1  pdf=https://arxiv.org/pdf/2604.15393v1.pdf

Abstract:
Sequential Quantum State Discrimination (SQSD) can be naturally framed as a sequential decision-making problem: at each time step, an agent must decide whether to perform an additional measurement to gather more information or to conclude with an optimal decision based on the current belief. In this paper, we formally cast SQSD into a static-hidden-state Partially Observable Markov Decision Process (POMDP) framework. We demonstrate that this formulation precisely subsumes the conventional minimum-error discrimination (MED) scheme as a special one-step case. Furthermore, we apply a regular grid-based discretization to the continuous belief simplex and approximate the possibly continuous measurement space using a finite library. Then we provide rigorous mathematical bounds on the resulting errors and analyze the computational complexity for both offline planning and online execution. Our analysis confirms that the inherent trade-off between accuracy and complexity, as well as the curse of dimensionality regarding the number of hypotheses, are also prominently observed in the quantum regime. Finally, we provide a working example of binary state discrimination to derive explicit forms of various functions and present numerical simulations for trine state discrimination to visualize the sequential structure of our POMDP-based SQSD.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15405v1
- Title: Optimal algorithms for materializing stabilizer states and Clifford gates from compact descriptions
- Authors: Hyunho Cha, Jungwoo Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15405v1  pdf=https://arxiv.org/pdf/2604.15405v1.pdf

Abstract:
Stabilizer states admit compact classical descriptions, but many downstream tasks still require their full amplitude vectors. Since the output itself has size $2^n$, the main algorithmic question is whether one can materialize an $n$-qubit stabilizer state vector in optimal $O(2^n)$ time, rather than paying an additional polynomial overhead. We answer this question in the affirmative. Starting from the standard quadratic-form representation of stabilizer states, we give an algorithm that runs in $O(2^n)$ time and $O(2^n)$ space. The idea is to maintain a cached parity word that records all future off-diagonal quadratic phase increments simultaneously. As consequences, we obtain an optimal procedure for materializing a stabilizer state vector from a standard check-matrix description, and an optimal algorithm for expanding a Clifford tableau into its full dense matrix. These results close the asymptotic gap for dense stabilizer and Clifford materialization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15412v1
- Title: Renormalization and Non-perturbative Dynamics in Conformal Quantum Mechanics
- Authors: Jacob Hafjall, Thomas A. Ryttov
- Categories: quant-ph (primary); quant-ph; hep-ph; hep-th
- Links: abs=https://arxiv.org/abs/2604.15412v1  pdf=https://arxiv.org/pdf/2604.15412v1.pdf

Abstract:
We study conformal quantum mechanics by first considering the perturbative $S$-matrix in various dimensions. The model has two couplings and we study perturbatively the degree of ultraviolet divergences arising in the interplay between the two couplings. We then focus on the inverse square potential in one spatial dimension and compute the beta function to arbitrarily perturbative and non-perturbative orders. This we do in both the bound state sector and scattering sector. We provide explicit, exact and infinite series results of the first few non-perturbative orders.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15427v1
- Title: Tensor Networks with Belief Propagation Cannot Feasibly Simulate Google's Quantum Echoes Experiment
- Authors: Pablo Bermejo, Benjamin Villalonga, Brayden Ware, Guifre Vidal, Aaron Szasz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15427v1  pdf=https://arxiv.org/pdf/2604.15427v1.pdf

Abstract:
In the recent quantum echoes experiment, Google Quantum AI showed that out-of-time-order correlators (OTOCs) for random-circuit time evolution can be measured using a quantum processor more than 10,000x faster than they can be computed to similar accuracy via classical computation. This claim was substantiated by comparison with a variety of state-of-the-art classical simulation methods. One classical simulation method that was not explicitly tested was tensor networks with belief propagation (TNBP). TNBP should be poorly suited to simulating Google's echoes experiment: the states involved are highly entangled, a challenge for tensor network states; and the Willow chip has dense 2D connectivity, a challenge for belief propagation. Here we confirm, via a combination of theoretical scaling arguments and explicit numerical simulation, the intuition that TNBP is unable to simulate the quantum echoes experiment. We show that the OTOC circuits generate enough entanglement that they are largely incompressible, implying that other approaches in which OTOCs are computed by evolving a tensor network state in the Schrödinger picture will also fail. Our results further reinforce the claim that the quantum echoes experiment cannot be reproduced by classical computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15432v1
- Title: Efficient $n$-qubit entangling operations via a superconducting quantum router
- Authors: Xuntao Wu, Haoxiong Yan, Gustav Andersson, Alexander Anferov, Christopher R. Conner, Yash J. Joshi, Bayan Karimi, Amber M. King, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15432v1  pdf=https://arxiv.org/pdf/2604.15432v1.pdf

Abstract:
Quantum algorithms on near-term quantum processors are typically executed using shallow quantum circuits composed of one- and two-qubit gates. However, as circuit depth and gate number increase, gate imperfections and qubit decoherence begin to dominate, limiting algorithmic complexity. An alternative approach is to explore gates involving more than two qubits. In previous work (X. Wu et al., Physical Review X 14, 041030 (2024)), we demonstrated a new superconducting qubit architecture with user-selectable two-qubit interactions via a reconfigurable router, used to connect pairs of qubits. Here, we leverage this novel architecture to realize programmable and efficient multi-qubit operations involving more than two qubits, resulting in faster preparation of multi-qubit entangled states with good fidelities. We also successfully apply model-free reinforcement learning to perform multi-qubit gates, including training a two-qubit controlled-Z gate as well as three-qubit controlled-SWAP and controlled-controlled-phase (Fredkin and Toffoli) gates. Higher $n$th-order gates may also be feasible, using our high-connectivity router design. This could provide a more efficient and higher-fidelity implementation of complex quantum algorithms and a more practical approach to quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15435v1
- Title: Quantum Search without Global Diffusion
- Authors: John Burke, Ciaran McGoldrick
- Categories: quant-ph (primary); quant-ph; cs.DS
- Links: abs=https://arxiv.org/abs/2604.15435v1  pdf=https://arxiv.org/pdf/2604.15435v1.pdf

Abstract:
Quantum search is among the most important algorithms in quantum computing. At its core is quantum amplitude amplification, a technique that achieves a quadratic speedup over classical search by combining two global reflections: the oracle, which marks the target, and the diffusion operator, which reflects about the initial state. We show that this speedup can be preserved when the oracle is the only global operator, with all other operations acting locally on non-overlapping partitions of the search register. We present a recursive construction that, when the initial and target states both decompose as tensor products over these chosen partitions, admits an exact closed-form solution for the algorithm's dynamics. This is enabled by an intriguing degeneracy in the principal angles between successive reflections, which collapse to just two distinct values governed by a single recursively defined angle.   Applied to unstructured search, a problem that naturally satisfies the tensor decomposition, the approach retains the $O(\sqrt{N})$ oracle complexity of Grover search when each partition contains at least $\log_2(\log_2 N)$ qubits. On an 18-qubit search problem, partitioning into two stages reduces the non-oracle circuit depth by as much as 51%-96% relative to Grover, requiring up to 9% additional oracle calls. For larger problem sizes this oracle overhead rapidly diminishes, and valuable depth reductions persist when the oracle circuit is substantially deeper than the diffusion operator. More broadly, these results show that a global diffusion operator is not necessary to achieve the quadratic speedup in quantum search, offering a new perspective on this foundational algorithm. Moreover, the scalar reduction at the heart of our analysis inspires and motivates new directions and innovations in quantum algorithm design and evaluation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15436v1
- Title: Parity-unfolded distillation architecture for noise-biased platforms
- Authors: Konstantin Tiurev, Christoph Fleckenstein, Christophe Goeller, Paul Schnabl, Matthias Traube, Nitica Sakharwade, Anette Messinger, Josua Unger, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15436v1  pdf=https://arxiv.org/pdf/2604.15436v1.pdf

Abstract:
We introduce the parity-unfolded architecture, a fault-tolerant quantum computing scheme that relies on direct preparation and teleportation of small-angle rotations $ Z^{1/2^{k}}$ rather than approximating them with the conventional (Clifford + $T$) gate set. The architecture is enabled by efficient distillation of gates from an arbitrary level of the Clifford hierarchy, which we refer to as parity unfolding. With it, a state $|Z_k\rangle = Z^{1/2^{k}}|{+}\rangle$ can be prepared fault-tolerantly using $2^{k+3} + O(2^{k/2})$ biased-noise qubits on a planar chip with nearest-neighbour connectivity. For algorithms requiring native $Z^{1/2^{k}}$ gates, such as the Quantum Fourier Transform and phase estimation, the proposed scheme allows to reduce resource overheads for up to $k=7$, i.e., up to $T^{1/32}$. Furthermore, when used for the synthesis of arbitrary small-angle rotations, parity-unfolded distillation of ($T$ + $\sqrt{T}$) reduces the minimum achievable logical error rate by 43% while cutting the resource requirements by 26%, when compared to unfolded distillation of only the $T$ gate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15441v1
- Title: Quantum computation at the edge of chaos
- Authors: Tomohiro Hashizume, Zhengjun Wang, Frank Schlawin, Dieter Jaksch
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15441v1  pdf=https://arxiv.org/pdf/2604.15441v1.pdf

Abstract:
A key challenge in classical machine learning is to mitigate overparameterization by selecting sparse solutions. We translate this concept to the quantum domain, introducing quantum sparsity as a principle based on minimizing quantum information shared across multiple parties. This allows us to address fundamental issues in quantum data processing and convergence issues such as the barren plateau problem in Variational Quantum Algorithm (VQA). We propose a practical implementation of this principle using the topological Entanglement Entropy (TEE) as a cost function regularizer. A non-negative TEE is associated with states with a sparse structure in a suitable basis, while a negative TEE signals untrainable chaos. The regularizer, therefore, guides the optimization along the critical edge of chaos that separates these regimes. We link the TEE to structural complexity by analyzing quantum states encoding functions of tunable smoothness, deriving a quantum Nyquist-Shannon sampling theorem that bounds the resource requirements and error propagation in VQA. Numerically, our TEE regularizer demonstrates significantly improved convergence and precision for complex data encoding and ground-state search tasks. This work establishes quantum sparsity as a design principle for robust and efficient VQAs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15510v1
- Title: Magnetic domains stabilized by symmetry-protected zero modes
- Authors: Pavel Kos, Dominik S. Wild, Kristian Knakkergaard Nielsen
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2604.15510v1  pdf=https://arxiv.org/pdf/2604.15510v1.pdf

Abstract:
Understanding mechanisms for the breakdown of thermalization in closed quantum systems is a central problem in quantum many-body physics. We demonstrate strong non-ergodic behavior in the XX model on coupled chains, where domain-wall initial states retain an inhomogeneous magnetization profile for arbitrarily long times. We find that this effect arises due to exponentially many zero modes protected by chiral symmetry. Using an analysis based on the Lanczos algorithm, we identify a localization transition in the thermodynamic limit at a critical coupling between the chains. We further show that antiferromagnetic defects in the initial state and symmetry-breaking perturbations restore slow thermalization, whereas it remains robust for symmetry-conserving perturbations. These results establish that degenerate, symmetry-protected subspaces can give rise to thermodynamically stable non-ergodic dynamics in experimentally accessible quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15540v1
- Title: Accessible Quantum Correlations Under Complexity Constraints
- Authors: Álvaro Yángüez, Noam Avidan, Jan Kochanowski, Thomas A. Hahn
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.IT
- Links: abs=https://arxiv.org/abs/2604.15540v1  pdf=https://arxiv.org/pdf/2604.15540v1.pdf

Abstract:
Quantum systems may contain underlying correlations which are inaccessible to computationally bounded observers. We capture this distinction through a framework that analyses bipartite states only using efficiently implementable quantum channels. This leads to a complexity-constrained max-divergence and a corresponding computational min-entropy. The latter quantity recovers the standard operational meaning of the conditional min-entropy: in the fully quantum case, it quantifies the largest overlap with a maximally entangled state attainable via efficient operations on the conditional subsystem. For classical-quantum states, it further reduces to the optimal guessing probability of a computationally bounded observer with access to side information. Lastly, in the absence of side information, the computational min-entropy simplifies to a computational notion of the operator norm. We then establish strong separations between the information-theoretic and complexity-constrained notions of min-entropy. For pure states, there exist highly entangled families of states with extremal min-entropy whose efficiently accessible entanglement in terms of computational min-entropy is exponentially suppressed. For mixed states, the separation is even sharper: the information-theoretic conditional min-entropy can be highly negative while the complexity-constrained quantity remains nearly maximal. Overall, our results demonstrate that computational constraints can fundamentally limit the quantum correlations that are observable in practice.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15552v1
- Title: Feature-level analysis and adversarial transfer in rotationally equivariant quantum machine learning
- Authors: Maureen Krumtünger, Martin Sevior, Muhammad Usman
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15552v1  pdf=https://arxiv.org/pdf/2604.15552v1.pdf

Abstract:
Group-equivariant quantum models are designed to exploit symmetry and can improve trainability, but it remains unclear how symmetry constraints shape their adversarial robustness. We study this question through a feature-level analysis of equivariant quantum models in a transfer-attack setting. Under equivariance with an invariant readout, predictions depend only on the group-twirled input, which identifies the symmetry-invariant information accessible to the model together with a complementary uninformative subspace. Specializing this framework to a rotationally equivariant quantum model, we derive an explicit characterization of the accessible information in terms of rotation-invariant image statistics distributed across distinct symmetry sectors. Using targeted input transformations, we determine which of these statistics are actually relied upon for classification across several datasets. We find that equivariance alone does not guarantee transfer robustness: even within the restricted invariant feature space, the model can rely on brittle statistics, particularly ring-averaged intensities in the rotationally equivariant model, that remain vulnerable to classical transfer attacks. Guided by this analysis, we show that suppressing the symmetry sector associated with the brittle feature substantially improves robustness. These results establish a systematic mechanism to exploit symmetry-dependent features for adversarial robustness in future quantum machine learning models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15603v1
- Title: A Game Theoretic Approach for Optimizing Quantum Error Budget Distribution
- Authors: Asif Akhtab Ronggon, Tasnuva Farheen
- Categories: quant-ph (primary); quant-ph; cs.SE
- Links: abs=https://arxiv.org/abs/2604.15603v1  pdf=https://arxiv.org/pdf/2604.15603v1.pdf

Abstract:
Current fault-tolerant quantum compilers allocate error budgets uniformly during resource estimation, causing suboptimal physical resource overhead. We optimize this allocation using a potential game formulation, where Nash Equilibrium yields a Pareto-optimal distribution across logical operations, T-state distillation, and rotation synthesis. An iterated best response (IBR) algorithm converges to this equilibrium through monotonic descent of the shared cost function. Evaluation across 433 MQT benchmarks demonstrates an average reduction of 30.22\% in physical resource requirements relative to uniform baselines, with peak improvements of 97.81\% for specific circuit instances. This establishes a game-theoretic foundation for strategic error budget optimization in fault-tolerant quantum design automation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15604v1
- Title: Many-Body Amplified Nonclassical Photon Emission in Cavity-Coupled Atomic Arrays
- Authors: Tang Jing, Yuangang Deng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15604v1  pdf=https://arxiv.org/pdf/2604.15604v1.pdf

Abstract:
The generation of high-performance nonclassical light remains a cornerstone of quantum technologies, yet faces a fundamental trade-off between emission purity and brightness. Here, we demonstrate that cavity-mediated many-body spin-exchange interactions provide a route to overcome this constraint by collectively amplifying spectral anharmonicity. In a cavity-coupled atomic array with a programmable relative phase $φ$, the resulting interference-interaction mechanism reshapes the dressed-state manifold and enables deterministic switching between distinct quantum emission regimes. For $φ=0$, constructive interference yields high-purity single-photon emission with antibunching improved by four orders of magnitude while preserving strong photon flux. Conversely, for $φ=π$, destructive interference creates a dark single-photon manifold, resonantly activating two-photon processes to produce bright and pure photon-pair bundles. Our work establishes interference-engineered many-body interactions as a scalable mechanism for on-demand quantum light generation and open a new avenue for harnessing collective many-body physics in quantum photonics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15605v1
- Title: Deterministic multiphoton bundle emission via interference-interaction control
- Authors: Jing Tang, Yuangang Deng
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2604.15605v1  pdf=https://arxiv.org/pdf/2604.15605v1.pdf

Abstract:
The controlled generation of nonclassical light beyond single photons remains a central challenge in quantum optics, due to the difficulty of enhancing multiphoton processes while suppressing lower-order excitations. Here we propose an interference-interaction-engineered scheme for programmable few-photon emission in a cavity-QED system of three atoms coupled to orthogonal cavity modes. By adiabatically eliminating an auxiliary Fabry-Pérot cavity, we generate a tunable cavity-mediated spin-exchange interaction $χ$, which, combined with a controllable geometric phase $φ$, reshapes the many-body dressed-state spectrum. This interplay enables selective addressing of excitation manifolds ($N=1,2,3$), establishing a direct mapping between excitation structure and photon-emission channels. For $φ=0$, constructive interference enhances the spectral anharmonicity of low-excitation manifolds, yielding tunable single- and two-photon emission associated with the $N=1$ and $N=2$ manifolds. In contrast, for $φ=2π/3$, destructive interference suppresses lower-order excitation pathways and activates a resonant three-photon channel originating from the $N=3$ manifold. Importantly, the cavity-mediated interaction $χ$ further enhances spectral separation between manifolds, enabling a substantial improvement in multiphoton purity while maintaining a sizable photon population. We demonstrate a three-order-of-magnitude enhancement in two-photon purity and more than two orders of magnitude improvement in three-photon emission. Our results establish a unified interference-interaction framework in which effective optical nonlinearities can be programmably engineered through phase and interaction, providing a scalable route toward high-purity multiphoton sources and programmable quantum photonic devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15616v1
- Title: Overcoming the Lamb Shift in System-Bath Models via KMS Detailed Balance: High-Accuracy Thermalization with Time-Bounded Interactions
- Authors: Hongrui Chen, Zhiyan Ding, Ruizhe Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15616v1  pdf=https://arxiv.org/pdf/2604.15616v1.pdf

Abstract:
We investigate quantum thermal state preparation algorithms based on system-bath interactions and uncover a surprising phenomenon in the weak-coupling regime. We rigorously prove that, if the system-bath interaction is engineered so that the transition part of the approximate Lindbladian generator satisfies the KMS detailed balance condition, then the unique fixed point of the dynamics can be made arbitrarily close to the Gibbs state in the weak-coupling limit, regardless of the structure of the Lamb shift term. Importantly, this remains true even when the approximate Lindbladian differs substantially from the ideal Davies generator and the Lamb shift term does not commute with the thermal state. Our result shows that the role of the KMS detailed balance condition extends well beyond standard Lindbladian dynamics, serving as a general principle for a broader class of dissipative systems. Furthermore, by combining this with a general perturbation framework, we bound the mixing time of the dynamics and establish an end-to-end complexity of $O(\varepsilon^{-1})$ for Gibbs state preparation. These guarantees apply to any Hamiltonian for which the corresponding KMS-detailed-balance Lindbladian is known to mix rapidly.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15626v1
- Title: Bridge the Gap between Classical and Quantum Neural Networks with Residual Connections
- Authors: Junxu Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15626v1  pdf=https://arxiv.org/pdf/2604.15626v1.pdf

Abstract:
We introduce a Hybrid Quantum Residual Network (HQRN) and establish an exact functional correspondence between its state evolution and the dynamics of classical networks with residual connections. When inputs are restricted to the computational basis, the HQRN reduces to its classical analog, enabling the direct translation of optimized classical weights into quantum unitary operations, effectively inheriting the landscape benefits of classical optimization. Conversely, when processing general mixed states, the HQRN leverages off-diagonal quantum correlations to resolve features inaccessible to its classical analog. We validate this framework through digit recognition and bipartite entanglement classification. Notably, HQRN achieves high classification accuracy even for adversarial separable states that mimic the marginal measurement statistics of entangled pairs. Our results bridge the gap between classical and quantum residual learning, paving a scalable pathway for deep quantum architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15666v1
- Title: Explainable quantum regression algorithm with encoded data structure
- Authors: C. -C. Joseph Wang, F. Perkkola, I. Salmenperä, A. Meijer-van de Griend, J. K. Nurminen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15666v1  pdf=https://arxiv.org/pdf/2604.15666v1.pdf

Abstract:
Hybrid variational quantum algorithms are promising for solving practical problems, such as combinatorial optimization, quantum chemistry simulation, quantum machine learning, and quantum error correction on noisy quantum computers. However, variational quantum algorithms (derived from randomized hardware-efficient ansatz or adaptive ansatz) become a black box, not trustworthy for model interpretation, and not to mention for application deployment in informing critical decisions. In this paper, we construct the first interpretable quantum regression algorithm, in which the quantum state exactly encodes the classical data table and the variational parameters correspond directly to the regression coefficients, which are real numbers by construction, providing a high degree of model interpretability and minimal cost to optimize due to the right expressiveness. We also exploit the encoded data structure to reduce the gate complexity of computing the regression map. To reduce circuit depth in nonlinear regression, our algorithm can be extended by directly constructing nonlinear features via classical preprocessing, such as independent encoded column vectors. By design, the model performance is determined by the cost function measurement results $\mathcal{C}$ synchronous to the mean squared errors (MSE) for the regression models. We derived the read-out errors induced by one-hot encoding and compact encoding; the required physical qubit resources are exponentially compressed for the compact encoding to be favorable for noisy quantum devices. We also derive the cost function dependent sample complexity $ \in \mathcal{O}\left(σ^{2}(\mathcal{C}) \ln (1/α)/ε^{2}\right)$ under the error budget $ε$ and confidence tolerance $α$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15693v1
- Title: Observable-Guided Generator Selection for Improving Trainability in Quantum Machine Learning with a $ \mathfrak{g} $-Purity Interpretation under Restricted Settings
- Authors: Hiroshi Ohno
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15693v1  pdf=https://arxiv.org/pdf/2604.15693v1.pdf

Abstract:
To study generator design for parameterized unitaries in quantum machine learning (QML), we propose an observable-guided generator selection algorithm for $ n $-qubit Pauli-string generator pools. The proposed method selects generators based on two criteria: maintaining large first-order sensitivity in the gradients and suppressing second-order interference in the Hessian matrix. Under a restricted setting with Pauli-string observables and candidate generators, the selection problem can be formulated as a binary optimization problem that favors mutually anti-commuting generators. Numerical experiments on a synthetic dataset with a small-scale five-qubit circuit show that the selected generators yield faster training than random generator selection in our setting, while exhibiting similar expressibility. Furthermore, under additional algebraic assumptions, the proposed criteria admit an interpretation in terms of the $ \mathfrak{g} $-purity of the observable: the first-order sensitivity is proportional to the $ \mathfrak{g} $-purity, whereas the second-order interference, namely the off-diagonal elements of the Hessian matrix, is upper-bounded by it. These results suggest that observable-guided generator selection is a promising direction for improving trainability in restricted QML settings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15752v1
- Title: Quantifying Uhlmann curvature from Yang-Mills action and its implications in quantum multiparameter estimation
- Authors: Yi-Lin Ge, Bing-Shu Hu, Ling-Yun Deng, Xiao-Ming Lu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15752v1  pdf=https://arxiv.org/pdf/2604.15752v1.pdf

Abstract:
The geometry of quantum states has profound implications in quantum multiparameter estimation. While the Riemannian structure of quantum state space is well understood, the full understanding of the curvature structure of mixed quantum states is still an open problem. Inspired by the Yang-Mills action in non-Abelian gauge theory, we propose a scalar quantifying the Uhlmann curvature and establish its connection to the measurement incompatibility in quantum multiparameter estimation problems. We show that this curvature measure is gauge invariant, reparametrization invariant, and vanishes if and only if the Uhlmann curvature vanishes. We also explicitly calculate the Uhlmann curvature for the joint estimation of phase and phase diffusion as an example.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15755v1
- Title: Optically detected magnetic resonance of nitrogen-vacancy centers in diamond using two-photon excitation
- Authors: Lam T. Nguyen, Khanh Kieu
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.atom-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.15755v1  pdf=https://arxiv.org/pdf/2604.15755v1.pdf

Abstract:
We demonstrate the use of two-photon excitation for observing the ground state optically detected magnetic resonance (ODMR) of nitrogen-vacancy centers in diamonds at room temperature. An ultrafast femtosecond laser at 1040 nm was used for excitation, while fluorescence signal read out was achieved through a combination of a PMT and a lock-in amplifier. The imaging capability of two-photon excitation fluorescence (2PEF) was utilized to map the distribution of NV centers in a bulk diamond and micro-sized diamonds. For the first time, ODMR traces of the nitrogen-vacancy center are observed with two-photon excitation, providing a promising tool for fast 3D quantum sensing and imaging.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15763v1
- Title: Machine-learning-assisted material and geometry characterization from Casimir force measurement
- Authors: Hideo Iizuka, Shanhui Fan
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.15763v1  pdf=https://arxiv.org/pdf/2604.15763v1.pdf

Abstract:
A broadband electromagnetic source is important for scientific and technological applications. Quantum vacuum fluctuations, which manifest most prominently in the Casimir effect, provide a fundamentally broadband electromagnetic source. Here we explore a potential consequence of the broadband nature of quantum vacuum fluctuations, by showing that such fluctuations can enable measurement of material permittivity over a broad frequency range. Specifically, we consider the Casimir force in a parallel-plate geometry, with one plate covered by a nanoscopic thin film. Using a machine learning approach, we show that one can infer both the thickness of the film and its permittivity over a broad frequency range, starting from the dependency of the Casimir forces on the spacing between the two plates. Our work highlights the application potential of using vacuum fluctuations as a naturally-existing broadband electromagnetic source for material characterization, and shows that the inverse problem in Casimir force calculation can be solved with machine learning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15765v1
- Title: Orkan: Cache-friendly simulation of quantum operations on hermitian operators
- Authors: Timo Ziegler
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15765v1  pdf=https://arxiv.org/pdf/2604.15765v1.pdf

Abstract:
Classical simulation of quantum operations is essential for algorithm design, noise characterisation, and benchmarking of quantum hardware. The most general physically realisable operation can be described by a positive linear map acting on a hermitian operator, representing either a density matrix or an observable. Established simulators vectorise the density matrix on an $n$-qubit Hilbert space and reuse state-vector kernels, storing all $2^{2n}$ elements and forgoing the benefits of hermitian symmetry. In this work, I introduce \emph{Orkan}, a simulation library that uses a tiled memory layout storing only the lower triangle of the hermitian matrix at tile granularity, roughly halving both the memory footprint and the wall time to simulate the evolution of quantum states under generic quantum operations. The implementation treats any hermitian operator uniformly and is agnostic to whether the Schrödinger or Heisenberg picture is used. Dedicated $k$-local conjugation algorithms update all entries of the hermitian matrix in a single pass. Benchmarks against Qiskit Aer, QuEST, and Qulacs show consistent wall-clock speedups of $2$-$4{\times}$ partly attributable to the reduced memory footprint.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15799v1
- Title: Spectral design principles for local-excitation retention in impurity-assisted atomic arrays
- Authors: Junpei Oba
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.comp-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.15799v1  pdf=https://arxiv.org/pdf/2604.15799v1.pdf

Abstract:
Enhanced local-excitation retention in atomic arrays allows to exploit cooperative radiative effects to suppress emission and prolong excited-state lifetimes. We consider an impurity-assisted setting involving a single storage atom being initially excited and study the survival of local excitation under neither write nor retrieval fields. Because the corresponding dynamics can involve multiple interfering collective modes, the survival dynamics cannot determined from the smallest collective decay rate alone. Thus, using a biorthogonal eigenmode decomposition of an effective non-Hermitian Hamiltonian, we show that the survival dynamics are jointly governed by the decay rates of the eigenmodes and their overlaps with the initial excitation. Large oscillations occur when multiple long-lived modes have comparable weights. Accordingly, we introduce a physically motivated spectral surrogate objective that favors both small weighted decay rates and an initial-state weight concentrated on a single subradiant mode. As a proof of principle of this spectral design, we apply the surrogate to constrained atom-position optimization under minimum-distance constraints and obtain nontrivial aperiodic configurations with enhanced local-excitation retention. Our findings unveil spectral design principles for local-excitation retention in impurity-assisted atomic arrays and provide a proof of principle for their inverse design.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15836v1
- Title: A Practical Semi-Quantum Signature Protocol with Improved Eavesdropping Detection
- Authors: Zengyu Pang, Hua Xiang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15836v1  pdf=https://arxiv.org/pdf/2604.15836v1.pdf

Abstract:
Semi-quantum signature (SQS) schemes aim to enable quantum signature functionality in scenarios where only a subset of participants possess full quantum capabilities, thereby improving practical deployability while preserving quantum security advantages. Within this framework, we present a practical SQS protocol based on Bell states. The protocol is designed so that only the signer requires full quantum capability, significantly alleviating the quantum burden on the remaining participants. To strengthen security in semi-quantum environments, we incorporate an improved eavesdropping-detection mechanism that more effectively detects tampering. Compared with many existing schemes, which do not explicitly consider tampering of already generated signatures in their unforgeability analyses, the proposed protocol is designed to remain secure in the presence of such tampering.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15867v1
- Title: Approximate Cosine Similarity Estimation via an Angle-Encoding Hadamard Test
- Authors: Hiroshi Ohno
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15867v1  pdf=https://arxiv.org/pdf/2604.15867v1.pdf

Abstract:
The Hadamard test is a standard quantum primitive for estimating inner products and expectation values, but in data-processing settings its practical utility is often limited by the cost of preparing amplitude-encoded quantum states. In this study, we investigate an angle-encoding variant of the Hadamard test for estimating cosine similarity between normalized real-valued vectors. The proposed method decomposes the similarity computation into elementwise two-qubit Hadamard-test circuits that can, in principle, be executed in parallel, resulting in constant circuit depth with respect to the vector dimension at the expense of a larger qubit footprint and classical post-processing. Because the resulting estimator is approximate, we analyze the induced bias and show that it is non-negative under the approximation used in our derivation. Numerical experiments on random normalized vectors show that, in the tested setting, the estimation error decreases as the vector dimension increases. We further illustrate a possible application to cosine-attention-based Transformer models. These results suggest that the angle-encoding Hadamard test may provide a useful design point for near-term similarity estimation when shallow circuit depth is preferred over compact qubit usage.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15886v1
- Title: Asymptotic optimality of Grover-Radhakrishnan-Korepin algorithm
- Authors: Kun Zhang, Kang-Yuan Chen, Xiao-Hui Wang, Vladimir Korepin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15886v1  pdf=https://arxiv.org/pdf/2604.15886v1.pdf

Abstract:
Grover's algorithm is a cornerstone of quantum algorithms and is strictly optimal in oracle-query complexity. While the full search problem admits no further improvement, one may trade accuracy for speed in the partial search problem, where the task is to identify only the block containing the target item. The best known quantum algorithm for the partial search problem is the Grover-Radhakrishnan-Korepin (GRK) algorithm, whose optimality has long been conjectured but not proved. In this work, we prove the optimality of GRK in the large-block limit. We formulate partial search as a time-optimal control problem and apply the Pontryagin maximum principle to derive the switching-function dynamics, establish the bang-bang structure of regular extremals, and exclude non-optimal switching patterns. As a result, we show that the optimal regular extremal has the global-local-global form, which yields a control-theoretic proof of the asymptotic optimality of the GRK algorithm in oracle-query complexity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15895v1
- Title: Digital Predistortion for Flux Control of Tunable Superconducting Qubits
- Authors: Dharun Venkateswaran, Felice Francesco Tafuri, Yuanzheng Paul Tan, Bruno Aznar Martinez, Alisa Danilenko, Likai Yang, Arnaud Carignan-Dugas, Christoph Hufnagel, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2604.15895v1  pdf=https://arxiv.org/pdf/2604.15895v1.pdf

Abstract:
Flux-tunable superconducting qubits rely on fast flux control pulses to implement two-qubit entangling quantum gates, a key building block for quantum algorithms. However, distortion effects introduced by non-ideal control electronics, parasitic components, and the cryogenic quantum chip response can all degrade the gate fidelity. We present a digital predistortion (DPD) framework for characterizing and then compensating for these distortions using a combination of infinite impulse response (IIR) and finite impulse response (FIR) filters. Experiments on a flux-tunable quantum processing unit (QPU) demonstrate a successful correction of step-response distortions on the flux-control line, with a compensated control signal showing only sub-percent deviations from the ideal target linear behavior. The demonstrated method enables automated rapid calibration of flux control channels for superconducting QPUs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15912v1
- Title: Sensing of Low-Frequency Electric Fields Using Rydberg EIT within the Fisher Information Framework
- Authors: Tianyu Zhou, Haipeng Xie, Xin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.15912v1  pdf=https://arxiv.org/pdf/2604.15912v1.pdf

Abstract:
Rydberg atoms, which possess exceptionally large electric dipole moments, offer a promising route for electric field sensing as well as metrology traceable to the International System of Units (SI); however, current research predominantly focuses on the microwave (MW) regime, leaving the quasi-direct current (quasi-DC) and low-frequency bands, ubiquitous in power systems, largely unexplored. In this paper, we present a theoretical investigation into low-frequency electric field detection. To this end, we establish a comprehensive modeling framework incorporating Fisher information (FI) and the Cramér-Rao lower bound (CRLB) to quantify the fundamental precision limits of electromagnetically induced transparency (EIT) readouts. Building upon this framework, we propose a linearized sensing strategy utilizing a DC-biased two-point differential measurement. Numerical validations demonstrate that this approach effectively mitigates the weak-field insensitivity for both DC and AC fields, achieving a CRLB-limited sensitivity bound of approximately $1\times 10^{-4}$ V/m/$\sqrt{\text{Hz}}$. Furthermore, to surpass the single-pass sensitivity limit, we introduce a Fabry-Pérot (FP) cavity-enhanced configuration. This architecture leverages intracavity phase modulation to significantly steepen the transmission slope, boosting the FI by over two orders of magnitude compared to standard free-space configurations. This work provides a rigorous theoretical basis and design guidance for the high-precision quantum monitoring of electromagnetic environments in smart grids.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15920v1
- Title: Local qubit invariants on quantum computer
- Authors: Szilárd Szalay, Frédéric Holweck
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2604.15920v1  pdf=https://arxiv.org/pdf/2604.15920v1.pdf

Abstract:
We present two general methods to implement quantum circuits for the direct measuring of local unitary invariants on quantum computers. We work these out for important three-qubit invariants, and also demonstrate these on the IBM Quantum Platform for important entanglement measures of three qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15953v1
- Title: Finite-Time Thermodynamics of an Autonomous Information Machine
- Authors: Wanyan Chen, Miao Chen, Yu-Han Ma
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2604.15953v1  pdf=https://arxiv.org/pdf/2604.15953v1.pdf

Abstract:
While externally driven information engines are well understood, the thermodynamic constraints of their autonomous counterparts remain an open question. Here, we investigate the finite-time operation of an autonomous machine functioning as both an information eraser and a refrigerator, revealing that its irreversibility is bounded by the transient information geometry. Beyond steady-state boundaries, we map the landscape of optimal operation times across both functional modes, uncovering a unique synergistic regime where erasure power $P$ and efficiency $η$ increase simultaneously. Fundamentally, this performance is governed by a trade-off relation, $v(1-η)P/η\le D$, where $v$ is the operational speed and $D$ denotes an information-geometric distance. Our findings pave the way for optimizing fast autonomous information-energy conversion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15971v1
- Title: A Modular Cryogenic Link for Microwave Quantum Communication Over Distances of Tens of Meters
- Authors: Josua D. Schär, Simon Storz, Paul Magnard, Philipp Kurpiers, Janis Lütolf, Melvin Gehrig, Jean-Claude Besse, Anatoly Kulikov, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2604.15971v1  pdf=https://arxiv.org/pdf/2604.15971v1.pdf

Abstract:
Quantum technologies promise a radically new way to solve classically intractable computing problems. Superconducting circuits as a platform are at the forefront of this field. The cryogenic operation temperatures of superconducting circuits however impose challenges for the further scaling to many connected quantum information processing units into a local area or global network. In this work, we present a hardware solution for connecting quantum devices operating at microwave frequencies into local area networks, which enable the exchange of quantum information between spatially separated parties. Specifically, we demonstrate a modular system spanning distances of 5, 10 and 30 meters operated at cryogenic temperatures and connecting two superconducting circuit systems, located in individual dilution refrigerators, through a quantum communication channel. We develop a thermal model to evaluate the heat transfer processes in the setup, optimize the design and select appropriate materials for its construction. The assembled 30-meter-long system achieves operating temperatures of below 50 mK after a cooldown time of about six and a half days. This link enables the execution of distributed quantum computing and communication algorithms. It also adds the resource of non-locality, certified by a loophole-free Bell test, to the field of quantum science and technology with superconducting circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16015v1
- Title: Discovering quantum phenomena with Interpretable Machine Learning
- Authors: Paulin de Schoulepnikoff, Hendrik Poulsen Nautrup, Hans J. Briegel, Gorka Muñoz-Gil
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cs.LG
- Links: abs=https://arxiv.org/abs/2604.16015v1  pdf=https://arxiv.org/pdf/2604.16015v1.pdf

Abstract:
Interpretable machine learning techniques are becoming essential tools for extracting physical insights from complex quantum data. We build on recent advances in variational autoencoders to demonstrate that such models can learn physically meaningful and interpretable representations from a broad class of unlabeled quantum datasets. From raw measurement data alone, the learned representation reveals rich information about the underlying structure of quantum phase spaces. We further augment the learning pipeline with symbolic methods, enabling the discovery of compact analytical descriptors that serve as order parameters for the distinct regimes emerging in the learned representations. We demonstrate the framework on experimental Rydberg-atom snapshots, classical shadows of the cluster Ising model, and hybrid discrete-continuous fermionic data, revealing previously unreported phenomena such as a corner-ordering pattern in the Rydberg arrays. These results establish a general framework for the automated and interpretable discovery of physical laws from diverse quantum datasets. All methods are available through qdisc, an open-source Python library designed to make these tools accessible to the broader community.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16023v1
- Title: MacWilliams Identities for Intrinsic Quantum Codes
- Authors: Eric Kubischta, Ian Teixeira
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2604.16023v1  pdf=https://arxiv.org/pdf/2604.16023v1.pdf

Abstract:
We develop an intrinsic enumerator framework for quantum error correction in unitary representations of symmetry groups. An intrinsic quantum code is a subspace of a representation $V$ of a group $G$, and errors are organized by the decomposition of the conjugation representation on $\mathcal{L}(V)$ into isotypic subspaces. Associated with any orthogonal decomposition of $\mathcal{L}(V)$ we introduce two families of quadratic enumerators, called projector and twirl enumerators, which satisfy positivity, normalization, and Knill--Laflamme type inequalities. When the conjugation representation is multiplicity--free, these enumerators are related by a linear transform that we interpret as an intrinsic MacWilliams identity. For $G=\mathrm{SU}(2)$, we compute this transform explicitly in terms of Wigner $6j$-symbols. Applied to symmetric-power representations, this gives linear programming bounds for permutation-invariant qubit and qudit codes, including extremality results for the four-qubit, seven-qubit, and three-qutrit examples treated here. We also develop the general equivariant theory in the presence of multiplicities, where the enumerators become matrix-valued, the MacWilliams transform becomes block unitary, and the resulting feasibility problem becomes semidefinite; we illustrate this theory in a first non-multiplicity-free $\mathrm{SU}(3)$ example.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16051v1
- Title: Comment on "A General Framework for Constructing Local Hidden-state Models to Determine the Steerability"
- Authors: Nick von Selzam, Florian Marquardt
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16051v1  pdf=https://arxiv.org/pdf/2604.16051v1.pdf

Abstract:
We point out that the method presented in a recent arXiv article by Jia et al. (arXiv:2512.21848) for constructing local hidden-state models closely follows the framework we developed in N. von Selzam & F. Marquardt (PRX Quantum, 2025) for constructing local hidden-variable models. While Jia et al. cite our work, the extent of the methodological overlap and the degree of textual similarity are not adequately reflected by the attribution given. We document this overlap in detail.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16071v1
- Title: Security Framework for Quantum Distance-Bounding
- Authors: Kevin Bogner, Aysajan Abidin, Dave Singelee, Bart Preneel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16071v1  pdf=https://arxiv.org/pdf/2604.16071v1.pdf

Abstract:
Distance-bounding (DB) protocols let a verifier upper-bound a prover's physical distance by timing rapid challenge-response exchanges. Quantum communication promises simpler DB protocols with stronger security guarantees, yet existing quantum distance-bounding (QDB) proposals are analysed in ad-hoc models and, to the best of our knowledge, lack a common game-based treatment of standard fraud attacks. We contribute (i) a reusable security framework for QDB that fixes system and timing assumptions, specifies a quantum-capable adversary model, formalises distance-, mafia-, and terrorist-fraud experiments, and includes a simple i.i.d. depolarizing noise model; and (ii) an application of this framework to a published QDB protocol. For this protocol we characterise the honest per-round acceptance probability under noise and lift it to the multi-round setting, yielding explicit completeness guarantees as a function of the number of fast rounds, the acceptance threshold, and the noise parameter. For active adversaries we bound the per-round success probability of distance-fraud attacks and analyse the best known mafia-fraud strategy, deriving corresponding multi-round soundness bounds. We also show that the protocol is inherently insecure against terrorist-fraud in our model. The framework cleanly separates protocol-independent definitions from protocol-specific analysis and can be used to evaluate existing and future QDB protocols on a common basis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16101v1
- Title: Quantum-Resistant Quantum Teleportation
- Authors: Xin Jin, Nitish Kumar Chandra, Mohadeseh Azari, Jinglei Cheng, Zilin Shen, Kaushik P. Seshadreesan, Junyu Liu
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2604.16101v1  pdf=https://arxiv.org/pdf/2604.16101v1.pdf

Abstract:
We propose a quantum-resistant quantum teleportation (QRQT) framework protected by post-quantum cryptography (PQC) to secure the classical correction channel, which is vulnerable to quantum adversaries. By applying PQC to the classical control bits, QRQT eliminates the classical attack surface of quantum teleportation. Our analysis reveals that quantum memory is a hidden bottleneck linking physical and computational security: its finite coherence time simultaneously limits communication distance, constrains tolerable PQC overhead, and restricts the adversary attack window. Under realistic parameters (1 ms coherence, fiber-optic propagation), the maximum secure teleportation distance ranges from 191 km (FrodoKEM-1344) to 199 km (Kyber512). We show that the joint classical-quantum attack probability exhibits a non-monotonic, Bell-shaped profile due to the opposing time dependencies of classical cryptanalysis and quantum decoherence, establishing a bounded optimal attack window beyond which adversarial success decays exponentially. We further analyze how leakage of classical correction bits affects teleportation security under four stochastic leakage models: independent exponential, sequential, burst, and correlated leakage, also accounting for amplitude damping on the shared Bell pair. For each scenario, we derive closed-form expressions for the average Holevo quantity and teleportation fidelity as functions of time, providing measurement-independent upper bounds on extractable information and guiding the design of leakage-resilient quantum communication protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16107v1
- Title: Entanglement and photoelectron holography in dissociative photoionization: molecular quantum eraser
- Authors: Sebastian Hell, Paul Winter, Martin Gärttner, Julian Späthe, Saurabh Mhatre, Dejan B. Milošević, Gerhard G. Paulus, Manfred Lein, et al.
- Categories: quant-ph (primary); quant-ph; physics.chem-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.16107v1  pdf=https://arxiv.org/pdf/2604.16107v1.pdf

Abstract:
In a double-slit experiment with a bipartite system, the visibility of interference fringes depends on the availability of which-way information. Here, we report the formation of a Bell-like state of photoelectron and residual ion in the multiphoton dissociative ionization of the D$_2$ molecule. Evidence for entanglement is provided by the correlated emission directions of photoelectron and ion, which is observed using a COLTRIMS reaction microscope. In the presence of this correlation, the holographic interference fringes contained in the photoelectron momentum distributions are suppressed, indicating the existence of which-way information. We show that the which-way information is erased, and the interference pattern is restored, when a single ionic state is selected. The experimental observations and conclusions are fully supported by the numerical solution of the electronic-nuclear time-dependent Schrödinger equation. Our work demonstrates that coincidence spectroscopy of ions and electrons is a powerful method for studying fundamental concepts of quantum information science within the context of ultrafast light-matter interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16136v1
- Title: Quantum Noise Suppression Beyond the Standard Quantum Limit in a Hybrid Magnonic Optomechanical System
- Authors: Alolika Roy, Amarendra K. Sarma
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.16136v1  pdf=https://arxiv.org/pdf/2604.16136v1.pdf

Abstract:
We theoretically study how quantum measurement noise can be engineered in a hybrid cavitymagnomechanical platform for precision force sensing. The proposed configuration consists of a driven optomechanical cavity, with a movable mirror on one side plus a fixed semi-transparent mirror on the other side, coupled to a magnon mode, with an OPA placed inside the cavity. We show that the magnon mediated dynamics reshapes the added-noise spectrum leading to improved sensitivity compared to a conventional optomechanical sensor. In particular, by satisfying the coherent quantum noise cancellation (CQNC) criterion, radiation-pressure back-action can be fully suppressed. In addition, a larger OPA pump gain permits operation beyond the standard quantum limit at substantially reduced laser power, thereby mitigating power-related constraints without sacrificing performance. These combined advantages provide a practical pathway to below-SQL weak force detection and can outperform existing approaches based on squeezing in magnomechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16139v1
- Title: Converting non-Hermitian degeneracies of any order: Hierarchies of exceptional points and degeneracy manifolds
- Authors: Grigory A. Starkov, Sharareh Sayyad
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2604.16139v1  pdf=https://arxiv.org/pdf/2604.16139v1.pdf

Abstract:
The emergence of various types of degeneracies plays a crucial role in optimizing and engineering different physical phenomena in non-Hermitian physics. In our work, we focus on the derogatory Exceptional Points (EPs), which are characterized by multiple Jordan blocks corresponding to the same eigenvalue. We demonstrate that, under certain infinitesimal perturbations, a derogatory EP can be converted into an EP of different structure without varying the total order of degeneracy. In particular, such conversion can increase the size of the largest Jordan block and, hence, the sensitivity of the eigenspectrum to parameter variation, which is an important feature for practical applications. Furthermore, by analyzing all possible conversions, we introduce hierarchies of degeneracies of the same order that appear when perturbing non-Hermitian systems. We systematically explore hierarchies in the absence of any symmetry and when pseudo-Hermitian symmetry is present. Our study facilitates engineering various degeneracies of non-Hermitian systems, paving the way to extending the implications of non-Hermitian physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16140v1
- Title: Characterizing all non-Hermitian degeneracies using algebraic approaches: Defectiveness and asymptotic behavior
- Authors: Sharareh Sayyad, Grigory A. Starkov
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2604.16140v1  pdf=https://arxiv.org/pdf/2604.16140v1.pdf

Abstract:
The presence of degeneracies plays a crucial role in describing the behavior of non-Hermitian (NH) systems. In these systems, there are two key types of degeneracies: $n$-bolical degeneracies, which are analogous to Hermitian degeneracies, and various forms of exceptional points, each associated with different orders that correspond to sizes of the Jordan blocks. These types of degeneracies may coalesce at the same energy level, forming multi-block degeneracies. To understand how a multi-block degenerate NH system responds to perturbations, one should address how each types of involved degeneracies disperse. In this work, we systematically characterize the asymptotic behavior of all types of multi-block degeneracies in NH systems using a rigorous mathematical formulation. Through a range of examples, we demonstrate that our algebraic approach can facilitate the analysis of NH degeneracies in various settings relevant to experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16144v1
- Title: Gravitationally induced wave-function collapse from dynamical bifurcation
- Authors: C. A. S. Almeida
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; gr-qc
- Links: abs=https://arxiv.org/abs/2604.16144v1  pdf=https://arxiv.org/pdf/2604.16144v1.pdf

Abstract:
We propose an effective non-relativistic framework in which wave-function collapse emerges as a deterministic dynamical instability induced by gravitational self-interaction and regulated by short-distance repulsion. The dynamics is described by a nonlinear Schrödinger equation supplemented by a phenomenological repulsive sector ensuring regularity at high densities. Using a variational Gaussian ansatz, we derive an explicit effective energy functional and show that extended quantum states lose stability beyond a critical mass scale. This loss of stability is associated with a bifurcation in the reduced dynamical system governing the wave-function width, leading to the emergence of stable localized configurations. Within this picture, collapse corresponds to the dynamical selection of one of these localized attractors, driven by infinitesimal asymmetries in the initial state and occurring without stochastic noise or environmental coupling. The mechanism provides a controlled and quantitative realization of gravity-induced localization, extending Schrödinger--Newton-type models while avoiding their pathological short-distance behavior. Possible implications for mesoscopic systems probing the quantum-to-classical transition are briefly discussed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16164v1
- Title: A unified framework for efficient quantum simulation of nonlinear spectroscopy
- Authors: Long Xiong, Xiaoyang Wang, Xiaoxia Cai, Xiao Yuan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16164v1  pdf=https://arxiv.org/pdf/2604.16164v1.pdf

Abstract:
Nonlinear spectroscopy is a cornerstone of quantum science, providing unique access to multi-point correlations, quantum coherence, and couplings that are invisible to linear methods. However, classical simulation of these phenomena is fundamentally limited by the exponential growth of the Hilbert space, and practical quantum algorithms for the nonlinear regime have remained largely unexplored. Here, we present a unified quantum algorithmic framework for computing $n$-th order nonlinear spectroscopies. By reformulating multi-time responses as a weighted sum of expectation values at finite pump amplitudes via a generalized parameter shift rule, our approach bypasses the costly evaluation of high-order commutators and time-dependent operator expansions. This reformulation enables efficient execution via real-time evolution on current quantum hardware, ensuring inherent noise resilience. We validate the framework on IBM's superconducting quantum processors, successfully obtain higher-order response functions of a 12-qubit XXZ spin-chain. Furthermore, the versatility of our method is demonstrated by resolving quasi-particle excitation spectra in spin-liquids and identifying interaction-induced cross-peaks in atomic systems. Our results establish a practical and scalable pathway for probing complex quantum dynamics on near-term quantum devices, extending the reach of quantum simulation into the nonlinear domain.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16165v1
- Title: Single-Satellite Quantum Repeater Performance Analysis
- Authors: Cameron Paterson, Jasminder S. Sidhu, Thomas Brougham, Sarah E. McCarthy, Daniel K. L. Oi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16165v1  pdf=https://arxiv.org/pdf/2604.16165v1.pdf

Abstract:
Space-based entanglement distribution has the potential to extend the range of quantum communication beyond that achievable through optical fibres that are constrained by exponential losses. Quantum repeaters have been proposed to mitigate the effects of channel losses for both fibre and satellite networks. Although quantum repeaters can improve entanglement distribution efficiency, the rate is constrained by classical communication latency in the entanglement swapping process. Direct dual downlink entangled pair distribution does not suffer such a latency restriction, hence can ``brute force'' the problem of high dual channel loss through increased source rate. Hence, the comparative requirements of direct pair distribution versus quantum repeater satellites are important for the design and deployment of space-based entanglement distribution systems. Here, we consider the simplest case of a single satellite establishing entanglement between two ground stations, comparing the performance of direct dual downlink to that of a space-based quantum repeater for general overpass geometries. We also study the long-term entanglement distribution performance for different ground station pairs and determine altitudinal dependence. Finally, we study the fidelity distribution of a satellite repeater system through Monte Carlo modelling of waiting times and rate statistics, exploring the effect of quantum memory capacity, decoherence rates, and operational policies. These results will inform mission design for future space-borne quantum repeater nodes, as well as requirements on space-based memory platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16174v1
- Title: All-photonic quantum key distribution beyond the single-repeater bound
- Authors: Matthew S. Winnel, Sergio Juárez, Chithrabhanu Perumangatt, Taofiq Paraiso, R. Mark Stevenson
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16174v1  pdf=https://arxiv.org/pdf/2604.16174v1.pdf

Abstract:
Quantum protocols require classical signaling, and when classical signals propagate faster than quantum ones, standard rate-loss limits can be surpassed. We introduce an all-photonic measurement-device-independent quantum key distribution protocol that exceeds the single-repeater bound without error correction. When quantum signals travel at two-thirds the classical speed, the key rate scaling approaches $η^{2/5}$. We propose a single-rail, temporally multiplexed architecture that extends twin-field-type protocols to multiple nodes and surpasses their key rate without ideal quantum memories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16190v1
- Title: Coherence dynamics in Simon's quantum algorithm
- Authors: Linlin Ye, Zhaoqi Wu, Shao-Ming Fei
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16190v1  pdf=https://arxiv.org/pdf/2604.16190v1.pdf

Abstract:
Quantum coherence plays a pivotal role in quantum algorithms. We study the coherence dynamics of the evolved states in Simon's quantum algorithm based on Tsallis relative $α$ entropy and $l_{1,p}$ norm. We prove that the coherences of the first register and the second register both rely on the dimension $N$ of the state spaces of the $n$ qubit systems, and increase with the increase of $N$. We show that the oracle operator $O$ does not change the coherence. Moreover, we study the coherence dynamics in the Simon's quantum algorithm and prove that in overall the coherence is in production when $N>4$ and in depletion when $N<4$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16194v1
- Title: Strain-induced modification of spin-optical dynamics in silicon vacancy centers for integrated quantum technologies
- Authors: Maximilian Hollendonner, Fedor Dzmitryevich Hrunski, Daniel Scheller, Kim Ullerich, Shravan Kumar Parthasarathy, Wolfgang Knolle, Maximilian Schober, Mirjam Neubauer, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16194v1  pdf=https://arxiv.org/pdf/2604.16194v1.pdf

Abstract:
Silicon vacancy (VSi) centers in 4H silicon carbide have emerged as a highly promising platform for semiconductor-based quantum technologies, combining excellent spin and optical properties with an industrial-grade, CMOS-compatible material. As these defects are increasingly integrated into practical quantum devices, they inevitably encounter lattice strain. However, while the impact of strain is well documented for other solid-state defects like NV centers in diamond, its specific influence on key VSi spin dynamics such as initialization fidelity and state lifetimes remain largely unexplored. In this work, we address this critical gap by designing fully optical pulse sequences and incorporating the effective spin-3/2 strain Hamiltonian into our analysis. This combined approach allows us to isolate both axial and transverse strain contributions and systematically characterize their effect on the metastable state transition rates. Specifically, we reveal that strain significantly reduces the transition rates from the energetically lowest metastable state to the ground state quartet, leading to decreased photon emission. Supported by first-principles calculations, our findings provide a deeper understanding of VSi spin-strain dynamics, yielding crucial insights for the robust deployment of these centers in realistic, strain-prone environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16202v1
- Title: Squeezing and measurement of a mechanical quadrature via PID feedback
- Authors: Alberto Hijano, Tero T. Heikkilä
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16202v1  pdf=https://arxiv.org/pdf/2604.16202v1.pdf

Abstract:
Proportional-Integral-Derivative (PID) control is used for automatically regulating a measurable quantity to a desired setpoint. It is widely used in different types of classical control electronics. Here, we show how extending the feedback theory in quantum systems to include the derivative and integral parts influences both the transient and steady-state behavior of the amplitude and squeezing of a mechanical quadrature in an optomechanical system. We show that, in contrast to standard proportional feedback, derivative feedback affects both the conditional and unconditional squeezing. Furthermore, we demonstrate how feedback may be employed to drive a mechanical quadrature to track a desired reference signal. Our findings offer new routes for an improved quantum state control and measurement precision.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16209v1
- Title: Towards Ultra-High-Rate Quantum Error Correction with Reconfigurable Atom Arrays
- Authors: Chen Zhao, Casey Duckering, Andi Gu, Nishad Maskara, Hengyun Zhou
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2604.16209v1  pdf=https://arxiv.org/pdf/2604.16209v1.pdf

Abstract:
Quantum error correction is widely believed to be essential for large-scale quantum computation, but the required qubit overhead remains a central challenge. Quantum low-density parity-check codes can substantially reduce this overhead through high-rate encodings, yet finite-size instances with practical logical error rates often achieve encoding rates only around or below $1/10$. Here, building on a recent ultra-high-rate construction by Kasai, we identify new structural conditions on the underlying affine permutation matrices that make encoding rates exceeding $1/2$ compatible with efficient implementation on reconfigurable neutral atom arrays. These conditions define a co-designed family of ultra-high-rate quantum codes that supports efficient syndrome extraction and atom rearrangement under realistic parallel control constraints. Using a hierarchical decoder with high accuracy and good throughput, we study the performance under a circuit-level noise model with $p=0.1\%$, achieving per-logical-per-round error rates of $1.3_{-0.9}^{+3.0} \times 10^{-13}$ with a $[[2304,1156,\leq 14]]$ code and $2.9_{-1.5}^{+3.1} \times 10^{-11}$ with a $[[1152,580,\leq 12]]$ code. These results approach the teraquop regime, highlighting the promise of this code family for practical ultra-high-rate quantum error correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16210v1
- Title: Preparation and detection of quasiparticles for quantum simulations of scattering
- Authors: Mattia Morgavi, Peter Majcen, Marco Rigobello, Simone Montangero, Pietro Silvi
- Categories: quant-ph (primary); quant-ph; hep-lat
- Links: abs=https://arxiv.org/abs/2604.16210v1  pdf=https://arxiv.org/pdf/2604.16210v1.pdf

Abstract:
We introduce a method for the selective preparation and detection of quasiparticle wave packets, based on creation operators that generate dressed, localized excitations on top of interacting vacua of (quasi-)one-dimensional quantum lattice theories. This method exploits maximally localized Wannier functions (MLWFs) constructed from quasiparticle bands at intermediate system sizes, enabling the construction of unitary local dressed creation operators. The algorithm allows for species-resolved wave-packet preparation and detection, enabling the separation of known quasiparticle contributions from unknown resonances. We test this approach with matrix product states (MPS) on pure hardcore Hamiltonian QCD on a ladder lattice, detecting scattering outputs and mass resonances.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16216v1
- Title: A digitally controlled silicon quantum processing unit
- Authors: Members of the HRL Quantum Team, Collaborators, :, Michael Abraham, Edwin Acuna, Tower S. Adams, Moonmoon Akmal, Matthew R. Alfaro, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16216v1  pdf=https://arxiv.org/pdf/2604.16216v1.pdf

Abstract:
Commercially-relevant quantum computers will require large numbers of high-performing qubits that can be manufactured, integrated, and controlled at scale. Silicon exchange-only (EO) qubits are a strong candidate modality due to their control-signal simplicity and compatibility with advanced semiconductor manufacturing, but questions remain around the achievability of sufficiently low noise and a scalable control and wiring solution. Here we introduce a quantum processing unit composed of a custom-designed cryogenic CMOS controller, a novel high-density superconducting ribbon cable, and a low-noise EO qubit device. The quantum chip features a three-rail array of 54 exchange-coupled quantum dots, configurable to host up to 18 EO qubits. We integrate and use these components to demonstrate qubit performance for both single-qubit and entangling operations that advances the EO state of the art by an order of magnitude. We further validate this system by implementing a distance-5 repetition code and a quantum error detecting code then make detailed comparisons with simulations. Our approach facilitates a utility-scale quantum computer with manageable operational and capital requirements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16236v1
- Title: Long-term Performance Analysis of a Commercial QKD Device Under Real-world Deployment Conditions
- Authors: Alisson Tezzin, Gustavo M. Uhdre, Oscar Martins, Sabrina Rufo, Vitor G. A. Carneiro
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16236v1  pdf=https://arxiv.org/pdf/2604.16236v1.pdf

Abstract:
Quantum key distribution (QKD) has reached a commercially viable stage, with several companies offering hardware systems designed for operational deployment. Evaluating the performance of commercial QKD devices under real-world deployment conditions is essential for users seeking to understand the practical limitations and operational reliability of these systems. In this paper, we present a long-term performance analysis of ID Quantique's Clavis XGR deployed within the Rio Quantum Network, in Brazil. Our study provides a detailed characterization of key operational metrics, such as secret key rate, quantum bit error rate (QBER), visibility, and detection counts, mapping their behavior over extended periods of continuous operation. We analyze the system's stability across two distinct optical links: a 40 km indoor spooled fiber and a 3.5 km outdoor deployed underground fiber. Monitored under both unregulated tropical ambient fluctuations and actively controlled thermal stress, our results demonstrate excellent overall baseline resilience, with the system maintaining visibility above 97% and QBER below 1% on average. These findings provide practical insights into the expected behavior and thermal bottlenecks of commercial QKD systems in field deployments, particularly in tropical climates, helping to inform realistic expectations for operational quantum-safe infrastructures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16274v1
- Title: Yttrium ion as a platform for quantum information processing
- Authors: Christopher N. Gilbreth, Dmytro Filin, Marianna S. Safronova, Guanming Lao, Eric R. Hudson
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2604.16274v1  pdf=https://arxiv.org/pdf/2604.16274v1.pdf

Abstract:
Engineering large-scale quantum computers which simultaneously provide high-fidelity quantum operations, low memory errors, low crosstalk, and reasonable resource usage remains an outstanding challenge across quantum computing platforms. In trapped ions, progress has largely focused on alkaline-earth and ytterbium ions, whose simple electronic structures facilitate control over their internal state. Here we investigate singly-ionized yttrium ($^{89}\mathrm{Y}^+$), a two-valence-electron ion whose ground-state manifold hosts a nuclear-spin qubit and which also features a variety of low-lying metastable manifolds, for applications in quantum information processing. Because experimental data are limited, we perform high-resolution laser-induced fluorescence spectroscopy to measure the hyperfine structure of several low-lying levels, and carry out comprehensive electronic structure calculations to determine lifetimes, transition matrix elements, and hyperfine coefficients for manifolds addressable with visible, near-visible, or infrared wavelengths. Using these results, we analyze schemes for qubit storage, initialization, readout, leakage mitigation, and single- and two-qubit gates. These results position $^{89}\mathrm{Y}^+$ as a uniquely capable next-generation trapped-ion qubit, combining field-insensitive nuclear-spin or clock-qubit storage with spectrally isolated transitions for operations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16276v1
- Title: Aziz and Howl's Gravity-Induced Entanglement Channel is Essentially Classical Mechanics
- Authors: Hanyu Xue, Ziqian Tang, Chen Yang, Zizhao Han, Zikuan Kan, Yulong Liu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16276v1  pdf=https://arxiv.org/pdf/2604.16276v1.pdf

Abstract:
Aziz and Howl argued that a classical gravitational field can generate quantum entanglement through a quantum-field-theoretic channel mediated by virtual matter propagation. However, their claimed channel is more naturally and accurately understood as semiclassical wavepacket motion in an external gravitational field, rather than as a distinctively quantum-field-theoretic entangling effect. Moreover, the result of their perturbative computation is incorrectly magnified: they selected a discontinuous wavefunction with infinite kinetic energy as the initial state and simultaneously treated it as stationary. Once a correct treatment using Gaussian wavepacket is adapted, the resulting effect will be negligibly small.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16283v1
- Title: Boson correlations are spurious for classical states
- Authors: Daniel E. Salazar, Fabrice P. Laussy
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; physics.optics
- Links: abs=https://arxiv.org/abs/2604.16283v1  pdf=https://arxiv.org/pdf/2604.16283v1.pdf

Abstract:
We show that boson correlations from quantum states with a Glauber-Sudarshan representation of their density matrix which provides a well-behaved probability distribution -- including coherent states, thermal states, and all states that can be deemed classical -- are a manifestation of the Simpson paradox: they are spurious correlations from statistical (ensemble) averages over uncorrelated measurements made in varying geometries, due to a process of symmetry-breaking as a confounding factor. Bosonic correlations encoded by the wavefunction appear to be formed in the geometry assumed, which however is not that of the statistical ensemble but varies from realization to realization. This calls to distinguish between quantum and statistical averages and sheds new understandings on the fundamental problems of nonclassicality and quantum advantage.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16285v1
- Title: How to unitarily map between any two pure states with a single closed-form exponential
- Authors: Peter T. J. Bradshaw, Marcus Gouveia, Jonte R. Hance
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2604.16285v1  pdf=https://arxiv.org/pdf/2604.16285v1.pdf

Abstract:
It is well-known that any two pure quantum states (in the same Hilbert space) can be mapped to any other using unitary transformations. However, previous approaches to this problem required two explicit bases for the Hilbert space, one each for the initial and target states, and thus their complexity necessarily scales with the dimension of the Hilbert space. In this Letter, we show how to utilize novel algebraic methods to construct a closed-form exponential unitary transformation which achieves this in general, using only a single unitary generator. This construction is independent of any bases and agnostic to the dimension of the Hilbert space. We highlight the usefulness of this tool for studying relationships between systems of pure states in quantum information theory, as well in elementary analyses of quantum circuits and unitary operators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16292v1
- Title: Fast, High-Fidelity Erasure Detection of Dual-Rail Qubits with Symmetrically Coupled Readout
- Authors: Jimmy Shih-Chun Hung, Arbel Haim, Mouktik Raha, Gihwan Kim, Ziwen Huang, Ming-Han Chou, Mitch D'Ewart, Erik Davis, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.16292v1  pdf=https://arxiv.org/pdf/2604.16292v1.pdf

Abstract:
Erasure qubits are a promising platform for implementing hardware-efficient quantum error correction. Realizing the error-correction advantages of this encoding requires frequent mid-circuit erasure checks that are fast, high-fidelity, and scalable. Here, we realize erasure detection with a hardware-efficient circuit consisting of a single readout resonator dispersively and symmetrically coupled to both transmons of a dual-rail qubit. We use this circuit to demonstrate single-shot erasure detection in 384 ns with minimal impact on the dual-rail logical manifold, achieving a residual error per check of $6.0(2) \times 10^{-4}$, with only $8(3) \times 10^{-5}$ induced dephasing per check, and an erasure error per check of $2.54(1)\times 10^{-2}$. The high degree of matched dispersive readout coupling ($χ$-matching) within the dual-rail qubit code space also allows us to realize a new modality: time-continuous erasure detection performed in parallel with single-qubit gates. Here we achieve a median $7.2 \times 10^{-5}$ error per gate with $< 1 \times 10^{-5}$ error induced by erasure detection. This demonstrates a reduction in erasure detection overhead as well as a crucial ingredient for soft information quantum error correction. Together, these results establish symmetrically coupled dispersive readout as a fast, hardware-efficient, and scalable component for erasure-based quantum error correction using transmon dual-rail qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2603.23651v1
- Title: Quantum Graph Theory by Example
- Authors: Gian Luca Spitzer, Ion Nechita
- Categories: math.OA (primary); math.OA; math-ph; math.QA; quant-ph
- Links: abs=https://arxiv.org/abs/2603.23651v1  pdf=https://arxiv.org/pdf/2603.23651v1.pdf

Abstract:
Quantum graphs have been introduced by Duan, Severini, and Winter to describe the zero-error behaviour of quantum channels. Since then, quantum graph theory has become a field of study in its own right. A substantial source of difficulty in working with quantum graphs compared to classical graphs stems from the fact that they are no longer discrete objects. This makes it generally difficult to construct insightful, non-trivial examples. We present a collection of non-trivial quantum graphs that can be thought of in discrete terms, and that can be expressed in the diagrammatic formalism introduced by Musto, Reutter, and Verdon. The examples arise as the quantum graphs acted on by increasingly smaller classical matrix groups, and are parametrised by triples of matrices $(A, B, C)$. The parametrisation reveals a clean decomposition of quantum graph structure into classical and genuinely quantum components: $A$ and $C$ are described by a classical weighted graph called the strange graph, while $B$ provides a purely quantum contribution with no classical analogue. Based on this model, we give exact formulas or establish bounds for quantum graph parameters, such as the number of connected components, the chromatic number, the independence number, and the clique number. Our results provide the first large, parametric families of quantum graphs for which standard graph parameters can be computed analytically.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15417v1
- Title: Ultrastrong Coupling Signatures in Photon Statistics from Terahertz Higgs-Polaritons
- Authors: Spenser Talkington, Benjamin Kass, Martin Claassen
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.supr-con; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15417v1  pdf=https://arxiv.org/pdf/2604.15417v1.pdf

Abstract:
The ultrastrong coupling regime of cavity photons and quantum materials has emerged as a pathway to modify materials properties, however definitive signatures of ultrastrong coupling remain elusive. Focusing on the quantum photon statistics of light transmitted through a cavity-embedded superconductor, we show that a two-photon Higgs polariton at strong coupling realizes a photonic nonlinearity at the single terahertz photon level. We find that as light-matter coupling increases, the photon statistics show pronounced changes due to the formation of a hybrid photon-matter dark-cavity state with finite photon occupancy, producing testable signatures of ultrastrong coupling. We derive a non-Markovian input output relation and study the cavity-embedded superconductor 2H-NbSe2 as it approaches ultrastrong light-matter coupling. Our results reveal a diagnostic for ultrastrong coupling in the two-photon coincidence statistics that is absent in total counts.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15419v1
- Title: Singlet-only always-on gapless exchange (SAGE) spin qubits: Charge noise effects and two-qubit gates
- Authors: Nathan L. Foulk, Katharina Laubscher, Silas Hoffman, Sankar Das Sarma
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15419v1  pdf=https://arxiv.org/pdf/2604.15419v1.pdf

Abstract:
Singlet-only always-on gapless exchange (SAGE) spin qubits are an alternative type of exchange-only (EO) qubits that encode a single qubit in the spins of four electrons located in four tunnel-coupled quantum dots. While conventional EO qubits are susceptible to local magnetic field gradients caused by local nuclear environments and $g$-factor variations, the SAGE qubit subspace is inherently protected from magnetic-gradient-induced Pauli errors by virtue of the singlet-only encoding, which is invariant under magnetic field gradients, and the always-on exchange couplings, which provide energetic leakage protection. However, the always-on operation simultaneously increases the qubit's sensitivity to charge noise. Here, starting from a Hubbard model describing the underlying electronic structure of the coupled quantum dots, we characterize the performance of SAGE qubits in the presence of $1/f$ charge noise that induces fluctuations in both the dot chemical potentials and the interdot tunnel couplings. We calculate SAGE idle coherence times and show that realistic CPMG-like pulse sequences can be used to significantly extend SAGE single-qubit coherence times for experimentally relevant charge noise strengths. We likewise study the fidelity of SAGE two-qubit gates in the presence of charge and magnetic noise and again propose a simple refocusing strategy to mitigate the noise, while increased ramp times of the entangling pulse suppress leakage into noncomputational states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15445v1
- Title: Universal Description of Decoherence in Scale-Invariant Environments
- Authors: Carlos Argüelles, Gabriela Barenboim, Gonzalo Herrera, Tanvi Krishnan, Héctor Sanchis
- Categories: hep-ph (primary); hep-ph; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15445v1  pdf=https://arxiv.org/pdf/2604.15445v1.pdf

Abstract:
When a quantum system couples to a scale-invariant environment, what form must its decoherence take? We prove that the answer is unique: under locality, Lorentz invariance, unitarity, and continuous scale invariance, the effect of any such environment is mathematically equivalent to that of an \emph{unparticle bath} -- a scale-invariant continuum of states -- characterized entirely by the scaling dimension $d_{\mathcal{U}}$ of the coupled operator. This is not a modelling choice but a consequence of conformal symmetry. All decoherence and dissipation exponents are fixed by $d_{\mathcal{U}}$ through exact consistency relations, providing falsifiable predictions independent of microscopic details. We validate the framework using multi-channel transport data from the unitary Fermi gas, where two genuinely independent observables yield a consistent $d_{\mathcal{U}} = 7/4$. We further show that quantum Ising criticality, inflationary cosmology, and high-energy astrophysical neutrinos -- spanning more than 25 orders of magnitude in energy -- are unified as specific realizations of the same structure. A decoherence phase transition at $d_{\mathcal{U}} = 5/2$, where quantum coherence is \emph{protected} rather thandestroyed at long times, is a qualitative prediction inaccessible to any memoryless dynamical description.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15550v1
- Title: Incoherence-assisted mode excitation in non-Hermitian resonant systems
- Authors: Amin Hashemi, Vinzenz Zimmermann, Armando Perez-Leija, Andrea Blanco-Redondo
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15550v1  pdf=https://arxiv.org/pdf/2604.15550v1.pdf

Abstract:
We introduce and experimentally demonstrate an approach for selective mode excitation in non-Hermitian resonant systems using incoherent light. This method eliminates the need for precise phase control that is often required in coherent excitation schemes. Using this technique on a silicon photonic platform with coupled ring resonators, we successfully excite the topological edge state of a non-Hermitian Su-Schrieffer-Heeger (SSH) model. Our work shows that incoherence-assisted excitation is a robust and passive strategy for topological state preparation, which broadens the scope of non-Hermitian topological photonics thereby providing a practical and experimentally viable tool for selective mode excitation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15645v1
- Title: PINNACLE: An Open-Source Computational Framework for Classical and Quantum PINNs
- Authors: Shimon Pisnoy, Hemanth Chandravamsi, Ziv Chen, Aaron Goldgewert, Gal Shaviner, Boris Shragner, Steven H. Frankel
- Categories: cs.LG (primary); cs.LG; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15645v1  pdf=https://arxiv.org/pdf/2604.15645v1.pdf

Abstract:
We present PINNACLE, an open-source computational framework for physics-informed neural networks (PINNs) that integrates modern training strategies, multi-GPU acceleration, and hybrid quantum-classical architectures within a unified modular workflow. The framework enables systematic evaluation of PINN performance across benchmark problems including 1D hyperbolic conservation laws, incompressible flows, and electromagnetic wave propagation. It supports a range of architectural and training enhancements, including Fourier feature embeddings, random weight factorization, strict boundary condition enforcement, adaptive loss balancing, curriculum training, and second-order optimization strategies, with extensibility to additional methods. We provide a comprehensive benchmark study quantifying the impact of these methods on convergence, accuracy, and computational cost, and analyze distributed data parallel scaling in terms of runtime and memory efficiency. In addition, we extend the framework to hybrid quantum-classical PINNs and derive a formal estimate for circuit-evaluation complexity under parameter-shift differentiation. Results highlight the sensitivity of PINNs to architectural and training choices, confirm their high computational cost relative to classical solvers, and identify regimes where hybrid quantum models offer improved parameter efficiency. PINNACLE provides a foundation for benchmarking physics-informed learning methods and guiding future developments through quantitative assessment of their trade-offs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15653v1
- Title: Growth of quantum dots by droplet etching epitaxy in molecular beam epitaxy: theory, practice, and review
- Authors: Declan Gossink, Undurti S. Sainadh, Glenn S. Solomon
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15653v1  pdf=https://arxiv.org/pdf/2604.15653v1.pdf

Abstract:
GaAs quantum dots grown by droplet etching epitaxy are high-quality solid-state sources of quantum light. Despite implementation in devices that exploit quantum phenomenon, a comprehensive review on the crystal growth of quantum dots grown by droplet etching epitaxy is absent, unlike for other quantum dot growth techniques such as the related droplet epitaxy method or Stranski-Krastanov growth of InAs quantum dots. This review presents a detailed overview of the droplet etching epitaxy growth technique in the molecular beam epitaxy environment, with emphasis on the growth parameters necessary to realize high-quality quantum dots. We systematically cover the three main phases of droplet etching epitaxy - droplet deposition, droplet etching, and nanohole regrowth - and relate experimental results to theories on crystal growth. The review concludes with an introduction to GaAs quantum dot photoluminescence and the extension of droplet etching epitaxy beyond the AlGaAs/GaAs material system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15775v1
- Title: Federated Learning with Quantum Enhanced LSTM for Applications in High Energy Physics
- Authors: Abhishek Sawaika, Durga Pritam Suggisetti, Udaya Parampalli, Rajkumar Buyya
- Categories: cs.LG (primary); cs.LG; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15775v1  pdf=https://arxiv.org/pdf/2604.15775v1.pdf

Abstract:
Learning with large-scale datasets and information-critical applications, such as in High Energy Physics (HEP), demands highly complex, large-scale models that are both robust and accurate. To tackle this issue and cater to the learning requirements, we envision using a federated learning framework with a quantum-enhanced model. Specifically, we design a hybrid quantum-classical long-shot-term-memory model (QLSTM) for local training at distributed nodes. It combines the representative power of quantum models in understanding complex relationships within the feature space, and an LSTM-based model to learn necessary correlations across data points. Given the computing limitations and unprecedented cost of current stand-alone noisy-intermediate quantum (NISQ) devices, we propose to use a federated learning setup, where the learning load can be distributed to local servers as per design and data availability. We demonstrate the benefits of such a design on a classification task for the Supersymmetry(SUSY) dataset, having 5M rows. Our experiments indicate that the performance of this design is not only better that some of the existing work using variational quantum circuit (VQC) based quantum machine learning (QML) techniques, but is also comparable ($Δ\sim \pm 1\%$) to that of classical deep-learning benchmarks. An important observation from this study is that the designed framework has $<$300 parameters and only needs 20K data points to give a comparable performance. Which also turns out to be a 100$\times$ improvement than the compared baseline models. This shows an improved learning capability of the proposed framework with minimal data and resource requirements, due to the joint model with an LSTM based architecture and a quantum enhanced VQC.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15790v1
- Title: Holographic Stirling engines and the route to Carnot efficiency
- Authors: Nikesh Lilani, Manus R. Visser
- Categories: hep-th (primary); hep-th; cond-mat.quant-gas; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15790v1  pdf=https://arxiv.org/pdf/2604.15790v1.pdf

Abstract:
We compute the efficiency of the reversible Stirling engine, with and without regeneration, for a broad class of working substances including Van der Waals fluids, quantum ideal gases (Bose and Fermi), Bose-Einstein condensates, thermal conformal field theories (CFTs), and holographic CFTs. Regeneration acts as an internal heat recycling mechanism that enhances efficiency by reducing the net heat exchange with external reservoirs. For regenerative Stirling cycles, a central role is played by the intrinsic heat mismatch between the two isochoric branches, which controls the deviation of the efficiency from the Carnot bound and quantifies the extent to which internally exchanged heat can be perfectly recycled. We identify a general sufficient condition for attaining Carnot efficiency, namely that the fixed-volume heat capacity is independent of the volume, ensuring that the isochoric heat mismatch vanishes. While this condition is satisfied for classical ideal gases and Van der Waals fluids, it is violated for quantum ideal gases and CFT working substances. For thermal CFT states dual to AdS-Schwarzschild and AdS-Reissner-Nordström black holes we obtain exact expressions for the Stirling efficiency. In the fixed-potential ensemble, we show that the Stirling efficiency asymptotes to the Carnot value in the large-potential limit, with a faster approach in the presence of regeneration.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15820v1
- Title: Hilbert Space Fragmentation and Gauge Symmetry
- Authors: Thea Budde, Marina Kristć Marinković, Joao C. Pinto Barros
- Categories: hep-lat (primary); hep-lat; cond-mat.stat-mech; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15820v1  pdf=https://arxiv.org/pdf/2604.15820v1.pdf

Abstract:
The Hamiltonian formulation of lattice gauge theories plays a central role in quantum simulations of gauge theories, and understanding their spectrum and other properties is expected to become crucial in the upcoming years. The relevant Hamiltonians in this framework possess local symmetry at each lattice site and may exhibit higher-form symmetries. There are then an exponentially large number of dynamically disconnected symmetry sectors, most of which are not translation-invariant. An exponential number of dynamically disconnected sectors, i.e., Hilbert space fragmentation, can also occur in systems in which no such symmetries have been identified. In this contribution, we describe an emergent gauge symmetry that is valid only in a subset of sectors of the fragmented $S=1$ dipole-conserving spin chain. These non-invertible symmetries can label exponentially many of the model's sectors. Simulating this Hamiltonian, which is not gauge-invariant, yields an exact quantum simulation of a gauge theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15858v1
- Title: Module Lattice Security (Part I): Unconditional Verification of Weber's Conjecture for $k \le 12$
- Authors: Ming-Xing Luo
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15858v1  pdf=https://arxiv.org/pdf/2604.15858v1.pdf

Abstract:
Weber's conjecture (1886) governs three aspects of lattice-based cryptography: the solvability of the Principal Ideal Problem, the freeness of modules over rings of integers, and the tightness of worst-case-to-average-case reductions in Ring-LWE (R-LWE) and Module-LWE (MLWE). Existing verifications for $k \ge 9$ rely on Generalized Riemann Hypothesis (GRH). In this paper, we present the first unconditional proof for $k \le 12$. Our method combines the Fukuda-Komatsu computational sieve, inductive structure of the cyclotomic $\mathbb{Z}_2$-tower, and Herbrand's theorem.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15888v1
- Title: Enhancing Neural-Network Variational Monte Carlo through Basis Transformation
- Authors: Zhixuan Liu, Dongheng Qian, Jing Wang
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.dis-nn; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15888v1  pdf=https://arxiv.org/pdf/2604.15888v1.pdf

Abstract:
Neural-network variational Monte Carlo (NNVMC) has emerged as a powerful tool for solving quantum many-body problems, yet systematic pathways for improving its accuracy remain largely heuristic. Here, we introduce a physically motivated basis transformation for NNVMC that enhances variational expressivity without increasing the complexity of the neural-network ansatz itself. By formulating the many-body wave function in a Gaussian basis, we introduce a single learnable locality parameter, $α$, that reshapes the target ground state into a more learnable representation. This approach introduces minimal computational overhead and can be readily combined with existing neural-network architectures. Using the three-dimensional homogeneous electron gas as a benchmark, we show that the optimized basis transformation consistently lowers the variational energy for both FermiNet and message-passing neural-network architectures. Notably, for the latter, it enables a more precise determination of the Fermi liquid to Wigner crystal phase transition. More broadly, our results highlight basis transformation as a new route to improving NNVMC in continuous space, showing that accuracy can be enhanced not only by refining the ansatz but also by making the target ground state easier to represent.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.15924v1
- Title: Ultrafast Current Switching from Quantum Geometry in Semimetals
- Authors: Youngjae Kim, Sejoong Kim, Jun-Won Rhim
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.mes-hall; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2604.15924v1  pdf=https://arxiv.org/pdf/2604.15924v1.pdf

Abstract:
Technological progress towards next-generation electronics critically relies on achieving faster switching with reduced energy consumption. Because device operation speeds are fundamentally constrained by the intrinsic properties of constituent materials, identifying systems with inherently superior switching capabilities is essential. Here, we propose that semimetallic systems characterized by non-trivial quantum geometry, including quadratic band-touching semimetals and singular flat bands, can serve as a promising platform for ultrafast switching at voltages compatible with modern electronics. We show that, in such quantum geometric semimetals, an electric current is generated instantaneously upon application of a moderate external electric field, reaching its steady-state value. As a consequence, the current exhibits rapid and stable on-off switching behaviour under periodic optical pulse trains, demonstrating robustness under experimentally feasible conditions. In terms of switching speed, this quantum geometric semimetal outperforms conventional metals, semiconductors, and graphene. We identify the microscopic origin of this behaviour as interband coupling governed by the Hilbert-Schmidt quantum distance, together with a finite density of states at the band-touching point. This mechanism further leads to a universal classification of conductivity for both gapless and gapped quantum geometric semimetals. Finally, first-principles calculations suggest realistic material platforms, including bilayer graphene, cyclic graphene, monolayer bismuth and V3F8-in which the predicted instantaneous current switching can be directly realized, further supported by time-dependent density functional theory simulations performed for representative systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16102v1
- Title: Exact Steady State of a One-end Driven XXZ Spin Chain with Boundary Field
- Authors: V. Popkov, T. Prosen
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2604.16102v1  pdf=https://arxiv.org/pdf/2604.16102v1.pdf

Abstract:
We find an exact nonequilibrium steady state of an open dissipatively driven XXZ spin-1/2 chain with source or sink spin bath at one end and an arbitrary boundary field at the other end.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16137v1
- Title: Observation of Strong-to-Weak Spontaneous Symmetry Breaking in a Dephased Fermi Gas
- Authors: Si Wang, Thomas G. Kiely, Dorothee Tell, Johannes Obermeyer, Marnix Barendregt, Petar Bojović, Philipp M. Preiss, Abhijat Sarma, et al.
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2604.16137v1  pdf=https://arxiv.org/pdf/2604.16137v1.pdf

Abstract:
Symmetry-based classification of quantum phases of matter is one of the most foundational organizing principles in physics; however, an analogous framework for mixed, decohered quantum states has only begun to emerge. A central new concept is strong-to-weak spontaneous symmetry breaking (SW-SSB), a sharp transition in mixed quantum states that is invisible to any observable linear in the density matrix and that has since been predicted across a broad class of open and monitored quantum systems. It also provides a unifying language for phenomena as disparate as the decodability of topological quantum memories and the emergence of classical hydrodynamics from decohered quantum dynamics. Here we report the first experimental observation of SW-SSB, in dephased single-component fermionic matter imaged by a quantum gas microscope. A quantum-classical estimator built on a machine-learned Gaussian reference state gives direct access to the nonlinear Rényi-1 and Rényi-2 correlators that diagnose SW-SSB, and reveals long-range Rényi order in the dephased Fermi liquid. Adding a commensurate superlattice drives the underlying fermions through a metal-to-insulator transition that, after full dephasing, manifests as a sharp SW-SSB phase transition. Our results uncover the symmetry principle behind information-theoretic transitions in open quantum systems, and extend Landau's symmetry paradigm into the regime of real, decohering quantum devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16179v1
- Title: Quantum-Inspired Simulation of 2D Turbulent Rayleigh-Bénard Convection
- Authors: Nis-Luca van Hülst, Mario Guillaume Cecile, Hai-Yen Van, Tomohiro Hashizume, Eugene de Villiers, Dieter Jaksch
- Categories: physics.flu-dyn (primary); physics.flu-dyn; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2604.16179v1  pdf=https://arxiv.org/pdf/2604.16179v1.pdf

Abstract:
Turbulent thermal convection governs heat transport in systems ranging from stellar interiors to industrial heat exchangers. Two-dimensional Rayleigh-Bénard convection serves as a paradigm for these flows, reproducing key features such as thin boundary layers, large-scale circulation, and sustained plume dynamics. While Matrix Product State (MPS) methods have demonstrated significant compression of isothermal turbulent fields, their application to buoyancy-driven flows with active thermal coupling has remained unexplored. We apply MPS to two-dimensional Rayleigh-Bénard convection with dynamical simulations up to $\mathrm{Ra} = 10^{10}$. An a priori decomposition of DNS snapshots up to $\mathrm{Ra} = 10^{11}$ shows that the bond dimension $χ$ required to represent the flow fields grows without saturation, in contrast to the plateauing of $χ$ reported for velocity fields in isothermal 2D turbulence. Crucially, however, dynamical simulations solving the governing equations directly in the compressed MPS format at fixed $χ$ show that the $χ$ required to recover statistical observables, such as the Nusselt number, scales significantly more favorably with $\mathrm{Ra}$ than the a priori complexity suggests. At $\mathrm{Ra} = 10^{10}$, a relative error of $1.8\%$ in the mean Nusselt number is achieved with a nearly 9-fold reduction in degrees of freedom, using a $χ$ comparable to that required at $\mathrm{Ra} = 10^{9}$. Spectral analysis confirms the progressive recovery of spatial and temporal scales with increasing $χ$. These findings establish MPS as a scalable tool for simulating thermally driven turbulence, suggesting the method may remain viable for investigations of the ultimate regime at substantially higher $\mathrm{Ra}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16218v1
- Title: Quantum Tomography and Entanglement in Semi-Leptonic $h\to VV^*$ Decays at Higher Orders
- Authors: Dorival Gonçalves, Ajay Kaladharan, Alberto Navarro
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2604.16218v1  pdf=https://arxiv.org/pdf/2604.16218v1.pdf

Abstract:
Angular correlations in Higgs decays to electroweak gauge bosons, $h \to ZZ^*, WW^*$, provide a powerful probe of both new physics effects and quantum information observables. We present a systematic study of semi-leptonic decays $h \to V V^* \to \ell^+\ell^- q\bar{q}$ and $\ell^\pm ν_\ell q\bar{q}'$, including finite final state fermion masses, NLO QCD, and NLO electroweak corrections. We show that finite final state quark masses can induce effects that go beyond the two-qutrit description in more inclusive regimes, while remaining controllable with suitable kinematic selections. QCD corrections lead to modest percent-level shifts, whereas electroweak corrections can significantly modify the angular structure, particularly in the $h\to ZZ^*$ channels. We assess the impact of these effects on the reconstructed density matrix and entanglement measures, finding that, while they modify the angular observables, semi-leptonic channels retain an effective two-qutrit description.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.16290v1
- Title: Renormalised thermodynamics for Bose gases from low to critical temperatures
- Authors: Michael H. Heinrich, Alexander Wowchik, Jürgen Berges
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2604.16290v1  pdf=https://arxiv.org/pdf/2604.16290v1.pdf

Abstract:
We compute thermodynamic properties of dilute Bose gases using non-perturbative approximations of the two-particle irreducible (2PI) effective action. It is shown how to systematically renormalise the self-consistent descriptions beyond conventional Gaussian approximations such as Hartree-Fock-Bogoliubov theory. This allows us to determine the condensate depletion from low to high temperatures, including its critical behaviour at the phase transition. While the universal anomalous dimension at criticality is vanishing for Gaussian approximations, we determine its non-zero value at next-to-leading order of a self-consistent expansion in the number of field components.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2403.03284v2
- Title: Quantum communication networks with defects in silicon carbide
- Authors: Philipp Sohr, Philipp Koller, Sebastian Ecker, Matthias Fink, Thomas Scheidl, Rupert Ursin, Muhammad Junaid Arshad, Cristian Bonato, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2403.03284v2  pdf=https://arxiv.org/pdf/2403.03284v2.pdf

Abstract:
Quantum communication promises unprecedented capabilities enabled by the transmission of quantum states of light. However, current implementations face severe distance limitations due to photon loss. Silicon carbide (SiC) defects have emerged as a promising quantum device platform, offering strong optical transitions, long spin coherence lifetimes and the opportunity for integration with semiconductor devices. Some defects with optical transitions in the telecom range have been identified, allowing to interface with fiber networks without the need for wavelength conversion. These unique properties make SiC an attractive platform for the implementation of quantum nodes for quantum communication networks. We provide an overview of the most prominent defects in SiC and their implementation in spin-photon interfaces. Furthermore, we model an exemplary, memory-enhanced quantum communication protocol in order to extract the parameters required to surpass a direct point-to-point link performance. Based on these insights, we summarize the key steps required towards the deployment of SiC devices in large-scale quantum communication networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2403.12691v3
- Title: Efficient thermalization and universal quantum computing with quantum Gibbs samplers
- Authors: Cambyse Rouzé, Daniel Stilck França, Álvaro M. Alhambra
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2403.12691v3  pdf=https://arxiv.org/pdf/2403.12691v3.pdf

Abstract:
The preparation of thermal states of matter is a crucial task in quantum simulation. In this work, we prove that a recently introduced, efficiently implementable dissipative evolution thermalizes to the Gibbs state in time scaling polynomially with system size at high enough temperatures for any Hamiltonian that satisfies a Lieb-Robinson bound, such as local Hamiltonians on a lattice. Furthermore, we show the efficient adiabatic preparation of the associated purifications or ``thermofield double'' states. These results establish the efficient preparation of high-temperature Gibbs states and their purifications. In the low-temperature regime, we show that implementing this family of dissipative evolutions for inverse temperatures polynomial in the system's size is computationally equivalent to polynomial time quantum computations. On a technical level, for high temperatures, our proof makes use of the mapping of the generator of the evolution into a Hamiltonian, and then connecting its convergence to that of the infinite temperature limit. For low temperature, we instead perform a perturbation at zero temperature and resort to circuit-to-Hamiltonian mappings akin to the proof of universality of quantum adiabatic computing. Taken together, our results show that a family of quasi-local dissipative evolutions efficiently prepares a large class of quantum many-body states of interest, and has the potential to mirror the success of classical Monte Carlo methods for quantum many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2403.18927v3
- Title: Optimal Coherent Quantum Phase Estimation via Tapering
- Authors: Dhrumil Patel, Shi Jie Samuel Tan, Yigit Subasi, Andrew T. Sornborger
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2403.18927v3  pdf=https://arxiv.org/pdf/2403.18927v3.pdf

Abstract:
Due to its significance as a subroutine, in this work, we consider the coherent version of the quantum phase estimation problem, where given an arbitrary input state and black-box access to unitaries $U$ and controlled-$U$, the goal is to estimate the phases of $U$ in superposition. Most existing phase estimation algorithms involve intermediary measurements that disrupt coherence. Only a couple of algorithms, including the standard quantum phase estimation algorithm, consider this coherent setting. However, the standard algorithm only succeeds with a constant probability. To boost this success probability, one can employ the coherent median technique, resulting in an algorithm with asymptotically optimal query complexity (the total number of calls to $U$ and controlled-$U$). However, this coherent median technique requires a large number of ancilla qubits and a computationally expensive quantum sorting network.   To address this, in this work, we propose an improved version of the standard algorithm called the tapered quantum phase estimation (tQPE) algorithm, which leverages tapering (or window) functions commonly used in classical signal processing. Our algorithm achieves the asymptotically optimal query complexity without requiring the expensive coherent median technique to boost success probability. Moreover, we find the absolutely optimal taper - not only in the asymptotic scaling but in terms of exact performance. We provide an efficiently preparable ancilla state based on an approximation of the optimal taper, which incurs at most a factor-of-two increase in the probability of error, thereby maintaining near-optimal performance in practice. In the appendices, we give an explicit construction of the taper state preparation circuit. Finally, we derive an error bound for coherent QPE when the phase estimate is used as a control and subsequently uncomputed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2406.16488v2
- Title: All-optical production of Bose-Einstein condensates with 2 Hz repetition rate
- Authors: Mareike Hetzel, Martin Quensen, Jan Simon Haase, Carsten Klempt
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2406.16488v2  pdf=https://arxiv.org/pdf/2406.16488v2.pdf

Abstract:
Bose-Einstein condensates (BECs) of neutral atoms constitute an important quantum system for fundamental research and precision metrology. Many applications require short preparation times of BECs, for example, for optimized data acquisition rates in scientific applications, and reduced dead times and improved bandwidths for atomic quantum sensors. Here, we report on the generation of rubidium BECs with a repetition rate of more than 2 Hz. The system relies on forced evaporation in a dynamically adjusted optical potential, which is created by the spatial modulation of laser beams. Our system provides a versatile source of the ubiquitous rubidium BECs, and promotes their exploitation for high-precision atom interferometers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2407.19801v5
- Title: Elastic scattering of twisted electrons by CO$_2$ molecules at high energies
- Authors: Raul Sheldon Pinto, Rakesh Choubisa
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2407.19801v5  pdf=https://arxiv.org/pdf/2407.19801v5.pdf

Abstract:
Elastic scattering of a twisted (Bessel) electron beam by CO$_2$ molecules is studied theoretically at high energies. The molecule's structure is optimized using coupled cluster theory and density functional theory with correlation-consistent and Pople basis sets. Coulomb potentials are used in the static approximation. The differential and total scattering cross-sections are computed in the first Born approximation. All cross-sections are orientation-averaged using a passive rotational averaging technique. The scattering is studied by the impact of the twisted beam with topological charges in the range $m_l$ = 1 and $m_l$ = 20. The cross sections are, in addition, averaged over the target's impact parameters, which accounts for the cross sections of a large distribution of CO$_2$ molecules. Finally, the molecule's total cross-section by plane waves and twisted beams is reported. The proposed methodology can be applied to study any polyatomic molecule, regardless of its structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2410.01252v2
- Title: Resource-efficient equivariant quantum convolutional neural networks
- Authors: Koki Chinzei, Quoc Hoan Tran, Yasuhiro Endo, Hirotaka Oshima
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2410.01252v2  pdf=https://arxiv.org/pdf/2410.01252v2.pdf

Abstract:
Equivariant quantum neural networks (QNNs) are promising variational models that exploit symmetries to improve machine learning capabilities. Despite theoretical developments in equivariant QNNs, their implementation on near-term quantum devices remains challenging due to limited computational resources. This study proposes a resource-efficient model of equivariant quantum convolutional neural networks (QCNNs) called equivariant split-parallelizing QCNN (sp-QCNN). Using a group-theoretical approach, we encode general symmetries into our model beyond the translational symmetry addressed by previous sp-QCNNs. We achieve this by splitting the circuit at the pooling layer while preserving symmetry. This splitting structure effectively parallelizes QCNNs to improve measurement efficiency in estimating the expectation value of an observable and its gradient by order of the number of qubits. Our model also exhibits high trainability and generalization performance, including the absence of barren plateaus. Numerical experiments demonstrate that the equivariant sp-QCNN can be trained and generalized with fewer measurement resources than a conventional equivariant QCNN in a noisy quantum data classification task. Our results contribute to the advancement of practical quantum machine learning algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2410.10194v2
- Title: Wire Codes
- Authors: Nouédyn Baspin, Dominic Williamson
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2410.10194v2  pdf=https://arxiv.org/pdf/2410.10194v2.pdf

Abstract:
Quantum information is fragile and must be protected by a quantum error-correcting code for large-scale practical applications. Recently, highly efficient quantum codes have been discovered which require a high degree of spatial connectivity. This raises the question of how to realize these codes with minimal overhead under physical hardware connectivity constraints. Here, we introduce a general recipe to transform any quantum stabilizer code into a subsystem code that has local interactions, with weight and degree three, on a given graph. We call the subsystem codes produced by our recipe wire codes, and their code parameters depend on the input code and the given graph. Wire codes can be adapted to have a local implementation on any graph that supports a low-density embedding of the input Tanner graph, with an overhead that depends on the embedding. In particular, applying our results to a stabilizer code and a subdivision of its own Tanner graph, yields a quantum weight reduction procedure with a multiplicative qubit overhead and distance reduction that are linear in the input check degree and weight, respectively. Applying our results to hypercubic lattices leads to a construction of local subsystem codes with optimal scaling code parameters in any fixed spatial dimension. Similarly, applying our results to families of expanding graphs leads to local codes on these graphs with code parameters that depend on the degree of expansion. Our results constitute a general method to construct low-overhead subsystem codes on general graphs, which can be applied to adapt highly efficient quantum error correction procedures to hardware with restricted connectivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2504.05289v4
- Title: Direct Measurement of the Singlet Lifetime and Photoexcitation Behavior of the Boron Vacancy Center in Hexagonal Boron Nitride
- Authors: Richard A. Escalante, Andrew J. Beling, Daniel G. Ang, Niko R. Reed, Justin J. Welter, John W. Blanchard, Cecilia Campos, Edwin Coronel, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.05289v4  pdf=https://arxiv.org/pdf/2504.05289v4.pdf

Abstract:
Optically active spin defects in van der Waals (vdW) materials are a promising platform for quantum sensing, potentially enabling shorter standoff distances than defects in diamond and thus improved measurement signal-to-noise ratio (SNR) and spatial resolution. The most studied such defect is the negatively charged boron vacancy center ($V^{-}_{B}$) in hexagonal boron nitride (hBN), yet many of its electronic and spin transition rates and branching ratios remain unknown. Here, we use time-resolved photoluminescence (PL) measurements with a nanosecond rise-time 515 nm laser to directly measure the singlet state lifetime of a $V^{-}_{B}$ ensemble in neutron-irradiated, sub-micron flakes of hBN. We perform this measurement on 16 flakes at room temperature and obtain an average lifetime of 15(3) ns. Additionally, we probe the PL dynamics of thermal and optically polarized electronic spin distributions of the $V^{-}_{B}$ ensemble in a sub-micron hBN flake, and fit our results to a 9-level model to extract electronic transition rates. Lastly, we present PL measurements that potentially indicate optically-induced conversion of $V^{-}_{B}$ to another electronic state, or possibly the neutral charge state ($V^{0}_{B}$), in neutron-irradiated hBN flakes of size $>$ 1 $μ$m.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2504.06812v3
- Title: Semi-classical geometric tensor in multiparameter quantum information
- Authors: Satoya Imai, Jing Yang, Luca Pezzè
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2504.06812v3  pdf=https://arxiv.org/pdf/2504.06812v3.pdf

Abstract:
The discrepancy between quantum distinguishability in Hilbert space and classical distinguishability in probability space is expressed by the gap between the quantum and classical Fisher information matrices (QFIM and CFIM, respectively). This intrinsic quantum obstruction is generally not saturable and plays a central role in both fundamental insights and practical applications in modern quantum physics. Here, we develop a geometrical framework for this gap by introducing the notion of semi-classical geometric tensor (SCGT). We relate this quantity to the quantum geometric tensor (QGT), whose real part equals the QFIM. We prove the matrix inequality between QGT and SCGT, which sharpens the standard inequality between QFIM and CFIM and provides novel multiparameter information bounds: the real part of the SCGT reproduces the CFIM plus an additional nonnegative contribution capturing quantum obstruction. This further motivates a natural extension of the Berry phase to the semi-classical setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2505.03640v2
- Title: Environmental Quantum States Trigger Emission in Nonlinear Photonics
- Authors: Jia-Qi Li, Xin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.03640v2  pdf=https://arxiv.org/pdf/2505.03640v2.pdf

Abstract:
Light-matter interactions are traditionally governed by two fundamental paradigms: spontaneous and stimulated radiation. However, in nonlinear multi-photon regimes, these classical mechanisms break down, revealing new possibilities for light emission. Here, we report the discovery of a novel mechanism, termed triggered emission, in which an emitter, largely detuned from single-photon states, is triggered by the quantum state of the environment to emit a highly correlated photon pair, doublon. By identifying two critical conditions, energy matching and wavefunction overlap, we demonstrate that the dynamics of the emitter are profoundly shaped by the environment's quantum state. Using this framework, we construct a novel superposition state comprising a localized single-photon state and a propagating, strongly correlated two-photon wavepacket. Furthermore, we realize the multi-photon unidirectional emission by modulating the emitter and the photon state. Our findings not only deepen the understanding of nonlinear emitter dynamics but also provide a versatile platform for quantum computing and quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2505.15302v2
- Title: Robust and compact single-lens crossed-beam optical dipole trap for Bose-Einstein condensation in microgravity
- Authors: Jan Simon Haase, Alexander Fieguth, Igor Bröckel, Janina Hamann, Jens Kruse, Carsten Klempt
- Categories: quant-ph (primary); quant-ph; physics.ins-det; physics.optics; physics.space-ph
- Links: abs=https://arxiv.org/abs/2505.15302v2  pdf=https://arxiv.org/pdf/2505.15302v2.pdf

Abstract:
We present a novel concept for a compact and robust crossed-beam optical dipole trap (cODT) based on a single lens, designed for the efficient generation of Bose-Einstein condensates (BECs) under dynamic conditions. The system employs two independent two-dimensional acousto-optical deflectors (AODs) in combination with a single high-numerical-aperture lens to provide three-dimensional control over the trap geometry, minimizing potential misalignments and ensuring long-term operational stability. By leveraging time-averaged potentials, rapid and efficient evaporative cooling sequences toward BECs are enabled. The functionality of the cODT under microgravity conditions has been successfully demonstrated in the Einstein-Elevator in Hannover, Germany, where the beam intersection was shown to remain stable throughout the microgravity phase of the flight. In addition, the system has been implemented in the sensor head of the INTENTAS project to verify BEC generation. Additional realization of one- and two-dimensional control of arrays of condensates through dynamic trap shaping was achieved. This versatile approach allows for advanced quantum sensing applications in mobile and space-based environments based on all-optical BECs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2505.16457v3
- Title: Maximum Separation of Quantum Communication Complexity With and Without Shared Entanglement
- Authors: Atsuya Hasegawa, François Le Gall, Augusto Modanese
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2505.16457v3  pdf=https://arxiv.org/pdf/2505.16457v3.pdf

Abstract:
We present relation problems whose input size is $n$ such that they can be solved with no communication for entanglement-assisted quantum communication models, but require $Ω(n)$ qubit communication for $2$-way quantum communication models without prior shared entanglement. This is the maximum separation of quantum communication complexity with and without shared entanglement. To our knowledge, our result even shows the first lower bound on quantum communication complexity without shared entanglement when the upper bound of entanglement-assisted quantum communication models is zero. Our result refutes a quantum analog of Newman's theorem.   The problem we consider is parallel repetition of any non-local game which has a perfect quantum strategy and no perfect classical strategy, and for which a parallel repetition theorem holds with exponential decay.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2507.18714v2
- Title: Non-perturbative switching rates in bistable open quantum systems: from driven Kerr oscillators to dissipative cat qubits
- Authors: Léon Carde, Ronan Gautier, Nicolas Didier, Alexandru Petrescu, Joachim Cohen, Alexander McDonald
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.18714v2  pdf=https://arxiv.org/pdf/2507.18714v2.pdf

Abstract:
In this work, we use path integral techniques to predict the switching rate in a single-mode bistable open quantum system. While analytical expressions are well-known to be accessible for systems subject to Gaussian noise obeying classical detailed balance, we generalize this approach to a class of quantum systems, those which satisfy the recently-introduced hidden time-reversal symmetry [1]. In particular, in the context of quantum computing, we deliver precise estimates of bit-flip error rates in cat-qubit architectures, circumventing the need for costly numerical simulations. Our results open new avenues for exploring switching phenomena in multistable single- and many-body open quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2507.21313v3
- Title: Orthogonalization speed-up from quantum coherence after a sudden quench
- Authors: Beatrice Donelli, Gabriele De Chiara, Francesco Scazza, Stefano Gherardini
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2507.21313v3  pdf=https://arxiv.org/pdf/2507.21313v3.pdf

Abstract:
We introduce a nonequilibrium phenomenon, reminiscent of Anderson's orthogonality catastrophe (OC), that arises in the transient dynamics following an interaction quench between a quantum system and a localized defect. Even if the system comprises only a single particle, the overlap between the asymptotic and initial superposition states vanishes according to a power-law scaling with the number of energy eigenstates entering the initial state and an exponent that depends on the interaction strength. The presence of quantum coherence in the initial state is reflected onto the discrete counterpart of an infinite discontinuity in the quasiprobability distribution of work due to the quench transformation, and onto the subsequent power-law decay of the work distribution. The positivity loss of the work distribution is directly linked with a reduction of the minimal time imposed by quantum mechanics for the state to orthogonalize, thus leading to a quantum coherence-enhanced state-orthogonalization. We propose an experimental test of coherence-enhanced orthogonalization dynamics based on Ramsey interferometry of a trapped cold-atom system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2507.23130v2
- Title: A multi-dimensional quantum estimation and model learning framework based on variational Bayesian inference
- Authors: Federico Belliardo, Erik M. Gauger, Tim H. Taminiau, Yoann Altmann, Cristian Bonato
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.23130v2  pdf=https://arxiv.org/pdf/2507.23130v2.pdf

Abstract:
The advancement and scaling of quantum technology has made the learning and identification of quantum systems and devices in highly-multidimensional parameter spaces a pressing task for a variety of applications. In many cases, the integration of real-time feedback control and adaptive choice of measurement settings places strict demands on the speed of this task. Here we present a joint model selection and parameter estimation algorithm that is fast and operable on a large number of model parameters. The algorithm is based on variational Bayesian inference (VBI), which approximates the target posterior distribution by optimizing a tractable family of distributions, making it more scalable than exact inference methods relying on sampling and that generally suffer from high variance and computational cost in high-dimensional spaces. We show how a regularizing prior can be used to select between competing models, each comprising a different number of parameters, identifying the simplest model that explains the experimental data. The regularization can further separate the degrees of freedom, e.g. quantum systems in the environment or processes, which contribute to major features in the observed dynamics, with respect to others featuring small coupling, which only contribute to a background. As an application of the introduced framework, we consider the problem of the identification of multiple individual nuclear spins with a single electron spin quantum sensor, relevant for nanoscale nuclear magnetic resonance. With the number of environmental spins unknown a priori, our Bayesian approach is able to correctly identify the model, i.e. the number of spins and their couplings. We benchmark the algorithm on both simulated and experimental data, using standard figures of merit, and demonstrating that we can estimate dozens of parameters within minutes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2508.00468v2
- Title: Inference of maximum parsimony phylogenetic trees with model-based classical and quantum methods
- Authors: Jiawei Zhang, Yibo Chen, Yang Zhou, Jun-Han Huang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.00468v2  pdf=https://arxiv.org/pdf/2508.00468v2.pdf

Abstract:
The maximum parsimony phylogenetic tree reconstruction problem is NP-hard, presenting a computational bottleneck for classical computing and motivating the exploration of emerging paradigms like quantum computing. To this end, we design three optimization models compatible with both classical and quantum solvers. Our method directly searches the complete solution space of all possible tree topologies and ancestral states, thereby avoiding the potential biases associated with pre-constructing candidate internal nodes. Among these models, the branch-based model drastically reduces the number of variables and explicit constraints through a specific variable definition, providing a novel modeling approach effective not only for phylogenetic tree building but also for other tree problems. The correctness of this model is validated with a classical solver, which obtains solutions that are generally better than those from heuristics on the GAPDH gene dataset. Moreover, our quantum simulations successfully find the exact optimal solutions for small-scale instances with rapid convergence, highlighting the potential of quantum computing to offer a new avenue for solving these intractable problems in evolutionary biology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2508.04689v2
- Title: Probabilistic quantum algorithm for Lyapunov equations and matrix inversion
- Authors: Marcello Benedetti, Ansis Rosmanis, Matthias Rosenkranz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.04689v2  pdf=https://arxiv.org/pdf/2508.04689v2.pdf

Abstract:
We present a probabilistic quantum algorithm for preparing mixed states which, in expectation, are proportional to the solutions of Lyapunov equations -- linear matrix equations ubiquitous in the analysis of classical and quantum dynamical systems. Building on previous results by Zhang et al., arXiv:2304.04526, at each step the algorithm can (i) return the current state, (ii) apply a trace nonincreasing completely positive map, or (iii) restart. We introduce a deterministic stopping rule, which leads to an efficient algorithm with a bounded expected number of calls to oracles representing the two input matrices of the Lyapunov equations. We also consider preparing a mixed state that approximates the normalized inverse of a positive definite matrix $A$. In its most general form, the algorithm generates mixed states, which approximate matrix-valued weighted sums and integrals. It can be shown that block encodings and states yield two incomparable computational resources even when they represent the same piece of data. While block encodings of functions have received much attention in the literature, our work takes a step toward the less explored problem of encoding functions into mixed states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2508.07359v2
- Title: Quantum-Classical Hybrid Computation of Electron Transfer in a Cryptochrome Protein via VQE-PDFT and Multiscale Modeling
- Authors: Yibo Chen, Zirui Sheng, Weitang Li, Yong Zhang, Xun Xu, Jun-Han Huang, Yuxiang Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.07359v2  pdf=https://arxiv.org/pdf/2508.07359v2.pdf

Abstract:
Accurate calculation of strongly correlated electronic systems requires proper treatment of both static and dynamic correlations, which remains challenging for conventional methods. To address this, we present VQE-PDFT,aquantum-classical hybrid framework that integrates variational quantum eigensolver with multiconfiguration pair-density functional theory (MC-PDFT). This framework strategically employs quantum circuits for multiconfigurational wavefunction representation while utilizing density functionals for correlation energy evaluation. The hybrid strategy maintains accurate treatment of static and dynamic correlations while reducing quantum resource requirements compared to highly expressive quantum algorithms. Benchmark validation, performed via noiseless quantum circuit simulator, on the Charge-Transfer dataset confirmed that VQE-PDFT achieved results comparable to conventional MC-PDFT. Building upon this, we developed shallow-depth hardware-efficient ansatz circuits and integrated them into a QM/MM multiscale architecture to enable applications in complex biological systems. This extended framework, when applied to electron transfer in the European robin cryptochrome protein ErCRY4 with noiseless simulations, yielded transfer rates that aligned well with experimental measurements. Finally, as a proof-of-concept hardware demonstration, we executed the reduced-density-matrix measurements for a single protein conformation on a 13-qubit superconducting device and showed the impact of noise through a comprehensive error analysis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2508.11962v2
- Title: Coherence and decoherence in generalized and noisy Shor's algorithm
- Authors: Linlin Ye, Zhaoqi Wu, Nanrun Zhou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.11962v2  pdf=https://arxiv.org/pdf/2508.11962v2.pdf

Abstract:
Quantum coherence constitutes a fundamental physical mechanism essential to the study of quantum algorithms. We study the coherence and decoherence in generalized Shor's algorithm where the register $A$ is initialized in arbitrary pure state, or the combined register $AB$ is initialized in any pseudo-pure state, which encompasses the standard Shor's algorithm as a special case. We derive both the lower and upper bounds on the performance of the generalized Shor's algorithm, and establish the relation between the probability of calculating $r$ when the register $AB$ is initialized in any pseudo-pure state and the one when the register $A$ initialized in arbitrary pure state. Moreover, we study the coherence and decoherence in noisy Shor's algorithm and give the lower bound of the probability that we can calculate $r$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2509.01892v2
- Title: Accelerating BP-based decoders for QLDPC Codes with Local Syndrome-Based Preprocessing
- Authors: Wenxuan Fan, Yasunari Suzuki, Gokul Subramanian Ravi, Yosuke Ueno, Ilkwon Byun, Koji Inoue, Teruo Tanimoto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.01892v2  pdf=https://arxiv.org/pdf/2509.01892v2.pdf

Abstract:
Due to the high error rate of qubits, detecting and correcting errors is essential for achieving fault-tolerant quantum computing (FTQC). Quantum low-density parity-check (QLDPC) codes are one of the most promising quantum error correction (QEC) methods due to their high encoding rates. BP (Belief Propagation)-based decoders are widely used and highly competitive for QLDPC codes because BP offers inherent parallelism and strong scalability. However, BP-based decoders still suffer from high decoding latency, a large portion of which is spent in the iterative BP stage.   In this paper, we propose a lightweight preprocessing step that utilizes local patterns in the syndrome to detect likely trivial error events and provide them as hints to BP-based decoders. These hints accelerate BP convergence and thereby reduce the overall decoding time. The proposed preprocessing step offers a broadly compatible approach to reducing the latency of BP-based QLDPC decodes. On the bivariate bicycle code $[[144,12,12]]$ at low physical error rates, our method achieves a $10\times$ speedup in decoding time for BP-OSD, and more than $2\times$ speedup for both BP-LSD and Relay-BP. Our method maintains the logical error rate when combined with BP-OSD and Relay-BP, while further achieving a significant reduction in logical error rate when combined with BP-LSD.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2509.20665v4
- Title: Lower Bounds for Learning Hamiltonians from Time Evolution
- Authors: Ziyun Chen, Jerry Li, Joseph Slote
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.20665v4  pdf=https://arxiv.org/pdf/2509.20665v4.pdf

Abstract:
Learning about a Hamiltonian $H$ from its time evolution $e^{-iHt}$ is a fundamental task in quantum science. A flurry of recent work has developed powerful new algorithms with provable guarantees for this task, for a variety of natural settings. Despite this, relatively little is known about lower bounds for learning Hamiltonians. In particular, in the natural setting where we assume $H$ is a $k$-local Hamiltonian on $n$ qubits, all existing algorithms require total evolution time at least $n^{Ω(k)}$ to learn the parameters of $H$, and it remained open whether one could obtain even faster algorithms -- or at the very least, if one could obtain better runtimes for simpler tasks, such as estimating a single designated coefficient of the Hamiltonian.   In this work we show the answer is essentially no, by obtaining strong lower bounds for these problems. We find that not only do $k$-local Hamiltonians require $n^{Ω(k)}$ time evolution or interactions to learn, but also that in several senses, learning anything about a Hamiltonian is just as hard as learning everything. In particular, we find the same $n^{Ω(k)}$ lower bound holds for learning a single coefficient of a $k$-local Hamiltonian $H$, even if the rest of $H$ is already known. We also show an $n^{Ω(k)}$ lower bound for the task of effective Hamiltonian learning, where one seeks only to learn a unitary that approximately implements time evolution of $H$. Several related lower bounds, such as for general sparse (but not necessarily local) $H$ are also given.   On the technical side, we make a new connection between Hamiltonian learning lower bounds and the analysis of Boolean functions, where we introduce a novel extremal property that may be of independent interest.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2603.24522v2
- Title: A Description of the Quantum Mpemba Effect using the Steepest-Entropy-Ascent Quantum Thermodynamics Framework
- Authors: Luis Enrique Rocha-Soto, Cesar Eduardo Damian-Ascencio, Adriana Saldaña-Robles, Sergio Cano-Andrade
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.24522v2  pdf=https://arxiv.org/pdf/2603.24522v2.pdf

Abstract:
The quantum Mpemba effect is a phenomenon characterized by an exponential relaxation from a non-equililbrium state to a steady state. This effect was predicted with an analysis of the Liouvillian superoperator and experimentally demonstrated in a three-level system. In this work, the system dynamics of the Mpemba effect is predicted within the steepest-entropy-ascent quantum thermodynamics framework considering a single constituent three-level isolated system. The system is projected from a four-dimensional Hilbert space onto a three-dimensional one using the Feshbach projection in order to compare the theoretical results with experimental data. Since the quantum Mpemba effect is characterized by a dissipative acceleration, the relaxation parameter, $τ_D$, plays a fundamental rol in the dissipative dynamics predicted by the model and is determined using machine learning methods, resulting in a model that thermodynamically describes this phenomenon at the quantum level.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2409.01051v2
- Title: INTENTAS -- An entanglement-enhanced atomic sensor for microgravity
- Authors: O. Anton, I. Bröckel, D. Derr, A. Fieguth, M. Franzke, M. Gärtner, E. Giese, J. S. Haase, et al.
- Categories: physics.ins-det (primary); physics.ins-det; cond-mat.quant-gas; physics.atom-ph; physics.space-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2409.01051v2  pdf=https://arxiv.org/pdf/2409.01051v2.pdf

Abstract:
The INTENTAS project aims to develop an atomic sensor utilizing entangled Bose-Einstein condensates (BECs) in a microgravity environment. This key achievement is necessary to advance the capability for measurements that benefit from both entanglement-enhanced sensitivities and extended interrogation times. The project addresses significant challenges related to size, weight, and power management (SWaP) specific to the experimental platform at the Einstein-Elevator in Hannover. The design ensures a low-noise environment essential for the creation and detection of entanglement. Additionally, the apparatus features an innovative approach to the all-optical creation of BECs, providing a flexible system for various configurations and meeting the requirements for rapid turnaround times. Successful demonstration of this technology in the Einstein-Elevator will pave the way for a future deployment in space, where its potential applications will unlock high-precision quantum sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2503.02497v4
- Title: A PennyLane-Centric Dataset to Enhance LLM-based Quantum Code Generation using RAG
- Authors: Abdul Basit, Nouhaila Innan, Muhammad Haider Asif, Minghao Shao, Muhammad Kashif, Alberto Marchisio, Muhammad Shafique
- Categories: cs.SE (primary); cs.SE; cs.AI; quant-ph
- Links: abs=https://arxiv.org/abs/2503.02497v4  pdf=https://arxiv.org/pdf/2503.02497v4.pdf

Abstract:
Large Language Models (LLMs) offer powerful capabilities in code generation, natural language understanding, and domain-specific reasoning. Their application to quantum software development remains limited, in part because of the lack of high-quality datasets both for LLM training and as dependable knowledge sources. To bridge this gap, we introduce \textit{PennyLang}, an off-the-shelf, high-quality dataset of 3,347 PennyLane-specific quantum code samples with contextual descriptions, curated from textbooks, official documentation, and open-source repositories. Our contributions are threefold: (1) the creation and open-source release of PennyLang, a purpose-built dataset for quantum programming with PennyLane; (2) a framework for automated quantum code dataset construction that systematizes curation, annotation, and formatting to maximize downstream LLM usability; and (3) a baseline evaluation of the dataset across multiple open-source and commercial models, including ablation studies, all conducted within a retrieval-augmented generation (RAG) pipeline. Using PennyLang with RAG substantially improves performance: for example, Qwen 7B's success rate rises from 8.7% without retrieval to 41.7% with full-context augmentation, and LLaMa 4 improves from 78.8% to 84.8%, while also reducing hallucinations and enhancing quantum code correctness. Moving beyond Qiskit-focused studies, we bring LLM-based tools and reproducible methods to PennyLane for advancing AI-assisted quantum development.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2507.18286v3
- Title: Unconventional Thermalization of a Localized Chain Interacting with an Ergodic Bath
- Authors: Konrad Pawlik, Nicolas Laflorencie, Jakub Zakrzewski
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2507.18286v3  pdf=https://arxiv.org/pdf/2507.18286v3.pdf

Abstract:
The study of many-body localized (MBL) phases intrinsically links spectral properties with eigenstate characteristics: localized systems exhibit Poisson level statistics and area-law entanglement entropy, while ergodic systems display volume-law entanglement and follow random matrix theory predictions, including level repulsion. Here, we introduce the interacting Anderson Quantum Sun model, which significantly deviates from these conventional expectations. In addition to standard localized and ergodic phases, we identify a regime that exhibits volume-law entanglement coexisting with intermediate spectral statistics. We also identify another nonstandard regime marked by Poisson level statistics, sub-volume entanglement growth, and rare-event-dominated correlations, indicative of emerging ergodic instabilities. These results highlight unconventional routes of ergodicity breaking and offer fresh perspectives on how Anderson localization may be destabilized.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2508.04935v2
- Title: Chern junctions in Moiré-Patterned Graphene/PbI2
- Authors: Sun Yan, M. Monteverde, V. Derkach, K. Watanabe, T. Taniguchi, F. Chiodi, H. Bouchiat, A. D. Chepelianskii
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2508.04935v2  pdf=https://arxiv.org/pdf/2508.04935v2.pdf

Abstract:
Expanding the moire material library continues to unlock novel quantum phases and emergent electronic behaviors. Here, we introduce PbI2 into the moire family and investigate the magnetotransport properties of moire superlattice in a hexagonal boron nitride/graphene/PbI2 heterostructures. In the high-field quantum Hall regime, we observe robust dissipationless transport at the charge neutrality point, indicative of incompressible states at filling factor vh = 0. Additionally, a fractional conductance plateau at 2/3 e2/h emerges, which we attribute to a Chern junction between domains with distinct Chern numbers originating from moire-modulated and conventional integer quantum Hall states. The moire Hofstadter spectrum displays an unconventional flavor sequence, likely influenced by proximity-induced spin-orbit coupling from the PbI2 layer. We also see coherent electronic interference along lines with Chern number vm = -2. These observations provide compelling evidence for the formation of moire domains that nontrivially interrupt incompressible quantum Hall states, reflecting the strong moire potential in the BN/graphene/PbI2 superlattice. We suggest that the moire Hofstadter spectrum coupled with the proximity-induced spin-orbit interaction from PbI2 gives rise to a high magnetic field topological insulator phase explaining ballistic transport at the charge neutrality point in the graphene monolayer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2508.21390v2
- Title: Generalized quantum singular value transformation with application in quantum conjugate gradient least squares algorithm
- Authors: Yu-Qiu Liu, Hefeng Wang, Hua Xiang
- Categories: math.NA (primary); math.NA; quant-ph
- Links: abs=https://arxiv.org/abs/2508.21390v2  pdf=https://arxiv.org/pdf/2508.21390v2.pdf

Abstract:
Quantum signal processing (QSP) and generalized quantum signal processing (GQSP) are essential tools for implementing the block encoding of matrix functions. The achievable polynomials of QSP have restrictions on parity, while GQSP eliminates these restrictions. But GQSP only constructs functions of unitary matrices. In this paper, we further investigate GQSP and extend it to general matrices. Compared with the quantum singular value transformation (QSVT), our proposed method relaxes the requirements on the parity of polynomials. We refer to this extension as generalized quantum singular value transformation (GQSVT). Subsequently, by utilizing the relationship between generalized matrix functions and standard matrix functions, we propose a classical-quantum hybrid quantum conjugate gradient least squares (CGLS) algorithm using GQSVT.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2509.01585v2
- Title: Dynamics of Loschmidt echoes from operator growth in noisy quantum many-body systems
- Authors: Takato Yoshimura, Lucas Sá
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2509.01585v2  pdf=https://arxiv.org/pdf/2509.01585v2.pdf

Abstract:
We study the dynamics of Loschmidt echoes in noisy quantum many-body systems without conservation laws. We first show that the operator Loschmidt echo in noisy unitary dynamics is equivalent to the operator norm of the corresponding dissipative dynamics upon noise averaging. We then analyze this quantity in two complementary ways, revealing universal dynamical behavior. First, we develop a heuristic picture for generic Floquet systems that connects Loschmidt echoes, out-of-time-order correlators, and operator growth, which is valid at any dissipation strength. We assert that the Loschmidt echo has two dynamical regimes depending on the time $t$ and the strength of the noise $p$: Gaussian decay for $pt\ll1$ and exponential decay (with a noise-independent decay rate) for $pt\gg1$. Lastly, we rigorously prove all our results for a solvable chaotic many-body quantum circuit, the dissipative random phase model -- thus providing exact insight into dissipative quantum chaos.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2509.19377v3
- Title: Relativistic Path-Integral Origin of the Dirac Equation, Quantum Collapse, Decoherence and Non-Hermitian Phenomena
- Authors: Wei Wen
- Categories: physics.gen-ph (primary); physics.gen-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2509.19377v3  pdf=https://arxiv.org/pdf/2509.19377v3.pdf

Abstract:
Relativity and quantum mechanics are two cornerstones of modern physics, yet their unification within a single-particle path integral and a dynamical explanation of quantum measurement remain unresolved. Historically, these two problems have been treated as separate, but here we show they are intimately linked. We construct a self-consistent relativistic path integral that yields the Dirac and other standard wave equations under differetialable potentials. More importantly, we find that this propagator contains a latent, nonlocal correlation that is activated by realistic electromagnetic noise. This correlation unifies unitary evolution and wave-function collapse into a single dynamical mechanism: while differentiable potentials preserve unitary driving, nondifferentiable noise activates a bounded-martingale stochastic process that induces collapse. We show that the characteristics of quantum measurement are naturally derived from this stochastic dynamical process, thereby turning the axioms of quantum measurement from postulates into dynamical consequences. Furthermore, averaging this stochastic evolution over the noise record recovers the Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) master equation, providing a first-principles derivation of decoherence free from the method of Born-Markov approximation. Extending this approach to composite systems establishes a stochastic foundation for effective non-Hermitian descriptions while preserving relativistic causality. Finally, because the noise spectrum governs the collapse process, engineering ``colored'' noise can actively accelerate or steer state reduction, suggesting new routes toward fast qubit reset and enhanced quantum control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2511.02907v2
- Title: Revisiting Nishimori multicriticality through the lens of information measures
- Authors: Zhou-Quan Wan, Xu-Dong Dai, Guo-Yi Zhu
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.dis-nn; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2511.02907v2  pdf=https://arxiv.org/pdf/2511.02907v2.pdf

Abstract:
The quantum error correction threshold is closely related to the Nishimori physics of random statistical models. We extend quantum information measures such as coherent information beyond the Nishimori line and establish them as sharp indicators of phase transitions over the full $p$-$T$ plane. These generalized measures admit a natural operational interpretation as diagnostics of inference mismatch for decoders operating at an effective temperature. We derive exact inequalities for several generalized measures, demonstrating that each attains its extremum along the Nishimori line. As a direct application, we study these measures in the 2d $\pm J$ random-bond Ising model-corresponding to a surface code under bit-flip noise-and revisit the Nishimori multicritical point. Among all indicators, coherent information exhibits the weakest finite-size effects, enabling a high-precision estimate $p_c=0.1092212(4)$ and the associated critical exponents.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2511.10125v2
- Title: Geometric foundations of thermodynamics in the quantum regime
- Authors: Álvaro Tejero, Martín de la Rosa
- Categories: math-ph (primary); math-ph; math.DG; quant-ph
- Links: abs=https://arxiv.org/abs/2511.10125v2  pdf=https://arxiv.org/pdf/2511.10125v2.pdf

Abstract:
In this work, we present a geometrical formulation of quantum thermodynamics based on contact geometry and principal fiber bundles. The quantum thermodynamic state space is modeled as a contact manifold, with equilibrium Gibbs states forming a Legendrian submanifold that encodes the fundamental thermodynamic relations. A principal fiber bundle over the manifold of density operators distinguishes the quantum state structure from thermodynamic labels: its fibers represent non-equilibrium configurations, and their unique intersections with the equilibrium submanifold enforce thermodynamic consistency. Quasistatic processes correspond to minimizing geodesics under the Bures-Wasserstein metric, leading to minimal dissipation, while the divergence of geodesic length toward rank-deficient states geometrically derives the unattainability aspect of the third law. Non-equilibrium extensions, formulated through pseudo-Riemannian metrics and connections on the principal bundle, introduce curvature-induced holonomy that quantifies a geometric source of irreversibility in cyclic processes. In this framework, the thermodynamic laws in the quantum regime emerge naturally as geometric consequences.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2512.15795v2
- Title: Localization from Infinitesimal Kinetic Grading: Finite-size Scaling, Kibble-Zurek Dynamics and Applications in Sensing
- Authors: Argha Debnath, Ayan Sahoo, Debraj Rakshit
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2512.15795v2  pdf=https://arxiv.org/pdf/2512.15795v2.pdf

Abstract:
We study a one-dimensional lattice model with site-dependent nearest-neighbor hopping amplitudes that follow a power-law profile. The hopping variation is controlled by a grading exponent, $|alpha|$, which serves as the tuning parameter of the system. In the thermodynamic limit, the ground state becomes localized in the limit $|alpha| \to 0$, signaling the presence of a critical point characterized by a diverging localization length. Using exact diagonalization methods, we perform finite-size scaling analysis, and extract the associated critical exponent governing the near-critical behavior. To further characterize the criticality, we analyze inverse participation ratio (IPR), energy gap between the ground and first excited state, and fidelity-susceptibility. We also investigate the nonequilibrium dynamics by linearly ramping the hopping profile at various rates and tracking the evolution of the localization length and the IPR. The Kibble-Zurek mechanism successfully explains the resulting dynamics of the system via the critical exponents obtained from static scaling analysis. The localization transition can be exploited as a resource for achieving quantum-enhanced sensitivity in the estimation of a parameter. Beyond its fundamental significance, the kinetic-grading-induced localization transition provides a natural platform for quantum sensing. Using the critical enhancement of the quantum Fisher information (QFI), we demonstrate that the system enables quantum-enhanced parameter estimation of the grading exponent. We propose both adiabatic and dynamical quantum critical sensors and demonstrate that they exhibit enhanced scaling of the QFI. Our results therefore establish graded kinetic systems not only as a new setting for localization physics, but also as a potential resource for designing quantum-enhanced sensing devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-21 10:08
- arXiv: 2604.07291v2
- Title: Groenewold-Moyal twists, integrable spin-chains and AdS/CFT
- Authors: Riccardo Borsato, Miguel García Fernández
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2604.07291v2  pdf=https://arxiv.org/pdf/2604.07291v2.pdf

Abstract:
We take the first steps to address via integrability the spectral problem of AdS/CFT dual pairs deformed by Groenewold-Moyal twists. In particular, we start by considering a twisted spin-chain that couples, through a Groenewold-Moyal twist deformation, two $\mathfrak{sl}(2)$-invariant spin-chains. We interpret this deformed spin-chain as a deformation of a subsector of the $AdS_3/CFT_2$ spin-chain, but the construction shares qualitative features also with the corresponding deformation of the $AdS_5/CFT_4$ spin-chain, for example. As in similar types of deformations, we show that there exists a certain basis in which the spin-chain Hamiltonian takes a Jordan-block form. At the same time, by working in the basis of eigenstates of the generators used to construct the Groenewold-Moyal twist, the Hamiltonian appears to be diagonalisable and with a deformed spectrum. Employing the method of the Baxter equation, we write down the energy of the ground state and of excited states in a perturbation of the deformation parameter. We then consider the string-theory side of the duality, where the twist is realised as a deformation of AdS of the type of Maldacena-Russo-Hashimoto-Itzhaki. We construct a deformation of the usual BMN classical solution, and in the large-$J$ limit we match the leading $\mathcal O(J^{-3})$ term of the energy of the spin-chain groundstate with a conserved charge of the string classical solution. Differently from the undeformed setup as well as similar kinds of deformations, we find that the general expression of this charge of the string sigma-model is non-local, and that it does not correspond to a standard isometry. Nevertheless, it can be computed from the monodromy matrix and it is part of the tower of conserved charges provided by integrability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

