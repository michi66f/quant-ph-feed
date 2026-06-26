- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23718v1
- Title: Dimensionality Reduction of QAOA Parameter Space with Kernel PCA for Max-Cut
- Authors: Sidharth Brahmandam, Vayd Ramkumar
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2606.23718v1  pdf=https://arxiv.org/pdf/2606.23718v1.pdf

Abstract:
The Quantum Approximate Optimization Algorithm (QAOA) is a leading variational algorithm for combinatorial optimization on near term quantum devices. As circuit depth increases, the number of optimization parameters grows, making the search landscape increasingly nonlinear and difficult to optimize. Previous studies have shown that optimal QAOA parameters often lie on a low dimensional manifold that can be approximated using Principal Component Analysis (PCA) at shallow circuit depths. However, the effectiveness of PCA decreases at higher depths because the underlying parameter manifold becomes increasingly nonlinear. In this work, we investigate Kernel Principal Component Analysis (KPCA) with a radial basis function kernel as a nonlinear dimensionality reduction technique for QAOA parameter optimization. The model is trained using 200 graphs from each of 3 graph families, namely Erdos-Renyi, Barabasi-Albert, and Watts-Strogatz, with graph sizes ranging from 7 to 10 nodes. Performance is evaluated on 30 test graphs containing 12 nodes at circuit depths 1, 2, 4, and 8. Experimental results demonstrate that KPCA consistently outperforms PCA at deeper circuit depths across all graph families. At depth 8, KPCA achieves approximation ratios above 0.86, while PCA declines to approximately 0.81 to 0.83. Both methods reduce the number of quantum circuit evaluations by more than 93 percent relative to unrestricted QAOA optimization. These findings suggest that nonlinear kernel methods more effectively capture the structure of the QAOA parameter manifold and provide a practical approach for scaling variational quantum optimization to deeper circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23719v1
- Title: A Hybrid Quantum-Classical Approach for Melt Pool Prediction in Laser Powder Bed Fusion
- Authors: Matthew M. Sato, Kincho H. Law
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2606.23719v1  pdf=https://arxiv.org/pdf/2606.23719v1.pdf

Abstract:
Laser powder bed fusion (LPBF) is a promising additive manufacturing technique that suffers from quality assurance concerns. Predicting melt pools from process parameters is crucial for assessing quality prior to manufacturing but remains a difficult problem because of the complex physical processes underlying LPBF. Quantum computers present a new computing paradigm, providing a new approach to information processing using quantum entanglement and superposition. This paper presents a practical demonstration of a hybrid quantum-classical model that leverages quantum computing to improve process parameter feature extraction with a quantum feature encoder. To make the quantum approach computationally feasible for large datasets, we first employ a clustering algorithm to reduce the number of expensive quantum computations. These quantum features are then processed by a classical neural network to predict the melt pool morphology, allowing for more accurate predictions of melt pools. We demonstrate the method using a quantum simulator, analyze the effect of measurement shot noise on the predictive performance of the network, and verify the results using quantum hardware. Finally, by examining which quantum features are most important, we provide insights that can inform the future design of more effective quantum encoding circuits. Ultimately, the performance improvement over purely classical networks validates the hybrid approach, demonstrating an engineering application of quantum computing using noisy and intermediate scale quantum (NISQ) devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23722v1
- Title: Quantum-enhanced estimation of stimulated Raman optical activity
- Authors: Mahadeva Chanda Durjoy, Girish S. Agarwal
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.23722v1  pdf=https://arxiv.org/pdf/2606.23722v1.pdf

Abstract:
In recent times there has been growing interest in Raman optical activity (ROA) for its label free detection of absolute configuration, conformation, and stereochemical structure in chiral biosamples and drug molecules. Since ROA signals are generally small, techniques such as stimulation by a probe beam can be used to enhance the signal strength. However, with a classical probe, the measurement precision is still fundamentally limited by its shot noise. To solve this problem we propose the use of two-mode squeezed vacuum and show that it can achieve sub-shot noise limited measurement sensitivity. Using quantum estimation theory, we derived the quantum Fisher information and the quantum Cramér-Rao bound (QCRB) for stimulated ROA measurement to quantify the precision enhancement. This improvement comes from photon-number correlations which suppress the intensity fluctuation common to both modes. We further show that balanced detection of the output intensity difference is a practical measurement scheme that approaches the QCRB and becomes optimal in the small-chirality limit. This opens a promising path toward more sensitive Raman chiroptical spectroscopy of weak and photosensitive samples.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23726v1
- Title: Ultra-Low-Rate Information Reconciliation: Repetition Coding or Dedicated Codes?
- Authors: Erdem Eray Cil, Laurent Schmalen
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2606.23726v1  pdf=https://arxiv.org/pdf/2606.23726v1.pdf

Abstract:
We compare repetition-based ultra-low-rate information reconciliation with dedicated ultra-low-rate codes for CV-QKD. Repetition coding offers a favorable performance-complexity trade-off, incurring only a moderate error-rate penalty while reducing decoding complexity by $2\times$, making it attractive for implementation-constrained systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23727v1
- Title: Certifying Quantum Optimization and Circuit Cutting by Using Quantum-Classical Moment Duality
- Authors: Ammar Daskin
- Categories: quant-ph (primary); quant-ph; cs.DS
- Links: abs=https://arxiv.org/abs/2606.23727v1  pdf=https://arxiv.org/pdf/2606.23727v1.pdf

Abstract:
We establish a direct quantum-classical duality based on the degree-$2$ Sum-of-Squares (SoS) semidefinite programming cone: the matrix of two-qubit Pauli-$Z$ correlation functions obtained from \emph{any} quantum state $ρ$ is automatically a feasible point of the classical Goemans-Williamson (GW) relaxation. This observation provides a universal ``safety net'' for quantum optimization algorithms: applying GW random hyperplane rounding to the quantum-driven moment matrix yields a certified expected cut value $\mathbb{E}[\mathrm{Cut}] \ge α_{\mathrm{GW}}\langle\mathcal{H}\rangle_ρ$, valid for every state produced by variational algorithms such as QAOA or the Variational Quantum Power Method (VQPM), regardless of convergence quality. We further show that the same moment matrix reveals the tensor-product structure of the underlying unitary circuit, enabling a polynomial-time, correlation-based circuit cutting procedure with rigorous error bounds. The framework is validated numerically on Max-Cut instances for variational quantum algorithms and on random states for circuit cutting, demonstrating that the cheap two-point correlation data are sufficient to locate near-optimal bipartitions and that the theoretical error bounds hold in practice.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23751v1
- Title: Challenges in Barren Plateau Mitigation with Dynamic Parameterized Quantum Circuits
- Authors: Sumeet Shirgure, Efekan Kökcü, Siyuan Niu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23751v1  pdf=https://arxiv.org/pdf/2606.23751v1.pdf

Abstract:
Variational quantum algorithms (VQAs) are a promising paradigm for quantum advantage, yet their trainability is severely hampered by barren plateaus (BPs). Several works have proposed using dynamic parameterized quantum circuits (DPQCs) which intersperse unitary layers with parameterized CPTP maps (e.g. engineered dissipation, feedforward gadgets, or periodic resets), as a potential route around BPs. We unite this class of circuits into a formalization for DPQCs. We identify constraints on the nature and the structure of DPQCs if they are to prevent a significant number of parameters from becoming untrainable. We further show via purification and Pauli path analysis, a mechanism with which cost function anti-concentrates in DPQCs while still suffering from untrainability of a significant number of parameters. Our analysis reveals ways to design DPQCs that do not have an exponentially concentrated cost function, and our results suggest that BP mitigation via DPQCs is at least as hard as designing BP-free unitaries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23777v1
- Title: Connecting Quantum Tomography and Quantum Retrodiction
- Authors: Sebastian Murk, Ian Tan, Fabian Müller, Dominik Šafránek
- Categories: quant-ph (primary); quant-ph; math-ph; math.ST; physics.data-an
- Links: abs=https://arxiv.org/abs/2606.23777v1  pdf=https://arxiv.org/pdf/2606.23777v1.pdf

Abstract:
Quantum tomography and quantum retrodiction are traditionally viewed as separate inference tasks: tomography reconstructs quantum states from measurement data, whereas retrodiction infers past quantum states from observed outcomes. We show that the two are manifestations of the same underlying principle. We prove that the Petz recovery map associated with a measurement channel is precisely the gradient update of the log-likelihood used in maximum-likelihood tomography. Consequently, repeated applications of the Petz map monotonically increase the likelihood. Extending beyond measurement channels, we derive a noncommutative generalization of the Petz map from the gradient of a generalized likelihood for arbitrary quantum channels. The resulting iterative procedure maximizes the likelihood and provides a general framework for quantum tomography, establishing a direct bridge between retrodiction, recovery maps, and statistical inference.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23796v1
- Title: A no-go theorem for privacy in distributed sensing using Gaussian states
- Authors: Jason L. Pereira, Damian Markham
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23796v1  pdf=https://arxiv.org/pdf/2606.23796v1.pdf

Abstract:
In the discrete variable setting, entangled resource states allow a set of parties to learn a global function of a set of spatially separated systems, whilst keeping the local parameters of those systems completely private. In the continuous variable setting, distributed sensing has been carried out using Gaussian resource states, but without the same guarantees about privacy. Here, we show that perfect privacy is impossible to achieve for any distributed sensing protocol that uses Gaussian states as a resource. We also introduce a measure of relative privacy, bounding the degree to which any Gaussian distributed sensing protocol can keep local parameters hidden.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23800v1
- Title: Unitary Designs from Doped Matchgate Circuits
- Authors: Fabian Ballar Trigueros, Zheng-Hang Sun, Xhek Turkeshi, Piotr Sierant, Poetri Sonya Tarabunga
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23800v1  pdf=https://arxiv.org/pdf/2606.23800v1.pdf

Abstract:
Matchgate circuits realize free-fermion dynamics: they are efficiently classically simulable, yet cannot on their own generate the generic randomness required for universal computation or unitary design formation. We study a controlled route beyond this integrable limit by doping matchgate circuits with non-Gaussian gates-physically, the injection of fermionic interactions into an otherwise free system. Using the matchgate commutant framework, we obtain analytic control over unitary $2$-design formation. For globally scrambled dynamics, the design problem maps exactly onto a classical birth-death Markov chain with an Ornstein-Uhlenbeck continuum limit, recasting the emergence of quantum randomness in terms of spectral gaps and mixing times and yielding rigorous bounds on the number of non-Gaussian gates needed for approximate $2$-designs. These bounds hold for a broad class of parity-preserving non-Gaussian gates, independently of microscopic details, with numerics indicating that the same mechanism governs higher-order designs. Used as local building blocks in a glued-circuit architecture, they yield approximate parity-preserving $2$-designs in polylogarithmic depth with a sparse non-Gaussian gate count, with implications for Page-like entanglement growth and fermionic classical-shadow protocols. Finally, locality reshapes this picture: in local brickwork dynamics, design formation is diffusion-limited and far slower. Our results establish doped matchgate circuits as a controlled, analytically tractable route from free fermions to interaction-generated quantum designs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23803v1
- Title: Infinite-Level Hierarchy of Solvable Quantum Circuits
- Authors: Michael A. Rampp, Suhail A. Rather, Pieter W. Claeys
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; nlin.SI
- Links: abs=https://arxiv.org/abs/2606.23803v1  pdf=https://arxiv.org/pdf/2606.23803v1.pdf

Abstract:
Dual-unitary circuits have emerged as a paradigm of exactly solvable yet non-integrable quantum dynamics. Recently, a generalization of dual unitarity attempting to extend the phenomenology of exactly solvable circuits has been introduced through a hierarchy of conditions, with dual unitarity as the first level. However, beyond the second level the proposed generalized dual-unitary hierarchy ceases to be solvable in the whole spacetime. We present an infinite hierarchy of solvability conditions remedying this problem. These new conditions can be combined with the generalized dual-unitary hierarchy to obtain circuits for which correlation functions and entanglement dynamics can be analyzed exactly in the whole spacetime. We show that this novel hierarchy possesses non-trivial solutions at every level. Our results demonstrate that dual unitarity can be systematically extended while preserving solvability, opening up investigations of exactly solvable non-integrable systems with more general properties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23809v1
- Title: Efficient Graph State Purification with Factorized Graph-Preserving Operations across Local Clifford Orbits
- Authors: Mingyuan Wang, Guus Avis, Kenneth Goodenough, Stefan Krastanov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23809v1  pdf=https://arxiv.org/pdf/2606.23809v1.pdf

Abstract:
Graph states form a broad class of multipartite entangled states underlying measurement-based quantum computation, quantum networks, and stabilizer codes. However, systematic entanglement distillation for arbitrary graph states remains challenging because the circuit design space grows rapidly with the number of parties. We introduce a group of Clifford operations that we call "factorized graph-preserving". It enables us to efficiently enumerate and optimize graph-state purification circuits at finite size for realistic noisy hardware. These operations map products of graph-basis states to products of graph-basis states, so their action can be represented as permutations of graph-basis labels. Moreover, this useful gate set admits a compact factorized description determined by simple graph-theoretic features. This structure also allows, after some initial cached precomputation, drastically lower computational complexity for simulating a gate. We further organize these operations over local-complementation (LC) orbits using minimum-edge representatives (MERs), which let us design purification circuits that apply to all locally equivalent graph states (up to a basis change). Using this framework, we optimize noisy finite-size multipartite distillation circuits for several graph-state families. Numerical results show that the resulting graph-preserving circuits can outperform standard recurrence-based purification protocols under realistic gate and measurement noise. Our results establish LC-orbit structure and factorized graph-preserving operations as practical tools for scalable, topology-aware and hardware-constrained graph-state distillation protocol design. Our work can also be interpreted as a graph-based heuristic for finding transversal gates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23817v1
- Title: Revealing high-dimensional entanglement through symmetry
- Authors: Jayden Webster, Florian Kanitschar, Emanuele Polino, Simon J. U. White, Sven Rogge, Farzad Ghafari, Marcus Huber, Nora Tischler
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23817v1  pdf=https://arxiv.org/pdf/2606.23817v1.pdf

Abstract:
Photons encoded in discrete time bins can be routinely prepared in temporal superposition states, enabling high-dimensional entanglement and enhanced quantum communication rates. However, characterizing this high-dimensional entanglement presents significant challenges, namely due to the involved measurement complexity or reliance on restrictive assumptions that compromise the generality of traditional approaches. Here, we develop and experimentally demonstrate a simple linear-optical scheme based on particle-exchange symmetry that allows us to probe high-dimensional entanglement in time-bin-encoded states. Combining Hong-Ou-Mandel interference with suitable transformations, our method not only certifies entanglement but also lower-bounds its dimensionality using only two dichotomic symmetry-based measurements. This bound is obtained through a new rigorous theoretical analysis and can be further improved by weak, physically motivated assumptions. The scheme remains effective at any timescale, even far below the temporal detector resolution used. Our work provides a powerful state-characterization tool and demonstrates that we can prove high-dimensional temporal entanglement on timescales inaccessible to the setup.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23823v1
- Title: Wavelet Matrix Product States for Quantum Fields
- Authors: Molly Kaplan, Antoine Tilloy
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; hep-th
- Links: abs=https://arxiv.org/abs/2606.23823v1  pdf=https://arxiv.org/pdf/2606.23823v1.pdf

Abstract:
We introduce a variational method to solve continuum quantum models with discrete tensor network techniques. The method leverages wavelet matrix product states (wMPS): matrix product states built on top of sufficiently regular ($N\geq 6$) Daubechies scaling functions. These states live in the continuum field theory Fock space, have finite energy density, and can be optimized with standard algorithms, without restriction to free theories. Further, exploiting the multi-resolution analysis built into wavelets, and its quantum circuit description, we can iteratively refine wMPS to obtain accurate approximations at arbitrarily fine length-scales. We showcase the efficiency of the method on the Lieb-Liniger model, computing energy density and correlation functions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23836v1
- Title: Mode-selective nonlinear interference for high-brightness and high-purity fiber-coupled SPDC sources
- Authors: Carlos Sevilla-Gutiérrez, Purujit Singh Chauhan, Varun Raj Kaipalath, Fabian Steinlechner
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.23836v1  pdf=https://arxiv.org/pdf/2606.23836v1.pdf

Abstract:
Single-mode-fiber-coupled spontaneous parametric down-conversion (SPDC) sources are a key resource for photonic quantum technologies, but in single-crystal geometries brightness, heralding efficiency, and spectral purity remain constrained by intrinsic trade-offs. Here, we show how nonlinear interference in a cascaded two-crystal type-II SPDC source can be used to engineer the modal structure of SPDC emission, improving the brightness--heralding-efficiency trade-off by more than one order of magnitude beyond the single-crystal limit. We further demonstrate two routes to near-unity spectral purity while retaining high brightness and/or heralding efficiency, even with standard periodically poled crystals, and study the additional advantages of aperiodic poling with Gaussian phase matching. Using a spectrally resolved Laguerre--Gauss modal decomposition, we show that these improvements arise from mode-selective interference of spatial-spectral SPDC modes within the nonlinear interferometer. We experimentally validate the model through sum-frequency-generation measurements of the spatial-spectral state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23894v1
- Title: When does dissipation help neural surrogates learn open quantum dynamics?
- Authors: Alauddin Ahmed
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23894v1  pdf=https://arxiv.org/pdf/2606.23894v1.pdf

Abstract:
Dissipation is usually viewed as an obstacle to predicting quantum dynamics, yet it can also contract trajectories toward steady states and thereby suppress accumulated prediction errors, leaving it unclear whether dissipation ultimately helps or hinders the learnability of open quantum dynamics. We investigate this question using Neural Ordinary Differential Equation (NODE) surrogates for open Heisenberg XYZ spin chains. Closed-system learnability deteriorates rapidly with system size, culminating in a static-prediction collapse at four qubits; dissipation reverses this trend, creating a broad high-fidelity regime at intermediate system sizes, while at four qubits a fidelity-aware objective recovers learnable rollout structure that is absent under closed-system training. Comparison against static and steady-state baselines reveals that dissipation improves performance through two fundamentally different mechanisms: at weak-to-moderate dissipation the surrogate captures nontrivial transient dynamics and substantially outperforms trivial predictors, whereas at stronger damping high fidelity increasingly reflects trajectory simplification toward the steady state rather than improved learned dynamics. These results show that dissipation can enhance the learnability of open quantum dynamics, but that fidelity alone is insufficient to distinguish genuine dynamical learning from steady-state trivialization: dissipative contraction and trajectory simplification are distinct effects that peak in different regimes and should be disentangled when evaluating learned quantum-dynamical surrogates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23934v1
- Title: Augmenting Imaginary-Time Evolution with Local Geometric Information
- Authors: Carlos L. Benavides-Riveros, Prachi Sharma, Fedor Šimkovic
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2606.23934v1  pdf=https://arxiv.org/pdf/2606.23934v1.pdf

Abstract:
Imaginary-time evolution (ITE) underpins a broad family of algorithms for ground-state preparation in quantum simulation and quantum many-body physics. In these methods, convergence is governed by the energy variance of the instantaneous state, causing the flow to approach the ground state only asymptotically. We introduce an augmented imaginary-time evolution (AITE) framework that replaces the standard gradient flow on the energy landscape with a geometrically informed descent along locally optimal directions, which are identified by exploiting the higher-order statistical structure of the instantaneous energy distribution. The resulting flow strictly outperforms standard ITE throughout the entire evolution and exhibits two qualitatively distinct regimes: a superlinear convergence regime, followed by an extinction regime in which the energy error vanishes exactly at a finite imaginary time, in sharp contrast to the asymptotic exponential decay of ITE. Standard ITE is recovered in the zero-skewness limit of AITE, implying that the acceleration extends naturally across the broader ITE algorithmic family.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23951v1
- Title: Mølmer-Sørensen gates in trapped-ions chains in the presence of correlated noise
- Authors: D. V. Donchenko, E. A. Anikin, O. Lakhmanskaya, K. Lakhmanskiy
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23951v1  pdf=https://arxiv.org/pdf/2606.23951v1.pdf

Abstract:
We analyze the impact of correlated laser frequency noise on Mølmer-Sørensen gates in qubit registers based on trapped-ion chains. Using perturbation theory, we calculate gate fidelities in the presence of noise with arbitrary power spectral density for different chain lengths and ion positions in the chain. With our approach, we account for simultaneous excitation of multiple phonon modes during gate operation. We find out that the impact of medium-frequency laser noise depends considerably on the positions of the ions in the chain. In contrast, low-frequency noise has similar effect for different chain lengths and ion positions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23952v1
- Title: Biophysical EPR Using Superconducting Resonators
- Authors: Austin R. Gamble Jarvi, Hamid R. Mohebbi, Ishit Raval, Omari Culzac, Jack Erickson, Sameh Hegazy, Don Carkner, Andrew Wiles, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23952v1  pdf=https://arxiv.org/pdf/2606.23952v1.pdf

Abstract:
We present innovations that enable the use of superconducting resonators for high sensitivity, high bandwidth pulsed electron paramagnetic resonance (EPR) measurements on biologically relevant samples with enhanced stability and throughput. A custom-built X-band pulsed EPR spectrometer with AWG and digital IF capability generated by an FPGA was used to control a novel patterned thin film planar superconducting microstrip resonator capable of generating Rabi fields sufficient to achieve 6 ns pi/2 Gaussian pulses using a 100 W solid-state HPA. The system allows automated sequential calibration, measurement, and analysis of five 3.5 uL samples contained in a sample cartridge. Performance was validated through measurements of double electron-electron resonance (DEER) distances in a variety of spin-labeled protein samples with biologically relevant concentrations, including measurements below 10 uM. The results enable broadening the scope of applications for both superconducting resonators and the use of EPR in biotechnology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23967v1
- Title: Polynomial-time exact diagonalization via sparse guided eigenwalks
- Authors: Zachary E. Chin, Mario Motta, Javier Robledo Moreno, Antonio Mezzacapo, Isaac L. Chuang, William Kirby
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23967v1  pdf=https://arxiv.org/pdf/2606.23967v1.pdf

Abstract:
Computing quantum ground states is generically difficult, but additional structure can sometimes allow diagonalization to be recast as a more feasible problem. For example, when the desired ground state is sparse in a given basis, diagonalization can be facilitated via graph search. We make this reformulation precise by introducing the eigenwalk problem, which seeks the support of a sparse eigenvector of a Hermitian matrix by exploring the graph induced by its nonzero entries. However, it is not obvious whether the relevant support vertices must always be efficiently reachable by a search on the graph. To resolve this question, we prove that for every sparse eigenvector, there exists a (possibly different) sparse eigenvector with the same eigenvalue whose support is tightly localized in the graph, with diameter scaling only linearly in the sparsity and independently of the total number of vertices. As a consequence, if a $2^n$-dimensional, ${\rm poly}(n)$-sparse Hamiltonian has an $\mathcal{O}(1)$-sparse extremal eigenvector and one support element is known, then an exact eigenvector with the same eigenvalue can be computed classically in ${\rm poly}(n)$ time. The same conclusion follows when the $\mathcal{O}(1)$-sparse eigenvector is non-extremal, provided that it is sparser than every eigenvector with a different eigenvalue. These results hold with no assumptions on the degeneracy, locality, spectral width, or spectral gap of the Hamiltonian, and the underlying support-localization principle also extends to problems beyond exact diagonalization, such as sparse principal component analysis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23999v1
- Title: Suppressing Self-Discharging of Quantum Batteries by Cavity Interactions
- Authors: Anass Jad, Abderrahim El Allati, Mohammad B. Arjmandi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23999v1  pdf=https://arxiv.org/pdf/2606.23999v1.pdf

Abstract:
We analyse a two-cavity architecture, in which a lossy cavity hosting $N$ qubits is coherently coupled to an auxiliary cavity, as a resource for the storage phase of an open quantum battery at non-zero temperature. Within a local Lindblad treatment in the resonant configuration, we find that the inter-cavity coupling enhances the suppression of self-discharging across every initial preparation, battery size, and temperature we examine, with the protection degrading smoothly as the mean thermal occupation increases. For a single qubit, the energy-basis coherence of a pure superposition leads to better long-time retention than fully excited state, highlighting the beneficial role of quantum coherence in protecting stored energy against thermal degradation. For two-qubit batteries, Bell-state preparations exhibit enhanced long-time ergotropy retention compared with the fully excited state, while the inclusion of qubit-qubit interactions produces only a weak dependence on the interaction type and strength within the parameter regime considered. Extending the analysis to multi-qubit GHZ-charged batteries with all-to-all Heisenberg interactions, we find that the normalized retained ergotropy increases monotonically with the number of qubits. This behavior is consistent with the collective enhancement of the qubit-cavity coupling in the symmetric Dicke manifold, indicating that larger quantum batteries can benefit from improved protection against self-discharge. These findings establish cavity-assisted protection as a promising strategy for mitigating self-discharging and realizing of long-lived quantum batteries in experimentally accessible platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24002v1
- Title: Picosecond Schrödinger cat states for ultrafast optical quantum processing
- Authors: Mamoru Endo, Kan Takase, Takefumi Nomura, Tatsuki Sonoyama, Kazuma Takahashi, Sachiko Takasu, Daiji Fukuda, Takahiro Kashiwazaki, et al.
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.24002v1  pdf=https://arxiv.org/pdf/2606.24002v1.pdf

Abstract:
Non-Gaussian states are essential resources for universal, fault-tolerant optical quantum computing, but their generation rate remains limited by low heralding probabilities and operation in nanosecond temporal modes. Here, we demonstrate multi-photon generalized photon subtraction in picosecond optical wave packets, establishing the state-generation capability required for high-rate operation by addressing the temporal-mode bottleneck that has constrained the achievable rate. Two interfering ultrashort squeezed vacua are heralded by photon-number-resolving detection with a high-speed transition-edge sensor and characterized by pulsed homodyne detection matched to 10-ps temporal modes at a 5-MHz pump repetition rate. We reconstruct Wigner functions without loss correction that exhibit up to four distinct negative regions for four-photon heralding, together with an effective cat-state amplitude of $α_{\mathrm{eff}} = 1.69$. This amplitude approaches the range of practical relevance for fault-tolerant cat-code architectures and for adaptive breeding toward logical-qubit generation, while the picosecond temporal mode establishes a platform compatible with high-rate, scalable time-multiplexed photonic architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24036v1
- Title: Spectrally engineered collinear type-0 SPDC source with enhanced spectral brightness for entanglement distribution
- Authors: Dong-Gil Im, Jungmo Lee, Kyungdeuk Park, Dongkyu Kim, Yonggi Jo, Yong Sup Ihn
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24036v1  pdf=https://arxiv.org/pdf/2606.24036v1.pdf

Abstract:
Entangled photon sources with high spectral brightness are important resources for photonic quantum information processing, particularly in quantum communication and quantum networking where usable photon flux of entangled photons is often constrained by channel loss and source inefficiency. Here, we demonstrate a spectrally engineered type-0 spontaneous parametric down-conversion (SPDC) source with enhanced spectral brightness for entanglement distribution. By pumping a 30-mm ppKTP crystal with an ultra-narrowband laser slightly detuned from degeneracy, photon-pair generation is concentrated into a narrow spectral bandwidth while retaining the strong nonlinear interaction of type-0 phase matching. The source produces a coincidence rate of 44.6 kHz corresponding to a detected spectral brightness of 0.507 MHz/mW/nm. We further integrate the source into a Sagnac interferometer to generate polarization-entangled photon pairs and demonstrate entanglement distribution through a 2.56 km free-space round-trip channel. Our results show that spectral engineering provides a practical route to compact, spectrally bright entangled-photon sources for quantum communication applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24048v1
- Title: An Analysis of Speculative Window Decoders for Quantum Error Correction
- Authors: Jocelyn Li, Margaret Martonosi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24048v1  pdf=https://arxiv.org/pdf/2606.24048v1.pdf

Abstract:
Fault-tolerant quantum computing is essential for realizing the substantial computational speedups that quantum computing can bring, but it requires real-time error decoding with high performance. Speculative window decoding improves performance by reducing the time spent waiting for dependencies from prior decoding windows.   However, speculative decoders have only been evaluated under the regime of superconducting qubits with fast gate speeds, surface codes, and matching decoders. Since different quantum technologies can have slower gate speeds, we evaluate the performance of speculative decoding under slow gate speeds. We also examine its sensitivity to speculation accuracy, decoder latency, processor count, and workload parallelism, which can vary across different quantum error correction codes, decoders, and hardware platforms.   This work presents design principles for identifying when speculative decoding yields the greatest performance improvements. It also reveals the conditions under which non-speculative decoders outperform speculative decoders.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24170v1
- Title: Low Spatial Cost CCZ Magic State Factory
- Authors: Sungyeon Kook, Yujin Kang, Ilkwon Sohn, Jun Heo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24170v1  pdf=https://arxiv.org/pdf/2606.24170v1.pdf

Abstract:
We propose a design framework for reconstructing gate-based magic state distillation protocols as compact joint-measurement architectures implementable with the surface code. The goal is to reduce the surface-code resource cost of a magic state factory while preserving the logical function and error-detection structure of the distillation protocol. We construct a reduced architecture for implementing an eight-to-three CCZ distillation protocol using smaller surface-code patches. The proposed factory preserves the single-fault-detection property and the leading-order error suppression of the protocol, while producing CCZ magic states with lower spatial cost than the design of Gidney and Fowler. The proposed design perspective can also be applied to T-state factories and other multiqubit non-Clifford resource-state factories. Our approach provides a framework for extending the design space of surface-code magic state factories beyond a single CCZ layout optimization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24185v1
- Title: Initial-state-dependent dephasing effect in non-Hermitian Su-Schrieffer-Heeger models
- Authors: Tao Min, Junjie Liu
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2606.24185v1  pdf=https://arxiv.org/pdf/2606.24185v1.pdf

Abstract:
Understanding the dynamical evolution of non-Hermitian systems under extra external dissipation is essential. Dephasing, a major realistic dissipation, is conventionally considered detrimental to information processing. However, its impact on non-Hermitian systems remains largely unexplored. Here, we focus on finite-sized non-Hermitian Su-Schrieffer-Heeger (SSH) lattice models with alternating gain and loss in real space and examine the dynamical evolution of the trace distance under pure dephasing. By tuning system parameters, this model supports phases with either parity-time or anti-parity-time symmetries, enabling us to explore the interplay between dephasing and different non-Hermitian symmetries. While the trace distance exhibits distinct dynamical behaviors across the different phases in the absence of dephasing, its response to dephasing is largely symmetry-independent but instead initial-state dependent. By varying initial states, we observe that increasing the dephasing strength can either merely accelerate the decay of the trace distance or stabilize it. Interestingly, we reveal two kinds of dephasing-induced stabilization that differ in the strong dephasing limit: a partial stabilization, where the trace distance approaches a finite value smaller than its initial value in the long-time limit, and a complete stabilization, where the trace distance remains at its initial value throughout the entire evolution. By analyzing the equation of motion, we attribute the initial-state dependent dephasing effect to the alternating gain and loss in the system and confirm its absence in Hermitian counterparts. Furthermore, in the anti-parity-time symmetry unbroken phase, we identify a continuous suppression-upon increasing the dephasing strength-of the otherwise exponential decay of the trace distance seen in the absence of dephasing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24205v1
- Title: From Spectral Singularities to Multipartite Entanglement Scaling at Higher-Order Exceptional Points
- Authors: Chunlai Yang, Shuheng Liu, Xinyao Huang, Kaiye Shi, Qiongyi He
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24205v1  pdf=https://arxiv.org/pdf/2606.24205v1.pdf

Abstract:
Exceptional points (EPs) are non-Hermitian spectral singularities exhibiting fractional-power responses, yet their implications for multipartite entanglement of interacting quantum many-body systems remain largely unexplored. Here we develop a general framework that links higher-order non-Hermitian degeneracies to the scaling behavior of genuine multipartite entanglement in interacting identical-qubit systems. Permutation symmetry of the identical qubits decomposes the exponentially large Hilbert space into independent irreducible-representation sectors, thereby constraining the maximal EP order of $N$ qubits to $N+1$ rather than $2^N$. Near an $n$th-order EP, genuine multipartite entanglement inherits the spectral response and generically exhibits a fractional-power scaling under weak perturbations. Explicit examples show that conventional two-body interactions support third- and fourth-order EPs with the corresponding entanglement responses, whereas higher-order EPs with genuine multipartite-entangled coalesced states require additional independent interaction channels, such as three-body interactions. Our results establish a fundamental connection among non-Hermitian degeneracies, multipartite entanglement, and symmetry, extending higher-order EP physics from spectral singularities to genuine many-body quantum correlations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24238v1
- Title: Ground-State Energy Solutions of the Lithium Atom: Zeroth-, First-, and Second-Order Perturbation Theory and the Variational Method
- Authors: Afraa Mahboubi, Büşra Gökçe Zolmaz, Devrim Karayer, Handenur Şay, Oğuzhan Kaya, Abdulkadir Senol
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2606.24238v1  pdf=https://arxiv.org/pdf/2606.24238v1.pdf

Abstract:
In this work, the ground-state energy of the lithium atom is systematically investigated using both time-independent perturbation theory and the variational method to provide a comprehensive pedagogical analysis of many-body atomic systems. The unperturbed Hamiltonian is initially constructed by neglecting electron-electron interactions, treating the system as three independent hydrogen-like electrons to yield a zeroth-order energy baseline of -275.51 eV. The antisymmetric fermionic nature of the exact wave function is rigorously enforced through the Slater determinant formalism. First-order perturbation theory is applied to evaluate static inter-electronic repulsion using exact Coulomb and exchange integrals, refining the energy state to -192.01 eV. To account for dynamical electronic correlation, second-order perturbation theory is computed numerically for virtual single-electron s-orbital transitions, leading to a total perturbative energy of -196.36 eV. A brief discussion of two-electron excitations is also included to encapsulate further physical realism within the framework. Furthermore, a non-orthogonal two-parameter variational approach is employed to model the shell-specific shielding effect. By optimizing the effective nuclear charges, the variational method establishes a superior upper bound energy of -201.187 eV. The results of both methods are comprehensively contrasted against each other and the reference baseline to provide critical insights into the nature of electron correlation and screening in multi-electron atoms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24242v2
- Title: Monitoring Beam Splitter Entanglement using Quantumness
- Authors: Hua-Li Chen, Hsien-Yi Hsieh, Chien-Ming Wu, Ole Steuernagel, Ray-Kuang Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24242v2  pdf=https://arxiv.org/pdf/2606.24242v2.pdf

Abstract:
We report on an experiment in which two independent squeezed vacuum states get entangled by mixing them with a balanced beam splitter. We follow standard practice and use an inseparability criterion to quantify their entanglement. However, this only allows us to witness the entanglement, but not to determine the deleterious effects of experimental imperfections due to the beam splitter mixing and the associated mode-mismatch and detection imperfections. We therefore introduce an alternative framework suitable for continuous variable systems using the states' quantumness, $Ξ$. We show that, under ideal circumstances, $Ξ$ is a conserved quantity under beam mixing. This allows us to benchmark the experiment's performance by comparing the states' quantumness $Ξ$ after the beam splitter mixing with $Ξ$ before. Such a comparison is not possible with entanglement witnesses, as the input states are unentangled. This highlights the main strength of our approach: its ability to generally quantify the quantumness of multi-mode continuous variable states and use this to probe different stages in an experiment.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24310v1
- Title: Non-adiabatic transitions in the density matrix formalism
- Authors: Pasquale Di Bari, Shreya Pandit, Ye-Ling Zhou
- Categories: quant-ph (primary); quant-ph; hep-ph
- Links: abs=https://arxiv.org/abs/2606.24310v1  pdf=https://arxiv.org/pdf/2606.24310v1.pdf

Abstract:
We show that a density matrix formalism provides a useful description of non-adiabatic transitions in two-state quantum systems.   Compared to a traditional Hamiltonian formalism, even in the absence of decoherence when there is full equivalence between the two, the density matrix formalism provides a convenient change of variables that yields a powerful general analytical solution. This solution nicely describes a transition regime between the well known Landau-Zener-Stuckelberg-Majorana (LZSM) approximation and the extremely non-adiabatic limit. Our results have very general applications, within a large variety of problems in quantum physics, neutrino physics, cosmology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24334v1
- Title: Wigner's Phase Space Current for Variable Beam Splitters -- Phase Space Rotations and Newtonian Trajectories
- Authors: Ole Steuernagel, Hsien-Yi Hsieh, Hua-Li Chen, Ray-Kuang Lee
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.24334v1  pdf=https://arxiv.org/pdf/2606.24334v1.pdf

Abstract:
Beam splitters allow us to superpose two continuous single mode quantum systems. To study the behaviour of beam splitters' strongly mode mixing dynamics we consider variable beam splitters acting on Wigner's phase space distribution, W , the evolution of which is governed by the continuity-equation {\partial τ} W = - {\nabla} J. We derive the form of the corresponding Wigner current, J. J's form allows us to use a classical trajectories-approach to analyze the influence of the two modes on each other. We show that the dynamics for variable beam splitters amounts to a rotation confined within the plane of the two positions together with the same simultaneous rotation confined within the plane of the two momenta. In this way explicit and very transparent expressions for the rotated Wigner distributions and Wigner currents can be given in terms of classical trajectories. This helps us to gain deeper insights and perform geometrical analyses of the mixing of modes at beam splitters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24360v1
- Title: Multipartite synchronization residuals in driven-dissipative spin networks
- Authors: Jatin Ghildiyal, Shubhrangshu Dasgupta, Asoka Biswas
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24360v1  pdf=https://arxiv.org/pdf/2606.24360v1.pdf

Abstract:
We introduce a phase-space measure of quantum synchronization that quantifies relative phase localization for two-qubit and three-qubit systems. This measure is built from the first angular moments of phase distributions obtained from Husimi-Q quasiprobability functions. Using this framework, we formulate a new class of synchronization residuals, motivated by subadditivity-type hierarchies of information-theoretic measures. We investigate these residuals in a driven-dissipative quantum Rabi network in the dispersive adiabatic regime. We show that, for two qubits, collective synchronization remains bounded by single-qubit contributions yielding a non-negative bipartite residual. The three-qubit nonequilibrium steady state exhibits a negative tripartite residual, which indicates collective phase synchronization, which cannot be described by pairwise decomposition. The corresponding entropy-based residuals, however, remain non-negative in both cases. Our results therefore, underscore that phase-sensitive synchronization measures and entropic correlation measures probe distinct aspects of open-system dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24368v1
- Title: Intrinsic spectral structure of bipartite nonlocal magic resource
- Authors: Xiao Huang, Guanhua Chen, Yao Yao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24368v1  pdf=https://arxiv.org/pdf/2606.24368v1.pdf

Abstract:
Bipartite nonlocal magic resource (BNMR) quantifies the irreducible nonstabilizerness residing in bipartite entanglement, yet its evaluation is intractable due to the full Hilbert space optimization. Here, we introduce a canonical encoding framework that exactly confines the BNMR of an arbitrary bipartite pure state within a minimal encoding core. This dimension reduction proves that pure-state BNMR is an intrinsic function of the nonzero Schmidt spectrum, extending its invariance from local unitary transformations to local isometries. Leveraging this spectral link, we derive the leading quadratic response of BNMR under spectral perturbations around its zeros. We apply this quadratic response to Haar-random states, deriving and numerically validating the BNMR profile: its distribution is sharply localized at the symmetric bipartition and exponentially suppressed toward asymmetric cuts, in stark contrast to the broadening Page curve of entanglement. Finally, we provide a closed-form expression for the BNMR of Schmidt rank-2 states, uncovering a hierarchy collapse in generalized GHZ states where bipartite and global nonlocal magic resources coincide exactly.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24431v1
- Title: Free-Space CV-QKD with Single-Mode Fiber Reception: Effective Coupling Statistics and Protocol-Dependent Reference Noise
- Authors: Hesham S. Ibrahim, Arnaud Coatanhay
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24431v1  pdf=https://arxiv.org/pdf/2606.24431v1.pdf

Abstract:
We study free-space continuous-variable quantum key distribution (CV-QKD) with single-mode fiber (SMF) reception under atmospheric turbulence. The optical channel is modeled by split-step propagation through random phase screens, followed by finite-aperture collection and projection onto the guided receiving mode. We first examine the standard GG02 setting and ask which receiver-side observable is sufficient for effective key-rate prediction. We show that a mean-loss description is generally too optimistic, whereas a scalar effective law for the SMF coupling efficiency provides an accurate downstream Gaussian-channel description within the effective model considered here. We then extend the optical model to a pilot-assisted architecture in which the signal and pilot propagate through correlated but non-identical turbulent realizations generated by a frozen-flow construction. In this case, the signal coupling law alone is no longer sufficient: signal--pilot phase mismatch and loss of post-coupling coherence produce an additional protocol-dependent reference-noise penalty. The results distinguish two regimes: a scalar coupling description is largely adequate for GG02, while transmitted-reference architectures require an additional differential reference observable beyond the signal coupling statistics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24456v1
- Title: Interaction-Enhanced Ergotropy in Phase-Driven Andreev Bound State Quantum Batteries
- Authors: Disha Verma, B. Vigneshwar, R. Sankaranarayanan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24456v1  pdf=https://arxiv.org/pdf/2606.24456v1.pdf

Abstract:
We investigate a phase-driven quantum battery composed of two interacting Andreev bound state (ABS) units, providing a minimal superconducting platform for coherent energy storage. By analyzing the ergotropy dynamics under a superconducting phase ramp, we show that the interplay between avoided-crossing excitation and interaction-induced hybridization strongly modifies the charging process. In the high-transparency regime relevant for graphene SNS junctions, the interaction enhances the stored extractable work and generates pronounced oscillatory charging dynamics associated with coherent redistribution between coupled ABS sectors. The phase-resolved evolution further reveals optimal charging windows during the Josephson cycle, indicating the possibility of phase-programmable energy extraction through partial-cycle operation. Overall, our results identify interaction-assisted avoided-crossing dynamics as a microscopic mechanism for controllable energy storage in superconducting quantum batteries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24469v1
- Title: When to Skip Syndrome Extraction in Surface-GKP Codes
- Authors: Vaughn Sohn, Changhun Oh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24469v1  pdf=https://arxiv.org/pdf/2606.24469v1.pdf

Abstract:
Fault-tolerant quantum error correction requires repeated syndrome extraction to address errors induced by the syndrome-extraction circuit itself. However, repeated syndrome extraction incurs significant overhead in terms of gate count and ancilla consumption (e.g., Gottesman-Kitaev-Preskill (GKP) states). Moreover, noisy syndrome extraction can itself inject additional errors into the data qubits. To address these issues, we propose a concrete adaptive skipping scheme for the surface-GKP code, a representative GKP-concatenated architecture, that uses analog information naturally generated during inner GKP correction. At each round, the scheme selects one of four actions: measuring both Z-type and X-type surface-code stabilizers, measuring only one type, or skipping both types and reusing previous syndromes. The decision is based on a reliability comparison between reusing the previous syndrome value and performing a new noisy syndrome extraction. Using circuit-level simulations, we show that the adaptive skipping scheme can reduce the number of surface-code stabilizer measurements while maintaining logical error rates comparable to or lower than those of the full-measurement baseline. The improvement is most pronounced when gate and measurement noise are larger than idle noise, so that avoiding unnecessary syndrome extraction reduces the noise injected into the code. These results indicate that analog information from inner GKP correction can be used not only to improve decoding but also to reduce the measurement overhead of outer-code syndrome extraction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24475v1
- Title: Exact log-depth preparation of highly entangled matrix product states
- Authors: Keisuke Murota, Frédéric Sauvage, Marco Ballarin, Gabriel Matos, Enrico Rinaldi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24475v1  pdf=https://arxiv.org/pdf/2606.24475v1.pdf

Abstract:
Preparing matrix product states (MPS) on a quantum device is a key subroutine in many quantum algorithms. The most competitive methods, based on the renormalisation group, prepare translationally invariant MPS of size $L$ and bond dimension $χ$, up to an error $\varepsilon$, in circuit depth $\tilde O(χ^{4}\log(L/\varepsilon))$ or $\tilde O(χ^{6}\log\log(L/\varepsilon))$. We improve multiple aspects of these methods. First, using block-encoded correction maps, whose post-selection succeeds with constant probability, we render the preparation exact without sacrificing the scaling in $L$. Second, through a generalisation of oblivious amplitude amplification to isometries, we reduce the bond-dimension dependence, improving the depth to $\tilde O(χ^{2}\log L + χ^{4})$ or $\tilde O(χ^{2}\log\log L + χ^{4})$, and even to $\tilde O(χ^{3}\log L)$ for incoherent preparations. Finally, we extend the framework to non-translationally invariant MPS and prove logarithmic-depth exact preparation for independent and identically distributed random tensor sequences. Confirmed by numerical studies, these results constitute, to the best of our knowledge, the most efficient exact MPS preparation protocols in the relevant parameter regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24507v1
- Title: Uncovering Latent Structures in Robust Pulse Sequences: A Model-Based Reinforcement Learning Approach for Adaptable Quantum Control
- Authors: Tobias Kiermeyer, Thomas Heydenreich, Léo Van Damme, Sebastian Hohenemser, Florian Marquardt, Steffen J. Glaser
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24507v1  pdf=https://arxiv.org/pdf/2606.24507v1.pdf

Abstract:
Real-time adaptive control of quantum systems requires rapid generation of robust, high-fidelity pulses across a continuous range of operating conditions. Standard optimization algorithms such as gradient-ascent pulse engineering (GRAPE) solve each instance independently, discarding information between runs and requiring costly reinitialization when parameters change. We present an approach to robust optimal quantum control based on model-based reinforcement learning, in which a single neural network -- embedding the Hamiltonian directly into the training pipeline -- generates robust gates across an entire family of gate configurations, without pre-computed training data. Demonstrated on a single-spin (two-level) system, the trained networks produce pulses for arbitrary rotation angles over a range of pulse durations, detunings, and field inhomogeneities in milliseconds, at fidelities comparable to multi-seed GRAPE. The framework is inherently adaptable: any parameter entering the Hamiltonian can serve as a network input, extending the approach to different systems and control settings. Beyond speed, the network reveals structure in the control landscape: it discovers the same structured phase profiles that appear in GRAPE solutions -- made identifiable through fidelity-invariant symmetry transformations -- but more consistently than independent optimization. This consistency enables smooth interpolation across the entire trained parameter space.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24511v1
- Title: How rare are Markovian quantum dynamics?
- Authors: Charlotte Bäcker, Nick Maryshchak, Walter T. Strunz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24511v1  pdf=https://arxiv.org/pdf/2606.24511v1.pdf

Abstract:
A profound understanding of decoherence and dissipation in quantum dynamics is crucial for the realistic modeling of the evolution of quantum systems. In open quantum dynamics one distinguishes between a memoryless, so-called Markovian evolution and dynamics incorporating memory effects, termed non-Markovian. In this work we study how prevalent memory effects are in the set of all such dynamics. We thus investigate how often a Markovian description is applicable. This question is approached by investigating randomly generated two-step qubit dynamics with respect to different concepts and witnesses of non-Markovianity. We observe that almost all dynamics are non-Markovian, and only a small (yet finite) fraction is Markovian. Furthermore, we study how this proportion changes when considering certain subclasses such as lower rank or mixed-unitary dynamics. Importantly, our results shed light on the relative ratios of -- and interrelations between -- the sets of dynamics that are non-Markovian with respect to different criteria. Finally, we investigate the fraction of dynamics in which the memory effects are necessarily of quantum nature and establish a connection between two recently developed concepts that characterize the quantumness of memory in non-Markovian dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24522v1
- Title: No-deleting principle for two unitary copies
- Authors: Dafa Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24522v1  pdf=https://arxiv.org/pdf/2606.24522v1.pdf

Abstract:
Pati and Braunstein defined a deleting machine and showed the impossibility of deleting one of two identical copies of an unknown quantum state. So far, no one has defined two non-identical copies of a quantum state, of course no one has discussed the impossibility of deleting one of two non-identical copies of an unknown quantum state. In this paper, we define $u|ψ>$ and $U|ψ>$, where $u$ and $U$ are any unitary operators, as two unitary copies of a quantum state $|ψ>$, and show that it is impossible to delete one of two unitary copies of an unknown state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24540v1
- Title: Offline Channel-Independent QAOA Angles for RIS Power Aggregation: Unit-Circle Phase Dictionaries and Infinite-Size Spin-Glass Limits
- Authors: Burhan Gulbahar
- Categories: quant-ph (primary); quant-ph; eess.SP
- Links: abs=https://arxiv.org/abs/2606.24540v1  pdf=https://arxiv.org/pdf/2606.24540v1.pdf

Abstract:
Reconfigurable intelligent surfaces (RIS) maximize received power by setting per-element phases. Discrete-phase optimization is NP-hard in the worst case, while the quantum approximate optimization algorithm (QAOA) applied to RIS faces limited phase alphabets, either per-problem angle optimization or uncharacterized training cost exposed to barren plateaus, and no scalable performance benchmark. We introduce a $2^{M}$-phase $θ$ dictionary for optimizing power $\|\mathbf{A} \, e^{jθ}\|^{2}$ having $K \times N$ channel matrix $\mathbf{A}$ and QAOA angle offline optimization with instance and size-independent infinite-size limit of the mixed-$q$ Gaussian ensemble of Basso et al. Our design bounds the spin-Hamiltonian interaction order to at most quartic for any $M$, and the deployed order-2 reduction lies below the even-$q\!\ge\!4$ regime in which constant-level QAOA limitations are proved. We perform analytical, state-vector, matrix-product-state and Pauli-path-simulation numerical studies for $N=K \leq 100$ and QAOA depth $p=9$, verifying offline angle transfer to Rayleigh, Rician/line-of-sight, cascaded double-fading and spatially-correlated RIS channels at $N\!\in\!\{5,12\}$. We observe performance reaching a near-optimal multi-start single-flip local-search reference for $N\!\le\!16$ under order-2 modeling with $2^{5}{=}32$-phase dictionary while the order-4 model shows a performance ceiling below the classical reference. The approach suggests a route to near-optimal large-$N$ performance on future fault-tolerant (FTQ) quantum computers, which enable the higher-depth QAOA circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24559v1
- Title: Electrical-Circuit Simulation of the Uhlmann Phase
- Authors: Yu-Huan Huang, Yu Wang, Jia-Chen Tang, Xu-Yang Hou, Hao Guo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24559v1  pdf=https://arxiv.org/pdf/2606.24559v1.pdf

Abstract:
The Uhlmann phase extends the concept of geometric phases to mixed quantum states through a parallel-transport condition on purification amplitudes, but its experimental realization has so far required sophisticated quantum platforms with carefully engineered auxiliary degrees of freedom. In this work, we reformulate the Uhlmann parallel-transport condition as a linear matrix differential equation and vectorize it to obtain an effective dynamical generator. This generator can be directly mapped onto the admittance matrix of a classical RC circuit, thereby translating the Uhlmann dynamics into the evolution of circuit node voltages. We illustrate the mapping using the equatorial-loop model and, via a rotating-frame transformation followed by a real decomposition, derive a time-independent, real-valued dynamical system suitable for analog implementation. LTspice simulations of the resulting active RC network faithfully reproduce the Uhlmann geometric phase and its topological transition at the critical purity, demonstrating that classical electrical circuits offer a simple and accessible platform for probing mixed-state geometric phases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24572v1
- Title: The Vector and Canonical Components of the Momentum Operator in 3D Euclidean Space Spanned by General Curvilinear Coordinates
- Authors: M. S. Shikakhwa
- Categories: quant-ph (primary); quant-ph; math-ph; physics.ed-ph
- Links: abs=https://arxiv.org/abs/2606.24572v1  pdf=https://arxiv.org/pdf/2606.24572v1.pdf

Abstract:
We construct the Hermitian vector and canonical components of the momentum operator in 3D Euclidean space spanned by general curvilinear coordinates (GCC's) using a simple, natural and unified approach based on identifying the momentum operator in any coordinate system as mass times the velocity operator. When this latter is calculated by applying the Heisenberg equation of motion, it returns ($-i\hbar$ times) the gradient operator plus an additional zero-valued sum, which when distributed among the components of the gradient, it makes each the Hermitian vector component of the momentum operator in GCC's. The canonical components follow immediately upon symmetrizing each of these vector components in the corresponding base vector. For accessability by wider audiences, we first develop the formalism for the simple polar coordinates and then we develop the case for GCC's.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24591v1
- Title: Auxiliary Schmidt Rank as a Resource for Photonic Bell Measurements
- Authors: Pradip Laha, Peter van Loock
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24591v1  pdf=https://arxiv.org/pdf/2606.24591v1.pdf

Abstract:
In quantum communication and fusion-based quantum computation, photonic Bell measurements are fundamentally limited when only passive linear optics is employed. While for qubits, some Bell states can be unambiguously identified with static beam splitters and no extra photons or entanglement, additional auxiliary photons or at least additional auxiliary degrees of freedom with a certain level of additional entanglement are needed to approach or attain a complete, deterministic Bell measurement. Here, we prove an exact resource threshold when the same two photons carry system qudits of dimension $d$ and a fixed auxiliary entangled state $Φ$, possibly distributed over several additional degrees of freedom, with total Schmidt rank $r_Φ$. We show that a single conclusive Bell-label functional can occur for $r_Φ\geqslant\lceil d/2\rceil$, but deterministic discrimination of all $d^2$ Bell-state labels requires $r_Φ\geqslant d$. A maximally entangled rank-$d$ auxiliary state achieves the bound by local Bell-basis sorting between each photon's system and auxiliary degrees of freedom. Thus, the auxiliary Schmidt rank is a certified resource for ancilla-photon-free, embedded photonic Bell measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24615v1
- Title: Quantum-enabled active matter at the atomic scale
- Authors: Sabrina Burgardt, Julian Feß, Alexander Guthmann, Silvia Hiebel, Aritra K. Mukhopadhyay, Sangyun Lee, Michael te Vrugt, Benno Liebchen, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.quant-gas; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2606.24615v1  pdf=https://arxiv.org/pdf/2606.24615v1.pdf

Abstract:
Active matter comprises particles that extract energy from their local environment and convert it into motion. Although active particles have been miniaturized down to the nanoscale, realizing activity at the fundamentally smaller scale of individual atoms remains an open challenge, where quantum effects become increasingly relevant. Here, we experimentally demonstrate that individual Cs-133 atoms confined in an optical dipole trap extract energy from an ultracold bath of Rb-87 atoms via quantum-mechanical spin interactions and convert it into active motion. We quantitatively reproduce the resulting dynamics using a parameter-free active Langevin model derived from kinetic theory and support it with event-driven Monte Carlo collision simulations. The microscopic origin of activity is identified as quantum spin exchange, which transfers discrete internal spin energy into kinetic motion. Our work establishes a quantum-enabled route to active matter at the fundamental size limit of single atoms and opens perspectives for exploring the interplay of activity, quantum physics, and mesoscopic non-equilibrium thermodynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24645v1
- Title: Reachability and optimal-time certificates for quantum control
- Authors: Younes Naceur, Llorenç Balada Gaggioli
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2606.24645v1  pdf=https://arxiv.org/pdf/2606.24645v1.pdf

Abstract:
Finite-time control is central to quantum technologies, yet rigorous limits on reachable targets and optimal control times remain largely unknown. We develop a framework for finite-time reachability and optimal-time certificates in constrained quantum control based on moment relaxations with implicitly time-dependent differential constraints. For fixed control horizons and control constraints, the method yields rigorous upper bounds on achievable terminal fidelities, lower bounds on the optimal control times required to reach them, and certificate gaps for benchmarking explicit control pulses. We demonstrate the versatility of our framework in three use cases: entangled-state preparation in two and three qubits, one-qubit gate synthesis across different control geometries, and excitation transfer in an $N$-qubit $XX$ chain. Our work establishes differential moment hierarchies as a practical tool for certifying reachability limits and optimal control times in quantum control, providing hardware-aware quantum speed limits while highlighting structure exploitation as a key ingredient for scalable certification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24659v1
- Title: Preparing multi-qudit states in a definite-weight subspace
- Authors: Nabi Zare Harofteh, Rafael I. Nepomechie
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24659v1  pdf=https://arxiv.org/pdf/2606.24659v1.pdf

Abstract:
We formulate a deterministic algorithm for preparing arbitrary multi-qudit states in a definite-weight subspace. By ordering the corresponding computational basis states according to a Gray code for multiset permutations, the state-preparation task is reduced to performing a sequence of controlled 2-qudit Gray rotations. We use this algorithm to prepare exact eigenstates of the SU(3)-invariant Heisenberg Hamiltonian, whose Bethe ansatz is nested. In particular, we describe the preparation of the Bethe states, which are SU(3) highest-weight states, as well as their lower-weight descendants. We also consider the preparation of $SU(d)$ Dicke states and their q-deformations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24681v1
- Title: A Universal All-Fiber Quantum Buffer for the Telecom Band
- Authors: Domenico Compagnini, Noemi Tagliavacche, Sara Congia, Andrea Bernardi, Marco Liscidini, Matteo Galli, Daniele Bajoni
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24681v1  pdf=https://arxiv.org/pdf/2606.24681v1.pdf

Abstract:
The realization of a scalable quantum internet relies on the ability to temporally align asynchronous photonic signals through on-demand buffering. While matter-based quantum memories achieve long storage times, their extremely narrow bandwidths and cryogenic requirements pose significant barriers to integration with existing telecommunications infrastructure. Conversely, current all-optical memories operate at room temperature but are hampered by high input/output losses and a lack of universality across different photonic degrees of freedom. Here, we demonstrate a universal, fully fiber-integrated quantum buffer operating over the full telecom C-band that overcomes these fundamental trade-offs. By implementing an actively switched dual-Sagnac cavity driven by cross-phase modulation, we achieve an ultra-low input/output loss of 0.46 dB and a storage time exceeding 18 $μ$s. The device exhibits an operational bandwidth exceeding 12.5 THz ($\sim$100 nm), covering the full telecom C-band. We show the simultaneous buffering of over 200 temporal modes with the ability to address them either collectively or one by one. We demonstrate high-fidelity storage for all three degrees of freedom compatible with optical fiber propagation, namely time-bin, frequency-bin, and polarization qubits, along with faithful preservation of entanglement, confirming the platform's true universality. These results provide a robust, room-temperature solution for the high-rate synchronization of multidimensional quantum states, clearing a major hurdle for the deployment of global photonic quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24705v1
- Title: Exceptional by Design: Long-Range Hopping as a Knob for Exceptional Point Control
- Authors: Carolina Martinez-Strasser, Dario Bercioux, Nico Leumer
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24705v1  pdf=https://arxiv.org/pdf/2606.24705v1.pdf

Abstract:
Exceptional points are degeneracies unique to non-Hermitian systems, where eigenvalues and eigenvectors coalesce, rendering the Hamiltonian defective. We investigate the exceptional-point structure and topological properties of a generalized non-Hermitian Rice-Mele model with balanced gain and loss, as well as next-nearest-neighbor hopping. The system hosts only second-order exceptional points under both periodic and open boundary conditions. Under periodic boundary conditions, the exceptional points in parameter space lie on lines and ellipses that are independent of the next-nearest-neighbor hopping, since the latter enters the bulk Hamiltonian only as an identity contribution. Under open boundary conditions, this independence is broken: the next-nearest-neighbor hopping not only shifts the energy of existing exceptional points but also generates new ones, with a specific condition signaling a topological gap closing observed only in the open-boundary spectrum. At special parameter points, multiple simultaneous second-order exceptional points yield degenerate configurations whose degeneracy grows with system size. Exceptional point locations are identified numerically via the condition number of the eigenvector matrix and confirmed by Jordan decomposition. The topological phase diagram, computed via a winding number framework for non-Hermitian systems without symmetry protection, reveals sectors with zero, one, and two edge states; the bulk-boundary correspondence is confirmed, and the non-Hermitian skin effect is absent.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24723v1
- Title: Rotational Vacuum Friction of Nonabsorbing Particles
- Authors: F. Javier García de Abajo, Alejandro Manjavacas
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24723v1  pdf=https://arxiv.org/pdf/2606.24723v1.pdf

Abstract:
A nonabsorbing particle rotating in vacuum can lose angular momentum only by converting mechanical energy into electromagnetic radiation. Here, we develop a quantum theory of rotational vacuum friction for small lossless particles and show that axial symmetry qualitatively changes the leading dissipation channel. At zero temperature, the frictional torque scales as $M\proptoΩ^7$ with rotation frequency $\ Omega$ in anisotropic particles due to the emission of correlated photon pairs whose frequencies sum to $2Ω$, while a contribution to the torque linear in $\ Omega$ is found at finite temperature. In contrast, axisymmetric particles are protected against photon-assisted friction regardless of temperature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24736v1
- Title: On the Limits of Stretching Quantum Pseudorandomness
- Authors: Boyang Chen, Andrea Coladangelo, Yao-Ting Lin, Nikos Skoumios, Justin Tysdal, Yiming Wang
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2606.24736v1  pdf=https://arxiv.org/pdf/2606.24736v1.pdf

Abstract:
Pseudorandom states, introduced by Ji, Liu, and Song (CRYPTO '18), are quantum analogues of classical pseudorandom generators. A fundamental property of classical pseudorandom generators is that their output can be stretched to arbitrary polynomial length. Whether an analogous stretching property holds for quantum pseudorandom states remains unclear.   In this work, we prove the first black-box separation between single-copy secure pseudorandom states ($\mathsf{1PRS}$) with different output lengths. Specifically, we construct a quantum oracle relative to which $\mathsf{1PRS}$ with output length $m(n)=1.1n$ exist, but $\mathsf{1PRS}$ with output length $m(n)=Ω(n^{2+ε})$ do not, for any $ε>0$. Our proof leverages the Common Haar Random State (CHRS) model introduced by Chen, Coladangelo, and Sattath (EUROCRYPT '25), and introduces a technique to bound the effective number of resource CHRS states utilized by any $\mathsf{1PRS}$ generator in this model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24746v1
- Title: Asymptotic Compression of Interactive Quantum Communication using Type-Constrained de Finetti Reduction
- Authors: Louis Desruisseaux, Simon Ducharme, Gurleen Padda, Dave Touchette
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.IT
- Links: abs=https://arxiv.org/abs/2606.24746v1  pdf=https://arxiv.org/pdf/2606.24746v1.pdf

Abstract:
For many information processing tasks, de Finetti-style theorems can often simplify the analysis in worst-case input scenarios for which the task exhibits some permutation-invariance symmetry, as they can allow for a reduction from an analysis on worst-case inputs to that of i.i.d. inputs. If further information is available on the inputs, it might be advantageous to reflect this information in the de Finetti reduction. In our work, we focus on a form of such constraint, based on the type of the input. This allows us to obtain a conceptually simple proof of a new de Finetti reduction for classical probability distributions, derived from elementary properties from the method of types. We apply our constrained de Finetti reduction to the compression of quantum interactive communication protocols with classical inputs, and prove that the prior-free quantum information cost equals the worst-case input amortized quantum communication cost.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24772v1
- Title: A high-fidelity two-qubit gate for multimode superconducting P-mon qubits
- Authors: Frederik Pfeiffer, Federico A. Roy, Niklas J. Glaser, Julius Feigl, Leon Koch, Kevin Kiener, Gleb Krylov, Johannes Schirk, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24772v1  pdf=https://arxiv.org/pdf/2606.24772v1.pdf

Abstract:
To scale superconducting quantum processors, it is essential to achieve long coherence times while engineering interactions that do not introduce additional decoherence channels. In superconducting qubit systems, this can be realized using multimode circuits that feature a protected qubit mode alongside a distinct mediator mode. Building on this concept, our recently developed P-mon qubit provides intrinsic protection against decoherence from the readout environment. We extend this approach to controlled two-qubit interactions, by exploiting the mediator modes of P-mons for on-demand coupling. Because direct interactions between the qubit modes are strongly suppressed, unwanted $ZZ$-type interactions are significantly reduced to below $3.6(5)~\text{kHz}$ in the idle state. When tuning the coupled mediator modes on resonance, the cross-Kerr interaction between the qubit and the hybridized mediator modes leads to a qubit-state dependent frequency shift. By selectively addressing these transitions, we implement a $180~\text{ns}$ long CZ gate and determine a fidelity of $99.62(4)~\text{%}$. These results represent a significant step toward a scalable superconducting architecture that maintains high performance at scale.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24789v1
- Title: Faster algorithm for achieving minimal-size quantum decision diagrams
- Authors: Juul Sanders, Sebastiaan Brand, Arend-Jan Quist, Tim Coopmans
- Categories: quant-ph (primary); quant-ph; cs.DS
- Links: abs=https://arxiv.org/abs/2606.24789v1  pdf=https://arxiv.org/pdf/2606.24789v1.pdf

Abstract:
The decision diagram (DD) data structure enables fast linear-algebra calculations by bringing vectors into a normal form and subsequently merging equivalent ones, yielding a minimally-sized DD modulo the equivalence relation. A fruitful application area is quantum-circuit simulation, where the vectors represent quantum states. The Local Invertible Map Decision Diagram (LIMDD) type, merges LIM-equivalent (typically Pauli-gate equivalent) vectors, can efficiently simulate Clifford circuits as well as some high-T-count circuits, and has theoretically been proven exponentially faster for simulation than other well-developed data structures, including other common DD variants. However, these exponential advantages have not fully materialized yet in existing implementations, for which the normal-form procedure, which is a highly complex algorithm, is either absent or only partially implemented. We here present a novel normal-form algorithm for Pauli-LIMDDs, achieving a worst-case speedup from $O(n^3)$ to $O(n^2)$ for an $n$-qubit DD node with a single child node while keeping the $O(n^3)$ run time in case of two distinct children nodes. We implement the algorithm as part of QolDDer, our Pauli-LIMDD simulator for quantum circuits, written from scratch in C/C++. The implementation realizes the theoretically-proven advantages of Pauli-LIMDDs on Clifford circuits, is significantly faster than the existing LIMDD simulators on such circuits, and on a public quantum-circuit data set often outperforms them by an order of magnitude. In the future, we envision that our work will enable further application and development of LIMDD variants, not only for quantum design tasks, but also for analysis of linear-algebra-based systems in general.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24792v1
- Title: Compressed Quantum Operators and Roots of Hermite Polynomials
- Authors: Serge Adonsou, Guillaume Dauphinais, David W. Kribs, Rajesh Pereira
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24792v1  pdf=https://arxiv.org/pdf/2606.24792v1.pdf

Abstract:
The fundamental position and momentum operators of quantum mechanics are unbounded, but finite rank compressions of the operators can be considered to obtain partial information on the operators and their properties. Motivated by problems in photonic quantum computing, we bring together results from quantum theory and the theory of orthogonal polynomials to show that a natural finite rank compression of the position and momentum operator representation on Fock space Hilbert space has eigenvalues given by roots of the classical Hermite polynomials. We discuss the corresponding compressed displacement operators and potential applications in approximate quantum error correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24798v1
- Title: Anomalous weak values in a generalized Mach-Zehnder interferometer extracted directly from intensity measurements
- Authors: Ismaele V. Masiello, Hartmut Lemmel, Andreas Dvorak, Stephan Sponar, Yuji Hasegawa
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.24798v1  pdf=https://arxiv.org/pdf/2606.24798v1.pdf

Abstract:
Weak values provide a powerful framework for characterizing quantum systems. Their experimental extraction conventionally relies on weak conditioned von Neumann measurements, involving weak interactions and meter states that increase experimental complexity and often limit measurement efficiency. Here we introduce a method to fully characterize path weak-values in a generalized Mach-Zehnder interferometer employing neither meter states nor weak interactions. We experimentally demonstrate the technique in matter-wave interferometry. We identify anomalous weak values and, equivalently, negative quasiprobability distributions, which reflect the nonclassical behavior of the quantum system. The approach relies uniquely on intensity measurements at the output ports of the interferometer combined with controlled relative phase shifts between the paths. The absence of meter states enables considerable simplification of the setup and shorter measurement times, while preserving full access to weak values with comparable or increased accuracy. The scheme is directly applicable to a broad class of experiments involving two-level quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24808v1
- Title: Large-Language-Model Discovery of Quantum LDPC Codes through Structured Concept Evolution
- Authors: Zidu Liu, Florian Marquardt
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2606.24808v1  pdf=https://arxiv.org/pdf/2606.24808v1.pdf

Abstract:
Quantum computers could outperform classical machines on important problems, but only if the errors that pervade quantum hardware can be corrected at scale. Quantum low-density parity-check (qLDPC) codes offer a promising route to this goal by combining sparse parity checks with finite encoding rate and growing distance, but their construction remains a challenging discrete design problem. Here we introduce structured concept evolution (SCE), a search framework that pairs a large language model with a structured algebraic mutation grammar to discover lifted-product code families, a class of CSS qLDPC codes. Instead of asking the LLM to design codes from first principles, SCE evolves structured concepts consisting of algebraic specifications paired with executable programs that realize them, using hierarchical mutations that modify the group algebra, protograph geometry, or base space. Running SCE, we discover a diverse set of competitive code families, ranging from abelian constructions to families over non-abelian groups beyond those underlying standard designs such as bivariate-bicycle codes, and characterize them under code-capacity depolarizing noise with BP+OSD decoding. These results are obtained with lightweight models (GPT-5.4-mini and GPT-5.4-nano).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24869v1
- Title: Rapid Cavity-Based Mid-Circuit Measurement and Feedforward in a Neutral Atom Array
- Authors: Tsai-Chen Lee, Jacquelyn Ho, Yue-Hui Lu, Tai Xiang, Nathaniel B. Vilas, Zhenjie Yan, Dan M. Stamper-Kurn
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2606.24869v1  pdf=https://arxiv.org/pdf/2606.24869v1.pdf

Abstract:
Measuring part of a quantum system in the midst of its evolution and acting on the result in real time is essential for numerous quantum information protocols. Neutral-atom arrays are a leading platform for quantum information processing, but their mid-circuit measurement-and-feedforward cycle times have remained slow, typically exceeding 1 ms. Here we demonstrate fast mid-circuit measurement and real-time feedforward in an array of atomic qubits coupled to a high-finesse optical cavity. Local light shifts tune individual data qubits out of resonance with the cavity, shielding their coherence, while a near-resonant probe drives a selected qubit whose emission is collected with Purcell enhancement. Mid-circuit measurements of four qubits with sub percent infidelity reduce the coherence of a fifth unmeasured data qubit by less than 2%. We implement real-time feedforward to correct measurement-induced phase shifts and to realize an adaptive circuit for optimal quantum state discrimination and conditional state preparation. Our approach reduces the measurement-and-feedforward cycle time to below 100 $μ$s and establishes optical cavities as a route to fast control of neutral-atom quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23785v1
- Title: Controlled Chaos in 4D SCFTs
- Authors: Florent Baume, Atakan Çavuşoğlu, Vivek Chakrabhavi, Jonathan J. Heckman
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.23785v1  pdf=https://arxiv.org/pdf/2606.23785v1.pdf

Abstract:
Chaotic dynamics play an important role in a number of physical systems. One of the qualitative hallmarks of this behavior is the appearance of a sufficiently "complex" spectrum of energy levels. This also makes it challenging to directly verify the onset of chaos in interacting quantum field theories. We present a class of 4D superconformal field theories (SCFTs) given by orbifolds of 4D $\mathcal{N} = 4$ Super Yang--Mills theory in which operator mixing in a controlled subsector is described by an effective spin chain in one spatial dimension with nearest neighbor interactions tuned by the marginal couplings of the SCFT. Tuning the marginal couplings results in a chaotic spectrum, while generically the spin chain exhibits Anderson localization. We diagnose the onset of chaos by analyzing the statistical distribution of eigenvalues of the dilatation operator, in particular properties such as eigenvalue level repulsion, spectral rigidity, and the spectral form factor. We also show that other diagnostics such as Krylov complexity sometimes do not faithfully capture this information. This structure defines a chaotic billiard in the target space of the stringy realization. We also comment on the large $N$ holographic dual description, where the controlled single spin chain approximation must be supplemented by multi-trace dynamics, i.e., the splitting and joining of multiple spin chains.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23799v1
- Title: Fermi surface change and $d$-wave superconductivity in the square lattice Kondo-Heisenberg model
- Authors: Alexander Nikolaenko, Riccardo Rende, Luciano Loris Viteritti, Subir Sachdev, Ya-Hui Zhang
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.dis-nn; cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2606.23799v1  pdf=https://arxiv.org/pdf/2606.23799v1.pdf

Abstract:
We study the two-dimensional Kondo-Heisenberg model on a square lattice, with the conduction electrons away from half-filling, using neural network quantum states. Mapping the ground-state phase diagram as a function of the Kondo and Heisenberg couplings, we identify (i) at weak Kondo coupling, antiferromagnetic Néel order with a Fermi surface whose enclosed area counts only the conduction electrons and is insensitive to the Néel order, and (ii) at strong coupling, a heavy Fermi liquid with a Fermi surface whose enclosed area counts both the conduction electrons and the spins. In the crossover between these regimes, we find $d_{x^2-y^2}$ superconductivity, evidenced by off-diagonal long-range order in the pair-pair correlations and a pairing-amplitude dome that coexists with the underlying magnetic phase. Our results establish Fermi volume change and unconventional superconductivity as intrinsic features of the two-dimensional Kondo-Heisenberg model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23810v1
- Title: Universal Dynamical Response to Slow Driving in Chaotic Systems
- Authors: Nachiket Karve, Nathan Rose, David Campbell, Anatoli Polkovnikov
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; nlin.CD; quant-ph
- Links: abs=https://arxiv.org/abs/2606.23810v1  pdf=https://arxiv.org/pdf/2606.23810v1.pdf

Abstract:
We propose a unified perspective on classical and quantum chaos based on the stability of a system's stationary states under slow driving. We probe this sensitivity via the system's susceptibility to the average protocol speed, which we call the ``speed-Fisher information," and relate it to irreversible entropy production in the system. We show that chaotic dynamics manifests as a divergence of the speed-Fisher information with the protocol time, and that this response is controlled by the perturbation's low-frequency spectral weight. This approach to chaos applies to both classical and quantum Hamiltonian systems, and naturally extends to non-Hamiltonian classical flows. We illustrate this framework with simple classical and quantum examples, along with a non-Hamiltonian flow that qualitatively exhibits analogous low-frequency spectral behavior.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23822v1
- Title: Quantum turbulence in the many-body regime
- Authors: Sayak Bhattacharjee, Mahendra K. Verma, Alexander V. Balatsky, Srinivas Raghu
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.str-el; nlin.CD; quant-ph
- Links: abs=https://arxiv.org/abs/2606.23822v1  pdf=https://arxiv.org/pdf/2606.23822v1.pdf

Abstract:
We discuss phenomenology associated with turbulent hydrodynamics in quantum fluids from a condensed-matter perspective. We begin with weakly-interacting superfluids, often modeled by a mean-field theory governed by the Gross-Pitaevskii equation. Considering the effect of quantum fluctuations beyond the mean-field approximation, we propose a study of many-body quantum effects in turbulent hydrodynamics, especially near zero temperature. We motivate examples of quantum many-body systems where such effects may be uncovered. These include bosons confined in a periodic potential in low spatial dimensions (one and two), and the associated quantum critical point of the superfluid-insulator transition, realized in present-day ultracold-atom and quantum computing platforms. We conclude by listing a set of (open) questions that may be answered using modern quantum many-body techniques. This article is part of the theme issue 'Frontiers of turbulence and statistical physics'.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23908v1
- Title: Analysis of the frequency shift in coherent population trapping resonance's dynamic continuous-wave spectroscopy at the phase-jump modulation and its comparison with the conventional approach
- Authors: E. D. Chivilis, E. A. Tsygankov
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.23908v1  pdf=https://arxiv.org/pdf/2606.23908v1.pdf

Abstract:
We present the research of dynamic continuous-wave spectroscopy of the coherent population trapping resonance at the phase-jump modulation. Λ system of levels supplemented by a nonabsorbing state and bichromatic optical field, whose spectral components have different intensities, are considered. We demonstrate that the asymmetry leads to an additional nonlinear shift of the error-signal frequency under unisotropic relaxation of the ground-state density-matrix elements. We also investigate the conventional approach where the frequency difference of the optical field components is harmonically modulated to obtain the error signal. Comparison demonstrates that in the high-frequency modulation regime the corresponding frequency shift is more linear than at the phase-jump modulation for nonshort integration times.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24150v1
- Title: Gate-Controlled Spin Qubits in Confined Altermagnets
- Authors: Hamed Vakili
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24150v1  pdf=https://arxiv.org/pdf/2606.24150v1.pdf

Abstract:
We propose gate-defined spin qubits in electrostatically confined altermagnetic quantum dots. Elliptical confinement of the $d$-wave altermagnetic structure produces a low-energy doublet with opposite spin polarization. For the range of parameters used here, the qubit states energy gap lies in the microwave range while the leakage gap remains in the meV range. Even without spin-orbit coupling, time-dependent simulations show that a phase-controlled quadrupolar gate drive about a fixed bias point implements $X_{π/2}$ and $X_π$ rotations by resonantly modulating the confinement anisotropy. We extend the study to two-qubits using a double quantum dot. We show that the double quantum dot spectrum can be cleanly projected onto isolated quantum dot product states with a nonzero nonlocal Pauli block in the effective logical two-qubit Hamiltonian. Resonant central-barrier modulation then drives the logical two-qubit component close to a maximally entangled state. These calculations show anisotropic altermagnetic quantum dots as a route to locally gate-controlled spin qubits without requiring spin-orbit coupling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24190v1
- Title: Dynamical low-rank methods for the Wigner equation I: separable difference potential
- Authors: Sihong Shao, Yuehan Shao
- Categories: math.NA (primary); math.NA; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24190v1  pdf=https://arxiv.org/pdf/2606.24190v1.pdf

Abstract:
Recent advances in dynamical low-rank approximation (DLRA) have demonstrated its effectiveness in high-dimensional simulations. However, existing DLRA algorithms still face significant challenges when handling systems that involve complex collision terms, including the pseudo-differential operator (${\rm Ψ}$) in the Wigner equation, a representative operator characterized by nonlocality. It is deserving to carry out a series of works to develop the DLRA algorithms for solving the Wigner equation. As the first step in this series of works, we propose an efficient DLRA algorithm for the Wigner equation, using a separable decomposition of the difference potential. We combine this separable assumption with two often-used truncations of ${\rm Ψ}$, namely $\mathcal{K}$-truncation and $\mathcal{Y}$-truncation, to obtain a kind of separated representation of ${\rm Ψ}$. Complexity analysis and several challenging experiments, including harmonic oscillators, Gaussian barrier scattering, electron-electron scattering, and a Helium-like system, all of which satisfy the separable assumption, confirm that the proposed DLRA algorithm has significant advantages, achieving a reduction in computational effort by one to two orders of magnitude in both runtime and memory requirements compared to the full-grid approach. It is worth noting that, even in the absence of a predetermined low-rank structure for the solution, DLRA can still serve as a numerical scheme that balances efficiency and accuracy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24247v1
- Title: Doppler-enhanced superheterodyne Rydberg microwave receiver
- Authors: Yuwen Yin, Ruimin Chen, Shibing Ji, Jinlian Hu, Shaofeng Wang, Yunhui He, Jingxu Bai, Xiao-Qiang Shao, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24247v1  pdf=https://arxiv.org/pdf/2606.24247v1.pdf

Abstract:
We report the enhanced sensitivity of the Rydberg microwave (MW) receiver by exploiting the Doppler effect in a vapor cell. A two-photon Rydberg ladder scheme is implemented via the co-propagation of probe and coupling lasers, which enhances the Doppler effect. When an MW field is applied, microwave dressing modifies the velocity-dependent resonance condition, enabling stronger contributions from atoms with non-zero velocities and leading to an enhancement of the EIT transmission. Based on this mechanism, we achieve a sensitivity of $35.1\ \mathrm{nV\ cm^{-1}\ Hz^{-1/2}}$ using the heterodyne technique, which is 1.5 times better than that obtained in the counter-propagating configuration. Meanwhile, the required local oscillator (LO) field is reduced by a factor of 17.6 compared with the counter-propagating configuration, which is advantageous for applications requiring minimal radiation and low power consumption. Moreover, the co-propagating configuration is more amenable to integration or portable sensing platforms because multiple laser fields can be delivered through a single optical fiber.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24264v2
- Title: Discovery of connectivity-trainability trade-off of IQP Circuits for Hamiltonian Optimization
- Authors: Quoc Chuong Nguyen
- Categories: cs.SI (primary); cs.SI; math.NA; physics.data-an; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24264v2  pdf=https://arxiv.org/pdf/2606.24264v2.pdf

Abstract:
Instantaneous Quantum Polynomial-time (IQP) circuits are promising candidates for near-term quantum advantage due to the conjectured classical hardness of their sampling task. However, their capabilities for optimization remain largely unexplored. We present a systematic investigation of the performance and trainability of IQP circuits for Hamiltonian optimization. Our results reveal a trade-off between optimization performance and circuit connectivity, demonstrating that the circuit structure plays a key role in determining the ability of IQP circuits to reach low-energy states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24312v1
- Title: Universal Extraction of Quantum Critical Exponents and Phase Transitions via Tailored Hilbert Space
- Authors: Ye Xiong
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.str-el; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24312v1  pdf=https://arxiv.org/pdf/2606.24312v1.pdf

Abstract:
Finite-size scaling and the renormalization group form the central toolkit   for analyzing quantum phase transitions (QPTs). In this Letter, we introduce   a novel Hilbert-space tailoring scheme to probe quantum critical phenomena.   Applied to the second-order QPT of the one-dimensional (1D) XY model, our method   yields precise critical points and exponents on lattices containing merely 50   unit cells. We further establish the universal applicability of this   framework via investigations of the Berezinskii-Kosterlitz-Thouless   transition in the 1D XXZ chain: critical parameters are recovered   with as few as 12 lattice sites. This technique may open an alternative,   efficient route to universally characterize QPT across many-body lattice systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24332v1
- Title: Enhancing quantum-classical configuration interaction methods using a neural-network classifier
- Authors: Severino Zeni, Giovanni Varutti, Jacopo Nespolo, Dimitrios Trypogeorgos
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24332v1  pdf=https://arxiv.org/pdf/2606.24332v1.pdf

Abstract:
Selected configuration interaction methods achieve near-exact electronic structure calculations by iteratively constructing compact variational spaces, but their efficiency depends critically on the heuristics used to identify important determinants. Here, we introduce a data-driven selection framework that recasts determinant importance as a binary classification task and integrates a neural-network classifier into the iterative CI workflow through an active-learning loop. At each iteration, a random subset of candidate determinants is labelled via temporary diagonalisation, and the trained classifier guides selection of the remaining configurations. We demonstrate the utility of this framework for both classical and quantum CI methods by calculating the ground-state energy of a diatomic molecule. Our method achieves result parity with traditional configuration interaction methods at substantially lower computational cost: roughly a $\times 5$ reduction in memory and per-iteration cost for the classical cHCI variant, and convergence in markedly fewer iterations for the quantum-classical cSQD variant. These results establish classifier-assisted determinant selection as a lightweight, method-agnostic tool for compressing variational spaces and accelerating both classical and hybrid quantum-classical configuration interaction algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24405v1
- Title: On the Berry-Keating Operator
- Authors: Fabio Bagarello, Sergiusz Kużel
- Categories: math-ph (primary); math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24405v1  pdf=https://arxiv.org/pdf/2606.24405v1.pdf

Abstract:
We review here two different viewpoints on the Berry-Keating operator $H_{BK}$, whose connection to the Riemann hypothesis remains an intriguing and not yet fully understood question, despite considerable attention in the recent literature. In particular, we propose two somehow complementary views to $H_{BK}$: the first is based on a purely Hilbertian point of view, on dilation operators and on the Mellin transform. The second is a distributional approach, with a specific view to ladder operators, generalized eigenstates of $H_{BK}$, and generalized coherent states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24440v1
- Title: Perfect State Transfer on Quotient Graphs in Shunt Decomposition-Based Quantum Walks
- Authors: Banita Katuwal, Srinath M S, Y Lakshmi Naidu, Supriyo Dutta
- Categories: math.CO (primary); math.CO; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24440v1  pdf=https://arxiv.org/pdf/2606.24440v1.pdf

Abstract:
This paper investigates perfect state transfer (PST) in discrete-time quantum walks constructed via the shunt decomposition method. The walks are defined on a graph $G$ and its associated quotient graph $G/π$, induced by an equitable partition $π$. Through the shunt decomposition of $G$, we derive an explicit relation between the shift operator of the parent graph $G$ and that of its quotient graph $G/π$. We construct a reflection operator based on the characteristic matrix, which establishes a connection between the transition operator of the parent graph and that of its lower-dimensional quotient graph. We then prove that PST occurs on $G$ if and only if it occurs on $G/π$. Furthermore, we express the unitary evolution operator of the quotient graph in terms of Chebyshev polynomials of the first kind, from which we derive explicit criteria for PST. As an application, we establish PST on the cycle graph $C_{n}$ at time $k = n/2$, and lift the result to the parent graph $C_{2n}$ via the equitable partition $π$. We further show that if an equitable partition $π$ of $G$ induces a quotient isomorphic to $K_n^{\circlearrowleft}$, the complete digraph on $n$ vertices with a loop at every vertex, then PST occurs at step $k = n$, and the walk is periodic at $k = 2n$. This framework is applied to two families of graphs, which are the complete bipartite digraph $K_{n,n}^{\rightleftharpoons}$ and the circulant graph $\operatorname{Circ}(2n, S)$, where $S$ consists of all odd residues modulo $2n$ and $n = 2^s$ for some $s \geq 1$, establishing PST in their respective line digraphs. Collectively, these results also answer the question posed by Godsil and Zhan concerning which shunt decompositions or embeddings of a graph admit PST.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24613v1
- Title: The $ω$-Effect from a Multimode Squeezed Graviton State
- Authors: Nick E. Mavromatos, Sarben Sarkar
- Categories: gr-qc (primary); gr-qc; hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24613v1  pdf=https://arxiv.org/pdf/2606.24613v1.pdf

Abstract:
The $ω$-effect in entangled neutral-meson systems provides a sensitive probe of CPT violation induced by quantum-gravitational environments. In open quantum systems, interactions with inaccessible gravitational degrees of freedom can render the reduced meson dynamics non-unitary, causing the CPT operator to become ill-defined, even when the underlying microscopic Hamiltonian is CPT invariant. We present a microscopic derivation of the $ω$-effect arising from a multimode squeezed gravitational environment generated by an axion cloud around a Kerr black hole. Using the Takagi decomposition of the associated complex symmetric squeezing kernel, the graviton field is expressed in terms of independent squeezed supermodes possessing anomalous correlators. These correlators provide a microscopic quantum counterpart of the stochastic fluctuations that appear in earlier D-particle foam descriptions of the $ω$-effect, replacing phenomenological variances of flavour-changing D-particle recoil by calculable graviton correlation functions. After tracing over the graviton bath, the anomalous correlators and the weak-interactions-induced mixing combine to generate transitions between the antisymmetric and symmetric two-meson sectors. This results in a small exchange-symmetric admixture, parametrised by $ω$, in the otherwise antisymmetric EPR state. We obtain an explicit expression for $ω$ in terms of a sum over Takagi supermodes weighted by their squeezing amplitudes and phases together with the weak-interaction flavour-mixing matrix element. The resulting framework suggests that the $ω$-effect may be a generic signature of non-classical states of gravitational environments, extending beyond the specific axion-cloud scenario considered here. The observability of the $ω$-effect from other astrophysical and microscopic black-hole sources is discussed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24643v1
- Title: The Quantum Split-Step Fourier Algorithm for Nonlinear Optical Waveguides
- Authors: Fabio Biancalana
- Categories: physics.optics (primary); physics.optics; nlin.PS; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24643v1  pdf=https://arxiv.org/pdf/2606.24643v1.pdf

Abstract:
We introduce the Quantum Split-Step Fourier (QSSF) algorithm for nonlinear optical waveguides, a numerical framework that combines split-step propagation of the nonlinear Schrödinger equation with a commutator-preserving Bogoliubov evolution of Gaussian quantum fluctuations. The method propagates the classical mean field together with the Bogoliubov matrices $U$ and $V$, from which reduced second moments, covariance matrices, symplectic eigenvalues, and entropic measures are constructed for arbitrary spectral windows. Applied to soliton-driven resonant radiation, QSSF shows that the selected radiation band acquires a steadily increasing von Neumann entropy and a corresponding loss of purity, quantifying its entanglement with the rest of the spectrum in the lossless Gaussian setting. The analysis also reveals a surprisingly pronounced low-dimensional structure: although the radiation occupies many Fourier bins, its reduced Gaussian state is dominated by only a few Williamson modes. QSSF therefore provides a practical information-theoretic diagnostic for quantum correlations in nonlinear frequency conversion, supercontinuum generation, and multimode squeezed-light formation in ultrafast waveguide platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24676v1
- Title: Nonlinear refractive index of warm rubidium vapor
- Authors: L. Kardum, G. Premec, N. Šantić, D. Aumiler
- Categories: physics.atom-ph (primary); physics.atom-ph; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24676v1  pdf=https://arxiv.org/pdf/2606.24676v1.pdf

Abstract:
The potential to precisely control both the linear and nonlinear index of refraction through optical manipulation of the atomic states has recently pushed warm alkali vapors to the forefront of research in the field of quantum sensors, quantum memories, and quantum fluids of light. Rubidium (Rb) vapor in centimeter-scale glass cells or millimeter-scale MEMS cells has proven to be a very promising platform for these applications, yet only a handful of research works have been dedicated to the investigation of the (non)linear refractive index of Rb vapor. We present results of theoretical calculations of the (non)linear refractive index of warm Rb vapor, based on the optical Bloch equations for 6-level Rb atoms interacting with a probe laser. They are compared to the experimental results obtained using an interferometric technique, showing excellent quantitative agreement. A Kerr nonlinear refractive index $n_2$ of up to $10^{-4}$ cm$^2$/W is obtained. Python scripts for all theoretical calculations presented in this work are provided, including the refractive index calculation, that can readily be used in practical implementations for simulating the (non)linear refractive index of Rb vapor including the effects of Doppler broadening, transit time broadening, pressure broadening, saturation, optical pumping, and spin-exchange collisions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24713v1
- Title: Symmetric mass generation of interacting chiral fermions on a one-dimensional lattice without fermion doubling
- Authors: V. A. Zakharov, Atsushi Ueda, Frank Verstraete, C. W. J. Beenakker
- Categories: hep-th (primary); hep-th; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24713v1  pdf=https://arxiv.org/pdf/2606.24713v1.pdf

Abstract:
Symmetric mass generation is the interaction-induced opening of a fermion gap without spontaneous symmetry breaking. The anomaly-free 3-4-5-0 model of Wang and Wen provides a minimal one-dimensional setting for this phenomenon, but a direct lattice realization faces two obstacles: fermion doubling for local chiral discretizations and perturbative irrelevance of the six-fermion gapping interaction. We address both obstacles. First, we formulate the model on a strictly one-dimensional tangent-fermion lattice, where a nonlocal hopping produces a single chiral branch without a mirror partner while retaining an efficient tensor-network representation. Second, we add a Hubbard-type density-density interaction (Luttinger parameter $K$) that reduces the scaling dimension of the 3-4-5-0 interaction from $5$ to $5K$, making it relevant for $K<2/5$. Density-matrix renormalization group calculations show the opening of an excitation gap in this regime without the appearance of a degenerate ground state, the hallmark of symmetric mass generation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24720v1
- Title: On the localization transition from MAA to AA models
- Authors: Hangdong Qiu, Yunhua Wang
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24720v1  pdf=https://arxiv.org/pdf/2606.24720v1.pdf

Abstract:
Despite their potential similarity between the mosaic Aubry-André (MAA) and AA models, the MAA model allows mobility edges (MEs), whereas the AA model does not. Here we develop a new double quasiperiodic MAA (DMAA) model consisting of one primitive MAA with nonzero even-site potentials and the other modified one with both nonzero odd-site potentials and a tunable amplitude factor, to reveal how localization transitions evolve from MAA to AA models. Interplays and competitions among the extended, critical and localized states arising from superpositions of double quasi-periodic MAA potentials enable new twice and multiple localization-delocalization transitions besides the original single localization transition. Our numerical calculations on inverse participation ratio, normalized participation ratio, fractal dimension and real-space wavefunction distribution confirm such localization features. The continuum model simulations on the experimental polariton modes also yield consistent results and hence validate their experimental feasibility. The constructed DMAA model provides a new framework for studying the localization transition processes between two analogous quasiperiodic models and broadens the understanding of Anderson localization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24765v1
- Title: Two-Electron Effects Extend High-Harmonic Generation into the keV Regime
- Authors: Isobel McSweeney, Andres Marchisio, Javier Rivera-Dean, Philipp Stammer, Paraskevas Tzallas, Marcelo F. Ciappina, Maciej Lewenstein
- Categories: physics.atom-ph (primary); physics.atom-ph; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24765v1  pdf=https://arxiv.org/pdf/2606.24765v1.pdf

Abstract:
Two-electron processes can generate high harmonics beyond the conventional single-active-electron cutoff. Motivated by recent experimental evidence of an extended secondary plateau in the helium high-harmonic spectrum [S. Wang et al, Optica, (2023); S. Wang et al, In Print in Nature Photon., (2026)], we present a two-electron generalisation of the strong-field approximation. We analyse the resulting expressions using the saddle-point method and determine the extended cutoff. We find good agreement with classical predictions of cutoff scalings of $4.7$ and $5.5$ times the ponderomotive energy, which significantly exceed the established single-electron scaling of 3.17. We calculate high-harmonic spectra generated via a two-electron process in helium atoms driven by an intense few-cycle infrared laser pulse. Our results demonstrate that the harmonic spectrum extends far beyond the water window, reaching photon energies up to $\approx 1.2\,\mathrm{keV}$ in the soft x-ray region. The large spectral bandwidth can support the generation of sub-attosecond soft x-ray pulses, which are of particular interest for probing ultrafast dynamics across matter, including applications in core-level spectroscopy and biological imaging.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24803v1
- Title: Introduction to matrix-product states and tensor networks
- Authors: Grégoire Misguich
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24803v1  pdf=https://arxiv.org/pdf/2606.24803v1.pdf

Abstract:
These notes provide an introduction to tensor-network methods in quantum many-body physics, with an emphasis on matrix-product states (MPS). They develop the basic tensor-network language, including graphical notation, virtual indices, bond dimensions, gauge freedom, canonical forms, QR and singular-value decompositions, and the role of entanglement in controlling the efficiency of the representation. The main MPS algorithms are then introduced, including contractions, correlation functions, matrix-product operators, DMRG, and time-evolution methods. The notes also briefly discuss projected entangled-pair states (PEPS) as a higher-dimensional generalization of MPS, together with the basic ideas behind approximate PEPS contraction. Finally, tensor-network representations of mixed states, quantum channels, and Lindblad dynamics are presented, with applications to thermal states and open quantum systems. The presentation is accompanied by short Julia code examples based on ITensor, ITensorMPS, and TensorMixedStates. These notes were written for the 9th Les Houches Summer School on Computational Physics: Open Quantum Systems, held in June 2026.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.24864v1
- Title: Universality beyond the Kibble-Zurek mechanism in the condensation of coherently coupled Bose gases
- Authors: Subhadeep Patra, Paolo Comaron, Arko Roy
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24864v1  pdf=https://arxiv.org/pdf/2606.24864v1.pdf

Abstract:
We study the universal spatial statistics of point-like topological defects formed during the nonequilibrium condensation of a coherently coupled Bose gas using the stochastic projected Gross-Pitaevskii equation. The symmetry-breaking transition is driven by a linear quench of the chemical potential, leading to stochastic vortex nucleation in the individual condensate components. When the two components are considered together, these elementary defects may combine across components to emerge as composite topological defects known as full quantum vortices. Beyond the mean defect density predicted by the Kibble-Zurek mechanism (KZM), we investigate the spatial organization of both the elementary and composite defects and show that their positions are well described by a Poisson point process, revealing a universal stochastic geometry. This universality is further described through Voronoi tessellation, whose cell-area statistics follow Poisson-Voronoi predictions. We also introduce the spatial form factor for characterizing the vortex configurations and demonstrate the emergence of a characteristic dip-ramp-plateau structure. Our results establish universal stochastic geometry of topological defects beyond conventional Kibble-Zurek scaling and identify it as a fundamental feature of nonequilibrium condensation in coherently coupled Bose gases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2406.07884v3
- Title: Reinforcement Learning to Disentangle Multiqubit Quantum States from Partial Observations
- Authors: Pavel Tashev, Stefan Petrov, Matthew T. Diaz, Friederike Metz, Alaina M. Green, Norbert M. Linke, Marin Bukov
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2406.07884v3  pdf=https://arxiv.org/pdf/2406.07884v3.pdf

Abstract:
Using partial knowledge of a quantum state to control multiqubit entanglement is a largely unexplored paradigm in the emerging field of quantum interactive dynamics with the potential to address outstanding challenges in quantum state preparation and compression, quantum control, and quantum complexity. We present a deep reinforcement learning (RL) approach using an actor-critic algorithm for constructing short disentangling circuits for states with up to 16 qubits. With access to only two-qubit reduced density matrices, our agent decides which pairs of qubits to apply two-qubit gates on; requiring only local information makes it directly applicable on modern NISQ devices, as we demonstrated experimentally on a trapped-ion quantum computer. Utilizing a permutation-equivariant transformer architecture, the agent can autonomously identify qubit permutations within the state, and adjusts the disentangling protocol accordingly. Once trained, it provides circuits from different initial states without further optimization. We demonstrate the agent's ability to identify and exploit the entanglement structure of multi-qubit states. We analyze the disentangling circuits constructed by the agent for 4- and 5-qubit Haar-random states, and observe strong correlations between consecutive gates and among the qubits involved. Through extensive benchmarking, we show the efficacy of the RL approach to find disentangling protocols with minimal gate resources. We explore the resilience of our trained agents to noise, highlighting their potential for real-world quantum computing applications. Analyzing optimal disentangling protocols, we report a general circuit to prepare an arbitrary 4-qubit state using at most 5 two-qubit (10 CNOT) gates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2505.00457v3
- Title: On estimating Schatten norm and power distances between quantum states
- Authors: Yupan Liu, Qisheng Wang
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.DS
- Links: abs=https://arxiv.org/abs/2505.00457v3  pdf=https://arxiv.org/pdf/2505.00457v3.pdf

Abstract:
We study the computational complexity of estimating the quantum Schatten $α$-norm distance ${\rm T}_α(ρ_0,ρ_1)$, given ${\rm poly}(n)$-size state-preparation circuits of $n$-qubit quantum states $ρ_0$ and $ρ_1$. This quantity serves as a lower bound on the trace distance and, for $α> 1$, is interchangeable with its powered version $Λ_α(ρ_0,ρ_1)$. For any constant $α> 1$, we develop an efficient rank-independent quantum estimator for ${\rm T}_α(ρ_0,ρ_1)$ with time complexity ${\rm poly}(n)$, achieving an exponential speedup over the prior best results of $\exp(n)$ due to Wang, Guan, Liu, Zhang, and Ying (TIT 2024). When $0<α<1$ is a constant, the quantum Schatten $α$-power distance $Λ_α(ρ_0,ρ_1)$ becomes a distance metric. Accordingly, we provide a rank-efficient quantum estimator for this quantity.   Our quantum algorithm reveals a dichotomy in the computational complexity of the Quantum State Distinguishability Problem with Schatten $α$-norm (QSD $_α$), which involves deciding whether ${\rm T}_α(ρ_0,ρ_1)$ is at least $2/5$ or at most $1/5$. This dichotomy arises between the cases of $α> 1$ and $0 < α\leq 1$:   1. For any constant $α>1$, QSD$_α$ is $\sf BQP$-complete.   2. For any $1 \leq α(n) \leq 1+{\rm negl}(n)$, QSD$_α$ is $\sf QSZK$-complete, implying that no efficient quantum estimator for ${\rm T}_α(ρ_0,ρ_1)$ exists unless ${\sf BQP}={\sf QSZK}$. This $\sf QSZK$-hardness result also extends to the promise problem defined by $Λ_α(ρ_0,ρ_1)$ for constant $0<α<1$.   The hardness results follow from reductions based on new rank-dependent inequalities for ${\rm T}_α(ρ_0,ρ_1)$ when $1\leq α\leq \infty$ and for $Λ_α(ρ_0,ρ_1)$ when $0<α<1$, which are of independent interest.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2506.00755v2
- Title: Exponential speedup in quantum simulation of Kogut-Susskind Hamiltonian via orbifold lattice
- Authors: Georg Bergner, Masanori Hanada, Emanuele Mendicelli
- Categories: quant-ph (primary); quant-ph; hep-lat; hep-ph; hep-th; nucl-th
- Links: abs=https://arxiv.org/abs/2506.00755v2  pdf=https://arxiv.org/pdf/2506.00755v2.pdf

Abstract:
We demonstrate that the orbifold lattice Hamiltonian -- an approach known for its efficiency in simulating SU($N$) Yang-Mills theory and QCD on digital quantum computers -- can reproduce the Kogut-Susskind Hamiltonian in a controlled limit. While the original Kogut-Susskind approach faces significant implementation challenges on quantum hardware, we show that it emerges naturally as the infinite scalar mass limit of the orbifold lattice formulation, even at finite lattice spacing. Our analysis provides both a general analytical framework applicable to SU($N$) gauge theories in arbitrary dimensions and specific numerical evidence for $(2+1)$-dimensional SU($N$) Yang-Mills theories ($N=2,3$). Using Euclidean path integral methods, we quantify the convergence rate by comparing the standard Wilson action with the orbifold lattice action, matching lattice parameters, and systematically extrapolating results as the bare scalar mass approaches infinity. This reformulation resolves longstanding technical obstacles and offers a straightforward implementation protocol for digital quantum simulation of the Kogut-Susskind Hamiltonian with exponential speedup compared to classical methods and previously known quantum methods, modulo a standard assumptions made also for the original Kogut-Susskind approach.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2506.13724v2
- Title: Logical qubits with erasure conversion using metastable neutral atoms
- Authors: Bichen Zhang, Genyue Liu, Guillaume Bornet, Sebastian P. Horvath, Pai Peng, Shuo Ma, Shilin Huang, Shruti Puri, et al.
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2506.13724v2  pdf=https://arxiv.org/pdf/2506.13724v2.pdf

Abstract:
Implementing large-scale quantum algorithms with practical advantage will require fault-tolerance achieved through quantum error correction, but the associated overhead is prohibitive. This overhead can be reduced by engineering physical qubits with fewer errors, and by shaping the residual errors to be more easily correctable. In this work, we demonstrate quantum error correcting codes and logical qubit circuits in a metastable ytterbium-171 nuclear spin qubit with a noise bias towards erasure errors. These errors can be located separately from any syndrome information diagnosing the error, and we demonstrate adaptive circuit execution based on erasure information. We show that dephasing errors on the qubit during coherent transport can be strongly suppressed, and implement entangling gates that maintain a high fidelity in the presence of gate beam inhomogeneity or pointing errors. Furthermore, we demonstrate logical qubit encoding in the [[4, 2, 2]] code, with error correction during decoding based on mid-circuit erasure measurements despite the fact that the code is too small to correct any Pauli errors. Finally, we demonstrate logical qubit teleportation between multiple code blocks with conditionally selected ancillas based on mid-circuit erasure checks, a key part of leakage-robust error correction schemes using neutral atoms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2506.22383v4
- Title: Higher-Order Adiabatic Elimination in Atom-Cavity Systems and Its Impact on Spin-Squeezing Generation
- Authors: Stefano Giaccari, Giulia Dellea, Marco G. Genoni, Gianluca Bertaina
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.22383v4  pdf=https://arxiv.org/pdf/2506.22383v4.pdf

Abstract:
Spin-squeezed states are metrologically useful quantum states where entanglement allows for enhanced sensing with respect to the standard quantum limit. Key challenges include the efficient preparation of spin-squeezed states and the scalability of estimation precision with the number $N$ of probes. Recently, in the context of the generation of spin-squeezed states via coupling of three-level atoms to an optical cavity, it was shown that increasing the atom-cavity coupling can be detrimental to spin squeezing generation, an effect that is not captured by the standard second-order adiabatic cavity removal approximation. We describe adiabatic elimination techniques to derive an effective Lindblad master equation up to third order for the atomic degrees of freedom. Numerical simulations show that the spin squeezing scalability loss is correctly reproduced by the reduced open system dynamics, highlighting the role of higher-order contributions. Furthermore, we conjecture an extension beyond leading order of the adiabatic elimination technique to the case of conditional dynamics under quantum non-demolition continuous measurement and fast cavity loss, whose reliability is again confirmed by numerical simulation of the dynamics and the corresponding behavior of spin squeezing as a function of $N$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2510.01065v2
- Title: Flexible Catalysis
- Authors: Máté Weisz, Sergii Strelchuk
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.01065v2  pdf=https://arxiv.org/pdf/2510.01065v2.pdf

Abstract:
In quantum information and computation, a central challenge is to determine which quantum states can be transformed into which others under restricted sets of free operations. While many transformations are impossible directly, catalytic processes can enable otherwise forbidden conversions: an auxiliary quantum state (the catalyst) facilitates the transformation while remaining unchanged. In this work, we introduce flexible catalysis, a generalization in which the catalyst is allowed to transform into a different auxiliary state, provided it remains a valid catalyst. We show that this framework subsumes both standard catalytic and multicopy transformations, and we analyse its advantages across several classes of free operations. In particular, we prove that when the free operations are local unitaries or permutation matrices, flexible catalysis enables state extractions that are unattainable with standard catalysis alone.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2510.06909v2
- Title: Optimizing LOCC Protocols on Product Stiefel Manifold
- Authors: Ze-Tong Li, Cheng-Kai Zhu, Xin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.06909v2  pdf=https://arxiv.org/pdf/2510.06909v2.pdf

Abstract:
Characterizing the operational limits of Local Operations and Classical Communication (LOCC) is a central problem in distributed quantum information, yet remains computationally intractable due to the non-convex geometry of the LOCC set. We introduce a geometric framework that embeds the physical constraints of fixed-round LOCC protocols onto the product Stiefel manifold, converting a constrained protocol-design problem into unconstrained Riemannian optimization. We demonstrate this framework through entanglement distillation: by directly optimizing finite-copy LOCC protocols, we discover achievable protocols whose fidelities match positive partial transpose (PPT) upper bounds to within numerical precision, and we provide numerical evidence for both the operational advantage of adaptive communication rounds and the super-additivity of coherent information under two-way processing. These results establish Riemannian manifold optimization as a practical tool for probing the physical limits of future quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2511.08488v2
- Title: A Quantum Non-Gaussianity Criterion Based on Photon Correlations $g^{(2)}$ and $g^{(3)}$
- Authors: Christoph Hotter, Clara Henke, Cornelis Jacobus van Diepen, Peter Lodahl, Anders Søndberg Sørensen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.08488v2  pdf=https://arxiv.org/pdf/2511.08488v2.pdf

Abstract:
Quantum non-Gaussian states, which cannot be written as mixtures of Gaussian states, are necessary to achieve a quantum advantage in continuous variable systems. They represent an important benchmark for the realization of an advanced quantum light source, as they cannot be made by simple means such as displacement and squeezing. We introduce an attenuation-resistant sufficient criterion for quantum non-Gaussian states based on the second- and third-order correlation functions, $g^{(2)}$ and $g^{(3)}$. The general non-linear bound for classical mixtures of Gaussian states is $\sqrt{g^{(3)}} + 3 \sqrt{g^{(2)}} \geq 2$. Any mixture of Gaussian states must fulfill this inequality, thus, the violation of it represents a direct confirmation of quantum non-Gaussianity. We experimentally show the non-Gaussianity of the state produced by a quantum dot single-photon source, where we obtain $\sqrt{g^{(3)}} + 3 \sqrt{g^{(2)}} = 0.174 (13)$, which represents a statistical significance of more than $100$ standard deviations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2511.15295v4
- Title: Tensor-network approach to quantum optical state evolution beyond the Fock basis
- Authors: Nikolay Kapridov, Egor Tiunov, Dmitry Chermoshentsev
- Categories: quant-ph (primary); quant-ph; physics.comp-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2511.15295v4  pdf=https://arxiv.org/pdf/2511.15295v4.pdf

Abstract:
Understanding the quantum evolution of light in nonlinear media is central to the development of next-generation quantum technologies. Yet modeling these processes remains computationally demanding, as the required resources grow rapidly with photon number and phase-space resolution. Here we introduce a tensor-network approach that efficiently captures the dynamics of nonlinear optical systems in a continuous-variable representation. Using the matrix product state (MPS) formalism, both quantum states and operators are encoded in a highly compressed form, enabling direct numerical integration of the Schrödinger equation. We demonstrate the method by simulating degenerate spontaneous parametric down-conversion (SPDC) and show that it accurately reproduces established theoretical benchmarks - energy conservation, pump depletion, and quadrature squeezing - even in regimes where conventional Fock-basis simulations become infeasible. For high-intensity pump fields ($α= 100$), the MPS representation achieves compression ratios above $3\cdot 10^3$ while preserving physical fidelity. This framework opens a scalable route to modeling multimode quantum light and nonlinear optical phenomena beyond the reach of traditional methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2511.18621v2
- Title: Teleportation-based quantum state tomography
- Authors: Gustavo Rigolin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.18621v2  pdf=https://arxiv.org/pdf/2511.18621v2.pdf

Abstract:
We explicitly show that the quantum teleportation protocol can be employed to completely reconstruct arbitrary two- and three-qubit density matrices. We also extend the present analysis to n-qubit density matrices. The only quantum resources needed to implement the teleportation-based quantum state tomography protocol are the ability to make Bell measurements and the ability to prepare a few different single qubit states to be teleported from Alice to Bob.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2512.01229v2
- Title: Passive Polarization Stabilization for Robust Entanglement Distribution via Cross-Aligned Polarization Maintaining Fiber Pairs
- Authors: Jin-Woo Kim, Minchul Kim, Jiho Park, Junsang Oh, Kyongchun Lim, Byung-Seok Choi, Chun Ju Youn
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.01229v2  pdf=https://arxiv.org/pdf/2512.01229v2.pdf

Abstract:
Maintaining stable entanglement distribution through perturbed fiber links is essential for practical quantum-optics experiments, yet it remains challenging because of polarization fluctuations and phase or temporal-delay variations. We demonstrate stable entangled-photon transmission using a cross-aligned polarization-maintaining fiber (CAPMF) structure composed of two polarization-maintaining fiber sections with mutually orthogonal principal axes. The CAPMF configuration passively compensates polarization fluctuations without real-time active polarization control. We theoretically analyze the CAPMF structure and experimentally verify its stabilization performance under external mechanical perturbations. In the experiment, the single-mode fiber configuration yields an average visibility of $0.7655$ and a CHSH value of $S=1.7714$, whereas the CAPMF configuration maintains an average visibility of $0.9843$ and a CHSH value of $S=2.6838$. These results show that CAPMF offers a simple and robust architecture for stabilizing fiber-interface sections in practical entanglement-distribution systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2512.06602v2
- Title: High-harmonic generation driven by temporal-mode quantum states of light
- Authors: Juan M. González-Monge, Felipe Reibnitz Willemann, Johannes Feist
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2512.06602v2  pdf=https://arxiv.org/pdf/2512.06602v2.pdf

Abstract:
We develop a theoretical framework for high-harmonic generation (HHG) driven by quantum states of light based on a temporal-mode expansion of the electromagnetic field. This approach extends previous single plane-wave mode treatments to realistic pulse configurations and arbitrary multi-mode states of light, resolving conceptual inconsistencies arising from non-normalizable infinite plane waves and establishing consistency between analytical and numerical methods. We derive a correction factor that quantifies deviations from the diagonal approximation (in which the yield becomes a statistical average over classical-field simulations) both for the response of a single atom and in the many-atom regime. Our results confirms that the HHG spectrum for atoms driven by any quantum state of light in free space is accurately described by averaging semi-classical calculations over the Husimi distribution, with no observable genuine quantum effects in the spectrum. We also demonstrate that in the many-atom regime, the mean-field coherent-state approximation underlying this treatment does not preserve probabilities, although unitarity is restored by in the diagonal approximation. The absence of genuine quantum effects in the HHG yield is attributed to the large photon numbers ($\sim 10^{11}$) required to reach HHG intensities in free space, which render quantum fluctuations negligible. We discuss nanophotonic environments with ultrasmall mode volumes as potential platforms where few-photon strong-field processes could exhibit genuine quantum signatures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2512.11054v3
- Title: Crystalline Spectral Form Factors
- Authors: Dmitrii A. Trunin, David A. Huse
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cond-mat.stat-mech; nlin.CD; nlin.CG
- Links: abs=https://arxiv.org/abs/2512.11054v3  pdf=https://arxiv.org/pdf/2512.11054v3.pdf

Abstract:
We investigate crystalline-like behavior of the spectral form factor in unitary quantum systems with extremely strong eigenvalue repulsion. Using a low-temperature Coulomb gas as a model of repulsive eigenvalues, we derive the Debye-Waller factor suppressing periodic oscillations of the spectral form factor and estimate the order of its singularities at multiples of the Heisenberg time. We also reproduce this crystalline-like behavior using perturbed permutation circuits and random matrix ensembles associated with Lax matrices. Our results lay a foundation for future studies of quantum systems that exhibit intermediate level statistics between standard random matrix ensembles and permutation circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2512.19413v2
- Title: Clifford Volume and Free Fermion Volume: Complementary Scalable Benchmarks for Quantum Computers
- Authors: Attila Portik, Orsolya Kálmán, Thomas Monz, Zoltán Zimborás
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.19413v2  pdf=https://arxiv.org/pdf/2512.19413v2.pdf

Abstract:
As quantum computing advances toward the late-NISQ and early fault-tolerant eras, scalable and platform-independent benchmarks are essential for quantifying computational capacity in a classically verifiable manner. We introduce two volumetric benchmarks, Clifford Volume and Free Fermion Volume, that assess quantum hardware by testing the execution of random Clifford and free fermion operations. These two groups of unitaries possess a combination of properties that make them ideal for benchmarking: (i) each is individually efficient to simulate classically, enabling verification at scale; (ii) together they form a universal gate set; (iii) they serve as essential algorithmic primitives in practical applications (including shadow tomography and quantum chemistry); and (iv) their definitions are formulated abstractly, without explicit reference to hardware-specific features such as qubit connectivity or native gate sets. This framework thus enables scalable and fair cross-platform comparisons and tracks meaningful computational advancement. We demonstrate the practical feasibility of these benchmarks through extensive numerical simulations across realistic noise parameters and through experimental validation on Quantinuum's H2-1 trapped-ion quantum computer, which achieves a Clifford Volume of 34.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2512.23810v2
- Title: Syndrome aware mitigation of logical errors
- Authors: Dorit Aharonov, Yosi Atia, Eyal Bairey, Zvika Brakerski, Itsik Cohen, Omri Golan, Ilya Gurwich, Netanel H. Lindner, et al.
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2512.23810v2  pdf=https://arxiv.org/pdf/2512.23810v2.pdf

Abstract:
Broad applications of quantum computers will require error correction (EC). However, hardware roadmaps indicate that physical qubit numbers will remain limited in the foreseeable future, leading to residual logical errors that constrain the size and accuracy of achievable computations. Recent work suggested logical error mitigation (LEM), which applies known error mitigation (EM) methods to logical errors, eliminating their effect at the cost of a runtime overhead.   We introduce syndrome-aware logical error mitigation (SALEM), which mitigates logical errors conditioned on the error syndromes measured during error correction. The runtime overhead of SALEM is exponentially lower than that of LEM schemes which do not make use of syndrome data, enabling substantially larger circuit volumes that can be executed accurately. Compared to the routinely used combination of error correction and syndrome rejection (post-selection), SALEM increases the size of reliably executable computations by orders of magnitude. In the practical setting where space and time overheads are fixed and error reduction methods are compared by their resulting estimation errors, we observe a surprising phenomenon: SALEM, which tightly combines EC with EM, can outperform physical EM even above the standard fault-tolerance (pseudo) threshold. Thus, SALEM can make use of EC in regimes of physical error rates where EC is commonly deemed useless.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2603.27676v2
- Title: Resource theory of interactive quantum instruments
- Authors: Chung-Yun Hsieh, Armin Tavakoli, Huan-Yu Ku, Paul Skrzypczyk
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.27676v2  pdf=https://arxiv.org/pdf/2603.27676v2.pdf

Abstract:
Quantum instruments describe both the classical outcome and the updated quantum state in a measurement process. To do this in a non-trivial way, instruments must have the capability to interact coherently with the state that they measure. Here, we develop a resource theory for instruments. We consider a relevant quantifier of the separation between interactive and non-interactive instruments and show that it admits three distinct operational interpretations in terms of quantum information tasks. These concern (i) the preservation of maximally entangled states after a local measurement, (ii) the average ability to preserve random states after measurement, and (iii) the ability to recover the classical information generated from measuring half of a maximally entangled state. We also introduce a natural set of allowed operations and show that the third task fully characterises the resource content of instruments. Our general framework reproduces as special cases established resource theories for channels and measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2604.01217v2
- Title: Conditional channel entropy sets fundamental limits on thermodynamic quantum information processing
- Authors: Himanshu Badhani, Siddhartha Das
- Categories: quant-ph (primary); quant-ph; cond-mat.other; cs.IT; hep-th; math-ph
- Links: abs=https://arxiv.org/abs/2604.01217v2  pdf=https://arxiv.org/pdf/2604.01217v2.pdf

Abstract:
The thermodynamic resourcefulness of quantum channels primarily depends on their underlying causal structure and their ability to generate quantum correlations. We quantify this interplay within the resource theory of athermality for bipartite quantum channels in the presence of a side channel acting as memory, referred to as the resource theory of conditional athermality. For channels with trivial output Hamiltonians, we characterize the optimal one-shot rates for distilling the identity gate from a given channel, as well as the cost of simulating the channel using the identity gate, under conditional Gibbs-preserving superchannels. We show that these rates have a direct trade-off relation with the conditional channel entropies, attributing operational significance to signaling in quantum processes. Furthermore, we establish an asymptotic equipartition property for the conditional channel min-entropy for classes of channels that are either tele-covariant or no-signaling from the non-conditioning input to the conditioning output. As a consequence, we demonstrate asymptotic reversibility of the resource theory for these channels. The asymptotic conditional athermality capacity of a tele-covariant channel is half the superdense coding capacity of its Choi state. Our work establishes the conditional channel entropy as a primitive information-theoretic concept for quantum processes, elucidating its potential for wider applications in quantum information science.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2604.03744v2
- Title: How Events Separated by a Timelike Interval Can Help Us Understand Quantum Nonlocality
- Authors: Luiz Carlos Ryff
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.03744v2  pdf=https://arxiv.org/pdf/2604.03744v2.pdf

Abstract:
Quantum entanglement plays a fundamental role in quantum cryptography and computation. An important example of quantum entanglement can be found in the correlations of Einstein, Podolsky, and Rosen (EPR). However, despite the plethora of articles related to the topic, different interpretations of the EPR correlations coexist, and a consensus has not yet been reached. In this article, we seek to demonstrate, through the simple and direct application of quantum formalism, how events separated by timelike intervals can, strangely enough, help us better understand some aspects of the so-called "quantum nonlocality" associated with EPR correlations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2604.26927v2
- Title: The most discriminable quantum states in the multicopy regime
- Authors: Maria Kvashchuk, Polina Chernyshova, Lucas E. A. Porto, Ties-A. Ohst, Lucas B. Vieira, Marco Túlio Quintino
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.26927v2  pdf=https://arxiv.org/pdf/2604.26927v2.pdf

Abstract:
This work investigates which sets of quantum states give rise to the highest achievable success probability in minimum-error state discrimination if multiple copies of the unknown state are given. Specifically, we consider uniformly distributed ensembles of the form $\left\{\frac{1}{N},ρ_i^{\otimes k}\right\}_{i=1}^N$, where $N$ states in dimension $d$ are provided in $k$ identical copies, and derive universal limits in this scenario. For pure state ensembles, we prove that whenever $N$ is large enough to support a state $k$-design, these designs will exactly give rise to the maximally discriminable sets. We further show that when $N$ exceeds the size required for a $k$-design, mixed states can outperform all pure state ensembles. We then recognise that the problem of most discriminable classical states in the multi-copy regime is in one-to-one correspondence to the concept of the multiplicative Bayes capacity of independent uses of classical channels, a concept that emerges naturally in the context of classical information leakage. This connection allows us to completely solve the classical analogue of our problem when $N\geq \binom{d + k - 1}{k}$, and to prove that quantum systems offer a quadratic advantage (in number of copies $k$) over classical ones. Then, we prove that this classical over quantum advantage is strongly reduced when one is restricted to real quantum states, more precisely, when $N \geq k + 1$, pure real qubits only offer a constant advantage over classical bits. Finally, we introduce computational techniques to find sets of most discriminable ensembles and to obtain rigorous universal upper bounds on the maximal success probability for multi-copy state discrimination in cases that are analytically intractable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2605.05158v2
- Title: The Saturable Electronic Reluctance Switch: Switchable low-power and low-noise generation of magnetic fields using permanent magnets
- Authors: P. D. Taylor-Burdett, C. A. Burhan, S. Mason, F. R. Lebrun-Gallagher, S. Weidt, W. K. Hensinger
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.05158v2  pdf=https://arxiv.org/pdf/2605.05158v2.pdf

Abstract:
Across many areas of science, there is a need to generate magnetic fields that are both ultra-stable and switchable on and off. Current-carrying wire configurations are switchable but are susceptible to current noise. Existing current-controlled approaches to switching the field produced by a permanent magnet involve altering the magnets magnetisation, which typically requires large field pulses and produces excessive power dissipation in high frequency applications. We present a hybrid technique to switch the field of any arbitrary magnet through use of a non-linear ferromagnetic circuit, named the Saturable Electronic Reluctance Switch (SERS). The circuit achieves a linear and monotonic ramp of the magnetic field up to a current threshold, above which the field becomes constant. Crucially, the applied current has minimal influence on the magnetic field stability and demagnetisation of the magnet is avoided. The power dissipated in each switching cycle is expected to be many orders of magnitude less than for existing permanent magnet switching approaches. SERS is also robust to fabrication errors, suppressing noise in the control current by several orders of magnitude in a non-ideal device. To illustrate its application, a SERS-driven device is proposed for generating ultra-stable magnetic field gradients in a scalable trapped-ion quantum computer. We find this device offers an order of magnitude reduction in power dissipation compared to state-of-the-art current carrying wires, while reducing magnetic field noise originating from current fluctuations by up to five orders of magnitude.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2605.19248v2
- Title: Quantum Entanglement Halves the Oblivious Update Bandwidth
- Authors: Sagar Dubey
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2605.19248v2  pdf=https://arxiv.org/pdf/2605.19248v2.pdf

Abstract:
We consider $(n,k)$ MDS-coded distributed storage over $\mathbb{F}_q$ with per-node storage $α$ symbols. For the oblivious update problem, where a single message symbol changes and neither helpers nor the stale node know which, the classical lower bound is $αk \log_2 q$ bits. We prove that when the $k$ contacted helpers share prior quantum entanglement, the update bandwidth is $\lceil α/2 \rceil \cdot k \log_2 q$ bits-equivalent, a factor approaching 2 reduction. For $α= 2$, a $[[k, k-2]]_q$ CSS code achieves bandwidth $k \log_2 q$ with one qudit per helper. For general $α$, a $[[\lceil α/2 \rceil k, \lceil α/2 \rceil k - α]]_q$ CSS code achieves the bound with $\lceil α/2 \rceil$ qudits per helper. The matching converse uses the superdense coding bound: the stale node holds all transmitted qudits and hence the entangled partners, so each helper's channel supports at most $D^2$ distinguishable signals for dimension $D$. The result holds for all $(n,k)$ pairs with sufficiently large prime $q$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2605.21898v2
- Title: Concatenating Algebraic Codes over High-Rate Quantum LDPC Codes
- Authors: Adam Wills, Michael E. Beverland, Lev S. Bishop, Jay M. Gambetta, Patrick Rall, Vikesh Siddhu, Andrew W. Cross
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.21898v2  pdf=https://arxiv.org/pdf/2605.21898v2.pdf

Abstract:
Different quantum error correction schemes trade off overhead, error suppression, and hardware connectivity. Code concatenation can relax these tradeoffs by using an outer code whose non-local connectivity is supplied by logical operations of an inner code rather than directly by hardware. Prior works showed that this can reduce memory overhead for local low-rate inner codes such as the surface code. Here, we study concatenation over non-local, high-rate inner codes. Such inner codes experience correlated errors among the many logical qubits in a single codeblock. We handle this by treating each block as a single logical Galois qudit, enabling concatenation with algebraic outer codes with excellent parameters and, crucially, list decoders. In particular, we consider a memory system formed by concatenating quantum Reed-Solomon outer codes over the gross code. For fault-tolerant syndrome extraction, we develop a Galois qudit Shor scheme using "time-like" Reed-Solomon protection against measurement errors. Interestingly, a lightweight fault tolerance scheme, that would fail for qubits, works well for large-alphabet qudits, suggesting a very different theory of fault tolerance for such qudits. The whole protocol is optimised via improved bicycle instruction logical error rates, novel compilation strategies, and recent decoder post-selection rules. At uniform $10^{-3}$ physical noise, the concatenated gross code reaches the teraquop regime, which it previously could not access, with a lower space overhead than the $288$-qubit two-gross code, while offering several advantages from the engineering standpoint. Beyond our main case study, we believe the core ideas of Galois qudits, quantum Reed-Solomon outer codes, and list decoding, will prove generically powerful and highly transferable ideas across high-rate quantum architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.03181v3
- Title: Generalised simultaneous transmission of arbitrary quantum states and classical information
- Authors: Nicholas Zaunders, Timothy C. Ralph
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.03181v3  pdf=https://arxiv.org/pdf/2606.03181v3.pdf

Abstract:
We present a protocol which allows for arbitrary optical quantum states to simultaneously carry and transmit classical data, without sacrificing the integrity of either the quantum or classical information. Our scheme encodes classical information via displacements in the phase space prior to transmission and retrieves each classical symbol via a Gaussian continuous-variable teleportation. The original quantum state is then restored by guessing the the original displacement and performing the appropriate inverse operation. In the limit of sufficiently high classical signal and high squeezing, we show that our scheme is capable of perfectly reconstructing both the input classical signal and the input quantum state without loss of coherence. An example is given in terms of the transmission of a dual-rail Bell state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.14077v2
- Title: Link-Free Multi-Node Timing Synchronization for Scalable Quantum Networking
- Authors: Jacob E. Humberd, Mohmad Junaid Ul Haq, Angel Fraire Estrada, Ike Deitch, Tian Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.14077v2  pdf=https://arxiv.org/pdf/2606.14077v2.pdf

Abstract:
Precise timing synchronization is essential for distributed quantum networking, enabling entanglement distribution, quantum teleportation, and entanglement swapping across remote nodes. Existing synchronization architectures rely on dedicated timing-distribution infrastructure, most notably White Rabbit networks, which constrain topology, scalability, and deployment in free-space and satellite environments. Here we demonstrate link-free synchronization of quantum network nodes using independently operating miniature rubidium atomic clocks and computational post-processing. We validate the approach on a deployed metropolitan-scale telecom fiber network spanning three geographically separated nodes. Following drift correction, atomic-clock-based synchronization achieves timing performance approaching that of a White Rabbit benchmark and remains stable over continuous 8-hour operation. As a stringent test of quantum-network functionality, we observe Hong-Ou-Mandel interference across spatially separated nodes with visibility exceeding 70%, statistically equivalent to that obtained using dedicated White Rabbit timing links. To the best of our knowledge, this represents the first observation of quantum interference across a deployed metropolitan-scale telecom fiber network synchronized entirely without dedicated timing-transfer infrastructure. These results establish atomic-clock-based synchronization as a scalable, topology-independent alternative to conventional timing-distribution architectures and a practical pathway toward terrestrial, airborne, and space-based quantum networks where dedicated timing links are unavailable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.18428v2
- Title: Quantum algorithm for Valiant-Vazirani reduction
- Authors: Patrick Kelly, Victoria S. Ordonez, Michael R. Geller, Yohannes Abate
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.18428v2  pdf=https://arxiv.org/pdf/2606.18428v2.pdf

Abstract:
There is growing interest in extensions of the standard model of gate-based quantum computation to include auxiliary degrees of freedom evolving according to a nonlinear Schrödinger equation. By reducing the   Boolean satisfiability problem SAT to quantum state discrimination, Abrams and Lloyd argued that the right type of nonlinearity can be used to solve NP and #P problems in polynomial time, at least in an   idealized noise-free limit. For practical implementation, however, we are restricted to simulated and emergent nonlinearities, such as that appearing in mean field models for ultracold atoms and similar   ensembles. A prominent example is the torsion model, which arises in two-component Bose-Einstein condensates and spin models with all-to-all Ising interaction. But torsion-based state discrimination appears to   fall short of solving SAT. Here we close this gap by constructing the filtered oracle of the Valiant-Vazirani theorem, providing a randomized polynomial-time reduction from SAT to UNIQUE SAT, a promise problem   where there is at most 1 satisfying assignment. In the noise-free limit, the UNIQUE SAT problem can be solved in polynomial time using torsion nonlinearity. Quantum Valiant-Vazirani reduction is no faster than   the efficient classical version, but a fault-tolerant implementation coupled to a nonlinear quantum coprocessor simulating torsion would enable polynomial time solution to NP (but not #P) problems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.22832v2
- Title: Linear optical Bell state measurement for rotation-symmetric cat codes
- Authors: Issa Oe, Suguru Endo, Rui Asaoka
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.22832v2  pdf=https://arxiv.org/pdf/2606.22832v2.pdf

Abstract:
Rotation-symmetric cat (RS-cat) codes are a bosonic-code platform for quantum information processing, combining finite-energy realizability with robustness against photon loss through their discrete rotational symmetry. For applications in long-distance quantum communication and fusion-based quantum computation (FBQC), efficient Bell state measurement (BSM) is a key primitive. In this work, we consider a BSM protocol for RS-cat codes using only a half beam splitter (HBS) and photon-number-resolving detectors (PNRDs). By exploiting the characteristic photon-number structure induced by the discrete rotational symmetry of RS-cat codes, our protocol extracts both photon-number modulo and phase information for Bell-state discrimination. We show that, under ideal loss-free conditions, the proposed BSM protocol becomes deterministic for arbitrary symmetry order $N$ for sufficiently large amplitudes $α$. We further numerically evaluate the success probability under photon loss and identify the loss regime in which higher-order RS-cat codes provide an advantage. Finally, we show that post-selection can enhance the success probability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.23454v2
- Title: Improved State Readout in NV Centers using Regression Models and Rabi Driving
- Authors: Fritz Haltenberger, Manpreet Singh Jattana
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23454v2  pdf=https://arxiv.org/pdf/2606.23454v2.pdf

Abstract:
Readout of state populations in nitrogen-vacancy centers from fluorescence measurements at room-temperature is routinely achieved via contrast-based calibration. The fidelities achieved by this conventional approach are limited by reducing the dynamical fluorescence behaviour of the NV center to a scalar value, and calculating the population of each possible state independently. To address these limitations, we use regression models trained on experimental data to map the fluorescence signals onto ideal simulated populations. Additionally, we enhance the informational content of the fluorescence signals by performing measurements during induced Rabi oscillations. Our results demonstrate that including these dynamical signals significantly reduces state readout errors across multiple tested models. Notably, linear ridge regression performs nearly on par with a non-linear kernel-based model, showing that simple models already capture the relevant mapping between the enhanced fluorescence signals and the underlying state populations. This data-driven approach provides a robust alternative that achieves higher fidelities than conventional calibration in our setting, paving the way for high-fidelity state readout in solid-state quantum registers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2506.08095v2
- Title: Altermagnet-Superconductor Heterostructure: a Scalable Platform for Braiding of Majorana Modes
- Authors: Themba Hodge, Eric Mascot, Stephan Rachel
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2506.08095v2  pdf=https://arxiv.org/pdf/2506.08095v2.pdf

Abstract:
Topological quantum computation, featuring qubits built out of anyonic excitations known as Majorana zero modes (MZMs), have long presented an exciting pathway towards scalable quantum computation. Recently, the advent of altermagnetic materials has presented a new pathway towards localized MZMs on the boundary of two-dimensional materials, consisting of an altermagnetic film, subject to a superconducting proximity effect from a superconducting substrate. In this work, we demonstrate the possibility for an altermagnet-superconductor heterostructure, to not only harbor MZMs, but also freely manipulate their position along the topological boundary of the material, via rotation of the Néel vector. Using this mechanism, on a square platform, we utilize a time-dependent method to simulate the Z-gate via braiding, and then extend this to a larger H-junction, where we implement the $\sqrt{\rm X}$ and $\sqrt{\rm Z}$ gate on a single-qubit system. Further, this structure is eminently scalable to many-qubit systems, thus providing the essential ingredients towards universal quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2511.22669v2
- Title: Accurate computation of the energy variance and $\langle\langle \mathcal{L}^\dagger \mathcal{L} \rangle\rangle$ using iPEPS
- Authors: Emilio Cortés Estay, Naushad A. Kamar, Philippe Corboz
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2511.22669v2  pdf=https://arxiv.org/pdf/2511.22669v2.pdf

Abstract:
Infinite projected entangled-pair states (iPEPS) provide a powerful tensor network ansatz for two-dimensional quantum many-body systems in the thermodynamic limit. In this paper we introduce an approach to accurately compute the energy variance of an iPEPS, enabling systematic extrapolations of the ground-state energy to the exact zero-variance limit. It is based on the contraction of a large cell of tensors using the corner transfer matrix renormalization group (CTRMG) method, to evaluate the correlator between pairs of local Hamiltonian terms. We show that the accuracy of this approach is substantially higher than that of previous methods, and we demonstrate the usefulness of variance extrapolation for the Heisenberg model, for a free fermionic model, and for the Shastry-Sutherland model. Finally, we apply the approach to compute $\langle \langle \mathcal{L}^\dagger \mathcal{L} \rangle \rangle$ for an open quantum system described by the Liouvillian $\mathcal{L}$, in order to assess the quality of the steady-state solution and to locate first-order phase transitions, using the dissipative quantum Ising model as an example.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2604.22112v2
- Title: Enhanced Tantalum Superconducting Resonator Performance via All-Surface Organic Monolayer Passivation
- Authors: Harsh Gupta, Moritz Singer, Benedikt Schoof, Anna Cattani-Scholz, Shreya Sharma, Luca Rommeis, Marc Tornow
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2604.22112v2  pdf=https://arxiv.org/pdf/2604.22112v2.pdf

Abstract:
Tantalum is a promising platform for superconducting quantum circuits, yet coherence times remain limited by dielectric losses from interfacial two-level systems (TLS), exacerbated by native oxide regrowth. Here, we implement molecular surface passivation using self-assembled organic monolayers on freshly etched tantalum and silicon in coplanar waveguide resonators. Surface characterization by contact angle, XPS, FTIR and TEM confirm the formation of ordered, nanometer-thick films that suppress oxide formation. Microwave measurements in the ~5-9 GHz range reveal internal quality factors up to 1.8x10^6 in the single-photon regime at 100 mK, representing a ~140% improvement over untreated devices with native oxide. Power and temperature dependent measurements attribute this enhancement to reduced TLS-induced losses. These results demonstrate that molecular passivation effectively engineers low-loss interfaces and provides a scalable route toward high-coherence superconducting quantum devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2605.10424v2
- Title: Quantum Correlations of Neutrinos in the Kerr-Newman Space-time
- Authors: Ze-Wen Li, Shu-Jun Rong
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2605.10424v2  pdf=https://arxiv.org/pdf/2605.10424v2.pdf

Abstract:
Quantum phases provide a connection between gravitation and quantum information, which proposes a novel avenue to explore the properties of space-time. In this paper, we investigate the quantum correlations (QCs) of neutrinos in the Kerr--Newman space-time. Both radial and non-radial propagations are considered under the weak-field approximation. The results show that, for inward propagations, the oscillation probabilities and QCs differ significantly from those obtained in the Schwarzschild metric. In the case of radial outward propagation, the larger angular momentum $a$ increases the oscillation period of the survival probability $P_{ee}$, entanglement, and monogamy of nonlocality, whereas the larger charge $Q$ decreases the corresponding periods. For non-radial propagations, $M$ and $a$ can noticeably modulate the amplitudes of the considered QCs, which is not observed in the case of radial propagations. Furthermore, we find that, despite differences in their variation ranges, entanglement and coherence exhibit highly consistent oscillation behaviors in both radial and non-radial propagation cases. These findings provide a comprehensive understanding for the neutrinos-based relativistic quantum information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2605.13956v2
- Title: q-Askey Deformations of Double-Scaled SYK
- Authors: Sergio E. Aguilar-Gutierrez, Trivko Kukolj, Josef Seitz
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2605.13956v2  pdf=https://arxiv.org/pdf/2605.13956v2.pdf

Abstract:
We construct families of deformations of the double-scaled SYK (DSSYK) model and investigate their bulk interpretation. We introduce microscopic deformations of the SYK model which, after ensemble averaging and in the double-scaling limit, are described by a transfer matrix encoding the recurrence relations of basic orthogonal polynomials in the q-Askey scheme. For certain families of deformations in the semiclassical limit at finite temperature, the chord number (encoding Krylov complexity) corresponds to the length of an Einstein-Rosen bridge connecting an End-Of-The-World brane to an anti-de Sitter asymptotic boundary. By increasing one of the deformation parameters, the models eventually exhibit discrete energy levels, signaling a new geometric transition in sine dilaton gravity. Via the SYK-Schur duality, Krylov complexity also admits a representation-theoretic interpretation as the spread of the SU(2) spin in the index of an $\mathcal{N}=2$ SU(2) gauge theory. We study the operator algebras of the deformed theories. The algebras can be type II$_1$ or type I$_\infty$ factors, depending on the operators that are included. The entanglement entropy between the type II$_1$ algebras for a pure state manifests as an extremal surface through the Ryu-Takayanagi formula. We discuss connections between our results and the emergence of baby universes in the bulk.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2605.27729v3
- Title: QSignAI: Quantum-Randomness-Seeded Identity Signatures at the Intersection of AI for Science and Science for AI
- Authors: Dongping Liu, Aoyu Zhang, Luyao Zhang
- Categories: cs.CR (primary); cs.CR; cs.AI; cs.ET; quant-ph
- Links: abs=https://arxiv.org/abs/2605.27729v3  pdf=https://arxiv.org/pdf/2605.27729v3.pdf

Abstract:
The 2024-2025 Nobel and Turing awards recognised AI and quantum science simultaneously. Yet no deployed system has brought these streams together for the public. This paper presents QSignAI, a production-deployed platform demonstrating a bidirectional AI-quantum relationship in a real-time event participation system. We address three questions: can quantum-randomness generation via a two-source extractor be embedded in an AI-driven social platform with acceptable latency; can an AI bot make quantum phenomena perceptually legible to general audiences; and does the combined system work in practice? A conversational bot routes each participant's first message through a quantum pipeline comprising a Toeplitz two-source extractor over independent single-qubit Hadamard measurements on SV1 and DM1 simulators, plus a 2-qubit Bell state, producing a unique quantum-randomness-seeded identity signature per participant. The first two questions are answered through system architecture and qualitative deployment evidence from live events; the third through successful production deployment. The current deployment uses cloud quantum simulators; physical QPU randomness is the near-term extension. Measurable benchmarks are identified as priority future work.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-25 10:25
- arXiv: 2606.22479v2
- Title: Quantum Metric Bound State of Light
- Authors: Jinchao Zhao, Rongning Liu, Xue-Yang Song, K. T. Law
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.dis-nn; quant-ph
- Links: abs=https://arxiv.org/abs/2606.22479v2  pdf=https://arxiv.org/pdf/2606.22479v2.pdf

Abstract:
The spatial confinement of defect-induced bound states is conventionally governed by the effective mass in dispersive bands. More recently, Compact Localized States (CLSs) arising from exact destructive interference have been utilized to achieve confinement in flat bands. However, CLSs rely on pristine lattice symmetries and fine-tuned defect profiles. The introduction of a generic local impurity inevitably breaks these strict phase-matching conditions, resulting in extensive bound states whose fundamental length scale has remained an open question. Here, we establish a third regime of confinement: the quantum metric bound state. We provide a rigorous mathematical proof demonstrating that in the absence of kinetic energy and CLS protection, the exponential decay length of these states is lower-bounded by the quantum metric of the unperturbed flat band. We demonstrate the tightness of this geometric limit by constructing a family of highly tunable flat-band generators, and we verify its universality across diverse realistic architectures. Ultimately, this classification establishes the independently measurable quantum metric as a predictive design principle for engineering confined modes in synthetic wave platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24913v1
- Title: Variants of the Quantum Phase Operator for the Harmonic Oscillator
- Authors: Bogdan D. Djordjevic, Nikolay A. Ivanov
- Categories: quant-ph (primary); quant-ph; math.OA
- Links: abs=https://arxiv.org/abs/2606.24913v1  pdf=https://arxiv.org/pdf/2606.24913v1.pdf

Abstract:
We introduce and study quantum phase operators associated with the Quantum Harmonic Oscillator (QHO). We show that these operators are trace-class perturbations of the Susskind-Glogower operators and examine their mathematical and physical properties. The construction is motivated by the physically relevant two-phase case.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24922v1
- Title: Constraint-Aware Quantum Optimization of Defect Configurations in Doped ZrO2: XY-Mixer QAOA and Grover Adaptive Search
- Authors: Huajing Song
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2606.24922v1  pdf=https://arxiv.org/pdf/2606.24922v1.pdf

Abstract:
Quantum optimization offers a route to searching the large defect-configuration spaces that arise in materials design. We develop an end-to-end, constraint-aware quantum optimization workflow for composition-defect search in a doped ZrO2 thermal-barrier-coating (TBC) material system, using a MACE-MPA-0 energy dataset to fit a 24-variable QUBO over 8 cation-occupation and 16 oxygen-vacancy variables with exactly two rare-earth substitutions and one oxygen vacancy, yielding 448 feasible configurations. The QUBO surrogate reproduces the MACE energies with held-out R2 = 0.997 (full-data R2 = 0.999, RMSE = 17 meV). We validate two complementary quantum pathways against exact enumeration: a constraint-preserving XY-mixer QAOA that confines sampling to the feasible subspace and places 86% of probability mass within 1 meV of the MACE optimum at depth p = 3, and a fault-tolerant constrained Grover Adaptive Search oracle with explicit fixed-point arithmetic, branch-safe comparison, feasibility checking, and phase kickback. Across threshold cases, the validated oracle uses 324 high-level logical qubits, or 352 to 358 with conservative clean-ancilla v-chain accounting, and requires 3.6 to 4.3 x 104 Toffoli gates per Grover (GAS) iteration. An idealized feasible-space amplification estimate suggests up to a 240x reduction in total Toffoli cost relative to the full 224 occupation space, providing a resource-estimation bridge between materials-informed QUBO modeling, constraint-aware QAOA, and fault-tolerant threshold search.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24928v1
- Title: Reading Weakly, Acting Strongly: A Static Parity Horizon and its Dynamical Bypass in the Monitored Lipkin-Meshkov-Glick Model
- Authors: Stavros Mouslopoulos
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2606.24928v1  pdf=https://arxiv.org/pdf/2606.24928v1.pdf

Abstract:
We study the broken-symmetry phase of the Lipkin-Meshkov-Glick (LMG) model, whose two lowest states form a near-degenerate parity doublet split by tunnelling. We show that the same instanton action S_inst that sets the doublet splitting also controls how much parity information a static J_z magnetisation readout can extract. Although J_z measures magnetisation rather than parity - and so distinguishes the two wells easily while remaining almost blind to their relative sign - WKB barrier arguments together with exact diagonalisation show that the spectral gap, the total-variation distance, and the nonlinear distinguishability measures (Jensen-Shannon divergence and Chernoff information) share a single instanton exponent, rather than the doubled exponent a naive small-deviation expansion in the lobes would suggest. Exact diagonalisation up to N = 4500 supports a common leading exponent for all four quantities, with fitted values within a few percent of the WKB instanton value in the largest reliable windows. The same coupling acts strongly inside the doublet: its off-diagonal element grows as |J_01| -> N m_*/2, so the bath can disturb the parity label far more strongly than it can read it from a frozen histogram. We call this separation the static parity horizon - a benchmark for the idealised static J_z channel, not a universal bound on time-resolved monitoring. Restoring the full monitored dynamics, continuous-monitoring simulations (1.48 million full-LMG trajectories with matched QND controls across 77 independent settings) show that a time-resolved homodyne record extracts parity information hidden from the single-shot histogram, over a finite window of system sizes organised by the ratio xi = omega_01/Gamma_01 of coherent doublet rotation to measurement-induced dephasing, and closing again under strong measurement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24932v1
- Title: Recursive QLSTM with Dynamic Variational Quantum Circuit Adaptation
- Authors: Samuel Yen-Chi Chen, Yifeng Peng, Jiun-Cheng Jiang, Chun-Hua Lin, Kuo-Chung Peng, Junghoon Justin Park, Huan-Hsin Tseng, Hsin-Yi Lin, et al.
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.ET; cs.LG; cs.NE
- Links: abs=https://arxiv.org/abs/2606.24932v1  pdf=https://arxiv.org/pdf/2606.24932v1.pdf

Abstract:
Recent advances in quantum computing and machine learning have motivated the development of quantum models for sequential data processing. In this paper, we propose a Recursive Quantum Long Short-Term Memory model, or Recursive QLSTM, which extends QLSTM through metacore-based recursive constructions. We numerically test the model under different input sequence lengths, metacore designs, and recursive rules, and identify the best-performing architecture among these variants. For this selected model, we further provide theoretical arguments explaining why its recursive structure improves temporal information propagation and enhances learning performance. Our results suggest that Recursive QLSTM offers a flexible and effective framework for quantum recurrent learning over input time series of various lengths.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24933v1
- Title: Self-Modulating Quantum Fast-Weight Programmers for Efficient Adaptive Sequential Learning
- Authors: Samuel Yen-Chi Chen, Yifeng Peng, Kuo-Chung Peng, Jiun-Cheng Jiang, Chun-Hua Lin, Junghoon Justin Park, Huan-Hsin Tseng, Hsin-Yi Lin, et al.
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.ET; cs.LG; cs.NE
- Links: abs=https://arxiv.org/abs/2606.24933v1  pdf=https://arxiv.org/pdf/2606.24933v1.pdf

Abstract:
Recent advances in quantum machine learning have motivated efficient models for sequential data processing. In this paper, we propose Self-Modulating Quantum Fast Weight Programmers, or Self-Modulating QFWP, which extends Quantum Fast Weight Programmers by introducing adaptive modulation over both newly generated fast-weight updates and historical fast-weight memory. Numerical results show that the proposed mechanism improves convergence stability and prediction performance across varying model settings, including different numbers of qubits and input sequence lengths. We further provide theoretical arguments explaining how self-modulation balances new information injection with memory retention, thereby enhancing temporal information propagation. These results suggest that Self-Modulating QFWP is a compact and effective framework for quantum machine learning on time-series data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24939v1
- Title: Bright-state source cancellation in dissipative shortcut Raman atom optics
- Authors: Asad Ali, Saif Al-Kuwari, M. I. Hussain, H. Kuniyil, M. T. Rahim, Saeed Haddadi
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.24939v1  pdf=https://arxiv.org/pdf/2606.24939v1.pdf

Abstract:
Spontaneous Raman scattering limits shortcut-assisted atom optics, but its microscopic origin is obscured once the lossy excited state is adiabatically eliminated. We organize the problem around a single quantity: in the instantaneous dark-bright basis the lower-manifold optical source is carried entirely by the bright-state amplitude, $S=Ωb$, so that primary spontaneous scattering reduces to the compact functional. This recovers the known dissipative-STIRAP loss in transparent form and makes the action of a shortcut explicit: ideal counterdiabatic STIRSAP cancels the bright-state \emph{source}, not the optical decay coefficient. We show this cancellation is exact in the full three-level model at the counterdiabatic point, for arbitrary one-photon detuning, Rabi frequency, and pulse duration. The residual source splits into orthogonal quadratures -- shortcut mismatch (real) and two-photon Doppler detuning (imaginary) -- which invites a velocity-selective protocol that nulls the Doppler quadrature for a chosen momentum class with a second, phase-shifted lower-state field. Our central result is that this source nulling is never superior to simply chirping the two-photon detuning: the two coincide only when the selected class $δ_c$ is small compared with the bright-state gap, and the nulling degrades and then fails as $δ_c\to|μ|$  -- precisely the regime of launched or warm clouds and high-order large-momentum-transfer (LMT) optics that motivates velocity selection. The controlling quantity is the magnitude of the residual Hamiltonian perturbation a scheme leaves behind, not the residual source it cancels. As a complement to existing multi-pulse decay budgets, we cast a single-pulse mode-error budget for LMT interferometry entirely in terms of the bright-state source, and delineate when shortcut-assisted Raman control reduces the total scattering cost.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25011v1
- Title: Fast and Parallel High-Rate STAR Architecture for Megaquop Quantum Simulation
- Authors: Refaat Ismail, Milan Kornjača, Hong-Ye Hu, Nishad Maskara, Sheng-Tao Wang, Hengyun Zhou, Chen Zhao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25011v1  pdf=https://arxiv.org/pdf/2606.25011v1.pdf

Abstract:
Fault-tolerant quantum simulation is approaching a phase where encoding overhead, logical Clifford operations, magic-state preparation, and rotation synthesis must be optimized together for efficient implementation. Space-Time efficient Analog Rotation (STAR) architectures reduce two of these costs by preparing small-angle rotation magic states directly, and the transversal STAR variant further lowers the Clifford overhead. Existing concrete implementations, however, largely inherit the low $O(1/d^2)$ encoding rate of the surface code, while high-rate codes have not yet been integrated into comparably explicit architectures. Here, we introduce a high-rate STAR architecture for local lattice Hamiltonian simulation based on a symmetry-driven co-design of the algorithm, QEC code, and neutral-atom hardware. Translation symmetries of the target lattice determine the choice of bicycle chain codes, a tunable family of self-dual bivariate bicycle codes that natively implement Clifford gates required for lattice simulation. Disjoint logical representatives allow STAR injections to be performed in parallel on all $k$ logical qubits in a code block, amortizing resource state preparation and enabling practical post-selection rates. On neutral-atom platform, the same translation symmetry compiles the key logical operations into low-depth, hardware-native acousto-optic-deflector shifts. End-to-end estimates show that an $8 \times 8$ transverse-field Ising simulation to $T^* \approx 8 (zJ)^{-1}$ requires $2240$ physical qubits and $\sim 200$ s per shot, a $\sim 5.5\times$ space reduction relative to a surface code STAR baseline at comparable speed; for Fermi-Hubbard dynamics to $T^* \approx 4 (zt)^{-1}$, the corresponding estimates are $\sim 6300$ physical qubits and $\sim 200$ s per shot. These results provide a concrete route toward early fault-tolerant quantum simulation with high-rate codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25029v1
- Title: Efficient Quantum Circuits for Coherent Conversion Between General First- and Second-Quantized Many-Body Representations
- Authors: Jack S. Baker, Gaurav Saxena, Thi Ha Kyaw
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25029v1  pdf=https://arxiv.org/pdf/2606.25029v1.pdf

Abstract:
Quantum simulation at fixed particle number admits two equivalent descriptions, a first-quantized (particle) representation and a second-quantized (occupation-number) representation. Their quantum resource costs differ sharply across computational tasks, so the ability to convert coherently between them is valuable. We construct an explicit unitary $Q$, with inverse $Q^\dagger$, that maps a first-quantized state to its fixed-$N$ occupation-number form while diagnosing the input's particle-exchange symmetry. The conversion is therefore symmetry-agnostic at the input yet fully resolved at the output, and it applies uniformly to bosonic, fermionic, and parastatistical sectors. At its foundation lies a structural identification that we place at the center of this work: the quantum Schur transform supplied by Schur-Weyl duality is the non-abelian Fourier transform of the commuting pair $(S_N,U(d))$, and the occupation-number representation is its weight basis, retaining only the labels shared by both factors, the irrep $λ$ and the $\mathfrak{u}(d)$ weight. This reduction is lossless for bosons and fermions, while a canonical Gelfand-Tsetlin promise renders it one-to-one for the remaining sectors. Algorithmically, $Q$ composes the strong Schur transform with reversible arithmetic that computes occupations as successive row-sum differences of the Gelfand-Tsetlin pattern, yielding gate complexity $\mathrm{poly}(N,d,\log(1/ε))$. The converted state is prepared efficiently in quantum memory. Any classical algorithm that outputs it explicitly, however, pays a cost set by the sector dimension, which is polynomial of degree $N$ in $d$ at fixed $N$ and exponential in $N$ when $d=Θ(N)$. Finally, an efficient classical sampler for the induced occupation-number distribution would yield one for arbitrary quantum circuits, contrary to standard complexity assumptions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25037v1
- Title: Arbitrarily Loss-Tolerant Quantum Position Verification in a Single Execution
- Authors: Llorenç Escolà-Farràs, Boris Škorić, Florian Speelman
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25037v1  pdf=https://arxiv.org/pdf/2606.25037v1.pdf

Abstract:
Quantum position verification (QPV) seeks to certify the spatial location of an untrusted prover, but is challenged fundamentally by entanglement-based attacks and experimentally by photon loss. Both issues were addressed separately in different works and were simultaneously resolved for sequentially repeated protocols in \textit{Phys.\ Rev.\ Lett.}\ \textbf{135},~260801 via a commitment-based modification that renders security independent of transmission losses. However, single-execution protocols are preferable in practice, and the original techniques do not extend to the parallel setting due to their reliance on sequential structure. We overcome this by utilizing different techniques based on no-signalling correlations, lifting the commitment modification to the parallel regime while preserving the security guarantees of the underlying QPV protocol. Applying this to a BB84-based QPV protocol suitable for near-term implementation and secure against bounded-entanglement adversaries, we prove that fixing a threshold~$k$ on the number of successfully committed qubits yields an adversarial acceptance probability that decays exponentially in~$k$. The resulting protocol maintains robustness to noise levels of up to~$3.7\%$ and remains secure under arbitrarily slow quantum communication, as does the original protocol. This yields the first fully loss-tolerant single-shot QPV protocol secure against entangled attackers, making QPV feasible over arbitrary distances. Finally, we refine the sequential analysis and obtain improved quantitative parameters for experimental implementations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25048v1
- Title: Majorana-Pauli stabilizer codes and duality webs of fermionic topological phases
- Authors: Meng Sun, Zongyuan Wang, Nathanan Tantivasadakarn, Yu-An Chen
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; math-ph
- Links: abs=https://arxiv.org/abs/2606.25048v1  pdf=https://arxiv.org/pdf/2606.25048v1.pdf

Abstract:
Stabilizer codes provide exact lattice realizations of bosonic topological orders. In contrast, systematic stabilizer descriptions of intrinsically fermionic topological phases remain much less developed. In this work, we introduce Majorana-Pauli stabilizer codes, a class of exactly solvable fermionic lattice models whose stabilizers are built from both generalized Pauli operators and Majorana operators. As a main example, we construct an exactly solvable stabilizer realization of the fermionic toric code: an intrinsically fermionic $\mathbb Z_2$ topological order in $(2{+}1)$ dimensions, using $\mathbb Z_8$ Pauli operators coupled to Majorana modes. Within this stabilizer framework, the anyons, string operators, fusion rules, and braiding statistics all follow naturally from the stabilizer algebra. More broadly, we show that the fermionic toric code belongs to a duality web generated by anyon condensation and by gauging bosonic or fermion-parity symmetries. This web connects bosonic topological orders, symmetry-enriched topological phases, and both bosonic and fermionic symmetry-protected topological phases, all within a common stabilizer description. We further show that the construction extends to all Abelian fermionic topological orders with gapped boundaries and to all supercohomology fermionic SPT phases in $(2{+}1)$ dimensions. Going beyond Majorana operators, we introduce fermionic versions of the clock and shift operators and use them to construct an exact bosonization map for $\mathbb Z_D^F$ symmetries for $D$ even. Using this, we realize a stabilizer model for a nontrivial $\mathbb Z_8^F$ fermionic SPT phase with no free-fermion analog. Altogether, these results extend the stabilizer-code paradigm to a broad class of intrinsically fermionic phases bridging fermionic quantum many-body physics to quantum error correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25053v1
- Title: A Contactless Heat Engine Driven by Nonreciprocal Fluctuation-Induced Torques
- Authors: Dhruv Shah, Kiryl Asheichyk, David Gelbwaser-Klimovsky, Noah Graham, Mehran Kardar, Matthias Krüger
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2606.25053v1  pdf=https://arxiv.org/pdf/2606.25053v1.pdf

Abstract:
We describe a contactless heat engine in which quantum and thermal electromagnetic fluctuations act as the working medium. The setup consists of two concentric cylinders held at different temperatures. The inner cylinder stably levitates within the outer one due to repulsive nonequilibrium Casimir forces. The chirality of the setup is broken by using nonreciprocal dielectric materials, akin to application of a magnetic field along the common cylinder axis. Using Rytov fluctuational electrodynamics, we show that heat transfer and torque can be expressed in terms of an angular-momentum-resolved heat flux density, $Φ_n(ω)$: each exchanged photon carries energy $\hbar ω$ and angular momentum $\hbar n$. In reciprocal media contributions from modes $n$ and $-n$ cancel and there is no net torque; nonreciprocity breaks this symmetry and powers rotation of the inner cylinder. Even in the absence of contact, electromagnetic fluctuations produce a frictional torque opposing rotation that we compute. This enables computation of characteristic steady state rotations, and estimation of the engine efficiency (which remains bounded by the Carnot limit). The cylindrical setup provides a natural realization of fluctuation-induced angular-momentum transfer and a possible route toward nanoscale contactless engines.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25061v1
- Title: Nonlocal Quantum Phase Transitions
- Authors: Alessandro Coppo, Aanal Jayesh Shah, Hadiseh Alaeian, Valentina Brosco, Roberto Di Candia, Simone Felicetti
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2606.25061v1  pdf=https://arxiv.org/pdf/2606.25061v1.pdf

Abstract:
Phase transitions are paradigmatic examples of emergent phenomena, in which symmetries present at the microscopic level can be spontaneously broken in the thermodynamic limit. Two primary physical mechanisms can drive this symmetry breaking: thermal fluctuations in classical phase transitions and quantum fluctuations in quantum critical phenomena. Here, we introduce $nonlocal$ $quantum$ $fluctuations$ as a new fundamental mechanism to drive phase transitions. We show that entanglement shared between environmental modes can induce a correlated symmetry breaking in remote systems, independent of their spatial separation. Using the framework of driven-dissipative phase transitions, we theoretically investigate a system composed of two nonlinear quantum resonators placed at arbitrarily large spatial separations, each coupled to independent local Markovian baths. We consider the regime in which remote environmental modes are prepared in broadband entangled states. We show that near the critical point, where the susceptibility to weak perturbations diverges, quantum correlations in the environments govern the system critical behavior. While these correlations manifest locally only as effective thermal fluctuations, at the global level they give rise to an emergent nonlocal phase transition, marked by the spontaneous symmetry breaking of a collective mode shared by the two remote systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25080v1
- Title: Quantum Primitive for Output-Hiding Function Sharing
- Authors: Olivia R. Hartzell
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25080v1  pdf=https://arxiv.org/pdf/2606.25080v1.pdf

Abstract:
A quantum information-theoretic primitive is introduced for determining a discrete-valued function that depends on multiple parties' local private inputs. The primitive permits the parties to mutually learn each others' local inputs, and thereby determine function values, while their individual systems remain independent of these inputs. The resulting function values are shared among the parties, but may remain information-theoretically hidden from any external observer, as well as from adversarial state-preparation or measurement processes within the quantum system, in every iteration. In particular, while classically producing a shared function with these information-theoretic properties requires the use of private keys or hidden randomness, in the proposed setting it is achieved using quantum resources alone. I outline the primitive's general properties while applications across a broad range of secure quantum communication and computation settings including: quantum key distribution, multi-party coordination and decision schemes, function evaluation, and in some settings, protocols for fairly generated private coins, are relegated to further publications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25085v1
- Title: Note About Koopman-von Neumann Theory and Density Matrix
- Authors: J. Kluson
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25085v1  pdf=https://arxiv.org/pdf/2606.25085v1.pdf

Abstract:
In this short note we study Koopman-von Neumann theory for N-particle system. We argue that it is natural to identify classical N-particle distribution function as diagonal form of density matrix operator in coordinate representation. We also determine generalized BBGKY hierarchy for reduced density matrix in coordinate representation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25100v1
- Title: Detection of patterns in a discrete-outcome sensor network
- Authors: Pranjal Agarwal, Nada Ali, Mark Hillery
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25100v1  pdf=https://arxiv.org/pdf/2606.25100v1.pdf

Abstract:
A discrete outcome quantum sensor network is one in which we are only interested in which detectors are activated. This can be studied in either the strong or weak interaction regime. If the detectors interact strongly with the environment, it is possible to definitely find which ones were activated. If the interaction is weaker, there is a possibility of making an error, and the object is to minimize the probability of this happening. Here we will be interested in this weaker interaction regime. We will also assume that only certain patterns of detectors will be activated, different patterns being translated versions of a fundamental one. Our object will be to find which pattern has been activated. We will look at both one and two-dimensional detector arrays and make use of techniques from minimum-error state discrimination.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25117v1
- Title: Feasibility-driven QAOA with penalty scheduling
- Authors: Francesco Ferrari, Matteo Vandelli, Daniele Dragoni
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25117v1  pdf=https://arxiv.org/pdf/2606.25117v1.pdf

Abstract:
Most available quantum algorithms address constrained optimization problems by treating constraints as soft penalty terms within a QUBO formulation. This approach requires careful adjustment of the penalty coefficients, which scales poorly with the number of constraints and lacks a proper strategy to balance feasibility and solution quality. In this work, we introduce two extensions of standard linear-ramp QAOA (lr-QAOA) tailored to problems with multiple heterogeneous constraints. We first construct $Λ$-lr-QAOA, in which each penalty term is assigned its own linear-ramp schedule, promoting penalty weights from external hyperparameters to internal variational parameters of QAOA, similarly to the objective and mixer parameters. By optimizing all schedules jointly in a single run, this approach eliminates nested penalty tuning and scales more efficiently to multiple constraints. The optimization is guided by a feasibility-driven loss function that pushes the quantum state towards high-quality feasible solutions. As a further refinement, we introduce piecewise-ramp QAOA, in which the linear ramps are replaced by two-segment piecewise schedules, enhancing the expressiveness of the Ansatz at the cost of a small parameter overhead independent of the circuit depth. We benchmark both methods on Earth-observation satellite mission planning tasks formulated as budget-constrained Maximum Weight Independent Set problems. Numerical results show that piecewise-ramp QAOA consistently outperforms lr-QAOA and $Λ$-lr-QAOA across circuit depths and system sizes. Furthermore, both $Λ$-lr-QAOA and piecewise-ramp QAOA exhibit a high feasibility rate, which is crucial in industrial applications. Our analysis highlights an intrinsic feasibility-optimality trade-off, which we address by introducing a filtered variant of the loss providing a single hyperparameter to tune this balance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25124v1
- Title: Self-testing Quantum Supermaps
- Authors: Victor Barizien, Cyril Branciard, Alastair A. Abbott, Jean-Daniel Bancal, Pavel Sekatski
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25124v1  pdf=https://arxiv.org/pdf/2606.25124v1.pdf

Abstract:
By certifying quantum operations from measurement statistics directly, without any assumption on the internal workings of the devices involved, self-testing enables a uniquely reliable identification of quantum objects. While such device-independent characterization has been shown to be possible for states, measurements and channels, it has so far not been extended to quantum supermaps -- operations that act on quantum channels themselves and can combine them in either a well-defined causal order or also, remarkably, in an indefinite causal order. Here we show that quantum supermaps can be identified device-independently. Specifically, we obtain two levels of certification, depending on the network structure of the experiment: when each slot of the supermap accepts a single uncharacterized black box, identification up to local embedding combs is obtained; when several black boxes are inserted within each slot, identification up to local extracting and injecting maps is achieved. We illustrate our approach on four examples -- the identity comb, a bit-flip error-correcting comb, the comb describing Grover's algorithm, and the quantum switch -- providing in particular the first self-test of both a quantum algorithmic comb and a causally indefinite quantum process. Notably, in the latter case, this provides a new way to certify causal indefiniteness in a device-independent manner.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25260v1
- Title: Closed Quantum Boltzmann Bridges: Coherent Revivals, Hidden Microstates, and the Emergence of Classical Two-Time Entropy Conditioning
- Authors: Sina Kazemian, Ghazal Farhani, Younes Javanmard
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25260v1  pdf=https://arxiv.org/pdf/2606.25260v1.pdf

Abstract:
The classical Boltzmann Bridge describes entropy histories conditioned on both an initial low-entropy macrostate and a later macrostate. Unlike the usual past-only formulation of the thermodynamic arrow, this two-time conditioning can produce entropy profiles that rise above the final entropy and then decrease toward the imposed endpoint. In this work, we formulate closed quantum analogues of the Boltzmann Bridge using macro-subspace projectors, unitary time evolution, and Boltzmann entropy defined by the dimension of coarse-grained macroscopic sectors. We first study a minimal coherent chamber-qubit model, in which each particle has only a two-state chamber degree of freedom. Although this model is the most direct quantization of the classical two-box system, its bridge entropy profile is dominated by coherent oscillations and revivals rather than classical relaxation. We then introduce a hidden-microstate bridge, in which each chamber sector contains unresolved internal degrees of freedom while the full dynamics remain unitary. Numerical experiments show that increasing the internal Hilbert-space dimension suppresses sample-dependent revival behavior and produces bridge entropy profiles whose sign structure and coarse-grained shape increasingly agree with the classical Boltzmann Bridge. We further use a Random Forest classifier to explore the parameter regime separating revival-dominated quantum behavior from classical-like coarse-grained bridge behavior. These results suggest that classical two-time-conditioned entropy behavior is not recovered by quantizing the chamber variable alone, but can emerge statistically from closed quantum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25261v1
- Title: A Mean-Field Lindblad Master Equation Framework for Interaction-Driven Decoherence in Solid-State Qubit Ensembles
- Authors: Dhiman Nandi, Sanghamitra Neogi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25261v1  pdf=https://arxiv.org/pdf/2606.25261v1.pdf

Abstract:
Multi-qubit systems are essential for scalable quantum technologies, but their performance is often limited by decoherence from qubit--qubit interactions and environmental noise. Although environmental decoherence in single-qubit systems and gate fidelity in multi-qubit systems have been widely studied, a predictive framework connecting qubit interactions, concentration, spatial distribution, and bath occupation to relaxation and decoherence times remains lacking. Here, we develop a multi-qubit mean-field Lindblad master equation (MQMF-LME) framework for the population and coherence dynamics of a solid-state qubit in an interacting multi-qubit environment. The framework treats one qubit as the system of interest and the surrounding qubits as an effective bath, incorporating intrinsic relaxation and bidirectional excitation transfer between the system and the bath. Analytical solutions provide closed-form expressions for density-matrix dynamics, steady-state populations, relaxation time $T_1$, and decoherence time $T_2$, while numerical simulations extend the framework to concentration-dependent dynamics, $1/f$-noise-induced dephasing, and material-specific excitation-transfer mechanisms. For a model system with Förster resonance energy transfer (FRET)-mediated excitation exchange, higher qubit concentrations reduce both $T_1$ and $T_2$, whereas $1/f$ noise reduces $T_2$ without changing $T_1$. Applied to Er$^{3+}$-doped CeO$_2$, the framework shows that long-range FRET-mediated excitation transfer reproduces the experimental decrease in relaxation time with dopant concentration, whereas short-range Dexter-type exchange does not, identifying FRET-mediated excitation transfer as the dominant mechanism. The MQMF-LME framework provides a modular route for linking microscopic interactions and environmental noise sources to measurable decoherence times in solid-state multi-qubit systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25264v1
- Title: Quantum conditional mutual information and channel capacity
- Authors: D. -S. Wang
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2606.25264v1  pdf=https://arxiv.org/pdf/2606.25264v1.pdf

Abstract:
Information measures acquire operational meaning through coding theorems. The quantum conditional mutual information (QCMI) is nonnegative due to strong subadditivity, yet a direct connection with channel coding has remained elusive. In this work, we propose a quantum communication task-conditional quantum communication-that fills this gap. We show that the optimal rate for establishing quantum correlation between two parties, assisted by a third system, is given by half the QCMI. This result naturally extends the classical key generation capacity of Csiszár and Ahlswede to the quantum domain. We place our model within the family tree of quantum protocols and compute the conditional capacity for several example channels. Our results provide new insights for code design in reliable quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25267v1
- Title: Rapid and robust laser-frequency auto-locking using Bayesian-optimization and discrete-wavelet-transformation algorithms
- Authors: Min Jiang, Xiao-Li Chen, Si-Bin Lu, Jia-Hao Fu, Zhan-Wei Yao, Shao-Kang Li, Min Ke, San-Ming Song, et al.
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2606.25267v1  pdf=https://arxiv.org/pdf/2606.25267v1.pdf

Abstract:
Rapid and robust laser-frequency auto-locking is essential for the field deployment of quantum communications, quantum computing, and precision-measurement technologies; however, achieving this remains a considerable challenge. Here, we propose and demonstrate an auto-locking scheme employing Bayesian optimization and discrete biorthogonal wavelet transformation. First, the reference is rapidly sought by making intelligent use of historical observations, eliminating the inherent blindness of the traditional parameter-scanning method. Second, the frequency reference is robustly identified by pinpointing transition signals with the discrete biorthogonal wavelet transformation and analyzing their immutable frequency differences and relative magnitudes, which are determined by the inherent atomic structure and remain resistant to environmental disturbances. This proposed approach achieves a fivefold acceleration in reference searching compared to conventional scanning methods in the case where the laser frequency drifts far away from the reference. Crucially, it achieves an identification accuracy of more than 99.5 %, even under severe 50 % laser-intensity fluctuations, $9.95^\circ$ photodiode misalignment, and $18^\circ$C Rb cell temperature elevation. Finally, locking the laser frequency to the identified reference with a lead zirconate titanate-current double-servo loop narrows the linewidth to 20 kHz. We believe that this rapid, robust, and high-performance auto-locking technique will be pivotal towards the deployment of the next generation of practical quantum technologies in demanding field environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25314v1
- Title: High-Rate and Resource-Efficient All-Photonic Quantum Repeater Architectures with 9 km Repeater Spacing
- Authors: Ryosuke Shiina, Kenneth Goodenough, Nathan Arnold, Filip Rozpędek
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25314v1  pdf=https://arxiv.org/pdf/2606.25314v1.pdf

Abstract:
Quantum communication between two distant parties will serve as a cornerstone of the future quantum internet. However, generating enough entangled Bell pairs over long distances is a critical bottleneck. Although photons are ideal carriers of quantum information, overcoming photon loss and the exponential attenuation of signals remains a major challenge. We propose an all-photonic quantum repeater architecture that enables quantum communication over 1,000 km with an equidistant repeater spacing of 9 km. This repeater spacing is enabled by elementary entangled Bell pairs protected through the concatenation of continuous-variable and discrete-variable quantum error correction codes, namely, the bosonic Gottesman-Kitaev-Preskill (GKP) code and the [[7,1,3]] Steane code, whose combination yields a synergistic improvement in robustness against photon loss. This architecture incorporates a new ranking criterion and a multi-reflection mirror-based optical cavity as a free-space photonic memory module, which we model in terms of its length and mirror-reflection efficiency. Additionally, we propose two heuristic construction methods for the elementary entangled Bell pairs. One method introduces up to two-qubit correlated errors within each logical qubit but requires a large number of GKP qubits, while the other allows up to three-qubit correlated errors within each logical qubit but requires fewer GKP qubits. To more accurately capture realistic physical conditions during photonic resource preparation, we include switching-induced imperfections in our simulations, in addition to other standard optical imperfections. In the presence of these imperfections, our realization requires only a few thousand GKP qubits per repeater station per protocol run, a resource requirement significantly smaller than the corresponding resource requirements of prior third-generation all-photonic repeater proposals.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25330v1
- Title: Routing Codes: High-Rate Quantum LDPC Codes with Short, Parallel Non-Local Connectivity
- Authors: Jiaxuan Zhang, Zhao-Yun Chen, Peng Duan, Jia-Ning Li, Tian-Hao Wei, Qing-Yang Hou, Wei-Cheng Kong, Yu-Chun Wu, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25330v1  pdf=https://arxiv.org/pdf/2606.25330v1.pdf

Abstract:
Quantum low-density parity-check (qLDPC) codes are promising candidates for realizing large-scale fault-tolerant quantum computing. Although many codes with favorable theoretical parameters have been developed, their practical adoption must take hardware implementability into account. For mainstream quantum platforms such as superconductors and neutral atoms, the connectivity, the length of non-local couplings, and the complexity of wiring or atom rearrangement are key factors that dictate the difficulty of hardware realization. Here, we propose a new family of qLDPC codes, termed routing codes. Within this family, we find explicit instances whose encoding rates are comparable to those of bivariate bicycle (BB) codes, while systematically reducing qubit connectivity, shortening the length of non-local couplings, and, crucially, making all non-local couplings mutually parallel. This parallelism fundamentally eliminates wiring crossings in superconducting multi-layer architectures and drastically simplifies the scheduling of atom movement in neutral-atom arrays. Under circuit-level simulation, the weight-7 routing codes reduce the physical qubit overhead by approximately a factor of 8, compared to surface codes achieving a same logical error rate. These results establish routing codes as a hardware-centric qLDPC family that bridges the gap between theoretical optimality and near-term physical feasibility.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25397v1
- Title: Quantum tomography of free electrons
- Authors: Y. Fang, J. Kuttruff, Z. Zhao, L. Moehrle, P. Hommelhoff, P. Baum
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.25397v1  pdf=https://arxiv.org/pdf/2606.25397v1.pdf

Abstract:
Determining the quantum state of a given quantum-mechanical system is a fundamental task in physics. Quantum-state tomography has been pivotal for establishing quantum optics [1-4] and for revealing the properties of bound charges in materials [5-7]. An emerging other object for studying and utilizing quantum effects are free electrons, elementary particles that are central to high-resolution microscopy [8,9], electron-based quantum optics [10-17], ul-trafast electron microscopy [18-24] and particle accelerators [25-27]. However, free electrons are intrinsically incoherent, and we lack a broadly applicable method to measure and control their quantum state beyond special cases with discrete energy sidebands [28,29]. Here, we report a universal approach to measure arbitrary free-electron quantum states in continuous variables. Two monochromatic but spectrally shifted laser waves produce interfering quan-tum paths that directly reveal the density matrix and thus all essential properties of the pure wavepackets, the ensemble, and their interlinks. As a first application, we show how the quantum state of a single electron is modified by many-body Coulomb interactions of a sur-rounding electron gas. The reported concepts and results provide insight into otherwise hid-den correlations in electron beams and enable the controlled optimization of exceptional quantum states for free-electron quantum optics or quantum electron microscopy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25471v1
- Title: A phase-space approach for performing continuous-variable quantum teleportation with a non-Gaussian resource
- Authors: Ankita, Arpita Chatterjee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25471v1  pdf=https://arxiv.org/pdf/2606.25471v1.pdf

Abstract:
We present a comprehensive phase-space analysis of continuous-variable quantum teleportation employing a photon-subtracted two-mode squeezed Fock state (PS-TMSFS) as an entangled resource. We investigate the usefulness of PS-TMSFS within the Braunstein-Kimble teleportation protocol. We explain the generation scheme for the resource state and derive the analytical expression for the success probability associated with the photon-subtraction process. The Wigner characteristic function of PS-TMSFS is calculated and then employed to determine the fidelity for coherent and squeezed state inputs. The dependence of the success probability and teleportation fidelity on the squeezing parameter and beam-splitter transmissivity is analyzed in detail for both symmetric and asymmetric photon-subtraction scenarios. We find that the teleportation fidelity exhibits a strong dependence on the resource parameters and is highly sensitive to variations in the subtraction process. The photon-subtraction process modifies the non-Gaussianity of the resource state, but no substantial enhancement of the teleportation fidelity is detected. Despite the non-Gaussian character of the resource state, fidelity above the classical coherent-state benchmark is observed only for the symmetric $(1,1) $ photon-subtraction configuration in the low-squeezing regime that decreases with increasing squeezing. The remaining configurations remain below the classical threshold throughout the parameter range considered. These findings indicate that the PS-TMSFS may not be a suitable resource for continuous-variable quantum teleportation and offers insight into the limitations of this class of non-Gaussian states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25510v1
- Title: Quantum metrology of electric and magnetic dipole moments: ultimate limits and optimal regimes
- Authors: Simone Cavazzoni, Paolo Bordone, Matteo G. A. Paris
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25510v1  pdf=https://arxiv.org/pdf/2606.25510v1.pdf

Abstract:
The characterization of electric and magnetic dipole moments (EDM and MDM) in quantum systems is central to fundamental physics and quantum sensing. While EDM searches provide powerful probes of CP violation within and beyond the Standard Model, precise MDM estimation is crucial for high-precision magnetometry and the development of quantum sensors. In this work, we address the ultimate precision limits for separate and simultaneous estimation of both dipole moments in a generic two-level system coupled to electromagnetic fields. We analyze three classes of quantum probes/strategies: unitary and depolarizing dynamics, and thermal equilibrium states. For each, we derive the quantum Fisher information (matrix), identify optimal probes, and determine the ideal operating conditions, such as evolution times and temperatures, that maximize estimation precision. We further assess the compatibility and sloppiness of the statistical models, showing that orthogonal dipole moments configurations enable joint estimation of EDM and MDM, whereas parallel configurations are intrinsically sloppy, permitting only the estimation of a single parameter combination. Our results provide a unified metrological framework for estimation schemes ranging from neutron EDM searches to molecular magnetometry, and highlight the distinct roles of coherence, noise, and thermalization in multiparameter quantum sensing of dipole moments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25511v1
- Title: Preparing two-mode magnonic Schrödinger cat states in a cavity-magnon-qubit system
- Authors: Gen Li, Gang Liu, Rong-Can Yang, Jie Li
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.optics
- Links: abs=https://arxiv.org/abs/2606.25511v1  pdf=https://arxiv.org/pdf/2606.25511v1.pdf

Abstract:
The cavity-magnon-qubit system has recently been demonstrated as a new platform for preparing macroscopic quantum states in magnonic systems. Here, we propose to prepare a two-mode magnonic cat state, which is also a non-Gaussian entangled state, based on this practical system involving two yttrium-iron-garnet (YIG) spheres and a superconducting qubit coupled to a common microwave cavity. By adiabatically eliminating the cavity and resonantly driving the qubit, an effective magnon-qubit conditional-displacement interaction is achieved. Further working in the magnon-magnon strong-coupling regime and considering two identical magnon frequencies and coupling strengths to the cavity, two hybridized magnon modes are formed, of which the bright mode is prepared in a cat state after a projective measurement on the qubit, while the dark mode remains in its initial vacuum state. Such a state corresponds to a two-mode cat state of two original magnon modes, which share strong non-Gaussian entanglement. We also discuss practical dissipation and dephasing effects on the cat state. The results indicate that strong nonclassicality and non-Gaussian entanglement are present in the two-mode cat state using fully feasible parameters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25587v1
- Title: Controlling radiative dynamics of a giant $Λ$-type atom via interference induced by the vacuum of a waveguide
- Authors: Ci-Ming Deng, Ge Sun, Jing Lu, Lan Zhou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25587v1  pdf=https://arxiv.org/pdf/2606.25587v1.pdf

Abstract:
We investigate the dynamics of a $Λ$-type giant atom (GA) whose both transition coupled to the guided modes of a one-dimensional (1D) waveguide at two spatially separated points with the GA initially excited and the electromagnetic (EM) modes of waveguide in vacuum. The spontaneous emission properties of this GA is investigated by solving the delay-differential equation for the amplitude of the 3GA in its excited state. Signatures of non-Markovian behavior is manifested in a population trapping in the excited state of the GA in the regime where the distance $d$ of the coupling points is smaller or comparable to the coherent length $L$ characterizing the width of the emitted wave packet. And an exact Markovian dynamics is also found when $d\geq L$ via the inference by adjusting the energy spacing and the inherent time delay besides the complex phases in the atom-light coupling, matching the behavior of a small atom coupled to a waveguide.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25598v1
- Title: The Cost of Removing Tunability in Quantum Data Re-Uploading
- Authors: Anthony Yuezhang Liu, Lirandë Pira
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25598v1  pdf=https://arxiv.org/pdf/2606.25598v1.pdf

Abstract:
Fixed encoding data re-uploading quantum circuits provide a striking example of universality emerging from a highly constrained architecture. However, universality alone is insufficient for assessing the theoretical and practical value of fixed and tunable upload circuits. The resource cost of removing tunability remains poorly understood. In this work, we establish quantitative depth-error scaling for approximating tunable upload circuits with fixed upload circuits. We show that a tunable upload circuit can be approximated by a fixed upload circuit using depth \( D = O_σ\!\left[(\log(1/\varepsilon))^σ\right] \) for every \(σ>1\), with a target dependent constant overhead, thereby improving the previously known polynomial dependence on \(1/\varepsilon\) with the same overhead. Our proof is based on an auxiliary extension approximation mechanism that combines Gevrey class construction, Jackson's theorem and generalized quantum signal processing theorem. Thus, the expressive power lost by removing tunability can be recovered using only polylogarithmic growth in circuit depth with a target dependent constant overhead. We further identify a periodic mismatch obstruction intrinsic to fixed upload approximations and use Turán-Nazarov inequalities to prove logarithmic lower bounds \( D = Ω(\log(1/\varepsilon)) \) for the approximation of mismatch class target tunable upload circuits. Conceptually, our analysis reveals two structural mechanisms underlying approximation in fixed upload architectures: auxiliary extensions and mismatch obstructions. These results provide a quantitative understanding of how expressivity is transferred from tunable frequencies into circuit depth, and suggest a broader framework for studying approximation complexity in quantum signal processing and related quantum learning models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25600v1
- Title: Two-dimensional Hyperbolic RNN Neural Quantum State
- Authors: H. L. Dao
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cs.LG; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2606.25600v1  pdf=https://arxiv.org/pdf/2606.25600v1.pdf

Abstract:
In the first part of this work, we construct the first type of two-dimensional (2D) hyperbolic neural quantum state (NQS) in the form of the Lorentz 2DRNN (Recurrent Neural Network) and benchmark its performance against the Euclidean 2DRNN in the paradigmatic $N\times N$ 2D Transverse Field Ising Model (2DTFIM) setting with different lattice sizes up to $N=12$ and at different transverse magnetic field strengths. We find that hyperbolic Lorentz 2DRNN NQS definitively outperform Euclidean 2DRNN NQS when the system is at the phase transition point when the physics can be described by a conformal field theory (CFT), which is known to be dual to an Anti-de-Sitter (AdS) space whose spatial geometry is hyperbolic. In the second part of this work, we benchmark the performances of the recently introduced one-dimensional (1D) hyperbolic NQS including Poincaré RNN/GRU and Lorentz RNN/GRU against their Euclidean NQS versions in $N\times N$ 2DTFIM, which has to be converted to a one-dimensional setting to allow for the use of 1D NQS. The findings in this case extend our previous results that 1D hyperbolic NQS definitively outperform 1D Euclidean NQS, thanks to the combined effects of the hierarchical structure comprising the first and $N^{th}$ neighbor interactions present in the 1D system arising from the 2D lattice and the CFT physics at the critical point. While more studies with larger system sizes are required, our work serves as a proof-of-concept for the utility, effectiveness as well as the superior performances of one- and two-dimensional hyperbolic NQS ansatzes compared to the existing Euclidean NQS in many-body quantum physics systems, especially when these systems exhibit structural hierarchy or when they are at criticality, or a combination of both.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25635v1
- Title: Anomalous topological superradiant phases
- Authors: You-Qi Lu, Yu-Yu Zhang, Zi-Xiang Hu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25635v1  pdf=https://arxiv.org/pdf/2606.25635v1.pdf

Abstract:
We present a novel set of light-matter topology realized by implementing a finite-component quantum Rabi array with a photonic analog of the Su-Schrieffer-Heeger (SSH) configuration. We demonstrate how complex light-matter couplings with species-dependent phases lead to the closure of superradiance-induced band gap in a manner that differs from that in the SSH model. We uncover an topological superradiant phase transition from a normal phase to a topological superradiant electromagnet phase, which is characterized both by a local order parameter and a global topological invariant. Novel superradiance-enhanced edge states emerge with significantly amplified excitations superior to those in topological normal phase. Strikingly, tuning light-atom coupling induces novel topological superradiant electric and magnetic phases, exhibiting chiral edge-mode excitation at opposite boundaries. Our proposed setup offers a tunable platform for topological quantum optics, advancing applications in topological superradiant lasers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25638v1
- Title: Towards Robust Optimal Measurements Against Noise in Quantum Metrology
- Authors: Xinglei Yu, Xinzhi Zhao, Liangsheng Li, Stanisław Kurdziałek, Chengjie Zhang, Chuan-Feng Li, Guang-Can Guo
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.25638v1  pdf=https://arxiv.org/pdf/2606.25638v1.pdf

Abstract:
Quantum parameter estimation utilizes quantum mechanical effects to attain higher measurement precision than classical schemes. In practical implementations, however, noise is inevitably present during the measurement process, causing a decrease in precision. Quantifying the impact of noise on different measurements is of considerable significance. Here, we experimentally investigate robust optimal measurements based on the theory of Fisher information measurement noise susceptibility (FI MENOS), which quantifies how susceptible a measurement is to noise. By constructing a polarizing Mach-Zehnder interferometer, we implement phase estimation under controlled noise. Our results indicate that different measurements exhibit distinct sensitivities to noise. To assess the influence of diverse noise types on precision, we further construct an experimental setup capable of introducing various forms of noise. The experimental results affirm that FI MENOS represents the worst-case scenario for estimation precision, enabling us to evaluate the noise immunity of optimal measurements. Our work provides a deeper insight into quantum metrology with noise, marking a notable advancement in quantifying the robustness of quantum estimation schemes against measurement noise effects.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25650v1
- Title: Spin-Momentum Impedance and Filtering by a Spin-Coupled Absorbing Boundary Condition
- Authors: Alireza Jozani
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25650v1  pdf=https://arxiv.org/pdf/2606.25650v1.pdf

Abstract:
Absorbing boundaries are often treated as scalar sinks. Here we show that a spin-coupled absorbing boundary for a Pauli particle acts instead as a spin--momentum impedance. Its tangential boundary symbol has two branches, $iκ\pm|\boldsymbolξ|$, coupling normal absorption to in-plane momentum. In a harmonic guide, the transverse ground state samples $|\boldsymbolξ|\sim \ell_\perp^{-1}\sim\sqrtω$; narrowing the guide therefore strengthens a local evanescent boundary response without introducing a bulk potential barrier. Solving the detector-present spinor absorbing-boundary evolution, we identify boundary-induced filtering: the prompt detector flux is suppressed, the fixed-window detected fraction is reduced, and a delayed oscillatory sector appears. Over that window the restricted mean detection time is fitted by $A+B\sqrtω$, with setup-dependent coefficients. The robust result is a spin--momentum filtering mechanism with boundary scale $|\boldsymbolξ|\sim\sqrtω$, not a universal arrival-time law.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25653v1
- Title: Long-lasting Topological Entanglement in a Monitored Rashba Nanowire
- Authors: Emanuele Guida, Giulia Salatino, Gianluca Passarelli, Angelo Russomanno, Procolo Lucignano
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2606.25653v1  pdf=https://arxiv.org/pdf/2606.25653v1.pdf

Abstract:
We study the topological properties of a monitored Rashba chain along quantum-jump trajectories, investigating the persistence of the initial topological value of the disconnected entanglement entropy (DEE). We find that the DEE persists in its topological value for a time linear in the system size, even if the dissipation acts on the boundary and affects the topological Majorana modes. The reason for this phenomenon lies in the absence of particle conservation and in the degeneracy of the topological manifold, allowing the monitoring to let the system switch between different topological states -- alternatively creating and annihilating a Majorana mode -- while producing a poisoning of finite-energy ballistically propagating quasiparticles that eventually destroy the topological entanglement structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25666v1
- Title: Quantum Detectability in Invisibility Cloaks
- Authors: Mohammad Mehdi Sadeghi
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.25666v1  pdf=https://arxiv.org/pdf/2606.25666v1.pdf

Abstract:
Classical invisibility cloaks are designed to suppress selected scattering signatures and thereby make an object appear absent to external electromagnetic probes. However, the suppression of a classical scattering observable does not, by itself, establish that all information about the concealed object has been removed from the detected quantum state of light. Here we formulate the detectability of classically cloaked objects as a quantum-state distinguishability problem. Treating a linear passive cloak as an effective Gaussian quantum channel acting on the accessible detected modes, we show that local quantum undetectability requires the detected first and second moments to be independent of the hidden-object parameter. In this framework, quantum Fisher information provides an operational criterion for whether the concealed parameter remains estimable from the detected output state. We derive displacement- and covariance-level detectability conditions and show that a nonzero parameter imprint surviving in the detected Gaussian state leads to a nonzero accessible quantum Fisher information. To connect the criterion with a physical cloaking model, we analyze a regularized cylindrical transformation-optical cloak in the Born limit and compare the scaling of the classical scattering response with the derivative-based quantum sensitivity. The analysis shows that reducing a scattering amplitude is not equivalent to eliminating local quantum-state sensitivity. Loss, environmental noise, and finite numerical aperture degrade the accessible information, but quantum undetectability is reached only when the parameter imprint is removed from the detected state or projected entirely outside the accessible subspace. These results provide a Gaussian-channel framework for assessing when classical cloaking does, and does not, imply quantum-state undetectability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25669v1
- Title: Exact Leg-Cut Influence Functional and Emergence of Gaussian Entanglement Theory in a Statistical-Dressing Ladder Model
- Authors: Babatunde Moses Ayeni
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2606.25669v1  pdf=https://arxiv.org/pdf/2606.25669v1.pdf

Abstract:
The emergence of Gaussian effective field theories in low-dimensional quantum systems is traditionally understood through top-down frameworks such as bosonization and Luttinger-liquid theory. However, these approaches typically focus on the long-wavelength degrees of freedom in ways that do not directly track how non-Gaussian lattice-scale correlations are progressively discarded under coarse-graining. In this work, we present an exact lattice formulation from which this phenomenon emerges analytically. We analyze a two-leg hard-core ladder under a leg bipartition, where non-local statistical strings cross the entanglement cut. We construct an exact lattice influence-functional representation showing that the reduced state factorizes strictly into a product-state amplitude and a full-counting-statistics functional. By introducing a commuting linked-cluster superoperator hierarchy that bypasses Baker-Campbell-Hausdorff ordering ambiguities, we prove that the first mixedness-generating sector is strictly density-density in character. Under a specific systematic coarse-graining procedure, we analytically derive the suppression of higher-order corrections, providing a controlled, closed-form framework showing how highly non-Gaussian lattice states evolve toward their quadratic continuum form under coarse-graining. We corroborate these analytical predictions through finite-size exact diagonalization and entanglement-spectrum diagnostics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25690v1
- Title: Quantum steering in networks: Measurement-device-independent detection, continuous variables, and practical Gaussian schemes
- Authors: Shao-Hua Hu, Chung-Yun Hsieh, Huan-Yu Ku, Ray-Kuang Lee, Paolo Abiuso
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25690v1  pdf=https://arxiv.org/pdf/2606.25690v1.pdf

Abstract:
We consider quantum steering certification in multipartite networks, with a focus on minimal trust scenarios: all-except-one parties are untrusted and treated device-independently. We show that it is always possible to lift steering certification to the measurement-device-independent regime, in which even the (last) trusted party can treat their local hardware as a black-box, except for a set of fiduciary quantum states used as the inputs to the experiment. This holds both for finite-dimensional systems as well as for bosonic continuous-variable systems, for which we provide a full characterization in the bipartite case. Additionally, we introduce measurement-device-independent network steering protocols based entirely on Gaussian operations -- which cannot be used for fully device-independent protocols, and thus become instead a viable option for minimal trust certification as soon as a single trusted input is inserted in the network. Our results present a basis for steering-based applications (such as randomness generation) with minimal trust beyond full nonlocality and with feasible experimental requirements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25735v1
- Title: Radial Schmidt mode detector of entangled photons
- Authors: Radhika Prasad, Nilakshi Senapati, Abhinandan Bhattacharjee, Anand K Jha
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25735v1  pdf=https://arxiv.org/pdf/2606.25735v1.pdf

Abstract:
High-dimensional spatially entangled two-photon state generated by spontaneous parametric down-conversion process (SPDC) has become a promising resource for several quantum information science applications. For harnessing high-dimensional entanglement advantages, detection capability in the Schmidt basis is a necessity. Spatial entanglement has been explored in several modal bases, such as pixel, azimuthal, and radial modes. Among them, pixel and azimuthal entanglement have been widely utilized due to efficient access to their Schmidt modes, while radial-mode entanglement remains underexploited. This is because for radial coordinates, there is neither a Schmidt-decomposed form for the SPDC photons nor is there a technique for measuring high-dimensional radial Schmidt modes, which is a major roadblock in harnessing radial mode advantages. In this work, we first theoretically show that the azimuthal averaging of SPDC two-photon state yields a radial Schmidt-decomposed form under typical experimental situations. We then demonstrate an innovative approach for extracting the radial Schmidt modes and their spectrum by characterizing the density matrix in the radial basis of one of the SPDC photons. Finally, we report the first-ever measurement of radial Schmidt spectrum of upto 50 radial Schmidt modes with about 98\% fidelity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25768v1
- Title: Sp(2N, R) interferometry in multi-mode Gaussian bosonic systems for optimal metrology and quantum control
- Authors: Chenwei Lv, Renbao Liu
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; physics.optics
- Links: abs=https://arxiv.org/abs/2606.25768v1  pdf=https://arxiv.org/pdf/2606.25768v1.pdf

Abstract:
Multi-mode interferometers for bosons in Gaussian states are important systems for quantum metrology with precision beyond the standard quantum limit and for bosonic quantum computing. However, there is a lack of theoretical foundation for generic $N$-mode Gaussian interferometry. In this work, we study quantum metrology and quantum control in multi-mode bosonic systems with quadratic Hamiltonians, exploiting the fundamental Sp$(2N,R)$ symmetry of such interferometers. We show that the optimal quantum control to maximize sensitivity requires aligning squeezing and displacement in the same direction. We propose Sp$(2N,R)$ echo, a multi-mode generalization of the SU$(1,1)$ interferometry, to achieve the sensitivity of phase estimation set by the quantum Fisher information. In addition, we introduce a geometrical means for reversing many-body dynamics with Sp$(2N,R)$ dynamical symmetry, such as dynamics of the bosonic Kitaev chain. Our schemes are readily realizable in optical, atomic, and mechanical platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25789v1
- Title: A Short Note on the Generators of Controlled Quantum Gates
- Authors: Richard M. Milbradt, Christian B. Mendl
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25789v1  pdf=https://arxiv.org/pdf/2606.25789v1.pdf

Abstract:
We present the analytical generators for arbitrary multi-qubit controlled gates. Closed forms for the generating Hamiltonians are given for gates with both multiple control and target qubits, as well as for arbitrary control conditions. This allows us to go beyond gate-based simulations of quantum circuits and incorporate decoherence and other noise in simulations of quantum computers. We exemplify this by simulating the impact of a harmonic oscillator interacting with two qubits during the application of a controlled NOT gate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25795v1
- Title: Benchmarking Dark Matter Search using a Parity-Check Protocol with Machine-Learning Optimized Pulses
- Authors: Yu-Han Chang, Ilya Moskalenko, Marko Kuzmanović, Ognjen Stanisavljević, Isak Björkman, David Díez-Ibáñez, Yikun Gu, Akash V. Dixit, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con; gr-qc; hep-ex
- Links: abs=https://arxiv.org/abs/2606.25795v1  pdf=https://arxiv.org/pdf/2606.25795v1.pdf

Abstract:
We report on an improved microwave detection protocol for dark matter candidates such as the axion and the dark photon. We employ a superconducting transmon qubit dispersively coupled to a double-cavity system, enabling quantum non-demolition measurements of the photon occupation in a relatively short-lived storage cavity. To reduce the experimental cycle time and enhance sensitivity for axion and dark-photon searches, we operate this detector in a regime of increased qubit-cavity coupling, resulting in Stark shifts of 4.6 MHz. In this regime, conventional control pulses suffer from strong frequency-detuning sensitivity and photon-number-dependent errors. We address this limitation by implementing frequency-detuning-robust $π/2$ pulses (obtained by machine-learning optimization) that preserve high-fidelity qubit control over a bandwidth of approximately 20 MHz. We experimentally validate this protocol and demonstrate single-photon detection performance comparable to previous implementations, despite significantly reduced qubit coherence times and storage-cavity lifetimes. Using parity-based measurement sequences combined with a Hidden Markov Model (HMM) analysis, we achieve background rates on the order of $\mathcal{O}(20)$ Hz. In the absence of a magnetic field, we derive exclusion limits on the dark photon model for dark matter, reaching a sensitivity to the kinetic mixing angle of $ε_{95\%} \sim 1\times10^{-14}$ at 5.051 GHz. These results establish machine-learning robust control as a key enabler for faster, more scalable microwave quantum sensors for dark-matter searches.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25807v1
- Title: A Candidate Framework for Free-Space Quantum Key Distribution based on Geometrical-Configuration Modulation
- Authors: Yu-Ming Bai, Yu-Xuan Liu, Ming-Han Ding, Jun-Lin Li
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2606.25807v1  pdf=https://arxiv.org/pdf/2606.25807v1.pdf

Abstract:
This paper proposes a candidate framework for free-space quantum key distribution (QKD) based on geometrical-configuration modulation (GM). In the minimal implementation considered here, Alice coherently splits a single photon emitted from one source into two spatial output modes with a tunable separation, and uses the source separation $R$ as the GM variable that defines the prepared single-photon spatial superposition state. Bob records the single-photon detection coordinate in the far field or Fourier plane, providing the correlated data used for soft-input information reconciliation. Based on this physical mechanism, we first establish an $R-x$ protocol model in which the source separation $R$ and the single-photon detection coordinate $x$ are random variables, and further propose an $R-Δx$ extension based on the difference variable $Δx$ between adjacent accepted detection events to mitigate slowly varying center drift in free-space links. The framework specifies state preparation, far-field conditional probabilities, soft-input information generation, parameter estimation, reconciliation, and asymptotic candidate key-rate formulas. A complete composable security analysis further requires derive an explicit computable upper bound on Eve's information from experimentally observed parameters, together with finite-key analysis and experimental validation under free-space conditions. The proposed candidate framework (GM-QKD) provides a modulation approach based on spatial degrees of freedom in which the source geometry serves as the modulation variable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25815v1
- Title: Collective rotational cat states of molecules in microwave cavities
- Authors: Volker Karle, Florian Kluibenschedl, Mikhail Lemeshko, Vasil Rokaj
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25815v1  pdf=https://arxiv.org/pdf/2606.25815v1.pdf

Abstract:
We show theoretically that an ensemble of polar molecules coupled to a microwave cavity supports hybrid rotational-photonic cat states. The cavity couples to a symmetric rotor in the bright manifold of $N$ molecules with $\sqrt{N}$-enhancement. In the dispersive limit of the collective strong coupling regime, virtual multilevel transitions induce an effective Kerr nonlinearity, as confirmed by Wigner tomography and a Schrieffer-Wolff analysis, leading to parity-locked cat structure in the cavity sectors. Collective molecular rotations thus provide a new route to hybrid light-matter cat states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25860v1
- Title: Nonlinear Dynamics of Coherent Parametric Amplification in Multipartite two-level System under Intrinsic Decoherence
- Authors: Muhammad Ibrahim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25860v1  pdf=https://arxiv.org/pdf/2606.25860v1.pdf

Abstract:
In this work, we study the dynamics of global quantum discord and quantum Fisher information in a multipartite system of two-level atoms interacting with a coherent field. The model includes parametric amplification, Kerr-type nonlinearity, and intrinsic decoherence to examine how these effects control quantum correlations and parameter-estimation sensitivity. The results show that, without intrinsic decoherence, both quantities exhibit rapid oscillations with clear collapse and revival behavior. Strong Kerr nonlinearity and strong parametric amplification enhance global quantum discord, while quantum Fisher information becomes maximum under a suitable balance of Kerr nonlinearity and amplification strength. Increasing the number of atoms generally strengthens global quantum discord but does not always improve quantum Fisher information. Intrinsic decoherence damps the oscillations and drives the system toward steady-state behavior.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25870v1
- Title: Evolving Quantum Error-Correcting Encodings for Molecular Simulation
- Authors: Kenny Heitritter, James Brown, Tarini Hardikar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25870v1  pdf=https://arxiv.org/pdf/2606.25870v1.pdf

Abstract:
Useful quantum algorithms require many coupled discrete design choices. We study LLM-driven evolutionary program synthesis -- a language model edits a program, an external verifier scores the result, and high-scoring programs are retained and re-mutated -- as a tool for quantum-computing research. As a case study, we apply this loop to the Generalized Superfast Encoding (GSE), a fermion-to-qubit encoding whose prior molecular constructions reach code distance $3$. The search discovered interpretable constructor programs whose codes have \emph{exact} distance $5$ on the molecular instances tested, and distance $6$ on one $20$-mode instance, under strict stabilizer-coset semantics. To our knowledge these are the first GSE/superfast encodings beyond distance $3$ for dense molecular Hamiltonians. A second search, guided by verifier analysis of the first artifact, found a circulant constructor that reaches a five-qubits-per-mode floor on the tested $12$-, $14$-, $16$-, and $20$-mode instances, with certified dense-rule fallback at the failing $18$-mode case. As secondary resource descriptors, in a code-capacity \emph{memory} comparison at $p=10^{-3}$ the resulting encodings use $4.2$--$5.0\times$ fewer data qubits than a scoped per-mode Jordan--Wigner $+$ $[[25,1,5]]$ surface route and have $3.4$--$8.2\times$ lower logical-failure rates under finite-weight decoding tables with explicit truncation brackets; we claim no circuit-level fault-tolerance or Trotter-cost advantage. The search trajectory illustrates a general operating lesson: rewarding distance alone selects trivial dense graphs, whereas holding verified distance fixed and rewarding compression selects structured rules.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25889v1
- Title: Resonant false vacuum decay in two dimensions on a 4000-qubit quantum annealer
- Authors: Gregor Humar, Jean-Yves Desaules, Luka Pavešić, Marko Ljubotina, Zlatko Papić, Kristel Michielsen, Jaka Vodeb
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2606.25889v1  pdf=https://arxiv.org/pdf/2606.25889v1.pdf

Abstract:
From cosmology to quantum matter, metastable states often decay through the nucleation and growth of competing domains, with false vacuum decay providing the paradigmatic example of this process. Here we demonstrate a distinct regime in which domain growth outpaces nucleation by orders of magnitude and is controlled by local resonance conditions. Using a programmable quantum annealer with more than 4000 qubits, we realize a two-dimensional quantum Ising model whose metastable spin-polarized state encodes a false vacuum. At a specific value of the longitudinal field, single-spin flips at the boundary of a seeded bubble become resonant, enabling kinetically constrained expansion. Combining experiment with tensor-network simulations and stochastic circuit modeling, we observe nearly ballistic growth of true-vacuum domains with sub-ballistic interface broadening, consistent with Kardar--Parisi--Zhang universality. Our results establish a growth-dominated regime of false vacuum decay and show how large-scale quantum simulation can access nonequilibrium metastable dynamics relevant to quantum field theory, cosmology, and strongly correlated matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25920v1
- Title: Finite-Shot Sensitivity for Moment Estimation in Quantum Metrology
- Authors: Shaowei Du, Shuheng Liu, Weidong Li, Luca Pezzè, Augusto Smerzi, Qiongyi He
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25920v1  pdf=https://arxiv.org/pdf/2606.25920v1.pdf

Abstract:
The quantum Cramér-Rao bound can be saturated only asymptotically and does not specify how many measurements are needed for a concrete estimator to approach it. We develop a finite-measurement theory for method-of-moments estimation, where the parameter is inferred from the sample mean of a calibrating observable rather than from the full likelihood. For general quantum statistical models, the expansion is written in terms of the calibration curve and the central moments of the measured observable. Nonlinear calibration curves make the usual moment estimator biased at finite measurement number; we construct a bias-corrected estimator with bias $O(ν^{-3})$. This gives sensitivity corrections beyond the leading error-propagation term of the chosen moment protocol. We identify a general density-matrix condition under which the full $1/ν^2$ correction vanishes. In unitary examples, the leading residual correction appears at order $1/ν^3$, is governed by calibration curvature, and can be reduced or cancelled by higher-rank components of the same measured observable. The resulting thresholds quantify how many measurements are needed before the asymptotic sensitivity of a moment-estimation protocol is operationally visible.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25929v1
- Title: Klein--Gordon Dynamics from Intrinsic Phase Periodicity
- Authors: Emiliano Puddu
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2606.25929v1  pdf=https://arxiv.org/pdf/2606.25929v1.pdf

Abstract:
This work develops a phase-based formulation of relativistic wave dynamics, demonstrating that the Klein--Gordon equation emerges naturally from the foundational assumption of intrinsic phase periodicity in material fields. Mapping the phase directly onto the classical action, we postulate that localized excitations possess an invariant rest-frame oscillation governed by a proper frequency $ω_0$. This physical condition establishes an operational mass-frequency relation, $m = \hbar ω_0 / c^2$, without requiring rest energy as an independent, axiomatic input. We show that the Klein--Gordon equation arises as the minimal local, linear, Lorentz-invariant field equation compatible with this internal phase structure. Within this framework, mass acts as an intrinsic frequency scale governing wave propagation, and relativistic kinematics is fully recovered as a structural consequence of phase coherence. This approach provides a unified wave-mechanical interpretation where particle dynamics maps onto the group velocity of dispersive wave packets, offering an intuitive account of free propagation, dispersion, and tunneling across potential barriers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25933v1
- Title: From spectral structure to sensing limits in quantum thermometry
- Authors: Youssef Aiache, Simone Cavazzoni, Abderrahim El Allati, Paolo Bordone, Matteo G. A. Paris
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25933v1  pdf=https://arxiv.org/pdf/2606.25933v1.pdf

Abstract:
The precision of a quantum thermometer is fundamentally constrained by the spectral structure of the probe itself, and a systematic mapping between the configurations of energy levels and thermometric performance provides relevant information to design optimized devices. In this work, we establish such a mapping by analyzing a broad class of quantum systems, ranging from finite spin ensembles and degenerate atoms to confining potentials, quantum walks, and continuous-spectrum models. We derive exact scaling laws for the quantum Fisher information, revealing two distinct high-temperature universality classes: finite-spectrum probes exhibit a $T^{-4}$ decay, while unbounded or continuous spectra yield a slower $T^{-2}$ decay. At low temperatures, we show that sensitivity, though universally exponentially suppressed, can be enhanced arbitrarily by engineering degenerate excited states or a quantum walk on a fully connected topology. By contrast, specific quantum walk topologies provide a distinct enhancement mechanism based on gap engineering, whereby an optimal network size yields an optimized $T^{-2}$ low-temperature scaling. Furthermore, power-law spectra enable tunable scaling of thermometric performance with system size, offering a design principle for optimal probes in specific temperature windows. Our results contribute to transform spectral information into a resource for quantum thermometry, providing both fundamental bounds and practical guidelines to tailored temperature sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25974v1
- Title: Tensor network characterization and mitigation of readout errors
- Authors: Yuchen Guo, Shuo Yang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.25974v1  pdf=https://arxiv.org/pdf/2606.25974v1.pdf

Abstract:
Readout errors are a major bottleneck to extracting reliable information from near-term quantum processors, especially when spatial correlations are non-negligible. We present a unified tensor-network framework that models the readout process as a matrix product operator (MPO), enabling efficient characterization and mitigation beyond uncorrelated approximations. The MPO model is trained via likelihood optimization on calibration data and applies to multiple tasks, including nonlocal observable estimation, random circuit sampling, and random-measurement protocols, such as classical shadows and learning-based tomography. Experiments on a superconducting processor and numerical simulations up to 20 qubits show that the MPO model captures correlated readout errors that uncorrelated models miss, with a sample cost that grows only near-linearly with system size. When extended to two-dimensional systems, the framework can also be integrated with tensor-network quantum error-correction decoders by performing joint inference over data and readout errors. These results establish tensor-network readout error mitigation as a scalable and versatile approach for noise-aware quantum data processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26034v1
- Title: Estimating Fidelity to a Reference Quantum State
- Authors: Qisheng Wang
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.IT
- Links: abs=https://arxiv.org/abs/2606.26034v1  pdf=https://arxiv.org/pdf/2606.26034v1.pdf

Abstract:
We consider the problem of estimating the fidelity of an unknown quantum state to a known reference state to within additive error $\varepsilon$. We show that the sample complexity is $O(r^2/\varepsilon^2)$ with optimal $\varepsilon$-dependence when the reference state is of rank $r$, improving the previous best $O(r^2\log^2(1/\varepsilon)/\varepsilon^4)$ due to Utsumi, Nakata, Wang, and Takagi (QIP 2026). We also provide a lower bound of $Ω(r/\varepsilon^2)$, improving the previous best $Ω(r/\varepsilon+1/\varepsilon^2)$, with implications to quantum query complexity. Moreover, we further consider the case where the unknown state is of rank at most $r$ while the reference state can be arbitrary, for which the sample complexity is shown to be $O(r^2/\varepsilon^4)$. As an application, we present an approach to tolerant quantum state certification, generalizing the exact certification studied in Bădescu, O'Donnell, and Wright (STOC 2019).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26076v1
- Title: Many-Body Second Order Green's Function Theory for Ab Initio Molecular Quantum Electrodynamics
- Authors: Amirhosein Amini, Jaime Cerda, Leopoldo Mejía, Arkajit Mandal
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2606.26076v1  pdf=https://arxiv.org/pdf/2606.26076v1.pdf

Abstract:
In this work, we develop two many-body quantum electrodynamic methods to calculate the ground-state energies of strongly coupled light-matter molecular systems. Specifically, we extend the second-order many-body Green's function theory (GF2) for electronic systems to incorporate electron-boson couplings. We employ two ansätze to treat the bosonic part of the system, namely the coherent-state (CS) and Lang-Firsov (LF) transformed vacuum state. These are combined with the GF2 method to construct two new approaches, which we refer to as CS-GF2 and LF-GF2. We benchmark CS- and LF-GF2 by studying various molecular systems inside an optical cavity. We investigate $\mathrm{H}_2$ and $\mathrm{LiH}$ potential energy surfaces, keto-eneol tautomerization energy barrier, van-der Waals interactions between two $\mathrm{H_2}$ molecules and the torsional potential energy surface of the ethylene molecule, $\mathrm{C_2H_4}$. Both methods provide highly accurate energies, with only modest additional improvement observed in LF-GF2.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26084v1
- Title: Operational detection of Wigner negativity in arbitrary quantum states from few copies
- Authors: Sudip Chakrabarty, Bivas Mallick, Ananda G. Maity, A. S. Majumdar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.26084v1  pdf=https://arxiv.org/pdf/2606.26084v1.pdf

Abstract:
States with negative Wigner functions form a fundamental class of nonclassical resource underlying quantum advantage. Here we develop a unified framework to detect Wigner negativity of arbitrary states using experimentally accessible moments of the Wigner function that can be estimated from a modest number of state copies. Exploiting constraints satisfied by positive phase-space distributions, we derive complementary hierarchies of negativity criteria based on $\mathcal{L}_p$-norm inequalities, log-convexity relations, and Hankel-matrix positivity, yielding increasingly powerful witnesses of Wigner negativity without full phase-space tomography. The framework further enables quantitative characterization of Wigner negativity from a small number of experimentally accessible observables. Next, we establish an exact multicopy representation of all Wigner moments as expectation values of parity-based observables, providing a practical and scalable route to their experimental estimation. We demonstrate the performance of our scheme through numerical simulations of randomized-measurement and classical-shadow protocols. Finally, we show that the framework extends naturally to identifying nonclassical resources such as bipartite and multipartite entanglement. These results establish Wigner moments as a versatile tool for the scalable detection and quantification of nonclassical resources in continuous-variable quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26085v1
- Title: Analytic Approach to Quantum Control Using Quantum Signal Processing
- Authors: Aishwarya Majumdar, John M. Martyn, Yuan Liu, Nathan Wiebe
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.26085v1  pdf=https://arxiv.org/pdf/2606.26085v1.pdf

Abstract:
Realizing coherent quantum computation requires precise and robust manipulation of quantum systems through quantum control protocols. Most quantum control techniques rely on heuristic methods for designing the driving pulses that steer the system towards a target state. Such methods are often based on brute-force optimization and offer limited understanding of the solution landscape. In contrast, quantum algorithms offer a rich body of analytical methods with rigorous error guarantees for implementing unitary and non-unitary transformations, which suggests a promising direction for developing new approaches to quantum control. Among various such algorithms, quantum signal processing (QSP) has emerged as a powerful framework for quantum algorithm design, implementation, and optimization. However, its potential for quantum control remains largely unexplored. In this work, we establish QSP-Control, an analytical framework for quantum control of qubit-oscillator dynamics. We focus on dispersively coupled qubit-oscillator systems and employ the QSP formalism to mitigate unwanted nonlinear effects arising from cross-Kerr interactions. In addition, we develop constructions for precise manipulation of Fock states by designing Fock-state-selective operators, based on structural parallels between the Jaynes-Cummings interaction and QSP. These findings demonstrate how several practically relevant problems in quantum control can be mapped to forms amenable to QSP, offering both a systematic design framework and an interpretable perspective on quantum control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26088v1
- Title: Simulating Universal Quantum Gate Sets on Photonic OAM Qubits: Single-Qubit and Multi-Qubit Operations via Spatial Light Modulator Phase Holography
- Authors: Saleha Maqsood, Muhammad Kamran, Tahir Malik
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.26088v1  pdf=https://arxiv.org/pdf/2606.26088v1.pdf

Abstract:
Spatial light modulators (SLMs) have emerged as reconfigurable platforms for photonic quantum information processing, offering software-defined control over the orbital angular momentum (OAM) of light encoded in Laguerre-Gaussian (LG) beams. This paper presents a comprehensive simulation and hardware-grounded fidelity analysis of quantum gate operations implemented on the HOLOEYE LC 2012 transmissive SLM. A realistic three-channel noise model comprising 8-bit quantisation noise, twisted-nematic (TN) electronic and thermal noise, and phase-wrap clipping error is obtained from the manufacturer's datasheet without free-parameter fitting, yielding a total noise of $σ_{\text{total}} = 92.4\text{mrad}$. The complete universal single-qubit gate set $\{X, Y, Z, S, T, H\}$ and two-qubit entangling gates $\{\text{CNOT}, \text{CZ}, \text{SWAP}\}$ are simulated on a $512 \times 512$ computational grid. Results show that predicted gate fidelity are in the range of $F = 0.9914\text{--}0.9936$, with fork grating gates limited primarily by TN noise and phase gates achieving higher fidelity owing to zero phase-wrap clipping error. In addition, Bell state preparation via the H-CNOT circuit achieves $F(Φ^+) = 0.9914$ after two SLM interactions. We benchmark our obtained results against six published experimental studies spanning the 78%--99.6% fidelity range. Finally, a wavelength-dependent analysis identifies 450--532 nm operation as the optimal regime for this device.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26090v1
- Title: Fast mixing of all-to-all quantum systems at high temperatures
- Authors: Thiago Bergamaschi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.26090v1  pdf=https://arxiv.org/pdf/2606.26090v1.pdf

Abstract:
It is shown that arbitrary quantum $k$-local Hamiltonians with bounded strength interactions admit a quantum Gibbs sampler [CKG23] with a system-size independent spectral gap, at sufficiently high temperatures. This generalizes the existing quantum fast-mixing results beyond the geometrically-local setting. As a consequence, such systems admit fully-polynomial time quantum approximation algorithms for partition functions and global expectation values.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24899v1
- Title: From Meta Idea to Advanced Mathematical Discovery -- Human-AI Co-Discovery of Sign-Embedding Quantum Algorithms
- Authors: Yanqiao Wang, Jin-Peng Liu, Peng Li, Yang Liu
- Categories: cs.LG (primary); cs.LG; cs.AI; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24899v1  pdf=https://arxiv.org/pdf/2606.24899v1.pdf

Abstract:
AI-assisted mathematics is often evaluated on solving predefined problems. In practice, however, many important advances begin earlier, when a vague research intuition is transformed into a concrete problem, a promising route, and a theorem family worth proving. This report studies that stage through a case study that led to sign-embedding quantum algorithms for matrix equations and matrix functions, foundational primitives in quantum linear algebra and operator-output quantum algorithms. The project began with a human-originated intuition that rational approximation is especially effective for jump-type functions such as the sign function, and might therefore serve as a design principle for quantum algorithms. Rather than merely assisting after the problem was fixed, AI-assisted exploration, including workflows later integrated into the agentic AI-mathematician system AIM, played a key role in expanding this intuition into a route map, comparing candidate formulations, and converging toward sign embedding as the central framework. AIM then helped connect a known matrix-sign identity to wider classes of matrix equations and matrix functions, and drafted proof and complexity calculations. The decisive scientific judgments remained human: selecting which human-AI-expanded routes were worth pursuing, rejecting a Cayley-trapezoidal approximation when its validity required a hidden condition, and refining the Sylvester implementation from a coarse quadratic-gap query route to the final factorized and scaled analysis. The report argues that human-AI co-discovery workflows, with systems such as AIM as important components, are most valuable not as standalone theorem provers, but as research partners for problem formation, connection discovery, derivation, and skeptical review inside a human-gated research loop.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.24904v1
- Title: Spectral Leakage and Masking Effects in the Measurement of Hyperuniformity
- Authors: Yang Jiao
- Categories: cond-mat.soft (primary); cond-mat.soft; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24904v1  pdf=https://arxiv.org/pdf/2606.24904v1.pdf

Abstract:
The detection of hyperuniformity relies critically on accurate characterization of the small-wavenumber behavior of the static structure factor of the system. In practice, however, measurements are performed on finite subsystems or through incomplete observations that effectively mask portions of the underlying configuration. Inspired by a recent numerical study [Y. Liu, X. Li, J. Tian, X. Yan, G. Zhang, {\it J. Chem. Phys.} {\bf 164}, 094102 (2026)], we develop a unified theoretical framework that quantifies how finite windows and spatially correlated binary masks modify the observed structure factor. We show that the measured structure factor $S_{obs}(k)$ is the convolution of the intrinsic structure factor with the spectral density of the observation function, whether it is a compact window or an extended random mask. For generic hyperuniform systems with small-$k$ scaling $S(k)\sim k^α$, finite observation window induces a universal quadratic leakage term at sufficiently small wavenumbers (i.e., $k \lesssim 1/L$), leading to an apparent $k^{2}$ scaling independent of the true exponent. The true hyperuniform exponent $α$ can only be measured in the intermediate regime $1/L \ll k \ll q_c$. In stealthy hyperuniform systems, where the intrinsic structure factor possesses a spectral gap, all observed small-$k$ power arises entirely from this convolution mechanism. For spatially correlated masks, we derive the corresponding convolution relation in terms of the mask spectral density and identify conditions under which hyperuniform signatures are suppressed, preserved, or distorted. Our results establish quantitative criteria for reliably extracting intrinsic scaling exponents and distinguishing genuine hyperuniform order from measurement-induced artifacts.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25129v1
- Title: Halo-Independent Quantum Sensor Probes of Low-Velocity Dark Matter
- Authors: Muping Chen, Graciela B. Gelmini, Volodymyr Takhistov, Koichiro Yasuda
- Categories: hep-ph (primary); hep-ph; astro-ph.CO; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25129v1  pdf=https://arxiv.org/pdf/2606.25129v1.pdf

Abstract:
We present a halo-independent framework for sub-GeV dark matter (DM) direct detection using quantum sensors with sub-eV energy thresholds. Such detectors enable access to low DM velocities and may be sensitive to departures from the Standard Halo Model that are challenging to probe with conventional direct DM detection experiments. The method expresses the DM scattering event rate in terms of a detector and particle model-dependent response function, and a universal halo function common to all experiments to be determined from data. This allows the local DM velocity distribution to be constrained. As representative implementations, we consider TES (Al) and MKID (TiN)-like sensors and show that their differing material responses probe complementary regimes of the DM velocity distribution. Applying the framework to mock data derived from several benchmark local halo models, we demonstrate how the assumed halo function could be reconstructed. This framework demonstrates the potential of quantum sensors as a new avenue for mapping the local DM velocity distribution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25194v1
- Title: Hodge Spectral Surrogates for Topology-Constrained Optimization
- Authors: Satoshi Kanno, Yoshi-aki Shimada
- Categories: math.AT (primary); math.AT; cs.CG; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25194v1  pdf=https://arxiv.org/pdf/2606.25194v1.pdf

Abstract:
Topological information is widely used in data analysis, network design, and machine learning, and topological constraints naturally arise when optimizing or generating objects with prescribed homological structure. However, directly controlling Betti numbers and persistent homology is difficult because they are discrete and combinatorial. We propose a differentiable framework for topology-constrained optimization based on Hodge-spectral relaxations of homological constraints and low-pass spectral filters. From soft graphs and soft clique complexes, we construct Hodge-Laplacian-type spectral relaxations that unify graph clique complexes and Vietoris--Rips filtrations of point clouds. In the hard limit, the penalty-regularized ambient operator recovers the ordinary Hodge Laplacian on the active subcomplex, while in the soft regime it serves as a differentiable low-frequency spectral surrogate. Homological information is represented by zero and near-zero modes, and differentiable topological objectives are defined using heat filters, resolvent filters, and polynomial Laplacian moments. For point clouds, we show that the proposed Hodge spectral-filter losses yield more spatially distributed gradients, smoother scale-normalized behavior under persistence-pairing changes, and geometry-aware update directions than persistent-homology-based losses. For graph clique complexes, Laplacian moments control normalized first-Betti-type quantities and can be combined with ordinary graph-feature objectives. We also discuss connections to trace-based normalized Betti-number estimation, polynomial spectral methods, and possible quantum trace estimation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25196v1
- Title: Modeling and Analysis of Phase Instability in Photonic Processor
- Authors: Gökhan Elmas, Igor Litvin, Paul Kohl, Janis Nötzel
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25196v1  pdf=https://arxiv.org/pdf/2606.25196v1.pdf

Abstract:
Achieving both reconfigurability and stable output signals is a critical challenge in the development of integrated photonic circuits for large-scale optical quantum information processing. This has led to the creation of multimode photonic processors, also known as reconfigurable multimode interferometers, which have wide-ranging applications in quantum and classical information processing. However, maintaining phase stability in multi-port input signals remains a significant hurdle, particularly due to the phase instabilities introduced by active cooling systems and temperature drifts in the photonic processor. In this study, we propose theoretical models to simulate phase instability in photonic processors and validate them against experimental results. Two distinct modeling approaches were employed: a Brownian random walk and phase reconstruction based on experimentally observed oscillating harmonics. Additionally, we verified and applied our model to a specific application for input phase correction using self-feedback control within the photonic processor.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25364v1
- Title: A Unified Josephson Dynamics Perspective for Single-Cavity BECs: From Self-Trapping to Dynamical Phase Transitions
- Authors: Soi-Chan Lei
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25364v1  pdf=https://arxiv.org/pdf/2606.25364v1.pdf

Abstract:
We investigate a two-component Bose-Einstein condensate (BEC) strongly coupled to a single optical cavity, effectively described by a mean-field Dicke model supplemented with interatomic nonlinearities. Here, we propose a unified theoretical framework demonstrating that macroscopic quantum self-trapping (MQST) natively emerges between two internal atomic energy levels within a single cavity. By deriving the dimensionless semiclassical Josephson equations (SJE) governing this purely internal-state architecture, we analytically determine the critical nonlinear threshold and intrinsic phase shift mechanism for the phase transition. Based on this framework, we present two approaches for manipulating quantum phase transitions: dynamic in-situ tuning via photon pumping and inducing non-equilibrium dynamical phase transitions (DPT) via real-time parameter quenches. Furthermore, we rigorously prove that the effective charging energy driving this system scales exactly as one-quarter of the effective spin-dependent interaction energy -- the precise parameter governing recent spin-orbit coupled (SOC) BEC experiments. Incorporating realistic $^{87}$Rb atomic parameters, we substantiate that these single-cavity MQST and transition dynamics are highly feasible for observation under current state-of-the-art cold-atom technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25378v1
- Title: Wide-field NV magnetometry under simultaneous high-pressure and high-temperature conditions
- Authors: Masahiro Ohkuma, Eikichi Kimura, Shumpei Ohyama, Miu Tezuka, Ryo Matsumoto, Shinobu Onoda, Yoshihiko Takano, Shintaro Azuma, et al.
- Categories: physics.app-ph (primary); physics.app-ph; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25378v1  pdf=https://arxiv.org/pdf/2606.25378v1.pdf

Abstract:
We demonstrate wide-field optically detected magnetic resonance (ODMR) under simultaneous high-pressure and high-temperature conditions using nitrogen-vacancy (NV) centers. Although NV-center magnetometry has been widely used for spatially resolved magnetic-field imaging, its application to extreme environments combining pressure and temperature remains challenging. In this work, we show that ODMR can be observed at 5 GPa and 500 K, demonstrating the feasibility of NV spin readout under such combined extreme conditions. We further perform wide-field ODMR of iron at 7 GPa and 500 K, where the stray magnetic field from the sample is spatially visualized through the pressure cell. These results establish NV-center magnetometry as a promising platform for imaging magnetic phenomena in materials under high-pressure and high-temperature environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25411v1
- Title: Spin-imbalanced fermion on a dynamic lattice
- Authors: Jie Liu, Xiaofan Zhou, Suotang Jia
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25411v1  pdf=https://arxiv.org/pdf/2606.25411v1.pdf

Abstract:
We investigate the magnetic order of a one-dimensional spin-1/2 fermion dynamical lattice, where itinerant fermions are coupled to bond-centered localized spins via an Ising-like spin dependent hopping. The model provides an anisotropic dynamical extension of conventional spin-1/2 fermion systems, in which the motion of itinerant fermions is directly modulated by the configuration of localized spins. Using density matrix renormalization group simulations, we map out the ground state phase diagram in various parameter spaces. Depending on the interplay among the hopping dependent on localized spins, the longitudinal field, and the external Zeeman field, two distinct phases are obtained: a paramagnetic phase and a spin-density-wave phase. Most notably, in the partially spin-polarized fermion phase, the spin-density wave ordering wave vector exhibits two distinct phenomena, corresponding respectively to the nesting vectors $2k_{F\uparrow}$ and $2k_{F\downarrow}$ of the spin-resolved Fermi surfaces. We further demonstrate that the two spin-density wave phases are robust against the repulsive Hubbard interaction between itinerant fermions. Our results reveal a novel route for tuning magnetic modulations in one-dimensional correlated systems and enrich the microscopic understanding of dynamical lattice magnetism.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25433v1
- Title: Weak decay of the positronium ion
- Authors: Nishat Ul Sani, M. Jamil Aslam, Ishtiaq Ahmed
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25433v1  pdf=https://arxiv.org/pdf/2606.25433v1.pdf

Abstract:
The positronium ion ($\mathrm{Ps}^-$), a coulombic three-body bound state of two electrons and a positron, predominantly decays via electron-positron annihilation into electromagnetic final states. While its radiative decay channels have been extensively studied, much less attention has been given to weak processes in this system. In this work, we investigate the rare decay $\mathrm{Ps}^- \to e^- ν_μ\barν_μ$, obtained by replacing the photon in $\mathrm{Ps}^- \to e^- γ$ with a virtual $Z$ boson. Treating the three-body process as an effective two-body transition, $\mathrm{Ps}^- \to e^- Z^*\left(\to ν_μ\barν_μ\right)$, we compute the decay rate by explicitly evaluating all spin configurations of the initial bound state and final particles. The result agrees with that obtained using the standard spin-summation formalism of quantum field theory. We find that the branching ratio is comparable to that of the weak decay of ortho-positronium, $\mathrm{o\text{-}Ps} \to γν\barν$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.25957v1
- Title: From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response
- Authors: Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi
- Categories: cs.RO (primary); cs.RO; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.25957v1  pdf=https://arxiv.org/pdf/2606.25957v1.pdf

Abstract:
Locating survivors of building collapses within the first 72 hours is a critical challenge in disaster response, and existing sensing modalities provide only partial information about the structure beneath the rubble.   This paper proposes drone-based quantum magnetometry as a complementary modality and develops a simulation pipeline spanning rubble physics, sensor-array deployment, and active spatial reconstruction. We use Unreal Engine to generate a steel-reinforced concrete parking-garage collapse and compute the induced magnetic field via a per-triangle dipole approximation, establishing that meaningful magnetic structure is recoverable in the sub-pT to sub-nT range from roughly 1 m above the roofline. Then, we feed sparse multi-sensor samples into a Gaussian Process Regression back-end driven by Bayesian active sampling and validate the pipeline across multiple independent collapse realizations; a three-sensor array optimizes the trade-off between gradient resolution and UAV payload constraints, and active sampling reaches peak structural correlation in roughly $100$ samples. Together, these results indicate that quantum-grade sensing could become a useful tool for drone-based structural analysis and potentially void detection in collapsed buildings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26081v1
- Title: Folds of one curve: the superradiant phase diagram of Dicke modes with interacting matter
- Authors: Max Hörmann
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2606.26081v1  pdf=https://arxiv.org/pdf/2606.26081v1.pdf

Abstract:
We give a thermodynamic-limit account of Dicke models with one cavity mode coupled collectively to interacting matter. Integrating out the cavity yields an exact self-consistent functional of the magnetisation $m$, $\tilde e(m) = λm^2/2 + e_{\rm mat}(λm)$: a classical penalty on the bare-matter energy $e_{\rm mat}$ in the self-consistent field $h = λm$, with $λ= g^2/(2ω_c)$ the collective coupling. Supplying only that scalar field, the photon creates no phase the matter does not already possess. States holding a minimum form one connected curve, $λ(m) = μ_{\rm mat}^{-1}(m)/m$, so superradiant first-order transitions are folds of one equation of state not crossings of disjoint sheets, and a fold can straighten into a continuous line. The remaining rules are local, each with a spectral counterpart: onset by the leading singularity of $e_{\rm mat}$ (a softening polariton), order by one bare response -- the Landau quartic, or a divergent susceptibility forcing a Larkin-Pikin (LP) fold. For the Dicke-Ising model the Landau coefficients are exact, giving in closed form the second-order boundary and both zero-quartic fields, one tricritical; a $1/d$ expansion maps all four phases, with the AS-PS transition first order for $d\le d_{uc}=3=4-z$ (LP) and tricritical points in the $(d,ε)$ plane above. At the degenerate quadruple point the matter is a Rydberg-blockade chain, solved by strict-blockade iDMRG: the antiferromagnetic superradiant (AS) phase persists as a finite 1D wedge, first order into the corner. Other magnets: the triangular antiferromagnet keeps a continuous superradiant-superradiant line (3D-XY, no fold forced); the compass chain a BKT-functional onset; the Heisenberg and XX chains, via a conserved operator, a spectrally silent first-order onset; and the Dicke-Heisenberg diagram an exact tricritical point at the saturation corner.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.26096v1
- Title: Higher Berry curvature, second Chern numbers and magnetoelectric coupling in crystalline insulators
- Authors: Niclas Heinsdorf, Ken Shiozaki
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2606.26096v1  pdf=https://arxiv.org/pdf/2606.26096v1.pdf

Abstract:
We rewrite a lattice model of the four-dimensional Chern insulator as a family of translationally-invariant infinite chains over the three-dimensional Brillouin zone and compute its higher three-form Berry curvature using infinite matrix product states (iMPS). We calculate the topological phase diagram of the associated Dixmier--Douady--Kapustin--Spodyneiko (DDKS) number as a function of the model's mass term, and show that it is exactly congruent to the phase diagram in terms of the second Chern number, the analytic expression of which is known for this particular model. This agreement demonstrates that higher Berry curvature can be used to compute second Chern numbers in a manifestly quantized manner. Motivated by the connection between the second Chern form and the Chern--Simons axion coupling, we study magnetoelectric coupling in three dimensions and its relation to higher Berry phases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2407.01975v3
- Title: Imposing Constraints on Driver Hamiltonians and Mixing Operators: From Theory to Practical Implementation
- Authors: Hannes Leipold, Federico M. Spedalieri, Stuart Hadfield, Eleanor Rieffel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2407.01975v3  pdf=https://arxiv.org/pdf/2407.01975v3.pdf

Abstract:
Driver Hamiltonians and Mixing Operators that satisfy constraints is an important part of ansatz construction for many quantum algorithms. In this manuscript, we give general algebraic expressions for finding Hamiltonian terms and analogously unitary primitives, that satisfy constraint embeddings and use these to give complexity characterizations of the related problems. We prove that knowing if operators exist that enforce classical constraints is NP-Complete in the general case, but give algorithmic procedures with worse-case polynomial runtime to find any operators with a constant locality bound; a useful result since many constraints imposed admit local operators to enforce them in practice. We then give algorithmic procedures to turn these algebraic primitives into Hamiltonian drivers and unitary mixers that can be used for Constrained Quantum Annealing (CQA) and Quantum Alternating Operator Ansatz (QAOA) constructions by tackling practical problems related to finding an appropriate set of reduced generators and defining corresponding drivers and mixers accordingly. We consider a new QAOA approach based on the maximally disjoint subset as well as higher order constraint satisfaction terms for 1-in-3 SAT, which dramatically outperform the X-mixer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2501.15218v3
- Title: Construction of new type of CNOT gate using cross-resonance pulse in the transmon-PPQ system
- Authors: Jeongsoo Kang, Younghun Kwon
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2501.15218v3  pdf=https://arxiv.org/pdf/2501.15218v3.pdf

Abstract:
The transmon, known for its fast operation time and the coherence time of tens of microseconds, is the most commonly used qubit for superconducting quantum processors. However, it is still necessary to enhance the coherence time and the gate fidelity of superconducting quantum processors for the practical implementation of fault-tolerant quantum computing. Meanwhile, a novel superconducting qubit, which has the ability to protect the Cooper-pair parity on the superconducting island, has been proposed. This new qubit shows better coherence performance than the transmon, but it does not yet have an efficient method for realizing a superconducting hybrid system that harnesses it.   In this work, we show how to implement a new type of CNOT gate in a superconducting hybrid system composed of tunable transmon and parity-protected qubit by applying a cross-resonance pulse. First, we provide hardware specifications and pulse parameters to construct a successful two-qubit gate in the hybrid system. Second, we show that our method can supply a CNOT gate of average fidelity with more than 0.998. Therefore, our work implies that the hybrid system may provide a new platform for quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2503.19172v2
- Title: Resource-state Quantum RAM for Fast and Error-Correctable Queries
- Authors: Francesco Cesa, Hannes Bernien, Hannes Pichler
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2503.19172v2  pdf=https://arxiv.org/pdf/2503.19172v2.pdf

Abstract:
Quantum devices can process data in a fundamentally different way than classical computers. To leverage this potential, many algorithms require the aid of a quantum Random Access Memory (QRAM), i.e. a module capable of efficiently loading datasets onto the quantum processor. However, a realisation of this building block is still outstanding due to its formidable resource requirements, which become even more demanding in quantum error-correction schemes. Here we show that the challenge of implementing QRAM can be entirely reduced to a state-preparation problem: since such resource-state is independent on the memory, our approach allows one to prepare it offline, opening the door to new design strategies. As an example, we introduce a heralded 'QRAM factory' which enables improved fidelities with high acceptance rate. More broadly, our results introduce the concept of resource-state QRAM: we study its performance in noisy settings, showing that it preserves the noise-resilience of standard QRAM, and discuss how it can be efficiently combined with quantum error-correction. Finally, we propose an implementation with neutral-atom hardware, where our analysis suggests that high-fidelity and low-latency queries can be implemented.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2505.21203v2
- Title: Quantum Optimal Control Using MAGICARP: Combining Pontryagin's Maximum Principle and Gradient Ascent
- Authors: Denis Janković, Jean-Gabriel Hartmann, Paul-Louis Etienney, Killian Lutz, Yannick Privat, Paul-Antoine Hervieux
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2505.21203v2  pdf=https://arxiv.org/pdf/2505.21203v2.pdf

Abstract:
We introduce the MAGICARP algorithm, a numerical optimization method for quantum optimal control problems that combines the structure provided by Pontryagin's Maximum Principle (PMP) and the robustness of gradient ascent techniques, such as GRAPE. MAGICARP is formulated as a "shooting technique", aiming to determine the appropriate initial adjoint momentum to realize a target quantum gate. This method naturally incorporates time and energy optimal constraints through a PMP-informed pulse structure. We demonstrate MAGICARP's effectiveness through illustrative numerical examples, comparing its performance to GRAPE and highlighting its advantages in specific scenarios.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2509.14445v2
- Title: Coherent Control of Quantum-Dot Spins with Cyclic Optical Transitions
- Authors: Zhe Xian Koong, Urs Haeusler, Jan M. Kaspari, Christian Schimpf, Benyam Dejen, Ahmed M. Hassanen, Daniel Graham, Yusuf Karli, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2509.14445v2  pdf=https://arxiv.org/pdf/2509.14445v2.pdf

Abstract:
Solid-state spins are promising as interfaces from stationary qubits to single photons for quantum communication technologies. Semiconductor quantum dots have excellent optical coherence, exhibit near unity collection efficiencies when coupled to photonic structures, and possess long-lived spins for quantum memory. However, the incompatibility of performing optical spin control and single-shot readout simultaneously has been a challenge faced by almost all solid-state emitters. To overcome this, we leverage light-hole mixing to realize a highly asymmetric lambda system in a negatively charged heavy hole exciton in Faraday configuration. By compensating GHz-scale differential Stark shifts, induced by unequal coupling to Raman control fields, and by performing nuclear-spin cooling, we achieve quantum control of an electron-spin qubit with a $π$-pulse contrast of 97.4% while preserving spin-selective optical transitions with a cyclicity of 471 (50). We demonstrate this scheme for both GaAs and InGaAs quantum dots, and show that it is compatible with the operation of a nuclear quantum memory. Our approach thus enables repeated emission of indistinguishable photons together with qubit control, as required for single-shot readout, photonic cluster-state generation, and quantum repeater technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2509.20962v2
- Title: Distillation of supersinglet states
- Authors: Saeed Ahmad, Shuang Li, Jonathan Raghoonanan, Kaixuan Zhou, Valentin Ivannikov, Tim Byrnes
- Categories: quant-ph (primary); quant-ph; physics.app-ph
- Links: abs=https://arxiv.org/abs/2509.20962v2  pdf=https://arxiv.org/pdf/2509.20962v2.pdf

Abstract:
We introduce an entanglement distillation (purification) protocol for supersinglet states composed of N qubits. The supersinglet state we target is a total spin zero state with zero spin variance, and has a fully entangled structure involving all qubits. In our distillation protocol, three copies of an initial spin zero state are measured in the local total spin basis such that a higher fidelity supersinglet state is generated upon postselection. The initial state can be prepared using conventional Bell state distillation methods distributed in a way to target the supersinglet symmetries. The protocol uses only local operations and classical communications, and is suitable for long-distance applications such as quantum clock synchronization and cryptography, and avoids a high dimensional Schur transform such that it can be used for tasks such as quantum metrology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2510.06659v2
- Title: Layer codes as partially self-correcting quantum memories
- Authors: Shouzhen Gu, Libor Caha, Shin Ho Choe, Zhiyang He, Aleksander Kubica, Eugene Tang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.06659v2  pdf=https://arxiv.org/pdf/2510.06659v2.pdf

Abstract:
We investigate layer codes, a family of three-dimensional stabilizer codes that can achieve optimal scaling of code parameters and a polynomial energy barrier, as candidates for self-correcting quantum memories. First, we introduce two decoding algorithms for layer codes with provable guarantees for local stochastic and adversarial noise, respectively. We then prove that layer codes constitute partially self-correcting quantum memories which outperform previously analyzed models such as the cubic code and the welded solid code. Notably, we argue that partial self-correction without the requirement of efficient decoding is more common than expected, as it arises solely from a diverging energy barrier. This draws a sharp distinction between partially self-correcting systems and partially self-correcting memories. Another novel aspect of our work is an analysis of layer codes constructed from random Calderbank-Shor-Steane codes. We show that these random layer codes have optimal scaling (up to logarithmic corrections) of code parameters and a polynomial energy barrier. Finally, we present numerical studies of their memory times and report behavior consistent with partial self-correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2510.24439v3
- Title: Fundamental limit on the heralded single photons' spectral brightness
- Authors: Tse-Yu Lin, Wei-Kai Huang, Pei-Yu Tu, Yong-Fan Chen, Ite A. Yu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.24439v3  pdf=https://arxiv.org/pdf/2510.24439v3.pdf

Abstract:
Heralded single photons (HSPs) are the versatile flying qubits in quantum communication and networks due to their ability to remove the randomness of arrival time and enhance the transmission reliability. As the generation rate of HSPs increases or their linewidth narrows, both of which are desirable for quantum information processing, the fundamental limit of spectral brightness (SB), defined as the generation rate per unit linewidth, remains unclear. To examine the existence and value of such a limit, we systematically studied the SB together with the cross-correlation function, or equivalently, the signal-to-background ratio (SBR). We ultimately derive an upper bound on SB that applies universally to all types of HSP sources. A newly defined quantity governs this limit, the quality factor, which is the product of SBR and effective SB. The quality factor indicates how closely an HSP source approaches an ideal noise-free source. Furthermore, by employing an HSP source based on hot atomic vapor, we achieved an SB of $(8.5\pm0.3)$$\times$$10^5$ pairs/s/MHz and a quality factor of $0.73\pm0.02$ under the single-photon criterion. Both values represent the highest reported performance to date among all HSP platforms. These results provide a unified benchmark for evaluating and optimizing HSP sources.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2511.10267v3
- Title: Quantum Simulation of Non-Hermitian Special Functions and Dynamics via Contour-based Matrix Decomposition
- Authors: Chao Wang, Huan-Yu Liu, Cheng Xue, Xi-Ning Zhuang, Menghan Dou, Zhao-Yun Chen, Guo-Ping Guo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.10267v3  pdf=https://arxiv.org/pdf/2511.10267v3.pdf

Abstract:
Simulating non-Hermitian dynamics on quantum computers is often hindered by the decay of success probability and the instability of non-diagonalizable matrices. Here, we present contour-based matrix decomposition (CBMD), a rigorous and versatile quantum functional calculus framework for simulating non-Hermitian matrix functions. By generalizing the matrix Cauchy residue theorem, CBMD decomposes holomorphic non-Hermitian operators into an analytic infinite contour-residue identity, followed by finite truncation with controlled error to yield linear combinations of Hermitian components. For first-order dynamics, CBMD achieves optimal query complexity across all parameters, strictly matching the optimal performance bounds within the linear combination of Hamiltonian simulation (LCHS) paradigm. Beyond first-order systems, the framework naturally generalizes to complex operator functions, including second-order wave dynamics and non-Hermitian special functions such as Bessel and Airy evolutions. Furthermore, CBMD systematically suppresses the asymptotic growth of non-Hermitian components, yielding a significant reduction in the required number of amplitude amplifications compared to the naive scheme of combining monomials via linear combination of unitaries (LCU) after Taylor expansion. Notably, CBMD avoids explicit dependence on matrix diagonalizability, effectively mitigating the long-standing challenges associated with ill-conditioned eigenvectors and Jordan blocks. Our work establishes a systematic matrix calculus that bridges high-performance classical numerics and fault-tolerant quantum algorithms. It should be noted that CBMD inherits standard LCU overheads, and requires the target function to have a bounded growth order on the real axis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2511.15124v2
- Title: Beyond Trotterization: Variational Product Formulas for Quantum Simulation
- Authors: Ibsal Assi, Michael Vogl, Meenu Kumari, J. P. F. LeBlanc
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.15124v2  pdf=https://arxiv.org/pdf/2511.15124v2.pdf

Abstract:
We propose a variational alternative to the Trotter-Suzuki decomposition that provides greater control over errors while preserving the unitary structure of time evolution. The variational parameters in our ansatz are derived from a global action principle, where Euler-Lagrange equations govern their optimal dynamics. Unlike conventional wavefunction-based variational methods, our approach specifically targets the time evolution operation and this allows a single set of optimized parameters to be applied to any initial state for a fixed Hamiltonian avoiding costly optimization procedures. Our method outperforms the standard Trotter-Suzuki formulas, typically achieving higher accuracy than higher-order Suzuki schemes. This translates directly to quantum computing applications, where it enables the design of quantum circuits with fewer gates which reduces noise and improves precision. Although we focus on quantum dynamics, the method is broadly applicable to problems involving general time-evolution operators. Applied to various model Hamiltonians, our approach reduces errors by factors of 2 to 5 compared to Trotter-Suzuki decompositions, demonstrating its promise for accurate quantum simulation with improved efficiency. In certain cases, the variational ansatz achieves higher accuracy than more complex higher-order Suzuki formulas while reducing the gate count by nearly half within a single circuit layer. Furthermore, we derive approximate analytical expressions for the variational parameters up to cubic order in time, valid for generic Hamiltonians. These approximations enable long-time quantum simulations with improved accuracy over equivalent Suzuki decompositions, providing ready-to-use evolution formulas that match Suzuki's gate complexity while delivering better performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2512.03853v3
- Title: Modelling the Impact of Device Imperfections on Electron Shuttling in SiMOS devices
- Authors: Jack J. Turner, Christian W. Binder, Guido Burkard, Andrew J. Fisher
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2512.03853v3  pdf=https://arxiv.org/pdf/2512.03853v3.pdf

Abstract:
Extensive theoretical and experimental work has established high-fidelity electron shuttling in Si/SiGe systems, whereas demonstrations in Si/SiO2 (SiMOS) remain at an early stage. To help address this, we perform full 3D simulations of conveyor-belt charge shuttling in a realistic SiMOS device, building on earlier 2D modelling. We solve the Poisson and time-dependent Schrodinger equations for varying shuttling speeds and gate voltages, focusing on potential pitfalls of typical SiMOS devices such as oxide-interface roughness, gate fabrication imperfections, and charge defects along the transport path. The simulations reveal that for low clavier-gate voltages, the additional oxide screening in multi-layer gate architectures causes conveyor-belt shuttling to collapse to the bucket-brigade mode, inducing considerable orbital excitation in the process. Increasing the confinement restores conveyor-belt operation, which we find to be robust against interface roughness, gate misalignment, and charge defects buried in the oxide. However, our results indicate that defects located at the Si/SiO2-interface can induce considerable orbital excitation. For lower conveyor gate biases, positive defects in the transport channel can even capture passing electrons. Hence we identify key challenges and find operating regimes for reliable charge transport in SiMOS architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2512.05037v2
- Title: Expanding the Neutral Atom Gate Set: Native iSWAP and Exchange Gates from Dipolar Rydberg Interactions
- Authors: Pedro Ildefonso, Andrew Byun, Aleksei Konovalov, Javad Kazemi, Michael Schuler, Wolfgang Lechner
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.05037v2  pdf=https://arxiv.org/pdf/2512.05037v2.pdf

Abstract:
We present a native realization of iSWAP and parameterized \textit{exchange} gates for neutral-atom quantum processing units. Our approach leverages strong dipole-dipole interactions between two different dipole-coupled Rydberg states, employing optimal control techniques to design high-fidelity, time-efficient gate pulses. To minimize experimental complexity, we utilize global driving fields acting identically on all atoms and apply pulse smoothing techniques. While detrimental van-der-Waals interactions pose a significant challenge, we demonstrate that for both $^{133}$Cs, as a representative alkali atom, and $^{88}$Sr, an alkaline-earth species, high-fidelity pulses can nevertheless be obtained over a broad range of parameters. We identify candidate protocols with reduced susceptibility to noise and analyze their performance under realistic conditions, accounting for atomic motion, Rydberg decay, and experimentally motivated laser frequency and intensity noise. Crucially, we demonstrate that in both Alkali and alkaline-earth-based systems, we can obtain fast iSWAP gates with fidelities of $99.9\%$ under realistic experimental conditions. These results pave the way for expanding the neutral-atom gate set beyond conventional Rydberg-blockade-based entangling gates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2512.13809v2
- Title: Universal Statistics of Measurement-Induced Entanglement in Tomonaga-Luttinger liquids
- Authors: Kabir Khanna, Romain Vasseur
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; hep-th
- Links: abs=https://arxiv.org/abs/2512.13809v2  pdf=https://arxiv.org/pdf/2512.13809v2.pdf

Abstract:
We study the statistics of measurement-induced entanglement (MIE) after partial measurement on a class of one-dimensional quantum critical states described by Tomonaga-Luttinger liquids at low energies. Using a replica trick to average over measurement outcomes in the charge basis and tools from conformal field theory (CFT), we derive closed-form expressions for the cumulants of MIE. We show that exact Born-averaging over microscopic measurement outcomes becomes equivalent at low energy to averaging over conformal boundary conditions weighted by their corresponding partition functions. Our results yield distinctive critical behavior across all cumulants in the regime where the unmeasured parts of the system are maximally separated. We also obtain the full distribution of MIE, finding that it is generically bimodal and exhibits fat-tails. We corroborate our analytical predictions by numerical calculations and find good agreement between them.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2601.00064v3
- Title: Pauli stabilizer formalism for topological quantum field theories and generalized statistics
- Authors: Yitao Feng, Hanyu Xue, Ryohei Kobayashi, Po-Shen Hsin, Yu-An Chen
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; hep-th; math.QA
- Links: abs=https://arxiv.org/abs/2601.00064v3  pdf=https://arxiv.org/pdf/2601.00064v3.pdf

Abstract:
Topological quantum field theory (TQFT) provides a unifying framework for describing topological phases of matter and for constructing quantum error-correcting codes, playing a central role across high-energy physics, condensed matter, and quantum information. A central challenge is to formulate topological order on lattices and to extract the properties of topological excitations from microscopic Hamiltonians. In this work, we construct new classes of lattice gauge theories as Pauli stabilizer models, realizing a wide range of TQFTs in general dimensions. We develop a lattice description of extended excitations and systematically determine their generalized statistics. Our main example is the (4+1)D fermionic-loop toric code, obtained by condensing the $e^2m^2$-loop in the (4+1)D $\mathbb Z_4$ toric code. We show that the loop excitation exhibits fermionic loop statistics: the 24-step loop-flipping process yields a phase of $-1$. Our Pauli stabilizer models realize all twisted 2-form gauge theories in (4+1)D, the higher-form Dijkgraaf-Witten TQFT classified by $H^5(B^2G,U(1))$. Beyond (4+1)D, the fermionic-loop toric codes form a family of $\mathbb Z_2$ topological orders in arbitrary dimensions, realized as explicit Pauli stabilizer codes using $\mathbb Z_4$ qudits. Finally, we develop a Pauli-based framework that defines generalized statistics for extended excitations in any dimension, yielding computable lattice unitary processes to detect nontrivial statistics. For example, we propose anyonic membrane statistics in (6+1)D, as well as fermionic membrane and volume statistics in arbitrary dimensions. We construct new families of $\mathbb Z_2$ topological orders: the fermionic-membrane toric code and the fermionic-volume toric code. In addition, we demonstrate that $p$-dimensional excitations in $2p+2$ spatial dimensions can support anyonic $p$-brane statistics for only even $p$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2605.14924v4
- Title: Nonlocal Topological Maxwell Demon Teleporting Ergotropy via Surface-Code Quantum Error Correction
- Authors: M. Y. Abd-Rabbou, Cong-Feng Qiao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.14924v4  pdf=https://arxiv.org/pdf/2605.14924v4.pdf

Abstract:
Surface-code quantum error correction has recently achieved logical error rates below the physical threshold on superconducting processors, establishing topologically ordered states as experimentally accessible resources. Whether these resources can support thermodynamic operations beyond fault-tolerant computation remains open. We introduce a nonlocal Maxwell demon protocol that transfers ergotropy between spatially separated quantum batteries using only local operations and classical communication over a shared surface code. Alice expends ergotropy to encode a logical qubit and transmits a classical syndrome record to Bob, who decodes via minimum-weight perfect matching and conditionally charges his battery, with no direct energy exchange across the channel. Active syndrome monitoring exponentially suppresses logical errors below the topological threshold $p_{\rm th} \approx 0.013$, converting physical qubits directly into recoverable ergotropy. For finite-size codes at distance $L = 7$, net extracted work changes sign at a thermodynamic critical error rate $p_c \approx 0.014 > p_{\rm th}$, a physically significant finite-size effect relevant to near-term devices. Causality enforces an irreducible quadratic infrastructure cost $W_{\rm bulk} \propto N^2$, strictly satisfying the second law at all separations and defining a fundamental thermodynamic horizon $N_{\rm max} \approx 78$ beyond which positive net work extraction is impossible regardless of code distance or decoder quality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2605.18494v2
- Title: Quantum magic of strongly correlated fermions $-$ the Hubbard dimer
- Authors: Edoardo Zavatti, Gabriele Bellomia, Massimo Capone
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2605.18494v2  pdf=https://arxiv.org/pdf/2605.18494v2.pdf

Abstract:
We study the non-stabilizerness (quantum magic) content of the Hubbard dimer, an analytically solvable, yet completely non-trivial, model of strongly correlated fermions. We consider zero- and finite-temperature properties as well as the time evolution after a quantum quench drives the system out of equilibrium. We evaluate local and nonlocal non-stabilizerness using both the robustness of magic and the stabilizer Renyi entropy, demonstrating how the latter often fails in detecting the mixed stabilizer states that are typically found in this kind of systems. Finally, we compare the non-stabilizerness with other genuine resources of quantum-state complexity, i.e., the fermionic non-Gaussianity and the superselected two-site entanglement. Our findings corroborate the role of non-stabilizerness as a fundamental quantum resource, capturing aspects of quantum complexity that elude traditional information-theoretic measures and providing a novel perspective on fermionic systems with tunable interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2605.20346v2
- Title: Forced Gap Post-Selection for Quantum LDPC Codes and their Operations
- Authors: Adam Wills, Theodore J. Yoder, Isaac Chuang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.20346v2  pdf=https://arxiv.org/pdf/2605.20346v2.pdf

Abstract:
We develop a simple and general post-selection strategy for high-rate quantum codes that is transferrable across decoders. After an initial baseline run, the decoder is re-run once per logical observable, and forced in these latter runs to provide a solution where the given observable has the complementary outcome. Shots are rejected that find logically complementary solutions with similar likelihoods compared to the baseline. Using the Relay-BP decoder, we benchmark the strategy on the $72$-qubit and $144$-qubit bivariate bicycle codes, as well as surgery gadgets for the latter. In comparison to previous post-selection strategies, our results offer an improved logical error rate by over a factor of $4$ on the same circuit and physical error rate, and at the same rate of post-selection. Our strategies are also lightweight, relying only on FPGA-friendly belief propagation, whereas the previous best used repeated rounds of a high-latency BP-OSD decoder.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2605.24824v3
- Title: Point-group symmetry analysis of many-electron wavefunctions on a quantum computer
- Authors: Rei Sakuma, Kenji Sugisaki, Shu Kanno, Toshinari Itoko, Hajime Nakamura
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.24824v3  pdf=https://arxiv.org/pdf/2605.24824v3.pdf

Abstract:
A point group is a set of spatial symmetry operations in molecular systems and is an indispensable tool for analyzing molecular orbitals and spectroscopy experiments in chemistry. Several quantum algorithms to exploit this symmetry have been proposed, but practical implementations of point-group symmetry operations and the detailed symmetry analysis of realistic many-electron wavefunctions are still missing. In this work, we propose an ancilla-free hybrid method to analyze point-group symmetries of many-electron states, which works for both abelian and non-abelian groups. For a given wavefunction, our method calculates the projection weights of point-group irreducible representations by applying orbital rotations derived from the eigenvectors of the representation matrices, making it applicable to arbitrary basis functions. The usefulness of our approach is demonstrated through numerical simulations of benzene and ferrocene molecules. Furthermore, we perform a hardware demonstration of the weight calculation of the ground state and the first excited state of benzene in $D_{2h}$ symmetry, using up to 32 qubits of IBM's ibm_kawasaki device. By combining a tensor-network based encoding scheme and error mitigation techniques, we find the weights of irreducible representations for both states are faithfully reproduced within a few percent error. Our results suggest that the proposed method serves as a practical tool for analyzing symmetry properties of many-electron wavefunctions in realistic material simulations on near-term and early fault-tolerant quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2605.26096v2
- Title: Rounding Almost Commuting Hamiltonians
- Authors: Islam Faisal, Anand Natarajan, Alexander Poremba
- Categories: quant-ph (primary); quant-ph; cond-mat.other; cs.CC
- Links: abs=https://arxiv.org/abs/2605.26096v2  pdf=https://arxiv.org/pdf/2605.26096v2.pdf

Abstract:
Commuting Hamiltonians lie at the boundary between classical constraint satisfaction and quantum many-body physics, exhibiting rich quantum structure while remaining more tractable than general noncommuting models. In contrast, physical Hamiltonians are rarely exactly commuting, which naturally motivates the study of almost commuting Hamiltonians. Despite their relevance, the implications of approximate commutation are only poorly understood.   In this work, we show how to efficiently approximate any almost commuting $2$-local qubit Hamiltonian by a commuting one: we give a new locality-preserving algorithmic rounding technique that maps any $2$-local Hamiltonian $H=\sum_{i=1}^m h_i$ with $\|[h_i,h_j]\| \leq ε$ to a nearby Hamiltonian $\hat{H}$ whose terms pair-wise commute, and which is within overall distance $\|H-\hat{H}\| = O(m\,ε^{1/6})$. As a consequence, we show that $δ$-approximations to the ground energy for $ε$-almost commuting $2$-local qubit Hamiltonians lie in $\mathsf{NP}$ when $δ\gg mε^{1/6}$, extending the classical containment well beyond the commuting setting. Finally, we present two applications of our rounding framework: Gibbs sampling and fast Hamiltonian simulation for almost commuting systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.00358v2
- Title: Software compensation of trigger-synchronous control-frame errors in qubits and qudits
- Authors: Gaurav A. Tathed, Nicholas C. F. Zutt, Collin J. C. Epstein, Crystal Senko
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.00358v2  pdf=https://arxiv.org/pdf/2606.00358v2.pdf

Abstract:
Quantum control experiments are often subject to coherent, time-dependent disturbances that vary over timescales comparable to the experiment duration. We show that when such disturbances are reproducible with respect to a trigger signal, their effect can be measured and compensated through software-defined updates to the control frequency and phase. We experimentally verify the performance of our protocol using a trapped $^{137}$Ba$^+$ ion experiencing magnetic-field-induced energy shifts synchronous with the laboratory AC mains power. Using this compensation technique, the calibrated AC line contribution to the instantaneous oscillator detuning is reduced by $21(9)\times$, and the fitted AC-induced phase amplitude is reduced below the measurement uncertainty. We use randomized benchmarking to validate the compensation performance in quantum gate sequences, recovering an average single-qubit gate fidelity of 99.93(1)\% with a magnetic-field-sensitive qubit. Finally, we extend the compensation framework to multi-level qudit control. Using the Bernstein-Vazirani algorithm as a benchmark, we increase the algorithm's success probability from 10(7)\% to 70(9)\% in a 16 level system when compensation is enabled. Our results demonstrate that trigger-synchronized coherent errors can be reframed as deterministic control-frame errors and corrected in software.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.02197v2
- Title: Quantum-inspired Topographic Stereovision
- Authors: Fanglin Bao, Youfei Xie, Syed Masood
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.02197v2  pdf=https://arxiv.org/pdf/2606.02197v2.pdf

Abstract:
We revisit the conventional triangulation in distant stereovision, when shape rather than distance is the relevant observable. We show through the information-regret analysis that the optimal measurements for absolute distance and relative topography are unexpectedly different and incompatible, exposing an observable-measurement mismatch. To resolve this, we introduce stereo regularization to address stereo anisotropies that violate prevailing emitter-number conservation. Accordingly, we propose a topographic interferometer, which exploits cross-detector correlations to probe topography without measuring the distance profile. Our Fizeau-imaging interferometer turns parallax paths into Mach-Zehnder arms and employs a central path as the local oscillator for balanced homodyne detection, saturating the quantum Fisher information with improved topographic error scaling. This enables topographic stereovision of thermal sources beyond the Rayleigh limit, with feasible experimental demonstrations within existing techniques for remote sensing and astronomy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.07826v3
- Title: The classical boundaries of the EPR argument and quantum ontology
- Authors: Vincenzo Chilla
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2606.07826v3  pdf=https://arxiv.org/pdf/2606.07826v3.pdf

Abstract:
Von Neumann's Hilbert-space formalism of quantum mechanics constitutes a logico-physical theory of observed or measured reality. Imposing the logical constraint of Booleanity, essential for objectively shareable descriptions among observers, reveals the physical meaning of classicality inherently embedded within the formalism itself. Starting from this consideration, the present work reformulates the quantum-classical transition via Hilbert-space classical mechanics (HCM), grounding classicality not in the dynamical limit ($\hbar \to 0$), but in the logical constraint of Booleanity (i.e., the mutual commutativity of preparable states). Within this state-centric framework, applying the Einstein-Podolsky-Rosen (EPR) criterion alongside locality and measurement independence reduces standard quantum mechanics to the HCM model. Thus, the EPR argument reveals not quantum incompleteness, but the implicit classical boundaries of its own premises. To resolve this impasse, we articulate a nuanced quantum ontology grounded in a fundamental structural bipartition between the observational environment and the observed object, which accommodates three categorical distinctions: ontic, processional, and tropos-existential. Building on this, we propose a criterion of objective reality wherein descriptive objectivity is treated as merely a sufficient condition for physical reality. This addresses the historical Bohr-Einstein ambiguity, enabling the quantum formalism to ontologically unify objective measured phenomena and non-objective observed interference within a context-dependent framework.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.21362v2
- Title: Bell inequalities tailored to optimal global randomness certification
- Authors: Ignacio Perito, Raffaele D'Avino, Michał Jung, Piotr Mironowicz, Antonio Acín, Remigiusz Augusiak
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.21362v2  pdf=https://arxiv.org/pdf/2606.21362v2.pdf

Abstract:
We present two novel families of bipartite Bell inequalities designed to achieve optimal global randomness certification for an arbitrary number of outputs $d$. We first use symmetry arguments to argue that their maximal quantum violations certify $2\log d$ random bits. For the first family, we construct a quantum realization using $d\times d$ maximally entangled states which provides a quantum violation that we conjecture to be optimal for any $d$. It is then numerically shown that the obtained quantum violation certifies optimal global randomness, up to numerical precision, for $d=3,4$. For the second family, we provide the optimal quantum violation and its quantum realization for any $d$, again using $d\times d$ maximally entangled states and projective measurements over at least two unbiased bases on one of the parties. We self-test this realization for $d=3$, which implies the optimal certification of two fully random trits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.21369v2
- Title: Maximal global device-independent randomness from projective measurements in every dimension
- Authors: Máté Farkas, Piotr Mironowicz, Remigiusz Augusiak
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.21369v2  pdf=https://arxiv.org/pdf/2606.21369v2.pdf

Abstract:
Device-independent random number generation (DIQRNG) is the most secure form of generating private randomness using quantum physical processes. Its strength lies in producing numbers that are impossible to predict by any eavesdropper restricted by the laws of quantum theory. Moreover, security is proven solely from observed measurement statistics, without the need to characterise or trust the devices used in random number generation. Implementing DIQRNG is, however, costly, as it requires high-quality entangled systems. It is therefore important to make the best use of available resources. In this work, we show that using projective measurements -- which are most readily implementable experimentally -- one can certify $2\log(d)$ bits of device-independent randomness from a bipartite system of local dimension $d$ for every $d \ge 2$, thus reaching the theoretically maximum possible rate of DIQRNG. We provide explicit protocols reaching $2\log(d)$ bits based on mutually unbiased bases. Furthermore, we compute numerical bounds on the rate for the case of imperfect implementations, showing that our protocols are robust to experimental noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.22080v2
- Title: Optimizing Pump Conditions of Parametric Amplifiers for Fast Multiplexed Readout of Superconducting Qubits
- Authors: Jeongwon Kim, Wei Dai, Omrie Ovdat, Akiva Feintuch, Nir Alfasi, Yonuk Chong
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.22080v2  pdf=https://arxiv.org/pdf/2606.22080v2.pdf

Abstract:
Low-noise parametric amplifiers are widely used as the first-stage amplifier in qubit readout chains. The performance of parametric amplifiers depends sensitively on the choice of the pump condition. We propose a strategy for determining the pump condition that is tailored for fast multiplexed readout. Choosing the amplifier pump to maximize the signal-to-noise ratio (SNR) improvement at the readout frequency of the limiting qubit--the qubit that requires the longest readout time to reach a target SNR--minimizes the total multiplexed readout time. We demonstrate our pump calibration strategy experimentally on a five-qubit multiplexed readout chain with a traveling-wave parametric amplifier. Using our strategy, we reduce the multiplexed readout time by 320 ns compared to optimizing the average SNR improvement on all qubits, without degrading the target SNR for any qubit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2504.15571v2
- Title: High-sensitivity and high-resolution collaborative determination of birefringence coefficient using weak measurement
- Authors: Shuqi Gao, Min Zhang, Jiahui Hou, Qingchen Liu, Hongyu Li, Xiaomin Guo, Yanqiang Guo, Liantuan Xiao
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2504.15571v2  pdf=https://arxiv.org/pdf/2504.15571v2.pdf

Abstract:
Precise nanofilm birefringence characterization is essential for high-sensitivity polarization response and strong anti-interference detection in photodetectors. We present a high-sensitivity and high-resolution birefringence coefficient determination system for nm-level membranes based on weak measurement, addressing the sensitivity-resolution trade-off. A tunable bandwidth light source is exploited to achieve simultaneous and complementary measurements of momentum (P-pointer) and intensity (I-pointer), enabling calibration-free operation across various bandwidths, and to realize high-precision phase difference monitoring of the measured membranes. This method maps the birefringence effect to a weak-value amplified signal of spectral shift and light intensity. The optimal resolution, achieved at a spectral width of 6 nm, is $1.12 \times 10^{-8}$ RIU, while the optimal sensitivity is achieved when the light source is a narrow-linewidth coherent laser, reaching 4710 mV/RIU. The linear range of the system covers a broad birefringence coefficient range for crystals, from $10^{-6}$ to 0.1. Furthermore, the auxiliary optical path eliminates substrate interference, achieving a detection limit of birefringence coefficient as low as $10^{-8}$ RIU. This approach, characterized by high precision, high sensitivity, and strong robustness, provides an effective solution for the detection of optical nano-thin membrane parameters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2511.03253v2
- Title: Quantum Error Correction-like Noise Mitigation for Wave-like Dark Matter Searches with Quantum Sensors
- Authors: Hajime Fukuda, Takeo Moroi, Thanaporn Sichanugrist
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2511.03253v2  pdf=https://arxiv.org/pdf/2511.03253v2.pdf

Abstract:
We propose a quantum error correction-like noise mitigation protocol for enhancing the sensitivity of wave-like dark matter searches with quantum sensors. Our protocol uses multiple sensors to mitigate the noise affecting each sensor individually, allowing for the suppression of excitation noise that is parallel to the dark matter signal. We demonstrate that our protocol can improve the sensitivity to dark matter signals by a factor of $\sqrt{N}$, where $N$ is the number of sensors used, for small $N$. Furthermore, for sufficiently large $N$, we find that our protocol achieves the same performance as the standard quantum limit by the ideal measurement, which non-entangled sensors with parallel noise cannot reach due to the unknown phase of the dark matter field. Our work can be widely applied to various types of signals with unknown phases, and has the potential to enhance the sensitivity of quantum sensors such as arrays of resonant cavities.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-06-26 10:26
- arXiv: 2606.11296v3
- Title: Tripartite Entanglement in $e^+ e^- \to t \bar{t} Z$
- Authors: Dorival Gonçalves, Alberto Navarro, Kazuki Sakurai
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2606.11296v3  pdf=https://arxiv.org/pdf/2606.11296v3.pdf

Abstract:
Multipartite entanglement is a uniquely quantum form of correlation that captures collective properties of a composite quantum state beyond those encoded in its bipartite subsystems. We investigate this phenomenon in the process $e^+e^-\to t\bar tZ$ at a future lepton collider, where the final state spins span the tripartite Hilbert space $\mathscr{H} = \mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^3$. Starting from the Standard Model helicity amplitudes, we reconstruct the full $12\times 12$ spin density matrix and characterise its entanglement structure through one-to-one negativities, one-to-other negativities, and the genuine multipartite negativity, evaluated at three increasingly inclusive levels of phase space integration. Pairwise entanglement is generally suppressed relative to the collective (one-to-other) and the genuine multipartite entanglement, and all measures decrease as more kinematic information is integrated out. Assuming quantum tomography in the fully leptonic decay channel at $\sqrt{s}=1$ TeV, we find that collective entanglement should be accessible at a realistic high-luminosity polarised lepton collider. By contrast, certifying genuine multipartite entanglement is more challenging, with only limited sensitivity projected for a specific polarisation benchmark within the expected ILC luminosity. The study establishes $e^+e^-\to t \bar{t}Z$ as an attractive laboratory for probing multipartite entanglement in high-energy collisions and provides a general mixed state framework that applies to any tripartite spin system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

