- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16244v1
- Title: LiDMaS: Architecture-Level Modeling of Fault-Tolerant Magic-State Injection in GKP Photonic Qubits
- Authors: Dennis Delali Kwesi Wayo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16244v1  pdf=https://arxiv.org/pdf/2601.16244v1.pdf

Abstract:
Fault-tolerant quantum computation in photonic architectures relies on the efficient preparation of high-fidelity logical magic states under realistic constraints imposed by finite squeezing and photon loss. In this work, we study logical T-gate magic-state preparation in GKP-encoded photonic qubits using a repeat-until-success injection protocol combined with outer surface-code protection. We develop an architecture-level modeling framework based on a lightweight density-matrix simulator implemented with standard numerical linear algebra. Finite squeezing is mapped to effective logical dephasing, depolarizing noise is included at the logical level, and photon loss is treated as a heralded erasure process. This approach avoids explicit continuous-variable wavefunction simulation, hardware-specific photonic models, and quantum software frameworks, enabling transparent and computationally efficient exploration of architectural trade-offs. We perform systematic parameter sweeps over squeezing values from 8 to 16 dB, baseline loss probabilities between 0.01 and 0.03, and surface-code distances d = 1, 3, 5, and 7. Across this regime, we evaluate repeat-until-success probability, average injection overhead, and logical magic-state fidelity. We find that success probabilities exceed 0.94 across all studied parameters, with an average overhead close to unity. After outer-code protection, logical fidelities reach approximately 0.77 to 0.80 and show weak sensitivity to moderate photon loss but a strong dependence on squeezing. Phase-boundary analysis identifies minimum squeezing requirements needed to simultaneously achieve high success probability and logical fidelity. These results provide quantitative design guidance for scalable photonic fault-tolerant quantum architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16257v1
- Title: Quantum Cellular Automata on a Dual-Species Rydberg Processor
- Authors: Ryan White, Vikram Ramesh, Alexander Impertro, Shraddha Anand, Francesco Cesa, Giuliano Giudici, Thomas Iadecola, Hannes Pichler, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2601.16257v1  pdf=https://arxiv.org/pdf/2601.16257v1.pdf

Abstract:
As quantum devices scale to larger and larger sizes, a significant challenge emerges in scaling their coherent controls accordingly. Quantum cellular automata (QCAs) constitute a promising framework that bypasses this control problem: universal dynamics can be achieved using only a static qubit array and global control operations. We realize QCAs on a dual-species Rydberg array of rubidium and cesium atoms, leveraging independent global control of each species to perform a myriad of quantum protocols. With simple pulse sequences, we explore many-body dynamics and generate a variety of entangled states, including GHZ states, 96.7(1.7)%-fidelity Bell states, 17-qubit cluster states, and high-connectivity graph states. The versatility and scalability of QCAs offers compelling routes for scaling quantum information systems with global controls, as well as new perspectives on quantum many-body dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16258v1
- Title: Multi-invariants in stabilizer states
- Authors: Sriram Akella, Abhijit Gadde, Jay Pandey
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2601.16258v1  pdf=https://arxiv.org/pdf/2601.16258v1.pdf

Abstract:
Multipartite entanglement is a natural generalization of bipartite entanglement, but is relatively poorly understood. In this paper, we develop tools to calculate a class of multipartite entanglement measures - known as multi-invariants - for stabilizer states. We give an efficient numerical algorithm that computes multi-invariants for stabilizer states. For tripartite stabilizer states, we also obtain an explicit formula for any multi-invariant using the GHZ-extraction theorem. We then present a counting argument that calculates any Coxeter multi-invariant of a q-partite stabilizer state. We conjecture a closed form expression for the same. We uncover hints of an interesting connection between multi-invariants, stabilizer states and topology. We show how our formulas are further simplified for a restricted class of stabilizer states that appear as ground states of interesting models like the toric code and the X-cube model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16264v1
- Title: Quantum algorithm for simulating non-adiabatic dynamics at metallic surfaces
- Authors: Robert A. Lang, Paarth Jain, Juan Miguel Arrazola, Danial Motlagh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16264v1  pdf=https://arxiv.org/pdf/2601.16264v1.pdf

Abstract:
Non-adiabatic dynamics at molecule-metal interfaces govern diverse and technologically important phenomena, from heterogeneous catalysis to dye-sensitized solar energy conversion and charge transport across molecular junctions. Realistic modeling of such dynamics necessitates taking into account various charge and energy transfer channels involving the coupling of nuclear motion with a very large number of electronic states, leading to prohibitive cost using classical computational methods. In this work we introduce a generalization of the Anderson-Newns Hamiltonian and develop a highly optimized quantum algorithm for simulating the non-adiabatic dynamics of realistic molecule-metal interfaces. Using the PennyLane software platform, we perform resource estimations of our algorithm, showing its remarkably low implementation cost for model systems representative of various scientifically and industrially relevant molecule-metal systems. Specifically, we find that time evolution for models including $100$ metal orbitals, $8$ molecular orbitals, and $20$ nuclear degrees of freedom, requires only $271$ qubits and $7.9 \times 10^7$ Toffoli gates for $1000$ Trotter steps, suggesting non-adiabatic molecule-metal dynamics as a fruitful application of first-generation fault-tolerant quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16266v1
- Title: Post-processing optimization and optimal bounds for non-adaptive shadow tomography
- Authors: Andrea Caprotti, Joshua Morris, Borivoje Dakić
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16266v1  pdf=https://arxiv.org/pdf/2601.16266v1.pdf

Abstract:
Informationally overcomplete POVMs are known to outperform minimally complete measurements in many tomography and estimation tasks, and they also leave a purely classical freedom in shadow tomography: the same observable admits infinitely many unbiased linear reconstructions from identical measurement data. We formulate the choice of reconstruction coefficients as a convex minimax problem and give an algorithm with guaranteed convergence that returns the tightest state-independent variance bound achievable by post-processing for a fixed POVM and observable. Numerical examples show that the resulting estimators can dramatically reduce sampling complexity relative to standard (canonical) reconstructions, and can even improve the qualitative scaling with system size for structured noncommuting targets.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16269v1
- Title: Engineering Near-Infrared Two-Level Systems in Confined Alkali Vapors
- Authors: Gilad Orr, Golan Ben-Ari, Eliran Talker
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2601.16269v1  pdf=https://arxiv.org/pdf/2601.16269v1.pdf

Abstract:
We combined experimental and theoretical investigations of an effective two-level atomic system operating in the near-infrared telecom wavelength regime, realized using hot rubidium vapor confined within a sub-micron-thick cell. In this strongly confined geometry, atomic coherence is profoundly influenced by wall-induced relaxation arising from frequent atom-surface collisions. By analyzing both absorption and fluorescence spectra, we demonstrate that the optical response is dominated by a closed cycling transition, which effectively isolates the atomic dynamics to a two-level configuration despite the presence of multiple hyperfine states. This confinement-induced selection suppresses optical pumping into uncoupled states and enables robust, controllable light-matter interaction at telecom wavelengths within a miniature atomic platform. Our results establish a practical route to realizing near-infrared atomic two-level systems in compact vapor-cell devices, opening new opportunities for integrated quantum photonic technologies, including on-chip quantum memories, telecom-band frequency references, and scalable quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16275v1
- Title: Experimental observation of conformal field theory spectra
- Authors: Xiangkai Sun, Yuan Le, Stephen Naus, Richard Bing-Shiun Tsai, Lewis R. B. Picard, Sara Murciano, Michael Knap, Jason Alicea, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2601.16275v1  pdf=https://arxiv.org/pdf/2601.16275v1.pdf

Abstract:
Conformal field theories (CFTs) feature prominently in high-energy physics, statistical mechanics, and condensed matter. For example, CFTs govern emergent universal properties of systems tuned to quantum phase transitions, including their entanglement, correlations, and low-energy excitation spectra. Much of the rich structure predicted by CFTs nevertheless remains unobserved in experiment. Here we directly observe the energy excitation spectra of emergent CFTs at quantum phase transitions -- recovering universal energy ratios characteristic of the underlying field theories. Specifically, we develop and implement a modulation technique to resolve a Rydberg chain's finite-size spectra, variably tuned to quantum phase transitions described by either Ising or tricritical Ising CFTs. We also employ local control to distinguish parities of excitations under reflection and, in the tricritical Ising chain, to induce transitions between distinct CFT spectra associated with changing boundary conditions. By utilizing a variant of the modulation technique, we furthermore study the dynamical structure factor of the critical system, which is closely related to the correlation of an underlying Ising conformal field. Our work not only probes the emergence of CFT features in a quantum simulator, but also provides a technique for diagnosing a priori unknown universality classes in future experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16317v1
- Title: Exploring Noisy Quantum Thermodynamical Processes via the Depolarizing-Channel Approximation
- Authors: Jian Li, Xiaoyang Wang, Marcus Huber, Nicolai Friis, Pharnam Bakhshinezhad
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16317v1  pdf=https://arxiv.org/pdf/2601.16317v1.pdf

Abstract:
Noise and errors are unavoidable in any realistic quantum process, including processes designed to reduce noise and errors in the first place. In particular, quantum thermodynamical protocols for cooling can be significantly affected, potentially altering both their performance and efficiency. Analytically characterizing the impact of such errors becomes increasingly challenging as the system size grows, particularly in deep quantum circuits where noise can accumulate in complex ways. To address this, we introduce a general framework for approximating the cumulative effect of gate-dependent noise using a global depolarizing channel. We specify the regime in which this approximation provides a reliable description of the noisy dynamics. Applying our framework to the thermodynamical two-sort algorithmic cooling (TSAC) protocol, we analytically derive its asymptotic cooling limit in the presence of noise. Using the cooling limit, the optimal cooling performance is achieved by a finite number of qubits--distinguished from the conventional noiseless TSAC protocol by an infinite number of qubits--and fundamental bounds on the achievable ground-state population are derived. This approach opens new avenues for exploring noisy quantum thermodynamical processes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16343v1
- Title: Unambiguous randomness from a quantum state
- Authors: Fionnuala Curran
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16343v1  pdf=https://arxiv.org/pdf/2601.16343v1.pdf

Abstract:
Intrinsic randomness is generated when a quantum state is measured in any basis in which it is not diagonal. In an adversarial scenario, we quantify this randomness by the probability that a correlated eavesdropper could correctly guess the measurement outcomes. What if the eavesdropper is never wrong, but can sometimes return an inconclusive outcome? Inspired by analogous concepts in quantum state discrimination, we introduce the unambiguous randomness of a quantum state and measurement, and, relaxing the assumption of perfect accuracy, randomness with a fixed rate of inconclusive outcomes. We solve these problems for any state and projective measurement in dimension two, as well as for an isotropically noisy state measured in an unbiased basis of any dimension. In the latter case, we find that, given a fixed amount of total noise, an eavesdropper correlated only to the noisy state is always outperformed by an eavesdropper with joint correlations to both a noisy state and a noisy measurement. In fact, we identify a critical error parameter beyond which the joint eavesdropper achieves perfect guessing probability, ruling out any possibility of private randomness.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16369v1
- Title: Reducing TLS loss in tantalum CPW resonators using titanium sacrificial layers
- Authors: Zachary Degnan, Chun-Ching Chiu, Yi-Hsun Chen, David Sommers, Leonid Abdurakhimov, Lihuang Zhu, Arkady Fedorov, Peter Jacobson
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2601.16369v1  pdf=https://arxiv.org/pdf/2601.16369v1.pdf

Abstract:
We demonstrate a substantial reduction in two-level system loss in tantalum coplanar waveguide resonators fabricated on high-resistivity silicon substrates through the use of an ultrathin titanium sacrificial layer. A 0.2nm titanium film, deposited atop pre-sputtered α-tantalum, acts as a solid-state oxygen getter that chemically modifies the native Ta oxide at the metal-air interface. After device fabrication, the titanium layer is removed using buffered oxide etchant, leaving behind a chemically reduced Ta oxide surface. Subsequent high-vacuum annealing further suppresses two-level system loss. Resonators treated with this process exhibit internal quality factors Qi exceeding an average of 1.5 million in the single-photon regime across ten devices, over three times higher than otherwise identical devices lacking the titanium layer. These results highlight the critical role of interfacial oxide chemistry in superconducting loss and reinforce atomic-scale surface engineering as an effective approach to improving coherence in tantalum-based quantum circuits. The method is compatible with existing fabrication workflows applicable to tantalum films, offering a practical route to further extending T1 lifetimes in superconducting qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16396v1
- Title: Subspace-Confined QAOA with Generalized Dicke States for Multi-Channel Allocation in 5G CBRS Networks
- Authors: Gunsik Min, Youngjin Seo, Jun Heo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16396v1  pdf=https://arxiv.org/pdf/2601.16396v1.pdf

Abstract:
Efficient spectrum sharing in the Citizens Broadband Radio Service (CBRS) band is essential for maximizing 5G network capacity, particularly when high-traffic base stations require simultaneous access to multiple channels. Standard formulations of the Quantum Approximate Optimization Algorithm (QAOA) impose such multi-channel constraints using penalty terms, so most of the explored Hilbert space corresponds to invalid assignments. We propose a subspace-confined QAOA tailored to CBRS multi-channel allocation, in which each node-wise channel register is initialized in a Generalized Dicke state and evolved under an intra-register XY mixer. This ansatz confines the dynamics to a tensor product of Johnson graphs that exactly encode per-node Hamming-weight constraints. For an 8-node CBRS interference graph with 24 qubits, the effective search space is reduced from the full Hilbert space of size $2^{24}$ to 2916 feasible configurations. Within this subspace, the algorithm converges rapidly to low-conflict assignments without large penalty coefficients. Simulations on instances with up to eight nodes show that the proposed ansatz achieves near-optimal conflict levels and consistently outperforms standard penalty-based QAOA and a greedy classical heuristic in terms of feasibility. Noise simulations with depolarizing channels further indicate that the constraint-preserving structure maintains a high feasibility ratio in NISQ-relevant error regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16416v1
- Title: Low-Loss, High-Coherence Airbridge Interconnects Fabricated by Single-Step Lithography
- Authors: Jibang Fu, Bo Ren, Jiandong Ouyang, Cong Li, Kechengqi Zhu, Yonggang Che, Xiang Fu, Shichuan Xue, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16416v1  pdf=https://arxiv.org/pdf/2601.16416v1.pdf

Abstract:
Airbridges are essential for creating high-performance, low-parasitic interconnects in integrated circuits and quantum devices. Conventional multi-step fabrication methods hinder miniaturization and introduce process-related defects. We report a simplified process for fabricating nanoscale airbridges using only a single electron-beam lithography step. By optimizing a multilayer resist stack with a triple-exposure-dose scheme and a thermal reflow step, we achieve smooth, suspended metallic bridges with sub-200-nm features that exhibit robust mechanical stability. Fabricated within a gradiometric SQUID design for superconducting transmon qubits, these airbridges introduce no measurable additional loss in the relaxation time $T_1$, while enabling a 2.5-fold enhancement of the dephasing time $T_2^*$. This efficient method offers a practical route toward integrating high-performance three-dimensional interconnects in advanced quantum and nano-electronic devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16435v1
- Title: Circulant quantum channels and its applications
- Authors: Bing Xie, Lin Zhang
- Categories: quant-ph (primary); quant-ph; math.FA; math.OA
- Links: abs=https://arxiv.org/abs/2601.16435v1  pdf=https://arxiv.org/pdf/2601.16435v1.pdf

Abstract:
This note introduces a family of circulant quantum channels -- a subclass of the mixed-permutation channels -- and investigates its key structural and operational properties. We show that the image of the circulant quantum channel is precisely the set of circulant matrices. This characterization facilitates the analysis of arbitrary $n$-th order Bargmann invariants. Furthermore, we prove that the channel is entanglement-breaking, implying a substantially reduced resource cost for erasing quantum correlations compared to a general mixed-permutation channel. Applications of this channel are also discussed, including the derivation of tighter lower bounds for $\ell_p$-norm coherence and a characterization of its action in bipartite systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16454v1
- Title: Gluing Randomness via Entanglement: Tight Bound from Second Rényi Entropy
- Authors: Wonjun Lee, Hyukjoon Kwon, Gil Young Cho
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2601.16454v1  pdf=https://arxiv.org/pdf/2601.16454v1.pdf

Abstract:
The efficient generation of random quantum states is a long-standing challenge, motivated by their diverse applications in quantum information processing tasks. In this work, we identify entanglement as the key resource that enables local random unitaries to generate global random states by effectively gluing randomness across the system. Specifically, we demonstrate that approximate random states can be produced from an entangled state $|ψ\rangle$ through the application of local random unitaries. We show that the resulting ensemble forms an approximate state design with an error saturating as $Θ(e^{-\mathcal{N}_2(ψ)})$, where $\mathcal{N}_2(ψ)$ is the second Rényi entanglement entropy of $|ψ\rangle$. Furthermore, we prove that this tight bound also applies to the second Rényi entropy of coherence when the ensemble is constructed using coherence-free operations. These results imply that, when restricted to resource-free gates, the quality of the generated random states is determined entirely by the resource content of the initial state. Notably, we find that among all $α$-Rényi entropeis, the second Rényi entropy yields the tightest bounds. Consequently, these second Rényi entropies can be interpreted as the maximal capacities for generating randomness using resource-free operations. Finally, moving beyond approximate state designs, we utilize this entanglement-assisted gluing mechanism to present a novel method for generating pseudorandom states in multipartite systems from a locally entangled state via pseudorandom unitaries in each of parties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16474v1
- Title: Quantum phase estimation with optimal confidence interval using three control qubits
- Authors: Kaur Kristjuhan, Dominic W. Berry
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16474v1  pdf=https://arxiv.org/pdf/2601.16474v1.pdf

Abstract:
Quantum phase estimation is an important routine in many quantum algorithms, particularly for estimating the ground state energy in quantum chemistry simulations. This estimation involves applying powers of a unitary to the ground state, controlled by an auxiliary state prepared on a control register. In many applications the goal is to provide a confidence interval for the phase estimate, and optimal performance is provided by a discrete prolate spheroidal sequence. We show how to prepare the corresponding state in a far more efficient way than prior work. We find that a matrix product state representation with a bond dimension of 4 is sufficient to give a highly accurate approximation for all dimensions tested, up to $2^{24}$. This matrix product state can be efficiently prepared using a sequence of simple three-qubit operations. When the dimension is a power of 2, the phase estimation can be performed with only three qubits for the control register, making it suitable for early-generation fault-tolerant quantum computers with a limited number of logical qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16494v1
- Title: Indefinite Causal Order from Failure-to-Glue: Contextual Semantics and Parametric Time
- Authors: Partha Ghose
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16494v1  pdf=https://arxiv.org/pdf/2601.16494v1.pdf

Abstract:
Indefinite causal order (ICO) has been studied via higher-order quantum processes (e.g.\ the quantum switch), process matrices, and quantum-gravity proposals involving superposed causal structure, yet the meaning of ``indefiniteness'' and its relation to definite-order explanations often remain opaque.   Part~I develops a category-theoretic formulation of definite-order explainability as a gluing problem: each definite causal ordering (a partial order/DAG type) is treated as a context, and causal separability amounts to a consistent global section (possibly after convex mixing), whereas causal nonseparability is a failure-to-glue. We also introduce a compact seven-valued contextual classifier -- an intuitionistic elaboration -- that separates variation across contexts from genuine indeterminacy.   Part~II applies this framework to a quantum-gravity motivated setting where the fundamental time is a parametric ordering variable $τ$, distinct from geometric (spacetime) time. Adopting a stochastic-quantization perspective on spin-network dynamics (Hilbert space not assumed fundamental) and reading the Wheeler--DeWitt condition as an equilibrium/stationarity constraint, we interpret ICO as indeterminacy of the parametric order of coarse-grained relational interventions, even when the microscopic update process is globally ordered by $τ$. Together, the two parts provide a common language for comparing ICO criteria and for stating precisely what ``no hidden definite order'' means.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16517v1
- Title: The optimal strategy of two-photon interferometric sensing in diverse noise environments
- Authors: Teng-fei Yan, Zhuo-zhuo Wang, Qi-qi Li, Peng-long Wang, Bai-hong Li, Rui-Bo Jin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16517v1  pdf=https://arxiv.org/pdf/2601.16517v1.pdf

Abstract:
Quantum sensing based on two-photon interferometry manifests quantum superiority beyond the classical precision limit. However, this superiority is usually diminished inevitably by the noise. Here, we analyze the sensitivity of two typical two-photon interferometries to the noise, that is, Hong-Ou-Mandel (HOM) and N00N state interferometry. It is found that HOM (N00N state) interference, which depends on the biphoton frequency difference (sum), is insensitive (sensitive) to the phase noise in both the manners of spectrally non-resolved and resolved detections in practice, suggesting their potential applications of sensing for different noise scenarios. Furthermore, spectrally resolved detection outperforms spectrally non-resolved one for the two interferometries, especially for the scope that exceeds the coherence time of biphotons. The findings provide an optimal strategy for the practical applications of two-photon interferometric sensing in diverse noise environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16537v1
- Title: Drive-Through Quantum Gate: Non-Stop Entangling a Mobile Ion Qubit with a Stationary One
- Authors: Ting Hsu, Wen-Han Png, Kuan-Ting Lin, Ming-Shien Chang, Guin-Dar Lin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16537v1  pdf=https://arxiv.org/pdf/2601.16537v1.pdf

Abstract:
Towards the scalable realization of a quantum computer, a quantum charge-coupled device (QCCD) based on ion shuttling has been considered a promising approach. However, the processes of detaching an ion from an array, reintegrating it, and driving non-uniform motion introduce severe heating, requiring significant time and laser power for re-cooling and stabilization. To mitigate these challenges, we propose a novel entangling scheme between a stationary ion qubit and a continuously transported mobile ion, which remains in uniform motion and minimizes motional heating. We theoretically demonstrate a gate error on the order of 0.01%, within reach of current technology. This approach enables resource-efficient quantum operations and facilitates long-distance entanglement distribution, where stationary trapped-ion arrays serve as memory units and mobile ions act as communication qubits passing beside them. Our results pave the way for an alternative trapped-ion architecture beyond the QCCD paradigm.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16545v1
- Title: Quantum graph resonances by cut-off technique
- Authors: Pavel Exner, Jiří Lipovský, Jan Pekař
- Categories: quant-ph (primary); quant-ph; math-ph; math.SP
- Links: abs=https://arxiv.org/abs/2601.16545v1  pdf=https://arxiv.org/pdf/2601.16545v1.pdf

Abstract:
We demonstrate how resonances in a quantum graph consisting of a compact core and semi-infinite leads can be identified from the eigenvalue behavior of the cut-off system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16570v1
- Title: Certification of quantum properties with imperfect measurements
- Authors: Leonardo Zambrano, Teodor Parella-Dilmé, Antonio Acín, Donato Farina
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16570v1  pdf=https://arxiv.org/pdf/2601.16570v1.pdf

Abstract:
The accurate characterization of quantum systems is essential for the advancement of quantum technologies. In particular, certifying convex functions of quantum states plays a central role in many applications. We present a certification method for experimentally prepared quantum states that accounts for both shot noise and measurement imperfections in the data-acquisition stage. Building upon previous work, our method extends confidence regions to accommodate imperfect control over measurements. The values of the functions can then be bounded using convex optimization techniques. We provide explicit prescriptions for quantifying the noise contribution from finite statistics and for estimating the effect of measurement imperfections. By jointly incorporating statistical and systematic errors, the method yields a robust certification framework for quantum experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16665v1
- Title: Efficient quantum machine learning with inverse-probability algebraic corrections
- Authors: Jaemin Seo
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2601.16665v1  pdf=https://arxiv.org/pdf/2601.16665v1.pdf

Abstract:
Quantum neural networks (QNNs) provide expressive probabilistic models by leveraging quantum superposition and entanglement, yet their practical training remains challenging due to highly oscillatory loss landscapes and noise inherent to near-term quantum devices. Existing training approaches largely rely on gradient-based procedural optimization, which often suffers from slow convergence, sensitivity to hyperparameters, and instability near sharp minima. In this work, we propose an alternative inverse-probability algebraic learning framework for QNNs. Instead of updating parameters through incremental gradient descent, our method treats learning as a local inverse problem in probability space, directly mapping discrepancies between predicted and target Born-rule probabilities to parameter corrections via a pseudo-inverse of the Jacobian. This algebraic update is covariant, does not require learning-rate tuning, and enables rapid movement toward the vicinity of a loss minimum in a single step. We systematically compare the proposed method with gradient descent and Adam optimization in both regression and classification tasks using a teacher-student QNN benchmark. Our results show that algebraic learning converges significantly faster, escapes loss plateaus, and achieves lower final errors. Under finite-shot sampling, the method exhibits near-optimal error scaling, while remaining robust against intrinsic hardware noise such as dephasing. These findings suggest that inverse-probability algebraic learning offers a principled and practical alternative to procedural optimization for QNN training, particularly in resource-constrained near-term quantum devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16671v1
- Title: Charging of a Quantum Battery by a Single-Photon Quantum Pulse
- Authors: Elnaz Darsheshdar, Seyed Mostafa Moniri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16671v1  pdf=https://arxiv.org/pdf/2601.16671v1.pdf

Abstract:
We study a minimal model for charging a quantum battery consisting of a two-level system (TLS) acting as a charger, coupled to a harmonic oscillator that serves as the quantum battery. A single-photon quantum pulse of light excites the TLS, which subsequently transfers its excitation to the isolated battery. The TLS may also decay into the electromagnetic environment. We obtain analytical solutions for the dynamics of the battery and determine the optimal pulse shape that maximizes the stored energy. The optimal pulse saturates a universal bound for the stored energy, determined by the TLS decay rates into the pulse and the environment. Furthermore, we derive the minimum charging time and establish a quantum speed limit at the exceptional point, where a critical transition occurs in the system's dynamics. We also present analytical expressions for the charging power and investigate the pulse duration that maximizes it.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16679v1
- Title: Classical Regularization in Variational Quantum Eigensolvers
- Authors: Yury Chernyak, Ijaz Ahamed Mohammad, Martin Plesch
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16679v1  pdf=https://arxiv.org/pdf/2601.16679v1.pdf

Abstract:
While quantum computers are a very promising tool for the far future, in their current state of the art they remain limited both in size and quality. This has given rise to hybrid quantum-classical algorithms, where the quantum device performs only a small but vital part of the overall computation. Among these, variational quantum algorithms (VQAs), which combine a classical optimization procedure with quantum evaluation of a cost function, have emerged as particularly promising. However, barren plateaus and ill-conditioned optimization landscapes remain among the primary obstacles faced by VQAs, often leading to unstable convergence and high sensitivity to initialization. Motivated by this challenge, we investigate whether a purely classical remedy, standard L2 squared-norm regularization, can systematically stabilize hybrid quantum-classical optimization. Specifically, we augment the Variational Quantum Eigensolver (VQE) objective with a quadratic penalty proportional to the squared norm of the parameters, without modifying the quantum circuit or measurement process. Across all tested Hamiltonians, H2, LiH, and the Random Field Ising Model (RFIM), we observe improved performance over a broad window of the regularization strength. Our large-scale numerical results demonstrate that classical regularization provides a robust, system-independent mechanism for mitigating VQE instability, enhancing the reliability and reproducibility of variational quantum optimization without altering the underlying quantum circuit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16697v1
- Title: Sparsity-dependent Complexity Lower Bound of Quantum Linear System Solvers
- Authors: Hitomi Mori, Yuta Kikuchi, Marcello Benedetti, Matthias Rosenkranz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16697v1  pdf=https://arxiv.org/pdf/2601.16697v1.pdf

Abstract:
Quantum linear system (QLS) solvers are a fundamental class of quantum algorithms used in many potential quantum computing applications, including machine learning and solving differential equations. The performance of quantum algorithms is often measured by their query complexity, which quantifies the number of oracle calls required to access the input. The main parameters determining the complexity of QLS solvers are the condition number $κ$ and sparsity $s$ of the linear system, and the target error $ε$. To date, the best known query-complexity lower bound is $Ω(κ\log(1/ε))$, which establishes the optimality of the most recent QLS solvers. The original proof of this lower bound is attributed to Harrow and Kothari, but their result is unpublished. Furthermore, when discussing a more general lower bound including the sparsity $s$ of the linear system, it has become folklore that it should read as $Ω( κ\sqrt{s}\log(1/ε))$. In this work, we establish the rigorous lower bound capturing the sparsity dependence of QLS. We prove the lower bound of $Ω(κ\sqrt{s})$ for any quantum algorithm that solves QLS with constant error. While the dependence on all parameters $κ,s,ε$ remains an open problem, our result provides a crucial stepping stone toward the complete characterization of QLS complexity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16698v1
- Title: Entanglement harvesting in the presence of cavities
- Authors: Jannik Ströhle, Nikolija Momcilovic
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16698v1  pdf=https://arxiv.org/pdf/2601.16698v1.pdf

Abstract:
So far, entanglement harvesting has been extensively studied in free space setups. Here, we provide a detailed analytical and numerical analysis of entanglement harvesting in cavities. Specifically, we adiabatically couple the quantized electromagnetic field to two identical Gaussian detectors located on the symmetry axis of a cylindrical cavity. Our numerical investigations reveal a strong dependence on the cavity length, while showing invariance under changes in the cavity radius in regimes of maximal entanglement. Moreover, we identify different scalings of the detector system parameters for entanglement inside and outside the light cone. Finally, we uncover a strong dependence of the harvested correlations on the cavity induced parity of the electromagnetic field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16734v1
- Title: SeeMPS: A Python-based Matrix Product State and Tensor Train Library
- Authors: Paula García-Molina, Juan José Rodríguez-Aldavero, Jorge Gidi, Juan José García-Ripoll
- Categories: quant-ph (primary); quant-ph; math.NA
- Links: abs=https://arxiv.org/abs/2601.16734v1  pdf=https://arxiv.org/pdf/2601.16734v1.pdf

Abstract:
We introduce SeeMPS, a Python library dedicated to implementing tensor network algorithms based on the well-known Matrix Product States (MPS) and Quantized Tensor Train (QTT) formalisms. SeeMPS is implemented as a complete finite precision linear algebra package where exponentially large vector spaces are compressed using the MPS/TT formalism. It enables both low-level operations, such as vector addition, linear transformations, and Hadamard products, as well as high-level algorithms, including the approximation of linear equations, eigenvalue computations, and exponentially efficient Fourier transforms. This library can be used for traditional quantum many-body physics applications and also for quantum-inspired numerical analysis problems, such as solving PDEs, interpolating and integrating multidimensional functions, sampling multivariate probability distributions, etc.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16758v1
- Title: Noise Resilience and Robust Convergence Guarantees for the Variational Quantum Eigensolver
- Authors: Mirko Legnini, Julian Berberich
- Categories: quant-ph (primary); quant-ph; eess.SY; math.OC
- Links: abs=https://arxiv.org/abs/2601.16758v1  pdf=https://arxiv.org/pdf/2601.16758v1.pdf

Abstract:
Variational Quantum Algorithms (VQAs) are a class of hybrid quantum-classical algorithms that leverage on classical optimization tools to find the optimal parameters for a parameterized quantum circuit. One relevant application of VQAs is the Variational Quantum Eigensolver (VQE), which aims at steering the output of the quantum circuit to the ground state of a certain Hamiltonian. Recent works have provided global convergence guarantees for VQEs under suitable local surjectivity and smoothness hypotheses, but little has been done in characterizing convergence of these algorithms when the underlying quantum circuit is affected by noise. In this work, we characterize the effect of different coherent and incoherent noise processes on the optimal parameters and the optimal cost of the VQE, and we study their influence on the convergence guarantees of the algorithm. Our work provides novel theoretical insight into the behavior of parameterized quantum circuits. Furthermore, we accompany our results with numerical simulations implemented via Pennylane.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16779v1
- Title: Investigating Retargetability Claims for Quantum Compilers
- Authors: Luke Southall, Joshua Ammermann, Rinor Kelmendi, Domenik Eichhorn, Ina Schaefer
- Categories: quant-ph (primary); quant-ph; cs.SE
- Links: abs=https://arxiv.org/abs/2601.16779v1  pdf=https://arxiv.org/pdf/2601.16779v1.pdf

Abstract:
In the NISQ-era, there is a wide variety of hardware manufacturers building quantum computers. Each of these companies may choose different approaches and hardware architectures for their machines. This poses a problem for quantum software engineering, as the retargetability of quantum programs across different hardware platforms becomes a non-trivial challenge. In response to this problem, various retargetable quantum compilers have been presented in the scientific literature. These promise the ability to compile software for different hardware platforms, enabling retargetability for quantum software. In this paper, we develop and apply a metric by which the retargetability of the quantum compilers can be assessed. We develop and run a study to analyze key aspects regarding the retargetability of the compilers Tket, Qiskit, and ProjectQ. Our findings indicate that Tket demonstrates the highest level of retargetability, closely followed by Qiskit, while ProjectQ lags behind. These results provide insights for quantum software developers in selecting appropriate compilers for their use-cases, and highlight areas for improvement in quantum compilers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16816v1
- Title: Harnessing Quantum Computing for Energy Materials: Opportunities and Challenges
- Authors: Seongmin Kim, In-Saeng Suh, Travis S. Humble, Thomas Beck, Eungkyu Lee, Tengfei Luo
- Categories: quant-ph (primary); quant-ph; cs.CE
- Links: abs=https://arxiv.org/abs/2601.16816v1  pdf=https://arxiv.org/pdf/2601.16816v1.pdf

Abstract:
Developing high-performance materials is critical for diverse energy applications to increase efficiency, improve sustainability and reduce costs. Classical computational methods have enabled important breakthroughs in energy materials development, but they face scaling and time-complexity limitations, particularly for high-dimensional or strongly correlated material systems. Quantum computing (QC) promises to offer a paradigm shift by exploiting quantum bits with their superposition and entanglement to address challenging problems intractable for classical approaches. This perspective discusses the opportunities in leveraging QC to advance energy materials research and the challenges QC faces in solving complex and high-dimensional problems. We present cases on how QC, when combined with classical computing methods, can be used for the design and simulation of practical energy materials. We also outline the outlook for error-corrected, fault-tolerant QC capable of achieving predictive accuracy and quantum advantage for complex material systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16840v1
- Title: Protocols to share genuine multipartite entanglement employing copies of biseparable states
- Authors: Swati Choudhary, Ujjwal Sen, Saronath Halder
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16840v1  pdf=https://arxiv.org/pdf/2601.16840v1.pdf

Abstract:
Sharing genuine multipartite entanglement by considering collective use of copies of biseparable states, which are entangled across all bipartitions but lack genuine multipartite entanglement at the single-copy level, plays a central role in several quantum information processing protocols, and has been referred as genuine multipartite entanglement activation. We present a protocol for three-qutrit systems showing that two copies of rank-two biseparable states, entangled across every bipartition, are sufficient to generate a genuinely multipartite entangled state with nonzero probability. This contrasts with the three-qubit scenario where many copies of biseparable states might be required for sharing genuine multipartite entanglement. We subsequently generalize our protocols to the case of an arbitrary number of parties. Our protocol does not rely on the implementation of joint measurements on the copies of states. Interestingly, the proposed construction naturally leads to the activation of genuinely nonlocal correlations, yielding a result that is stronger than genuine multipartite entanglement activation alone.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16875v1
- Title: Generation of fully phase controlled two-photon entangled states
- Authors: Ian Ford, Adrien Amour, Matthias Keller
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16875v1  pdf=https://arxiv.org/pdf/2601.16875v1.pdf

Abstract:
Control over the internal states of trapped ions makes them the ideal system to generate single and two-photon states. Coupling a single ion to an optical cavity enables efficient emission of single photons into a single spatial mode and grants control over their temporal shape, phase and frequency. Using the long coherence time of the ion's internal states and employing a scheme to protect the coherence of the ion-cavity interaction, we demonstrate the generation of a two-photon entangled state with full control over the phase. Initially, ion-photon entanglement is generated. A second photon is subsequently generated, mapping the ion's state onto the second photon. By adjusting the drive field the phase of the entangled state can be fully controlled. We implement this scheme in the most resource efficient way by utilizing a single $^{40}$Ca$^+$ ion coupled to an optical cavity and demonstrate the generation of a two-photon entangled stated with full phase control with a fidelity of up to 82\%.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16892v1
- Title: Quantum Position Verification with Remote Untrusted Devices
- Authors: Gautam A. Kavuri, Yanbao Zhang, Abigail R. Gookin, Soumyadip Patra, Joshua C. Bienfang, Honghao Fu, Yusuf Alnawakhtha, Dileep V. Reddy, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16892v1  pdf=https://arxiv.org/pdf/2601.16892v1.pdf

Abstract:
Many applications require or benefit from being able to securely localize remote parties. In classical physics, adversaries can in principle have complete knowledge of such a party's devices, and secure localization is fundamentally impossible. This limitation can be overcome with quantum technologies, but proposals to date require trusting vulnerable hardware. Here we develop and experimentally demonstrate a protocol for device-independent quantum position verification that guarantees security with only observed correlations from a loophole-free Bell test across a quantum network. The protocol certifies the position of a remote party against adversaries who, before each instance of the test, are weakly entangled, but otherwise have unlimited quantum computation and communication capabilities. Our demonstration achieves a one-dimensional localization that is 2.47(2) times smaller than the best, necessarily non-remote, classical localization protocol. Compared to such a classical protocol having identical latencies, the localization is 4.53(5) times smaller. This work anchors digital security in the physical world.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16898v1
- Title: Upper bounds on the purity of Wigner positive quantum states that verify the Wigner entropy conjecture
- Authors: Qipeng Qian, Christos Gagatsos
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16898v1  pdf=https://arxiv.org/pdf/2601.16898v1.pdf

Abstract:
We present analytical results toward the Wigner entropy conjecture, which posits that among all physical Wigner non-negative states the Wigner entropy is minimized by pure Gaussian states for which it attains the value $1+\lnπ$.Working under a minimal set of constraints on the Wigner function, namely, non-negativity, normalization, and the pointwise bound $πW\le 1$, we construct an explicit hierarchy of lower bounds $B_n$ on $S[W]$ by combining a truncated series lower bound for $-\ln x$ with moment identities of the Wigner function.This yields closed-form purity-based sufficient conditions ensuring $S[W]\ge 1+\lnπ$.In particular, we first prove that all Wigner non-negative states with $μ\le 4-2\sqrt3$ satisfy the Wigner entropy conjecture. We further obtain a systematic purity-only relaxation of the hierarchy, yielding the simple sufficient condition $μ\le 2/e$. On top of aforesaid results, our analysis clarifies why additional physicality constraints are necessary for purity-based approaches that aim to approach the extremal case $μ\leq1$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16941v1
- Title: Quantum Fisher information analysis for absorption measurements with undetected photons
- Authors: Martin Houde, Franz Roeder, Christine Silberhorn, Benjamin Brecht, Nicolás Quesada
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.16941v1  pdf=https://arxiv.org/pdf/2601.16941v1.pdf

Abstract:
We theoretically compare the quantum Fisher information (QFI) for three configurations of absorption spectroscopy with undetected idler photons: an SU(1,1) interferometer with inter-source idler loss, an induced-coherence (IC) setup in which the idler partially seeds a second squeezer together with a vacuum ancilla, and a distributed-loss (DL) scheme with in-medium attenuation. We calculate the QFI as a function of parametric gain for both full and signal-only detection access. For losses below 99% and low to moderate gain, the SU(1,1) configuration provides the largest QFI. At high gain and intermediate loss, the IC scheme performs best, while under extreme attenuation (transmission $<$ 1%) the DL model becomes optimal. These results delineate the measurement regimes in which each architecture is optimal in terms of information theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16952v1
- Title: Experimental investigation of nonclassicality in the simplest scenario via the degrees of freedom of light
- Authors: João M. M. Gama, Guilherme T. C. Cruz, Massy Khoshbin, Lorenzo Catani, José A. O. Huguenin, Wagner F. Balthazar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16952v1  pdf=https://arxiv.org/pdf/2601.16952v1.pdf

Abstract:
In this work, we experimentally investigate the classical-light emulation of different notions of nonclassicality in the simplest scenario. We implement this prepare-and-measure scenario involving four preparations and two binary-outcome measurements using two distinct experimental setups that exploit different degrees of freedom of light: polarization and first-order Hermite-Gaussian transverse modes. We additionally model experimental noise through an all-optical setup that reproduces the operational effect of a depolarizing channel. Our experimental results are consistent with the findings of Khoshbin et al. [Phys. Rev. A 109, 032212 (2024)]: under the assumption that the two measurements performed form a tomographically complete set, the observed statistics violate their noise-robust inequalities, indicating inconsistencies with preparation noncontextuality and bounded ontological distinctness for preparations. Although our implementation uses classical light, it reproduces the statistics predicted for the simplest scenario. Since the states and measurements of this scenario underpin computational advantages in tasks such as two-bit quantum random access codes -- among the simplest communication primitives enabling semi-device-independent certification of nonclassicality -- our implementation is directly relevant for such applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16961v1
- Title: Engineering discrete local dynamics in globally driven dual-species atom arrays
- Authors: Francesco Cesa, Andrea Di Fini, David Aram Korbany, Roberto Tricarico, Hannes Bernien, Hannes Pichler, Lorenzo Piroli
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2601.16961v1  pdf=https://arxiv.org/pdf/2601.16961v1.pdf

Abstract:
We introduce a method for engineering discrete local dynamics in globally-driven dual-species neutral atom experiments, allowing us to study emergent digital models through uniform analog controls. Leveraging the new opportunities offered by dual-species systems, such as species-alternated driving, our construction exploits simple Floquet protocols on static atom arrangements, and benefits of generalized blockade regimes (different inter- and intra-species interactions). We focus on discrete dynamical models that are special examples of Quantum Cellular Automata (QCA), and explicitly consider a number of relevant examples, including the kicked-Ising model, the Floquet Kitaev honeycomb model, and the digitization of generic translation-invariant nearest-neighbor Hamiltonians (e.g., for Trotterized evolution). As an application, we study chaotic features of discretized many-body dynamics that can be detected by leveraging only demonstrated capabilities of globally-driven experiments, and benchmark their ability to discriminate chaotic evolution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16968v1
- Title: Autonomous Optical Alignment of Satellite-Based Entanglement Sources using Reinforcement Learning
- Authors: Andrzej Gajewski, Robert Okuła, Marcin Pawłowski, Akshata Shenoy H
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16968v1  pdf=https://arxiv.org/pdf/2601.16968v1.pdf

Abstract:
Quantum entanglement distributed via satellites enable global-scale quantum communication. However, onboard sources are susceptible to misalignment due to dynamical orbital conditions. Here, we present two recalibration techniques for efficient generation of high quality entanglement using a periodically poled lithium niobate (PPLN)-based spontaneous parametric down-conversion (SPDC) source with minimum intervention. The first is a heuristic algorithm (HA) which mimics the manual alignment process in a laboratory. The second is based on reinforcement learning (RL). Our simulation demonstrates superior performance of RL with AUC=0.9119 compared to HA's 0.7042 in the modified ROC analysis (60 min threshold). RL achieves perfect alignment in 10 min as opposed to HA's 30 min. Both the methods operate within feasible satellite constraints, offering scalable automation for complex quantum communication scenarios.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16974v1
- Title: Formalising an operational continuum limit of quantum combs
- Authors: Clara Wassner, Jonáš Fuksa, Jens Eisert, Gregory A. L. White
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.16974v1  pdf=https://arxiv.org/pdf/2601.16974v1.pdf

Abstract:
Quantum combs are powerful conceptual tools for capturing multi-time processes in quantum information theory, constituting the most general quantum mechanical process. But, despite their causal nature, they lack a meaningful physical connection to time -- and are, by and large, arguably incompatible with it without extra structure. The subclass of quantum combs which assumes an underlying process is described by the so-called process tensor framework, which has been successfully used to study and characterise non-Markovian open quantum systems. But, although process tensors are motivated by an underlying dynamics, it is not a priori clear how to connect to a continuous process tensor object mathematically -- leaving an uncomfortable conceptual gap. In this work, we take a decisive step toward remedying this situation. We introduce a fully continuous process tensor framework by showing how the discrete multi-partite Choi state becomes a field-theoretic state in bosonic Fock space, which is intrinsically and rigorously defined in the continuum. With this equipped, we lay out the core structural elements of this framework and its properties. This translation allows for an information-theoretic treatment of multi-time correlations in the continuum via the analysis of their continuous matrix product state representatives. Our work closes a gap in the quantum information literature, and opens up the opportunity for the application of many-body physics insights to our understanding of quantum stochastic processes in the continuum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16261v1
- Title: A First Demonstration of the SQUAT Detector Architecture: Direct Measurement of Resonator-Free Charge-Sensitive Transmons
- Authors: H. Magoon, T. Aralis, T. Dyson, J. Anczarski, D. Baxter, G. Bratrud, R. Carpenter, S. Condon, et al.
- Categories: physics.ins-det (primary); physics.ins-det; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16261v1  pdf=https://arxiv.org/pdf/2601.16261v1.pdf

Abstract:
The Superconducting Quasiparticle-Amplifying Transmon (SQUAT) is a new sensor architecture for THz (meV) detection based on a weakly charge-sensitive transmon directly coupled to a transmission line. In such devices, energy depositions break Cooper pairs in the qubit capacitor islands, generating quasiparticles. Quasiparticles that tunnel across the Josephson junction change the transmon qubit parity, generating a measurable signal. In this paper, we present the design of first-generation SQUATs and demonstrate an architecture validation. We summarize initial characterization measurements made with prototype devices, comment on background sources that influence the observed parity-switching rate, and present experimental results showing simultaneous detection of charge and quasiparticle signals using aluminum-based SQUATs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16279v1
- Title: Anisotropic uncertainty principles for metaplectic operators
- Authors: Elena Cordero, Gianluca Giacchi, Edoardo Pucci
- Categories: math.AP (primary); math.AP; math-ph; math.SG; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16279v1  pdf=https://arxiv.org/pdf/2601.16279v1.pdf

Abstract:
We establish anisotropic uncertainty principles (UPs) for general metaplectic operators acting on   $L^2(\mathbb{R}^d)$, including degenerate cases associated with symplectic matrices whose   $B$-block has nontrivial kernel. In this setting, uncertainty phenomena are shown to be intrinsically   directional and confined to an effective phase-space dimension given by $\mathrm{rank}(B)$.   First, we prove sharp Heisenberg-Pauli-Weyl type inequalities involving only the directions   corresponding to $\ker(B)^\perp$, with explicit lower bounds expressed in terms of geometric   quantities associated with the underlying symplectic transformation. We also provide a complete   characterization of all extremizers, which turn out to be partially Gaussian functions with free   behavior along the null directions of $B$.   Building on this framework, we extend the Beurling-Hörmander theorem to the metaplectic   setting, obtaining a precise polynomial-Gaussian structure for functions satisfying suitable   exponential integrability conditions involving both $f$ and its metaplectic transform. Finally,   we prove a Morgan-type (or Gel'fand--Shilov type) uncertainty principle for metaplectic operators,   identifying a sharp threshold separating triviality from density of admissible functions and   showing that this threshold is invariant under metaplectic transformations.   Our results recover the classical Fourier case and free metaplectic transformations as special   instances, and reveal the geometric and anisotropic nature of uncertainty principles in the   presence of symplectic degeneracies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16304v1
- Title: Axial Anomaly, entanglement and polarization
- Authors: O. V. Teryaev
- Categories: hep-ph (primary); hep-ph; nucl-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16304v1  pdf=https://arxiv.org/pdf/2601.16304v1.pdf

Abstract:
The (pion) decays controlled by axial anomaly imply the specific entanglement between photons having also the counterparts for classical electromagnetic waves. This is also a specific case of Eisnstein-Podolsky-Rosen-Bohm-Aharonov effect. The absence of causality and non-locality in (angular) momentum conservation is manifested, being especially clear for the generalization to the case of time rather than space separation corresponds to the polarization of dileptons described by time-like pion transition formfactors which may be studied experimentally. The similar decays in external magnetic field manifest the interplay with vacuum conductivity in external magnetic field and longitudinal polarization of vector mesons observed in heavy-ion collisions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16306v1
- Title: A modified Lindblad equation for a Rabi driven electron-spin qubit with tunneling to a Markovian lead
- Authors: Emily Townsend, Joshua Pomeroy, Garnett W. Bryant
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16306v1  pdf=https://arxiv.org/pdf/2601.16306v1.pdf

Abstract:
We derive a modified Lindblad equation for the state of quantum dot tunnel coupled to a Markovian lead when the spin state of the dot is driven by an oscillating magnetic field. We show that the equation is a completely positive, trace-preserving map and find the jump operators. This is a driven-dissipative regime in which coherent driving is relevant to the tunneling and cannot be treated as simply a rotation modifying the system with a bath derived under a static magnetic field. This work was motivated by an experimental desire to determine the Zeeman splitting of an electron spin on a quantum dot (a spin qubit), and in a related work we show that this splitting energy can be found by measuring the charge occupancy of the dot while sweeping the frequency of the driving field \ arXiv:2503.17481. Here we cover the full derivation of the equation and give the jump operators. These jump operators are potentially useful for describing the stochastic behavior of more complex systems with coherent driving of a spin capable of tunneling on or off of a device, such as in electron spin resonance scanning tunneling microscopy. The jump operators have the interesting feature of combining jumps of electrons onto and off of the device.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16328v1
- Title: Bichromatic Tweezers for Qudit Quantum Computing in ${}^{87}$Sr
- Authors: Enrique A. Segura Carrillo, Eric J. Meier, Michael J. Martin
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16328v1  pdf=https://arxiv.org/pdf/2601.16328v1.pdf

Abstract:
Neutral atoms have become a competitive platform for quantum metrology, simulation, sensing, and computing. Current magic trapping techniques are insufficient to engineer magic trapping conditions for qudits encoded in hyperfine states with $J \neq 0$, compromising qudit coherence. In this paper we propose a scheme to engineer magic trapping conditions for qudits via bichromatic tweezers. We show it is possible to suppress differential light shifts across all magnetic sublevels of the $5s5p$ $\mathrm{^{3}P_2}$ state by using two carefully chosen wavelengths (with comparable tensor light shift magnitude and opposite sign) at an appropriate intensity ratio, thus suppressing light-shift induced dephasing, enabling scalar magic conditions between the ground state and $5s5p$ $\mathrm{^{3}P_2}$, and tensor magic conditions for qudits encoded within it. Furthermore, this technique enables robust operation at the tensor magic angle 54.7$^\circ$ with linear trap polarization via reduced sensitivity to uncertainty in experimental parameters. We expect this technique to enable new loading protocols, enhance cooling efficiency, and enhance nuclear spins' coherence times, thus facilitating qudit-based quantum computing in ${}^{87}$Sr in the $5s5p$ $\mathrm{^{3}P_2}$ manifold.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16329v1
- Title: National Quantum Strategies: A Data-Driven Approach to Understanding the Quantum Ecosystem
- Authors: Simon Richard Goorney, Emre Aslan, Aleksandrs Baskakovs, Borja Muñoz, Jacob Sherson
- Categories: physics.soc-ph (primary); physics.soc-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16329v1  pdf=https://arxiv.org/pdf/2601.16329v1.pdf

Abstract:
As quantum technologies (QT) move from foundational research toward industrial and societal deployment, national strategies have become critical instruments for shaping the future of this emerging field. In this study, we conduct the first large-scale, data-driven analysis of 62 national quantum strategic documents (QSDs) from 20 countries. Using AI-based natural language processing (topic modeling), we identify 12 topics present in the text, ranging from technical development areas to transversal aspects such as workforce development and governance. Temporal analysis reveals a distinct shift in policy discourse toward applications of QT and commercialisation, and relatively away from basic science. Our findings highlight the increasing diversification of the QT field, and contribute to the growing area of quantum policy studies. We advocate for more AI and data-driven analyses of the quantum ecosystem, to work toward a scalable framework for understanding the technological and societal challenges of the second quantum revolution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16423v1
- Title: Quantum Sensing MRI for Noninvasive Detection of Neuronal Electrical Activity in Human Brains
- Authors: Yongxian Qian, Ying-Chia Lin, Seyedehsara Hejazi, Kamri Clarke, Kennedy Watson, Xingye Chen, Nahbila-Malikha Kumbella, Justin Quimbo, et al.
- Categories: physics.med-ph (primary); physics.med-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16423v1  pdf=https://arxiv.org/pdf/2601.16423v1.pdf

Abstract:
Neuronal electrical activity underlies human cognition, yet its direct, noninvasive measurement in the living human brain remains a fundamental challenge. Existing neuroimaging techniques, including EEG, MEG, and fMRI, are limited by trade-offs in sensitivity and spatial or temporal resolution. Here we propose quantum sensing MRI (qsMRI), a noninvasive approach that enables direct detection of neuronal firing-induced magnetic fields using a clinical MRI system. qsMRI exploits endogenous proton (1H) nuclear spins in water molecules as intrinsic quantum sensors and decodes time-resolved phase information from free induction decay (FID) signals to infer neuronal magnetic fields. We validate qsMRI through simulations, phantom experiments, and human studies at rest and during motor tasks, and provide open experimental procedures to facilitate independent validation. We further present a case study demonstrating potential applications to neurological disorders. qsMRI represents a first-in-human application of quantum sensing on a clinical MRI platform, establishes a non-BOLD functional imaging modality, and enables interrogation of neuronal firing dynamics in both cortical and deep brain regions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16484v1
- Title: Integrated Photonic Quantum Computing: From Silicon to Lithium Niobate
- Authors: Hui Zhang, Yiming Ma, Di Zhu, Yuancheng Zhan, Yuzhi Shi, Zhanshan Wang, Leong Chuan Kwek, Anthony Laing, et al.
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16484v1  pdf=https://arxiv.org/pdf/2601.16484v1.pdf

Abstract:
Quantum technologies have surpassed classical systems by leveraging the unique properties of superposition and entanglement in photons and matter. Recent advancements in integrated quantum photonics, especially in silicon-based and lithium niobate platforms, are pushing the technology toward greater scalability and functionality. Silicon circuits have progressed from centimeter-scale, dual-photon systems to millimeter-scale, high-density devices that integrate thousands of components, enabling sophisticated programmable manipulation of multi-photon states. Meanwhile, lithium niobate, thanks to its wide optical transmission window, outstanding nonlinear and electro-optic coefficients, and chemical stability, has emerged as an optimal substrate for fully integrated photonic quantum chips. Devices made from this material exhibit high efficiency in in generating, manipulating, converting, storing, and detecting photon states, thereby establishing a basis for deterministic multi-photon generation and single-photon quantum interactions, as well as comprehensive frequency-state control. This review explores the development of integrated photonic quantum technologies based on both silicon and lithium niobate, highlighting invaluable insights gained from silicon-based systems that can assist the scaling of lithium niobate technologies. It examines the functional integration mechanisms of lithium niobate in electro-optic tuning and nonlinear energy conversion, showcasing its transformative impact throughout the photonic quantum computing process. Looking ahead, we speculate on the developmental pathways for lithium niobate platforms and their potential to revolutionize areas such as quantum communication, complex system simulation, quantum sampling, and optical quantum computing paradigms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16564v1
- Title: A Robust Strontium Tweezer Apparatus for Quantum Computing
- Authors: Marijn Venderbosch, Rik van Herk, Zhichao Guo, Jesús del Pozo Mellado, Max Festenstein, Deon Janse van Rensburg, Ivo Knottnerus, Yu Chih Tseng, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16564v1  pdf=https://arxiv.org/pdf/2601.16564v1.pdf

Abstract:
Neutral atoms for quantum computing applications show promise in terms of scalability and connectivity. We demonstrate the realization of a versatile apparatus capable of stochastically loading a 5x5 array of optical tweezers with single $^{88}$Sr atoms featuring flexible magnetic field control and excellent optical access. A custom-designed oven, spin-flip Zeeman slower, and deflection stage produce a controlled flux of Sr directed to the science chamber. In the science chamber, featuring a vacuum pressure of $3 \times 10^{-11}$ mbar, the Sr is cooled using two laser cooling stages, resulting in $\sim 3 \times 10^5$ atoms at a temperature of 5(1) $μ$K. The optical tweezers feature a $1/e^2$ waist of 0.81(2) $μ$m, and loaded atoms can be imaged with a fidelity of $\sim 0.997$ and a survival probability of $0.99^{+0.01}_{-0.02}$. The atomic array presented here forms the core of a full-stack quantum computing processor targeted for quantum chemistry computational problems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16646v1
- Title: Algebraic Geometry for Spin-Adapted Coupled Cluster Theory
- Authors: Fabian M. Faulstich, Svala Sverrisdóttir
- Categories: physics.chem-ph (primary); physics.chem-ph; math.AG; math.RT; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16646v1  pdf=https://arxiv.org/pdf/2601.16646v1.pdf

Abstract:
We develop and numerically analyze an algebraic-geometric framework for spin-adapted coupled-cluster (CC) theory. Since the electronic Hamiltonian is SU(2)-invariant, physically relevant quantum states lie in the spin singlet sector. We give an explicit description of the SU(2)-invariant (spin singlet) many-body space by identifying it with an Artinian commutative ring, called the excitation ring, whose dimension is governed by a Narayana number. We define spin-adapted truncation varieties via embeddings of graded subspaces of this ring, and we identify the CCS truncation variety with the Veronese square of the Grassmannian. Compared to the spin-generalized formulation, this approach yields a substantial reduction in dimension and degree, with direct computational consequences. In particular, the CC degree of the truncation variety -- governing the number of homotopy paths required to compute all CC solutions -- is reduced by orders of magnitude. We present scaling studies demonstrating asymptotic improvements and we exploit this reduction to compute the full solution landscape of spin-adapted CC equations for water and lithium hydride.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16703v1
- Title: Dirac-Bergmann algorithm and canonical quantization of $k$-essence cosmology
- Authors: Andrés Lueiza, Andronikos Paliathanasis, Nikolaos Dimakis
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16703v1  pdf=https://arxiv.org/pdf/2601.16703v1.pdf

Abstract:
We develop a general canonical quantization scheme for $k$-essence cosmology in scalar-tensor theory. Utilizing the Dirac-Bergmann algorithm, we construct the Hamiltonian associated with the cosmological field equations and identify the first- and second-class constraints. The introduction of appropriate canonically conjugate variables with respect to Dirac brackets, allows for the canonical quantization of the model. In these new variables, the Hamiltonian constraint reduces to a quadratic function with no potential term. Its quantum realization leads to a Wheeler-DeWitt equation reminiscent of the massless Klein-Gordon case. As an illustrative example, we consider the action of a tachyonic field and investigate the conditions under which a phantom crossing can occur as a quantum tunneling effect. For the simplified constant potential case, we investigate the consequences of different boundary conditions on the singularity avoidance and to the mean expansion rate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16747v1
- Title: Moderate-terahertz-induced plateau expansion of high-order harmonic generation to soft X-ray region
- Authors: Doan-An Trieu, Duong D. Hoang-Trong, Cam-Tu Le, Sang Ha, Ngoc-Hung Phan, F. V. Potemkin, Van-Hoang Le, Ngoc-Loan Phan
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16747v1  pdf=https://arxiv.org/pdf/2601.16747v1.pdf

Abstract:
Extending the high-harmonic cutoff with experimentally accessible fields is essential for advancing tabletop coherent extreme ultraviolet (EUV) and soft X-ray sources. Although terahertz (THz) assistance offers a promising route, cutoff extension at weak, laboratory-accessible THz strengths remain poorly understood. In this report, we comprehensively investigate THz-assisted high-order harmonic generation (HHG) using time-dependent Schrödinger equation simulations supported by classical trajectory analysis and Bohmian-based quantum dynamics. By mapping the plateau evolution versus THz strength, we show that even weak THz fields can extend the cutoff, producing a pronounced ``fish-fin'' structure whose prominent rays saturate near $I_p + 8 U_p$. We trace this extension to long electron excursions spanning several optical cycles before recombination, and provide a fully consistent explanation using both classical analysis and Bohmian trajectories flow. Our findings reveal that this cutoff-extension mechanism is remarkably robust, persisting across different atomic species and remaining insensitive to variations in the driving parameters. These results demonstrate that cutoff control is achievable with laboratory-scale THz fields, offering practical guidelines for engineering coherent high-energy HHG, and providing a robust pathway for tracking ultrafast electron motion in real time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16776v1
- Title: Z2 Lattice Gauge Theory on Non-trivial Topology and Its Quantum Simulation
- Authors: Jiaqi Hu, Shu Tian, Xiaopeng Cui, Rebing Wu, Man-Hong Yung, Yu Shi
- Categories: hep-lat (primary); hep-lat; cond-mat.other; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16776v1  pdf=https://arxiv.org/pdf/2601.16776v1.pdf

Abstract:
Wegner duality is essential for Z2 lattice gauge theory, yet the duality on non-trivial topologies has remained implicit. We extend Wegner duality to arbitrary topology and dimension, obtaining a new class of Ising models, in which topology is encoded in non-local domain-wall patterns. Without the overhead of gauge constraints, simulating this model on an L*L torus requires only L*L qubits with two-body couplings, halving the conventional four-body coupled 2L*L qubits, enabling full experimental realization of Z2 lattice gauge theory on near-term devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16883v1
- Title: Universal classical and quantum fluctuations in the large deviations of current of noisy quantum systems: The case of QSSEP and QSSIP
- Authors: Mathias Albert, Denis Bernard, Tony Jin, Stefano Scopa, Shiyi Wei
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16883v1  pdf=https://arxiv.org/pdf/2601.16883v1.pdf

Abstract:
We study the fluctuation statistics of integrated currents in noisy quantum diffusive systems, focusing on the Quantum Symmetric Simple Exclusion and Inclusion Processes (QSSEP/QSSIP). These one-dimensional fermionic (QSSEP) and bosonic (QSSIP) models feature stochastic nearest-neighbor hopping driven by Brownian noise, together with boundary injection and removal processes. They provide solvable microscopic settings in which quantum coherence coexists with diffusion. Upon noise averaging, their dynamics reduce to those of the classical SSEP/SSIP. We show that the cumulant generating function of the integrated current, at large scales, obeys a large deviation principle. To leading order in system size and for each noise realization, it converges to that of the corresponding classical process, establishing a classical typicality of current fluctuations in these noisy quantum systems. We further demonstrate a direct connection with Macroscopic Fluctuation Theory (MFT), showing that the large-scale equations satisfied by biased quantum densities coincide with the steady-state Hamilton equations of MFT, thereby providing a microscopic quantum justification of the MFT framework in these models. Finally, we identify the leading finite-size corrections to the current statistics. We show the existence of subleading contributions of purely quantum origin, which are absent in the corresponding classical setting, and provide their explicit expressions for the second and third current cumulants. These quantum corrections are amenable to direct experimental or numerical verification, provided sufficient control over the noise realizations can be achieved. Their presence points toward the necessity of a quantum extension of Macroscopic Fluctuation Theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.16951v1
- Title: Boundary critical phenomena in the quantum Ashkin-Teller model
- Authors: Yifan Liu, Natalia Chepiga, Yoshiki Fukusumi, Masaki Oshikawa
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16951v1  pdf=https://arxiv.org/pdf/2601.16951v1.pdf

Abstract:
We investigate the boundary critical phenomena of the one-dimensional quantum Ashkin-Teller model using boundary conformal field theory and density matrix renormalization group (DMRG) simulations. Based on the $\mathbb{Z}_2$-orbifold of the $c=1$ compactified boson boundary conformal field theory, we construct microscopic lattice boundary terms that renormalize to the stable conformal boundary conditions,, utilizing simple current extensions and the underlying $\mathrm{SU}(2)$ symmetry to explicitly characterize the four-state Potts point. We validate these theoretical identifications via finite-size spectroscopy of the lattice energy spectra, confirming their consistency with $D_4$ symmetry and Kramers-Wannier duality. Finally, we discuss the boundary renormalization group flows among these identified fixed points to propose a global phase diagram for the boundary criticality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2307.09566v2
- Title: Fast design and scaling of multi-qubit gates in large-scale trapped-ion quantum computers
- Authors: Lee Peleg, David Schwerdt, Jonathan Nemirovsky, Yotam Shapira, Nitzan Akerman, Ady Stern, Amit Ben Kish, Roee Ozeri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2307.09566v2  pdf=https://arxiv.org/pdf/2307.09566v2.pdf

Abstract:
Quantum computers based on crystals of trapped ions are a prominent technology for quantum computation. A unique feature of trapped ions is their long-range Coulomb interactions, which can be exploited to realize large-scale multiqubit entanglement gates. However, scaling up the number of qubits, $N$, in these systems, while retaining high-fidelity and high-speed operations, is challenging. Specifically, designing multiqubit entanglement gates in long ion crystals of hundreds of ions involves an NP-hard optimization problem, rendering scale-up not only a technological challenge, but also a conceptual challenge. Here we introduce a method that mitigates this challenge, effectively allowing for a polynomial-time design of fast, robust, and programmable entanglement gates, acting on the entire ion-crystal. We show that while the number of simultaneous entanglement operations scales as $N^2$, the gate duration scales as $N$, leading to a scaling advantage. We use our methods to investigate the drive-power requirements and susceptibility to noise and errors of these multiqubit gates. Our method delineates a path towards scaling up quantum computers based on ion-crystals with hundreds of qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2309.10804v2
- Title: Continuous-wave all-optical single-photon transistor based on a Rydberg-atom ensemble
- Authors: Iason Tsiamis, Oleksandr Kyriienko, Anders S. Sørensen
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2309.10804v2  pdf=https://arxiv.org/pdf/2309.10804v2.pdf

Abstract:
Continuous-wave (cw) architectures provide a promising route to interface disparate quantum systems by relaxing the need for precise synchronization. While essential cw components, including microwave single-photon transistors and microwave-optical converters, have been explored, an all-optical cw single-photon transistor has remained a missing piece. We propose a high-efficiency, high-gain implementation using Rydberg atoms, in which a control photon disrupts the transmission of a continuous probe beam via the van der Waals interaction. This device completes the set of components required for cw processing of quantum signals and paves the way for all-optical processing at the quantum level.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2309.10873v2
- Title: Continuous-wave quantum light control via engineered Rydberg-induced dephasing
- Authors: Iason Tsiamis, Oleksandr Kyriienko, Anders S. Sørensen
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2309.10873v2  pdf=https://arxiv.org/pdf/2309.10873v2.pdf

Abstract:
We analyze several implementations of all-optical single-photon transistors (SPTs) operating in the continuous-wave (cw) regime, as presented in the companion paper [Phys. Rev. A 113, L011701 (2026)]. The devices rely on ensembles of Rydberg atoms interacting via van der Waals interactions. Under electromagnetically induced transparency (EIT), a weak probe field is fully transmitted through the atomic ensemble in the absence of control photons. Exciting a collective Rydberg state with a single control photon breaks the EIT condition, thereby strongly suppressing the probe transmission. We show how collective Rydberg interactions in an atomic ensemble, confined either in an optical cavity or in free space, give rise to two distinct probe-induced dephasing mechanisms. These processes localize the control excitations, extend their lifetimes, and increase the device efficiency. We characterize the SPTs in terms of control-photon absorption probability and probe gain, supported by numerical simulations of realistic one- and three-dimensional ensembles. The proposed cw devices complement previously demonstrated SPTs and broaden the toolbox of quantum light manipulation circuitry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2405.20322v2
- Title: Quantum generalizations of Glauber and Metropolis dynamics
- Authors: András Gilyén, Chi-Fang Chen, Joao F. Doriguello, Michael J. Kastoryano
- Categories: quant-ph (primary); quant-ph; cs.DS
- Links: abs=https://arxiv.org/abs/2405.20322v2  pdf=https://arxiv.org/pdf/2405.20322v2.pdf

Abstract:
Classical Markov Chain Monte Carlo methods have been essential for simulating statistical physical systems and have proven well applicable to other systems with many degrees of freedom. Motivated by the statistical physics origins, Chen, Kastoryano, and Gilyén [CKG23] proposed a continuous-time quantum thermodynamic analogue to Glauber dynamics that is (i) exactly detailed balanced, (ii) efficiently implementable, and (iii) quasi-local for geometrically local systems. Physically, their construction resembles the dissipative dynamics arising from weak system-bath interaction. In this work, we give an efficiently implementable discrete-time counterpart to any continuous-time quantum Gibbs sampler. Our construction preserves the desirable features (i)-(iii) while does not decrease the spectral gap. Also, we give an alternative highly coherent quantum generalization of detailed balanced dynamics that resembles another physically derived master equation, and propose a smooth interpolation between this and earlier constructions. Moreover, we show how to make earlier Metropolis-style Gibbs samplers (which estimate energies both before and after jumps) exactly detailed balanced. We study generic properties of all constructions, including the uniqueness of the fixed point, the (quasi-)locality of the resulting operators. Finally, we prove that the spectral gap of our new highly coherent Gibbs sampler is constant at high temperatures, thereby it mixes fast. We hope that our systematic approach to quantum Glauber and Metropolis dynamics will lead to widespread applications in various domains.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2409.12932v3
- Title: Entanglement-enhanced quantum sensing via optimal global control with neutral atoms in a cavity
- Authors: Vineesha Srivastava, Sven Jandura, Gavin K Brennen, Guido Pupillo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2409.12932v3  pdf=https://arxiv.org/pdf/2409.12932v3.pdf

Abstract:
We present a deterministic protocol for the preparation of entangled states in the symmetric Dicke subspace of $N$ spins coupled to a common cavity mode that prepares entangled states useful for quantum sensing, achieving a precision significantly better than the standard quantum limit in the presence of photon cavity loss, spontaneous emission and dephasing. The protocol combines a new geometric phase gate which can be utilized for exact unitary synthesis on the Dicke subspace, an analytic solution of the noisy quantum channel dynamics and optimal control methods. This work opens the way to entanglement-enhanced sensing with cold trapped atoms in cavities and is extendable to other spin systems coupled to a bosonic mode.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2411.10343v2
- Title: Local Clustering Decoder as a fast and adaptive hardware decoder for the surface code
- Authors: Abbas B. Ziad, Ankit Zalawadiya, Canberk Topal, Joan Camps, György P. Gehér, Matthew P. Stafford, Mark L. Turner
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2411.10343v2  pdf=https://arxiv.org/pdf/2411.10343v2.pdf

Abstract:
To avoid prohibitive overheads in performing fault-tolerant quantum computation, the decoding problem needs to be solved accurately and at speeds sufficient for fast feedback. Existing decoding systems fail to satisfy both of these requirements, meaning they either slow down the quantum computer or reduce the number of operations that can be performed before the quantum information is corrupted. We introduce the Local Clustering Decoder as a solution that simultaneously achieves the accuracy and speed requirements of a real-time decoding system. Our decoder is implemented on FPGAs and exploits hardware parallelism to keep pace with the fastest qubit types. Further, it comprises an adaptivity engine that allows the decoder to update itself in real-time in response to control signals, such as heralded leakage events. Under a realistic circuit-level noise model where leakage is a dominant error source, our decoder enables one million error-free quantum operations with 4x fewer physical qubits when compared to standard non-adaptive decoding. This is achieved whilst decoding in under 1 us per round with modest FPGA resources, demonstrating that high-accuracy real-time decoding is possible, and reducing the qubit counts required for large-scale fault-tolerant quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2412.08724v2
- Title: Separability Lindblad equation for dynamical open-system entanglement
- Authors: Julien Pinske, Laura Ares, Benjamin Hinrichs, Martin Kolb, Jan Sperling
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2412.08724v2  pdf=https://arxiv.org/pdf/2412.08724v2.pdf

Abstract:
Providing entanglement for the design of quantum technologies in the presence of noise constitutes today's main challenge in quantum information science. A framework is required that assesses the build-up of entanglement in realistic settings. In this work, we put forth a new class of nonlinear quantum master equations in Lindblad form that unambiguously identify dynamical entanglement in open quantum systems via deviations from a separable evolution. This separability Lindblad equation restricts quantum trajectories to classically correlated states only. Unlike many conventional approaches, here the entangling capabilities of a process are not characterized by input-output relations, but separability is imposed at each instant of time. We solve these equations for crucial examples, thereby quantifying the dynamical impact of entanglement in non-equilibrium scenarios. Our results allow to benchmark the engineering of entangled states through dissipation. The separability Lindblad equation provides a unique path to characterizing quantum correlations caused by arbitrary system-bath interactions, specifically tailored for the noisy intermediate-scale quantum era.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2412.21118v3
- Title: Efficient Approximate Degenerate Ordered Statistics Decoding for Quantum Codes via Reliable Subset Reduction
- Authors: Ching-Feng Kung, Kao-Yueh Kuo, Ching-Yi Lai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2412.21118v3  pdf=https://arxiv.org/pdf/2412.21118v3.pdf

Abstract:
Efficient and scalable decoding of quantum codes is essential for high-performance quantum error correction. In this work, we introduce Reliable Subset Reduction (RSR), a reliability-driven preprocessing framework that leverages belief propagation (BP) statistics to identify and remove highly reliable qubits, substantially reducing the effective problem size. Additionally, we identify a degeneracy condition that allows high-order OSD to be simplified to order-0 OSD. By integrating these techniques, we present an ADOSD algorithm that significantly improves OSD efficiency. Our BP+RSR+ADOSD framework extends naturally to circuit-level noise and can handle large-scale codes with more than $10^4$ error variables. Through extensive simulations, we demonstrate improved performance over MWPM and Localized Statistics Decoding for a variety of CSS and non-CSS codes under the code-capacity noise model, and for rotated surface codes under realistic circuit-level noise. At low physical error rates, RSR reduces the effective problem size to less than 5\%, enabling higher-order OSD with accelerated runtime. These results highlight the practical efficiency and broad applicability of the BP+ADOSD framework for both theoretical and realistic quantum error correction scenarios.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2504.08494v2
- Title: Spin-state energetics of heme-related models with the variational quantum eigensolver
- Authors: Unathi Skosana, Sthembiso Gumede, Mark Tame
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.08494v2  pdf=https://arxiv.org/pdf/2504.08494v2.pdf

Abstract:
We present numerical calculations of the energetic separation between different spin states (singlet, triplet and quintet) for a simplified model of a deoxy-myoglobin protein using the variational quantum eigensolver (VQE) algorithm. The goal is to gain insight into the workflow and challenges of VQE simulations for transition metal complexes, with emphasis on methodology over hardware-specific implementation. The numerical calculations are performed using an in-house statevector simulator with single- and multi-reference trial wavefunctions based on the k-unitary pair coupled-cluster generalized singles and doubles or k-UpCCGSD ansatz. The spin-state energetics for active spaces of increasing size up to 10 spatial orbitals (20 spin orbitals or qubits) are computed with VQE and were found to agree with the classical complete active self-consistent field or CASSCF method to within 1-4 kcal/mol. We evaluate relevant multi-reference diagnostics and show that the spin states computed with VQE possess a sufficient degree of multi-reference character to highlight the presence of strong electron correlation effects. Our numerical simulations show that in the ideal case, the VQE algorithm is capable of reproducing spin-state energetics of strongly correlated systems such as transition metal complexes for both single- and multi-reference trial wavefunctions, asymptotically achieving good agreement with results from classical methods as the number of active orbitals increases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2504.13376v4
- Title: Addressing the Minor-Embedding Problem in Quantum Annealing and Evaluating State-of-the-Art Algorithm Performance
- Authors: Aitor Gomez-Tejedor, Eneko Osaba, Esther Villar-Rodriguez
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.ET
- Links: abs=https://arxiv.org/abs/2504.13376v4  pdf=https://arxiv.org/pdf/2504.13376v4.pdf

Abstract:
This study addresses the minor-embedding problem, which involves mapping the variables of an Ising model onto a quantum annealing processor. The primary motivation stems from the observed performance disparity of quantum annealers when solving problems suited to the processor's architecture versus those with non-hardware-native topologies. Our research has two main objectives: i) to analyze the impact of embedding quality on the performance of D-Wave Systems quantum annealers, and ii) to evaluate the quality of the embeddings generated by Minorminer, the standard minor-embedding technique in the quantum annealing literature, provided by D-Wave. Regarding the first objective, our experiments reveal a clear correlation between the average chain length of embeddings and the relative errors of the solutions sampled. This underscores the critical influence of embedding quality on quantum annealing performance. For the second objective, we evaluate Minorminer's embedding capabilities, the quality and robustness of its embeddings, and its execution-time performance on Erdös-Rényi graphs. We also compare its performance with Clique Embedding, another algorithm developed by D-Wave, which is deterministic and designed to embed fully connected Ising models into quantum annealing processors, serving as a worst-case scenario. The results demonstrate that there is significant room for improvement for Minorminer, suggesting that more effective embedding strategies could lead to meaningful gains in quantum annealing performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2504.14651v2
- Title: Exact Duality at Low Energy in a Josephson Tunnel Junction Coupled to a Transmission Line
- Authors: Luca Giacomelli, Michel H. Devoret, Cristiano Ciuti
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2504.14651v2  pdf=https://arxiv.org/pdf/2504.14651v2.pdf

Abstract:
We theoretically explore the low-energy behavior of a Josephson tunnel junction coupled to a finite-length, charge-biased transmission line and compare it to its flux-biased counterpart. For transmission lines of increasing length, we show that the low-energy charge-dependent energy bands of the charge-biased configuration can be exactly mapped onto those of the flux-biased system via a well-defined duality transformation of circuit parameters. In the limit of an infinitely long transmission line, the influence of boundary conditions vanishes, and both circuits reduce to a resistively shunted Josephson junction. This convergence reveals the system's intrinsic self-duality and critical behavior. Our exact formulation of charge-flux duality provides a foundation for generalizations to more complex superconductor-insulator phase transitions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2504.21306v2
- Title: Semiclassical Approach to Quantum Fisher Information
- Authors: Mahdi RouhbakhshNabati, Daniel Braun, Henning Schomerus
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2504.21306v2  pdf=https://arxiv.org/pdf/2504.21306v2.pdf

Abstract:
Quantum sensors driven into the quantum chaotic regime can have dramatically enhanced sensitivity, which, however, depends intricately on the details of the underlying classical phase space. Here, we develop an accurate semiclassical approach that provides direct and efficient access to the phase-space-resolved quantum Fisher information (QFI), the central quantity that quantifies the ultimate achievable sensitivity. This approximation reveals, in very concrete terms, that the QFI is large whenever a specific dynamical quantity tied to the sensing parameter displays a large variance over the course of the corresponding classical time evolution. Applied to a paradigmatic system of quantum chaos, the kicked top, we show that the semiclassical description is accurate already for modest quantum numbers, i.e., deep in the quantum regime, and it extends seamlessly to very high quantum numbers that are beyond the reach of other methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2505.12990v3
- Title: From Theory to Practice: Analyzing Variational Quantum Power Method for Quantum Optimization of QUBO Problems
- Authors: Ammar Daskin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.12990v3  pdf=https://arxiv.org/pdf/2505.12990v3.pdf

Abstract:
The variational quantum power method (VQPM), which adapts the classical power iteration algorithm for quantum settings, has shown promise for eigenvector estimation and optimization on quantum hardware. In this work, we provide a comprehensive theoretical and numerical analysis of VQPM by investigating its convergence, robustness, and qubit locking mechanisms. We present detailed strategies for applying VQPM to QUBO problems by leveraging these locking mechanisms. Based on the simulations for each strategy we have carried out, we give systematic guidelines for their practical applications. We also offer a numerical comparison with the quantum approximate optimization algorithm (QAOA) by running both algorithms on a set of trial problems and a simulation on noisy environments by using IBM Qiskit Aer simulation framework. Our results indicate that VQPM can be employed as an effective quantum optimization algorithm on quantum computers for QUBO problems, and this work can serve as an initial guideline for such applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2506.00647v3
- Title: Quantum Skip Gates: Coherently Conditioned Subroutines in Iterative Quantum Algorithms
- Authors: Kym Derriman
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.00647v3  pdf=https://arxiv.org/pdf/2506.00647v3.pdf

Abstract:
The Quantum Skip Gate (QSG) is a unitary circuit primitive that coherently superposes the execution and omission of an expensive quantum subroutine based on the outcome of a cheaper preceding subroutine, without mid-circuit measurement or loss of coherence. By using a control qubit and an internal flag, QSG enables conditional quantum logic entirely within a unitary framework. We demonstrate QSG experimentally in a Grover-style search on IBM quantum hardware with four data qubits and three Grover iterations, where it reduces costly subroutine calls by 9 to 25 percent and achieves 31 to 61 percent higher success-per-oracle efficiency relative to a fixed-order baseline. Noise-model simulations further confirm and strengthen these gains, reaching improvements of up to 45 percent when using an optimized swap-out design. These results show that coherently conditioned subroutines provide practical resource management, significantly reducing runtime cost and noise accumulation in near-term quantum algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2506.09037v2
- Title: Optimizing Sparse SYK
- Authors: Matthew Ding, Robbie King, Bobak T. Kiani, Eric R. Anschuetz
- Categories: quant-ph (primary); quant-ph; cs.DS
- Links: abs=https://arxiv.org/abs/2506.09037v2  pdf=https://arxiv.org/pdf/2506.09037v2.pdf

Abstract:
Finding the ground state of strongly-interacting fermionic systems is often the prerequisite for fully understanding both quantum chemistry and condensed matter systems. The Sachdev--Ye--Kitaev (SYK) model is a representative example of such a system; it is particularly interesting not only due to the existence of efficient quantum algorithms preparing approximations to the ground state such as Hastings--O'Donnell (STOC 2022), but also known no-go results for many classical ansatzes in preparing low-energy states. However, this quantum-classical separation is known to \emph{not} persist when the SYK model is sufficiently sparsified, i.e., when terms in the model are discarded with probability $1-p$, where $p=Θ(1/n^3)$ and $n$ is the system size. This raises the question of how robust the quantum and classical complexities of the SYK model are to sparsification.   In this work we initiate the study of the sparse SYK model where $p \in [Θ(1/n^3),1]$ and show there indeed exists a certain robustness of sparsification. We prove that with high probability, Gaussian states achieve only a $Θ(1/\sqrt{n})$-factor approximation to the true ground state energy of sparse SYK for all $p\geqΩ(\log n/n^2)$, and that Gaussian states cannot achieve constant-factor approximations unless $p \leq O(\log^2 n/n^3)$. Additionally, we prove that the quantum algorithm of Hastings--O'Donnell still achieves a constant-factor approximation to the ground state energy when $p\geqΩ(\log n/n)$. Combined, these show a provable separation between classical algorithms outputting Gaussian states and efficient quantum algorithms for the goal of finding approximate sparse SYK ground states whenever $p \geq Ω(\log n/n)$, extending the analogous $p=1$ result of Hastings--O'Donnell.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2506.13332v2
- Title: Efficient algorithms for quantum chemistry on modular quantum processors
- Authors: Tian Xue, Jacob P. Covey, Matthew Otten
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2506.13332v2  pdf=https://arxiv.org/pdf/2506.13332v2.pdf

Abstract:
Quantum chemistry is a promising application of future quantum computers, but the requirements on qubit count and other resources suggest that modular computing architectures will be required. We introduce an implementation of a quantum chemistry algorithm that is distributed across several computational modules: the distributed unitary selective coupled cluster (dUSCC). We design a packing scheme using the pseudo-commutativity of Trotterization to maximize the parallelism while optimizing the scheduling of all inter-module gates around the buffering of inter-module Bell pairs. We demonstrate dUSCC on a 3-cluster (H$_4$)$_3$ chain and show that it naturally utilizes the molecule's structure to reduce inter-module latency. We show that the run time of dUSCC is unchanged with inter-module latency up to $\sim$20$\times$ slower than intra-module gates in the (H$_4$)$_3$ while maintaining chemical accuracy. dUSCC should be "free" in the weakly entangled systems, and the existence of "free" dUSCC can be found efficiently using classical algorithms. This new compilation scheme both leverages pseudo-commutativity and considers inter-module gate scheduling, and potentially provides an efficient distributed compilation of other Trotterized algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2507.08358v2
- Title: Complexity of mixed Schatten norms of quantum maps
- Authors: Jan Kochanowski, Omar Fawzi, Cambyse Rouzé
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2507.08358v2  pdf=https://arxiv.org/pdf/2507.08358v2.pdf

Abstract:
We study the complexity of computing the mixed Schatten $\|Φ\|_{q\to p}$ norms of linear maps $Φ$ between matrix spaces. When $Φ$ is completely positive, we show that $\| Φ\|_{q \to p}$ can be computed efficiently when $q \geq p$. The regime $q \geq p$ is known as the non-hypercontractive regime and is also known to be easy for the mixed vector norms $\ell_{q} \to \ell_{p}$ [Boyd, 1974]. However, even for entanglement-breaking completely-positive trace-preserving maps $Φ$, we show that computing $\| Φ\|_{1 \to p}$ is $\mathsf{NP}$-complete when $p>1$. Moving beyond the completely-positive case and considering $Φ$ to be difference of entanglement breaking completely-positive trace-preserving maps, we prove that computing $\| Φ\|^+_{1 \to 1}$ is $\mathsf{NP}$-complete. In contrast, for the completely-bounded (cb) case, we describe a polynomial-time algorithm to compute $\|Φ\|_{cb,1\to p}$ and $\|Φ\|^+_{cb,1\to p}$ for any linear map $Φ$ and $p\geq1$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2507.18984v2
- Title: Scalable native multiqubit gates via engineered noncomputational-state interactions in superconducting fluxonium qubits
- Authors: Peng Zhao, Peng Xu, Zheng-Yuan Xue
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.18984v2  pdf=https://arxiv.org/pdf/2507.18984v2.pdf

Abstract:
Native multiqubit gates could be essential for bridging the gap from current noisy devices to future utility-scale quantum computers, as they can substantially reduce circuit depth for near-term applications on noisy devices and may also lower the physical overhead of fault-tolerant quantum computation. Here we introduce a scalable protocol for implementing native multi-controlled gates on fluxonium qubits, supporting an arbitrary number of control qubits ($N > 1$) while remaining compatible with existing single- and two-qubit gate realizations. Our approach leverages engineered interactions in noncomputational state manifolds to enable qubit-state selective transitions, which is activated for the direct implementation of $(C^{\otimes N})Z$ gates. We show that in square lattices with fluxonium qubits, $CCZ$, $CCCZ$, and $CCCCZ$ gates with errors around 0.01 (0.001) are achievable, with gate lengths of $50\,(100)\,\text{ns}$, $100\,(250)\,\text{ns}$, and $150\,(300)\,\text{ns}$, respectively. Looking forward, integrating these native multi-controlled gates with primitive single- and two-qubit gate sets within a single quantum processor could significantly enhance flexibility in circuit synthesis and offer a promising alternative pathway toward utility-scale quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2508.02638v2
- Title: Anticipating Decoherence for Enhancing Coherence in Quantum Systems
- Authors: Pranshu Maan, Yuheng Chen, Sean Borneman, Benjamin Lawrie, Alexander Puretzky, Hadiseh Alaeian, Alexandra Boltasseva, Vladimir M. Shalaev, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.02638v2  pdf=https://arxiv.org/pdf/2508.02638v2.pdf

Abstract:
Large-scale quantum systems require optical coherence between distant quantum devices, necessitating spectral indistinguishability. Scalable solid-state platforms offer promising routes to this goal. However, environmental disorders, including dephasing, spectral diffusion, and spin-bath interactions, influence the emitters' spectra and deteriorate the coherence. Using statistical theory, we identify correlations in spectral diffusion from slowly varying environmental coupling, revealing predictable dynamics extendable to other disorders. Importantly, this could enable the development of an anticipatory framework for forecasting and decoherence engineering in remote quantum emitters. To validate this framework, we demonstrate that a machine learning model trained on limited data can accurately forecast unseen spectral behavior. Realization of such a model on distinct quantum emitters could reduce the spectral shift by factors $\approx$ 2.1 to 15.8, depending on emitter stability, compared to no prediction. This work presents, for the first time, the application of anticipatory systems and replica theory to quantum technology, along with the first experimental demonstration of internal prediction that generalizes across multiple quantum emitters. These results pave the way for real-time decoherence engineering in scalable quantum systems. Such capability could lead to enhanced optical coherence and multi-emitter synchronization, with broad implications for quantum communication, computation, imaging, and sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2508.10500v2
- Title: Reservoir-Engineered Mechanical Cat States with a Driven Qubit
- Authors: M. Tahir Naseem
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.10500v2  pdf=https://arxiv.org/pdf/2508.10500v2.pdf

Abstract:
Macroscopic quantum superpositions, such as mechanical Schrödinger cat states, are central to emerging quantum technologies in sensing and bosonic error-correcting codes. We propose a scheme to generate such states by coupling a nanomechanical resonator to a coherently driven two-level system via both transverse and longitudinal interactions. Driving the qubit at twice the oscillator frequency activates resonant two-phonon exchange processes, enabling coherent conversion of drive energy into phonon pairs and their dissipative stabilization. Starting from the full time-dependent Hamiltonian, we derive an effective master equation for the mechanical mode by perturbative elimination of the lossy qubit. The reduced dynamics feature engineered two-phonon loss and a coherent squeezing term, which together drive the resonator into a deterministic Schrödinger-cat state. Our approach requires only a single driven qubit and no auxiliary cavity, offering a scalable and experimentally accessible route to macroscopic quantum superpositions in circuit-QED and related platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2510.08463v2
- Title: Approximating quantum states by states of low rank
- Authors: Nathaniel Johnston, Chi-Kwong Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.08463v2  pdf=https://arxiv.org/pdf/2510.08463v2.pdf

Abstract:
Given a positive integer k, it is natural to ask for a formula for the distance between a given density matrix (i.e., mixed quantum state) and the set of density matrices of rank at most k. This problem has already been solved when "distance" is measured in the trace or Frobenius norm. We solve it for all other unitary similarity invariant norms. We also present some consequences of our formula. For example, in the trace and Frobenius norms, the density matrix that is farthest from the set of low-rank density matrices is the maximally-mixed state, but this is not true in many other unitary similarity invariant norms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2510.08533v2
- Title: Fast Mixing of Quantum Spin Chains at All Temperatures
- Authors: Thiago Bergamaschi, Chi-Fang Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.08533v2  pdf=https://arxiv.org/pdf/2510.08533v2.pdf

Abstract:
It is shown that every one-dimensional Hamiltonian with short-range interaction admits a quantum Gibbs sampler [CKG23] with a system-size independent spectral gap at all finite temperatures. Consequently, their Gibbs states can be prepared in polylogarithmic depth, and satisfy exponential clustering of correlations, generalizing [Ara69].

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2510.16962v2
- Title: 28 GHz Wireless Channel Characterization for a Quantum Computer Cryostat at 4 Kelvin
- Authors: Ama Bandara, Viviana Centritto Arrojo, Heqi Deng, Masoud Babaie, Fabio Sebastiano, Edoardo Charbon, Evgenii Vinogradov, Eduard Alarcon, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.16962v2  pdf=https://arxiv.org/pdf/2510.16962v2.pdf

Abstract:
The scalability of quantum computing systems is constrained by the wiring complexity and thermal load introduced by dense wiring for control, readout and synchronization at cryogenic temperatures. To address this challenge, we explore the feasibility of wireless communication within a cryostat for a multi-core quantum computer, focusing on wireless channel characterization at cryogenic temperatures. We propose to place on-chip differential dipole antennas within the cryostat, designed to operate at 28 GHz in temperatures as low as 4 K. We model the antennas inside a realistic cryostat and, using full-wave electromagnetic simulations, we analyze impedance matching, spatial field distribution, and energy reverberation due to metallic structures. The wireless channel is characterized through measured channel impulse response (CIR) across multiple receiver antenna positions. The results demonstrate potential for reliable shortrange communication with high Signal-to-Noise Ratio (SNR) and limited sensitivity to positional variation, at the cost of nonnegligible delay spread, due to significant multipath effects.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2510.26189v4
- Title: Practical hybrid decoding scheme for parity-encoded spin systems
- Authors: Yoshihiro Nambu
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2510.26189v4  pdf=https://arxiv.org/pdf/2510.26189v4.pdf

Abstract:
We propose a practical hybrid decoding scheme for the parity-encoding architecture. This architecture was first introduced by N. Sourlas as a computational technique for tackling hard optimization problems, especially those modeled by spin systems such as the Ising model and spin glasses, and reinvented by W. Lechner, P. Hauke, and P. Zoller to develop quantum annealing devices. We study the specific model, called the SLHZ model, aiming to achieve a near-term quantum annealing device implemented solely through geometrically local spin interactions. Taking account of the close connection between the SLHZ model and a classical low-density-parity-check code, two approaches can be chosen for the decoding: (1) finding the ground state of a spin Hamiltonian derived from the SLHZ model, which can be achieved via stochastic decoders such as a quantum annealer or a classical Monte Carlo sampler; (2) using deterministic decoding techniques for the classical LDPC code, such as belief propagation and bit-flip decoder. The proposed hybrid approach combines the two approaches by applying bit-flip decoding to the readout of the stochastic decoder based on the SLHZ model. We present simulations demonstrating that this approach can reveal the latent potential of the SLHZ model, realizing soft-annealing concept proposed by Sourlas.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2510.26612v2
- Title: Discrete time quantum walk of locally interacting walkers
- Authors: Vikash Mittal, Tomasz Sowiński
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.26612v2  pdf=https://arxiv.org/pdf/2510.26612v2.pdf

Abstract:
In this work, we introduce a general form of a two-parameter family of local interactions between quantum walkers conditioned on the internal state of their coins. By choosing their particular case, we systematically study the impact of these interactions on the dynamics of two initially localized and noncorrelated walkers. Our general interaction framework, which reduces to several previously studied models as special cases, provides a versatile platform for engineering quantum correlations with applications in quantum simulation, state preparation, and sensing protocols. It also opens up the possibility of analyzing many-body interactions for larger numbers of walkers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2511.01988v2
- Title: Entropy-based random quantum states
- Authors: Harry J. D. Miller
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.01988v2  pdf=https://arxiv.org/pdf/2511.01988v2.pdf

Abstract:
In quantum information geometry, the curvature of von-Neumann entropy and relative entropy induce a natural metric on the space of mixed quantum states. Here we use this information metric to construct a random matrix ensemble for states and investigate its key statistical properties such as the asymptotic eigenvalue density and mean entropy. We present an algorithm for generating these entropy-based random density matrices, thus providing a new recipe for random state generation that differs from the well established Hilbert-Schmidt and Bures-Hall ensemble approaches. We also prove a duality between the entropy-based state ensemble and a random Hamiltonian model constructed from the thermodynamic length over the set of Gibbs states. This Hamiltonian model is found to display Wigner level repulsion, implying that the dual state ensemble can be realised as a random Gibbs state with respect to a class of chaotic Hamiltonians. As an application we use our model to compute the survival probability of a randomly evolved thermofield double state, predicting a ramp and plateau over time that is characteristic of quantum chaos. For other applications, the entropy-based ensemble can be used as an uninformative prior for Bayesian quantum state or Hamiltonian tomography.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2511.03537v3
- Title: Mutually Unbiased Bases and Orthogonal Latin Squares -- version 3
- Authors: Stefan Joka
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.03537v3  pdf=https://arxiv.org/pdf/2511.03537v3.pdf

Abstract:
In this paper, we prove that the existence of a complete set of mutually unbiased bases (MUBs) in N-dimensional Hilbert space implies the existence of a complete set of mutually orthogonal Latin squares (MOLSs) of order N. In particular, we prove that a complete set of MUBs does not exist in dimension six (the first dimension which is not a power of prime).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2511.07769v3
- Title: Local spreading of stabilizer Rényi entropy in a brickwork random Clifford circuit
- Authors: Somnath Maity, Ryusuke Hamazaki
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2511.07769v3  pdf=https://arxiv.org/pdf/2511.07769v3.pdf

Abstract:
Nonstabilizerness, or magic, constitutes a fundamental resource for quantum computation and a crucial ingredient for quantum advantage. Recent progress has substantially advanced the characterization of magic in many-body quantum systems, with stabilizer Rényi entropy (SRE) emerging as a computable and experimentally accessible measure. In this work, we investigate the spreading of SRE in terms of single-qubit reduced density matrices, where an initial product state that contains magic in a local region evolves under brickwork random Clifford circuits. For the case with Haar-random local Clifford gates, we find that the spreading profile exhibits a diffusive structure within a ballistic light cone when viewed through a normalized version of single-qubit SRE, despite the absence of explicit conserved charges. We further examine the robustness of this non-ballistic behavior of the normalized single-qubit SRE spreading by extending the analysis to a restricted Clifford circuit, where we unveil a superdiffusive spreading. Finally, we discuss that a similar non-ballistic spreading within the light cone is found for another indicator of the magic, i.e., the robustness of magic.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2511.12176v2
- Title: Reinforcement Learning for Charging Optimization of Inhomogeneous Dicke Quantum Batteries
- Authors: Xiaobin Song, Siyuan Bai, Da-Wei Wang, Hanxiao Tao, Xizhe Wang, Rebing Wu, Benben Jiang
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2511.12176v2  pdf=https://arxiv.org/pdf/2511.12176v2.pdf

Abstract:
Charging optimization is a key challenge to the implementation of quantum batteries, particularly under inhomogeneity and partial observability. This paper employs reinforcement learning to optimize piecewise-constant charging policies for an inhomogeneous Dicke battery. We systematically compare policies across four observability regimes, from full-state access to experimentally accessible observables (energies of individual two-level systems (TLSs), first-order averages, and second-order correlations). Simulation results demonstrate that full observability yields near-optimal ergotropy with low variability, while under partial observability, access to only single-TLS energies or energies plus first-order averages lags behind the fully observed baseline. However, augmenting partial observations with second-order correlations recovers most of the gap, reaching 94%-98% of the full-state baseline. The learned schedules are nonmyopic, trading temporary plateaus or declines for superior terminal outcomes. These findings highlight a practical route to effective fast-charging protocols under realistic information constraints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2511.17223v2
- Title: Faithful real embedding of a three-dimensional complex Kochen-Specker configuration
- Authors: Andrei Khrennikov, Karl Svozil
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.17223v2  pdf=https://arxiv.org/pdf/2511.17223v2.pdf

Abstract:
We describe a phase-adjusted realification procedure that embeds any finite set of rays in C^3 into R^3. By assigning an appropriate phase to each ray before applying the standard coordinate-wise map, we can arrange that two rays are orthogonal in C^3 if and only if their images are orthogonal in R^6, so the construction yields a faithful orthogonal representation of the original complex configuration. As a concrete example, we consider the 165 projectively distinct rays used in a C^3 Kochen-Specker configuration obtained from mutually unbiased bases, list these 165 rays explicitly in C^3, and give for each of them its image in R^6 under the canonical realification map. We also note that, because the original 3-element contexts are no longer maximal in R^6, the embedded configuration admits two-valued states even though its realisation with maximal contexts in C^3 is Kochen-Specker uncolourable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2512.07908v3
- Title: Symmetry-Based Quantum Codes Beyond the Pauli Group
- Authors: Zachary P. Bradshaw, Margarite L. LaBorde, Dillon Montero
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2512.07908v3  pdf=https://arxiv.org/pdf/2512.07908v3.pdf

Abstract:
Typical stabilizer codes aim to solve the general problem of fault-tolerance without regard for the structure of a specific system. By incorporating a broader representation-theoretic perspective, we provide a generalized framework that allows the code designer to take this structure into account. For any representation of a finite group, we produce a quantum code with a code space invariant under the group action, providing passive error mitigation against errors belonging to the image of the representation. Furthermore, errors outside this scope are detected and diagnosed by performing a projective measurement onto the isotypic components corresponding to irreducible representations of the chosen group, effectively generalizing syndrome extraction to symmetry-resolved quantum measurements. We show that all stabilizer codes are a special case of this construction, including qudit stabilizer codes, and show that there is a natural one logical qubit code associated to the dihedral group. Thus we provide a unifying framework for existing codes while simultaneously facilitating symmetry-aware codes tailored to specific systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2512.08540v2
- Title: Tunable passive squeezing of squeezed light through unbalanced double homodyne detection
- Authors: Niels Tripier-Mondancin, David Barral, Ganaël Roeland, Raúl Leonardo Rincon Celis, Yann Bouchereau, Nicolas Treps
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2512.08540v2  pdf=https://arxiv.org/pdf/2512.08540v2.pdf

Abstract:
The full characterization of quantum states of light is a central task in quantum optics and information science. Double homodyne detection provides a powerful method for the direct measurement of the Husimi Q quasi-probability distribution, offering a complete state representation in a simple experimental setting and a limited time frame. Here, we demonstrate that double homodyne detection can serve as more than a passive characterization tool. By intentionally unbalancing the input beamsplitter that splits the quantum signal, we show that the detection scheme itself performs an effective squeezing or anti-squeezing transformation on the state being measured. The resulting measurement directly samples the Q function of the input state as if it were acted upon by a squeezing operator whose strength is a tunable experimental parameter: the beamsplitter's reflectivity. We experimentally realize this technique using a robust polarization-encoded double homodyne detection to characterize a squeezed vacuum state. Our results demonstrate the controlled deformation of the measured Q function's phase-space distribution, confirming that unbalanced double homodyne detection is a versatile tool for simultaneous quantum state manipulation and characterization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2512.08921v3
- Title: Autonomous multi-ion optical clock with on-chip integrated photonic light delivery
- Authors: Tharon D. Morrison, Joonhyuk Kwon, Matthew A. Delaney, Michael Gehl, David R. Leibrandt, Daniel Stick, Hayden J. McGuinness
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.08921v3  pdf=https://arxiv.org/pdf/2512.08921v3.pdf

Abstract:
Integrated photonics in trapped-ion systems are critical for the realization of applications such as portable optical atomic clocks and scalable quantum computers. However, system-level integration of all required functionalities remains a key challenge. In this work, we demonstrate an autonomously operating optical clock having a short-term frequency instability of $3.14(5)\times 10^{-14} / \sqrtτ$ using an ensemble of four $^{171}\textrm{Yb}^{+}$ ions trapped in a multi-site surface-electrode trap at room temperature. All clock operations are performed with light delivered via on-chip waveguides. We showcase the system's resilience through sustained, autonomous operation featuring automated ion shuttling and reloading to mitigate ion loss during interleaved clock measurements. This work paves the way beyond component-level functionality to establish a viable and robust architecture for the next generation of portable, multi-ion quantum sensors and computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2512.11499v2
- Title: FRQI Pairs method for image classification using Quantum Recurrent Neural Network
- Authors: Rafał Potempa, Michał Kordasz, Sundas Naqeeb Khan, Krzysztof Werner, Kamil Wereszczyński, Krzysztof Simiński, Krzysztof A. Cyran
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2512.11499v2  pdf=https://arxiv.org/pdf/2512.11499v2.pdf

Abstract:
This study aims to introduce the FRQI Pairs method to a wider audience, a novel approach to image classification using Quantum Recurrent Neural Networks (QRNN) with Flexible Representation for Quantum Images (FRQI). The study highlights an innovative approach to use quantum encoded data for an image classification task, suggesting that such quantum-based approaches could significantly reduce the complexity of quantum algorithms. Comparison of the FRQI Pairs method with contemporary techniques underscores the promise of integrating quantum computing principles with neural network architectures for the development of quantum machine learning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2512.23469v2
- Title: Anisotropic Quantum Annealing vs Trit Annealing
- Authors: M. Haider Akbar, Özgür E. Müstecaplıoğlu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.23469v2  pdf=https://arxiv.org/pdf/2512.23469v2.pdf

Abstract:
Quantum annealing offers a promising strategy for solving complex optimization problems by encoding the solution into the ground state of a problem Hamiltonian. While most implementations rely on spin-$1/2$ systems, we explore the performance of quantum annealing on a spin-$1$ system where the problem Hamiltonian includes a single ion anisotropy term of the form $D\sum (S^z)^2$. Our results reveal that for a suitable range of the anisotropy strength $D$, the spin-$1$ annealer reaches the ground state with higher fidelity. We attribute this performance to the presence of the intermediate spin level and the tunable anisotropy, which together enable the algorithm to traverse the energy landscape through smaller, incremental steps instead of a single large spin flip. This mechanism effectively lowers barriers in the configuration space and stabilizes the evolution. These findings suggest that higher spin annealers offer intrinsic advantages for robust and flexible quantum optimization, especially for problems naturally formulated with ternary decision variables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.00266v2
- Title: Nature is stingy: Universality of Scrooge ensembles in quantum many-body systems
- Authors: Wai-Keong Mok, Tobias Haug, Wen Wei Ho, John Preskill
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; math-ph
- Links: abs=https://arxiv.org/abs/2601.00266v2  pdf=https://arxiv.org/pdf/2601.00266v2.pdf

Abstract:
Recent advances in quantum simulators allow direct experimental access to ensembles of pure states generated by measuring part of an isolated quantum many-body system. These projected ensembles encode fine-grained information beyond thermal expectation values and provide a new window into quantum thermalization. In chaotic dynamics, projected ensembles exhibit universal statistics governed by maximum-entropy principles, known as deep thermalization. At infinite temperature this universality is characterized by Haar-random ensembles. More generally, physical constraints such as finite temperature or conservation laws lead to Scrooge ensembles, which are maximally entropic distributions of pure states consistent with these constraints. Here we introduce Scrooge $k$-designs, which approximate Scrooge ensembles, and use this framework to sharpen the conditions under which Scrooge-like behavior emerges. We first show that global Scrooge designs arise from long-time chaotic unitary dynamics alone, without measurements. Second, we show that measuring a complementary subsystem of a scrambled global state drawn from a global Scrooge $2k$-design induces a local Scrooge $k$-design. Third, we show that a local Scrooge $k$-design arises from an arbitrary entangled state when the complementary system is measured in a scrambled basis induced by a unitary drawn from a Haar $2k$-design. These results show that the resources required to generate approximate Scrooge ensembles scale only with the desired degree of approximation, enabling efficient implementations. Complementing our analytical results, numerical simulations identify coherence, entanglement, non-stabilizerness, and information scrambling as essential ingredients for the emergence of Scrooge-like behavior. Together, our findings advance theoretical explanations for maximally entropic, information-stingy randomness in quantum many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2601.02150v2
- Title: Quantum Extreme Reservoir Computing for Phase Classification of Polymer Alloy Microstructures
- Authors: Arisa Ikeda, Akitada Sakurai, Kae Nemoto, Mayu Muramatsu
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2601.02150v2  pdf=https://arxiv.org/pdf/2601.02150v2.pdf

Abstract:
Quantum machine learning (QML) is expected to offer new opportunities to process high-dimensional data efficiently by exploiting the exponentially large state space of quantum systems. In this work, we apply quantum extreme reservoir computing (QERC) to the classification of microstructure images of polymer alloys generated using self-consistent field theory (SCFT). While previous QML efforts have primarily focused on benchmark datasets such as MNIST, our work demonstrates the applicability of QERC to engineering data with direct materials relevance. Through numerical experiments, we examine the influence of key computational parameters-including the number of qubits, sampling cost (the number of measurement shots), and reservoir configuration-on classification performance. The resulting phase classifications are depicted as phase diagrams that illustrate the phase transitions in polymer morphology, establishing an understandable connection between quantum model outputs and material behavior. These results illustrate QERC performance on realistic materials datasets and suggest practical guidelines for quantum encoder design and model generalization. This work establishes a foundation for integrating quantum learning techniques into materials informatics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2311.12718v3
- Title: Hybrid III-V/Silicon Quantum Photonic Device Generating Broadband Entangled Photon Pairs
- Authors: J. Schuhmann, L. Lazzari, M. Morassi, A. Lemaitre, I. Sagnes, G. Beaudoin, M. I. Amanti, F. Boeuf, et al.
- Categories: physics.optics (primary); physics.optics; cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2311.12718v3  pdf=https://arxiv.org/pdf/2311.12718v3.pdf

Abstract:
The demand for integrated photonic chips combining the generation and manipulation of quantum states of light is steadily increasing, driven by the need for compact and scalable platforms for quantum information technologies. While photonic circuits with diverse functionalities are being developed in different single material platforms, it has become crucial to realize hybrid photonic circuits that harness the advantages of multiple materials while mitigating their respective weaknesses, resulting in enhanced capabilities. Here, we demonstrate a hybrid III-V/Silicon quantum photonic device combining the strong second-order nonlinearity and direct bandgap of the III-V semiconductor platform with the high maturity and CMOS compatibility of the silicon photonic platform. Our device embeds the spontaneous parametric down-conversion (SPDC) of photon pairs into an AlGaAs source and their vertical routing to an adhesively-bonded silicon-on-insulator circuitry, within an evanescent coupling scheme managing both polarization states. This enables the on-chip generation of broadband (> 40 nm) telecom photons by type 0 and type 2 SPDC from the hybrid device, at room temperature and with internal pair generation rates exceeding $10^5$ $s^{-1}$ for both types, while the pump beam is strongly rejected. Two-photon interference with 92% visibility (and up to 99% upon 5 nm spectral filtering) proves the high energy-time entanglement quality of the produced quantum state, thereby enabling a wide range of quantum information applications on-chip, within an hybrid architecture compliant with electrical pumping and merging the assets of two mature and highly complementary platforms in view of out-of-the-lab deployment of quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2412.07676v4
- Title: Bootstrapping, autonomous testing, and initialization system for Si/Si$_x$Ge$_{1-x}$ multi-quantum-dot devices
- Authors: Tyler J. Kovach, Daniel Schug, M. A. Wolfe, E. R. MacQuarrie, Patrick J. Walsh, Owen M. Eskandari, Jared Benson, Mark Friesen, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cs.CV; cs.ET; quant-ph
- Links: abs=https://arxiv.org/abs/2412.07676v4  pdf=https://arxiv.org/pdf/2412.07676v4.pdf

Abstract:
Semiconductor quantum dot (QD) devices have become central to advancements in spin-based quantum computing. However, the increasing complexity of modern QD devices makes calibration and control -- particularly at elevated temperatures -- a bottleneck to progress, highlighting the need for robust and scalable autonomous solutions. A major hurdle arises from trapped charges within the oxide layers, which induce random offset voltage shifts on gate electrodes, with a standard deviation of approximately 83 mV of variation within state-of-the-art present-day devices. Efficient characterization and tuning of large arrays of QD qubits depend on choices of automated protocols. Here, we introduce a physically intuitive framework for a bootstrapping, autonomous testing, and initialization system (BATIS) designed to streamline QD device evaluation and calibration. BATIS navigates high-dimensional gate voltage spaces, automating essential steps such as leakage testing, formation of all current channels, and gate characterization in the presence of trapped charges. For forming the current channels, BATIS follows a non-standard approach that requires a single set of measurements regardless of the number of channels. Demonstrated at 1.3 K on a quad-QD Si/Si$_x$Ge$_{1-x}$ device, BATIS eliminates the need for deep cryogenic environments during initial device diagnostics, significantly enhancing scalability and reducing setup times. By requiring only minimal prior knowledge of the device architecture, BATIS represents a platform-agnostic solution, adaptable to various QD systems, which bridges a critical gap in QD autotuning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2501.12744v2
- Title: Bright and pure single-photon source in a silicon chip by nanoscale positioning of a color center in a microcavity
- Authors: Baptiste Lefaucher, Yoann Baron, Jean-Baptiste Jager, Vincent Calvo, Christian Elsässer, Giuliano Coppola, Frédéric Mazen, Sébastien Kerdilès, et al.
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2501.12744v2  pdf=https://arxiv.org/pdf/2501.12744v2.pdf

Abstract:
We present an all-silicon source of near-infrared linearly-polarized single photons, fabricated by nanoscale positioning of a color center in a silicon-on-insulator microcavity. The color center consists of a single W center, created at a well-defined position by Si$^{+}$ ion implantation through a 150 nm-diameter nanohole in a mask. A circular Bragg grating cavity resonant with the W's zero-phonon line at 1217 nm is fabricated at the same location as the nanohole. By Purcell enhancement of zero-phonon emission, we obtain a photon count rate of $1.29 \pm 0.01$ Mcounts/s at saturation under above-gap continuous-wave excitation with a Debye-Waller factor of $98.6\pm1.4 \%$. A clean photon antibunching behavior is observed up to pump powers ensuring saturation of the W's emission ($g^{(2)}(0)=0.06\pm0.02$ at $P=9.2P_{sat}$), evidencing that the density of additional parasitic fluorescent defects is very low. We also demonstrate the triggered emission of single photons with $93\pm2 \%$ purity under weak pulsed laser excitation. At high pulsed laser power, we reveal a detrimental effect of repumping processes, that could be mitigated using selective pumping schemes in the future. These results represent a major step towards on-demand sources of indistinguishable near-infrared single photons within silicon photonics chips.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2504.07508v3
- Title: Parton Distribution Functions in the Schwinger model from Tensor Network States
- Authors: Mari Carmen Bañuls, Krzysztof Cichy, C. -J. David Lin, Manuel Schneider
- Categories: hep-lat (primary); hep-lat; hep-ph; hep-th; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2504.07508v3  pdf=https://arxiv.org/pdf/2504.07508v3.pdf

Abstract:
Parton distribution functions (PDFs) describe the inner, non-perturbative structure of hadrons. Their computation involves matrix elements with a Wilson line along a direction on the light cone, posing significant challenges in Euclidean lattice calculations, where the time direction is not directly accessible. We propose implementing the light-front Wilson line within the Hamiltonian formalism using tensor network techniques. The approach is demonstrated in the massive Schwinger model (quantum electrodynamics in 1+1 dimensions), a toy model that shares key features with quantum chromodynamics. We present accurate continuum results for the fermion PDF of the vector meson at varying fermion masses, obtained from first-principle calculations directly in Minkowski space. Our strategy also provides a useful path for quantum simulations and quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2505.05174v2
- Title: Steady-state heat engines driven by finite reservoirs
- Authors: Iago N. Mamede, Saulo V. Moreira, Mark T. Mitchison, Carlos E. Fiore
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.other; quant-ph
- Links: abs=https://arxiv.org/abs/2505.05174v2  pdf=https://arxiv.org/pdf/2505.05174v2.pdf

Abstract:
We provide a consistent thermodynamic analysis of stochastic thermal engines driven by finite-size reservoirs, which are in turn coupled to infinite-size reservoirs. We consider a cyclic operation mode, where the working medium couples sequentially to hot and cold reservoirs, and a continuous mode with both reservoirs coupled simultaneously. We derive an effective temperature for the finite-size reservoirs determining the entropy production for two-state engines in the sequential coupling scenario, and show that finite-size reservoirs can meaningfully affect the power when compared to infinite-size reservoirs in both sequential and simultaneous coupling scenarios. We also investigate a three-state engine comprising two interacting units and optimize its performance in the presence of a finite reservoir. Notably, we show that the efficiency at maximum power can exceed the Curzon-Ahlborn bound with finite reservoirs. Our work introduces tools to optimize the performance of nanoscale engines under realistic conditions of finite reservoir heat capacity and imperfect thermal isolation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2509.05942v2
- Title: Theoretical Proposal of a Digital Closed-Loop Thermal Atomic-Beam Interferometer for High-Bandwidth, Wide-Dynamic-Range, and Simultaneous Absolute Acceleration-Rotation Sensing
- Authors: Tomoya Sato, Toshiyuki Hosoya, Martin Miranda, Hiroki Matsui, Yuki Miyazawa, Mikio Kozuma
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2509.05942v2  pdf=https://arxiv.org/pdf/2509.05942v2.pdf

Abstract:
We present a theoretical proposal and simulation study of a digital closed-loop thermal atomic-beam interferometer for inertial navigation applications. The scheme synchronizes phase biasing with momentum-kick reversal through the atomic transit time, extracting four interferometric phases to suppress Raman beam path-length errors, while two-photon detuning feedback maintains a pseudo-inertial frame and eliminates cross-coupling. The interferometer enables simultaneous measurements of acceleration and rotation based on an absolute, atom-interferometric reference, with high bandwidth and a wide dynamic range. Numerical simulations verify that acceleration and angular velocity can be measured simultaneously and independently in real time without cross-coupling, demonstrating the absolute, decoupled nature of the proposed measurement scheme. We further evaluate the noise-limited performance of the sensor and obtain sensitivities of $3{\rm μm / s^2 / \sqrt{Hz}}$ (velocity random walk) and $15{\rm μdeg / \sqrt{h}}$ (angular random walk) for a ${170}^{\circ}$ $^{85}$Rb beam and an interferometer arm length of 100~mm, surpassing the performance of sensors currently used in state-of-the-art inertial navigation systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2509.11797v3
- Title: Modified rational six vertex model on a rectangular lattice : new formula, homogeneous and thermodynamic limits
- Authors: Matthieu Cornillault, Samuel Belliard
- Categories: math-ph (primary); math-ph; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2509.11797v3  pdf=https://arxiv.org/pdf/2509.11797v3.pdf

Abstract:
We continue the work of Belliard, Pimenta and Slavnov (2024) studying the modified rational six vertex model. We find another formula of the partition function for the inhomogeneous model, in terms of a determinant that mix the modified Izergin one and a Vandermonde one. This expression enables us to compute the partition function in the homogeneous limit for the rectangular lattice, and then to study the thermodynamic limit. It leads to a new result, we obtain the first order of free energy with boundary effects in the thermodynamic limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2510.05653v3
- Title: Valley-dependent topological interface states in biased armchair nanoribbons of gapless single-layer graphene for transport applications
- Authors: Zheng-Han Huang, Jing-Yuan Lai, Yu-Shu G. Wu
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2510.05653v3  pdf=https://arxiv.org/pdf/2510.05653v3.pdf

Abstract:
Valley-dependent topological physics offers a promising avenue for designing nanoscale devices based on gapless single-layer graphene. To demonstrate this potential, we investigate an electrical bias-controlled topological discontinuity in valley polarization within a two-segment armchair nanoribbon of gapless single-layer graphene. This discontinuity is created at the interface by applying opposite in-plane, transverse electrical biases to the two segments. An efficient tight-binding theoretical formulation is developed to calculate electron states in the structure. In a reference configuration, we obtain energy eigenvalues and probability distributions that feature interface-confined electron eigenstates induced by the topological discontinuity. Moreover, to elucidate the implications of interface confinement for electron transport, a modified configuration is introduced to transform the eigenstates into transport-active, quasi-localized ones. We show that such states result in Fano "anti-resonances" in transmission spectra. The resilience of these quasi-localized states and their associated Fano fingerprints is examined with respect to fluctuations. Finally, a proof-of-concept band-stop electron energy filter is presented, highlighting the potential of this confinement mechanism and, more broadly, valley-dependent topological physics in designing nanoscale devices in gapless single-layer graphene.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2512.13448v2
- Title: Phase Space Electronic Structure Theory: From Diatomic Lambda-Doubling to Macroscopic Einstein-de Haas
- Authors: Linqing Peng, Tian Qiu, Nadine Bradbury, Xuezhi Bian, Mansi Bhati, Robert Littlejohn, Nathanael M. Kidwell, Joseph E. Subotnik
- Categories: physics.chem-ph (primary); physics.chem-ph; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2512.13448v2  pdf=https://arxiv.org/pdf/2512.13448v2.pdf

Abstract:
$Λ$-doubling of diatomic molecules is a subtle microscopic phenomenon that has long attracted the attention of experimental groups, insofar as rotation of molecular $\textit{nuclei}$ induces small energetic changes in the (degenerate) $\textit{electronic}$ state. A direct description of such a phenomenon clearly requires going beyond the Born-Oppenheimer approximation. Here we show that a phase space theory previously developed to capture electronic momentum and model vibrational circular dichroism -- and which we have postulated should also describe the Einstein-de Haas effect, a macroscopic manifestation of angular momentum conservation -- is also able to recover the $Λ$-doubling energy splitting (or $Λ$-splitting) of the NO molecule nearly quantitatively. The key observation is that, by parameterizing the electronic Hamiltonian in terms of both nuclear position ($\mathbf{X}$) and nuclear momentum ($\mathbf{P}$), a phase space method yields potential energy surfaces that explicitly include the electron-rotation coupling and correctly conserve angular momentum (which we show is essential to capture $Λ-$doubling). The data presented in this manuscript offers another small glimpse into the rich physics that one can learn from investigating phase space potential energy surfaces $E_{PS}(\mathbf{X},\mathbf{P})$ as a function of both nuclear position and momentum, all at a computational cost comparable to standard Born-Oppenheimer electronic structure calculations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-27 09:48
- arXiv: 2512.14495v2
- Title: Multimode Jahn-Teller Effect in Negatively Charged Nitrogen-Vacancy Center in Diamond
- Authors: Jianhua Zhang, Jun Liu, Z. Z. Zhu, K. M. Ho, V. V. Dobrovitski, C. Z. Wang
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2512.14495v2  pdf=https://arxiv.org/pdf/2512.14495v2.pdf

Abstract:
We present a first-principles study of the multimode Jahn-Teller (JT) effect in the exctied $^{3}E$ state of the negatively charged nitrogen-vacancy (NV) center in diamond. Using density functional theory combined with an intrinsic distortion path (IDP) analysis, we resolve the full activation pathways of the JT distortion and quantitatively decompose the distortion into contributions from individual vibrational modes. We find that multiple vibrational modes participate cooperatively in the JT dynamics, giving rise to a shallow adiabatic potential energy surface with low barriers, consistent with thermally activated pseudorotation. The dominant JT-active modes are found to closely correspond to vibrational features observed in two-dimensional electronic spectroscopy (2DES), in agreement with recent ab initio molecular dynamics simulations. Our results establish a microscopic, mode-resolved picture of vibronic coupling in the excited-state NV center and provide new insight into dephasing, relaxation, and optically driven dynamics relevant to solid-state quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17070v1
- Title: The Double Covariance Model: A Stochastic Reconstruction of Quantum Entangled States via Interplay of Micro-Macro Time Scales
- Authors: Andrei Khrennikov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17070v1  pdf=https://arxiv.org/pdf/2601.17070v1.pdf

Abstract:
This article presents a concrete mathematical framework for the generation of entangled quantum states from classical stochastic processes. We demonstrate that any density operator $ρ_{AB}$ of a composite system can be derived from the correlations between two underlying stochastic processes, $X(t)$ and $Y(t)$, representing the random fluctuations of its subsystems. This construction utilizes a two-scale temporal scheme - micro and macro time - where quantum correlations emerge as macro-correlations derived from underlying micro-correlations. We propose the Double Covariance Model (DCM), which reproduces the fundamental properties of quantum theory by treating the quantum state as the fourth-order moment structure of an underlying classical probability space.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17208v1
- Title: A pedagogical derivation of the first-order effective Hamiltonian for the two-mode Jaynes-Cummings model
- Authors: Alejandro R. Urzúa
- Categories: quant-ph (primary); quant-ph; physics.ed-ph
- Links: abs=https://arxiv.org/abs/2601.17208v1  pdf=https://arxiv.org/pdf/2601.17208v1.pdf

Abstract:
This work presents a pedagogical and self-contained derivation of the first-order effective Hamiltonian for the two-mode Jaynes-Cummings model in the dispersive regime. A perturbative unitary transformation removes nonresonant atom-field terms, revealing dispersive frequency shifts leading to an atom-induced effective beam-splitter interaction between the field modes. The resulting Hamiltonian is diagonalized through a simple geometric rotation in the two-mode bosonic space, providing a transparent interpretation of the underlying dynamics. The exposition emphasized clarity and physical insight, making effective Hamiltonian methods accessible for teaching and learning in multimode light-matter interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17384v1
- Title: The Universe as a Detector: A Quantum Filtering Formulation of the Diósi-Penrose Model
- Authors: John Gough, Dylon Rees
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2601.17384v1  pdf=https://arxiv.org/pdf/2601.17384v1.pdf

Abstract:
We consider the Diósi-Penrose problem but rather than postulating background gravitational fluctuations, we instead consider the quantum filter that arises from space-time homodyning the continuum of output quadrature described in the open quantum stochastic model presented here. This is described by a quantum Kushner-Stratonovich equation, typical of the form appearing in continuous-time collapse of the wave-function models in Quantum Decoherence Theory

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17394v1
- Title: Non-Markovian Decoherence Times in Finite-Memory Environments
- Authors: Ramandeep Dewan
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2601.17394v1  pdf=https://arxiv.org/pdf/2601.17394v1.pdf

Abstract:
Decoherence is often modeled using Markovian master equations that predict exponential suppression of coherence and are frequently used as effective bounds on quantum behavior in complex environments. Such descriptions, however, correspond to the singular physical limit of vanishing environmental memory. Here we formulate decoherence using a general time-nonlocal decoherence functional determined solely by the environmental force correlation function, with Markovian dynamics recovered explicitly as a limiting case.   For arbitrary stationary environments with finite temporal correlations, we show that the decoherence functional exhibits quadratic short-time growth that is model-independent within the finite-memory class considered. Consequently, the decoherence time defined operationally-without assuming exponential decay-scales as the square root of the environmental correlation time, independent of the detailed form of the bath correlation kernel.   These results are illustrated analytically for Gaussian-correlated, soft power-law, and Ornstein-Uhlenbeck environments. In the Ornstein-Uhlenbeck case, the non-Markovian dynamics admit an exact analytical closure, yielding a closed evolution equation for the coherence. Exact numerical simulations based on a pseudomode mapping confirm the predicted scaling and show that exponential decoherence emerges only in the memoryless limit.   Beyond coherence decay, we distinguish decoherence rates from observable loss of quantum signatures by analyzing purity and von Neumann entropy dynamics. We show that suppression of a specific coherence element need not coincide with irreversible entropy production. Finally, we introduce an inferred-memory perspective in which the environmental correlation time is treated as an operationally extractable parameter from dynamical data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17459v1
- Title: Qhronology: A Python package for studying quantum models of closed timelike curves
- Authors: Lachlan G. Bishop
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2601.17459v1  pdf=https://arxiv.org/pdf/2601.17459v1.pdf

Abstract:
Qhronology is a novel scientific-computing package for studying quantum models of closed timelike curves (CTCs) and simulating general quantum information processing and computation. Written in Python, the program provides a comprehensive framework for analyzing quantum theories of antichronological time travel, including functionality to calculate quantum resolutions to temporal paradoxes. It also operates as a complete quantum circuit simulator, enabling the examination of quantum algorithms and protocols in both numerical and symbolic capacities. In this paper, we formally introduce Qhronology, beginning with discussion on aspects of its design philosophy and architecture. An overview of its basic usage is then presented, along with a collection of examples demonstrating its various capabilities within a variety of distinct contexts. Lastly, the performance of the package's circuit simulation component is characterized by way of some simple empirical benchmarking.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17465v1
- Title: Bayesian quantum sensing using graybox machine learning
- Authors: Akram Youssry, Stefan Todd, Patrick Murton, Muhammad Junaid Arshad, Alberto Peruzzo, Cristian Bonato
- Categories: quant-ph (primary); quant-ph; cs.LG; eess.SP
- Links: abs=https://arxiv.org/abs/2601.17465v1  pdf=https://arxiv.org/pdf/2601.17465v1.pdf

Abstract:
Quantum sensors offer significant advantages over classical devices in spatial resolution and sensitivity, enabling transformative applications across materials science, healthcare, and beyond. Their practical performance, however, is often constrained by unmodelled effects, including noise, imperfect state preparation, and non-ideal control fields.   In this work, we report the first experimental implementation of a graybox modelling strategy for a solid-state open quantum system. The graybox framework integrates a physics-based system model with a data-driven description of experimental imperfections, achieving higher fidelity than purely analytical (whitebox) approaches while requiring fewer training resources than fully deep-learning models. We experimentally validate the method on the task of estimating a static magnetic field using a single-spin quantum sensor, performing Bayesian inference with a graybox model trained on prior experimental data. Using roughly 10,000 training datapoints, the graybox model yields several orders of magnitude improvement in mean squared error over the corresponding physics-only model. These results are broadly applicable to a wide range of quantum sensing platforms, not limited to single-spin systems, and are particularly valuable for real-time adaptive protocols, where model inaccuracies can otherwise lead to suboptimal control and degraded performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17514v1
- Title: Are Quantum Voting Protocols Practical?
- Authors: Nitin Jha, Abhishek Parakh
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2601.17514v1  pdf=https://arxiv.org/pdf/2601.17514v1.pdf

Abstract:
Quantum voting protocols aim to offer ballot secrecy and publicly verifiable tallies using physical guarantees from quantum mechanics, rather than relying solely on computational hardness. This article surveys whether such quantum voting protocols are practical. We begin by outlining core mathematical ideas such as the superposition principle, the no-cloning theorem, and quantum entanglement. We then define a common system and threat model, identifying key actors, trust assumptions, and security goals. Representative protocol families are reviewed, including entanglement-based schemes with central tallying, self-tallying designs that enable public verification, and authority-minimized approaches that certify untrusted devices through observable correlations. Finally, we evaluate implementation challenges, including loss, noise, device imperfections, scalability, and coercion resistance, and discuss realistic near-term deployment scenarios for small-scale elections.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17515v1
- Title: Quantum Phase Transitions in the Transverse-Field Ising Model: A Comparative Study of Exact, Variational, and Hardware-Based Approaches
- Authors: Rudraksh Sharma
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17515v1  pdf=https://arxiv.org/pdf/2601.17515v1.pdf

Abstract:
The quantum phase transitions provide a paradigm for studying collective quantum phenomena that are a result of competing non-commuting interactions. This paper will study the ground state properties and quantum critical dynamics of the one-dimensional transverse field Ising model through a combined perspective that includes exact diagonalisation, variational quantum eigensolver (VQE) simulations, and simulations on realistic physical quantum devices. We focus on a lattice of four spins, where we calculate the ground-state energies, magnetic order parameters and correlation functions at uniformly applied conditions, which is repeated by all systems. Precise diagonalisation provides both a benchmark, which is symmetry-conserving, and a depth-two, physics inspired variational approximation, which provides simulations accessible to hardware. The circuits that have been optimised identically are then placed on the IQM Garnet quantum processor, using a resource-efficient batched protocol. We find that the ground-state energies of shallow variational circuits are reliably captured by the circuit over the entire parameter space; the magnetic arrangement parameters and observables sensitive to correlation signal significantly more noise. The error analysis of quantitative analysis reveals a strong broadening of critical crossover on hardware, which is consistent with the noise attenuation of long-range correlations. These findings highlight the current capabilities as well as the fundamental limitations of noisy intermediate-scale quantum systems in modelling quantum critical phenomena as a benchmark to future enhancements in obtaining quantum hardware and quantum algorithms development.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17552v1
- Title: Autonomous phonon maser in levitated spin-mechanics
- Authors: Mohamed Hatifi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17552v1  pdf=https://arxiv.org/pdf/2601.17552v1.pdf

Abstract:
Levitated nanodiamonds hosting a single nitrogen-vacancy (NV) center provide an ultra-low-frequency mechanical mode with widely tunable dissipation and spin backaction under microwave dressing and optical pumping. We demonstrate that the driven NV spin can be tuned to act as an inverted gain medium for the center-of-mass motion, thereby stabilizing an autonomous phonon maser. In the separation-of-timescales regime where spin dynamics is fast, adiabatic elimination yields a reduced mechanical master equation with closed-form, detuning-dependent transition rates and a sharp threshold given by the sign change of the phonon-number damping. For representative levitated-NV parameters, we find that a percent-level dressed-basis inversion is sufficient to reach the threshold, and the small-signal gain can exceed the intrinsic mechanical loss by orders of magnitude. Full master-equation simulations confirm above-threshold self-oscillation and a phase-diffusing, coherent steady state, whose saturation follows the Maxwell-Bloch prediction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17580v1
- Title: PropHunt: Automated Optimization of Quantum Syndrome Measurement Circuits
- Authors: Joshua Viszlai, Satvik Maurya, Swamit Tannu, Margaret Martonosi, Frederic T. Chong
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17580v1  pdf=https://arxiv.org/pdf/2601.17580v1.pdf

Abstract:
Fault-Tolerant Quantum Computing (FTQC) relies on Quantum Error Correction (QEC) codes to reach error rates necessary for large scale quantum applications. At a physical level, QEC codes perform parity checks on data qubits, producing syndrome information, through Syndrome Measurement (SM) circuits. These circuits define a code's logical error rate and must be run repeatedly throughout the entire program. The performance of SM circuits is therefore critical to the success of a FTQC system.   While ultimately implemented as physical circuits, SM circuits have challenges that are not addressed by existing circuit optimization tools. Importantly, inside SM circuits themselves errors are expected to occur, and how errors propagate through SM circuits directly impacts which errors are detectable and correctable, defining the code's logical error rate. This is not modeled in NISQ-era tools, which instead optimize for targets such as gate depth or gate count to mitigate the chance that any error occurs. This gap leaves key questions unanswered about the expected real-world effectiveness of QEC codes.   In this work we address this gap and present PropHunt, an automated tool for optimizing SM circuits for CSS codes. We evaluate PropHunt on a suite of relevant QEC codes and demonstrate PropHunt's ability to iteratively improve performance and recover existing hand-designed circuits automatically. We also propose a near-term QEC application, Hook-ZNE, which leverages PropHunt's fine-grained control over logical error rate to improve Zero-Noise Extrapolation (ZNE), a promising error mitigation strategy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17592v1
- Title: Holstein Primakoff spin codes for local and collective noise
- Authors: Sivaprasad Omanakuttan, Tyler Thurtell, Andrew K. Forbes, Vikas Buchemmavari, Ben Q. Baragiola
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2601.17592v1  pdf=https://arxiv.org/pdf/2601.17592v1.pdf

Abstract:
Quantum error correction is essential for fault-tolerant quantum computation, yet most existing codes rely on local control and stabilizer measurements that are difficult to implement in systems dominated by collective interactions. Inspired by spin-GKP codes in PhysRevA.108.022428, we develop a general framework for Holstein-Primakoff spin codes, which maps continuous-variable bosonic codes onto permutation-symmetric spin ensembles via the Holstein-Primakoff approximation. We show that HP codes are robust to both collective and local-spin noise and propose an explicit measurement-free local error recovery procedure to map local noise into correctable collective-spin errors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17659v1
- Title: Generalized Aharonov-Bohm Effect
- Authors: Shan Gao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17659v1  pdf=https://arxiv.org/pdf/2601.17659v1.pdf

Abstract:
The Aharonov-Bohm (AB) effect highlights the fundamental role of electromagnetic potentials in quantum mechanics, manifesting as a phase shift for a charged particle in field-free regions. While well-established for static magnetic fluxes, the effect's behavior under time-varying fluxes remains an open and debated question. Employing the WKB method, we derive the AB phase shift for a time-dependent magnetic vector potential, demonstrating that for circular paths in the quasistatic regime, it is proportional to the time-averaged enclosed magnetic flux, \(Δφ_{\rm AB} = \frac{1}{T} \int_0^T e Φ(t) \, dt\), with the total phase shift, including kinetic contributions, equaling \(e Φ(0)\). For non-circular paths, the phase shift depends on both the flux history and path geometry, revealing the effect's hybrid nature involving gauge potentials and induced electric fields. We verify the consistency of our gauge choice with Maxwell's equations and discuss the implications for local versus nonlocal interpretations of the AB effect. We also generalize the results to scenarios with nonzero external magnetic fields, where the enclosed flux is through the actual electron paths, and for circular paths of radius $R$, the AB phase shift is also proportional to the time average of the enclosed flux \(Φ_{\rm enc}(R,t)\), with the total phase shift depending only on the initial enclosed flux \(e Φ_{\rm enc}(R,0)\); for general non-circular paths, the external magnetic field affects trajectories and phase accumulation through the Lorentz force, leading to additional path dependence. These findings clarify the role of gauge-dependent potentials and induced fields in the generalized AB effect, offering new theoretical insights and potential applications in quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17662v1
- Title: From Joint to Single-System Psi-Onticity Without Preparation Independence
- Authors: Shan Gao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17662v1  pdf=https://arxiv.org/pdf/2601.17662v1.pdf

Abstract:
The Pusey-Barrett-Rudolph (PBR) theorem establishes $ψ$-onticity for individual quantum systems, but its standard formulation relies on the Preparation Independence Postulate (PIP). This has led to a prevalent view that rejecting PIP leaves open the possibility of $ψ$-epistemic models for individual systems. In this work, we show that this understanding is incomplete: once the PBR theorem establishes $ψ$-onticity for composite systems prepared in product states, the $ψ$-onticity of the individual subsystems follows directly from the tensor-product structure of quantum mechanics, without invoking PIP or any further auxiliary assumptions. This result removes a key auxiliary assumption from the PBR theorem, closes a persistent loophole for preserving $ψ$-epistemic models, and strengthens the conceptual foundations of $ψ$-ontology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17665v1
- Title: Comment on "Aharonov-Bohm Phase is Locally Generated Like All Other Quantum Phases"
- Authors: Shan Gao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17665v1  pdf=https://arxiv.org/pdf/2601.17665v1.pdf

Abstract:
Marletto and Vedral [Phys. Rev. Lett. 125, 040401 (2020)] propose that the Aharonov-Bohm (AB) phase is locally mediated by entanglement between a charged particle and the quantized electromagnetic field, asserting gauge independence for non-closed paths. In this Comment, we critically analyze their model and demonstrate that the AB phase arises from the interaction with the vector potential \(\mathbf{A}\), not from entanglement, which is a byproduct of the quantum electrodynamics (QED) framework. We show that their field-based energy formulation, intended to reflect local electromagnetic interactions, is mathematically flawed due to an incorrect prefactor and yields \( +q \mathbf{v} \cdot \mathbf{A}_{\mathbf{s}} \) in the Coulomb gauge, conflicting with QED's \( -q \mathbf{v} \cdot \mathbf{A}_{\mathbf{s}} \). This equivalence to \( q \mathbf{v} \cdot \mathbf{A}_{\mathbf{s}} \) holds only approximately in the Coulomb gauge under static conditions, failing for time-dependent fields and other gauges, undermining their claim of a gauge-independent local mechanism. Furthermore, we confirm that the AB phase is gauge-dependent for non-closed paths, contradicting their assertion. Our analysis reaffirms the conventional explanation in the semi-classical picture, where the AB phase is driven by the vector potential \(\mathbf{A}\), with entanglement playing no causal role in its generation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17675v1
- Title: Realisation of Protected Cat Qutrit via Engineered Quantum Tunnelling
- Authors: Sangil Kwon, Daisuke Hoshi, Toshiaki Nagase, Daichi Sugiyama, Hiroto Mukai, Kengo Takemura, Rintaro Kojima, Yu Zhou, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17675v1  pdf=https://arxiv.org/pdf/2601.17675v1.pdf

Abstract:
Engineering quantum tunnelling in phase space has emerged as a viable method for creating a protected qubit with biased-noise properties. A promising approach is to combine a Kerr nonlinearity with multi-photon transitions, resulting in a system known as a Kerr parametric oscillator (KPO). In this work, we implement a three-photon KPO and explore its potential as a protected qutrit. We confirm quantum coherence by demonstrating three-photon Rabi oscillations and performing direct Wigner function measurements that reveal three-component cat-like states. We observe breathing-like dynamics in phase space, arising from exotic temporal interference between the qutrit and excited states. The frequency of this interference corresponds to the energy gap between the qutrit and excited manifolds, thereby providing an experimental hallmark of qutrit space protection. We also identify a higher-order pump term as the main mechanism suppressing photon occupation; mitigating this term is necessary to maximize protection. Our findings elucidate the basic quantum properties of the three-photon KPO and establish the first step toward its use as an alternative qutrit platform.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17686v1
- Title: Exponential Quantum Speedup on Structured Hard Instances of Maximum Independent Set
- Authors: Vicky Choi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17686v1  pdf=https://arxiv.org/pdf/2601.17686v1.pdf

Abstract:
Establishing quantum speedup for computationally hard problems of practical relevance, particularly combinatorial optimization problems, remains a central challenge in quantum computation. In this work, we identify a structurally defined family of classically hard maximum independent set (MIS) instances, and design and analyze a non-stoquastic adiabatic quantum optimization algorithm that exploits this structure. The algorithm runs in polynomial time and achieves an exponential speedup over both transverse-field quantum annealing and state-of-the-art classical solvers on these instances, under assumptions supported by analytical and numerical evidence. We identify the essential quantum mechanism enabling the speedup as the use of a non-stoquastic XX-driver to access a larger sign-structured admissible subspace beyond the stoquastic regime, which allows sign-generating quantum interference to create smooth evolution paths that bypass tunneling. This identifies a distinctive quantum mechanism underlying the speedup and explains why no efficient classical analogue is likely to exist. In addition, our analysis produces scalable small-scale models, derived from our structural reduction, that capture the essential dynamics of the algorithm. These models provide a concrete opportunity for verification of the quantum advantage mechanism on currently available universal quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17688v1
- Title: Traversability dynamics of minimal Sachdev-Ye-Kitaev Wormhole-inspired teleportation protocol with a parity-time ($\mathcal{PT}$)-symmetric non-Hermitian deformation
- Authors: Sudhanva Joshi, Sunil Kumar Mishra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17688v1  pdf=https://arxiv.org/pdf/2601.17688v1.pdf

Abstract:
Holography-inspired teleportation has recently emerged as a significant area of research in quantum many-body systems. In this work, we investigate the effects of $\mathcal{PT}$ symmetric non-unitary deformations on the traversability of the wormhole-inspired teleportation protocol modeled by coupled Sachdev-Ye-Kitaev systems prepared in a Thermofield Double state bath. By introducing balanced gain and loss terms to the boundary Hamiltonians, we identify a phase transition driven by spectral exceptional points, where the real energy eigenvalues of the effective Hamiltonian coalesce and bifurcate into complex conjugate pairs. We demonstrate that the $\mathcal{PT}$-broken phase acts as an amplifier, enabling exponential growth in the norm of the teleported signal while preserving the causal time window for the wormhole's traversability. A statistical study of disorder realizations reveals that the critical non-Hermiticity threshold $γ_c$ follows a log-normal distribution, reflecting the sensitivity of the transition to the microscopic level spacing of the chaotic SYK spectrum. Furthermore, we observe a ``Purification" effect deep in the broken phase, where the teleportation channel acts as an entanglement distiller, yielding near-perfect teleportation fidelity for post-selected states. Our results suggest that the non-Hermitian topology can be harnessed to enhance holographic quantum communication, providing a robust mechanism for signal amplification in noisy, minimal quantum many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17724v1
- Title: Quantum-Inspired Algorithms beyond Unitary Circuits: the Laplace Transform
- Authors: Noufal Jaseem, Sergi Ramos-Calderer, Gauthameshwar S., Dingzu Wang, José Ignacio Latorre, Dario Poletti
- Categories: quant-ph (primary); quant-ph; math-ph; physics.data-an
- Links: abs=https://arxiv.org/abs/2601.17724v1  pdf=https://arxiv.org/pdf/2601.17724v1.pdf

Abstract:
Quantum-inspired algorithms can deliver substantial speedups over classical state-of-the-art methods by executing quantum algorithms with tensor networks on conventional hardware. Unlike circuit models restricted to unitary gates, tensor networks naturally accommodate non-unitary maps. This flexibility lets us design quantum-inspired methods that start from a quantum algorithmic structure, yet go beyond unitarity to achieve speedups. Here we introduce a tensor-network approach to compute the discrete Laplace transform, a non-unitary, aperiodic transform (in contrast to the Fourier transform). We encode a length-$N$ signal on two paired $n$-qubit registers and decompose the overall map into a non-unitary exponential Damping Transform followed by a Quantum Fourier Transform, both compressed in a single matrix-product operator. This decomposition admits strong MPO compression to low bond dimension resulting in significant acceleration. We demonstrate simulations up to $N=2^{30}$ input data points, with up to $2^{60}$ output data points, and quantify how bond dimension controls runtime and accuracy, including precise and efficient pole identification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17725v1
- Title: Reducing Circuit Resources in Grover's Algorithm via Constraint-Aware Initialization
- Authors: Eunok Bae, Jeonghyeon Shin, Minjin Choi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17725v1  pdf=https://arxiv.org/pdf/2601.17725v1.pdf

Abstract:
Grover's search algorithm provides a quadratic speedup over classical brute-force search in terms of query complexity and is widely used as a versatile subroutine in numerous quantum algorithms, including those for combinatorial problems with large search spaces. For such problems, it is natural to reduce the effective search space by incorporating problem constraints at the initialization step, which in Grover's algorithm can be achieved by preparing structured initial states that encode constraint information. In this work, we present a systematic framework with a simple preprocessing procedure for constraint-aware initialization in Grover's algorithm, focusing on problems with linear constraints. While such structured initial states can reduce the number of oracle queries required to obtain a solution, their preparation incurs additional circuit-level costs. We therefore offer a conservative circuit-level resource analysis, showing that the resulting constraint-aware initialization can improve resource efficiency in terms of gate counts and circuit depth. The validity of the framework is further demonstrated numerically using the exact-cover problem. Overall, our results indicate that this approach serves as a practical baseline for achieving more resource-efficient implementations of Grover's algorithm compared to the standard uniform initialization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17732v1
- Title: Quantum fast-forwarding fermion-boson interactions via the polaron transform
- Authors: Harriet Apel, Burak Şahinoğlu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17732v1  pdf=https://arxiv.org/pdf/2601.17732v1.pdf

Abstract:
Simulating interactions between fermions and bosons is central to understanding correlated phenomena, yet these systems are inherently difficult to treat classically. Previous quantum algorithms for fermion-boson models exhibit computation costs that scale polynomially with the bosonic truncation parameter, $Λ$. In this work we identify the efficient unitary transformation enabling fast-forwarded evolution of the fermion-boson interaction term, yielding an interaction-picture based simulation algorithm with complexity polylogarithmic in $Λ$. We apply this transformation to explicitly construct an efficient quantum algorithm for the Hubbard-Holstein model and discuss its generalisation to other fermion-boson interacting models. This approach yields an important asymptotic improvement in the dependence on the bosonic cutoff and establishes that, for certain models, fermion-boson interactions can be simulated with resources comparable to those required for purely fermionic systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17757v1
- Title: Simple, Efficient, and Generic Post-Selection Decoding for qLDPC codes
- Authors: Haipeng Xie, Nobuyuki Yoshioka, Kento Tsubouchi, Ying Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17757v1  pdf=https://arxiv.org/pdf/2601.17757v1.pdf

Abstract:
Quantum error correction is indispensable for scalable quantum computation. Although encoding logical qubits substantially enhances noise resilience, achieving logical error rates low enough for practical algorithms remains challenging on existing hardware. Here we introduce argument reweighting, a simple and broadly applicable post-selection decoding strategy that boosts the performance of maximum-likelihood-type decoders, including minimum-weight perfect matching and belief-propagation families. The method suppresses logical errors by performing additional decoding rounds under reweighted error models, enabling acceptance of high-confidence syndrome outcomes. Circuit-level simulations across multiple decoders and qLDPC codes show that argument reweighting substantially suppresses logical errors, requiring a rejection rate of only $1.44\times10^{-5}$ to reduce the logical error rate by almost two orders of magnitude for the $[[144,12,12]]$ bivariate bicycle code. These results establish argument reweighting as a practical and resource-efficient approach for enhancing quantum fault tolerance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17788v1
- Title: Kirkwood-Dirac Quasiprobability as a Universal Framework for Quantum Measurements Across All Regimes
- Authors: Bo Zhang, Yusuf Turek
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17788v1  pdf=https://arxiv.org/pdf/2601.17788v1.pdf

Abstract:
The question of when the Kirkwood-Dirac quasiprobability serves as the most appropriate description for quantum measurements has remained unresolved, particularly across different measurement strengths. While known to generate anomalous weak values in the weak measurement regime and to reduce to classical probabilities under projective measurement, the physical mechanism governing its continuous transformation has been lacking. Here we demonstrate that the KD quasiprobability provides a general framework for all measurement regimes by identifying pointer-induced decoherence as the universal mechanism controlling this transition. We show that the decoherence factor F(t) simultaneously quantifies the loss of quantum coherence and interpolates the measurement strength from weak to strong. Within this framework, the KD quasiprobability naturally deforms from its full complex form-governing weak values-to the real, non-negative Wigner formula describing projective measurements, while maintaining informational completeness throughout the transition. Our work resolves the fundamental question of the KD distribution's applicability by establishing it as the universal framework that seamlessly connects all quantum measurement regimes through a physically transparent decoherence pathway.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17804v1
- Title: Bosonic Diffusive Channel: Quantum Metrology via Finite Non-Gaussian Resource
- Authors: Arman, Prasanta K. Panigrahi
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.17804v1  pdf=https://arxiv.org/pdf/2601.17804v1.pdf

Abstract:
We investigate the estimation of dephasing-induced decoherence in continuous-variable quantum systems using non-Gaussian probe states. By purifying the open system, we identify optimal probes, specifically squeezed cat and symmetric squeezed compass states, via quantum Fisher information. These results are in agreement with numerical simulation. In settings where the intra-cavity field is inaccessible and standard measurements are impractical, utilizing an ancilla approach where a qubit traverses or interacts with the cavity field, leading to measurement of the qubit, hence allowing estimation of the dephasing rate via Wigner function reconstruction or less costly marginal distribution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17819v1
- Title: Experimental Phase-Matching Quantum Cryptographic Conferencing in Symmetric and Asymmetric Fiber Channels
- Authors: Mi Zou, Bin-Chen Li, Shuai Zhao, Yingqiu Mao, Dandan Qin, Xiao Jiang, Teng-Yun Chen, Jian-Wei Pan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17819v1  pdf=https://arxiv.org/pdf/2601.17819v1.pdf

Abstract:
Quantum cryptographic conferencing (QCC) allows multiple parties to establish common secure keys in quantum networks with information-theoretic security. However, the secure transmission distances of current QCC implementations are still limited to the metropolitan areas. Here, we experimentally demonstrate the three-intensity phase-matching (PM) QCC protocol considering finite-size effects by employing frequency-locking and phase-tracking techniques for three parties. The key distribution capability of the PM QCC protocol is demonstrated in the symmetric fiber channels with the distance from each party to the measurement site up to 100 km. The network adaptability of the PM QCC protocol is demonstrated in asymmetric fiber channels used to simulate fiber channel configurations in real networks. Thus, the feasibility of applying the PM QCC protocol to practical intercity quantum networks with both symmetric and asymmetric channels is verified.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17850v1
- Title: Multivariate Rényi divergences characterise betting games with multiple lotteries
- Authors: Andrés F. Ducuara, Erkka Haapasalo, Ryo Takakura
- Categories: quant-ph (primary); quant-ph; math.PR
- Links: abs=https://arxiv.org/abs/2601.17850v1  pdf=https://arxiv.org/pdf/2601.17850v1.pdf

Abstract:
We provide an operational interpretation of the multivariate Rényi divergence in terms of economic-theoretic tasks based on betting, risk aversion, and multiple lotteries. We show that the multivariate Rényi divergence $D_{\underlineα}(\vec{P}_X)$ of probability distributions $\vec{P}_X =(p^{(0)}_X,\dots,p^{(d)}_X)$ and real-valued orders $\underlineα = (α_0, \dots, α_d)$ quantifies the economic-theoretic value that a rational agent assigns to $d$ lotteries with odds $o^{(k)}_X \propto (p_X^{(k)})^{-1}$ ($k=1,\dots,d$) on a random event described by $p^{(0)}_X$. In particular, when the odds are fair and the rational agent maximises over all betting strategies, the economic-theoretic value (the isoelastic certainty equivalent) that the agent assigns to the lotteries is exactly given by $w^{\mathrm{ICE}}_{\underline{R}}=\exp[D_{\underlineα}(\vec{P}_X)]$, where $\underline{R}=(R_1,\dots,R_d)$ is a risk-aversion vector with $R_k = 1+α_k/α_0$ being the risk-aversion parameter for lottery $k$. Furthermore, we introduce a new conditional multivariate Rényi divergence that characterises a generalised scenario where the agent uses side information. We prove that this new quantity satisfies a data processing inequality which can be interpreted as the increment in the economic-theoretic value provided by side information; crucially, such a data processing inequality is a consequence of the agent's economic-theoretically consistent risk-averse attitude towards every lottery and vice versa. Finally, we apply these results to the resource theory of informative measurements in general probabilistic theories (GPTs). By establishing quantitative connections between information theory, physics, and economics, our framework provides a novel operational foundation for quantum state betting games with multiple lotteries in the realm of quantum resource theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17856v1
- Title: On Tunneling in the Quantum Multiverse
- Authors: S. E. Ennadifi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17856v1  pdf=https://arxiv.org/pdf/2601.17856v1.pdf

Abstract:
Prompted by the longstanding interpretational controversy in quantum mechanics, quantum tunneling is heuristically addressed within the Everettian quantum multiverse. In this framework, the universal wavefunction splits into decohered reflected and transmitted branches under the environmetal effect after encountring a potential barrier. The observed tunneling is then experienced by the observer located in a tunneled world. The tunneling probability and the tunneling time are investigated in terms of the tunneled world relative weights and the branching duration, respectively. The macroscopic quantum tunneling, recently honored, is also discussed and the corresponding macroscopic tunneling time is approached based on the obtained results and known data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17870v1
- Title: Quantum Machine Learning Using Quantum Illumination With Quantum Enhanced Interference
- Authors: Pallab Biswas, Tamal Maity
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17870v1  pdf=https://arxiv.org/pdf/2601.17870v1.pdf

Abstract:
Quantum Machine Learning(QML) is developed by combining quantum mechanics principles with classical machine learning techniques in a hybrid framework that can give faster, exponential, more efficient power of quantum computing with the data driven intelligence. Quantum illumination(QI) is the quantum mechanical technique along with analysis of light matter interaction from source to detection end that connects quantum principle to hardware implementation. Superposition and entanglement control are deeply needed for the information-qubit processing in quantum computing. Improvement of measurement and performance are directly linked to detecting weak signal or intensity. This paper motivated that using quantum-enhanced technique how we can analysis previous superposition of qubit state which can clearly analyzed quantum interference diffraction patterns and its superposition using double slit experiment. Then constructed quantum neural network back propagation technique such that can give information of qubit position in any previous superposition state. Which is very import for any quantum optimization and search algorithm.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17876v1
- Title: Coherent Amplifier-Empowered Quantum Interferometer: Preserving Sensitivity and Quantum Advantage under High Loss
- Authors: Jie Zhao, Zeliang Wu, Haoran Liu, Yueya Liu, Xin Chen, Xinyun Liang, Wenfeng Huang, Chun-Hua Yuan, et al.
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.17876v1  pdf=https://arxiv.org/pdf/2601.17876v1.pdf

Abstract:
Quantum interferometers offer phase measurement capabilities that surpass the standard quantum limit (SQL), with phase sensitivity and quantum enhancement factor serving as key performance metrics. However, practical implementations face severe degradation of both metrics due to unavoidable losses, representing the foremost challenge in advancing quantum interferometry toward real-world applications. To address this challenge, we propose a coherent-amplifier-empowered quantum interferometer. The coherent amplifier dramatically suppresses the decay of both sensitivity and quantum enhancement under high-loss conditions, maintaining phase sensitivity beyond the original SQL even for losses exceeding 90%. Using an injected 4.2 dB squeezed-vacuum state in experimental demonstration, our scheme reduces the quantum enhancement degradation under 90% loss from 3.7 dB in a conventional quantum interferometer (CQI) to only 1.5 dB. More importantly, the phase sensitivity degradation under the same loss is limited to 4.0 dB, markedly outperforming the 11.2 dB degradation observed in a CQI. This improvement is enabled by the coherent amplifier's phase-sensitive photon amplification and its protection of the quantum state. This breakthrough in amplifier-empowered quantum interferometry overcomes the critical barrier to practical deployment, enabling robust quantum-enhanced measurements in lossy environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17919v1
- Title: Colour Centre Formation in Silicon-On-Insulator for On-Chip Photonic Integration
- Authors: Arnulf J. Snedker-Nielsen, David R. Gongora, Magnus L. Madsen, Christian H. Christiansen, Eike L. Piehorsch, Mathias Ø. Augustesen, Elvedin Memisevic, Sangeeth Kallatt, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2601.17919v1  pdf=https://arxiv.org/pdf/2601.17919v1.pdf

Abstract:
Colour centres in silicon have great potential as single photon sources for quantum technologies. Some of them - like the T centre - also possess optically-active spins that enable spin-photon interfaces for generating entangled photons and multi-spin registers. This paper explores the generation of several types of colour centres in silicon for mass-manufacturable silicon-on-insulator quantum devices. We investigate how different processes in the device development affect the presence of the quantum emitters, including thermal annealing and fabrication steps for optical nanostructures. The study reveals coupled formation dynamics between different colour centres, identifies optimal parameters for annealing processes, and reports on the sensitivity to annealing duration and nanofabrication procedures for photonic integrated circuits. Furthermore, we discern stable optical signals from colour centres in silicon which have not been identified before.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17924v1
- Title: Perturbation Theory and the Quantum Rabi-model
- Authors: Marcello Malagutti, Alberto Parmeggiani
- Categories: quant-ph (primary); quant-ph; math.AP; math.SP
- Links: abs=https://arxiv.org/abs/2601.17924v1  pdf=https://arxiv.org/pdf/2601.17924v1.pdf

Abstract:
In the first part of the paper we study a perturbative model of the Rabi system of Quantum Optics. We therefore are able to describe, through Rellich's theory, an analytic expansion of finite families, but of any fixed length, of eigenvalues. In particular, we prove that for finite families of eigenvalues the Braak conjecture holds. In the second part we study the asymptotics of the Weyl spectral counting function of a class of systems that generalize the Quantum Rabi Model to an $N$-level atom ($N\geq3$) with $N-1$ cavity modes of the electromagnetic field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17926v1
- Title: The hyperlink representation of entanglement and the inclusion-exclusion principle
- Authors: Silvia N. Santalla, Sudipto Singha Roy, Germán Sierra, Javier Rodríguez-Laguna
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2601.17926v1  pdf=https://arxiv.org/pdf/2601.17926v1.pdf

Abstract:
The entanglement entropy (EE) of any bipartition of a pure state can be approximately expressed as a sum of entanglement links (ELs). In this work, we introduce their exact extension, i.e. the entanglement hyperlinks (EHLs), a type of generalized mutual informations defined through the inclusion-exclusion principle, each of which captures contributions to the multipartite entanglement that are not reducible to lower-order terms. We show that any EHL crossing a factorized partition must vanish, and that the EHLs between any set of blocks can be expressed as a sum of all the EHLs that join all of them. This last result allows us to provide an exact representation of the EE of any block of a pure state, from the sum of the EHLs which cross its boundary. In order to illustrate their rich structure, we discuss some explicit numerical examples using ground states of local Hamiltonians. The EHLs thus provide a remarkable tool to characterize multipartite entanglement in quantum information theory and quantum many-body physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17930v1
- Title: A Rigorous and Self--Contained Proof of the Grover--Rudolph State Preparation Algorithm
- Authors: Antonio Falco, Daniela Falco-Pomares, Hermann G. Matthies
- Categories: quant-ph (primary); quant-ph; math.NA
- Links: abs=https://arxiv.org/abs/2601.17930v1  pdf=https://arxiv.org/pdf/2601.17930v1.pdf

Abstract:
Preparing quantum states whose amplitudes encode classical probability distributions is a fundamental primitive in quantum algorithms based on amplitude encoding and amplitude estimation. Given a probability distribution $\{p_k\}_{k=0}^{2^n-1}$, the Grover--Rudolph procedure constructs an $n$-qubit state $\ketψ=\sum_{k=0}^{2^n-1}\sqrt{p_k}\ket{k}$ by recursively applying families of controlled one-qubit rotations determined by a dyadic refinement of the target distribution. Despite its widespread use, the algorithm is often presented with informal correctness arguments and implicit conventions on the underlying dyadic tree. In this work we give a rigorous and self-contained analysis of the Grover--Rudolph construction: we formalize the dyadic probability tree, define the associated angle map via conditional masses, derive the resulting trigonometric factorizations, and prove by induction that the circuit prepares exactly the desired measurement law in the computational basis. As a complementary circuit-theoretic contribution, we show that each Grover--Rudolph stage is a uniformly controlled $\RY$ rotation on an active register and provide an explicit ancilla-free transpilation into the gate dictionary $\{\RY(\cdot),X,\CNOT(\cdot\to\cdot)\}$ using Gray-code ladders and a Walsh--Hadamard angle transform.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17936v1
- Title: Elementary Quantum Gates from Lie Group Embeddings in $U(2^n)$: Geometry, Universality, and Discretization
- Authors: Antonio Falco, Daniela Falco-Pomares, Hermann G. Matthies
- Categories: quant-ph (primary); quant-ph; math.NA
- Links: abs=https://arxiv.org/abs/2601.17936v1  pdf=https://arxiv.org/pdf/2601.17936v1.pdf

Abstract:
In the standard circuit model, elementary gates are specified relative to a chosen tensor factorization and are therefore extrinsic to the ambient group $U(2^n)$. Writing $N=2^n$, we introduce an intrinsic descriptor layer in $U(N)$ by declaring as primitive the motions inside faithful embedded copies of $SU(2)$, leading to the phase-free dictionary $\mathcal{G}^{SU}_{\mathrm{elem}}(n)=\bigcup_{φ\in\Emb(SU(2),U(N))}φ(SU(2))$, and we also discuss the phase-inclusive $U(2)$ variant. We show that $\Emb(SU(2),U(N))$ decomposes into finitely many $U(N)$-homogeneous strata indexed by isotypic multiplicities, with stabilizers given by centralizers; the canonical two-level sector is organized by $\Gr_2(\C^N)$ up to a $PSU(2)$ gauge. Equipping $U(N)$ with the Hilbert--Schmidt bi-invariant metric, each embedded subgroup is totally geodesic. Using two-level QR/Givens factorization together with an explicit generation of diagonal tori by two-level phase rotations, we prove phase-free universality $\langle\mathcal{G}^{SU}_{\mathrm{2lvl}}(n)\rangle=SU(N)$ and hence $\langle\mathcal{G}^{SU}_{\mathrm{elem}}(n)\rangle=SU(N)$. Full universality in $U(N)$ follows by adjoining the abelian diagonal/global $U(1)$ factors (equivalently, by passing to the $U(2)$ two-level dictionary). Finally, we record a modular finite-alphabet interface by lifting Solovay--Kitaev approximation in $SU(2)$ through two-level embeddings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17956v1
- Title: Quantum Radar System Using Born-Feynman path integrals approach
- Authors: Kumar Gautam, Akshit Dutta, Kumar Shubham
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2601.17956v1  pdf=https://arxiv.org/pdf/2601.17956v1.pdf

Abstract:
The paper relates to a quantum radar deployment by the Born-Feynman path integrals approach based on quantum dots. The radar system comprises a quantum dot-based entangled photon generator, a transmission module, a delay line, a detection module, and a signal processing unit. The quantum dot-based entangled photon generator produces entangled photon pairs via spontaneous parametric down-conversion or stimulated emission. The signal transmission module, equipped with a microwave antenna and beamforming elements, directs the signal photon toward a target. The delay line module synchronizes the retained idler photon with the returning signal photon, preserving quantum coherence. The detection module collects the reflected signal photon and uses a cryogenically cooled superconducting nanowire single photon detector (SNSPD) for detection. Finally, the signal processing unit analyzes the quantum correlation between the scattered and idler photons to enable precise quantum state comparison.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17960v1
- Title: Authentication in Security Proofs for Quantum Key Distribution
- Authors: Devashish Tupkary, Shlok Nahar, Ernest Y. -Z. Tan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17960v1  pdf=https://arxiv.org/pdf/2601.17960v1.pdf

Abstract:
Quantum Key Distribution (QKD) protocols rely on authenticated classical communication. Typical QKD security proofs are carried out in an idealized setting where authentication is assumed to behave honestly: it never aborts, and all classical messages are delivered faithfully with their original timing preserved. Authenticated channels that can be constructed in practice have different properties. Most critically, such channels may abort asymmetrically, such that only the receiving party may detect an authentication failure while the sending party remains unaware. Furthermore, an adversary may delay, reorder, or block classical messages. This discrepancy renders the standard QKD security definition and existing QKD security proofs invalid in the practical authentication setting. In this work we resolve this issue. Our main result is a reduction theorem showing that, under mild and easily satisfied protocol conditions, any QKD protocol proven secure under the honest authentication setting remains secure under a practical authentication setting. This result allows all existing QKD proofs to be retroactively lifted to the practical authentication setting with a minor protocol tweak.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17976v1
- Title: Quantum Paradoxes and the Quantum-Classical Transition under Unitary Measurement Dynamics with Random Hamiltonians
- Authors: Alexey A. Kryukov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.17976v1  pdf=https://arxiv.org/pdf/2601.17976v1.pdf

Abstract:
We develop a dynamical framework for quantum measurement based on stochastic but unitary evolution in projective state space. Random Hamiltonians drawn from the Gaussian Unitary Ensemble generate stochastic unitary dynamics of the quantum state, while equivalence classes reflecting finite detector resolution define classical observables as well as classical configuration-space and phase-space submanifolds. When the evolution is constrained to the phase-space submanifold, free Schrödinger dynamics reduces to Newtonian motion, while stochastic motion constrained to the classical configuration-space submanifold yields ordinary Brownian motion in classical space. Transition probabilities under the stochastic dynamics satisfy the Born rule, whereas the constrained classical evolution produces the normal probability distributions characteristic of classical measurements. We show that, in this setting, measurement, state reduction, and the quantum-classical transition emerge from unitary dynamics alone, without invoking nonunitary collapse or additional postulates. Entanglement and EPR correlations arise geometrically from the evolution of joint states in composite state space, preserving locality in spacetime. The framework provides a unified dynamical account of measurement and classicality compatible with the structure of quantum mechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18024v1
- Title: Linear combination of unitaries with exponential convergence
- Authors: Peter Brearley, Thomas Howarth
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18024v1  pdf=https://arxiv.org/pdf/2601.18024v1.pdf

Abstract:
We present a general method for decomposing non-unitary operators into a linear combination of unitary operators, where the approximation error decays exponentially. The decomposition is based on a smooth periodic extension of the identity map via the Fourier extension method, resulting in a sine series with exponentially decaying coefficients. Rewriting the sine series in terms of complex exponentials, then evaluating it on the Hermitian and anti-Hermitian parts of a non-unitary operator, yields its approximation by a linear combination of unitaries. When implemented in a quantum circuit, the subnormalisation of the resulting block encoding scales with the double logarithm of the inverse error, substantially improving over the polynomial relationship in existing methods. For hardware or applications with a fixed error budget, we discuss a strategy to minimise subnormalisation by exploiting the overcomplete nature of the Fourier extension basis. This regularisation procedure traces an error-subnormalisation Pareto front, identifying coefficients that maximise the subnormalisation at a fixed error budget. Fourier linear combinations of unitaries thus provides an accurate and versatile framework for non-unitary quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18035v1
- Title: A rigorous and complete security proof of decoy-state BB84 quantum key distribution
- Authors: Devashish Tupkary, Shlok Nahar, Amir Arqand, Ernest Y. -Z. Tan, Norbert Lütkenhaus
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18035v1  pdf=https://arxiv.org/pdf/2601.18035v1.pdf

Abstract:
We present a rigorous and complete security proof of the decoy-state BB84 quantum key distribution (QKD) protocol. Our analysis aims to achieve a high standard of mathematical rigour and completeness, thereby providing the necessary foundation for certification and standardization efforts. Beyond establishing the security of a specific protocol, this work develops a general and modular framework that can be readily adapted to a broad class of QKD protocols, including both prepare-and-measure and entanglement-based variants. Our framework unifies all major ingredients required for the analysis of realistic QKD protocols, including the analysis of classical authentication and classical processing, source-replacement schemes, finite-size analysis, source maps, squashing maps, and decoy-state techniques. In doing so, this work consolidates a diverse range of techniques scattered across the QKD literature into a unified formalism, representing a general and rigorous treatment of QKD security. Finally, it outlines a clear path towards incorporating practical imperfections within the same framework, thereby laying the groundwork for addressing implementation security in future analysis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18058v1
- Title: Differentiable Architecture Search for Adversarially Robust Quantum Computer Vision
- Authors: Mohamed Afane, Quanjiang Long, Haoting Shen, Ying Mao, Junaid Farooq, Ying Wang, Juntao Chen
- Categories: quant-ph (primary); quant-ph; cs.CV
- Links: abs=https://arxiv.org/abs/2601.18058v1  pdf=https://arxiv.org/pdf/2601.18058v1.pdf

Abstract:
Current quantum neural networks suffer from extreme sensitivity to both adversarial perturbations and hardware noise, creating a significant barrier to real-world deployment. Existing robustness techniques typically sacrifice clean accuracy or require prohibitive computational resources. We propose a hybrid quantum-classical Differentiable Quantum Architecture Search (DQAS) framework that addresses these limitations by jointly optimizing circuit structure and robustness through gradient-based methods. Our approach enhances traditional DQAS with a lightweight Classical Noise Layer applied before quantum processing, enabling simultaneous optimization of gate selection and noise parameters. This design preserves the quantum circuit's integrity while introducing trainable perturbations that enhance robustness without compromising standard performance. Experimental validation on MNIST, FashionMNIST, and CIFAR datasets shows consistent improvements in both clean and adversarial accuracy compared to existing quantum architecture search methods. Under various attack scenarios, including Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), Basic Iterative Method (BIM), and Momentum Iterative Method (MIM), and under realistic quantum noise conditions, our hybrid framework maintains superior performance. Testing on actual quantum hardware confirms the practical viability of discovered architectures. These results demonstrate that strategic classical preprocessing combined with differentiable quantum architecture optimization can significantly enhance quantum neural network robustness while maintaining computational efficiency.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18060v1
- Title: Overcoming Barren Plateaus in Variational Quantum Circuits using a Two-Step Least Squares Approach
- Authors: Francis Boabang, Samuel Asante Gyamerah
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2601.18060v1  pdf=https://arxiv.org/pdf/2601.18060v1.pdf

Abstract:
Variational Quantum Algorithms are a vital part of quantum computing. It is a blend of quantum and classical methods for tackling tough problems in machine learning, chemistry, and combinatorial optimization. Yet as these algorithms scale up, they cannot escape the barren-plateau phenomenon. As systems grow, gradients can vanish so quickly that training deep or randomly initialized circuits becomes nearly impossible. To overcome the barren plateau problem, we introduce a two-stage optimization framework. First comes the convex initialization stage. Here, we shape the quantum energy landscape, the Hilmaton landscape, into a smooth, low-energy basin. This step makes gradients easier to spot and keeps noise from derailing the process. Once we have gotten a stable gradient flow, we move to the second stage: nonconvex refinement. In this phase, we allow the algorithm to explore different energy minima, thereby making the model more expressive. Finally, we used our two-stage solution to perform quantum cryptanalysis of the quantum key distribution protocol (i.e., BB84) to determine the optimal cloning strategies. The simulation results showed that our proposed two-stage solution outperforms its random initialization counterpart.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18082v1
- Title: Feedback-Based Quantum Control for Safe and Synergistic Drug Combination Design
- Authors: Mai Nguyen Phuong Nhi, Lan Nguyen Tran, Le Bin Ho
- Categories: quant-ph (primary); quant-ph; physics.chem-ph; physics.comp-ph; physics.med-ph
- Links: abs=https://arxiv.org/abs/2601.18082v1  pdf=https://arxiv.org/pdf/2601.18082v1.pdf

Abstract:
Drug-drug interactions (DDIs) strongly affect the safety and efficacy of combination therapies. Despite the availability of large DDI databases, selecting optimal multi-drug combinations that balance safety, therapeutic benefit, and regimen size remains a challenging combinatorial optimization problem. Here, we present a quantum-control-based framework for DDI-aware drug combination optimization, in which known harmful and synergistic interactions are encoded into Ising Hamiltonians as penalties and rewards, respectively. The optimization is performed using the feedback-based quantum algorithm FALQON, a gradient-free variational approach. We study two clinically motivated tasks: the Maximum Safe Subset problem and the Synergy-Constrained Optimization problem. Numerical simulations using interaction data from Drugs.com and SYNERGxDB demonstrate efficient convergence and high-quality solutions for clinically relevant drug sets, including COVID-19 case studies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18083v1
- Title: Two-Polariton Blockade via Ultrastrong Light-Matter Coupling
- Authors: Ting-Ting Ma, Jian Tang, Yun-Lan Zuo, Ran Huang. Adam Miranowicz, Franco Nori, Hui Jing
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18083v1  pdf=https://arxiv.org/pdf/2601.18083v1.pdf

Abstract:
We demonstrate that a two-polariton blockade (2PB) can occur under resonant single-polariton driving in an atom-cavity system operating in the ultrastrong coupling (USC) regime-a phenomenon qualitatively distinct from, and unattainable in, both the strong and weak coupling regimes. In the USC regime, where the ratio of the atom-cavity coupling strength to the cavity resonance frequency exceeds 0.1, hybrid light-matter quasiparticles known as polaritons emerge. By employing modified second- and third-order correlation functions appropriate for the USC regime, we predict the emergence of 2PB, characterized by pronounced two-polariton bunching accompanied by suppressed three-polariton coincidences. This Letter introduces a novel route to achieving 2PB, with promising implications for the realization of multiparticle quantum light sources in the USC regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18108v1
- Title: Sparse QUBO Formulation for Efficient Embedding via Network-Based Decomposition of Equality and Inequality Constraints
- Authors: Kohei Suda, Soshun Naito, Yoshihiko Hasegawa
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18108v1  pdf=https://arxiv.org/pdf/2601.18108v1.pdf

Abstract:
Quantum annealing is a promising approach for solving combinatorial optimization problems. However, its performance is often limited by the overhead of additional qubits required for embedding logical QUBO models onto quantum annealers. This overhead becomes severe when logical QUBO models have dense connectivity. Such dense structures frequently arise when formulating equality and inequality constraints. To address this issue, we propose a method to construct a significantly sparser logical QUBO model for these constraints. By adding auxiliary variables based on specific network structures, our approach decomposes the original constraint into smaller, more manageable constraints. We demonstrate that this method reduces the number of edges (quadratic terms) from $O(N^2)$ to $O(N)$ for the one-hot constraint and to $O(N\log N)$ in the worst case for general equality constraints, where $N$ is the number of variables. Experimental results on D-Wave's hardware show that our formulation leads to substantial reductions in the number of qubits required for embedding, shorter average chain lengths, lower chain break rates, and higher feasible solution rates compared to conventional methods. This work provides a practical tool for efficiently solving constrained optimization problems on current and future quantum annealers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18164v1
- Title: Quantum Recurrent Unit: A Parameter-Efficient Quantum Neural Network Component
- Authors: Tzong-Daw Wu, Hsi-Sheng Goan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18164v1  pdf=https://arxiv.org/pdf/2601.18164v1.pdf

Abstract:
The rapid growth of modern machine learning (ML) models presents fundamental challenges in parameter efficiency and computational resource requirements. This study introduces the Quantum Recurrent Unit (QRU), a novel quantum neural network (NN) architecture specifically designed to address these challenges while remaining compatible with Noisy Intermediate-Scale Quantum (NISQ) devices. QRU leverages quantum controlled-SWAP (C-SWAP; Fredkin) gates to implement an information selection mechanism inspired by classical Gated Recurrent Units (GRUs), enabling selective processing of temporal information via quantum operations. Through its innovative recurrent architecture featuring measurement results feedforward state propagation and shared parameters across time steps, QRU achieves constant circuit depth and constant parameter count regardless of input sequence length, effectively circumventing stringent NISQ hardware constraints. We systematically validate QRU through three progressive experiments: (1) oscillatory behavior prediction, where 72-parameter QRU matches 197-parameter classical GRU performance; (2) Wisconsin Diagnostic Breast Cancer classification, where 35 parameters achieve 96.13% accuracy comparable to 167-parameter artificial NNs; and (3) MNIST handwritten digit recognition, where 132 parameters reach 98.05% accuracy, outperforming a 27,265-parameter convolutional NN. These results demonstrate that QRU consistently achieves comparable or superior performance with significantly fewer parameters than classical NNs while maintaining constant quantum circuit depth. The architecture's quantum-native design, combining C-SWAP-based information selection with novel recurrent processing, suggests QRU's potential as a fundamental building block for next-generation ML systems, offering a promising pathway toward more efficient and scalable quantum ML architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18290v1
- Title: Resource-Efficient Noise Spectroscopy for Generic Quantum Dephasing Environments
- Authors: Yuan-De Jin, Zheng-Fei Ye, Wen-Long Ma
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18290v1  pdf=https://arxiv.org/pdf/2601.18290v1.pdf

Abstract:
We present a resource-efficient method based on repetitive weak measurements to directly measure the noise spectrum of a generic quantum environment that causes qubit phase decoherence. The weak measurement is induced by a Ramsey interferometry measurement (RIM) on the qubit and periodically applied during the free evolution of the environment. We prove that the measurement correlation of such repetitive RIMs approximately corresponds to a direct sampling of the noise correlation function, thus enabling direct noise spectroscopy of the environment. Compared to dynamical-decoupling-based noise spectroscopy, this method can efficiently measure the full noise spectrum with the detected frequency range not limited by qubit coherence time. This method is also more resource-efficient than the correlation spectroscopy, as for the same detection accuracy with $N$ sampling times, it takes total detection time $O(N)$ while the latter one takes time $O(N^2)$. We numerically demonstrate this method for both bosonic and spin baths.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18327v1
- Title: Scalable Repeater Architecture for Long-Range Quantum Energy Teleportation in Gapped Systems
- Authors: M. Y. Abd-Rabbou, Irfan Siddique, Saeed Haddadi, Cong-Feng Qiao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18327v1  pdf=https://arxiv.org/pdf/2601.18327v1.pdf

Abstract:
Quantum Energy Teleportation (QET) constitutes a paradigm-shifting protocol that permits the activation of local vacuum energy through the consumption of pre-existing entanglement and classical communication. Nevertheless, the implementation of QET is severely impeded by the fundamental locality of gapped many-body systems, where the exponential clustering of ground-state correlations restricts energy extraction to microscopic scales. In this work, we address this scalability crisis within the framework of the one-dimensional anisotropic XY model. We initially provide a rigorous characterization of a monolithic measurement-induced strategy, demonstrating that while bulk projective measurements can theoretically induce long-range couplings, the approach is rendered physically untenable by exponentially diverging thermodynamic costs and vanishing success probabilities. To circumvent this impasse, we propose and analyze a hierarchical quantum repeater architecture adapted for energy teleportation. By orchestrating heralded entanglement generation, iterative entanglement purification, and nested entanglement swapping, our protocol effectively counteracts the fidelity degradation inherent in noisy quantum channels. We establish that this architecture fundamentally alters the operational resource scaling from exponential to polynomial. This proves, for the first time, the physical permissibility and computational tractability of activating vacuum energy at arbitrary distances. The significance lies not in net energy gain, but in establishing long-range QET as a viable protocol for remote quantum control and resource distribution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18347v1
- Title: Scaling of multicopy constructive interference of Gaussian states
- Authors: Matthieu Arnhem, Radim Filip
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18347v1  pdf=https://arxiv.org/pdf/2601.18347v1.pdf

Abstract:
Quantum technology advances crucially depend on the scaling up of essential quantum resources. Their ideal multiplexing offers more significant gains in applications; however, the scaling of the nonidentical, fragile and varying resources is neither theoretically nor experimentally known. For bosonic systems, multimode interference is an essential tool already widely exploited to develop quantum technology. Here, we analyze, predict and compare essential scaling laws for a constructive interference of multiplexed nonclassical Gaussian states carrying information by displacement with weakly fluctuating squeezing in different multimode interference architectures. The signal-to-noise ratio quantifies the increase in displacement relative to the noise. We introduce the gain-to-instability ratio to numerically estimate the effect of unexplored resource instabilities in a large scale interference scheme. The use of the gain-to-instability ratio to quantify the scaling laws opens steps for extensive theoretical investigation of other bosonic resources and follow-up feasible experimental verification necessary for further development of these platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18351v1
- Title: An Adaptive Purification Controller for Quantum Networks: Dynamic Protocol Selection and Multipartite Distillation
- Authors: Pranav Kulkarni, Leo Sünkel, Michael Kölle
- Categories: quant-ph (primary); quant-ph; cs.DC
- Links: abs=https://arxiv.org/abs/2601.18351v1  pdf=https://arxiv.org/pdf/2601.18351v1.pdf

Abstract:
Efficient entanglement distribution is the cornerstone of the Quantum Internet. However, physical link parameters such as photon loss, memory coherence time, and gate error rates fluctuate dynamically, rendering static purification strategies suboptimal. In this paper, we propose an Adaptive Purification Controller (APC) that autonomously optimizes the entanglement distillation sequence to maximize the "goodput," the rate of delivered pairs meeting a strict fidelity threshold. By treating protocol selection as a resource allocation problem, the APC dynamically switches between purification depths and protocol families (e.g., BBPSSW vs. DEJMPS) to navigate the trade-off between generation rate and state quality. Using a dynamic programming planner with Pareto pruning, simulation results demonstrate that our approach eliminates the "fidelity cliffs" inherent in static protocols and prevents resource wastage in high-noise regimes. Furthermore, we extend the controller to heterogeneous scenarios, demonstrating robustness for both multipartite GHZ state generation and continuous variable systems using effective noiseless linear amplification models. We benchmark its computational overhead, confirming real-time feasibility with decision latencies in the millisecond range per link.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18366v1
- Title: Bohr's complementarity principle tested on a real quantum computer via interferometer experiments
- Authors: Celia Álvarez Álvarez, Mariamo Mussa Juane
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18366v1  pdf=https://arxiv.org/pdf/2601.18366v1.pdf

Abstract:
Bohr's Complementarity Principle is a core concept of quantum mechanics. In this article, an updated complementarity relation for the wave and ondulatory aspects of a quantum system is presented and discussed. Two interferometric experiments are implemented in one and two qubit circuits and executed on real hardware. The final state density matrices are reconstructed using quantum state tomography and the complementarity relation is tested via direct computation. Results of the executions are presented both graphically and with a mean squared error analysis for a better comprehension.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18373v1
- Title: Atom-light hybrid interferometer for atomic sensing with quantum memory
- Authors: Xingchang Wang, Xinyun Liang, Liang Dong, Ying Zuo, Jianmin Wang, Dasen Yang, Linyu Chen, Georgios A. Siviloglou, et al.
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.18373v1  pdf=https://arxiv.org/pdf/2601.18373v1.pdf

Abstract:
Quantum memories feature a reversible conversion of optical fields into long-lived atomic spin waves, and are therefore ideal for operating as sensitive atomic sensors. However, up to now, atom-light interferometers have lacked an efficient approach to exploit their ultimate atomic sensing performance, since an extra optical delay line is required to compensate for the memory time. Here, we report a new protocol that records the photocurrent via heterodyne mixing with a stable local oscillator. The obtained complex quadrature amplitude that carries information imprinted on its phase by an external magnetic field, is successfully recovered from the interference patterns between the light and the atomic spin wave, without the stringent requirement of having them overlap in time. Our results reveal that the sensitivity scales favorably with the lifetime of the quantum memory. Our work may have important applications in building distributed quantum networks through quantum memory-assisted atom-light interferometers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18384v1
- Title: Quantum Error Correction on Error-mitigated Physical Qubits
- Authors: Minjun Jeon, Zhenyu Cai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18384v1  pdf=https://arxiv.org/pdf/2601.18384v1.pdf

Abstract:
We present a general framework for applying linear quantum error mitigation (QEM) techniques directly to physical qubits within a logical qubit to suppress logical errors. By exploiting the linearity of quantum error correction (QEC), we demonstrate that any linear QEM method$\unicode{x2014}$including probabilistic error cancellation (PEC), zero-noise extrapolation (ZNE), and symmetry verification$\unicode{x2014}$can be integrated into the physical layer without requiring modifications to the subsequent QEC decoder. Applying this framework to memory experiments using PEC, we analytically prove and numerically verify that the leading-order contribution to the logical error can be removed, increasing the effective code distance by 2. Our simulations on repetition and rotated surface codes show that a distance-3 code with physical-level PEC achieves logical error rates lower than or similar to a distance-5 unmitigated code while using 40% and 64% fewer qubits, respectively. These results establish physical-level QEM as a widely compatible and resource-efficient strategy for enhancing logical performance in early fault-tolerant architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18419v1
- Title: Emergent Cooperation in Quantum Multi-Agent Reinforcement Learning Using Communication
- Authors: Michael Kölle, Christian Reff, Leo Sünkel, Julian Hager, Gerhard Stenzel, Claudia Linnhoff-Popien
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.LG; cs.MA
- Links: abs=https://arxiv.org/abs/2601.18419v1  pdf=https://arxiv.org/pdf/2601.18419v1.pdf

Abstract:
Emergent cooperation in classical Multi-Agent Reinforcement Learning has gained significant attention, particularly in the context of Sequential Social Dilemmas (SSDs). While classical reinforcement learning approaches have demonstrated capability for emergent cooperation, research on extending these methods to Quantum Multi-Agent Reinforcement Learning remains limited, particularly through communication. In this paper, we apply communication approaches to quantum Q-Learning agents: the Mutual Acknowledgment Token Exchange (MATE) protocol, its extension Mutually Endorsed Distributed Incentive Acknowledgment Token Exchange (MEDIATE), the peer rewarding mechanism Gifting, and Reinforced Inter-Agent Learning (RIAL). We evaluate these approaches in three SSDs: the Iterated Prisoner's Dilemma, Iterated Stag Hunt, and Iterated Game of Chicken. Our experimental results show that approaches using MATE with temporal-difference measure (MATE\textsubscript{TD}), AutoMATE, MEDIATE-I, and MEDIATE-S achieved high cooperation levels across all dilemmas, demonstrating that communication is a viable mechanism for fostering emergent cooperation in Quantum Multi-Agent Reinforcement Learning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18426v1
- Title: A Theory of Single-Antenna Atomic Beamforming
- Authors: Mingyao Cui, Qunsong Zeng, Kaibin Huang
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2601.18426v1  pdf=https://arxiv.org/pdf/2601.18426v1.pdf

Abstract:
Leveraging the quantum advantages of highly excited atoms, Rydberg atomic receivers (RAREs) represent a paradigm shift in radio wave detection, offering high sensitivity and broadband reception. However, existing studies largely model RAREs as isotropic point receivers and overlook the spatial variations of atomic quantum states within vapor cells, thus inaccurately characterizing their reception patterns. To address this issue, we present a theoretical analysis of the aforementioned spatial responses of a standard local-oscillator (LO)- dressed RARE. Our results reveal that increasing the vapor-cell length produces a receive beam aligned with the LO field, with a beamwidth inversely proportional to the cell length. This finding enables atomic beamforming to enhance received signal-to-noise ratio using only a single-antenna RARE. Furthermore, we derive the achievable beamforming gain by characterizing and balancing the fundamental tradeoff between the effects of increasing the vapor cell length and the exponential power decay of laser propagating through the cell. To overcome the limitation imposed by exponential decay, we propose a novel RARE architecture termed segmental vapor cell. This architecture consists of vapor-cell segments separated by clear-air gaps, allowing the total cell length (and hence propagation loss) to remain fixed while the effective cell length increases. As a result, this segmented design expands the effective atom-field interaction area without increasing the total vapor cell length, yielding a narrower beamwidth and thus higher beamforming gain as compared with a traditional continuous vapor cell.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18482v1
- Title: Physics-Informed Hybrid Quantum-Classical Dispatching for Large-Scale Renewable Power Systems:A Noise-Resilient Framework
- Authors: Fu Zhang, Yuming Zhao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18482v1  pdf=https://arxiv.org/pdf/2601.18482v1.pdf

Abstract:
The integration of high-penetration renewable energy introduces significant stochasticity and non-convexity into power system dispatching, challenging the computational limits of classical optimization. While Variational Quantum Algorithms (VQAs) on Noisy Intermediate-Scale Quantum (NISQ) devices offer a promising path for combinatorial acceleration, existing approaches typically treat the power grid as a "black box", suffering from poor scalability (barren plateaus) and frequent violations of physical constraints. Bridging these gaps, this paper proposes a Physics-Informed Hybrid Quantum-Classical Dispatching (PI-HQCD) framework. We construct a topology-aware Hamiltonian that explicitly embeds linearized power flow equations, storage dynamics, and multi-timescale coupling directly into the quantum substrate, significantly reducing the search space dimensionality. We further derive a noise-adaptive regularization mechanism that theoretically bounds the effective Lipschitz constant of the objective function, guaranteeing convergence stability under realistic quantum measurement noise. Numerical experiments on the IEEE 39-bus benchmark and a 118-bus regional grid demonstrate that PI-HQCD achieves superior economic efficiency and higher renewable utilization compared to stochastic dual dynamic programming (SDDP). Theoretical analysis confirms that this topology-aware design leads to an O(1/N) gradient variance scaling, effectively mitigating barren plateaus and ensuring scalability for larger networks. This work establishes a rigorous paradigm for embedding engineering physics into quantum computing, paving the way for practical quantum advantage in next-generation grid operations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18499v1
- Title: Qubit-parity interference despite unknown interaction phases
- Authors: Kratveer Singh, Kimin Park, Vojtěch Švarc, Artem Kovalenko, Tuan Pham, Ondřej Číp, Lukáš Slodička, Radim Filip
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18499v1  pdf=https://arxiv.org/pdf/2601.18499v1.pdf

Abstract:
Quantum interference between interacting systems is fundamental to basic science and quantum technology, but it typically requires precise control of the interaction phases of lasers or microwave generators. Can interference be observed if those interaction phases are stable but unknown, usually prohibitive for complex state without active control? Here, we answer this question by experimentally preparing a Schrödinger-cat-like state of an internal qubit and a motional oscillator of a trapped $^{40}$Ca$^{+}$ ion, and its robustness to such uncontrolled phase. By applying alternating red and blue sideband pulses, we enforce a strict qubit-parity correlation and interference inherently insensitive to stable but unknown phases of the driving laser. For this qubit-parity interference, we use a minimal two-pulse interferometric sequence to demonstrate characteristic visibilities of $20\%$ and $40\%$, which approach the theoretical visibility limit, providing a scalable coherence witness without full state tomography for high-dimensional states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18506v1
- Title: Imperfect blockade in Rydberg superatoms
- Authors: Valentin Magro, Sébastien Garcia, Alexei Ourjoumtsev
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2601.18506v1  pdf=https://arxiv.org/pdf/2601.18506v1.pdf

Abstract:
Ensembles of atoms interacting via their Rydberg levels, known as "superatoms" for their ability to encode qubits and to emit single photons, attract increasing attention as building blocks for quantum network nodes. Assessing their performance requires an accurate, physically informative and numerically scalable description of interactions in a large and disordered ensemble. We derive such a description from first principles and successfully test it against brute-force numerics and experimental data. This model proves essential to make quantitative predictions about gate fidelities or photon emission efficiencies, and to guide experiments towards large-scale superatom-based systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18514v1
- Title: Simultaneous determination of multiple low-lying energy levels on a superconducting quantum processor
- Authors: Huili Zhang, Yibin Guo, Guanglei Xu, Yulong Feng, Jingning Zhang, Hai-feng Yu, S. P. Zhao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18514v1  pdf=https://arxiv.org/pdf/2601.18514v1.pdf

Abstract:
Determining the ground and low-lying excited states is critical in numerous scenarios. Recent work has proposed the ancilla-entangled variational quantum eigensolver (AEVQE) that utilizes entanglement between ancilla and physical qubits to simultaneously tagert multiple low-lying energy levels. In this work, we report the experimental implementation of the AEVQE on a superconducting quantum cloud platform, demonstrating the full procedure of solving the low-lying energy levels of the H$_2$ molecule and the transverse-field Ising models (TFIMs). We obtain the potential energy curves of H$_2$ and show an indication of the ferromagnetic to paramagnetic phase transition in the TFIMs from the average absolute magnetization. Moreover, we investigate multiple factors that affect the algorithmic performance and provide a comparison with ancilla-free VQE algorithms. Our work demonstrates the experimental feasibility of the AEVQE algorithm and offers a guidance for the VQE approach in solving realistic problems on publicly-accessible quantum platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18518v1
- Title: Quantum Key Distribution with a Negatively Charged Quantum Dot Single-Photon Source
- Authors: Parvendra Kumar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18518v1  pdf=https://arxiv.org/pdf/2601.18518v1.pdf

Abstract:
Various quantum key distribution protocols require bright single-photon sources with a very low probability of multiphoton emission. In this work, we investigate single-photon generation from a negatively charged quantum dot embedded in an elliptical pillar microcavity, driven using either resonant excitation or adiabatic rapid passage (ARP). Our results show that ARP excitation significantly suppresses multiphoton emission probability and improves photon indistinguishability compared to resonant excitation. We further evaluate the secure key rate of both BB84 and twin-field quantum key distribution (TF-QKD) using quantum-dot single-photon sources and compare their performance with that of Poisson-distributed photon sources (PDS) such as weak coherent pulses and down-conversion sources. The analysis reveals that adiabatic excitation offers a modest but consistent enhancement in secure key rate relative to resonant excitation. Moreover, quantum-dot single-photon sources outperform PDS sources over short and intermediate distances; however, at longer distances, PDS sources eventually surpass quantum-dot sources in both infinite decoy-state BB84 and TF-QKD.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18534v1
- Title: Certifying optimal device-independent quantum randomness in quantum networks
- Authors: Shuai Zhao, Rong Wang, Qi Zhao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18534v1  pdf=https://arxiv.org/pdf/2601.18534v1.pdf

Abstract:
Bell nonlocality provides a device-independent (DI) way to certify quantum randomness, based on which true random numbers can be extracted from the observed correlations without detail characterizations on devices for quantum state preparation and measurement. However, the efficiency of current strategies for DI randomness certification is still heavily constrained when it comes to non-maximal Bell values, especially for multiple parties. Here, we present a family of multipartite Bell inequalities that allows to certify optimal quantum randomness and self-test GHZ (Greenberger-Horne-Zeilinger) states, which are inspired from the stabilizer group of the GHZ state. Due to the simple representation of stabilizer group for GHZ states, this family of Bell inequalities is of simple structure and can be easily expanded to more parties. Compared with the Mermin-type inequalities, this family of Bell inequality is more efficient in certifying quantum randomness when non-maximal Bell values achieved. Meanwhile, the general analytical upper bound for the Holevo quantity is presented, and achieves better performance compared with the MABK (Mermin-Ardehali-Belinskii-Klyshko) inequality, Parity-CHSH (Clauser-Horne-Shimony-Holt) inequality and Holz inequality at $N=3$, which is of particular interests for experimental researches on DI quantum cryptography in quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18538v1
- Title: Sufficient conditions for additivity of the zero-error classical capacity of quantum channels
- Authors: Jeonghoon Park, Jeong San Kim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18538v1  pdf=https://arxiv.org/pdf/2601.18538v1.pdf

Abstract:
The one-shot zero-error classical capacity of a quantum channel is the amount of classical information that can be transmitted with zero probability of error by a single use. Then the one-shot zero-error classical capacity equals to the logarithmic value of the independence number of the noncommutative graph induced by the channel. Thus the additivity of the one-shot zero-error classical capacity of a quantum channel is equivalent to the multiplicativity of the independence number of the noncommutative graph. The independence number is not multiplicative in general, and it is not clearly understood when the multiplicativity occurs. In this work, we present sufficient conditions for multiplicativity of the independence number, and we give explicit examples of quantum channels. Furthermore, we consider a block form of noncommutative graphs, and provide conditions when the independence number is multiplicative.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18562v1
- Title: Bayesian Optimization for Quantum Error-Correcting Code Discovery
- Authors: Yihua Chengyu, Richard Meister, Conor Carty, Sheng-Ku Lin, Roberto Bondesan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18562v1  pdf=https://arxiv.org/pdf/2601.18562v1.pdf

Abstract:
Quantum error-correcting codes protect fragile quantum information by encoding it redundantly, but identifying codes that perform well in practice with minimal overhead remains difficult due to the combinatorial search space and the high cost of logical error rate evaluation. We propose a Bayesian optimization framework to discover quantum error-correcting codes that improves data efficiency and scalability with respect to previous machine learning approaches to this task. Our main contribution is a multi-view chain-complex neural embedding that allows us to predict the logical error rate of quantum LDPC codes without performing expensive simulations. Using bivariate bicycle codes and code capacity noise as a testbed, our algorithm discovers a high-rate code [[144,36]] that achieves competitive per-qubit error rate compared to the gross code, as well as a low-error code [[144,16]] that outperforms the gross code in terms of error rate per qubit. These results highlight the ability of our pipeline to automatically discover codes balancing rate and noise suppression, while the generality of the framework enables application across diverse code families, decoders, and noise models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18637v1
- Title: Universality of Many-body Projected Ensemble for Learning Quantum Data Distribution
- Authors: Quoc Hoan Tran, Koki Chinzei, Yasuhiro Endo, Hirotaka Oshima
- Categories: quant-ph (primary); quant-ph; cs.LG; stat.ML
- Links: abs=https://arxiv.org/abs/2601.18637v1  pdf=https://arxiv.org/pdf/2601.18637v1.pdf

Abstract:
Generating quantum data by learning the underlying quantum distribution poses challenges in both theoretical and practical scenarios, yet it is a critical task for understanding quantum systems. A fundamental question in quantum machine learning (QML) is the universality of approximation: whether a parameterized QML model can approximate any quantum distribution. We address this question by proving a universality theorem for the Many-body Projected Ensemble (MPE) framework, a method for quantum state design that uses a single many-body wave function to prepare random states. This demonstrates that MPE can approximate any distribution of pure states within a 1-Wasserstein distance error. This theorem provides a rigorous guarantee of universal expressivity, addressing key theoretical gaps in QML. For practicality, we propose an Incremental MPE variant with layer-wise training to improve the trainability. Numerical experiments on clustered quantum states and quantum chemistry datasets validate MPE's efficacy in learning complex quantum data distributions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18680v1
- Title: Error-mitigation aware benchmarking strategy for quantum optimization problems
- Authors: Marine Demarty, Bo Yang, Kenza Hammam, Pauline Besserve
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18680v1  pdf=https://arxiv.org/pdf/2601.18680v1.pdf

Abstract:
Assessing whether a noisy quantum device can potentially exhibit quantum advantage is essential for selecting practical quantum utility tasks that are not efficiently verifiable by classical means. For optimization, a prominent candidate for quantum advantage, entropy benchmarking provides insights based concomitantly on the specifics of the application and its implementation, as well as hardware noise. However, such an approach still does not account for finite-shot effects or for quantum error mitigation (QEM), a key near-term error suppression strategy that reduces estimation bias at the cost of increased sampling overhead. We address this limitation by developing a benchmarking framework that explicitly incorporates finite-shot statistics and the resource overhead induced by QEM. Our framework quantifies quantum advantage through the confidence that an estimated energy lies within an interval defined by the best-known classical upper and lower bounds. Using a proof-of-principle numerical study of the two-dimensional Fermi-Hubbard model at size $8\times8$, we demonstrate that the framework effectively identifies noise and shot-budget regimes in which the probabilistic error cancellation (PEC), a representative QEM method, is operationally advantageous, and potential quantum advantage is not hindered by finite-shot effects. Overall, our approach equips end-users with a framework based on lightweight numerics for assessing potential practical quantum advantage in optimization on near-future quantum hardware, in light of the allocated shot budget.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18704v1
- Title: Data-Driven Qubit Characterization and Optimal Control using Deep Learning
- Authors: Paul Surrey, Julian D. Teske, Tobias Hangleiter, Hendrik Bluhm, Pascal Cerfontaine
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2601.18704v1  pdf=https://arxiv.org/pdf/2601.18704v1.pdf

Abstract:
Quantum computing requires the optimization of control pulses to achieve high-fidelity quantum gates. We propose a machine learning-based protocol to address the challenges of evaluating gradients and modeling complex system dynamics. By training a recurrent neural network (RNN) to predict qubit behavior, our approach enables efficient gradient-based pulse optimization without the need for a detailed system model. First, we sample qubit dynamics using random control pulses with weak prior assumptions. We then train the RNN on the system's observed responses, and use the trained model to optimize high-fidelity control pulses. We demonstrate the effectiveness of this approach through simulations on a single $ST_0$ qubit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18718v1
- Title: Nontrivial bounds on extractable energy in quantum energy teleportation for gapped manybody systems with a unique ground state
- Authors: Taisanul Haque
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2601.18718v1  pdf=https://arxiv.org/pdf/2601.18718v1.pdf

Abstract:
We establish a universal, exponentially decaying upper bound on the average energy that can be extracted in quantum energy teleportation (QET) protocols executed on finite-range gapped lattice systems possessing a unique ground state. Under mild regularity assumptions on the Hamiltonian and uniform operator-norm bounds on the local measurement operators, there exist positive constants $C$ and $μ$ (determined by the spectral gap, interaction range and local operator norms) such that for any local measurement performed in a region $A$ and any outcome-dependent local unitaries implemented in a disjoint region $B$ separated by distance $d=\operatorname{dist}(A,B)$ one has $|E_A-E_B|\le C\,e^{-μd}.$ The bound is nonperturbative, explicit up to model-dependent constants, and follows from the variational characterization of the ground state combined with exponential clustering implied by the spectral gap.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18720v1
- Title: On the Stochastic-Quantum Correspondence
- Authors: Sami Calvo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18720v1  pdf=https://arxiv.org/pdf/2601.18720v1.pdf

Abstract:
This paper aims to first explain, somewhat more clearly, the Stochastic-Quantum correspondence put forward in by Barandes in 2023. Specifically, the quantum-mechanical bra-ket notation is used, illuminating some results of previous results. With this, we prove the six axioms of textbook quantum mechanics from a single axiom: every physical system evolves according to a, generally indivisible, stochastic law. Afterwards, we generalise the treatment to continuous bases, which showcases a problem with them, indicating that space (and other physical variables) may be discrete in nature. Some concrete examples are also given, including the generalisation to classical and quantum fields. Then, we treat some practical issues of this new stochastic approach, regarding the solving of problems in physics, which turns out to still be most tractable in the traditional way. Finally, we explain the classical limit, where a system of many particles is found to behave classically according to Newton's second law. Along with that, we present a way of solving the measurement problem, characterising what is an environment and a measuring device and explaining how the wavefunction collapse comes about. Specifically, it is found that what distinguishes an environment is its number of degrees of freedom, while a measuring device is a low-entropy type of environment.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18743v1
- Title: Approximate level-by-level maximum-likelihood decoding based on the Chase algorithm for high-rate concatenated stabilizer codes
- Authors: Takeshi Kakizaki
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18743v1  pdf=https://arxiv.org/pdf/2601.18743v1.pdf

Abstract:
Fault-tolerant quantum computation (FTQC) is expected to address a wide range of computational problems. To realize large-scale FTQC, it is essential to encode logical qubits using quantum error-correcting codes. High-rate concatenated codes have recently attracted attention due to theoretical advances in fault-tolerant protocols with constant-space-overhead and polylogarithmic-time-overhead, as well as practical developments of high-rate many-hypercube codes equipped with a high-performance level-by-level minimum-distance decoder (LMDD). We propose a general, high-performance decoder for high-rate concatenated stabilizer codes that extends LMDD by leveraging the Chase algorithm to generate a suitable set of candidate errors. Our simulation results demonstrate that the proposed decoder outperforms conventional decoders for high-rate concatenated Hamming codes under bit-flip noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18756v1
- Title: Efficient Trotter-Suzuki Schemes for Long-time Quantum Dynamics
- Authors: Marko Maležič, Johann Ostmeyer
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; hep-lat; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2601.18756v1  pdf=https://arxiv.org/pdf/2601.18756v1.pdf

Abstract:
Accurately simulating long-time dynamics of many-body systems is a challenge in both classical and quantum computing due to the accumulation of Trotter errors. While low-order Trotter-Suzuki decompositions are straightforward to implement, their rapidly growing error limits access to long-time observables. We present a framework for constructing efficient high-order Trotter-Suzuki schemes by identifying their structure and directly optimizing their parameters over a high-dimensional space. This method enables the discovery of new schemes with significantly improved efficiency compared to traditional constructions, such as those by Suzuki and Yoshida. Based on the theoretical efficiency and practical performance, we recommend two novel highly efficient schemes at $4^{\textrm{th}}$ and $6^{\textrm{th}}$ order. We also demonstrate the effectiveness of these decompositions on the Heisenberg model and the quantum harmonic oscillator, and find that for a fixed final time they perform better across the computational cost. Even when using large time steps, they surpass established low-order schemes like the Leapfrog. Finally, we investigate the in-practice performance of different Trotter schemes and find the decompositions with more uniform coefficients tend to feature improved error accumulation over long times. We have included this observation into our choice of recommended schemes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18767v1
- Title: Practical block encodings of matrix polynomials that can also be trivially controlled
- Authors: Martina Nibbi, Filippo Della Chiara, Yizhi Shen, Aaron Szasz, Roel Van Beeumen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18767v1  pdf=https://arxiv.org/pdf/2601.18767v1.pdf

Abstract:
Quantum circuits naturally implement unitary operations on input quantum states. However, non-unitary operations can also be implemented through block encodings, where additional ancilla qubits are introduced and later measured. While block encoding has a number of well-established theoretical applications, its practical implementation has been prohibitively expensive for current quantum hardware. In this paper, we present practical and explicit block encoding circuits implementing matrix polynomial transformations of a target matrix. With standard approaches, block-encoding a degree-$d$ matrix polynomial requires a circuit depth scaling as $d$ times the depth for block-encoding the original matrix alone. By leveraging the recently introduced Fast One-Qubit Controlled Select LCU (FOQCS-LCU) framework, we show that the additional circuit-depth overhead required for encoding matrix polynomials can be reduced to scale linearly in $d$ with no dependence on system size or the cost of block encoding the original matrix. Moreover, we demonstrate that the FOQCS-LCU circuits and their associated matrix polynomial transformations can be controlled with negligible overhead, enabling efficient applications such as Hadamard tests. Finally, we provide explicit circuits for representative spin models, together with detailed non-asymptotic gate counts and circuit depths.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18773v1
- Title: Hamiltonian Decoded Quantum Interferometry for General Pauli Hamiltonians
- Authors: Kaifeng Bu, Weichen Gu, Xiang Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18773v1  pdf=https://arxiv.org/pdf/2601.18773v1.pdf

Abstract:
In this work, we study the Hamiltonian Decoded Quantum Interferometry (HDQI) for the general Hamiltonians $H=\sum_ic_iP_i$ on an $n$-qubit system, where the coefficients $c_i\in \mathbb{R}$ and $P_i$ are Pauli operators. We show that, given access to an appropriate decoding oracle, there exist efficient quantum algorithms for preparing the state $ρ_{\mathcal P}(H) = \frac{\mathcal P^2(H)}{\text{Tr}[\mathcal P^2(H)]}$, where $\mathcal P(H)$ denotes the matrix function induced by a univariate polynomial $\mathcal P(x)$. Such states can be used to approximate the Gibbs states of $H$ for suitable choices of polynomials. We further demonstrate that the proposed algorithms are robust to imperfections in the decoding procedure. Our results substantially extend the scope of HDQI beyond stabilizer-like Hamiltonians, providing a method for Gibbs-state preparation and Hamiltonian optimization in a broad class of physically and computationally relevant quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 1712.08775v2
- Title: Note on Green Function Formalism and Topological Invariants
- Authors: Yehao Zhou, Junyu Liu
- Categories: hep-th (primary); hep-th; cond-mat.str-el; math-ph; math.AT; quant-ph
- Links: abs=https://arxiv.org/abs/1712.08775v2  pdf=https://arxiv.org/pdf/1712.08775v2.pdf

Abstract:
It has been discovered previously that the topological order parameter could be identified from the topological data of the Green's function, namely the (generalized) TKNN invariant in general dimensions, for both non-interacting and interacting systems. In this note, we show that this phenomenon has a clear geometric derivation. This proposal could be regarded as an alternative proof for the identification of the corresponding topological invariant and the topological order parameter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 1909.13808v3
- Title: $T \bar T$ and EE, with implications for (A)dS subregion encodings
- Authors: Aitor Lewkowycz, Junyu Liu, Eva Silverstein, Gonzalo Torroba
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/1909.13808v3  pdf=https://arxiv.org/pdf/1909.13808v3.pdf

Abstract:
We initiate a study of subregion dualities, entropy, and redundant encoding of bulk points in holographic theories deformed by $T \bar T$ and its generalizations. This includes both cut off versions of Anti de Sitter spacetime, as well as the generalization to bulk de Sitter spacetime, for which we introduce two additional examples capturing different patches of the bulk and incorporating the second branch of the square root dressed energy formula. We provide new calculations of entanglement entropy (EE) for more general divisions of the system than the symmetric ones previously available. We find precise agreement between the gravity side and deformed-CFT side results to all orders in the deformation parameter at large central charge. An analysis of the fate of strong subadditivity for relatively boosted regions indicates nonlocality reminiscent of string theory. We introduce the structure of operator algebras in these systems. The causal and entanglement wedges generalize to appropriate deformed theories but exhibit qualitatively new behaviors, e.g. the causal wedge may exceed the entanglement wedge. This leads to subtleties which we express in terms of the Hamiltonian and modular Hamiltonian evolution. Finally, we exhibit redundant encoding of bulk points, including the cosmological case.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.16998v1
- Title: Non-uniform modal power distribution caused by disorder in multimode fibers
- Authors: Mario Zitelli
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2601.16998v1  pdf=https://arxiv.org/pdf/2601.16998v1.pdf

Abstract:
The evolution of modal crosstalk in multimode fibers is investigated using four different experimental and numerical approaches. Results converge to demonstrate that the fiber disorder alone is capable of generating steady states characterized by non-uniform modal power distributions, which promote the lower-order modes at the expenses of the higher-order ones and are properly described by a weighted Bose-Einstein law.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17144v1
- Title: General framework for quantifying entanglement production in ultracold molecular collisions and chemical reactions
- Authors: Adrien Devolder, Paul Brumer, Timur Tscherbul
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.17144v1  pdf=https://arxiv.org/pdf/2601.17144v1.pdf

Abstract:
Entanglement, a defining feature of quantum mechanics, arises naturally from interactions between molecular systems. Yet the precise nature and quantification of entanglement in the products of molecular collisions and reactions remain largely unexplored. Here, we show that coupling between the external (motional) and internal degrees of freedom of the colliding molecules generates diverse forms of product-state entanglement: discrete-discrete, continuum-continuum, and hybrid discrete-continuum. We develop a general theoretical framework to quantify these entanglement forms directly from scattering S-matrix elements and identify a novel class of entangled states-multimode hybrid cat states, that exhibit multimode discrete-continuum entanglement. Although applicable at arbitrary collision energies, the formalism is illustrated in the ultracold and cold regimes for inelastic Rb+SrF and Rb+Sr$^+$ collisions, as well as the chemical reaction F+HD $\rightarrow$ HF+D, DF+H. We demonstrate that entanglement can be efficiently controlled near magnetic Feshbach resonances, paving the way for precise magnetic control of product-state entanglement generation in ultracold molecular collisions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17164v1
- Title: Highly accurate semiclassical strong-field Herman-Kluk propagator method for high-harmonic generation
- Authors: Phi-Hung Tran, Hao Quan Truong, R. Esteban Goetz, Anh-Thu Le
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.17164v1  pdf=https://arxiv.org/pdf/2601.17164v1.pdf

Abstract:
We extend our recently developed semiclassical strong-field Herman-Kluk propagator (SFHK) method to calculate high-order harmonic generation (HHG) for atoms in intense lasers. We show that our method, based on a combination of the Herman-Kluk propagator and the strong-field approximation, can provide highly accurate results for both HHG yield and phase, nearly identical to those from the exact numerical solutions of the time-dependent Schrödinger equation. We provide detailed analyses of our method and its applications to the HHG process, particularly the recombination time. The main computational task in this method is to solve the classical Newton equations for the active electron in the combined atomic potential and laser-electron interaction. The motion of the centers of the electron wave packets, modeled by coherent states, is governed by independent classical trajectories so that the computation can therefore be parallelized very efficiently.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17282v1
- Title: Entropic Efficiency of Bayesian Inference Protocols
- Authors: Nathan Shettell, Alexia Auffèves
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.17282v1  pdf=https://arxiv.org/pdf/2601.17282v1.pdf

Abstract:
Inference is a versatile tool that underlies scientific discovery, machine learning, and everyday decision-making: it describes how an agent updates a probability distribution as partial information is acquired from multiple measurements, reducing ignorance about a system's latent state. We define an inferential efficiency as the ratio of information gain to cumulative memory erasure cost, with inefficiency arising from unexploited correlations between the measured system and memories, and/or between memories and environment (noise). Using this efficiency, we benchmark two limiting measurement paradigms: sequential, in which the same memory is exploited iteratively, and parallel, in which many memories are exploited simultaneously. In both cases, the minimal erasure cost reflects correlations across memories: temporal in sequential, spatial in parallel. Remarkably, when all system-memory correlations are exploited for inference, both paradigms attain the same minimal erasure cost, even in the presence of noise. Conversely, the parallel paradigm performs better in the presence of unexploited correlations, stemming from hidden memories' degrees of freedom. This approach provides a quantitative, physically grounded criterion to compare inference strategies, determine their efficiency, and link target information gains to their minimal entropic cost.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17496v1
- Title: Emission of nitrogen-vacancy centers in diamond shaped by topological photonic waveguide modes
- Authors: Raman Kumar, Chandan, Gabriel I. López Morales, Richard Monge, Anton Vakulenko, Svetlana Kiriushechkina, Alexander B. Khanikaev, Johannes Flick, et al.
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2601.17496v1  pdf=https://arxiv.org/pdf/2601.17496v1.pdf

Abstract:
As the ability to integrate single photon emitters into photonic architectures improves, so does the need to characterize and understand their interaction. Here, we use a scanning diamond nanocrystal to investigate the interplay between the emission of room-temperature nitrogen-vacancy (NV) centers and a proximal topological waveguide. In our experiments, NVs serve as local, spectrally broad light sources which we exploit to characterize the waveguide bandwidth as well as the correspondence between light injection site and directionality of wave propagation. Further, we find that near-field coupling to the waveguide influences the spectral shape and ellipticity of the NV photoluminescence, hence allowing us to reveal nanostructured light fields with a spatial resolution defined by the nanoparticle size. Our results expand on the sensing modalities afforded by color centers, and portend novel opportunities in the development of on-chip, quantum optics devices leveraging topological photonics to best manipulate and readout single-photon emitters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17497v1
- Title: On the Impossibility of Simulation Security for Quantum Functional Encryption
- Authors: Mohammed Barhoush, Arthur Mehta, Anne Müller, Louis Salvail
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2601.17497v1  pdf=https://arxiv.org/pdf/2601.17497v1.pdf

Abstract:
Functional encryption is a powerful cryptographic primitive that enables fine-grained access to encrypted data and underlies numerous applications. Although the ideal security notion for FE (simulation security) has been shown to be impossible in the classical setting, those impossibility results rely on inherently classical arguments. This leaves open the question of whether simulation-secure functional encryption can be achieved in the quantum regime.   In this work, we rule out this possibility by showing that the classical impossibility results largely extend to the quantum world. In particular, when the adversary can issue an unbounded number of challenge messages, we prove an unconditional impossibility, matching the classical barrier. In the case where the adversary may obtain many functional keys, classical arguments only yield impossibility under the assumption of pseudorandom functions; we strengthen this by proving impossibility under the potentially weaker assumption of pseudorandom quantum states. In the same setting, we also establish an alternative impossibility based on public-key encryption. Since public-key encryption is not known to imply pseudorandom quantum states, this provides independent evidence of the barrier. As part of our proofs, we show a novel incompressibility property for pseudorandom states, which may be of independent interest.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17785v1
- Title: Performance Analysis of Quantum-Secure Digital Signature Algorithms in Blockchain
- Authors: Tushar Jain
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2601.17785v1  pdf=https://arxiv.org/pdf/2601.17785v1.pdf

Abstract:
The long-term security of public blockchains strictly depends on the hardness assumptions of the underlying digital signature schemes. In the current scenario, most deployed cryptocurrencies and blockchain platforms rely on elliptic-curve cryptography, which is vulnerable to quantum attacks due to Shor's algorithm. Therefore, it is important to understand how post-quantum (PQ) digital signatures behave when integrated into real blockchain systems. This report presents a blockchain prototype that supports multiple quantum-secure signature algorithms, focusing on CRYSTALS-Dilithium, Falcon and Hawk as lattice-based schemes. This report also describes the design of the prototype and discusses the performance metrics, which include key generation, signing, verification times, key sizes and signature sizes. This report covers the problem, background, and experimental methodology, also providing a detailed comparison of quantum-secure signatures in a blockchain context and extending the analysis to schemes such as HAETAE.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.17891v1
- Title: The Hamiltonian for an atom interacting with gravitational waves
- Authors: Linda M. van Manen, André Grossardt
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2601.17891v1  pdf=https://arxiv.org/pdf/2601.17891v1.pdf

Abstract:
Building on the relativistic Hamiltonian of Sonnleitner and Barnett arXiv:1806.00234 and its post-Newtonian extensions by Schwartz and Giuilini arXiv:1908.06929, we investigate composite atomic systems in dynamical gravitational backgrounds. Using a local inertial frame and a perturbed Minkowski metric, we derive curvature-dependent corrections to both center-of-mass and internal Hamiltonians for atoms interacting with weak gravitational waves. The resulting Hamiltonian contains distinct curvature couplings modifying the internal potential and affecting the center-of-mass dynamics. These contributions imply that internal-energy variations do not always reduce to mass renormalization and can induce genuine forces due to changes in momentum. The initial research was motivated by anomalous friction-like forces emerging in quantum optics, and clarified that the anomalous forces are mere relativistic corrections from mass-energy equivalence. Our results suggest that, with increasingly sensitive detectors, additional forces from gravitational wave interactions may become visible in future experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18232v1
- Title: Complex-Valued-Matrix Permanents: SPA-based Approximations and Double-Cover Analysis
- Authors: Junda Zhou, Pascal O. Vontobel
- Categories: cs.IT (primary); cs.IT; math.CO; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18232v1  pdf=https://arxiv.org/pdf/2601.18232v1.pdf

Abstract:
Approximating the permanent of a complex-valued matrix is a fundamental problem with applications in Boson sampling and probabilistic inference. In this paper, we extend factor-graph-based methods for approximating the permanent of non-negative-real-valued matrices that are based on running the sum-product algorithm (SPA) on standard normal factor graphs, to factor-graph-based methods for approximating the permanent of complex-valued matrices that are based on running the SPA on double-edge normal factor graphs.   On the algorithmic side, we investigate the behavior of the SPA, in particular how the SPA fixed points change when transitioning from real-valued to complex-valued matrix ensembles. On the analytical side, we use graph covers to analyze the Bethe approximation of the permanent, i.e., the approximation of the permanent that is obtained with the help of the SPA.   This combined algorithmic and analytical perspective provides new insight into the structure of Bethe approximations in complex-valued problems and clarifies when such approximations remain meaningful beyond the non-negative-real-valued settings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18248v1
- Title: A particle on a ring or: how I learned to stop worrying and love $θ$-vacua
- Authors: Mohammad Aghaie, Ryosuke Sato
- Categories: hep-ph (primary); hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18248v1  pdf=https://arxiv.org/pdf/2601.18248v1.pdf

Abstract:
Recently, Ai, Cruz, Garbrecht, and Tamarit (ACGT)~\cite{Ai:2020ptm, Ai:2024vfa, Ai:2024cnp, Ai:2025quf} claimed that there is no strong CP problem by adopting a new order of limits in the volume and topological sector. We critically examine this proposal by focusing on simple one-dimensional quantum mechanics on a ring. We demonstrate that consistent results are obtained only when one sums over all topological sectors \textit{before} taking the large $T$ limit. This observation justifies the conventional path integral formulation of gauge theories and implies that the strong CP problem does exist in QCD.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18331v1
- Title: Quantum Hyperuniformity and Quantum Weight
- Authors: Junmo Jeon, Shiro Sakai
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.dis-nn; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18331v1  pdf=https://arxiv.org/pdf/2601.18331v1.pdf

Abstract:
Extending hyperuniformity from classical to quantum fluctuations in electron systems yields a framework that identifies quantum phase transitions and reveals underlying gap structures through the quantum weight. We study long-wavelength fluctuations of many-body ground states through the charge-density structure factor by incorporating intrinsic quantum fluctuations into hyperuniformity. Although charge fluctuations at zero temperature are generally suppressed by particle-number conservation, their long-wavelength scaling reveals distinct universal behaviors that define quantum hyperuniformity classes. By exemplifying the Aubry-Andre model, we find that gapped, gapless, and localized-critical-extended phases are sharply distinguished by the quantum hyperuniformity classes. Notably, at the critical point, multifractal wave functions generate anomalous scaling behavior. We further show that, in quantum-hyperuniform gapped phases, the quantum weight provides a quantitative measure of the gap size through a universal power-law scaling. Along with classical hyperuniformity, quantum hyperuniformity serves a direct fingerprint of quantum criticality and a practical probe of quantum phase transitions in aperiodic electron systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18413v1
- Title: Fundamentals, Recent Advances, and Challenges Regarding Cryptographic Algorithms for the Quantum Computing Era
- Authors: Darlan Noetzold, Valderi Reis Quietinho Leithardt
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18413v1  pdf=https://arxiv.org/pdf/2601.18413v1.pdf

Abstract:
This book arises from the need to provide a clear and up-to-date overview of the impacts of quantum computing on cryptography. The goal is to provide a reference in Portuguese for undergraduate, master's, and doctoral students in the field of data security and cryptography. Throughout the chapters, we present fundamentals, we discuss classical and post-quantum algorithms, evaluate emerging patterns, and point out real-world implementation challenges. The initial objective is to serve as a guide for students, researchers, and professionals who need to understand not only the mathematics involved, but also its practical implications in security systems and policies. For more advanced professionals, the main objective is to present content and ideas so that they can assess the changes and perspectives in the era of quantum cryptographic algorithms. To that end, the text's structure was designed to be progressive: we begin with essential concepts, move on to quantum algorithms and their consequences (with emphasis on Shor's algorithm), present issues focusing on "families" of post-quantum schemes (based on lattices, codes, hash functions, multivariate, isogenies), analyze the state of the art in standardization (highlighting the NIST process), and finally, discuss migration, interoperability, performance, and cryptographic governance. We hope that this work will assist in the formation of critical thinking and informed technical decision-making, fostering secure transition strategies for the post-quantum era.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18449v1
- Title: Hamiltonian formulation of the $1+1$-dimensional $φ^4$ theory in a momentum-space Daubechies wavelet basis
- Authors: Mrinmoy Basak, Debsubhra Chakraborty, Nilmani Mathur, Raghunath Ratabole
- Categories: hep-th (primary); hep-th; hep-ex; hep-lat; hep-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18449v1  pdf=https://arxiv.org/pdf/2601.18449v1.pdf

Abstract:
We apply the wavelet formalism of quantum field theory to investigate nonperturbative dynamics within the Hamiltonian framework. In particular, we employ Daubechies wavelets in momentum space, whose basis functions are labeled by resolution and translation indices, providing a natural nonperturbative truncation of both infrared and ultraviolet truncation of quantum field theories. As an application, we compute the energy spectra of a free scalar field theory and the interacting $1+1$-dimensional $φ^4$ theory. This approach successfully reproduces the well-known strong-coupling phase transition in the $m^2 > 0$ regime. We find that the extracted critical coupling systematically converges toward its established value as the momentum resolution is increased, demonstrating the effectiveness of the wavelet-based Hamiltonian formulation for nonperturbative field-theoretic calculations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18458v1
- Title: Measurement induced faster symmetry restoration in quantum trajectories
- Authors: Katha Ganguly, Bijay Kumar Agarwalla
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18458v1  pdf=https://arxiv.org/pdf/2601.18458v1.pdf

Abstract:
Continuous measurement of quantum systems provides a standard route to quantum trajectories through the successive acquisition of information which further results in measurement back-action. In this work, we harness this back-action as a resource for global $U(1)$ symmetry restoration where continuous measurement is combined with a $U(1)$-preserving unitary evolution. Starting from a $U(1)$ symmetry-broken initial state, we simulate quantum trajectories generated by continuous measurements of both global and local observables. We show that under global monitoring, states containing superpositions of distant charge sectors restore symmetry faster than those involving nearby sectors. We establish the universality of this behavior across different measurement protocols. Finally, we demonstrate that local monitoring can further accelerate symmetry restoration for certain states that relax slowly under global monitoring.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18655v1
- Title: Quantum Rotation Diversity in Displaced Squeezed Binary Phase-Shift Keying
- Authors: Ioannis Krikidis
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18655v1  pdf=https://arxiv.org/pdf/2601.18655v1.pdf

Abstract:
We propose a quantum rotation diversity (QRD) scheme for optical quantum communication using binary phase-shift-keying displaced squeezed states and homodyne detection over Gamma-Gamma turbulence channels. Consecutive temporal modes are coupled by a passive orthogonal rotation that redistributes the displacement amplitude between slots, yielding a diversity order of two under independent fading and joint maximum-likelihood detection. Analytical expressions for the symbol-error rate performance, along with asymptotic results for the diversity and coding gains, are derived. The optimal rotation angle and energy allocation between displacement and squeezing are obtained in closed form. Furthermore, we show that when both the displacement amplitude and the squeezing strength scale with the total photon number, an effective diversity order of four is achieved. Numerical results validate the analysis and demonstrate the super-diversity behaviour of the proposed QRD scheme.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18710v1
- Title: Analyzing Images of Blood Cells with Quantum Machine Learning Methods: Equilibrium Propagation and Variational Quantum Circuits to Detect Acute Myeloid Leukemia
- Authors: A. Bano, L. Liebovitch
- Categories: cs.ET (primary); cs.ET; cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18710v1  pdf=https://arxiv.org/pdf/2601.18710v1.pdf

Abstract:
This paper presents a feasibility study demonstrating that quantum machine learning (QML) algorithms achieve competitive performance on real-world medical imaging despite operating under severe constraints. We evaluate Equilibrium Propagation (EP), an energy-based learning method that does not use backpropagation (incompatible with quantum systems due to state-collapsing measurements) and Variational Quantum Circuits (VQCs) for automated detection of Acute Myeloid Leukemia (AML) from blood cell microscopy images using binary classification (2 classes: AML vs. Healthy).   Key Result: Using limited subsets (50-250 samples per class) of the AML-Cytomorphology dataset (18,365 expert-annotated images), quantum methods achieve performance only 12-15% below classical CNNs despite reduced image resolution (64x64 pixels), engineered features (20D), and classical simulation via Qiskit. EP reaches 86.4% accuracy (only 12% below CNN) without backpropagation, while the 4-qubit VQC attains 83.0% accuracy with consistent data efficiency: VQC maintains stable 83% performance with only 50 samples per class, whereas CNN requires 250 samples (5x more data) to reach 98%. These results establish reproducible baselines for QML in healthcare, validating NISQ-era feasibility.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.18746v1
- Title: Coherent control of photon pairs via quantum interference between second- and third-order quantum nonlinear processes
- Authors: Alessia Stefano, Samuel E. Fontaine, J. E. Sipe, Marco Liscidini
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18746v1  pdf=https://arxiv.org/pdf/2601.18746v1.pdf

Abstract:
Genuine quantum interference between independent nonlinear processes of different order provides a route to coherent control that cannot be reduced to a classical field interference. Here we present an all-optical analogue of coherent carrier injection by exploiting interference between second- and third-order quantum nonlinear processes in an integrated photonic platform. Photon pairs generated via spontaneous parametric down-conversion and spontaneous four-wave mixing coherently contribute to the same final two-photon state, resulting in a phase-dependent modulation of both the generation rate and the spectral structure of the emitted biphoton state. We illustrate the features of such interference and how it can be used to shape biphoton wavefunctions and their quantum correlations. These results identify interference between nonlinear processes of different order as a distinct form of coherent quantum control within quantum nonlinear optics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2310.19296v2
- Title: Complex-valued Wigner entropy of a quantum state
- Authors: Nicolas J. Cerf, Anaelle Hertz, Zacharie Van Herstraeten
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2310.19296v2  pdf=https://arxiv.org/pdf/2310.19296v2.pdf

Abstract:
It is common knowledge that the Wigner function of a quantum state may admit negative values, so that it cannot be viewed as a genuine probability density. Here, we examine the difficulty in finding an entropy-like functional in phase space that extends to negative Wigner functions and then advocate the merits of defining a complex-valued entropy associated with any Wigner function. This quantity, which we call the complex Wigner entropy, is defined via the analytic continuation of Shannon's differential entropy of the Wigner function in the complex plane. We show that the complex Wigner entropy enjoys interesting properties, especially its real and imaginary parts are both invariant under Gaussian unitaries (displacements, rotations, and squeezing in phase space). Its real part is physically relevant when considering the evolution of the Wigner function under a Gaussian convolution, while its imaginary part is simply proportional to the negative volume of the Wigner function. Finally, we define the complex-valued Fisher information of any Wigner function, which is linked (via an extended de Bruijn's identity) to the time derivative of the complex Wigner entropy when the state undergoes Gaussian additive noise. Overall, it is anticipated that the complex plane yields a proper framework for analyzing the entropic properties of quasiprobability distributions in phase space.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2401.11980v3
- Title: On the uniqueness of compiling graphs under the parity transformation
- Authors: Florian Dreier, Wolfgang Lechner
- Categories: quant-ph (primary); quant-ph; math-ph; math.CO
- Links: abs=https://arxiv.org/abs/2401.11980v3  pdf=https://arxiv.org/pdf/2401.11980v3.pdf

Abstract:
In this article, we establish a mathematical framework that utilizes concepts from graph theory to formalize the parity transformation, an encoding strategy for compiling optimization problems on quantum devices. We introduce the transformation as a mapping that encompasses all possible compiled hypergraphs and investigate its uniqueness properties in more detail. Specifically, by introducing so-called loop labelings, we derive an alternative expression of the preimage of any set of compiled hypergraphs under this encoding procedure when all equivalence classes of graphs are being considered. We then deduce equivalent conditions for the injectivity of the parity transformation on any subset of all equivalences classes of graphs. Through concrete examples, we demonstrate that the parity transformation is not an injective mapping, and also introduce an important class of physical layouts and their corresponding set of constraints whose preimage is uniquely determined. In addition, we provide an algorithm which is based on classical algorithms from theoretical computer science and computes a compiled physical layout in this class in polynomial time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2404.13545v4
- Title: Two remote counting events induced by a single photon
- Authors: Lida Zhang
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2404.13545v4  pdf=https://arxiv.org/pdf/2404.13545v4.pdf

Abstract:
Motivated by Einstein's thought experiment that a single quantum particle diffracted after a pinhole could in principle produce an action in two or several places on a hemispherical imaging screen, here we explore theoretically the possibility to simultaneously detect the action of a single photon at two remote places. This is considered in a cascade quantum system composed of two spatially distant cavities each coupled to a qubit in the ultrastrong coupling regime. We show that a single-photon pulse incident on the two cavities can simultaneously excite the two remote qubits and lead to two subsequent single-photon detection events even when the separation between them is comparable to the spatial length of the photon pulse. Our results not only uncover new facets of photons at a fundamental level but also have practical applications, such as the generation of remote entanglement by a single photon through a dissipative channel which is otherwise unattainable in the strong-coupling regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2404.14258v3
- Title: Quantum-Enhanced Neural Exchange-Correlation Functionals
- Authors: Igor O. Sokolov, Gert-Jan Both, Art D. Bochevarov, Pavel A. Dub, Daniel S. Levine, Christopher T. Brown, Shaheen Acheche, Panagiotis Kl. Barkoutsos, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cond-mat.str-el; physics.chem-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2404.14258v3  pdf=https://arxiv.org/pdf/2404.14258v3.pdf

Abstract:
Kohn-Sham Density Functional Theory (KS-DFT) provides the exact ground state energy and electron density of a molecule, contingent on the as-yet-unknown universal exchange-correlation (XC) functional. Recent research has demonstrated that neural networks can efficiently learn to represent approximations to that functional, offering accurate generalizations to molecules not present during the training process. With the latest advancements in quantum-enhanced machine learning (ML), evidence is growing that Quantum Neural Network (QNN) models may offer advantages in ML applications. In this work, we explore the use of QNNs for representing XC functionals, enhancing and comparing them to classical ML techniques. We present QNNs based on differentiable quantum circuits (DQCs) as quantum (hybrid) models for XC in KS-DFT, implemented across various architectures. We assess their performance on 1D and 3D systems. To that end, we expand existing differentiable KS-DFT frameworks and propose strategies for efficient training of such functionals, highlighting the importance of fractional orbital occupation for accurate results. Our best QNN-based XC functional yields energy profiles of the H$_2$ and planar H$_4$ molecules that deviate by no more than 1 mHa from the reference DMRG and FCI/6-31G results, respectively. Moreover, they reach chemical precision on a system, H$_2$H$_2$, not present in the training dataset, using only a few variational parameters. This work lays the foundation for the integration of quantum models in KS-DFT, thereby opening new avenues for expressing XC functionals in a differentiable way and facilitating computations of various properties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2405.10360v2
- Title: Adversarial Robustness Guarantees for Quantum Classifiers
- Authors: Neil Dowling, Maxwell T. West, Angus Southwell, Azar C. Nakhl, Martin Sevior, Muhammad Usman, Kavan Modi
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cs.LG; nlin.CD
- Links: abs=https://arxiv.org/abs/2405.10360v2  pdf=https://arxiv.org/pdf/2405.10360v2.pdf

Abstract:
Despite their ever more widespread deployment throughout society, machine learning algorithms remain critically vulnerable to being spoofed by subtle adversarial tampering with their input data. The prospect of near-term quantum computers being capable of running {quantum machine learning} (QML) algorithms has therefore generated intense interest in their adversarial vulnerability. Here we show that quantum properties of QML algorithms can confer fundamental protections against such attacks, in certain scenarios guaranteeing robustness against classically-armed adversaries. We leverage tools from many-body physics to identify the quantum sources of this protection. Our results offer a theoretical underpinning of recent evidence which suggest quantum advantages in the search for adversarial robustness. In particular, we prove that quantum classifiers are: (i) protected against weak perturbations of data drawn from the trained distribution, (ii) protected against local attacks if they are insufficiently scrambling, and (iii) show evidence that they are protected against universal adversarial attacks if they are sufficiently chaotic. Our analytic results are supported by numerical evidence demonstrating the applicability of our theorems and the resulting robustness of a quantum classifier in practice. This line of inquiry constitutes a concrete pathway to advantage in QML, orthogonal to the usually sought improvements in model speed or accuracy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2407.07876v3
- Title: Approximate Unitary $k$-Designs from Shallow, Low-Communication Circuits
- Authors: Nicholas LaRacuente, Felix Leditzky
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2407.07876v3  pdf=https://arxiv.org/pdf/2407.07876v3.pdf

Abstract:
Random unitaries are useful in quantum information and related fields, but hard to generate with limited resources. An approximate unitary $k$-design is an ensemble of unitaries with an underlying measure over which the average is close to a Haar random ensemble up to the first $k$ moments. A particularly strong notion of approximation bounds the distance from Haar randomness in relative error. Such relative-error approximate designs are secure against queries by an adaptive adversary trying to distinguish it from a Haar ensemble. We construct relative-error approximate unitary $k$-design ensembles for which communication between subsystems is $O(1)$ in the system size. These constructions use the alternating projection method to analyze overlapping Haar averages, giving a bound on the convergence speed to the full averaging with respect to the $2$-norm. Using von Neumann subalgebra indices to replace system dimension, the 2-norm distance converts to relative error without introducing any additional dimension dependence. We use these constructions as the building blocks of a two-step protocol that achieves a relative-error design in $O \big ( (\log m + \log(1/ε) + k \log k ) k\, \text{polylog}(k) \big )$ depth, where $m$ is the number of qudits in the complete system and $ε$ the approximation error. This sublinear depth construction answers a variant of [Harrow and Mehraban 2023, Section 1.5, Open Questions 1 and 7]. Moreover, entanglement generated by the sublinear depth scheme follows area laws on spatial lattices up to corrections logarithmic in the full system size.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2407.10635v3
- Title: NPA Hierarchy for Quantum Isomorphism and Homomorphism Indistinguishability
- Authors: Prem Nigam Kar, David E. Roberson, Tim Seppelt, Peter Zeman
- Categories: quant-ph (primary); quant-ph; cs.DM; cs.DS; math.CO; math.OC
- Links: abs=https://arxiv.org/abs/2407.10635v3  pdf=https://arxiv.org/pdf/2407.10635v3.pdf

Abstract:
Mančinska and Roberson [FOCS'20] showed that two graphs are quantum isomorphic if and only if they admit the same number of homomorphisms from any planar graph. Atserias et al. [JCTB'19] proved that quantum isomorphism is undecidable in general, which motivates the study of its relaxations. In the classical setting, Roberson and Seppelt [ICALP'23] characterized the feasibility of each level of the Lasserre hierarchy of semidefinite programming relaxations of graph isomorphism in terms of equality of homomorphism counts from an appropriate graph class. The NPA hierarchy, a noncommutative generalization of the Lasserre hierarchy, provides a sequence of semidefinite programming relaxations for quantum isomorphism. In the quantum setting, we show that the feasibility of each level of the NPA hierarchy for quantum isomorphism is equivalent to equality of homomorphism counts from an appropriate class of planar graphs. Combining this characterization with the convergence of the NPA hierarchy, and noting that the union of these classes is the set of all planar graphs, we obtain a new proof of the result of Mančinska and Roberson [FOCS'20] that avoids the use of quantum groups. Moreover, this homomorphism indistinguishability characterization also yields a randomized polynomial-time algorithm deciding exact feasibility of each fixed level of the NPA hierarchy of SDP relaxations for quantum isomorphism.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2408.11902v2
- Title: One-to-One Correspondence between Deterministic Port-Based Teleportation and Unitary Estimation
- Authors: Satoshi Yoshida, Yuki Koizumi, Michał Studziński, Marco Túlio Quintino, Mio Murao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2408.11902v2  pdf=https://arxiv.org/pdf/2408.11902v2.pdf

Abstract:
Port-based teleportation is a variant of quantum teleportation, where the receiver can choose one of the ports in his part of the entangled state shared with the sender, but cannot apply other recovery operations. We show that the optimal fidelity of deterministic port-based teleportation (dPBT) using $N=n+1$ ports to teleport a $d$-dimensional state is equivalent to the optimal fidelity of $d$-dimensional unitary estimation using $n$ calls of the input unitary operation. From any given dPBT, we can explicitly construct the corresponding unitary estimation protocol achieving the same optimal fidelity, and vice versa. Using the obtained one-to-one correspondence between dPBT and unitary estimation, we derive the asymptotic optimal fidelity of port-based teleportation given by $1-O(d^4)N^{-2}\leq F \leq 1-Ω(d^4)N^{-2}$, which improves the previously known result given by $1-O(d^5)N^{-2} \leq F \leq 1-Ω(d^2) N^{-2}$. We also show that the optimal fidelity of unitary estimation for the case $n\leq d-1$ is $F = {n+1 \over d^2}$, and this fidelity is equal to the optimal fidelity of unitary inversion with $n\leq d-1$ calls of the input unitary operation even if we allow indefinite causal order among the calls.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2411.05562v2
- Title: Wigner entropy conjecture and the interference formula in quantum phase space
- Authors: Zacharie Van Herstraeten, Nicolas J. Cerf
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2411.05562v2  pdf=https://arxiv.org/pdf/2411.05562v2.pdf

Abstract:
Wigner-positive quantum states have the peculiarity to admit a Wigner function that is a genuine probability distribution over phase space. The Shannon differential entropy of the Wigner function of such states -- called Wigner entropy for brevity -- emerges as a fundamental information-theoretic measure in phase space and is subject to a conjectured lower bound, reflecting the uncertainty principle. In this work, we prove that this Wigner entropy conjecture holds true for a broad class of Wigner-positive states known as beam-splitter states, which are obtained by evolving a separable state through a balanced beam splitter and then discarding one mode. Our proof relies on known bounds on the $p$-norms of cross Wigner functions and on the interference formula, which relates the convolution of Wigner functions to the squared modulus of a cross Wigner function. Originally discussed in the context of signal analysis, the interference formula is not commonly used in quantum optics although it unveils a strong symmetry under convolution exhibited by Wigner functions of pure states. We provide here a simple proof of the formula and highlight some of its implications. Finally, we prove an extended conjecture on the Wigner-Rényi entropy of beam-splitter states, albeit in a restricted range for the Rényi parameter $α\geq 1/2$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2412.08626v3
- Title: Numerical study of computational cost of maintaining adiabaticity for long paths
- Authors: Thomas D. Cohen, Hyunwoo Oh, Veronica Wang
- Categories: quant-ph (primary); quant-ph; hep-lat; nucl-th
- Links: abs=https://arxiv.org/abs/2412.08626v3  pdf=https://arxiv.org/pdf/2412.08626v3.pdf

Abstract:
Recent work argued that the scaling of a dimensionless quantity $Q_D$ with path length is a better proxy for quantifying the scaling of the computational cost of maintaining adiabaticity than the timescale. It also conjectured that generically the scaling will be superlinear (although special cases exist in which it is linear). The quantity $Q_D$ depends only on the properties of ground states along the Hamiltonian path and the rate at which the path is followed. In this paper, we demonstrate that this conjecture holds for simple Hamiltonian systems that can be studied numerically. In particular, the systems studied exhibit the behavior that $Q_D$ grows approximately as $L \log L$ where $L$ is the path length when the threshold error is fixed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2412.11782v2
- Title: Conveyor-belt superconducting quantum computer
- Authors: Francesco Cioni, Roberto Menta, Riccardo Aiudi, Marco Polini, Vittorio Giovannetti
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2412.11782v2  pdf=https://arxiv.org/pdf/2412.11782v2.pdf

Abstract:
The processing unit of a solid-state quantum computer consists in an array of coupled qubits, each locally driven with on-chip microwave lines that route carefully-engineered control signals to the qubits in order to perform logical operations. This approach to quantum computing comes with two major problems. On the one hand, it greatly hampers scalability towards fault-tolerant quantum computers, which are estimated to need a number of qubits -- and, therefore driving lines -- on the order of $10^6$. On the other hand, these lines are a source of electromagnetic noise, exacerbating frequency crowding and crosstalk, while also contributing to power dissipation inside the dilution fridge. We here tackle these two overwhelming challenges by presenting a novel quantum processing unit (QPU) for a universal quantum computer which is globally (rather than locally) driven. Our QPU relies on a string of superconducting qubits with always-on ZZ interactions, enclosed into a closed geometry, which we dub ``conveyor belt''. Strikingly, this architecture requires only $\mathcal{O}(N)$ physical qubits to run a computation on $N$ computational qubits, in contrast to previous $\mathcal{O}(N^2)$ proposals for global quantum computation. Additionally, universality is achieved via the implementation of single-qubit gates and a one-shot Toffoli gate. The ability to perform multi-qubit operations in a single step could vastly improve the fidelity and execution time of many algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2502.02652v2
- Title: Lieb-Robinson bounds with exponential-in-volume tails
- Authors: Ben T. McDonough, Chao Yin, Andrew Lucas, Carolyn Zhang
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; math-ph
- Links: abs=https://arxiv.org/abs/2502.02652v2  pdf=https://arxiv.org/pdf/2502.02652v2.pdf

Abstract:
Lieb-Robinson bounds demonstrate the emergence of locality in many-body quantum systems. Intuitively, Lieb-Robinson bounds state that with local or exponentially decaying interactions, the correlation that can be built up between two sites separated by distance $r$ after a time $t$ decays as $\exp(vt-r)$, where $v$ is the emergent Lieb-Robinson velocity. In many problems, it is important to also capture how much of an operator grows to act on $r^d$ sites in $d$ spatial dimensions. Perturbation theory and cluster expansion methods suggest that at short times, these volume-filling operators are suppressed as $\exp(-r^d)$ at short times. We confirm this intuition, showing that for $r > vt$, the volume-filling operator is suppressed by $\exp(-(r-vt)^d/(vt)^{d-1})$. This closes a conceptual and practical gap between the cluster expansion and the Lieb-Robinson bound. We then present two very different applications of this new bound. Firstly, we obtain improved bounds on the classical computational resources necessary to simulate many-body dynamics with error tolerance $ε$ for any finite time $t$: as $ε$ becomes sufficiently small, only $ε^{-O(t^{d-1})}$ resources are needed. A protocol that likely saturates this bound is given. Secondly, we prove that disorder operators have volume-law suppression near the "solvable (Ising) point" in quantum phases with spontaneous symmetry breaking, which implies a new diagnostic for distinguishing many-body phases of quantum matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2502.03413v4
- Title: Polarization entanglement and qubit error rate dependence on the exciton-phonon coupling in self-assembled quantum dots
- Authors: Urmimala Dewan, Parvendra Kumar, Amarendra K. Sarma
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2502.03413v4  pdf=https://arxiv.org/pdf/2502.03413v4.pdf

Abstract:
Polarization-entangled photons are key resources for a wide range of protocols in quantum computation and quantum key distribution. Achieving a near-unity degree of polarization entanglement is essential for minimizing qubit error rates in secure key distribution. In this work, we theoretically investigate polarization-entangled photon pairs generated via a quantum-dot radiative cascade embedded in a micropillar cavity. To account for the unavoidable exciton-phonon interactions in the quantum dot-cavity system, we develop a polaron master-equation framework and examine its impact on the degree of entanglement and the resulting qubit error rate. We derive analytical expressions for phonon-induced incoherent scattering rates and show that one-photon incoherent processes dominate, leading to a substantial reduction of entanglement. We further demonstrate that at elevated phonon-bath temperatures, cavity-mediated effects, such as cross-coupling between exciton states, ac Stark shifts, and multiphoton emission, are significantly suppressed due to phonon-induced renormalization of the cavity coupling strength and the Rabi frequency. Finally, we analyze a BBM92 quantum key distribution protocol and study the evolution of the qubit error rate as a function of the phonon-bath temperature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2502.20558v3
- Title: Leveraging Qubit Loss Detection in Fault Tolerant Quantum Algorithms
- Authors: Gefen Baranes, Madelyn Cain, J. Pablo Bonilla Ataides, Dolev Bluvstein, Josiah Sinclair, Vladan Vuletic, Hengyun Zhou, Mikhail D. Lukin
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2502.20558v3  pdf=https://arxiv.org/pdf/2502.20558v3.pdf

Abstract:
Qubit loss errors constitute a dominant source of noise in many quantum hardware systems, particularly in neutral atom quantum computers. We develop a theoretical framework to effectively detect and correct loss errors in logical algorithms and leverage such loss information in decoding. Considering general quantum error correction codes and logical circuits, we introduce a delayed-erasure decoder for experimentally-motivated error models which leverages information from delayed loss detection to accurately correct loss errors, even when the precise moment of the error is unknown. Using this decoder, we identify strategies for detecting and correcting loss errors based on the logical circuit structure. For deep circuits prior to logical measurement, we explore methods to integrate loss detection into syndrome extraction with minimal overhead, identifying optimal strategies depending on the qubit loss fraction in the noise and hardware capabilities. In contrast, we find that many key algorithmic subroutines involve frequent gate teleportation, shortening the circuit depth before logical measurement and naturally replacing qubits with no additional experimental overhead. We simulate this setting using a toy model algorithm for small-angle synthesis, and find a significant performance improvement as the loss fraction increases. These results provide a path forward for advancing large-scale fault tolerant quantum computation in systems with loss error detection.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2503.06977v4
- Title: Experimental observation of non-Markovian quantum exceptional points
- Authors: Hao-Long Zhang, Pei-Rong Han, Fan Wu, Wen Ning, Zhen-Biao Yang, Shi-Biao Zheng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.06977v4  pdf=https://arxiv.org/pdf/2503.06977v4.pdf

Abstract:
One of the most remarkable features that distinguish open systems from closed ones is the presence of exceptional points (EPs), where two or more eigenvectors of a non-Hermitian operator coalesce, accompanying the convergence of the correcponding eigenvalues. So far, EPs have been demonstrated on a number of platforms, ranging from classical optical systems to fully quantum-mechanical spin-boson models. In these demonstrations, the reservoir that induced the non-Hermiticity was treated as a Markovian one, without considering its memory effect. We here present the first experimental demonstration of non-Markovian quantum EPs, engineered by coupling a Josephson-junction-based qubit to a leaky electromagnetic resonator, which acts as a non-Markovian reservoir. We map out the spectrum of the extended Liouvillian superoperator by observing the quantum state evolution of the qubit and the pseudomode, in which the memory of the reservoir is encoded. We identify a two-fold second-order EP and a third-order EP in the Liouvillian spectrum, which cannot be realized with a Markovian reservoir. Our results pave the way for experimental exploration of exotic phenomena associated with non-Markovian quantum EPs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2503.12789v2
- Title: Lower bounding the MaxCut of high girth 3-regular graphs using the QAOA
- Authors: Edward Farhi, Sam Gutmann, Daniel Ranard, Benjamin Villalonga
- Categories: quant-ph (primary); quant-ph; cs.DM; math.CO
- Links: abs=https://arxiv.org/abs/2503.12789v2  pdf=https://arxiv.org/pdf/2503.12789v2.pdf

Abstract:
We study MaxCut on 3-regular graphs of minimum girth $g$ for various $g$'s. We obtain new lower bounds on the maximum cut achievable in such graphs by analyzing the Quantum Approximate Optimization Algorithm (QAOA). For $g \geq 16$, at depth $p \geq 7$, the QAOA improves on previously known lower bounds. Our bounds are established through classical numerical analysis of the QAOA's expected performance. This analysis does not produce the actual cuts but establishes their existence. When implemented on a quantum computer, the QAOA provides an efficient algorithm for finding such cuts, using a constant-depth quantum circuit. To our knowledge, this gives an exponential speedup over the best known classical algorithm guaranteed to achieve cuts of this size on graphs of this girth. We also apply the QAOA to the Maximum Independent Set problem on the same class of graphs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2503.15843v2
- Title: Reducing T Gates with Unitary Synthesis
- Authors: Tianyi Hao, Amanda Xu, Swamit Tannu
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2503.15843v2  pdf=https://arxiv.org/pdf/2503.15843v2.pdf

Abstract:
Quantum error correction is essential for achieving practical quantum computing but has a significant computational overhead. Among fault-tolerant (FT) gate operations, non-Clifford gates, such as $T$, are particularly expensive due to their reliance on magic state distillation. These costly $T$ gates appear frequently in FT circuits as many quantum algorithms require arbitrary single-qubit rotations, such as $R_x$ and $R_z$ gates, which must be decomposed into a sequence of $T$ and Clifford gates. In many quantum circuits, $R_x$ and $R_z$ gates can be fused to form a single $U3$ unitary. However, existing synthesis methods, such as Gridsynth, rely on indirect decompositions, requiring separate $R_z$ decompositions that result in a threefold increase in $T$ count.   This work presents TensoR-based Arbitrary unitary SYNthesis (trasyn), a novel FT synthesis algorithm that directly synthesizes arbitrary single-qubit unitaries, avoiding the overhead of separate $R_z$ decompositions. By leveraging tensor network-based search, our approach enables native $U3$ synthesis, reducing the $T$ count, Clifford gate count, and approximation error. Compared to Gridsynth-based circuit synthesis, for 187 representative benchmarks, our design reduces the T count by up to 3.5$\times$, and Clifford gates by 7$\times$, resulting in up to 4$\times$ improvement in overall circuit infidelity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2503.18772v4
- Title: Characterization of a quantum bus between two driven qubits
- Authors: Alberto Hijano, Henri Lyyra, Juha T. Muhonen, Tero T. Heikkilä
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.18772v4  pdf=https://arxiv.org/pdf/2503.18772v4.pdf

Abstract:
We investigate the use of driven qubits coupled to a harmonic oscillator to implement a $\sqrt{i\mathrm{SWAP}}$-gate. By dressing the qubits through an external driving field, the qubits and the harmonic oscillator can be selectively coupled, allowing for the measurement of individual qubit states, as well as leading to effective qubit-qubit interactions. We compare the qubit readout on bare and dressed qubits, and demonstrate that when coupled to low-frequency resonators, dressed qubits provide a more robust readout than bare qubits in the presence of damping and thermal effects. Furthermore, we study the impact of various system parameters on the fidelity of the two-qubit gate, identifying an optimal range for quantum computation. Our findings guide the implementation of high-fidelity quantum gates in experimental setups, for example those employing nanoscale mechanical resonators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2505.12873v2
- Title: Quantum Algorithms for Causal Estimands
- Authors: Rishi Goel, Casey R. Myers, Sally Shrapnel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.12873v2  pdf=https://arxiv.org/pdf/2505.12873v2.pdf

Abstract:
Modern machine learning (ML) methods typically fail to adequately capture causal information. Consequently, such models do not handle data distributional shifts, are vulnerable to adversarial examples, and often learn spurious correlations. Causal ML, or causal inference, aims to solve these issues by estimating the expected outcome of counterfactual events, using observational and/or interventional data, where causal relationships are typically depicted as directed acyclic graphs. It is an open question as to whether these causal algorithms provide opportunities for quantum enhancement. In this paper we consider a recently developed family of non-parametric, continuous causal estimators and derive quantum algorithms for these tasks. Kernel evaluation and large matrix inversion are critical sub-routines of these classical algorithms, which makes them particularly amenable to a quantum treatment. Unlike other quantum ML algorithms, closed form solutions for the estimators exist, negating the need for gradient evaluation and variational learning. We describe several new hybrid quantum-classical algorithms and show that uniform consistency of the estimators is retained. Furthermore, if one is satisfied with a quantum state output that is proportional to the true causal estimand, then these algorithms inherit the exponential complexity advantages given by quantum linear system solvers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2505.13717v3
- Title: Symmetry-guided quantum state preparation: Branched-Subspaces Adiabatic Preparation (B-SAP)
- Authors: Davide Cugini, Giacomo Guarnieri, Mario Motta, Dario Gerace
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.13717v3  pdf=https://arxiv.org/pdf/2505.13717v3.pdf

Abstract:
Quantum state preparation lies at the heart of quantum computation and quantum simulations, enabling the investigation of complex manybody systems across physics, chemistry, and data science. While existing methods such as Variational Quantum Algorithms (VQAs) and Adiabatic Preparation (AP) offer viable pathways, both face substantial limitations. Here we introduce a hybrid algorithm that integrates the conceptual strengths of both VQAs and AP, enhanced via the use of group-theoretic structures and classical post-processing to approximate ground and excited states of many-body Hamiltonian models. We validate our approach by applying it to the one-dimensional XYZ Heisenberg model with periodic boundary conditions, evaluating its performance across a broad range of parameters and system sizes. Our results show accurate preparation of low-energy eigenstates, achieved with circuit depths with polynomial scaling versus system size.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2506.02054v2
- Title: Quantum Key Distribution by Quantum Energy Teleportation
- Authors: Shlomi Dolev, Kazuki Ikeda, Yaron Oz
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2506.02054v2  pdf=https://arxiv.org/pdf/2506.02054v2.pdf

Abstract:
Quantum energy teleportation (QET) is a process that leverages quantum entanglement and local operations to transfer energy between two spatially separated locations without physically transporting particles or energy carriers. We construct a QET-based quantum key distribution (QKD) protocol and analyze its security and robustness to noise in both the classical and the quantum channels. We generalize the construction to an $N$-party information sharing protocol, possessing a feature that dishonest participants can be detected.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2506.02570v3
- Title: Superconducting integrated on-demand quantum memory with microwave pulse preservation
- Authors: Aleksei R. Matanin, Nikita S. Smirnov, Anton I. Ivanov, Victor I. Polozov, Daria A. Moskaleva, Elizaveta I. Malevannaya, Margarita V. Androshuk, Yulia A. Agafonova, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2506.02570v3  pdf=https://arxiv.org/pdf/2506.02570v3.pdf

Abstract:
Microwave quantum memory represents a critical component for quantum radars and resource-efficient approaches to quantum error correction. Superconducting microwave resonators provide highly efficient storage, long coherence times, on-demand reading and even in memory pulse engineering, but it is still challenging to overcome design and materials induced loss channels for on-chip realization. In this work, we present a novel architecture of integrated superconducting quantum memory with a dynamically controlled RF-SQUID coupling element in pulse regime, thus ensuring high efficiency storage and cycling storage time. It demonstrates a memory cycle time of 1.51 $μs$ and 57.5% storage fidelity with preservation of the stored pulse shape during the retrieval at single-photon level excitations. We establish that while the proposed active coupler realization introduces no measurable fidelity degradation, the primary limitation arises from impedance matching and materials imperfections. Still the device was used only for storing finite-duration near-single-photon classical microwave pulses, we assert that it operates as a linear device when the photon population in the common resonator remains low so it should be compatible with quantum state storage.The proposed architecture highlights a disruptive potential for on-chip qubit and memory integration for scalable quantum error correction, while identifying specific avenues for near-unity storage fidelity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2506.17391v2
- Title: A competitive NISQ and qubit-efficient solver for the LABS problem
- Authors: Marco Sciorilli, Giancarlo Camilo, Thiago O. Maciel, Askery Canabarro, Lucas Borges, Leandro Aolita
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.17391v2  pdf=https://arxiv.org/pdf/2506.17391v2.pdf

Abstract:
Pauli Correlation Encoding (PCE) is as a qubit-efficient variational approach to combinatorial optimization problems. The method offers a polynomial reduction in qubit count and a super-polynomial suppression of barren plateaus. Here, we extend the PCE-based framework to solve the Low Autocorrelation Binary Sequences (LABS) problem, a notoriously hard problem often used as a benchmark for classical and quantum solvers. To illustrate this,we simulate two variants of the PCE quantum solver for LABS instances of up to $N=45$ binary variables: one with commuting and one with maximally non-commuting sets of Pauli operators. The simulations use $4$ qubits and a circuit Ansatz with a total of $30$ two-qubit gates. We benchmark our method against the state-of-the-art classical solver and other quantum schemes. We observe improved scaling in the total time to reach the exact solution, outperforming the best-performing classical heuristic while using only a fraction of the quantum resources required by other quantum approaches. In addition, we perform proof-of-principle demonstrations on IonQ's Forte quantum processor, showing that the final solution is resilient to noise. Our findings point at PCE-based solvers as a promising quantum-inspired classical heuristic for hard problems as well as a tool to reduce the resource requirements for actual quantum algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2506.20355v2
- Title: Practical insights on the effect of different encodings, ansätze and measurements in quantum and hybrid convolutional neural networks
- Authors: Jesús Lozano-Cruz, Albert Nieto-Morales, Oriol Balló-Gimbernat, Adan Garriga, Antón Rodríguez-Otero, Alejandro Borrallo-Rentero
- Categories: quant-ph (primary); quant-ph; cs.CV
- Links: abs=https://arxiv.org/abs/2506.20355v2  pdf=https://arxiv.org/pdf/2506.20355v2.pdf

Abstract:
This study investigates the design choices of parameterized quantum circuits (PQCs) within quantum and hybrid convolutional neural network (HQNN and QCNN) architectures, applied to the task of satellite image classification using the EuroSAT dataset. We systematically evaluate the performance implications of data encoding techniques, variational ansätze, and measurement in approx. 500 distinct model configurations. Our analysis reveals a clear hierarchy of influence on model performance. For hybrid architectures, which were benchmarked against their direct classical equivalents (e.g. the same architecture with the PQCs removed), the data encoding strategy is the dominant factor, with validation accuracy varying over 30% for distinct embeddings. In contrast, the selection of variational ansätze and measurement basis had a comparatively marginal effect, with validation accuracy variations remaining below 5%. For purely quantum models, restricted to amplitude encoding, performance was most dependent on the measurement protocol and the data-to-amplitude mapping. The measurement strategy varied the validation accuracy by up to 30% and the encoding mapping by around 8 percentage points.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2507.05554v2
- Title: Theory Framework of Multiplexed Photon-Number-Resolving Detectors
- Authors: Xiaobin Zhao, Hezheng Qin, Hong X. Tang, Linran Fan, Quntao Zhuang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.05554v2  pdf=https://arxiv.org/pdf/2507.05554v2.pdf

Abstract:
Photon counting is a fundamental component in quantum optics and quantum information. However, implementing ideal photon-number-resolving (PNR) detectors remains experimentally challenging. Multiplexed PNR detection offers a scalable and practical alternative by distributing photons across multiple modes and detecting their presence using simple ON-OFF detectors, thereby enabling approximate photon-number resolution. In this work, we establish a theoretical model for such detectors and prove that the estimation error in terms of photon number moments decreases inverse proportionally to the number of detectors. Thanks to the enhanced PNR capability, multiplexed PNR detector provides an advantage in cat-state breeding protocols. Assuming a two-photon subtraction case, $7$dB of squeezing, and an array of 20 detectors of efficiency $95\%$, our calculation predicts fidelity $\sim0.88$ with a success probability $\sim 3.8\%$, representing orders-of-magnitude improvement over previous works. Similar enhancement also extends to cat-state generation with the generalized photon number subtraction. With experimentally feasible parameters, our results suggest that megahertz-rate cat-state generation is achievable using an on-chip array of \emph{tens} of ON-OFF detectors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2507.11766v3
- Title: The Gorini-Kossakowski-Sudarshan-Lindblad problem and the geometry of CP maps
- Authors: Paul E. Lammert
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2507.11766v3  pdf=https://arxiv.org/pdf/2507.11766v3.pdf

Abstract:
The Lindblad equation embodies a fundamental paradigm of the quantum theory of   open systems, and the Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) generation theorem says precisely which superoperators can appear on its right-hand side. These are the generators of completely positive trace-preserving (or nonincreasing) semigroups. We prove a generalization, with time-dependent generator, as an application of an investigation of the geometry of the class of completely positive (CP) maps. The treatment of the finite-dimensional setting is based on a basis-free Choi-Jamiołkowski type isomorphism. The infinite-dimensional case is bootstrapped from the finite-dimensional theory via a sequence of finite-dimensional approximations. Kraus decomposition is established along the way, in the guise of an extremal decomposition of the closed convex cone of CP maps. No appeal is made to results from the representation theory of operator algebras.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2507.16602v2
- Title: Multi-qubit Rydberg gates between distant atoms
- Authors: Antonis Delakouras, Georgios Doultsinos, David Petrosyan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.16602v2  pdf=https://arxiv.org/pdf/2507.16602v2.pdf

Abstract:
We propose an efficient protocol to realize multi-qubit gates in arrays of neutral atoms. The atoms encode qubits in the long-lived hyperfine sublevels of the ground electronic state. To realize the gate, we apply a global laser pulse to transfer the atoms to a Rydberg state with strong blockade interaction that suppresses simultaneous excitation of neighboring atoms arranged in a star-graph configuration. The number of Rydberg excitations, and thereby the parity of the resulting state, depends on the multiqubit input state. Upon changing the sign of the interaction and de-exciting the atoms with an identical laser pulse, the system acquires a geometric phase that depends only on the parity of the excited state, while the dynamical phase is completely canceled. Using single qubit rotations, this transformation can be converted to the C$_k$Z or C$_k$NOT quantum gate for $k+1$ atoms. We also present extensions of the scheme to implement quantum gates between distant atomic qubits connected by a quantum bus consisting of a chain of atoms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2508.05632v2
- Title: Partial projected ensembles and spatiotemporal structure of information scrambling
- Authors: Saptarshi Mandal, Pieter W. Claeys, Sthitadhi Roy
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2508.05632v2  pdf=https://arxiv.org/pdf/2508.05632v2.pdf

Abstract:
Thermalisation and information scrambling in out-of-equilibrium quantum many-body systems are deeply intertwined: local subsystems dynamically approach thermal density matrices while their entropies track information spreading. Projected ensembles--ensembles of pure states conditioned on measurement outcomes of complementary subsystems--provide higher-order probes of thermalisation, converging at late times to universal maximum-entropy ensembles. In this work, we introduce the partial projected ensemble (PPE) as a framework to study how the spatiotemporal structure of scrambling is imprinted on projected ensembles. The PPE consists of an ensemble of mixed states induced on a subsystem by measurements on a spatially separated part of its complement, tracing out the remainder, naturally capturing scenarios involving discarded outcomes or noise-induced losses. We show that statistical fluctuations of the PPE faithfully track the causal lightcone of information spreading, revealing how scrambling dynamics are encoded in ensemble structure. In addition, we demonstrate that the probabilities of bit-string probabilities (PoPs) associated with the PPE exhibit distinct dynamical regimes and provide an experimentally accessible probe of scrambling. Both PPE fluctuations and PoPs display exponential sensitivity to the size of the discarded region, reflecting exponential degradation of quantum correlations under erasure. We substantiate these findings using the non-integrable kicked Ising chain, combining numerics in the ergodic regime with exact results at its self-dual point. We extend our analysis to a many-body localised (MBL) regime numerically, along with analytic results for the $\ell$-bit model. The linear and logarithmic lightcones characteristic of ergodic and MBL regimes emerge naturally from PPE dynamics, establishing it as a powerful tool for probing scrambling and deep thermalisation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2508.13462v3
- Title: Noise-Resilient Spatial Search with Lackadaisical Quantum Walks
- Authors: Gabriel Mauricio Oswald Vieira, Nelson Maculan, Franklin de Lima Marquezino
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.13462v3  pdf=https://arxiv.org/pdf/2508.13462v3.pdf

Abstract:
Quantum walks are a powerful framework for the development of quantum algorithms, with lackadaisical quantum walks (LQWs) standing out as an efficient model for spatial search. In this work, we investigate how broken-link decoherence affects the performance of LQW-based search on a two-dimensional toroidal grid. We show through numerical simulations that, while decoherence drives the loopless walk toward a uniform distribution and eliminates its search capability, the inclusion of self-loops significantly mitigates this effect. In particular, even under noise, the marked vertex remains identifiable with probability well above uniform, demonstrating that self-loops enhance the robustness of LQWs in realistic scenarios. These findings extend the known advantages of LQWs from the noiseless setting to noisy environments, consolidating self-loops as a valuable resource for designing resilient quantum search algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2508.16275v2
- Title: Dissipation-driven topological phase transitions in open quantum systems independent of system Hamiltonian
- Authors: Tian-Shu Deng, Fan Yang
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2508.16275v2  pdf=https://arxiv.org/pdf/2508.16275v2.pdf

Abstract:
We investigate dissipation-driven topological phase transitions in one-dimensional quantum open systems governed by the Lindblad equation with linear dissipation operators, which ensure the density matrix retains its Gaussian form throughout the dynamics. By employing the modular Hamiltonian framework, we rigorously demonstrate that the $\rm{Z}_2$ topological invariant characterizing steady states in one-dimensional class D systems is exclusively dependent on the dissipation operators, rather than the system Hamiltonian. Through a sudden quench protocol where the system evolves from the steady state of one Lindbladian to another, we reveal that topological transitions can occur at analytically predictable critical times, even when the initial and final steady states share identical topological indices. These transitions are shown, both analytically and numerically, to depend solely on dissipation parameters. Entanglement spectrum analysis demonstrates bulk-edge correspondence in non-equilibrium density matrices via coexisting single-particle gap closures (periodic boundaries) and topologically protected zero modes (open boundaries), directly underpinning the detection of dissipation-induced topology in quantum simulators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2508.16482v2
- Title: Decoherent histories with(out) objectivity in a (broken) apparatus
- Authors: Benoît Ferté, Davide Farci, Xiangyu Cao
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2508.16482v2  pdf=https://arxiv.org/pdf/2508.16482v2.pdf

Abstract:
We characterize monitored quantum dynamics in a solvable model exhibiting a phase transition between a measurement apparatus and a scrambler. We show that approximate decoherent histories emerge in both phases with respect to a coarse-grained extensive observable. However, the apparatus phase, where quantum Darwinism emerges, is distinguished by the non-ergodicity of the histories and their correlation with the measured qubit, which selects an ensemble of preferred pointer states. Our results demonstrate a clear distinction between two notion of classicality, decoherent histories and environment-induced decoherence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2509.11074v2
- Title: Spectrum measurement of quantum channels and application to Hamiltonian parameter estimation
- Authors: Yuan-De Jin, Wen-Long Ma
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.11074v2  pdf=https://arxiv.org/pdf/2509.11074v2.pdf

Abstract:
Quantum channels describe the most general dynamics of open quantum systems. A quantum channel, as a linear map on vectorized quantum states, can be represented by a single matrix, whose spectrum is called the channel spectrum. Here we propose a general method to measure the channel spectrum and apply this method to Hamiltonian parameter estimation. We first demonstrate that the channel spectrum can be measured by tracking the probability of a specific outcome in repeated application of the same channel. Then we construct and analyze {a class of concatenated channels, with each one being a unitary channel followed by a weak-measurement channel induced by a Ramsey sequence of a probe qubit}. We show that the spectrum measurement of such concatenated channels can be utilized for estimating the parameters in the free Hamiltonians generating the unitary channels of the target system. As practical examples, we numerically demonstrate that a probe spin qubit can accurately sense nuclear spin clusters for nanoscale nuclear magnetic resonance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2509.13528v2
- Title: Evaluating the Limits of QAOA Parameter Transfer at High-Rounds on Sparse Ising Models With Geometrically Local Cubic Terms
- Authors: Elijah Pelofske, Marek Rams, Andreas Bärtschi, Piotr Czarnik, Paolo Braccia, Lukasz Cincio, Stephan Eidenbenz
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2509.13528v2  pdf=https://arxiv.org/pdf/2509.13528v2.pdf

Abstract:
The emergent practical applicability of the Quantum Approximate Optimization Algorithm (QAOA) for approximate combinatorial optimization is a subject of considerable interest. One of the primary limitations of QAOA is the task of finding a set of good parameters. Parameter transfer is a phenomenon where QAOA angles trained on problem instances that are self-similar tend to perform well for other problem instances from that similar class. This suggests a potentially highly efficient and scalable non-variational learning method for QAOA angle finding. We systematically study QAOA parameter transferability from small problems (16, 27 qubits) onto large problem instances (up to 156 qubits) for heavy-hex graph Ising models with geometrically local higher order terms using the Julia based QAOA simulation tool JuliQAOA to perform classical angle finding for up to 49 QAOA layers. Parameter transfer of the fixed angles is validated using a combination of full statevector, Projected Entangled Pair States, Matrix Product State, and LOWESA numerical simulations. We find that the QAOA parameter transfer from single instances applied to unseen problem instances does not in general provide monotonically improving performance as a function of p - there are many cases where the performance temporarily decreases as a function of p - but despite this the transferred angles have a general trend of improved expectation value as the QAOA depth increases, in many cases converging close to the true ground-state energy of the 100+ qubit instances. We also sample the hardware-compatible Ising models using the ensemble of fixed QAOA angles on several superconducting qubit IBM Quantum processors with 127, 133, and 156 qubits. We find continuous solution quality improvement of the hardware-compatible QAOA circuits run on the IBM NISQ processors up to p=5 on ibm_fez, p=9 on ibm_torino, and p=10 on ibm_pittsburgh.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2509.20052v2
- Title: Nontrivial multi-product commutation relation toward reducing T-count in sequential Pauli-based computation
- Authors: Yusei Mori, Hideaki Hakoshima, Keisuke Fujii
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.20052v2  pdf=https://arxiv.org/pdf/2509.20052v2.pdf

Abstract:
Quantum compilers that reduce the number of T gates are essential for minimizing the overhead of fault-tolerant quantum computation. Achieving further T-count reduction calls for identifying equivalent circuit transformation rules beyond those utilized in existing tools. In this paper, we rewrite any given Clifford+T circuit using a Clifford block followed by a sequential Pauli-based computation, and introduce a nontrivial, ancilla-free transformation rule, the multi-product commutation relation (MCR). MCR constructs gate sequences based on specific commutation properties among multi-Pauli operators, yielding seemingly non-commutative instances that can be commuted, thereby enabling gate orderings that cannot be derived from pairwise commutation alone. To evaluate whether existing compilers account for this commutation rule, we create a benchmark circuit dataset using quantum circuit unoptimization. This approach intentionally adds redundancy to the circuit while keeping its equivalence, allowing a quantitative evaluation of compiler performance by comparison with the original circuit. Our numerical experiments reveal that the transformation rule based on MCR is not yet incorporated into current compilers, despite their demonstrated effectiveness for T-count reduction. These findings suggest an untapped potential for further T-count reduction by integrating MCR-aware transformations, paving the way for improvements in quantum compilers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.05479v2
- Title: Cored product codes for quantum self-correction in three dimensions
- Authors: Brenden Roberts, Jin Ming Koh, Yi Tan, Norman Y. Yao
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2510.05479v2  pdf=https://arxiv.org/pdf/2510.05479v2.pdf

Abstract:
The existence of self-correcting quantum memories in three dimensions is a long-standing open question at the interface between quantum computing and many-body physics. We take the perspective that large contributions to the entropy arising from fine-tuned spatial symmetries, including the assumption of an underlying regular lattice, are responsible for fundamental challenges to realizing self-correction. Accordingly, we introduce a class of disordered quantum codes, which we call "cored product codes". These codes are derived from classical factors via the hypergraph product but undergo a coring procedure which allows them to be embedded in a lower number of spatial dimensions while preserving code properties. As a specific example, we focus on a fractal code based on the aperiodic pinwheel tiling as the classical factor and perform finite temperature numerical simulations on the resulting three-dimensional quantum memory. We provide evidence that, below a critical temperature, the memory lifetime increases with system size for codes up to 60000 qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.05795v4
- Title: Efficient Post-Selection for General Quantum LDPC Codes
- Authors: Seok-Hyung Lee, Lucas H. English, Stephen D. Bartlett
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.05795v4  pdf=https://arxiv.org/pdf/2510.05795v4.pdf

Abstract:
Post-selection strategies that discard low-confidence computational results can significantly improve the effective fidelity of quantum error correction at the cost of reduced acceptance rates, which can be particularly useful for offline resource state generation and other moderate-depth fault-tolerant circuits. Prior work has primarily relied on the "logical gap" metric with the minimum-weight perfect matching decoder, but this approach faces fundamental limitations including computational overhead that scales exponentially with the number of logical qubits and poor generalizability to arbitrary codes beyond surface codes. We develop post-selection strategies based on computationally efficient heuristic confidence metrics that leverage error cluster statistics (specifically, aggregated cluster sizes and log-likelihood ratios) from clustering-based decoders, which are applicable to arbitrary quantum low-density parity check (QLDPC) codes. We validate our method through extensive numerical simulations on surface codes, bivariate bicycle codes, and hypergraph product codes, demonstrating orders of magnitude reductions in logical error rates with moderate abort rates. For instance, applying our strategy to the [[144, 12, 12]] bivariate bicycle code achieves approximately three orders of magnitude reduction in the logical error rate with an abort rate of only 1% (19%) at a physical error rate of 0.1% (0.3%). Additionally, we integrate our approach with the sliding-window framework for real-time decoding, featuring early mid-circuit abort decisions that eliminate unnecessary overheads. Notably, its performance matches or even surpasses the original strategy for global decoding, while exhibiting favorable scaling in the number of rounds. Our approach provides a practical foundation for efficient post-selection in fault-tolerant quantum computing with QLDPC codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.07547v2
- Title: Constructive counterexamples to the additivity of minimum output Rényi entropy of quantum channels for all $p>1$
- Authors: Harm Derksen, Benjamin Lovitz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.07547v2  pdf=https://arxiv.org/pdf/2510.07547v2.pdf

Abstract:
We present explicit quantum channels with strictly sub-additive minimum output Rényi entropy for all $p>1$, improving upon prior constructions which handled $p>2$. Our example is provided by explicit constructions of linear subspaces with high geometric measure of entanglement. This construction applies in both the bipartite and multipartite settings. As further applications, we use our construction to find entanglement witnesses with many highly negative eigenvalues, and to construct entangled mixed states that remain entangled after perturbation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.07561v2
- Title: Correlation Lengths for Stochastic Matrix Product States
- Authors: Lubashan Pathirana, Albert H. Werner
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2510.07561v2  pdf=https://arxiv.org/pdf/2510.07561v2.pdf

Abstract:
We introduce a general model of stochastically generated matrix product states (MPS) in which the local tensors share a common distribution and form a strictly stationary sequence, without requiring spatial independence. Under natural conditions on the associated transfer operators, we prove the existence of thermodynamic limits of expectations of local observables and establish almost-sure exponential decay of two-point correlations. In the homogeneous (random translation-invariant) case, for any error tolerance in probability, the two-point function decays exponentially in the distance between the two sites, with a deterministic rate. In the i.i.d. case, the exponential decay still holds with a deterministic rate, with the probability approaching one exponentially fast in the distance. For strictly stationary ensembles with decaying spatial dependence, the correlation decay quantitatively reflects the mixing profile: ($ρ$)-mixing yields polynomial bounds with high probability, while stretched-exponential (resp. exponential) decay in ($ρ$) (resp. ($β$)) yields stretched-exponential (resp. exponential) decay of the two-point function, again with correspondingly strong high-probability guarantees. Altogether, the framework unifies and extends recent progress on stationary ergodic and Gaussian translation-invariant ensembles, providing a transfer-operator route to typical correlation decay in random MPS.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.18186v3
- Title: Burau representation, Squier's form, and non-Abelian anyons
- Authors: Alexander Kolpakov
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2510.18186v3  pdf=https://arxiv.org/pdf/2510.18186v3.pdf

Abstract:
We introduce a frequency-tunable, two-dimensional non-Abelian control of operation order constructed from the reduced Burau representation of the braid group $B_3$, specialised at $t=e^{iω}$ and unitarized by Squier's Hermitian form. Coupled to two non-commuting qubit unitaries $A$, $B$, the resulting switch admits a closed expression for the single-shot Helstrom success probability and a fixed-order ceiling $p_{\mathrm{fixed}}$, defining the fixed-order ceiling $p_{\mathrm{fixed}}^*$ and the witness gaps $Δ_{\rm sw}(ω)=p_{\mathrm{switch}}(ω)-p_{\mathrm{fixed}}^*$ and $Δ_{\rm test}(ω)=p_{\mathrm{test}}(ω)-p_{\mathrm{fixed}}^*$.   The non-Abelian mixers can either enhance or suppress the bare switch advantage, which we quantify by the interference contrast $Δ_{\rm int}(ω):=Δ_{\rm test}(ω)-Δ_{\rm sw}(ω)=p_{\rm test}(ω)-p_{\rm switch}(ω)$. Across the Squier positivity region, $Δ_{\rm int}(ω)$ takes both positive (constructive) and negative (destructive) values, a hallmark of matrix-valued (non-Abelian) order control, while $Δ_{\rm sw}(ω)>0$ certifies algebraic causal non-separability.   Numerical simulations confirm both enhancement and suppression regimes, establishing a minimal $B_3$ braid control that reproduces the characteristic interference pattern expected from a \emph{Gedankenexperiment} in anyonic statistics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.19073v2
- Title: Practical Noise Mitigation for Quantum Annealing via Dynamical Decoupling: Toward Industry-Relevant Optimization using Trapped Ions
- Authors: Sebastian Nagies, Chiara Capecci, Marcel Seelbach Benkner, Javed Akram, Sebastian Rubbert, Dimitrios Bantounas, Michael Moeller, Michael Johanning, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.19073v2  pdf=https://arxiv.org/pdf/2510.19073v2.pdf

Abstract:
Quantum annealing is a framework for solving combinatorial optimization problems. While it offers a promising path towards a practical application of quantum hardware, its performance in real-world devices is severely limited by environmental noise that can degrade solution quality. We investigate the suppression of local field noise in quantum annealing protocols through the periodic application of dynamical decoupling pulses implementing global spin flips. As test problems, we construct minimal Multiple Object Tracking QUBO instances requiring only five and nine qubits, as well as cutting stock instances of five and six qubits. Moreover, using the Sherrington--Kirkpatrick model, we demonstrate the robustness of our protocol to problem structure and size. To further place our results in a practical context, we consider a trapped-ion platform based on magnetic gradient-induced coupling as a reference architecture, using it to define experimentally realistic noise and coupling parameters. We show that external magnetic field fluctuations, typical in such setups, significantly degrade annealing fidelity, while moderate dynamical decoupling pulse rates, which are achievable in current experiments, restore performance to near-ideal levels. Our analytical and numerical results reveal a universal scaling behavior, with fidelity determined by a generalized parameter combining noise amplitude and dynamical decoupling pulse interval. While our analysis is grounded in the trapped-ion platform, the proposed noise mitigation strategy and resulting performance improvements are applicable to a broad range of quantum annealing implementations and establish a practical and scalable route for error mitigation in near-term devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.23815v2
- Title: Differential magnetometry with partially flipped Dicke states
- Authors: Iagoba Apellaniz, Manuel Gessner, Géza Tóth
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.23815v2  pdf=https://arxiv.org/pdf/2510.23815v2.pdf

Abstract:
We study magnetometry of gradients and homogeneous background fields along the three orthogonal directions using two spatially separated spin ensembles. We derive trade-off relations for the achievable estimation precision of these parameters. Dicke states, optimal for homogeneous field estimation, can be locally rotated into states sensitive to magnetic gradients by rotating the spins in one subensemble. We determine bounds for the precision for gradient metrology in the three orthogonal directions as a function of the sensitivities to the homogenous field in those directions. The resulting partially flipped Dicke state saturates the bounds above, showing similar sensitivity in two directions but significantly reduced sensitivity in the third. Exploiting entanglement between the two ensembles, this state achieves roughly twice the precision attainable by the best bipartite separable state, which is a product of local Dicke states. For small ensembles, we explicitly identify measurement operators saturating the quantum Cramér-Rao bound, while for larger ensembles, we propose simpler but suboptimal schemes. In both cases, the gradient is estimated from second moments and correlations of angular momentum operators. Our results demonstrate how the metrological properties of Dicke states can be exploited for quantum-enhanced multiparameter estimation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2511.00857v2
- Title: Optimizing magnetic coupling in lumped element superconducting resonators for molecular spin qubits
- Authors: Marcos Rubín-Osanz, David Rodriguez, Ignacio Gimeno, Wenzel Kersten, Nerea González-Prato, María C. Pallarés, Sebastián Roca-Jerat, Marina C. de Ory, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2511.00857v2  pdf=https://arxiv.org/pdf/2511.00857v2.pdf

Abstract:
We engineer lumped-element superconducting resonators that maximize magnetic coupling to molecular spin qubits, achieving record single-spin couplings up to $100$ kHz and collective couplings exceeding $10$ MHz. The resonators interact with PTMr organic free radicals, model spin systems with $S=1/2$ and a quasi-isotropic $g \simeq 2$, dispersed in polymer matrices. The highest collective spin-photon coupling strengths are attained with resonators having large inductors, which therefore interact with most spins in the molecular ensemble. By contrast, the coupling of each individual spin $G_{1}$ is maximized in resonators having a minimum size inductor, made of a single wire. The same platform has been used to study spin relaxation and spin coherent dynamics in the dispersive regime, when spins are energetically detuned from the resonator. We find evidences for the Purcell effect, i.e. the photon induced relaxation of those spins that are most strongly coupled to the circuit. The rate of this process gives access to the distribution of single spin photon couplings in a given device. For resonators with a $50$ nm wide constriction at the inductor center, single maximum $G_{1}$ values reach $\sim 100$ kHz. Pumping the spins with strong pulses fed through an independent transmission line induces coherent Rabi oscillations. The spin excitation then proceeds via either direct resonant processes induced by the main pulse frequency or, in the case of square-shaped pulses, via the excitation of the cavity by sideband frequency components. The latter process measures the cavity mode hybridization with the spins and can be eliminated by using Gaussian shaped pulses. These results establish a scalable route toward integrated molecular-spin quantum processors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2511.14802v2
- Title: Hybrid Quantum-Classical Dispatching for High-Renewable Power Systems:A Noise-Resilient Variational Approach with Real-World Validation
- Authors: Fu Zhang, Yuming Zhao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.14802v2  pdf=https://arxiv.org/pdf/2511.14802v2.pdf

Abstract:
This study introduces a hybrid quantum-classical dispatching framework designed for power systems with high renewable penetration. The proposed method integrates a variational quantum algorithm with classical optimization to provide noise-resilient performance under realistic hardware constraints. Extensive numerical tests and a real-world case study demonstrate significant improvements in cost reduction, dispatch reliability, and robustness to device noise. The approach highlights the potential of near-term quantum computing to address critical challenges in renewable energy integration. The results bridge the gap between quantum algorithms and practical energy system operations, offering a pathway for sustainable and efficient power system management.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2511.17047v2
- Title: Chiral cavity-magnonic system for the unidirectional photon blockade
- Authors: Jiaxin Yang, Yilou Liu, Rui-Shan Zhao, Xiao-Tao Xie
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.17047v2  pdf=https://arxiv.org/pdf/2511.17047v2.pdf

Abstract:
We propose an scheme for directional single-photon source based on a chiral cavity-magnon system. In this system, the magnon mode in a single-crystal yttrium iron garnet (YIG) sphere is coupled to only one of two rotating microwave modes in the torus-shaped microwave cavity. When two-photon drives are applied to both ports of the waveguide, the chiral cavity-magnon coupling leads to an unconventional photon blockade in one propagation direction, resulting in directional single-photon emission. The emission direction of the single-photon source can be controlled by reversing the biased magnetic field. Furthermore, we further examine the effects of imperfect chiral cavity-magnon coupling and the coupling between the two cavity modes on the photon blockade behavior. The results show that the system retains robustness in the presence of these nonideal factors, and the unidirectional photon blockade effect remains clearly preserved.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2511.20031v2
- Title: A Comprehensive Characterization of the Vacuum Beam Guide and Its Applications
- Authors: Yuexun Huang, Delaney Smith, Pei Zeng, Debayan Bandyopadhyay, Junyu Liu, Rana X Adhikari, Liang Jiang
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2511.20031v2  pdf=https://arxiv.org/pdf/2511.20031v2.pdf

Abstract:
The proposed vacuum beam guide (VBG) represents a transformative advance in quantum channel technology, guaranteeing an ultra-low level of attenuation and a broad transmission linewidth, which offers an unprecedented quantum capacity, exceeding Tera-qubits per second on a continental scale. However, the stability of the VBG in terms of interferometry remains unexamined. To address this gap, we have developed a comprehensive noise budget for sources of phase noise in the VBG, highlighting its capabilities for precision interferometry. This model facilitates a comprehensive characterization of the VBG as a photonic quantum channel, thereby allowing a detailed investigation of its potential. Our theoretical analysis finds no technical or fundamental blockers for a VBG and predicts its expected performance in a wide range of quantum applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2511.21660v2
- Title: FPGA-tailored algorithms for real-time decoding of quantum LDPC codes
- Authors: Satvik Maurya, Thilo Maurer, Markus Bühler, Drew Vandeth, Michael E. Beverland
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.21660v2  pdf=https://arxiv.org/pdf/2511.21660v2.pdf

Abstract:
Real-time decoding is crucial for fault-tolerant quantum computing but likely requires specialized hardware such as field-programmable gate arrays (FPGAs), whose parallelism can alter relative algorithmic performance. We analyze FPGA-tailored versions of three decoder classes for quantum low-density parity-check (qLDPC) codes: message passing, ordered statistics, and clustering. For message passing, we analyze the recently introduced Relay decoder and its FPGA implementation; for ordered statistics decoding (OSD), we introduce a filtered variant that concentrates computation on high-likelihood fault locations; and for clustering, we design an FPGA-adapted generalized union-find decoder. We design a systolic algorithm for Gaussian elimination on rank-deficient systems that runs in linear parallel time, enabling fast validity checks and local corrections in clustering and eliminating costly full-rank inversion in filtered-OSD. Despite these improvements, both remain far slower and less accurate than Relay, suggesting message passing is the most viable route to real-time qLDPC decoding.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.11407v2
- Title: Quantum limits of a space-time reference frame
- Authors: Davide Mattei, Esteban Castro-Ruiz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.11407v2  pdf=https://arxiv.org/pdf/2512.11407v2.pdf

Abstract:
We study the limitations for defining spatial and temporal intervals when the only available reference frame is a single composite quantum system, whose internal degrees of freedom serve as a temporal reference, a clock, and whose center of mass degrees of freedom act as a spatial reference, a rod. By combining quantum speed limits with the mass energy equivalence of special relativity, we show that spatial localizability and temporal resolution are not independent: sharpening one inevitably blurs the other. Specifically, the internal energy coherence needed for precise timekeeping affects the center of mass dynamics, enhancing position spreading during free evolution. As a result, a single composite system cannot act as a perfect quantum reference frame for both space and time, leading to a Heisenberg like uncertainty relation between spatial and temporal intervals. After analyzing this trade off from an external perspective, we formulate it in a purely relational manner, by means of covariant observables relative to the space time quantum reference frame, uncovering an additional intrinsic uncertainty of order the Compton wavelength of the frame.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.11418v2
- Title: Stabilizer-based quantum simulation of fermion dynamics with local qubit encodings
- Authors: Anthony Gandon, Samuele Piccinelli, Max Rossmannek, Francesco Tacchino, Alberto Baiardi, Jannes Nys, Ivano Tavernelli
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.11418v2  pdf=https://arxiv.org/pdf/2512.11418v2.pdf

Abstract:
Simulating the dynamical properties of large-scale many-fermion systems is a longstanding goal of quantum chemistry, material science and condensed matter. Local fermion-to-qubit encodings have opened a new path for practical fermionic simulations on digital quantum hardware where fermionic statistics are not enforced at the hardware level. In this paper, we explore these local encodings from the perspective of the corresponding time-evolution unitaries. Specifically, we propose a new framework for digital implementations of these qubit-encoded fermionic time-evolution unitaries based on \emph{flow sets}, which are one-dimensional subsets of the directed fermionic interaction graph. We find that any local fermionic encoding, when restricted to a given flow set, adopts a simple structure that we can classify systematically. For each categorized flow-set form, we propose a low-depth qubit quantum circuit that implements the time evolution unitary using the stabilizer formalism. As an application of our construction, we introduce novel flow-based decompositions for known two-dimensional encodings, leading to efficient circuit decompositions of time-evolution unitaries. We generally observe a space-time trade-off, where mappings with larger qubit-to-fermion ratios yield shallower time-evolution quantum circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.11436v2
- Title: Nonreciprocal flow of fluctuations, populations and correlations between doubly coupled bosonic modes
- Authors: Zbigniew Ficek
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.11436v2  pdf=https://arxiv.org/pdf/2512.11436v2.pdf

Abstract:
Interesting new correlation and unidirectional properties of two bosonic modes under the influence of environment appear when the modes are mutually coupled through the simultaneously applied linear mode-hopping and nonlinear squeezing interactions. Under such double coupling, it is found that while the Hamiltonian of the system is clearly Hermitian the dynamics of the quadrature components of the field operators can be attributed to non-Hermicity of the system. It is manifested in an asymmetric coupling between the quadrature components which then leads to a variety of remarkable features. In particular, we identify how the emerging exceptional point controls the conversion of thermal states of the modes into single-mode classically or quantum squeezed states. Furthermore, for reservoirs being in squeezed states, we find that the two-photon correlations present in these reservoirs are responsible for unidirectional flow of populations and correlations among the modes and the flow can be controlled by appropriate tuning of the mutual orientation of the squeezed noise ellipses. In the course of analyzing these effects we find that the flow of the population creates the first-order coherence between the modes which, on the other hand rules out an enhancement of the two photon correlations responsible for entanglement between the modes. These results suggest new alternatives for the creation of single mode squeezed fields and the potential applications for controlled unidirectional transfer of population and correlations in bosonic chains.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.12704v2
- Title: Entanglement, Coherence, and Recursive Linking in Dicke states : A Topological Perspective
- Authors: Sougata Bhattacharyya, Sovik Roy
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.12704v2  pdf=https://arxiv.org/pdf/2512.12704v2.pdf

Abstract:
This work investigates the topological structure of multipartite entanglement in symmetric Dicke states $|D_n^{(k)}\rangle$. By viewing qubits as topological loops, we establish a direct correspondence between the recursive measurement dynamics of Dicke states and the stability of $n$-Hopf links. We utilize the Schmidt rank to quantify bipartite entanglement resilience and introduce the $l_1$-norm of quantum coherence as a measure of link fluidity. We demonstrate that unlike fragile states such as $ \left| GHZ \right \rangle$ (analogous to Borromean rings), Dicke states exhibit a robust, self-similar topology where local measurements preserve the global linking structure through non-vanishing residual coherence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.16232v2
- Title: Amplifying Decoherence-Free Many-Body Interactions with Giant Atoms Coupled to Parametric Waveguide
- Authors: Xin Wang, Zhao-Min Gao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.16232v2  pdf=https://arxiv.org/pdf/2512.16232v2.pdf

Abstract:
Parametric amplification offers a powerful means to enhance quantum interactions through field squeezing, yet it typically introduces additional noise which accelerates quantum decoherence, a major obstacle for scalable quantum information processing. The squeezing field is implemented in cavities rather than continuous waveguides, thereby limiting its scalability for applications in quantum simulation. Giant atoms, which couple to waveguides at multiple points, provide a promising route to mitigate dissipation via engineered interference, enabling decoherence-free interactions. We extend the squeezing-amplified interaction to a novel quantum platform combining giant atoms with traveling-wave parametric waveguides based on $χ^{(2)}$ nonlinearity. By exploiting destructive interference between different coupling points, the interaction between giant atoms is not only significantly enhanced but also becomes immune to squeezed noise. Unlike conventional waveguide quantum electrodynamics without a squeezing pump, the giant emitters exhibit both exchange and pairing interactions, making this platform particularly suitable for simulating many-body quantum physics. More intriguingly, the strengths of these interactions can be smoothly tuned by adjusting the squeezing and coupling parameters. Our architecture thus provides a versatile and scalable platform for quantum simulation of strongly correlated physics and paves the way toward robust quantum control in many-body regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.24304v2
- Title: In defense of temporal Tsirelson bound
- Authors: Antoni Wójcik, Jan Wójcik
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.24304v2  pdf=https://arxiv.org/pdf/2512.24304v2.pdf

Abstract:
In a recent paper, Chatterjee et al. [Phys. Rev. Lett 135, 220202 (2025)] analyze and experimentally implement a specific unitary evolution of a simple quantum system. The authors refer to this type of dynamics as a "superposition of unitary time evolutions." They claim that such an evolution enables a violation of the temporal Tsirelson bound in the Leggett-Garg scenario, a claim that is supported by their experimental results. In this work, we show that the proposed evolution can be understood within a more conventional framework, without invoking a superposition of evolutions. Furthermore, we demonstrate that the apparent violation of the bound arises because the measured quantities are not consistent with the assumptions of the Leggett-Garg scenario.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.02413v2
- Title: Minimal length: A source of quantum non-locality
- Authors: H. Moradpour, S. Jalalzadeh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.02413v2  pdf=https://arxiv.org/pdf/2601.02413v2.pdf

Abstract:
The narrow and subtle difference between the Hilbert spaces of operators corresponding to the purely quantum mechanical momentum and the generalized momentum that includes minimal length effects is polished. Additionally, the existence of complex numbers in quantum mechanics may be justifiable as a consequence of minimal length. A novel quantum entanglement generation is also reported, indicating the power of theories including a minimal length in enriching the current understanding of quantum non-locality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.03253v2
- Title: Grand-Canonical Typicality
- Authors: Cedric Igelspacher, Roderich Tumulka, Cornelia Vogel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.03253v2  pdf=https://arxiv.org/pdf/2601.03253v2.pdf

Abstract:
We study how the grand-canonical density matrix arises in macroscopic quantum systems. ``Canonical typicality'' is the known statement that for a typical wave function $Ψ$ from a micro-canonical energy shell of a quantum system $S$ weakly coupled to a large but finite quantum system $B$, the reduced density matrix $\hatρ^S_Ψ=\mathrm{tr}^B |Ψ\rangle\langle Ψ|$ is approximately equal to the canonical density matrix $\hatρ_\mathrm{can}=Z^{-1}_\mathrm{can} \exp(-β\hat{H}^S)$. Here, we discuss the analogous statement and related questions for the \emph{grand-canonical} density matrix $\hatρ_\mathrm{gc}=Z^{-1}_\mathrm{gc} \exp(-β(\hat{H}^S-μ_1 \hat{N}_{1}^S-\ldots-μ_r\hat{N}_{r}^S))$ with $\hat{N}_{i}^S$ the number operator for molecules of type $i$ in the system $S$. This includes (i) the case of chemical reactions and (ii) that of systems $S$ defined by a spatial region which particles may enter or leave. It includes the statements (a) that the density matrix of the appropriate (generalized micro-canonical) Hilbert subspace $H_\mathrm{gmc} \subset H^S \otimes H^B$ (defined by a micro-canonical interval of total energy and suitable particle number sectors), after tracing out $B$, yields $\hatρ_\mathrm{gc}$; (b) that typical $Ψ$ from $H_\mathrm{gmc}$ have reduced density matrix $\hatρ^S_Ψ$ close to $\hatρ_\mathrm{gc}$; and (c) that the conditional wave function $ψ^S$ of $S$ has probability distribution $\mathrm{GAP}_{\hatρ_\mathrm{gc}}$ if a typical orthonormal basis of $H^B$ is used. That is, we discuss the foundation and justification of both the density matrix and the distribution of the wave function in the grand-canonical case. We also extend these considerations to the so-called generalized Gibbs ensembles, which apply to systems for which some macroscopic observables are conserved.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2601.04827v2
- Title: PACOX: A FPGA-based Pauli Composer Accelerator for Pauli String Computation
- Authors: Tran Xuan Hieu Le, Tuan Hai Vu, Vu Trung Duong Le, Hoai Luan Pham, Yasuhiko Nakashima
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.04827v2  pdf=https://arxiv.org/pdf/2601.04827v2.pdf

Abstract:
Pauli strings are a fundamental computational primitive in hybrid quantum-classical algorithms. However, classical computation of Pauli strings suffers from exponential complexity and quickly becomes a performance bottleneck as the number of qubits increases. To address this challenge, this paper proposes the Pauli Composer Accelerator (PACOX), the first dedicated FPGA-based accelerator for Pauli string computation. PACOX employs a compact binary encoding with XOR-based index permutation and phase accumulation. Based on this formulation, we design a parallel and pipelined processing element (PE) cluster architecture that efficiently exploits data-level parallelism on FPGA. Experimental results on a Xilinx ZCU102 FPGA show that PACOX operates at 250 MHz with a dynamic power consumption of 0.33 W, using 8,052 LUTs, 10,934 FFs, and 324 BRAMs. For Pauli strings of up to 19 qubits, PACOX consistently outperforms state-of-the-art CPU-based methods in terms of execution speed, while also requiring significantly less memory and achieving a much lower power-delay product. These results demonstrate that PACOX delivers high computational speed with superior energy efficiency for Pauli-based workloads in hybrid quantum-classical systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2402.11259v2
- Title: Electronic analogue of Fourier optics with mass-less Dirac fermions scattered by quantum dot lattice
- Authors: Partha Sarathi Banerjee, Rahul Marathe, Sankalpa Ghosh
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2402.11259v2  pdf=https://arxiv.org/pdf/2402.11259v2.pdf

Abstract:
The field of electron optics exploits the analogy between the movement of electrons or charged quasiparticles, primarily in two-dimensional materials subjected to electric and magnetic (EM) fields and the propagation of electromagnetic waves in a dielectric medium with varied refractive index. We significantly extend this analogy by introducing an electronic analogue of Fourier optics dubbed as Fourier electron optics (FEO) with massless Dirac fermions (MDF), namely the charge carriers of single-layer graphene under ambient conditions, by considering their scattering from a two-dimensional quantum dot lattice (TDQDL) treated within Lippmann-Schwinger formalism. By considering the scattering of MDF from TDQDL with a defect region, as well as the moiré pattern of twisted TDQDLs, we establish an electronic analogue of Babinet's principle in optics. Exploiting the similarity of the resulting differential scattering cross-section with the Fraunhofer diffraction pattern, we construct a dictionary for such FEO. Subsequently, we evaluate the resistivity of such scattered MDF using the Boltzmann approach as a function of the angle made between the direction of propagation of these charge-carriers and the symmetry axis of the dot-lattice, and Fourier analyze them to show that the spatial frequency associated with the angle-resolved resistivity gets filtered according to the structural changes in the dot lattice, indicating wider applicability of FEO of MDF.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2405.20379v2
- Title: Fate of many-body localization in an Abelian lattice gauge theory
- Authors: Indrajit Sau, Debasish Banerjee, Arnab Sen
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; cond-mat.str-el; hep-lat; quant-ph
- Links: abs=https://arxiv.org/abs/2405.20379v2  pdf=https://arxiv.org/pdf/2405.20379v2.pdf

Abstract:
We address the fate of many-body localization (MBL) of mid-spectrum eigenstates of a matter-free $U(1)$ quantum-link gauge theory Hamiltonian with random couplings on ladder geometries. Apart from level spacing distribution indicators like disorder-averaged mean level spacing, we also consider an intensive estimator $\mathcal{D} \in [0,1/4]$, which acts as a measure of elementary plaquettes on the lattice that are active or inert in mid-spectrum eigenstates as well as the concentration of these eigenstates in Fock space, with $\mathcal{D}$ equal to its maximum value of $1/4$ for Fock states in the electric flux basis. We calculate its distribution, $p(\mathcal{D})$, for $L_x \times L_y$ lattices, with $L_y=2$ and $4$, as a function of (a dimensionless) disorder strength $α$ ($α=0$ implies zero disorder) using exact diagonalization in many disorder realizations. Although finite-size estimators based on level spacings do not give a reliable critical disorder strength, $α_c(L_y)$, beyond which MBL prevails as $L_x \rightarrow \infty$; a different estimator based on the skewness of $p(\mathcal{D})$ gives $α_c(L_y=2)=31.04 \pm 0.54$ using data for $L_x \leq 14$ due to faster convergence. $p(\mathcal{D})$ for wider ladders with $L_y=4$ show a lower tendency to localize, suggesting a lack of MBL in two dimensions. A remarkable observation is the resolution of the (monotonic) infinite-temperature autocorrelation function of single plaquette diagonal operators in typical high-energy Fock states into a plethora of emergent timescales of increasing spatio-temporal heterogeneity as the disorder is increased. At intermediate $α$ as well as for $α$ slightly below $α_c (L_y)$, a fraction of randomly selected initial Fock states display striking oscillatory temporal behavior of such plaquette operators in spatial regions formed out of connected plaquettes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2501.03314v4
- Title: Soft symmetries of topological orders
- Authors: Ryohei Kobayashi, Maissam Barkeshli
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; math.QA; quant-ph
- Links: abs=https://arxiv.org/abs/2501.03314v4  pdf=https://arxiv.org/pdf/2501.03314v4.pdf

Abstract:
(2+1)D topological orders possess emergent symmetries given by a group $\text{Aut}(\mathcal{C})$, which consists of the braided tensor autoequivalences of the modular tensor category $\mathcal{C}$ that describes the anyons. In this paper we discuss cases where $\text{Aut}(\mathcal{C})$ has elements that neither permute anyons nor are associated to any symmetry fractionalization but are still non-trivial, which we refer to as soft symmetries. We point out that one can construct topological defects corresponding to such exotic symmetry actions by decorating with a certain class of gauged SPT states that cannot be distinguished by their torus partition function. This gives a physical interpretation to work by Davydov on soft braided tensor autoequivalences. This has a number of important implications for the classification of gapped boundaries, non-invertible spontaneous symmetry breaking, and the general classification of symmetry-enriched topological phases of matter. We also demonstrate analogous phenomena in higher dimensions, such as (3+1)D gauge theory with gauge group given by the quaternion group $Q_8$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2503.08039v2
- Title: A quantum Monte Carlo algorithm for arbitrary high-spin Hamiltonians
- Authors: Arman Babakhani, Lev Barash, Itay Hen
- Categories: physics.comp-ph (primary); physics.comp-ph; cond-mat.other; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2503.08039v2  pdf=https://arxiv.org/pdf/2503.08039v2.pdf

Abstract:
We present a universal quantum Monte Carlo algorithm for simulating arbitrary high-spin (spin greater than 1/2) Hamiltonians, based on the recently developed permutation matrix representation (PMR) framework. Our approach extends a previously developed PMR-QMC method for spin-1/2 Hamiltonians [Phys. Rev. Research 6, 013281 (2024)]. Because it does not rely on a local bond decomposition, the method applies equally well to models with arbitrary connectivities, long-range and multi-spin interactions, and its closed-walk formulation allows a natural analysis of sign-problem conditions in terms of cycle weights. To demonstrate its applicability and versatility, we apply our method to spin-1 and spin-3/2 quantum Heisenberg models on the square lattice, as well as to randomly generated high-spin Hamiltonians. Additionally, we show how the approach naturally extends to general Hamiltonians involving mixtures of particle species, including bosons and fermions. We have made our program code freely accessible on GitHub.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2503.23433v2
- Title: Macroscopic "Lola/Mola" Cat State
- Authors: Harman Deep Kaur, Mariagrazia Trapanese, Kirill Zatrimaylov
- Categories: physics.pop-ph (primary); physics.pop-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2503.23433v2  pdf=https://arxiv.org/pdf/2503.23433v2.pdf

Abstract:
We present the first--ever example of a macroscopic system in a quantum superposition. The system in question is a Siamese cat known as Lola; however, on a time scale of about 12 hours it oscillates into a different state that we refer to as "Mola". In the "Lola" state, the system is sweet and friendly and allows to cuddle itself, but in the "Mola" state, it is malevolent and witchy. When the probability of the system being in the "Mola" state is high, decoherence is strongly discouraged!

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2509.01608v2
- Title: Reduced fidelities for free fermions out of equilibrium: From dynamical quantum phase transitions to Mpemba effect
- Authors: Gilles Parez, Vincenzo Alba
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.quant-gas; cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2509.01608v2  pdf=https://arxiv.org/pdf/2509.01608v2.pdf

Abstract:
We investigate the out-of-equilibrium dynamics after a quantum quench of the reduced fidelities between the states of a subregion $A$ at different times. Precisely, we consider the fidelity between the time-dependent state of $A$ and its initial value, as well as with the state at infinite time. We denote these fidelities as the reduced Loschmidt echo (RLE) and the final-state fidelity (FSF), respectively. If region $A$ is the full system, the RLE coincides with the standard Loschmidt echo. We focus on quenches from Gaussian states in several instances of the XY spin chain. In the hydrodynamic limit of long times and large sizes of $A$, with their ratio fixed, the reduced fidelities admit a quasiparticle picture interpretation. Interestingly, for some quenches in the hydrodynamic regime the RLE features a complicated structure with an infinite sequence of nested lightcones, corresponding to quasiparticles with arbitrary large group velocities. This leads to a ''staircase'' of cusp-like singularities in the time-derivative of the fidelity. At the sub-hydrodynamic regime for some quenches the RLE exhibits cusp-like singularities, similar to the so-called dynamical quantum phase transitions (DQPT). We conjecture a criterion for the occurrence of the DQPT and for the ''critical'' times at which the singularities occur. Finally, we discuss the hydrodynamic limit of the FSF. In particular, we show that it provides a valuable tool to detect the so-called quantum Mpemba effect.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2509.16199v3
- Title: Classical and quantum theory of magnonic and magnetoelastic nonlinear dynamics in continuum geometries
- Authors: Marco Brühlmann, Yunyoung Hwang, Jorge Puebla, Carlos Gonzalez-Ballestero
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2509.16199v3  pdf=https://arxiv.org/pdf/2509.16199v3.pdf

Abstract:
We provide a theory of spin and acoustic wave coupled nonlinear dynamics in continuum systems. Combining the Landau-Lifshitz-Gilbert equations with the magnetoelastic Hamiltonian, we derive classical equations of motion for the magnetization and acoustic wave amplitudes, that include magnonic nonlinearity -- both three- and four-magnon processes -- as well as linear and nonlinear magnetoelastic interactions. We focus on two-dimensional magnetic films sustaining surface acoustic waves, a geometry where our model successfully reproduces our recent experimental observation of phonon-to-magnon down-conversion under acoustic drive. We provide analytical expressions for all the rates in our equations, which make them particularly suitable for quantization. We then quantize our model, deriving Heisenberg-Langevin equations of motion for magnon and phonon operators, and show how to compute quantum expectation values in the mean field approximation. Our work paves the way toward acoustic control of magnons in the quantum regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2509.16311v2
- Title: Entanglement asymmetry for higher and noninvertible symmetries
- Authors: Francesco Benini, Pasquale Calabrese, Michele Fossati, Amartya Harsh Singh, Marco Venuti
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2509.16311v2  pdf=https://arxiv.org/pdf/2509.16311v2.pdf

Abstract:
Entanglement asymmetry is an observable in quantum systems, constructed using quantum-information methods, suited to detecting symmetry breaking in states -- possibly out of equilibrium -- relative to a subsystem. In this paper we define the asymmetry for generalized finite symmetries, including higher-form and noninvertible ones. To this end, we introduce a "symmetrizer" of (reduced) density matrices with respect to the $C^*$-algebra of symmetry operators acting on the subsystem Hilbert space. We study in detail applications to (1+1)-dimensional quantum field theories: First, we analyze spontaneous symmetry breaking of noninvertible symmetries, confirming that distinct vacua can exhibit different physical properties. Second, we compute the asymmetry of certain excited states in conformal field theories (including the Ising CFT), when the subsystem is either the full circle or an interval therein. The relevant symmetry algebras to consider are the fusion, tube, and strip algebras. Finally, we comment on the case that the symmetry algebra is a (weak) Hopf algebra.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.01477v2
- Title: Emission of pairs of Minkowski photons through the lens of the Unruh effect
- Authors: Juan V. O. Pêgas, Robert Bingham, Gianluca Gregori, George E. A. Matsas
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2510.01477v2  pdf=https://arxiv.org/pdf/2510.01477v2.pdf

Abstract:
We discuss the emission of pairs of photons by charges with generic worldlines in the Minkowski vacuum from the viewpoint of inertial observers and interpret them from the perspective of Rindler observers. We show that the emission of pairs of Minkowski photons corresponds, in general, to three distinct processes according to Rindler observers: scattering, and emission and absorption of pairs of Rindler photons. In the special case of uniformly accelerated charges, the radiation observed in the inertial frame can be fully described by the scattering channel in the Rindler frame. Therefore, the emission of pairs of Minkowski photons -- commonly referred to as Unruh radiation -- can be seen as further evidence supporting the Unruh effect.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.13167v2
- Title: Entropic uncertainty and coherence in Einstein-Gauss-Bonnet gravity
- Authors: Wen-Mei Li, Jianbo Lu, Shu-Min Wu
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2510.13167v2  pdf=https://arxiv.org/pdf/2510.13167v2.pdf

Abstract:
We investigate tripartite quantum-memory-assisted entropic uncertain and quantum coherence for GHZ and W states of a fermionic field in the background of a spherically symmetric black hole of Einstein-Gauss-Bonnet (EGB) gravity. Two distinct scenarios are analyzed: (i) the quantum memories (held by Bob and Charlie) are near the horizon while the measured particle (Alice) remains in the flat region, and (ii) the reverse configuration. Dimensional dependence is observed: in $d>5$ dimensions, the measurement uncertainty decreases monotonically with increasing horizon radius, while coherence increases; in $d=5$, both quantities exhibit non-monotonic behavior due to distinctive thermodynamic properties. Furthermore, comparative analysis reveals that the W state exhibits higher robustness in preserving coherence, whereas the GHZ state shows greater resistance to measurement uncertainty increase induced by Hawking radiation. Notably, the two scenarios yield qualitatively distinct behaviors: quantum coherence is consistently lower in Scenario 1 (quantum memory near horizon) than in Scenario 2 (measured particle near horizon), irrespective of the quantum state. For measurement uncertainty, the W state displays lower uncertainty in Scenario 1, while the GHZ state exhibits the opposite trend, with higher measurement uncertainty in Scenario 1. These results indicate that the characteristics of different quantum resources provide important insights into the selection and optimization of quantum states for information processing in curved spacetime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2510.23247v2
- Title: Chaos in Systems with Quantum Group Symmetry
- Authors: Victor Gorbenko, Aleksandr Zhabin
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2510.23247v2  pdf=https://arxiv.org/pdf/2510.23247v2.pdf

Abstract:
Quantum groups have a long and fruitful history of applications in integrable systems. Can quantum group symmetries exist in the absence of integrability? We provide an explicit example of a system with quantum group global symmetry which is chaotic. The example is a spin chain with next-to-nearest interaction term. We show the chaotic behavior of the system by studying the Eigenvalue statistics. The spin chain is non-unitary but PT-symmetric and, in addition to chaos, exhibits an interesting transition after which the eigenvalues become complex.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2511.04326v2
- Title: Quantum Entanglement as a Cohomological Obstruction
- Authors: Kazuki Ikeda
- Categories: math-ph (primary); math-ph; cond-mat.mes-hall; math.AG; math.QA; quant-ph
- Links: abs=https://arxiv.org/abs/2511.04326v2  pdf=https://arxiv.org/pdf/2511.04326v2.pdf

Abstract:
We recast quantum entanglement as a cohomological obstruction to reconstructing a global quantum state from locally compatible information. We address this by considering presheaf cohomologies of states and entanglement witnesses. Sheafification erases the global-from-local signature while leaving within-patch multipartite structure, captured by local entanglement groups introduced here. For smooth parameter families, the obstruction admits a differential-geometric representative obtained by pairing an appropriate witness field with the curvature of a natural unitary connection on the associated bundle of amplitudes. We also introduce a Quantum Entanglement Index (QEI) as an index-theoretic invariant of entangled states and explain its behavior. Finally, we outline a theoretical physics approach to probe these ideas in quantum many-body systems and suggest a possible entanglement-induced correction as an experimental validation. Detailed numerical implementations for concrete quantum many-body models are presented in the companion paper \cite{2026arXiv260113467I}.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2511.13409v2
- Title: On the Optimal Rate of Convergence for Translation-Invariant 1D Quantum Walks
- Authors: Benjamin Hinrichs, Pascal Mittenbühler
- Categories: math-ph (primary); math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2511.13409v2  pdf=https://arxiv.org/pdf/2511.13409v2.pdf

Abstract:
We study the convergence rate of translation-invariant discrete-time quantum dynamics on a one-dimensional lattice. We prove that the cumulative distributions function of the ballistically scaled position $X(n)/{n}$ after $n$ steps converges at a rate of $n^{-1/3}$ in the Lévy metric as $n\to\infty$. In the special case of step-coin quantum walks with two-dimensional coin space, we recover the same convergence rate for the supremum distance and prove optimality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.09948v2
- Title: Quantum Monte Carlo in Classical Phase Space with the Wigner-Kirkwood Commutation Function. Results for the Saturation Liquid Density of $^4$He
- Authors: Phil Attard
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.quant-gas; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2512.09948v2  pdf=https://arxiv.org/pdf/2512.09948v2.pdf

Abstract:
A Metropolis Monte Carlo algorithm is given for the case of a complex phase space weight, which applies generally in quantum statistical mechanics. Computer simulations using Lennard-Jones $^4$He near the $λ$-transition, including an expansion to third order of the Wigner-Kirkwood commutation function, give a saturation liquid density in agreement with measured values.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-28 09:47
- arXiv: 2512.18958v2
- Title: Correlation functions of harmonic lattices in d-dimensional space
- Authors: Masafumi Shimojo, Satoshi Ishihara, Hironobu Kataoka, Atsuko Matsukawa, Kazuo Koyama
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2512.18958v2  pdf=https://arxiv.org/pdf/2512.18958v2.pdf

Abstract:
We study the correlation functions between the dynamical variables and between their conjugate momenta at sites of a harmonic lattice in the $d$-dimensional Euclidean space. We show that at the thermodynamic limit, they can be expressed in terms of Lauricella's C-type hypergeometric series. Furthermore, using these expressions, we explicitly demonstrate that the correlators near the center of the lattice satisfying Diriclet boundary conditions coincide with those for the lattice with the periodic boundary conditions. By utilizing these expressions, we expect to make it easier to create programs that compute fast and highly precise for the quantum information quantities of subsystems within lattices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18810v1
- Title: Interaction-Conditional Semantics and the Dissolution of Quantum Paradoxes
- Authors: Jonathon Sendall
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2601.18810v1  pdf=https://arxiv.org/pdf/2601.18810v1.pdf

Abstract:
This paper argues that several canonical puzzles in quantum mechanics, including spin measurement, the double slit, entanglement correlations, and Wigner's friend, share a common origin in a semantic error and the illicit promotion of interaction conditional outcomes to intrinsic properties. I introduce four principles that license only configuration relative predication, grounding outcomes in physical measurement geometry while preserving objectivity. Applying these principles uniformly dissolves each puzzle without new physics or ad hoc interpretive machinery. Bell's theorem and the Kochen-Specker theorem are reframed not as dynamical mysteries but as constraints on permissible explanatory structure, evidence that intrinsic-outcome semantics is incompatible with empirical reality. The result is a relational objectivity that avoids both naive property realism and observer subjectivism.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18812v1
- Title: A framework to evaluate the performance of Variational Quantum Algorithms
- Authors: Ernesto Mamedaliev, Vladyslav Libov, Albert Nieto-Morales, Oskar Słowik, Arit Kumar Bishwas
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18812v1  pdf=https://arxiv.org/pdf/2601.18812v1.pdf

Abstract:
Variational Quantum Algorithms (VQAs) are promising methods for solving combinatorial optimization problems on noisy intermediate-scale quantum (NISQ) devices. However, benchmarking VQAs is difficult due to their stochastic behavior and the lack of standardized performance criteria. This work introduces a general framework for evaluating VQAs applied to Quadratic Unconstrained Binary Optimization (QUBO) problems. The framework uses three complementary metrics: feasibility, quality, and reproducibility. It also introduces a quality diagram that visualizes trade-offs between success probability and computational resources. Reproducibility is formalized using Shannon entropy, and a decision rule is defined for selecting algorithms under resource constraints. As a demonstration, the framework is applied to several VQAs using Conditional Value at Risk (CVaR) cost functions and different shot counts on a 16-qubit QUBO instance. The results show how the framework supports systematic benchmarking and provides a foundation for adaptive algorithm selection in hybrid quantum-classical workflows.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18814v1
- Title: Lightweight Quantum-Enhanced ResNet for Coronary Angiography Classification: A Hybrid Quantum-Classical Feature Enhancement Framework
- Authors: Jingsong Xia
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.LG
- Links: abs=https://arxiv.org/abs/2601.18814v1  pdf=https://arxiv.org/pdf/2601.18814v1.pdf

Abstract:
Background: Coronary angiography (CAG) is the cornerstone imaging modality for evaluating coronary artery stenosis and guiding interventional decision-making. However, interpretation based on single-frame angiographic images remains highly operator-dependent, and conventional deep learning models still face challenges in modeling complex vascular morphology and fine-grained texture patterns.Methods: We propose a Lightweight Quantum-Enhanced ResNet (LQER) for binary classification of coronary angiography images. A pretrained ResNet18 is employed as a classical feature extractor, while a parameterized quantum circuit (PQC) is introduced at the high-level semantic feature space for quantum feature enhancement. The quantum module utilizes data re-uploading and entanglement structures, followed by residual fusion with classical features, enabling end-to-end hybrid optimization with a strictly controlled number of qubits.Results: On an independent test set, the proposed LQER outperformed the classical ResNet18 baseline in accuracy, AUC, and F1-score, achieving a test accuracy exceeding 90%. The results demonstrate that lightweight quantum feature enhancement improves discrimination of positive lesions, particularly under class-imbalanced conditions.Conclusion: This study validates a practical hybrid quantum--classical learning paradigm for coronary angiography analysis, providing a feasible pathway for deploying quantum machine learning in medical imaging applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18822v1
- Title: Phase Diagrams of Information Backflow: Unifying Entanglement Revivals and Entropy Overshoots in Minimal Non-Markovian Models
- Authors: Koichi Nakagawa
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2601.18822v1  pdf=https://arxiv.org/pdf/2601.18822v1.pdf

Abstract:
Memory effects in non-Markovian dynamics are often diagnosed either via quantum-correlation revivals or via non-monotonic classical information measures, yet a unified minimal framework comparing their ``backflow phases'' is still lacking. Here we propose an information-backflow phase-diagram approach that places \emph{quantum entanglement revivals} and \emph{classical entropy overshoots} on the same footing through a common backflow functional $N_I=\int_{\dot I>0}\dot I\,dt$. On the quantum side, we employ a fractional (Caputo) extension of a two-state dissipative model embedded by thermo-field dynamics (TFD), yielding a closed-form intrinsic entanglement component $b^{(α)}_{qe}(t)=\frac14[E_α(-λ^αt^α)]^2\sin^2(ωt)$ and an integrated revival measure $N_{qe}$ that delineates a sharp boundary near $α\simeq 1/2$ in the $(α,ω/λ)$ plane. On the classical side, we consider a three-state model whose Markov generator is promoted either to an exponential-kernel generalized master equation (with exact Markov embedding) or to a semi-Markov process with Erlang-2 waiting times. We quantify non-monotonicity by the entropy overshoot $ΔH$ and KL-based diagnostics on the probability simplex. To strengthen the quantum--classical symmetry, we further introduce a \emph{fractional Mittag--Leffler memory kernel} in the classical dynamics and show that an analogous backflow transition emerges around $α\simeq 1/2$, indicating that the boundary originates from the kernel's mathematical structure rather than from quantumness per se. Overall, our results provide a compact, model-agnostic route to classify non-Markovianity by phase diagrams of information backflow and to interpret them via a shared embedding narrative: memory stored in hidden degrees of freedom returns to the observed sector as non-monotonic information flow.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18836v1
- Title: Feshbach-Villars Hamiltonian Approach to the Klein-Gordon Oscillator and Supercritical Step Scattering in Standard and Generalized Doubly Special Relativity
- Authors: A. Boumali, N. Jafari, Y. Chargui
- Categories: quant-ph (primary); quant-ph; gr-qc; hep-th
- Links: abs=https://arxiv.org/abs/2601.18836v1  pdf=https://arxiv.org/pdf/2601.18836v1.pdf

Abstract:
We develop a first-order Feshbach-Villars (FV) Hamiltonian framework for spin-0 relativistic quantum dynamics in the presence of Planck-scale kinematic deformations described within generalized doubly special relativity (G-DSR). Starting from a generic nonlinear momentum-space map, we derive the corresponding modified dispersion relation (MDR) at leading order in the Planck length \(l_p\) and construct a consistent FV linearization of the deformed Klein-Gordon operator. The resulting two-component Hamiltonian remains \(σ_3\)-pseudo-Hermitian at \(\mathcal{O}(l_p)\), which guarantees conservation of the FV charge and current and provides a current-based definition of reflection and transmission in stationary scattering.   As applications, we study two benchmark settings in which the FV metric structure is essential: (i) the one-dimensional Klein-Gordon oscillator and (ii) scattering from electrostatic step and barrier potentials. For the oscillator, we obtain controlled \(\mathcal{O}(l_p)\) branch-resolved spectral shifts and show how kinetic versus mass-shell deformations reshape the level spacing and the high-energy spectral compression. For step and barrier scattering, we compute reflection and transmission coefficients directly from the pseudo-Hermitian FV current and quantify the deformation-induced shift of the supercritical (pair-production) threshold. A comparative analysis of the Amelino-Camelia and Magueijo-Smolin realizations indicates that MS-type deformations generally delay the onset of the supercritical regime and reduce the magnitude of the negative transmitted flux within the validity domain \(l_p E \ll 1\).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18839v1
- Title: Quantum Simulation of the Polaron-Molecule Transition on a NISQ Device
- Authors: Hugo Catala, Ezequiel Valero, German Rodrigo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18839v1  pdf=https://arxiv.org/pdf/2601.18839v1.pdf

Abstract:
The simulation of strongly correlated fermionic systems remains one of the most significant challenges in computational physics due to the exponential growth of the Hilbert space and the fermionic sign problem. In this work, we present a digital quantum simulation framework to explore the Fermi polaron and the Bose-Einstein Condensate (BEC) to Bardeen-Cooper-Schrieffer (BCS) crossover. We develop a unified Hamiltonian formalism that bridges pairing superfluidity and impurity physics, mapping the system onto a gate-based quantum processor via the Jordan-Wigner transformation. Using a first-order Trotter-Suzuki decomposition, we implement a Ramsey interferometry protocol to extract the real-time dynamics and spectral response of the system.   Our results demonstrate a smooth transition from a dressed quasiparticle (polaron) regime to a stable molecular bound state, characterized by a linear energy renormalization in the strong-coupling limit. We validate our simulation against exact classical benchmarks and report successful execution on the Barcelona Supercomputing Center quantum hardware. Despite the inherent noise of the quantum hardware, the hybrid variational approach shows remarkable resilience, accurately capturing the bifurcation of the spectral density

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18856v1
- Title: Operationally induced preferred basis in unitary quantum mechanics
- Authors: Vitaly Pronskikh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18856v1  pdf=https://arxiv.org/pdf/2601.18856v1.pdf

Abstract:
The preferred-basis problem and the definite-outcome aspect of the measurement problem persist even if the detector is modeled unitarily, because experimental data are necessarily represented in a Boolean event algebra of mutually exclusive records whereas the theoretical description is naturally formulated in a noncommutative operator algebra with continuous unitary symmetry. This change of mathematical type constitutes the core of the 'cut': a structurally necessary interface from group-based kinematics to set-based counting. In the presented view the basis relevant for recorded outcomes is not determined by the system Hamiltonian alone; it is induced by the measurement mapping, i.e., by the detector channel together with the coarse-grained readout that defines an instrument. The probabilistic mapping is anchored in symmetry and measure theory: by Gleason-type uniqueness (Gleason for projections in $d>2$ and Busch's extension for Positive Operator-Valued Measures (POVMs) including $d=2$), the trace rule is the unique probability measure consistent with additivity over exclusive events and basis-independence of the unitary sector. A compact qubit--pointer model yields an induced unsharp POVM $E_\pm=\tfrac12(\id\pm η\,σ_z)$ with $η$ fixed by pointer resolution, displaying explicitly how the detector induces the relevant basis. Finally, nested-observer paradoxes are tightened into a non-composability lemma: joint assignment of outcome propositions is obstructed unless a joint instrument exists. This relocates the origin of randomness to the stochasticity of the transition rules.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18861v1
- Title: Post-selection games
- Authors: Víctor Calleja Rodríguez, Ivan A. Bocanegra-Garay, Mateus Araújo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18861v1  pdf=https://arxiv.org/pdf/2601.18861v1.pdf

Abstract:
In this paper, we introduce post-selection games, a generalization of nonlocal games where each round can be not only won or lost by the players, but also discarded by the referee. Such games naturally formalize possibilistic proofs of nonlocality, such as Hardy's paradox. We develop algorithms for computing the local and Tsirelson bounds of post-selection games. Furthermore, we show that they have an unbounded advantage in statistical power over traditional nonlocal games, making them ideally suited for analysing Bell tests with low detection efficiency.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18869v1
- Title: Eigenstate condensation in quantum systems with finite-dimensional Hilbert spaces
- Authors: Christopher David White, Michael Winer, Noam Bernstein
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2601.18869v1  pdf=https://arxiv.org/pdf/2601.18869v1.pdf

Abstract:
Random quantum states drawn from the Haar ensemble with a constraint on the energy expectation value $E_{\mathrm{av}} = \langle ψ| H | ψ\rangle$ display \textit{eigenstate condensation}: for $E_{\mathrm{av}}$ below a critical value $E_c$, they develop macroscopic overlap with the ground state. We study eigenstate condensation in systems with finite-dimensional Hilbert spaces. These systems display three phases: a ground-state phase, in which energy-constrained random states have macroscopic overlap with the ground state; a high-temperature phase, in which they have exponentially small overlap with each energy eigenstate; and an anti-ground-state phase, in which they have macroscopic overlap with the most highly excited state. In local spin systems the ground-state and anti-ground-state phases approach the middle of the spectrum as $1/[\text{system size}]$, but -- because the condensation phase transitions have exponential, rather than polynomial, finite-size scaling -- the crossover becomes exponentially sharp in system size and the high-temperature phase is best understood as an extended phase.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18870v1
- Title: Experimental Demonstration of Commutation Relations Using Intensity Correlations
- Authors: Hans Dang, Sebastian Luff, Martin Fischer, Markus Sondermann, Mojdeh. S. Najafabadi, Luis L. Sanchez-Soto, Gerd Leuchs
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18870v1  pdf=https://arxiv.org/pdf/2601.18870v1.pdf

Abstract:
The canonical commutation relation is a cornerstone of quantum theory and underlies the Heisenberg uncertainty principle. Although uncertainty relations have been extensively tested, direct verifications of the underlying commutation relation itself have remained elusive. We report an experimental demonstration of the bosonic commutation relation for optical field operators based on measurements of two distinct intensity correlation functions. From these measurements, we extract the expectation value of the field-operator commutator for both a single-photon state and coherent state. In both cases, the measured values are consistent with unity, in quantitative agreement with quantum theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18872v1
- Title: Against probability: A quantum state is more than a list of probability distributions
- Authors: Ladina Hausmann, Renato Renner
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18872v1  pdf=https://arxiv.org/pdf/2601.18872v1.pdf

Abstract:
The state $ρ$ of a quantum system can be represented by a vector $\mathbf{P}_{\mathcal{M}}(ρ)$ of outcome probabilities for a set of measurements $\mathcal{M}$. Such representations appear throughout physics, for example, in quantum field theory via correlation functions and in quantum foundations within generalized probabilistic frameworks. In this work, we identify an unavoidable tension: to enable operationally meaningful statements, the map ${ρ\mapsto \mathbf{P}_{\mathcal{M}}(ρ)}$ must be topologically robust $\unicode{x2013}$ preserving the notion of closeness between states. Yet, a probability representation that is topologically robust cannot simultaneously retain other essential structure, such as the subsystem structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18879v1
- Title: Multivariate Multicycle Codes for Complete Single-Shot Decoding
- Authors: Feroz Ahmed Mian, Owen Gwilliam, Stefan Krastanov
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2601.18879v1  pdf=https://arxiv.org/pdf/2601.18879v1.pdf

Abstract:
We introduce multivariate multicycle (MM) codes, a new family of quantum error correcting codes that unifies and generalizes bivariate bicycle codes, multivariate bicycle codes, abelian two-block group algebra codes, generalized bicycle codes, trivariate tricycle codes, and n-dimensional toric codes. MM codes are Calderbank-Shor-Steane (CSS) codes defined from length-t chain complexes with $t \ge 4$. The chief advantage of these codes is that they possess metachecks and high confinement that permit complete single-shot decoding, while also having additional algebraic structure that might enable logical non-Clifford gates. We offer a framework that facilitates the construction of long-length chain complexes through the use of Koszul complex. In particular, obtaining explicit boundary maps (parity check and metacheck matrices) is particularly straightforward in our approach. This simple but very general parameterization of codes permitted us to efficiently perform a numerical search, where we identify several MM code candidates that demonstrate these capabilities at high rates and high code distances. Examples of new codes with parameters $[[n,k,d]]$ include $[[96, 12, 8]]$, $[[96, 44, 4]]$ $[[144, 40, 4]]$, $[[216, 12, 12]]$, $[[360, 30, 6]]$, $[[384, 80, 4]]$, $[[486, 24, 12]]$, $[[486, 66, 9]]$ and $[[648, 60, 9]]$. Notably, our codes achieve confinement profiles that surpass all known single-shot decodable quantum CSS codes of practical blocksize.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18898v1
- Title: Fault-tolerant quantum simulation of the Pauli-Breit Hamiltonian for ab initio hybrid quantum-classical molecular design with applications to photodynamic therapy
- Authors: Emil Zak
- Categories: quant-ph (primary); quant-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2601.18898v1  pdf=https://arxiv.org/pdf/2601.18898v1.pdf

Abstract:
Relativistic spin effects drive subtle molecular phenomena ranging from intersystem crossing in photodynamic therapy to spin-mediated catalysis and high-resolution spectroscopy. These effects are described by the Pauli-Breit Hamiltonian, which extends the nonrelativistic electronic Hamiltonian by including one- and two-electron spin-orbit and spin-spin interactions. First-principles simulations of the full Pauli-Breit Hamiltonian rapidly become intractable on classical computers due to the exponential growth of the Hilbert space and the complexity of two-body spin-dependent terms. We propose a fault-tolerant quantum algorithm for computing molecular energy levels and properties governed by the Pauli-Breit Hamiltonian. Our approach block-encodes the relativistic Hamiltonian in a second-quantized, doubly factorized representation. By reformulating the Hamiltonian in a symmetry-adapted Majorana basis, we construct efficient linear-combination-of-unitaries circuits that encode spin-orbit interactions without effective or mean-field approximations. We introduce spin-controlled Pauli-SWAP networks that decouple spin and orbital control logic, enabling a unified treatment of relativistic spin mixing with only modest overhead relative to spin-free simulations. We analyze quantum resources in terms of logical qubits and T-gate complexity, showing that explicit spin degrees of freedom do not worsen the asymptotic scaling. The prefactor is reduced by a factor of two compared to direct linear-combination-of-unitaries approaches. Finally, we outline a hybrid quantum-classical workflow for designing photodynamic therapy photosensitizers, artificial photosynthesis catalysts, and other systems where accurate relativistic spin effects are essential.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18937v1
- Title: Complete transparency with three active-passive-coupled optical resonators
- Authors: Xiao-Bo Yan, Liu Yang, Bing He
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.18937v1  pdf=https://arxiv.org/pdf/2601.18937v1.pdf

Abstract:
The phenomena of induced transparency, with the typical examples of electromagnetically induced transparency (EIT) in atomic media and coupled optical resonators, have attracted tremendous interest since their discoveries. Due to the limitations of the involved elements, however, near-100\% transmissions were reported under highly demanding experimental conditions for atomic and other media. Based on a structure of three linearly coupled optical resonators, an active one carrying a possibly arbitrary optical gain and two passive ones simply with dissipation, we demonstrate that a transmitted light field can become completely transparent through the structure, which displays all properties similar to those of EIT. Manifested by a destructive interference to annihilate the intracavity field in the resonator directly coupled to the input, this complete transparency exists for any feasible power of the transmitted field and all realizable coupling strengths of the dark resonator with the input and the neighboring resonator, as long as the inter-cavity coupling for two other resonators is adjustable over a suitable range. A free control on the transparency window size and output field intensity can be realized by tuning two inter-cavity couplings without modifying the built-in system parameters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18941v1
- Title: Krylov's State Complexity and Information Geometry in Qubit Dynamics
- Authors: Carlo Cafaro, Emma Clements, Vishnu Vardhan Anuboyina
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18941v1  pdf=https://arxiv.org/pdf/2601.18941v1.pdf

Abstract:
We compare Krylov's state complexity with an information-geometric (IG) measure of complexity for the quantum evolution of two-level systems. Focusing on qubit dynamics on the Bloch sphere, we analyze evolutions generated by stationary and nonstationary Hamiltonians, corresponding to geodesic and nongeodesic trajectories. We formulate Krylov complexity in geometric terms, both instantaneously and in a time-averaged sense, and contrast it with an IG complexity of quantum evolutions characterized in terms of efficiency and curvature. We show that the two measures reflect fundamentally different aspects of quantum dynamics: Krylov's state complexity quantifies the directional spread of the evolving state relative to the initial state, whereas the IG complexity captures the effective volume explored along the trajectory on the Bloch sphere. This geometric distinction explains their inequivalent behavior and highlights the complementary nature of state-based and information-geometric notions of complexity in quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18953v1
- Title: Reinforcement Learning for Quantum Technology
- Authors: Marin Bukov, Florian Marquardt
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.stat-mech; cs.AI; cs.LG
- Links: abs=https://arxiv.org/abs/2601.18953v1  pdf=https://arxiv.org/pdf/2601.18953v1.pdf

Abstract:
Many challenges arising in Quantum Technology can be successfully addressed using a set of machine learning algorithms collectively known as reinforcement learning (RL), based on adaptive decision-making through interaction with the quantum device. After a concise and intuitive introduction to RL aimed at a broad physics readership, we discuss the key ideas and core concepts in reinforcement learning with a particular focus on quantum systems. We then survey recent progress in RL in all relevant areas. We discuss state preparation in few- and many-body quantum systems, the design and optimization of high-fidelity quantum gates, and the automated construction of quantum circuits, including applications to variational quantum eigensolvers and architecture search. We further highlight the interactive capabilities of RL agents, emphasizing recent progress in quantum feedback control and quantum error correction, and briefly discuss quantum reinforcement learning as well as applications to quantum metrology. The review concludes with a discussion of open challenges -- such as scalability, interpretability, and integration with experimental platforms -- and outlines promising directions for future research. Throughout, we highlight experimental implementations that exemplify the increasing role of reinforcement learning in shaping the development of quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18960v1
- Title: Quantum capacity analysis of finite-dimensional lossy channels
- Authors: Sofia Cocciaretto, Vittorio Giovannetti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18960v1  pdf=https://arxiv.org/pdf/2601.18960v1.pdf

Abstract:
Traditionally, Quantum Information, and Quantum Communication specifically, have been focused on qubit-based architectures. Recent results, however, highlighted that higher dimensional architectures (qudit-based) may present advantages both in terms of communication and computation; a family of channels called Multi-level Amplitude Damping (MAD) channels, which are a possible qudit generalization of the well known Amplitude Damping Channels, is able to model energy decay processes that may happen during signal transmission. In this work, the Quantum Capacity of 4-dimensional MAD's is studied, relying on a technique for computing it even outside of degradable and antidegradable conditions. We also characterized the complete region of antidegradability and degradability in the parameter space for a generic d-dimensional MAD using both analytical and semi-numerical methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18961v1
- Title: Private Proofs of When and Where
- Authors: Uma Girish, Greg Gluch, Shafi Goldwasser, Tal Malkin, Leo Orshansky, Henry Yuen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18961v1  pdf=https://arxiv.org/pdf/2601.18961v1.pdf

Abstract:
Position verification schemes are interactive protocols where entities prove their physical location to others; this enables interactive proofs for statements of the form "I am at a location $L$." Although secure position verification cannot be achieved with classical protocols (even with computational assumptions), they are feasible with quantum protocols.   In this paper we introduce the notion of zero-knowledge position verification, which generalizes position verification in two ways:   1. enabling entities to prove more sophisticated statements about their locations at different times (for example, "I was NOT near location $L$ at noon yesterday").   2. maintaining privacy for any other detail about their true location besides the statement they are proving.   We construct zero-knowledge position verification from standard position verification and post-quantum one-way functions. The central tool in our construction is a primitive we call position commitments, which allow entities to privately commit to their physical position in a particular moment, which is then revealed at some later time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18976v1
- Title: Qubit-qudit entanglement transfer in defect centers with high-spin nuclei
- Authors: W. -R. Hannes, Guido Burkard
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.18976v1  pdf=https://arxiv.org/pdf/2601.18976v1.pdf

Abstract:
We propose a scheme for accumulating entanglement between long-lived qudits provided by central nuclear spins of defect centers. Assuming a generic setting, the electron spin of each node acts as the communication qubit and may be entangled with other nodes, e.g., through a spin-photon interface. The generally available Ising component of the hyperfine interaction is shown to facilitate repeated entanglement transfer onto memory qudits of arbitrary dimension $d\le 2I+1$ with $I$ the nuclear spin quantum number. When $d$ is set to an integer power of two, maximal entanglement can be generated deterministically and without intermittent driving of nuclear spins. The scheme is applicable to several candidate systems, including the $^{73}$Ge germanium vacancy in diamond.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19057v1
- Title: Time-series based quantum state discrimination
- Authors: Samuel Jung, Neel Vora, Akel Hashim, Yilun Xu, Gang Huang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19057v1  pdf=https://arxiv.org/pdf/2601.19057v1.pdf

Abstract:
Accurate quantum state readout is crucial for error correction and algorithms, but measurement errors are detrimental. Readout fidelity is typically limited by a poor signal-to-noise ratio (SNR) and energy relaxation ($T_1$ decay), a significant problem for superconducting qubits. While most approaches classify results using clustering algorithms on integrated readout signals, these methods cannot distinguish a qubit that was initially in the ground state from one that decayed to it during measurement. We instead propose using machine learning (ML) on the raw, non-integrated analog signal. We apply time-series classification models, such as a long short-term memory (LSTM) network, to the full data trajectory. We find that our LSTM model, combined with filtering and feature engineering, consistently outperforms clustering. The largest improvements come from reclassifying points in the boundary regions between clusters. These points correspond to atypical measurement records, likely due to transient or noisy features lost during data integration. By retaining temporal information, sequence-aware models like LSTMs can better discriminate these trajectories, whereas clustering methods based on integrated values are more prone to misclassification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19059v1
- Title: The cost of quantum algorithms for biochemistry: A case study in metaphosphate hydrolysis
- Authors: Ryan LaRose, Alan Bidart, Ben DalFavero, Sophia E. Economou, J. Wayne Mullinax, Mafalda Ramôa, Jeremiah Rowland, Brenda Rubenstein, et al.
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2601.19059v1  pdf=https://arxiv.org/pdf/2601.19059v1.pdf

Abstract:
We evaluate the quantum resource requirements for ATP/metaphosphate hydrolysis, one of the most important reactions in all of biology with implications for metabolism, cellular signaling, and cancer therapeutics. In particular, we consider three algorithms for solving the ground state energy estimation problem: the variational quantum eigensolver, quantum Krylov, and quantum phase estimation. By utilizing exact classical simulation, numerical estimation, and analytical bounds, we provide a current and future outlook for using quantum computers to solve impactful biochemical and biological problems. Our results show that variational methods, while being the most heuristic, still require substantially fewer overall resources on quantum hardware, and could feasibly address such problems on current or near-future devices. We include our complete dataset of biomolecular Hamiltonians and code as benchmarks to improve upon with future techniques.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19093v1
- Title: Inverse-Squeezing Kennedy Receiver for Near-Helstrom Discrimination of Displaced-Squeezed BPSK
- Authors: Enhao Bai, Jian Peng, Tianyi Wu, Chen Dong, Kai Wen, Fengkai Sun, Zhenrong Zhang, Chun Zhou, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19093v1  pdf=https://arxiv.org/pdf/2601.19093v1.pdf

Abstract:
To address the discrimination problem of binary phase-shift keyed displaced squeezed vacuum states (S-BPSK), this paper proposes an Inverse-squeezing Kennedy (IS-Kennedy) receiver. This architecture incorporates an inverse-squeezing operator following the displacement operation of a conventional Kennedy receiver, mapping the S-BPSK signals onto equivalent large-amplitude coherent states. Furthermore, it employs a photon-number-resolving (PNR) detector to perform maximum a posteriori (MAP) decision-making. Theoretical analysis demonstrates that, under ideal conditions, the IS-Kennedy receiver effectively translates the transmitter's squeezing resources into a displacement gain at the receiver. Consequently, its error probability approaches the Helstrom bound across the entire energy spectrum, remaining within a constant factor of 3 dB. In the low-photon-number regime ($N \approx 0.6$), the proposed scheme surpasses the coherent-state limit, achieving an error rate below 1\%. Furthermore, this paper provides an in-depth analysis of system performance under non-ideal conditions, revealing the robustness of PNR detection against background dark counts and a characteristic ``parity photon-number step'' saturation effect arising from squeezing parameter mismatch.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19111v1
- Title: Introduction to Quantum Entanglement Geometry
- Authors: Kazuki Ikeda
- Categories: quant-ph (primary); quant-ph; hep-th; math-ph; math.QA; math.RT
- Links: abs=https://arxiv.org/abs/2601.19111v1  pdf=https://arxiv.org/pdf/2601.19111v1.pdf

Abstract:
This article is an expository account aimed at viewing entanglement in finite-dimensional quantum many-body systems as a phenomenon of global geometry. While the mathematics of general quantum states has been studied extensively, this article focuses specifically on their entanglement. When a quantum system varies over a classical parameter space, each fiber may look like the same Hilbert space, yet there may be no global identification because of twisting in the gluing data. Describing this situation by an Azumaya algebra, one always obtains the family of pure-state spaces as a Severi-Brauer scheme.   The main focus is to characterize the condition under which the subsystem decomposition required to define entanglement exists globally and compatibly, by a reduction to the stabilizer subgroup of the Segre variety, and to explain that the obstruction appears in the Brauer class. As a consequence, quantum states yield a natural filtration dictated by entanglement on the Severi-Brauer scheme.   Using a spin system on a torus as an example, we show concretely that the holonomy of the gluing can produce an entangling quantum gate, and can appear as an obstruction class distinct from the usual Berry numbers or Chern numbers. For instance, even for quantum systems that have traditionally been regarded as having no topological band structure, the entanglement of their eigenstates can be related to global geometric universal quantities, reflecting the background geometry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19152v1
- Title: Evolution of quantum geometric tensor of 1D periodic systems after a quench
- Authors: Jia-Chen Tang, Xu-Yang Hou, Yu-Huan Huang, Hao Guo. Chih-Chun Chien
- Categories: quant-ph (primary); quant-ph; cond-mat.other
- Links: abs=https://arxiv.org/abs/2601.19152v1  pdf=https://arxiv.org/pdf/2601.19152v1.pdf

Abstract:
We investigate the post-quench dynamics of the quantum geometric tensor (QGT) of 1D periodic systems with a suddenly changed Hamiltonian. The diagonal component with respect to the crystal momentum gives a metric corresponding to the variance of the time-evolved position, and its coefficient of the quadratic term in time is the group-velocity variance, signaling ballistic wavepacket dispersion. The other diagonal QGT component with respect to time reveals the energy variance. The off-diagonal QGT component features a real part as a covariance and an imaginary part representing a quench-induced curvature. Using the Su-Schrieffer-Heeger (SSH) model as an example, our numerical results of different quenches confirm that the post-quench QGT is governed by physical quantities and local geometric objects from the initial state and post-quench bands, such as the Berry connection, group velocities, and energy variance. Furthermore, the connections between the QGT and physical observables suggest the QGT as a comprehensive probe for nonequilibrium phenomena.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19159v1
- Title: The complexity of semidefinite programs for testing $k$-block-positivity
- Authors: Qian Chen, Benoît Collins
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19159v1  pdf=https://arxiv.org/pdf/2601.19159v1.pdf

Abstract:
We extend \cite{chen2025srkbp} by analyzing the complexity of the $k$-block-positivity testing algorithm. In this paper, we investigate a symmetry reduction scheme based on rectangular shaped Young diagrams. Connecting the complexity to the dimensions of irreducible representations of $\mathrm{U}(d)$, we derive an explicit formula for the complexity, which also clarifies why the semidefinite program hierarchy collapses in the $k=d$ case.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19166v1
- Title: High-Performance Exact Synthesis of Two-Qubit Quantum Circuits
- Authors: Andrew N. Glaudell, Michael Jarret, Swan Klein, Samuel S. Mendelson, T. C. Mooney, Mingzhen Tian
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19166v1  pdf=https://arxiv.org/pdf/2601.19166v1.pdf

Abstract:
Exact synthesis provides unconditional optimality and canonical structure, but is often limited to small, carefully scoped regimes. We present an exact synthesis framework for two-qubit circuits over the Clifford+$T$ gate set that optimizes $T$-count exactly. Our approach exhausts a bounded search space, exploits algebraic canonicalization to avoid redundancy, and constructs a lookup table of optimal implementations that turns synthesis into a query. Algorithmically, we combine meet-in-the-middle ideas with provable pruning rules and problem-specific arithmetic designed for modern hardware. The result is an exact, reusable synthesis engine with substantially improved practical performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19182v1
- Title: The strong converse exponent of composable randomness extraction against quantum side information
- Authors: Roberto Rubboli, Marco Tomamichel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19182v1  pdf=https://arxiv.org/pdf/2601.19182v1.pdf

Abstract:
We find a tight characterization of the strong converse exponent for randomness extraction against quantum side information. In contrast to previous tight bounds, we employ a composable error criterion given by the fidelity (or purified distance) to a uniform distribution in product with the marginal state. The characterization is in terms of a club-sandwiched conditional entropy recently introduced by Rubboli, Goodarzi and Tomamichel and used by Li, Li and Yu to establish the strong converse exponent for the case of classical side information. This provides the first precise operational interpretation of this family of conditional entropies in the quantum setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19184v1
- Title: Quantum simulation of the nonlinear Schrödinger equation via measurement-induced potential reconstruction
- Authors: Kaiwen Weng, Zhaoyuan Meng, Zixuan Yang, Guohui Hu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19184v1  pdf=https://arxiv.org/pdf/2601.19184v1.pdf

Abstract:
The nonlinear Schrödinger equation (NLSE) is a fundamental model that describes diverse complex phenomena in nature. However, simulating the NLSE on a quantum computer is inherently challenging due to the presence of the nonlinear term. We propose a hybrid quantum-classical framework for simulating the NLSE based on the split-step Fourier method. During the linear propagation step, we apply the kinetic evolution operator to generate an intermediate quantum state. Subsequently, the Hadamard test is employed to measure the Fourier components of low-wavenumber modes, enabling the efficient reconstruction of nonlinear potentials. The phase transformation corresponding to the reconstructed potential is then implemented via a quantum circuit using the phase kickback technique. To validate the efficacy of the proposed algorithm, we numerically simulate the evolution of a Gaussian wave packet, a soliton wave, and the wake flow past a cylinder. The simulation results demonstrate excellent agreement with the corresponding classical solutions. This work provide a concrete basis for analyzing accuracy-cost trade-offs in quantum-classical simulations of nonlinear dispersive wave dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19190v1
- Title: Analytical construction of $(n, n-1)$ quantum random access codes saturating the conjectured bound
- Authors: Takayuki Suzuki
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19190v1  pdf=https://arxiv.org/pdf/2601.19190v1.pdf

Abstract:
Quantum Random Access Codes (QRACs) embody the fundamental trade-off between the compressibility of information into limited quantum resources and the accessibility of that information, serving as a cornerstone of quantum communication and computation. In particular, the $(n, n-1)$-QRACs, which encode $n$ bits of classical information into $n-1$ qubits, provides an ideal theoretical model for verifying quantum advantage in high-dimensional spaces; however, the analytical derivation of optimal codes for general $n$ has remained an open problem. In this paper, we establish an analytical construction method for $(n, n-1)$-QRACs by using an explicit operator formalism. We prove that this construction strictly achieves the numerically conjectured upper bound of the average success probability, $\mathcal{P} = 1/2 + \sqrt{(n-1)/n}/2$, for all $n$. Furthermore, we present a systematic algorithm to decompose the derived optimal POVM into standard quantum gates. Since the resulting decoding circuit consists solely of interactions between adjacent qubits, it can be implemented with a circuit depth of $O(n)$ even under linear connectivity constraints. Additionally, we analyze the high-dimensional limit and demonstrate that while the non-commutativity of measurements is suppressed, an information-theoretic gap of $O(\log n)$ from the Holevo bound inevitably arises for symmetric encoding. This study not only provides a scalable implementation method for high-dimensional quantum information processing but also offers new insights into the mathematical structure at the quantum-classical boundary.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19206v1
- Title: Universal Operational Privacy in Distributed Quantum Sensing
- Authors: Min Namkung, Dong-Hyun Kim, Seongjin Hong, Yong-Su Kim, Su-Yong Lee, Hyang-Tag Lim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19206v1  pdf=https://arxiv.org/pdf/2601.19206v1.pdf

Abstract:
Privacy is a fundamental requirement in distributed quantum sensing networks, where multiple clients estimate spatially distributed parameters using shared quantum resources while interacting with potentially untrusted servers. Despite its importance, existing privacy conditions rely on idealized quantum bounds and do not fully capture the operational constraints imposed by realistic measurements. Here, we introduce a universal operational privacy framework for distributed quantum sensing, formulated in terms of the experimentally accessible classical Fisher information matrix and applicable to arbitrary protocols characterized by singular information structures. The proposed condition provides a protocol-independent criterion ensuring that no information about individual parameters is accessible to untrusted parties. We further experimentally demonstrate that a distributed quantum sensing protocol employing fewer photons than the number of estimated parameters simultaneously satisfies the universal privacy condition and achieves Heisenberg-limited precision. Our results establish universal operational constraints governing privacy in distributed quantum sensing networks and provide a foundation for practical, privacy-preserving quantum sensing beyond full-rank regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19209v1
- Title: Pareto-Front Engineering of Dynamical Sweet Spots in Superconducting Qubits
- Authors: Zhen Yang, Shan Jin, Yajie Hao, Guangwei Deng, Xiu-Hao Deng, Re-Bing Wu, Xiaoting Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19209v1  pdf=https://arxiv.org/pdf/2601.19209v1.pdf

Abstract:
Operating superconducting qubits at dynamical sweet spots (DSSs) suppresses decoherence from low-frequency flux noise. A key open question is how long coherence can be extended under this strategy and what fundamental limits constrain it. Here we introduce a fully parameterized, multi-objective periodic-flux modulation framework that simultaneously optimizes energy relaxation $T_1$ and pure dephasing $T_φ$, thereby quantifying the tradeoff between them. For fluxonium qubits with realistic noise spectra, our method enhances $T_φ$ by a factor of 3-5 compared with existing DSS strategies while maintaining $T_1$ in the hundred-microsecond range. We further prove that, although DSSs eliminate first-order sensitivity to low-frequency noise, relaxation rate cannot be reduced arbitrarily close to zero, establishing an upper bound on achievable $T_1$. At the optimized working points, we identify double-DSS regions that are insensitive to both DC and AC flux, providing robust operating bands for experiments. As applications, we design single- and two-qubit control protocols at these operating points and numerically demonstrate high-fidelity gate operations. These results establish a general and useful framework for Pareto-front engineering of DSSs that substantially improves coherence and gate performance in superconducting qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19279v1
- Title: Reinforcement Learning for Enhanced Advanced QEC Architecture Decoding
- Authors: Yidong Zhou, Lingyi Kong, Yifeng Peng, Zhiding Liang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19279v1  pdf=https://arxiv.org/pdf/2601.19279v1.pdf

Abstract:
The advent of promising quantum error correction (QEC) codes with efficient resource utilization and high-performance fault-tolerant quantum memories signifies a critical step towards realizing practical quantum computation. While surface codes have been a dominant approach, their limitations have spurred the development of more advanced QEC architectures. These advanced codes often present increased complexity, demanding innovative decoding methodologies. This work investigates the application of reinforcement learning (RL) techniques, including hybrid and multi-agent approaches, to enhance the decoding of various advanced QEC architectures. By leveraging the ability of RL to learn optimal strategies from noisy syndrome measurements, we explore the potential for achieving improved logical error rates and scalability compared to traditional decoding methods. Our approach examines the adaptation of reinforcement learning to exploit the structural properties of these modern QEC models. We also explore the benefits of combining different RL algorithms to address the multifaceted nature of the decoding problem, considering factors such as code degeneracy and real-world noise characteristics. With our proposed method, we are able to demonstrate that an autonomously trained agent can derive decoding schemes for the complex decoding requirement of advanced QEC architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19324v1
- Title: Graphene Josephson Junctions for Engineering Motional Quanta
- Authors: Zhen-Yang Peng, Mehdi Abdi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19324v1  pdf=https://arxiv.org/pdf/2601.19324v1.pdf

Abstract:
We propose a hybrid quantum device based on the graphene Josephson junctions, where the vibrational degrees of freedom of a graphene membrane couple to the superconducting circuits. The flexural mode-controlled tunneling of the Cooper pairs introduces a strong and tunable coupling even at the zero-point fluctuations level. By employing this interaction, we show that a parametric process can be efficiently implemented. We then investigate foundational and technological applications of our hybrid device empowered by nonlinear interactions, with fast generation of non-classical mechanical states, and critically enhanced quantum sensing under suitable quantum control. Our work provides the possibility of employing the graphene motional degree of freedom for quantum information processing in circuit quantum nanomechanical structures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19326v1
- Title: Beyond Photon Shot Noise: Chemical Limits in Spectrophotometric Precision
- Authors: Georg Engelhardt, Dahai He, JunYan Luo
- Categories: quant-ph (primary); quant-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2601.19326v1  pdf=https://arxiv.org/pdf/2601.19326v1.pdf

Abstract:
In this work, we investigate precision limitations in spectrophotometry (i.e., spectroscopic concentration measurements) imposed by chemical processes of molecules. Using the recently developed Photon-resolved Floquet theory, which generalizes Maxwell-Bloch theory for higher-order measurement statistics, we analyze a molecular model system subject to chemical reactions whose electronic and optical properties depend on the chemical state. Analysis of sensitivity bounds reveals: (i) Phase measurements are more sensitive than intensity measurements; (ii) Sensitivity exhibits three regimes: photon-shot-noise limited, chemically limited, and intermediate; (iii) Sensitivity shows a turnover as a function of reaction rate due to the interplay between coherent electronic dynamics and incoherent chemical dynamics. Our findings demonstrate that chemical properties must be considered to estimate ultimate precision limits in optical spectrophotometry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19348v1
- Title: Continuous-mode analysis of improved two-way CV-QKD
- Authors: Yanhao Sun, Jiayu Ma, Xiangyu Wang, Song Yu, Ziyang Chen, Hong Guo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19348v1  pdf=https://arxiv.org/pdf/2601.19348v1.pdf

Abstract:
Continuous-variable quantum key distribution (CV-QKD) enables information-theoretically secure key generation between legitimate parties. To further enhance system performance, an improved two-way CV-QKD protocol has been proposed, which is accessible in practice and exhibits increased robustness against excess noise. However, in practical implementations, device nonidealities inevitably drive the optical field from the single-mode regime into the continuous-mode regime. In this work, we introduce temporal modes to characterize the evolution of optical fields in the improved two-way protocol and establish a security analysis framework for the continuous-mode scenario based on adaptive normalization with calibrated shot-noise unit. In addition, finite-size effects are taken into account in the analysis. Our results demonstrate that the improved two-way protocol retains a performance advantage over one-way counterpart. The analysis provides useful guidance for the practical implementation and performance optimization of improved two-way CV-QKD systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19356v1
- Title: Experimental High-Accuracy and Broadband Quantum Frequency Sensing via Geodesic Control
- Authors: Si-Qi Chen, Qi-Tao Duan, Teng Li, He Lu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19356v1  pdf=https://arxiv.org/pdf/2601.19356v1.pdf

Abstract:
Accurate frequency estimation of oscillating signals over a broad bandwidth is a central task in quantum sensing, yet it is often compromised by spurious responses to higher-order harmonics in realistic multi-frequency environments. Here we experimentally demonstrate a high-accuracy and broadband quantum frequency sensing protocol based on geodesic control, implemented using the electron spin of a single nitrogen-vacancy center in diamond. By engineering an intrinsically single-frequency response, geodesic control enables bias-free frequency estimation with strong suppression of harmonic-induced systematic errors across a wide spectral range spanning from the megahertz to the gigahertz regime. Furthermore, by incorporating synchronized readout, we achieve millihertz-level frequency resolution under noisy signal conditions. Our results provide systematic experimental benchmarking of geodesic control for quantum frequency sensing and establish it as a practical approach for high-accuracy metrology in realistic environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19391v1
- Title: Remote magnon-phonon entanglement in the waveguide-magnomechanics
- Authors: Shi-fan Qi, Fan Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19391v1  pdf=https://arxiv.org/pdf/2601.19391v1.pdf

Abstract:
Generating long-distance quantum entanglement is crucial for advancing quantum information processing. In this work, we propose a protocol for generating remote magnon-phonon entanglement in a hybrid waveguide-magnomechanical system, where multiple spatially separated magnon modes couple to a common waveguide while interacting with their respective phonon modes. By applying tailored pulsed drives and engineering the magnon-phonon interactions, our scheme enables the creation of diverse long-distance and dynamically stable entanglement. Beyond basic magnon-phonon two-mode entanglement, it supports genuine multimode entanglement between a single phonon and multiple magnons, bipartite entanglement between a single magnon and multiple phonons, as well as genuine four-mode entanglement involving two magnons and two phonons. Moreover, we show that dissipative magnon-magnon interactions mediated by traveling photons can generate substantially stronger long-distance entanglement than coherent couplings. Our work provides an experimentally feasible scheme for the remote generation of magnon-phonon entanglement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19392v1
- Title: Nanomechanical sensor resolving impulsive forces below its zero-point fluctuations
- Authors: Martynas Skrabulis, Martin Colombano Sosa, Nicola Carlon Zambon, Andrei Militaru, Massimiliano Rossi, Martin Frimmer, Lukas Novotny
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19392v1  pdf=https://arxiv.org/pdf/2601.19392v1.pdf

Abstract:
The sensitivity of a mechanical transducer is ultimately limited by its inherent quantum fluctuations. Here, we use an optically levitated nanoparticle to measure impulsive forces smaller than the particle's zero-point momentum uncertainty. Our approach relies on reversibly squeezing the levitated particle's center-of-mass motion to coherently amplify the perturbation. We demonstrate resolving single impulsive-force kicks as small as 6.9 keV/c, a value 0.6 dB below the sensor's zero-point value.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19396v1
- Title: Mikado strategy for the detection of atoms in images of microtrap arrays
- Authors: Marc Cheneau, François Goudail
- Categories: quant-ph (primary); quant-ph; physics.data-an
- Links: abs=https://arxiv.org/abs/2601.19396v1  pdf=https://arxiv.org/pdf/2601.19396v1.pdf

Abstract:
Building on top of our recent work [arXiv:2502.08511], we introduce a new strategy to solve the problem of detecting atoms in high-resolution images of microtrap arrays. By alternating estimation and detection steps, we get rid of the need for an explicit model to compute the posterior occupancy probability of each site given its a priori optimal estimate. As direct benefits, we show an improved detection accuracy compared to our previous work when the sites are not optically well resolved, and we expect a greater robustness against real experimental conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19469v1
- Title: Quantum Zeno-like Paradox for Position Measurements: A Particle Precisely Found in Space is Nowhere to be Found in Hilbert Space
- Authors: Xabier Oianguren-Asua, Roderich Tumulka
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2601.19469v1  pdf=https://arxiv.org/pdf/2601.19469v1.pdf

Abstract:
On a quantum particle in the unit interval $[0,1]$, perform a position measurement with inaccuracy $1/n$ and then a quantum measurement of the projection $|φ\rangle\langleφ|$ with some arbitrary but fixed normalized $φ$. Call the outcomes $X \in[0,1]$ and $Y \in\{0,1\}$. We show that in the limit $n\to\infty$ corresponding to perfect precision for $X$, the probability of $Y=1$ tends to 0 for every $φ$. Since there is no density matrix, pure or mixed, which upon measurement of any $|φ\rangle\langleφ|$ yields outcome 1 with probability 0, our result suggests that a novel type of quantum state beyond Hilbert space is necessary to describe a quantum particle after a perfect position measurement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19581v1
- Title: Flux-tunable transmon incorporating a van der Waals superconductor via an Al/AlO$_x$/4Hb-TaS$_2$ Josephson junction
- Authors: Eliya Blumenthal, Ilay Mangel, Amit Kanigel, Shay Hacohen-Gourgy
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2601.19581v1  pdf=https://arxiv.org/pdf/2601.19581v1.pdf

Abstract:
Incorporating van der Waals (vdW) superconductors into Josephson elements extends circuit-QED beyond conventional Al/AlO$_x$/Al tunnel junctions and enables microwave probes of unconventional condensates and subgap excitations. In this work, we realize a flux-tunable transmon whose nonlinear inductive element is an Al/AlO$_x$/4Hb-TaS$_2$ Josephson junction. The tunnel barrier is formed by sequential deposition and full in-situ oxidation of ultrathin Al layers on an exfoliated 4Hb-TaS$_2$ flake, followed by deposition of a top Al electrode, yielding a robust, repeatable hybrid junction process compatible with standard transmon fabrication. Embedding the device in a three-dimensional copper cavity, we observe a SQUID-like flux-dependent spectrum that is quantitatively reproduced by a standard dressed transmon--cavity Hamiltonian, from which we extract parameters in the transmon regime. Across measured devices we obtain sub-microsecond energy relaxation ($T_1$ from $0.08$ to $0.69~μ$s), while Ramsey measurements indicate dephasing faster than our $16$ ns time resolution. We also find a pronounced discrepancy between the Josephson energy inferred from spectroscopy and that expected from the Ambegaokar--Baratoff relation using room-temperature junction resistances, pointing to nontrivial junction physics in the hybrid Al/AlO$_x$/4Hb-TaS$_2$ system. Although we do not resolve material-specific subgap modes in the present geometry, this work establishes a practical route to integrating 4Hb-TaS$_2$ into coherent quantum circuits and provides a baseline for future edge-sensitive designs aimed at enhancing coupling to boundary and subgap degrees of freedom in vdW superconductors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19610v1
- Title: Broadcasting quantum nonlinearity in hybrid systems
- Authors: Alisa D. Manukhova, Andrey A. Rakhubovsky, Radim Filip
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19610v1  pdf=https://arxiv.org/pdf/2601.19610v1.pdf

Abstract:
Linear oscillators contribute to most branches of contemporary quantum science. They have already successfully served as quantum sensors and memories, found applications in quantum communication, and hold promise for cluster-state-based quantum computing. To master universal quantum processing with linear oscillators, an unconditional nonlinear operation is required. We propose such an operation using light-mediated interaction with another system that possesses a nonlinearity equivalent to more than a quadratic potential. Such a potential grants access to a nonlinear operation that can be broadcast to the target linear system. The nonlinear character of the operation can be verified by observing adequate negative values of the target system's Wigner function and the squeezing of the variance of a certain nonlinear combination of the quadratures below the thresholds attainable by Gaussian states. We explicitly evaluate an optically levitated mechanical oscillator as a flexible source of nonlinearity for a proof-of-principle demonstration of the nonlinearity broadcasting to linear systems, for example, mechanical oscillators or macroscopic atomic spin ensembles.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19635v1
- Title: DynQ: A Dynamic Topology-Agnostic Quantum Virtual Machine via Quality-Weighted Community Detection
- Authors: Shusen Liu, Pascal Jahan Elahi, Ugo Varetto
- Categories: quant-ph (primary); quant-ph; cs.SE
- Links: abs=https://arxiv.org/abs/2601.19635v1  pdf=https://arxiv.org/pdf/2601.19635v1.pdf

Abstract:
Quantum cloud platforms remain fundamentally non-virtualised: despite rapid hardware scaling, each user program still monopolises an entire quantum processor, preventing resource sharing, economic scalability, and quality-of-service differentiation. Existing Quantum Virtual Machine (QVM) designs attempt spatial multiplexing through topology-specific or template-based partitioning, but these approaches are brittle under hardware heterogeneity, calibration drift, and transient defects, which dominate real quantum devices. We present DynQ, the first dynamic, topology-agnostic Quantum Virtual Machine that virtualises quantum hardware using quality-weighted community detection. Instead of imposing fixed geometric regions, DynQ models a quantum processor as a weighted graph derived from live calibration data and automatically discovers execution regions that maximise internal gate quality while minimising inter-region coupling. This operationalises the classical virtualisation principle of high cohesion and low coupling in a quantum-native setting, producing execution regions that are connectivity-efficient, noise-aware, and resilient to crosstalk and defects. We evaluate DynQ across five IBM Quantum backends using calibration-derived noise simulation and on two production devices, comparing against state-of-the-art QVM and standard compilation baselines. On hardware with pronounced spatial quality variation, DynQ achieves up to 19.1 percent higher fidelity and 45.1 percent lower output error. When transient hardware defects cause baseline executions to fail completely, DynQ adapts dynamically and achieves over 86 percent fidelity. By transforming calibrated device graphs into adaptive virtual hardware abstractions, DynQ decouples quantum programs from fragile physical layouts and enables reliable, high-utilisation quantum cloud services.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19650v1
- Title: Efficient Application of Tensor Network Operators to Tensor Network States
- Authors: Richard M. Milbradt, Shuo Sun, Christian B. Mendl, Johnnie Gray, Garnet K. -L. Chan
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2601.19650v1  pdf=https://arxiv.org/pdf/2601.19650v1.pdf

Abstract:
The performance of tensor network methods has seen constant improvements over the last few years. We add to this effort by introducing a new algorithm that efficiently applies tree tensor network operators to tree tensor network states inspired by the density matrix method and the Cholesky decomposition. This application procedure is a common subroutine in tensor network methods. We explicitly include the special case of tensor train structures and demonstrate how to extend methods commonly used in this context to general tree structures. We compare our newly developed method with the existing ones in a benchmark scenario with random tensor network states and operators. We find our Cholesky-based compression (CBC) performs equivalently to the current state-of-the-art method, while outperforming most established methods by at least an order of magnitude in runtime. We then apply our knowledge to perform circuit simulation of tree-like circuits, in order to test our method in a more realistic scenario. Here, we find that more complex tree structures can outperform simple linear structures and achieve lower errors than those possible with the simple structures. Additionally, our CBC still performs among the most successful methods, showing less dependence on the different bond dimensions of the operator.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19677v1
- Title: Transversal gates of the ((3,3,2)) qutrit code and local symmetries of the absolutely maximally entangled state of four qutrits
- Authors: Ian Tan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19677v1  pdf=https://arxiv.org/pdf/2601.19677v1.pdf

Abstract:
We provide a proof that there exists a bijection between local unitary (LU) orbits of absolutely maximally entangled (AME) states in $(\mathbb{C}^D)^{\otimes n}$ where $n$ is even, also known as perfect tensors, and LU orbits of $((n-1,D,n/2))_D$ quantum error correcting codes. Thus, by a result of Rather et al. (2023), the AME state of 4 qutrits and the pure $((3,3,2))_3$ qutrit code $\mathcal{C}$ are both unique up to the action of the LU group. We further explore the connection between the 4-qutrit AME state and the code $\mathcal{C}$ by showing that the group of transversal gates of $\mathcal{C}$ and the group of local symmetries of the AME state are closely related. Taking advantage of results from Vinberg's theory of graded Lie algebras, we find generators of both of these groups.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19703v1
- Title: Approximate Decoherence, Recoherence and Records in Isolated Quantum Systems
- Authors: Philipp Strasberg, Joseph Schindler, Jiaozi Wang, Andreas Winter
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; gr-qc
- Links: abs=https://arxiv.org/abs/2601.19703v1  pdf=https://arxiv.org/pdf/2601.19703v1.pdf

Abstract:
Using the framework of decoherent histories, we study which past events leave detectable records in isolated quantum systems under the realistic assumption that decoherence is approximate and not perfect. In the first part we establish -- asymptotically for a large class of (pseudo-)random histories -- that the number of reliable records can be much smaller than the number of possible events, depending on the degree of decoherence. In the second part we reveal a clear decoherence structure for long histories based on a numerically exact solution of a random matrix model that, as we argue, captures generic aspects of decoherence. We observe recoherence between histories with a small Hamming distance, for localized histories admitting a high purity Petz recovery state, and for maverick histories that are statistical outliers with respect to Born's rule. From the perspective of the Many Worlds Interpretation, the first part -- which views the self-location problem as a coherent version of quantum state discrimination -- reveals a "branch selection problem", and the second part sheds light on the emergence of Born's rule and the theory confirmation problem.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19713v1
- Title: Robust topological quantum state transfer with long-range interactions in Rydberg arrays
- Authors: Siri Raupach, Beatriz Olmos, Mathias B. M. Svendsen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19713v1  pdf=https://arxiv.org/pdf/2601.19713v1.pdf

Abstract:
We develop a theoretical framework for fast, robust and high-fidelity topological quantum state transfer in one-dimensional systems with long-range couplings, motivated by chains of Rydberg atoms with dipole-dipole interactions. Such long-range interactions naturally give rise to extended Su-Schrieffer-Heeger and Rice-Mele models supporting topologically protected edge states. We show that these edge states enable high-fidelity edge-to-edge excitation transfer using both time-independent protocols, based on coherent edge state dynamics, and time-dependent protocols, based on adiabatic modulation of system parameters. Long-range couplings play a central role by enhancing the relevant energy gaps, leading to a substantial improvement in transfer efficiency compared to nearest neighbour models. The resulting transfer is robust against positional disorder, reflecting its topological origin and highlighting the potential of long-range interacting platforms for reliable quantum state transfer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19719v1
- Title: Optimally Driven Dressed Qubits
- Authors: Alon Salhov, Sagi Nechushtan, Alex Retzker
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.atom-ph; physics.chem-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.19719v1  pdf=https://arxiv.org/pdf/2601.19719v1.pdf

Abstract:
The applicability and performance of qubits dressed by classical fields are limited because their control protocols give rise to an undesired counter-rotating term (CRT). This in turn forces operation in a regime where a (dressed) rotating-wave approximation (RWA) is valid, thereby restricting key aspects of their operation. Here, using only a single coupling axis in the laboratory frame, we introduce a dressed-qubit control protocol that optimally removes the CRT, eliminating the need for the RWA and delivering substantial improvements in multiple performance metrics, including single-qubit gate speed, two-qubit gate fidelity, spectroscopic range, clock stability, and coherence preservation. In addition, we provide a general parameterization together with a Floquet-based coherence-time expression, which elucidates the protocol's working principles and lowers the barrier to adoption. Collectively, these advances position our scheme as the state-of-the-art strategy for qubit control, paving the way for a wider class of quantum technologies to be realized using dressed-qubit architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19721v1
- Title: Quantum Light Detection with Enhanced Photonic Neural Network
- Authors: Stanisław Świerczewski, Dogyun Ko, Amir Rahmani, Juan Camilo López Carreño, Wouter Verstraelen, Piotr Deuar, Barbara Piętka, Timothy C. H. Liew, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2601.19721v1  pdf=https://arxiv.org/pdf/2601.19721v1.pdf

Abstract:
Advances in quantum technologies are accelerating the demand for optical quantum state sensors that combine high precision, versatility, and scalability within a unified hardware platform. Quantum reservoir computing offers a powerful route toward this goal by exploiting the nonlinear dynamics of quantum systems to process and interpret quantum information efficiently. Photonic neural networks are particularly well suited for such implementations, owing to their intrinsic sensitivity to photon-encoded quantum information. However, the practical realisation of photonic quantum reservoirs remains constrained by the inherently weak optical nonlinearities of available materials and the technological challenges of fabricating densely coupled quantum networks. To address these limitations, we introduce a hybrid quantum-classical detection protocol that integrates the advantages of quantum reservoirs with the adaptive learning capabilities of analogue neural networks. This synergistic architecture substantially enhances information-extraction accuracy and robustness, enabling low-cost performance improvements of quantum light sensors. Based on the proposed approach, we achieved significant improvements in quantum state classification, tomography, and feature regression, even for reservoirs with a relatively small nonlinearity-to-losses ratio $U/γ\approx 0.02$ in a network of only five nodes. By reducing reliance on material nonlinearity and reservoir size, the proposed approach facilitates the practical deployment of high-fidelity photonic quantum sensors on existing integrated platforms, paving the way toward chip-scale quantum processors and photonic sensing technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19737v1
- Title: A two-mode model for black hole evaporation and information flow
- Authors: Erfan Bayenat, Babak Vakili
- Categories: quant-ph (primary); quant-ph; gr-qc; hep-th
- Links: abs=https://arxiv.org/abs/2601.19737v1  pdf=https://arxiv.org/pdf/2601.19737v1.pdf

Abstract:
We develop and analyze a two-oscillator model for black hole evaporation in which an effective geometric degree of freedom and a representative Hawking radiation mode are described by coupled harmonic oscillators with opposite signs in their free Hamiltonians. The normal-mode structure is obtained analytically and the corresponding modal amplitudes determine the pattern of energy exchange between the two sectors. To bridge the discrete and semiclassical pictures, we introduce smooth envelope functions that provide a continuous effective description along the geometric variable. Numerical simulations in a truncated Fock space show that the two oscillators exchange quanta in an approximately out-of-phase manner, consistent with an effective conservation of $\langle n_x\rangle - \langle n_y\rangle$. The reduced entropy $S_x(t)$ exhibits periodic growth, indicating entanglement generation. These results demonstrate that even a minimal two-mode framework can capture key qualitative features of energy transfer and information flow during evaporation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19738v1
- Title: Quantum Circuit Pre-Synthesis: Learning Local Edits to Reduce $T$-count
- Authors: Daniele Lizzio Bosco, Lukasz Cincio, Giuseppe Serra, M. Cerezo
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.LG
- Links: abs=https://arxiv.org/abs/2601.19738v1  pdf=https://arxiv.org/pdf/2601.19738v1.pdf

Abstract:
Compiling quantum circuits into Clifford+$T$ gates is a central task for fault-tolerant quantum computing using stabilizer codes. In the near term, $T$ gates will dominate the cost of fault tolerant implementations, and any reduction in the number of such expensive gates could mean the difference between being able to run a circuit or not. While exact synthesis is exponentially hard in the number of qubits, local synthesis approaches are commonly used to compile large circuits by decomposing them into substructures. However, composing local methods leads to suboptimal compilations in key metrics such as $T$-count or circuit depth, and their performance strongly depends on circuit representation. In this work, we address this challenge by proposing \textsc{Q-PreSyn}, a strategy that, given a set of local edits preserving circuit equivalence, uses a RL agent to identify effective sequences of such actions and thereby obtain circuit representations that yield a reduced $T$-count upon synthesis. Experimental results of our proposed strategy, applied on top of well-known synthesis algorithms, show up to a $20\%$ reduction in $T$-count on circuits with up to 25 qubits, without introducing any additional approximation error prior to synthesis.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19762v1
- Title: Inter-branch message transfer on superconducting quantum processors: a multi-architecture benchmark
- Authors: Cameron V. Cogburn
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19762v1  pdf=https://arxiv.org/pdf/2601.19762v1.pdf

Abstract:
We treat inter-branch message transfer in a Wigner's-friend circuit as a practical benchmark for near-term superconducting quantum processors. Implementing Violaris' unitary message-transfer primitive, we compare performance across IBM Eagle, Nighthawk, and Heron (r2/r3) processors for message sizes up to $n=32$, without error mitigation. We study three message families -- sparse (one-hot), half-weight, and dense -- and measure conditional string success $p_{\mathrm{all}}=\Pr(P=μ\mid R=0)$, memory erasure after uncomputation, and correlation diagnostics (branch contrast and bitwise mutual information). The sparse family compiles to essentially constant two-qubit depth, yielding a depth-controlled probe of device noise: at $n=32$ we observe $p_{\mathrm{all}}$ spanning $\approx0.07$ to $\approx0.68$ across backends. In contrast, half and dense messages incur rapidly growing routing overhead, and transpiler-seed variability becomes a practical limitation near the coherence frontier. We further report an amplitude sweep (no-amplification test) and a divergence ``cousins'' sweep that quantifies degradation with branch-conditioned complexity. All data and figure-generation scripts are released.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19765v1
- Title: Spectral Codes: A Geometric Formalism for Quantum Error Correction
- Authors: Satoshi Kanno, Yoshi-aki Shimada
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2601.19765v1  pdf=https://arxiv.org/pdf/2601.19765v1.pdf

Abstract:
We present a new geometric perspective on quantum error correction based on spectral triples in noncommutative geometry. In this approach, quantum error correcting codes are reformulated as low energy spectral projections of Dirac type operators that separate global logical degrees of freedom from local, correctable errors. Locality, code distance, and the Knill Laflamme condition acquire a unified spectral and geometric interpretation in terms of the induced metric and spectrum of the Dirac operator. Within this framework, a wide range of known error correcting codes including classical linear codes, stabilizer codes, GKP type codes, and topological codes are recovered from a single construction. This demonstrates that classical and quantum codes can be organized within a common geometric language. A central advantage of the spectral triple perspective is that the performance of error correction can be directly related to spectral properties. We show that leakage out of the code space is controlled by the spectral gap of the Dirac operator, and that code preserving internal perturbations can systematically increase this gap without altering the encoded logical subspace. This yields a geometric mechanism for enhancing error correction thresholds, which we illustrate explicitly for a stabilizer code. We further interpret Berezin Toeplitz quantization as a mixed spectral code and briefly discuss implications for holographic quantum error correction. Overall, our results suggest that quantum error correction can be viewed as a universal low energy phenomenon governed by spectral geometry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19777v1
- Title: Resolving Gauge Ambiguities of the Berry Connection in Non-Hermitian Systems
- Authors: Ievgen I. Arkhipov
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2601.19777v1  pdf=https://arxiv.org/pdf/2601.19777v1.pdf

Abstract:
Non-Hermitian systems display spectral and topological phenomena absent in Hermitian physics; yet, their geometric characterization can be hindered by an intrinsic ambiguity rooted in the eigenspace of non-Hermitian Hamiltonians, which becomes especially pronounced in the pure quantum regime. Because left and right eigenvectors are not related by conjugation, their norms are not fixed, giving rise to a biorthogonal ${\rm GL}(N,{\mathbb C})$ gauge freedom. Consequently, the standard Berry connection admits four inequivalent definitions depending on how left and right eigenvectors are paired, giving rise to distinct Berry phases and generally complex-valued holonomies. Here we show that these ambiguities and the emergence of complex phases are fully resolved by introducing a covariant-derivative formalism built from the metric tensor of the Hilbert space of the underlying non-Hermitian Hamiltonian. The resulting unique Berry connection remains real-valued under an arbitrary ${\rm GL}(N,{\mathbb C})$ frame change, and transforms as an affine gauge potential, while reducing to the conventional Berry (or Wilczek-Zee) connection in the Hermitian limit. This establishes an unambiguous and gauge-consistent geometric framework for Berry phases, non-Abelian holonomies, and topological invariants in quantum systems described by non-Hermitian Hamiltonians.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19816v1
- Title: Simple broadband signal detection at the fundamental limit
- Authors: Anthony M. Polloreno, Graeme Smith
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2601.19816v1  pdf=https://arxiv.org/pdf/2601.19816v1.pdf

Abstract:
Broadband detection of a weak oscillatory field with unknown carrier frequency underlies magnetometry, axion searches and gravitational-wave sensing. We show that the Grover-like integration-time lower bound for this task is a geometric corollary an upper bound on the integrated quantum Fisher information, a metrological constraint. We further give an all-analog multi-resonant protocol based on a randomized Su-Schrieffer-Heeger control Hamiltonian and an m-register GHZ probe and verify near-optimal scaling through simulation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19820v1
- Title: Enhanced quantum state discrimination under general measurements with entanglement and nonorthogonality restrictions
- Authors: Swati Choudhary, Aparajita Bhattacharyya, Ujjwal Sen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19820v1  pdf=https://arxiv.org/pdf/2601.19820v1.pdf

Abstract:
The minimum error probability for distinguishing between two quantum states is bounded by the Helstrom limit, derived under the assumption that measurement strategies are restricted to positive operator-valued measurements. We explore scenarios in which the error probability for discriminating two quantum states can be reduced below the Helstrom bound under some constrained access of resources, indicating the use of measurement operations that go beyond the standard positive operator-valued measurements framework. We refer to such measurements as non-positive operator-valued measurements. While existing literature often associates these measurements with initial entanglement between the system and an auxiliary, followed by joint projective measurement and discarding the auxiliary, we demonstrate that initial entanglement between system and auxiliary is not necessary for the emergence of such measurements in the context of state discrimination. Interestingly, even initial product states can give rise to effective non-positive measurements on the subsystem, and achieve sub-Helstrom discrimination error when discriminating quantum states of the subsystem.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19823v1
- Title: A Folded Surface Code Architecture for 2D Quantum Hardware
- Authors: Zhu Sun, Zhenyu Cai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19823v1  pdf=https://arxiv.org/pdf/2601.19823v1.pdf

Abstract:
Qubit shuttling has become an indispensable ingredient for scaling leading quantum computing platforms, including semiconductor spin, neutral-atom, and trapped-ion qubits, enabling both crosstalk reduction and tighter integration of control hardware. Cai et al. (2023) proposed a scalable architecture that employs short-range shuttling to realize effective three-dimensional connectivity on a strictly two-dimensional device. Building on recent advances in quantum error correction, we show that this architecture enables the native implementation of folded surface codes on 2D hardware, reducing the runtime of all single-qubit logical Clifford gates and logical CNOTs within subsets of qubits from $\mathcal{O}(d)$ in conventional surface code lattice surgery to constant time. We present explicit protocols for these operations and demonstrate that access to a transversal $S$ gate reduces the spacetime volume of 8T-to-CCZ magic-state distillation by more than an order of magnitude compared with standard 2D lattice surgery approaches. Finally, we introduce a new "virtual-stack" layout that more efficiently exploits the quasi-three-dimensional structure of the architecture, enabling efficient multilayer routing on these two-dimensional devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19848v1
- Title: Theory of low-weight quantum codes
- Authors: Fuchuan Wei, Zhengyi Han, Austin Yubo He, Zimu Li, Zi-Wen Liu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19848v1  pdf=https://arxiv.org/pdf/2601.19848v1.pdf

Abstract:
Low check weight is practically crucial code property for fault-tolerant quantum computing, which underlies the strong interest in quantum low-density parity-check (qLDPC) codes. Here, we explore the theory of weight-constrained stabilizer codes from various foundational perspectives including the complexity of computing code weight and the explicit boundary of feasible low-weight codes in both theoretical and practical settings. We first prove that calculating the optimal code weight is an $\mathsf{NP}$-hard problem, demonstrating the necessity of establishing bounds for weight that are analytical or efficiently computable. Then we systematically investigate the feasible code parameters with weight constraints. We provide various explicit analytical lower bounds and in particular completely characterize stabilizer codes with weight at most 3, showing that they have distance 2 and code rate at most 1/4. We also develop a powerful linear programming (LP) scheme for setting code parameter bounds with weight constraints, which yields exact optimal weight values for all code parameters with $n\leq 9$. We further refined this constraint from multiple perspectives by considering the generator weight distribution and overlap. In particular, we consider practical architectures and demonstrate how to apply our methods to e.g.~the IBM 127-qubit chip. Our study brings the weight as a crucial parameter into coding theory and provide guidance for code design and utility in practical scenarios.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19857v1
- Title: Symmetric and Antisymmetric Quantum States from Graph Structure and Orientation
- Authors: Matheus R. de Jesus, Eduardo O. C. Hoefel, Renato M. Angelo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19857v1  pdf=https://arxiv.org/pdf/2601.19857v1.pdf

Abstract:
Graph states provide a powerful framework for describing multipartite entanglement in quantum information science. In their standard formulation, graph states are generated by controlled-$Z$ interactions and naturally encode symmetric exchange properties. Here we establish a precise correspondence between graph topology and exchange symmetry by proving that a graph state is fully symmetric under particle permutations if and only if the underlying graph is complete. We then introduce a generalized graph-based construction using a non-commutative two-qudit gate, denoted $GR$, which requires directed edges and an explicit vertex ordering. We show that complete directed graphs endowed with appropriate orientations, for an odd number of qudits generate fully antisymmetric multipartite states. Together, these results provide a unified graph-theoretic description of bosonic and fermionic exchange symmetry based on graph completeness and edge orientation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19889v1
- Title: Distinguishing synthetic unravelings on quantum computers
- Authors: Eloy Piñol, Piotr Sierant, Dustin Keys, Romain Veyron, Miguel Angel García-March, Tanner Reese, Morgan W. Mitchell, Jan Wehr, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.19889v1  pdf=https://arxiv.org/pdf/2601.19889v1.pdf

Abstract:
Distinct monitoring or intervention schemes can produce different conditioned stochastic quantum trajectories while sharing the same unconditional (ensemble-averaged) dynamics. This is the essence of unravelings of a given Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) master equation: any trajectory-ensemble average of a function that is linear in the conditional state is completely determined by the unconditional density matrix, whereas applying a nonlinear function before averaging can yield unraveling-dependent results beyond the average evolution. A paradigmatic example is resonance fluorescence, where direct photodetection (jump/Poisson) and homodyne or heterodyne detection (diffusive/Wiener) define inequivalent unravelings of the same GKSL dynamics. In earlier work, we showed that nonlinear trajectory averages can distinguish such unravelings, but observing the effect in that optical setting requires demanding experimental precision. Here we translate the same idea to a digital setting by introducing synthetic unravelings implemented as quantum circuits acting on one and two qubits. We design two unravelings - a projective measurement unraveling and a random-unitary "kick" unraveling - that share the same ensemble-averaged evolution while yielding different nonlinear conditional-state statistics. We implement the protocols on superconducting-qubit hardware provided by IBM Quantum to access trajectory-level information. We show that the variance across trajectories and the ensemble-averaged von Neumann entropy distinguish the unravelings in both theory and experiment, while the unconditional state and the ensemble-averaged expectation values that are linear in the state remain identical. Our results provide an accessible demonstration that quantum trajectories encode information about measurement backaction beyond what is fixed by the unconditional dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18811v1
- Title: Variational Quantum Circuit-Based Reinforcement Learning for Dynamic Portfolio Optimization
- Authors: Vincent Gurgul, Ying Chen, Stefan Lessmann
- Categories: cs.LG (primary); cs.LG; q-fin.CP; q-fin.PM; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18811v1  pdf=https://arxiv.org/pdf/2601.18811v1.pdf

Abstract:
This paper presents a Quantum Reinforcement Learning (QRL) solution to the dynamic portfolio optimization problem based on Variational Quantum Circuits. The implemented QRL approaches are quantum analogues of the classical neural-network-based Deep Deterministic Policy Gradient and Deep Q-Network algorithms. Through an empirical evaluation on real-world financial data, we show that our quantum agents achieve risk-adjusted performance comparable to, and in some cases exceeding, that of classical Deep RL models with several orders of magnitude more parameters. In addition to improved parameter efficiency, quantum agents exhibit reduced variability across market regimes, indicating robust behaviour under changing conditions. However, while quantum circuit execution is inherently fast at the hardware level, practical deployment on cloud-based quantum systems introduces substantial latency, making end-to-end runtime currently dominated by infrastructural overhead and limiting practical applicability. Taken together, our results suggest that QRL is theoretically competitive with state-of-the-art classical reinforcement learning and may become practically advantageous as deployment overheads diminish. This positions QRL as a promising paradigm for dynamic decision-making in complex, high-dimensional, and non-stationary environments such as financial markets. The complete codebase is released as open source at: https://github.com/VincentGurgul/qrl-dpo-public

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18843v1
- Title: Human Cardiac Measurements with Diamond Magnetometers
- Authors: Muhib Omar, Magnus Benke, Shaowen Zhang, Jixing Zhang, Michael Kuebler, Pouya Sharbati, Ara Rahimpour, Arno Gueck, et al.
- Categories: physics.med-ph (primary); physics.med-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18843v1  pdf=https://arxiv.org/pdf/2601.18843v1.pdf

Abstract:
We demonstrate direct, non-invasive and non-contact detection of human cardiac magnetic signals using quantum sensors based on nitrogen-vacancy (NV) centers in diamond. Three configurations were employed recording magnetocardiography (MCG) signals in various shielded and unshielded environments. The signals were averaged over a few hundreds up to several thousands of heart beats to detect the MCG traces. The compact room-temperature NV sensors exhibit sensitivities of 6-26 pT/Hz^(1/2) with active sensing volumes below 0.5 mm^3, defining the performance level of the demonstrated MCG measurements. While the present signals are obtained by averaging, this performance already indicates a clear path toward single-shot MCG sensing. To move beyond shielded environments toward practical clinical use, strong noise suppression is required. To this end, we implement NV-based gradiometry and achieve efficient common-mode noise rejection, enabled by the intrinsically small sensing volume of NV sensors. Together, these multi-platform results obtained across diverse magnetic environments provide a solid foundation for translating quantum sensors into human medical diagnostics such as MCG and magnetoencephalography (MEG).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18863v1
- Title: Tame Complexity of Effective Field Theories in the Quantum Gravity Landscape
- Authors: Thomas W. Grimm, David Prieto, Mick van Vliet
- Categories: hep-th (primary); hep-th; math-ph; math.LO; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18863v1  pdf=https://arxiv.org/pdf/2601.18863v1.pdf

Abstract:
Effective field theories consistent with quantum gravity obey surprising finiteness constraints, appearing in several distinct but interconnected forms. In this work we develop a framework that unifies these observations by proposing that the defining data of such theories, as well as the landscape of effective field theories that are valid at least up to a fixed cutoff, admit descriptions with a uniform bound on complexity. To make this precise, we use tame geometry and work in sharply o-minimal structures, in which tame sets and functions come with two integer parameters that quantify their information content; we call this pair their tame complexity. Our Finite Complexity Conjectures are supported by controlled examples in which an infinite Wilsonian expansion nevertheless admits an equivalent finite-complexity description, typically through hidden rigidity conditions such as differential or recursion relations. We further assemble evidence from string compactifications, highlighting the constraining role of moduli space geometry and the importance of dualities. This perspective also yields mathematically well-defined notions of counting and volume measures on the space of effective theories, formulated in terms of effective field theory domains and coverings, whose finiteness is naturally enforced by the conjectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18867v1
- Title: Jordan-Wigner mapping between quantum-spin and fermionic Casimir effects
- Authors: Katsumasa Nakayama, Kei Suzuki
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.mes-hall; cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18867v1  pdf=https://arxiv.org/pdf/2601.18867v1.pdf

Abstract:
The Jordan-Wigner transformation connects spin operators in one-dimensional spin systems and fermionic operators. In this work, we elucidate the relationship between the finite-size corrections in the spin representation and the fermionic Casimir effect in the corresponding fermion representation. In particular, we focus on the ground-state energy of one-dimensional transverse-field Ising and XY models, and show that all finite-size corrections can be interpreted as lattice fermionic Casimir effects. We further find several types of Casimir phenomena, such as the conventional Casimir energy from massless fields, damping behavior from massive fields, vanishing behavior from flat or nonrelativistic bands, and oscillating behavior from the finite-density effect. Our findings establish a dictionary between finite-size corrections in spin chains and fermionic Casimir effects, and provide experimentally relevant platforms for the fermionic Casimir phenomena.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18894v1
- Title: Dissipative diffusion in quantum state preparation: from passive cooling to system-bath engineering
- Authors: Tim Pokart, Lukas König, Sebastian Diehl, Jan Carl Budich
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18894v1  pdf=https://arxiv.org/pdf/2601.18894v1.pdf

Abstract:
We investigate and compare two particle number conserving protocols for the preparation of a topologically nontrivial state. The first is derived from thermally coupling the system to a cold bath, while the second is based on engineered dissipation. We numerically study the time required to reach the target state as well as its robustness against physically important perturbations. Crucially, in both protocols the cooling capability is limited by dissipatively induced diffusion processes. The resulting quadratic scaling of the cooling time with system size is corroborated also analytically using mean-field approximations and a purely classical random walk model. Furthermore, we find that the engineered protocol admits a unique and stable dark state, which contributes to an ongoing discussion regarding the applicability of dissipative state preparation to many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18922v1
- Title: Stacked quantum Ising systems and quantum Ashkin-Teller model
- Authors: Davide Rossini, Ettore Vicari
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18922v1  pdf=https://arxiv.org/pdf/2601.18922v1.pdf

Abstract:
We analyze the quantum states of an isolated composite system consisting of two stacked quantum Ising (SQI) subsystems, coupled by a local Hamiltonian term that preserves the $Z_2$ symmetry of each subsystem. The coupling strength is controlled by an intercoupling parameter $w$, with $w=0$ corresponding to decoupled quantum Ising systems. We focus on the quantum correlations of one of the two SQI subsystems, $S$, in the ground state of the global system, and study their dependence on both the state of the weakly-coupled complementary part $E$ and the intercoupling strength. We concentrate on regimes in which $S$ develops critical long-range correlations. The most interesting physical scenario arises when both SQI subsystems are critical. In particular, for identical SQI subsystems, the global system is equivalent to the quantum Ashkin-Teller model, characterized by an additional $Z_2$ interchange symmetry between the two subsystem operators. In this limit, one-dimensional SQI systems exhibit a peculiar critical line along which the length-scale critical exponent $ν$ varies continuously with $w$, while two-dimensional systems develop quantum multicritical behaviors characterized by an effective enlargement of the symmetry of the critical modes, from the actual $Z_2\oplus Z_2$ symmetry to a continuous O(2) symmetry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18964v1
- Title: Sedentary quantum walks on bipartite graphs
- Authors: Karen Meagher, Hermie Monterde
- Categories: math.CO (primary); math.CO; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18964v1  pdf=https://arxiv.org/pdf/2601.18964v1.pdf

Abstract:
If a quantum walk starting on a vertex tends to stay at home, then that vertex is said to be sedentary. We prove that almost all planar graphs and almost all trees contain at least two sedentary vertices for any assignment of edge weights -- a result that suggests vertex sedentariness is a common phenomenon in trees and planar graphs. For weighted bipartite graphs, we show that a vertex is not sedentary whenever 0 does not belong to its eigenvalue support. Consequently, each vertex in a nonsingular weighted bipartite graph is not sedentary, a stark contrast to weighted trees and weighted planar graphs. A corollary of this result is that every vertex in a bipartite graph with a unique perfect matching is not sedentary for any assignment of edge weights. We also construct new families of weighted bipartite graphs with sedentary vertices using the bipartite double and subdivision operations. Finally, we show that unweighted paths and unweighted even cycles contain no sedentary vertices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.18973v1
- Title: When Does Adaptation Win? Scaling Laws for Meta-Learning in Quantum Control
- Authors: Nima Leclerc, Chris Miller, Nicholas Brawand
- Categories: cs.LG (primary); cs.LG; cs.AI; eess.SY; quant-ph
- Links: abs=https://arxiv.org/abs/2601.18973v1  pdf=https://arxiv.org/pdf/2601.18973v1.pdf

Abstract:
Quantum hardware suffers from intrinsic device heterogeneity and environmental drift, forcing practitioners to choose between suboptimal non-adaptive controllers or costly per-device recalibration. We derive a scaling law lower bound for meta-learning showing that the adaptation gain (expected fidelity improvement from task-specific gradient steps) saturates exponentially with gradient steps and scales linearly with task variance, providing a quantitative criterion for when adaptation justifies its overhead. Validation on quantum gate calibration shows negligible benefits for low-variance tasks but $>40\%$ fidelity gains on two-qubit gates under extreme out-of-distribution conditions (10$\times$ the training noise), with implications for reducing per-device calibration time on cloud quantum processors. Further validation on classical linear-quadratic control confirms these laws emerge from general optimization geometry rather than quantum-specific physics. Together, these results offer a transferable framework for decision-making in adaptive control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19006v1
- Title: Frequency- and time-resolved second order quantum coherence function of IDTBT single-molecule fluorescence
- Authors: Quanwei Li, Yuping Shi, Lam Lam, K. Birgitta Whaley, Graham Fleming
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19006v1  pdf=https://arxiv.org/pdf/2601.19006v1.pdf

Abstract:
The frequency- and time-resolved second order quantum coherence function (g(2)(τ)) of single-molecule fluorescence has recently been proposed as a powerful new quantum light spectroscopy that can reveal intrinsic quantum coherence in excitation energy transfer in molecular systems ranging from simple dimers to photosynthetic complexes. Yet, no experiments have been reported to date. Here, we have developed a single-molecule fluorescence g(2)(τ) quantum light spectroscopy (SMFg2-QLS) that can simultaneously measure the fluorescence intensity, lifetime, spectra, and g(2)(τ) with frequency resolution, for a single molecule in a controlled environment at both room temperature and cryogenic temperature. As a proof of principle, we have studied single molecules of IDTBT (indacenodithiophene-co-benzothiadiazole), a semiconducting donor-acceptor conjugated copolymer with a chain-like structure that shows a high carrier mobility and annihilation-limited long-range exciton transport. We have observed different g(2)(τ=0) values with different bands or bandwidths of the single molecule IDTBT fluorescence. The general features are consistent with theoretical predictions and suggest non-trivial excited state quantum dynamics, possibly showing quantum coherence, although further analysis and confirmation will require additional theoretical calculations that take into account the complexity and inhomogeneity of individual IDTBT single molecular chains. Our results demonstrate the feasibility and promise of frequency- and time-resolved SMFg2-QLS to provide new insights into molecular quantum dynamics and to reveal signatures of intrinsic quantum coherence in photosynthetic light harvesting that are independent of the nature of the light excitation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19076v1
- Title: C2NP: A Benchmark for Learning Scale-Dependent Geometric Invariances in 3D Materials Generation
- Authors: Can Polat, Erchin Serpedin, Mustafa Kurban, Hasan Kurban
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; cond-mat.mes-hall; cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19076v1  pdf=https://arxiv.org/pdf/2601.19076v1.pdf

Abstract:
Generative models for materials have achieved strong performance on periodic bulk crystals, yet their ability to generalize across scale transitions to finite nanostructures remains largely untested. We introduce Crystal-to-Nanoparticle (C2NP), a systematic benchmark for evaluating generative models when moving between infinite crystalline unit cells and finite nanoparticles, where surface effects and size-dependent distortions dominate. C2NP defines two complementary tasks: (i) generating nanoparticles of specified radii from periodic unit cells, testing whether models capture surface truncation and geometric constraints; and (ii) recovering bulk lattice parameters and space-group symmetry from finite particle configurations, assessing whether models can infer underlying crystallographic order despite surface perturbations. Using diverse materials as a structurally consistent testbed, we construct over 170,000 nanoparticle configurations by carving particles from supercells derived from DFT-relaxed crystal unit cells, and introduce size-based splits that separate interpolation from extrapolation regimes. Experiments with state-of-the-art approaches, including diffusion, flow-matching, and variational models, show that even when losses are low, models often fail geometrically under distribution shift, yielding large lattice-recovery errors and near-zero joint accuracy on structure and symmetry. Overall, our results suggest that current methods rely on template memorization rather than scalable physical generalization. C2NP offers a controlled, reproducible framework for diagnosing these failures, with immediate applications to nanoparticle catalyst design, nanostructured hydrides for hydrogen storage, and materials discovery. Dataset and code are available at https://github.com/KurbanIntelligenceLab/C2NP.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19126v1
- Title: How Entanglement Reshapes the Geometry of Quantum Differential Privacy
- Authors: Xi Wang, Parastoo Sadeghi, Guodong Shi
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19126v1  pdf=https://arxiv.org/pdf/2601.19126v1.pdf

Abstract:
Quantum differential privacy provides a rigorous framework for quantifying privacy guarantees in quantum information processing. While classical correlations are typically regarded as adversarial to privacy, the role of their quantum analogue, entanglement, is not well understood. In this work, we investigate how quantum entanglement fundamentally shapes quantum local differential privacy (QLDP). We consider a bipartite quantum system whose input state has a prescribed level of entanglement, characterized by a lower bound on the entanglement entropy. Each subsystem is then processed by a local quantum mechanism and measured using local operations only, ensuring that no additional entanglement is generated during the process. Our main result reveals a sharp phase-transition phenomenon in the relation between entanglement and QLDP: below a mechanism-dependent entropy threshold, the optimal privacy leakage level mirrors that of unentangled inputs; beyond this threshold, the privacy leakage level decreases with the entropy, which strictly improves privacy guarantees and can even turn some non-private mechanisms into private ones. The phase-transition phenomenon gives rise to a nonlinear dependence of the privacy leakage level on the entanglement entropy, even though the underlying quantum mechanisms and measurements are linear. We show that the transition is governed by the intrinsic non-convex geometry of the set of entanglement-constrained quantum states, which we parametrize as a smooth manifold and analyze via Riemannian optimization. Our findings demonstrate that entanglement serves as a genuine privacy-enhancing resource, offering a geometric and operational foundation for designing robust privacy-preserving quantum protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19305v1
- Title: Broadband Heterodyne Microwave Detection using Rydberg Atoms with High Sensitivity
- Authors: Hsuan-Jui Su, Shao-Cheng Fang, Ting-An Li, Chen-Hao Chang, Yu-Chi Chen, Yi-Hsin Chen
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19305v1  pdf=https://arxiv.org/pdf/2601.19305v1.pdf

Abstract:
We present a Rydberg atom-based microwave electric field sensor that achieves extended dynamic range and enhanced sensitivity across a broad bandwidth. By characterizing the Autler-Townes (AT) splitting induced by a single-tone microwave field, we demonstrate a spectroscopic method that simultaneously extracts both the microwave frequency and electric field strength directly from the splitting pattern. We implement dual-tone heterodyne detection, achieving a minimum detectable field strength on the order of uV/cm and a sensitivity in the sub-uV/cm/Hz^1/2 regime, while extending the operational bandwidth up to 3 GHz. Through systematic characterization of frequency and power dependencies, we identify optimal operating conditions to minimize power broadening in the resonant AT regime and maximize sensitivity in the far-off-resonance AC Stark regime. The resulting platform combines high sensitivity, broad bandwidth, and a dynamic range of approximately 90 dB, establishing Rydberg atoms as practical sensors for precision electric field metrology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19517v1
- Title: Analytical solution of the Schrödinger equation with $1/r^3$ and attractive $1/r^2$ potentials: Universal three-body parameter of mixed-dimensional Efimov states
- Authors: Yuki Ohishi, Kazuki Oi, Shimpei Endo
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19517v1  pdf=https://arxiv.org/pdf/2601.19517v1.pdf

Abstract:
We study the Schrödinger equation with $1/r^3$ and attractive $1/r^2$ potentials. Using the quantum defect theory, we obtain analytical solutions for both repulsive and attractive $1/r^3$ interactions. The obtained discrete-scale-invariant energies and wave functions, validated by excellent agreement with numerical results, provide a natural framework for describing the universality of Efimov states in mixed dimension. Specifically, we consider a three-body system consisting of two heavy particles with large dipole moments confined to a quasi-one-dimensional geometry and resonantly interacting with an unconfined light particle. With the Born-Oppenheimer approximation, this system is effectively reduced to the Schrödinger equation with $1/r^3$ and $1/r^2$ potentials, and manifests the Efimov effect. Our analytical solution suggests that, for repulsive dipole interactions, the three-body parameter of the mixed-dimensional Efimov states is universally set by the dipolar length scale, whereas for attractive interactions it explicitly depends on the short-range phase. We also investigate the effects of finite transverse confinement and find that our analytical results are useful for describing the Efimov states composed of two polar molecules and a light atom.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19699v1
- Title: Orthogonally Constrained CASSCF Framework: Newton-Raphson Orbital Optimization and Nuclear Gradients
- Authors: Loris Delafosse, Vincent Robert, Saad Yalouz
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19699v1  pdf=https://arxiv.org/pdf/2601.19699v1.pdf

Abstract:
In a recent work, we introduced the foundations of an orthogonally constrained complete active space self-consistent field (OC-CASSCF) framework that produces state-specific molecular orbitals for mutually orthogonal multiconfigurational electronic states. In the present study, we extend this approach by incorporating a Newton-Raphson orbital-optimization scheme, for which we derive analytical expressions of the orbital gradient and Hessian. Furthermore, we outline a practical route toward the evaluation of analytical nuclear gradients, enabling geometry optimizations within the OC-CASSCF formalism. Benchmark calculations on the three lowest singlet states of LiH and H$_2$O molecules demonstrate a systematic improvement as compared to conventional state-averaged CASSCF, even when using modestly sized active spaces.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2601.19896v1
- Title: Real-Time Iteration Scheme for Dynamical Mean-Field Theory: A Framework for Near-Term Quantum Simulation
- Authors: Chakradhar Rangi, Aadi Singh, Ka-Ming Tam
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19896v1  pdf=https://arxiv.org/pdf/2601.19896v1.pdf

Abstract:
We present a time-domain iteration scheme for solving the Dynamical Mean-Field Theory (DMFT) self-consistent equations using retarded Green's functions in real time. Unlike conventional DMFT approaches that operate in imaginary time or frequency space, our scheme operates directly with real-time quantities. This makes it particularly suitable for near-term quantum computing hardware with limited Hilbert spaces, where real-time propagation can be efficiently implemented via Trotterization or variational quantum algorithms. We map the effective impurity problem to a finite one-dimensional chain with a small number of bath sites, solved via exact diagonalization as a proof-of-concept. The hybridization function is iteratively updated through time-domain fitting until self-consistency. We demonstrate stable convergence across a wide range of interaction strengths for the half-filled Hubbard model on a Bethe lattice, successfully capturing the metal-to-insulator transition. Despite using limited time resolution and a minimal bath discretization, the spectral functions clearly exhibit the emergence of Hubbard bands and the suppression of spectral weight at the Fermi level as interaction strength increases. This overcomes major limitations of two-site DMFT approximations by delivering detailed spectral features while preserving efficiency and compatibility with quantum computing platforms through real-time dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2108.09074v3
- Title: Entanglement Entropy in CFT and Modular Nuclearity
- Authors: Lorenzo Panebianco, Benedikt Wegener
- Categories: quant-ph (primary); quant-ph; math-ph; math.OA
- Links: abs=https://arxiv.org/abs/2108.09074v3  pdf=https://arxiv.org/pdf/2108.09074v3.pdf

Abstract:
In the framework of Algebraic Quantum Field Theory, several operator algebraic notions of entanglement entropy can be associated with any pair of causally disjoint spacetime regions $\mathcal{S}_A$ and $\mathcal{S}_B$ with positive relative distance. Among them, the canonical entanglement entropy is defined as the von Neumann entropy of a canonical intermediate type I factor. In this work, we show that the canonical entanglement entropy of the vacuum state is finite for a broad class of conformal nets including the $U(1)$-current model and the $SU(n)$-loop group models. Since previous studies suggest that this finiteness property is related to nuclearity properties of the system, we show that the mutual information is finite in any local QFT satisfying a modular $p$-nuclearity condition for some $0 < p < 1$. A similar finiteness result is established for another notion of entanglement entropy introduced in this paper. We conclude with remarks for future work in this direction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2204.02867v4
- Title: Optical purification of materials based on atom walking in traveling-wave lights
- Authors: Wenxi Lai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2204.02867v4  pdf=https://arxiv.org/pdf/2204.02867v4.pdf

Abstract:
An optical method for precise purification of chemical elements is introduced in this paper. The materials are supposed to be in the states of gaseous beams, which are coherently coupled to an external traveling light during purification. Before decoherence occurs, atoms periodically move in the light with different speeds that depends on masses and optical transition wave lengths of these atoms. The speed gradient leads to deflections of different atoms in different directions. The model is described by Schrödinger equations with analytical results. This method could be used for some hardly separable atoms and isotopes depending on the condition of atom coherent time. The present work opens a platform for applications of cold atom technology in the purification of atoms and molecules.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2307.08045v2
- Title: Beyond Classical Attention: Quantum Attention for Scalable Computation
- Authors: Xuyang Guo, Zhao Song, Xin Yang, Ruizhe Zhang
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2307.08045v2  pdf=https://arxiv.org/pdf/2307.08045v2.pdf

Abstract:
As large language models (LLMs) demonstrate outstanding performance across various tasks, attention-driven models have profoundly transformed the field of machine learning. Since attention computations account for the primary computational overhead in both model inference and training, efficiently computing attention matrices has become one of the core challenges in accelerating large language models. It is well-known that quantum machines possess computational advantages over classical machines, and the role of quantum computing in LLMs remains largely unexplored. In this work, we focus on leveraging the Grover search algorithm to efficiently compute a sparse attention matrix. Through comparisons with classical algorithms, we demonstrate that our method achieves quantum acceleration in polynomial time. Additionally, we observe that the generated quantum attention matrices naturally exhibit low-rank structures, providing further theoretical support for efficient modeling. Moreover, within the specific context of attention matrix computation, we conduct a systematic and detailed analysis of the error and time complexity of the proposed algorithm.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2402.06556v2
- Title: Parameter estimation for quantum jump unraveling
- Authors: Marco Radaelli, Joseph A. Smiga, Gabriel T. Landi, Felix C. Binder
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2402.06556v2  pdf=https://arxiv.org/pdf/2402.06556v2.pdf

Abstract:
We consider the estimation of parameters encoded in the measurement record of a continuously monitored quantum system in the jump unraveling, corresponding to a single-shot scenario, where information is continuously gathered. Here, it is generally difficult to assess the precision of the estimation procedure via the Fisher Information due to intricate temporal correlations and memory effects. In this paper we provide a full set of solutions to this problem. First, for multi-channel renewal processes we relate the Fisher Information to an underlying Markov chain and derive a easily computable expression for it. For non-renewal processes, we introduce a new algorithm that combines two methods: the monitoring operator method for metrology and the Gillespie algorithm which allows for efficient sampling of a stochastic form of the Fisher Information along individual quantum trajectories. We show that this stochastic Fisher Information satisfies useful properties related to estimation on a single run. Finally, we consider the case where some information is lost in data compression/post-selection and provide tools for computing the Fisher Information in this case. All scenarios are illustrated with instructive examples from quantum optics and condensed matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2404.06438v5
- Title: Non-Gaussian state teleportation with a nonlinear feedforward
- Authors: Vojtěch Kala, Mattia Walschaers, Radim Filip, Petr Marek
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2404.06438v5  pdf=https://arxiv.org/pdf/2404.06438v5.pdf

Abstract:
Measurement-induced quantum computation with continuous-variable cluster states utilizes teleportation to transmit and alter quantum states via measurement-and-feedforward control. One of the key challenges of this approach is the deterioration of quantum states caused by the noise added due to imperfect entanglement of the cluster. We analyze the propagation of a quantum non-Gaussian state with nonlinear squeezing through a small cluster state. We show that a nonlinear feedforward in the deterministic teleportation protocol reduces the added noise and improves the nonlinear squeezing transferred. In a probabilistic regime, the improvement can be manifested even with current experimental resources. Better processing of non-Gaussian states can bring us closer to the necessary interplay between cluster states and non-Gaussianity required by quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2410.17992v2
- Title: Iteratively decoded magic state distillation
- Authors: Kwok Ho Wan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2410.17992v2  pdf=https://arxiv.org/pdf/2410.17992v2.pdf

Abstract:
We present numerical simulation results for the 7-to-1 and 15-to-1 state distillation circuits, constructed using transversal CNOTs acting on multiple surface code patches. The distillation circuits are decoded iteratively using the method outlined in [arXiv:2407.20976]. We show that, with a re-configurable qubit architecture, we can perform fast magic state distillation in $\sim\mathcal{O}(1)$ code cycles. We confirm that both circuits suppress an injected input error rate $p$ to $\mathcal{O}(p^3)$ in the presence of additional circuit-level noise. We also outline how ZX-calculus and Pauli webs can be used to benchmark stabiliser proxies for these distillation circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2502.09681v2
- Title: Graph-Theoretic Analysis of $n$-Replica Time Evolution in the Brownian Gaussian Unitary Ensemble
- Authors: Tingfei Li, Jianghui Yu
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2502.09681v2  pdf=https://arxiv.org/pdf/2502.09681v2.pdf

Abstract:
In this paper, we investigate the $n$-replica time evolution operator $\mathcal{U}_n(t)\equiv e^{\mathcal{L}_nt} $ for the Brownian Gaussian Unitary Ensemble (BGUE) using a graph-theoretic approach. We examine the moments of the generating operator $\mathcal{L}_n$, which governs the Euclidean time evolution within an auxiliary $D^{2n}$-dimensional Hilbert space, where $D$ represents the dimension of the Hilbert space for the original system. Explicit representations for the cases of $n = 2$ and $n = 3$ are derived, emphasizing the role of graph categorization in simplifying calculations. Furthermore, we present a general approach to streamline the calculation of time evolution for arbitrary $n$, supported by a detailed example of $n = 4$. Our results demonstrate that the $n$-replica framework not only facilitates the evaluation of various observables but also provides valuable insights into the relationship between Brownian disordered systems and quantum information theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2502.09725v2
- Title: Non-stabilizerness of Neural Quantum States
- Authors: Alessandro Sinibaldi, Antonio Francesco Mello, Mario Collura, Giuseppe Carleo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2502.09725v2  pdf=https://arxiv.org/pdf/2502.09725v2.pdf

Abstract:
We introduce a methodology to estimate non-stabilizerness or "magic", a key resource for quantum complexity, with Neural Quantum States (NQS). Our framework relies on two schemes based on Monte Carlo sampling to quantify non-stabilizerness via Stabilizer Rényi Entropy (SRE) in arbitrary variational wave functions. When combined with NQS, this approach is effective for systems with strong correlations and in dimensions larger than one, unlike Tensor Network methods. Firstly, we study the magic content in an ensemble of random NQS, demonstrating that neural network parametrizations of the wave function capture finite non-stabilizerness besides large entanglement. Secondly, we investigate the non-stabilizerness in the ground state of the $J_1$-$J_2$ Heisenberg model. In 1D, we find that the SRE vanishes at the Majumdar-Ghosh point $J_2 = J_1/2$, consistent with a stabilizer ground state. In 2D, a dip in the SRE is observed near maximum frustration around $J_2/J_1 \approx 0.6$, suggesting a Valence Bond Solid between the two antiferromagnetic phases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2503.05884v2
- Title: Reassessing the boundary between classical and nonclassical for individual quantum processes
- Authors: Yujie Zhang, David Schmid, Yìlè Yīng, Robert W. Spekkens
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.05884v2  pdf=https://arxiv.org/pdf/2503.05884v2.pdf

Abstract:
There is a received wisdom about where to draw the boundary between classical and nonclassical for various types of quantum processes. For multipartite states, it is the divide between separable and entangled; for channels, the divide between entanglement-breaking and not; for sets of measurements, the divide between compatible and incompatible; for assemblages, the divide between steerable and unsteerable. However, these choices have not been motivated by any unified notion of what it means to be classically explainable. One well-motivated notion of classical explainability is the one based on generalized noncontextuality: a set of circuits is classically explainable if a generalized-noncontextual ontological model can realize the statistics they generate. In this work, we show that this notion can be leveraged to define a classical-nonclassical divide for individual quantum processes of arbitrary type. We begin the task of characterizing where the classical-nonclassical divide lies according to this proposal for a variety of different types of processes. In particular, we show that all of the following are judged to be nonclassical: every entangled state, every set of incompatible measurements, every non-entanglement-breaking channel, and every steerable assemblage. Our proposal differs from the received wisdom, however, insofar as it also judges certain subsets of the complementary classes to be nonclassical, including certain separable states, compatible sets of measurements, entanglement-breaking channels, and unsteerable assemblages. Finally, we prove structure theorems characterizing the classical-nonclassical divide based on whether a process admits of a specific type of frame representation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2503.23610v4
- Title: Powering Quantum Computation with Quantum Batteries
- Authors: Yaniv Kurman, Kieran Hymas, Arkady Fedorov, William J. Munro, James Quach
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.23610v4  pdf=https://arxiv.org/pdf/2503.23610v4.pdf

Abstract:
Executing quantum logic in cryogenic quantum computers requires a continuous energy supply from room-temperature control electronics. This dependence on external energy sources creates scalability limitations due to control channel density and heat dissipation. Here, we propose quantum batteries (QBs) as intrinsic quantum energy sources for quantum computation, enabling the thermodynamic limit of zero dissipation for unitary gates. Unlike classical power sources, QBs maintain quantum coherence with their load - a property that, while theoretically studied, remains unexploited in practical quantum technologies. We demonstrate that initializing a bosonic QB in a Fock state can supply the energy required for arbitrary unitary gates regardless of the circuit's depth, via the recycling of pre-charged energy. Crucially, allowing QB-qubit entanglement during computation lowers the QB initial energy requirements below established energy-fidelity bounds. This scheme facilitates a universal gate set controlled by a single parameter per qubit, its resonant frequency. The relative detuning of each qubit from the QB resonant frequency gives rise to qualitatively two gate types, off-resonance and around-resonance. The former facilitates dispersive gates which allow multi-qubit parity probing while the latter enables energy exchange between the QB and the qubits, driving both population transfer and entanglement generation. This mechanism utilizes the all-to-all connectivity of the shared resonator architecture to go beyond the standard single- and two-qubit native gates of current platforms with multi-qubit gate timescales of few pi/g, where g is the qubit-resonator coupling. The resultant speed-up includes also superextensive gates between symmetric Dicke states, characteristic of QB systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2504.00887v2
- Title: Enhanced sensitivity in microscale high-field NMR via nuclear-spin locking with NV centers
- Authors: Oliver T. Whaites, Jaime García Oliván, Jorge Casanova
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.00887v2  pdf=https://arxiv.org/pdf/2504.00887v2.pdf

Abstract:
Solid state defects such as nitrogen vacancy (NV) centers in diamond have been utilized for NMR sensing at ambient temperatures for samples at the nano-scale and up to the micro-scale. Similar to standard NMR, NV-sensitivities can be increased using tesla-valued magnetic fields to boost nuclear thermal polarization, while structural parameters, such as chemical shifts, are also enhanced. However, with standard microwave (MW) based sensing techniques, NV centers struggle to track fast megahertz Larmor frequencies encountered in high-field scenarios. Previous protocols have addressed this by mapping target NMR parameters to the signal amplitude rather than the frequency, using a mediating RF field. Although successful, protocol sensitivities are limited by the coherence time ($T_2^*$) of the NMR signal owing to the presence of stages where the sample magnetization freely evolves. In this work, we propose extending this coherence time, and consequently improving sensitivity, via amplitude encoding with weak nuclear spin locking instead of free evolution, thereby taking advantage of the longer sample coherence times ($T_{1ρ}$). We demonstrate this can enhance protocol sensitivities by $\gtrsim 4$ times.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2504.06217v2
- Title: Chernoff Information Bottleneck for Covert Quantum Target Sensing
- Authors: Giuseppe Ortolano, Ivano Ruo-Berchera, Leonardo Banchi
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2504.06217v2  pdf=https://arxiv.org/pdf/2504.06217v2.pdf

Abstract:
The paradigm of quantum metrology and sensing aims to identify a quantum advantage in precision at a fixed energy of the probe state. However, in practice, employing high-energy classical probes is often simpler than leveraging the quantum regime. This is not the case of covert sensing scenarios, where detection must be performed while avoiding to be discovered by an adversary, because increasing energy unduly facilitates the adversary. In this paper, we introduce a general framework to assess the quantum advantage in covert situations based on extending the information bottleneck principle to decision problems via the Chernoff information. We demonstrate how entangled photonic probes paired with photon counting significantly outperform classical coherent transmitters in covert detection and ranging, often representing the only option for secrecy. Thus, our work highlights the great potential of integrating quantum sensing into LiDAR and Radar systems to enhance covert performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2505.00386v3
- Title: Exact treatment of the memory kernel under time-dependent system-environment coupling via a train of delta distributions
- Authors: Yuta Uenaga, Kensuke Gallock-Yoshimura, Takano Taira
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2505.00386v3  pdf=https://arxiv.org/pdf/2505.00386v3.pdf

Abstract:
Memory effects in a quantum system coupled to an environment are one of the central features in the theory of open quantum systems. The dynamics of such quantum systems are typically governed by an equation of motion with a time-convolution integral of the memory kernel. However, solving such integro-differential equations is challenging, especially when the memory kernel is nonstationary (not time-translation invariant). In this paper, we analytically and nonperturbatively solve such integro-differential equations with a nonstationary memory kernel by employing a train of Dirac-delta switchings. We then apply this method to the damped Jaynes-Cummings model and the damped harmonic oscillator model to demonstrate that (i) our solution asymptotes to the well-known exact solution in the continuum limit, and that (ii) our method also enables us to visualize the memory effect in the environment.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2505.01614v3
- Title: Quantum-Assisted Vehicle Routing: Realizing QAOA-based Approach on Gate-Based Quantum Computer
- Authors: Talha Azfar, Osama Muhammad Raisuddin, Ruimin Ke, Jose Holguin-Veras
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2505.01614v3  pdf=https://arxiv.org/pdf/2505.01614v3.pdf

Abstract:
The Vehicle Routing Problem (VRP) is a fundamental combinatorial optimization challenge with broad applications in logistics and transportation. In this work, we present a quantum-assisted framework that integrates the Quantum Approximate Optimization Algorithm (QAOA) with a link-based formulation of VRP. Our approach encodes flow conservation and subtour elimination directly into the cost Hamiltonian, preserving graph structure while minimizing resource requirements for practical hardware implementation. We design and implement the full pipeline on a gate-based quantum computer, including problem formulation, encoding, circuit synthesis, and execution on IBM Quantum System One. Experimental results on small VRP instances highlight the effects of penalty scaling, coefficient normalization, and circuit depth on solution feasibility under hardware noise. While scalability remains constrained by circuit complexity and decoherence, the study demonstrates a practical pathway for implementing VRP on quantum hardware and identifies methodological directions for advancing near-term quantum optimization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2505.07798v3
- Title: PT symmetry and the square well potential: Antilinear symmetry rather than Hermiticity in scattering processes
- Authors: Philip D. Mannheim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.07798v3  pdf=https://arxiv.org/pdf/2505.07798v3.pdf

Abstract:
While a Hamiltonian with a real potential acts as a Hermitian operator when it acts on bound states, it produces resonances with complex energies in a scattering experiment. Scattering states are not square integrable, being instead delta function normalized. This lack of square integrability breaks the connection between Hermiticity and real eigenvalues, to thus allow for real bound state sector eigenvalues and complex scattering sector eigenvalues. When written as contour integrals delta functions take support in the complex plane, with the scattering amplitude being able to take support in the complex plane too. However, the scattering amplitude is CPT symmetric (or PT symmetric if C is conserved), regardless of whether or not states are square integrable. For resonance scattering this antilinear symmetry requires the presence of a complex conjugate pair of energies, one to describe the excitation of the resonance and the other to describe its decay, with it being their interplay that enforces probability conservation. Each complex pair of energy eigenvalues corresponds to only one observable resonance not two, to thus modify the standard pure decaying complex energy pole discussion of resonances. We show that the non-relativistic real potential square-well problem possesses PT symmetry in both the bound and scattering sectors, with there being complex conjugate pairs of energy eigenvalues in its scattering amplitude. For those values of the potential for which bound states lie right at the top of the well the scattering amplitude threshold branch point is an exceptional point, a characteristic of systems with antilinear symmetry at which there are more independent solutions to the Schrödinger equation than eigenstates of the Hamiltonian. The square well thus provides an explicit realization of how antilinearity is more general than Hermiticity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2505.08756v3
- Title: Designing open quantum systems for enabling quantum enhanced sensing through classical measurements
- Authors: Robert Mattes, Albert Cabot, Federico Carollo, Igor Lesanovsky
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.08756v3  pdf=https://arxiv.org/pdf/2505.08756v3.pdf

Abstract:
Quantum systems in nonequilibrium conditions, where coherent many-body interactions compete with dissipative effects, can feature rich phase diagrams and emergent critical behavior. Associated collective effects, together with the continuous observation of quanta dissipated into the environment -- typically photons -- allow to achieve quantum enhanced parameter estimation. However, protocols for tapping this enhancement typically involve intricate measurements on the combined system-environment state. Here we show that many-body quantum enhancement can in fact be obtained through classical measurements, such as photon counting and homodyne detection. We illustrate this in detail for a class of open spin-boson models which can be realized in trapped-ion or cavity QED setups. Our findings highlight a route towards the design of systems that enable a practical implementation of quantum enhanced metrology through continuous classical measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2505.24502v5
- Title: From top quarks to enhanced quantum key distribution: A Framework for Optimal Predictability of Quantum Observables
- Authors: Dennis I. Martínez-Moreno, Miguel Castillo-Celeita, Diego G. Bussandri
- Categories: quant-ph (primary); quant-ph; hep-ex; hep-ph; hep-th
- Links: abs=https://arxiv.org/abs/2505.24502v5  pdf=https://arxiv.org/pdf/2505.24502v5.pdf

Abstract:
Predicting the outcomes of quantum measurements is a cornerstone of quantum information theory and a key resource for quantum technologies. Here, we introduce a comprehensive framework for quantifying the predictability of measurements on a bipartite quantum system using error measures inherited from statistical learning theory: the Bayes risk and inference variance. We derive analytical expressions for the optimal measurement that minimizes the prediction error for any arbitrary observable and any two-qubit state. We establish a direct, quantitative link between the ability to surpass the fundamental limit of local unpredictability and the presence of Einstein-Podolsky-Rosen steering. Additionally, by optimizing measurement choices according to the minimal Bayes risk, we propose a modified entanglement-based quantum key distribution protocol achieving higher secure key rates than the standard BB84 protocol, demonstrating enhanced resilience to noise. We apply our framework in two scenarios: perfect Bell states affected by local amplitude-damping noises, and top-antitop quark pairs produced in high-energy colliders. Our work offers a novel perspective on quantum correlations, connecting statistical inference, fundamental quantum phenomena, and cryptographic applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2506.00292v2
- Title: Minimising the number of edges in LC-equivalent graph states
- Authors: Hemant Sharma, Kenneth Goodenough, Johannes Borregaard, Filip Rozpędek, Jonas Helsen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.00292v2  pdf=https://arxiv.org/pdf/2506.00292v2.pdf

Abstract:
Graph states are a powerful class of entangled states with numerous applications in quantum communication and quantum computation. Local Clifford (LC) operations that map one graph state to another can alter the structure of the corresponding graphs, including changing the number of edges. Here, we tackle the associated edge-minimisation problem: finding graphs with the minimum number of edges in the LC-equivalence class of a given graph. Such graphs are called minimum edge representatives (MER) and are crucial for minimising the resources required to create a graph state. We leverage Bouchet's algebraic formulation of LC-equivalence to encode the edge-minimisation problem as an integer linear program (EDM-ILP). We further propose a simulated annealing (EDM-SA) approach guided by the local clustering coefficient for edge minimisation. We identify new MERs for graph states with up to 16 qubits by combining EDM-SA and EDM-ILP. We extend the ILP to weighted-edge minimisation, where each edge has an associated weight, and prove that this problem is NP-complete. Finally, we employ our tools to minimise the resources required to create all-photonic generalised repeater graph states using fusion operations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2506.09298v4
- Title: Effective criteria for entanglement witnesses in small dimensions
- Authors: Łukasz Grzelka, Łukasz Skowronek, Karol Życzkowski
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2506.09298v4  pdf=https://arxiv.org/pdf/2506.09298v4.pdf

Abstract:
We present an effective set of necessary and sufficient criteria for block-positivity of matrices of order $4$ over $\mathbb{C}$. The approach is based on Sturm sequences and quartic polynomial positivity conditions presented in recent literature. The procedure allows us to test whether a given $4\times 4$ complex matrix corresponds to an entanglement witness, and it is exact when the matrix coefficients belong to the rationals, extended by $\mathrm{i}$. The method can be generalized to $\mathcal{H}_2\otimes\mathcal{H}_d$ systems for $d>2$ to provide necessary but not sufficient criterion for block-positivity. We also outline an alternative approach to the problem relying on Gröbner bases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2506.09763v3
- Title: Achieving the Quantum Fisher Information Bound in Pseudo-Hermitian Sensors
- Authors: Ievgen I. Arkhipov, Franco Nori, Şahin K. Özdemir
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.09763v3  pdf=https://arxiv.org/pdf/2506.09763v3.pdf

Abstract:
Non-Hermitian systems have attracted considerable interest over the last few decades due to their unique spectral and dynamical properties not encountered in Hermitian counterparts. An intensely debated question is whether non-Hermitian systems, described by pseudo-Hermitian Hamiltonians with real spectra, can offer enhanced sensitivity for parameter estimation when they are operated at or close to exceptional points. However, much of the current analysis and conclusions are based on mathematical formalism developed for Hermitian quantum systems, which is questionable when applied to pseudo-Hermitian Hamiltonians, whose Hilbert space metric is intrinsically parameter dependent. Here, we develop a covariant formulation of quantum Fisher information (QFI) defined on the deformed Hilbert space of pseudo-Hermitian Hamiltonians. This covariant framework ensures the preservation of the state norm and enables a consistent treatment of parameter sensitivity. We further show that the covariant QFI of pseudo-Hermitian systems is dual to the ordinary QFI of corresponding Hermitian systems. Importantly, this correspondence naturally imposes an upper bound on the covariant QFI and allows one to identify optimal projections which saturate the corresponding classical Fisher information to this ultimate limit. The developed framework also enables to set the criteria under which pseudo-Hermitian sensors can exhibit an advantage over their Hermitian counterparts of the same dimensionality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2506.22430v2
- Title: General many-body entanglement swapping protocol: opportunities for distributed quantum computing
- Authors: Santeri Huhtanen, Yousef Mafi, Ali G. Moghaddam, Teemu Ojanen
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2506.22430v2  pdf=https://arxiv.org/pdf/2506.22430v2.pdf

Abstract:
Sharing entangled pairs between non-signaling parties via entanglement swapping constitutes a striking demonstration of the nonlocality of quantum mechanics and a crucial building block for future quantum technologies. In this work, we generalize pair-swapping methods by introducing a many-body entanglement swapping protocol, which allows two non-signaling parties to share general many-body states along an arbitrary partitioning. The shared many-body state retains exactly the same Schmidt vectors as the target state and exhibits typically high fidelity, which approaches unity as the variance of the Schmidt coefficients vanishes. Moreover, we demonstrate how the three-party protocol can be generalized to many-body swapping networks, enabling a general many-body state sharing with unit fidelity via arbitrary number of intermediate nodes. This is achieved by replacing all but one of the unitary operations with those corresponding to the same Schmidt states but with a flattened spectrum, which also completely eliminates the need for postselection. We provide a proof of concept of the three-party protocol on real quantum hardware and discuss how it enables new functionalities, such as fault-tolerant entanglement swapping and new strategies for distributed quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2507.07092v2
- Title: Non-Gaussian Phase Transition and Cascade of Instabilities in the Dissipative Quantum Rabi Model
- Authors: Mingyu Kang, Yikang Zhang, Kenneth R. Brown, Thomas Barthel
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2507.07092v2  pdf=https://arxiv.org/pdf/2507.07092v2.pdf

Abstract:
The open quantum Rabi model describes a two-level system coupled to a harmonic oscillator. A Gaussian phase transition for the nonequilibrium steady states has been predicted when the bosonic mode is soft and subject to damping. We show that oscillator dephasing is a relevant perturbation, which leads to a non-Gaussian phase transition and an intriguing cascade of instabilities for $k$-th order bosonic operators, as well as a jump in the steady-state qubit polarization. For the soft-mode limit, the equations of motion form a closed hierarchy and spectral properties can be efficiently studied. To this purpose, we establish a fruitful connection to non-Hermitian Hamiltonians. The results for the phase diagram, stability boundaries, and relevant observables are based on mean-field analysis, exact diagonalization, perturbation theory, and Keldysh field theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2507.08936v2
- Title: Long-ranged gates in quantum computation architectures with limited connectivity
- Authors: Wolfgang Dür
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.08936v2  pdf=https://arxiv.org/pdf/2507.08936v2.pdf

Abstract:
We propose a quantum computation architecture based on geometries with nearest-neighbor interactions, including e.g. planar structures. We show how to efficiently split the role of qubits into data and entanglement-generation qubits. Multipartite entangled states, e.g. 2D cluster states, are generated among the latter, and flexibly transformed via mid-circuit measurements to multiple, long-ranged Bell states, which are used to perform several two-qubit gates in parallel on data qubits. We introduce planar architectures with $n$ data and $n$ auxiliary qubits that allow one to perform $O(\sqrt n)$ long-ranged two-qubit gates simultaneously, with only one round of nearest neighbor gates and one round of mid-circuit measurements. We also show that our approach is applicable in existing superconducting quantum computation architectures, with only a constant overhead.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2507.20045v2
- Title: Cornell Interaction in the Two-body Pauli-Schrödinger-type Equation Framework: The Symplectic Quantum Mechanics Formalism
- Authors: R. R. Luz, R. A. S. Paiva, G. X. A. Petronilo, A. E. Santana, T. M. Rocha Filho, R. G. G. Amorim
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2507.20045v2  pdf=https://arxiv.org/pdf/2507.20045v2.pdf

Abstract:
We investigate the quantum behavior of a quark-antiquark bound system under the influence of a magnetic field within the symplectic formulation of quantum mechanics. Employing a perturbative approach, we obtain the ground and first excited states of the system described by the Cornell potential, which incorporates both confining and non-confining interactions. After performing a Bohlin mapping in phase space, we solve the time-independent symplectic Pauli-Schrödinger-type equation and determine the corresponding Wigner function. Special attention is given to the observation of the confinement of the quark-antiquark, that is revealed in the phase space structure. Due to the presence of spin in the Hamiltonian, the results reveal that the magnetic field enhances the non-classicality of the Wigner function, signaling stronger quantum interference and a departure from classical behavior. The experimental mass spectra is used to estimate the intensity of the external field, leading to a value that is in order of the transient magnetic field measured in non-central heavy-ion collisions at RHIC and LHC.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2507.21217v2
- Title: Robust qubit interactions mediated by photonic topological edge states
- Authors: Boris Gurevich, Weihua Xie, Mohsen Yarmohammadi, Michael H. Kolodrubetz
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2507.21217v2  pdf=https://arxiv.org/pdf/2507.21217v2.pdf

Abstract:
We investigate the coupling of two spatially separated qubits via topologically protected edge states in a two-dimensional Hofstadter lattice. In this hybrid platform, the qubits are coupled to distinct edge sites of the lattice, enabling long-range interactions mediated by topological edge modes. We solve the full system Hamiltonian and analyze the resulting eigenstate structure to uncover the conditions under which coherent qubit interactions emerge. Our analysis reveals that the effective coupling is highly sensitive to the qubit placement, energy detuning, and the topological character of the edge spectrum. We obtain an analytical solution that goes beyond the perturbative regime, capturing the full interplay between the qubits and edge modes. These results provide a foundation for exploring information transport and many-body effects in engineered quantum systems where interactions are mediated by topological edge modes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2507.21289v2
- Title: Construction and Rigorous Analysis of Quantum-Like States
- Authors: Ethan Dickey, Abhijeet Vyas, Sabre Kais
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.21289v2  pdf=https://arxiv.org/pdf/2507.21289v2.pdf

Abstract:
Extending upon the observations of the emergence of quantum-like states from classical complex synchronized networks, this work adds mathematical rigor to the analysis of single Quantum-Like (QL) bits constructed by eigenvectors of the adjacency matrices of such networks. First, we rigorously show that symmetric construction of such networks (regular undirected/symmetric bipartite graph $G_C$ connecting two regular undirected subgraphs $G_A,\,G_B$) leads to an equal superposition of the $|+\rangle, |-\rangle$ Hadamard states (with basis $|0\rangle,\,|1\rangle$ set from eigenvectors of the subgraphs), and provide an analysis of sufficient conditions on the network for construction of such states. Second, we prove two methods to construct any arbitrary single qubit state $|ψ\rangle = a|0\rangle + b|1\rangle,\, |a|^2+|b|^2=1$ and provide a switching lemma for the boundaries of both methods. The first method of construction is by detuning the regularities of the two subgraphs and the second is by asymmetrically constructing the bipartite connection matrix $C$ by allowing it to be directed, and then detuning those regularities. While the intuition is derived from the motivation of using complex synchronized networks for quantum information storage and computations, the proofs for constructing eigenvectors that interact in a quantum-like fashion only require the structure of the graph embedded in the adjacency matrix. Practically, this means that synchronization is not important to creating quantum-like bits, only that the edge weights are generally unit or close to unit and that the subgraphs are regular. As such, the results on combinations of random k-regular graphs (precisely Erdős-Rényi graphs) may be independently interesting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2508.02578v2
- Title: Quantum chemistry with provable convergence via randomized sample-based Krylov quantum diagonalization
- Authors: Samuele Piccinelli, Alberto Baiardi, Stefano Barison, Max Rossmannek, Almudena Carrera Vazquez, Francesco Tacchino, Stefano Mensa, Edoardo Altamura, et al.
- Categories: quant-ph (primary); quant-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2508.02578v2  pdf=https://arxiv.org/pdf/2508.02578v2.pdf

Abstract:
Quantum algorithms based on classical processing of individual samples have recently emerged as the most effective and robust methods to approximate ground-state wave functions of many-body quantum systems on pre-fault-tolerant and early-fault-tolerant quantum devices. In these algorithms, the quantum computer acts as a sampling engine that generates the subspace in which the Hamiltonian is classically diagonalized. The recently proposed Sample-based Krylov Quantum Diagonalization (SKQD), uses quantum Krylov states as circuits from which samples are collected. Convergence guarantees can be derived for SKQD under similar assumptions to those of quantum phase estimation, provided that the ground-state wave function is well approximated by a polynomial subset of the full Hilbert space. However, implementations of SKQD for complex many-body Hamiltonians, such as quantum chemistry ones, are limited by the depths of time-evolution circuits needed to generate Krylov vectors. In this work, we introduce a method that combines SKQD with a qDRIFT randomized compilation of the Hamiltonian propagator. The resulting algorithm, termed SqDRIFT, enables quantum chemistry experiments on quantum processors, while preserving the convergence guarantees similar to the phase estimation algorithm. We demonstrate its viability by applying SqDRIFT to calculate the electronic ground-state energy of several polycyclic aromatic hydrocarbons, up to system sizes beyond the reach of exact diagonalization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2508.03506v3
- Title: Conditional squeezing induced by a two-level system: a first-principles approach to QND readout
- Authors: Phoenix M. M. Paing
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.03506v3  pdf=https://arxiv.org/pdf/2508.03506v3.pdf

Abstract:
We present a systematic Magnus expansion treatment of light-matter interaction beyond the Rotating Wave Approximation. We show that at the second order of Magnus series, the time-evolution operator acquires both energy-shifts and squeezing contributions. In addition to the energy shifts caused by vacuum and photon numbers, the second-order evolution operator contains a term that induces conditional squeezing of the field mode depending on the state of the atom. Such a term suggests a natural mechanism for phase-sensitive, quantum non-demolishing type measurements of squeezed light via homodyne detection. We also show that the second-order Magnus operator in a close SU(1,1) algebra, ensuring the exponentiation of the Magnus series yields a well-defined unitary evolution. By deriving squeezing directly from the Jaynes-Cummings Hamiltonian, our results clarify how energy shifts and $\hatσ$-dependent squeezing arise from an SU(1,1) structure, with direct implications for phase-sensitive and quantum nondemolition measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2508.10200v2
- Title: Time-resolved certification of frequency-bin entanglement over multi-mode channels
- Authors: Stéphane Vinet, Marco Clementi, Marcello Bacchi, Yujie Zhang, Massimo Giacomin, Luke Neal, Paolo Villoresi, Matteo Galli, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.10200v2  pdf=https://arxiv.org/pdf/2508.10200v2.pdf

Abstract:
Frequency-bin entangled photons can be efficiently produced on-chip which offers a scalable, robust and low-footprint platform for quantum communication, particularly well-suited for resource-constrained settings such as mobile or satellite-based systems. However, analyzing such entangled states typically requires active and lossy components, limiting scalability and multi-mode compatibility. We demonstrate a novel technique for processing frequency-encoded photons using linear interferometry and time-resolved detection. Our approach is fully passive and compatible with spatially multi-mode light, making it suitable for free-space and satellite to ground applications. As a proof-of-concept, we utilize frequency-bin entangled photons generated from a high-brightness multi-resonator source integrated on-chip to show the ability to perform arbitrary projective measurements over both single- and multi-mode channels. We report the first measurement of the joint temporal intensity between frequency-bin entangled photons, which allows us to certify entanglement by violating the Clauser-Horne-Shimony-Holt (CHSH) inequality, with a measured value of $|S|=2.32\pm0.05$ over multi-mode fiber. By combining time-resolved detection with energy-correlation measurements, we perform full quantum state tomography, yielding a state fidelity of up to $91\%$. We further assess our ability to produce non-classical states via a violation of time-energy entropic uncertainty relations and investigate the feasibility of a quantum key distribution protocol. Our work establishes a resource-efficient and scalable approach toward the deployment of robust frequency-bin entanglement over free-space and satellite-based links.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2508.10968v2
- Title: High-contrast double Bragg interferometry via detuning control
- Authors: Rui Li, Víctor José Martínez-Lahuerta, Naceur Gaaloul, Klemens Hammerer
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2508.10968v2  pdf=https://arxiv.org/pdf/2508.10968v2.pdf

Abstract:
We propose high-contrast Mach-Zehnder atom interferometers based on double Bragg diffraction (DBD) operating under external acceleration. To mitigate differential Doppler shifts and experimental imperfections, we introduce a tri-frequency laser scheme with dynamic detuning control. We evaluate four detuning-control strategies-conventional DBD, constant detuning, linear detuning sweep (DS-DBD), and a hybrid protocol combining detuning sweep with optimal control theory (OCT)-using exact numerical simulations and a five-level S-matrix model. The OCT strategy provides the highest robustness, maintaining contrast above 95\% under realistic conditions, while the DS-DBD strategy sustains contrast above 90\% for well-collimated Bose-Einstein condensates. These results offer practical pathways to high-contrast, large-momentum-transfer DBD-based interferometers for precision quantum sensing and fundamental physics tests.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2510.04766v3
- Title: Symmetric $C_Z$ gate for ultracold neutral atoms based on counterdiabatic driving at Rydberg excitation
- Authors: I. I. Beterov, K. V. Kozenko, P. Xu, I. I. Ryabtsev
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.04766v3  pdf=https://arxiv.org/pdf/2510.04766v3.pdf

Abstract:
We designed a scheme for a neutral atom Rydberg blockade $C_Z$ gate based on the double sequence of adiabatic pulses applied symmetrically to both atoms and using counterdiabatic driving for Rydberg excitation. This provides a substantial reduction in the quantum gate operation time compared to previously proposed double adiabatic schemes, and makes our scheme competitive with modern time-optimal protocols for high-fidelity entangling gates with neutral atoms. Our approach creates a bridge between fully adiabatic and time-optimal gate schemes. The use of adiabatic passage reduces the sensitivity of gate fidelity to variations in laser intensity, while counterdiabatic driving provides short gate times. The intensity and phase profiles of the laser pulse acting on the atoms are described analytically depending only on the gate duration. We demonstrated the applicability of this scheme for single-photon and two-photon schemes of Rydberg excitation in rubidium and cesium atoms, and, for the first time, discussed the implementation of a $C_Z$ gate using three-photon excitation of rubidium atoms. In contrast to many modern $C_Z$ gate protocols, our scheme does not generate intrinsic single-qubit phase shifts, although they still appear in two-photon configuration. We also designed a numerically optimized amplitude-robust gate with an analytically defined phase profile of the laser pulse and compared its performance with the counteradiabatic gate scheme.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2510.26754v3
- Title: Quantum Enhanced Dark-Matter Search with Entangled Fock States in High-Quality Cavities
- Authors: Benjamin Freiman, Xinyuan You, Andy C. Y. Li, Raphael Cervantes, Taeyoon Kim, Anna Grasselino, Roni Harnik, Yao Lu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.26754v3  pdf=https://arxiv.org/pdf/2510.26754v3.pdf

Abstract:
We present a quantum-enhanced protocol for detecting wave-like dark matter using an array of $N$ entangled superconducting cavities initialized in an $m$-photon Fock state. By distributing and recollecting the quantum state with an entanglement-distribution operation, the scan rate scales as $N^2(m+1)$ while thermal excitation is the dominant background, significantly outperforming classical single-cavity methods under matched conditions. We evaluate the robustness of our scheme against additional noise sources, including decoherence and beamsplitter infidelity, through theoretical analysis and numerical simulations. In practice, the key requirements, namely high-Q superconducting radio-frequency cavities that support long integration times, high-fidelity microwave beamsplitters, and universal cavity control, are already available on current experimental platforms, making the protocol experimentally feasible.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2510.27310v2
- Title: Manipulating Excitation Dynamics in Structured Waveguide Quantum Electrodynamics
- Authors: I Gusti Ngurah Yudi Handayana, Ya-Tang Yu, Wei-Hsuan Chung, H. H. Jen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.27310v2  pdf=https://arxiv.org/pdf/2510.27310v2.pdf

Abstract:
Waveguide quantum electrodynamics (wQED) has become a central platform for studying collective light-matter interactions in low-dimensional photonic environments. While conventional wQED systems rely on uniform chirality or reciprocal emitter-waveguide coupling, we propose a structured wQED framework, where the coupling directionality of each emitter can be engineered locally to control excitation transport in an atom-nanophotonic interface. For different combinations of patterned coupling directionalities of the emitters, we identify four representative configurations that exhibit distinct dynamical behaviors: centering, wave-like, leap-frog, and dispersion excitations. Spectral analysis of the effective non-Hermitian Hamiltonian reveals that these dynamics originate from interferences among subradiant eigenmodes. Variance analysis further quantifies the spreading of excitation as functions of interatomic spacing and global chirality, showing tunable localization-delocalization transitions. Including nonguided losses, we find that the transport characteristics remain robust for realistic coupling efficiencies (beta >= 0.99). These results establish structured wQED as a practical route to manipulate excitation localization, coherence, and transport through programmable directionality patterns, paving the way for controllable subradiant transport and chiral quantum information routing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2511.04243v2
- Title: Twirlator: A Pipeline for Analyzing Subgroup Symmetry Effects in Quantum Machine Learning Ansatzes
- Authors: Valter Uotila, Väinö Mehtola, Ilmo Salmenperä, Bo Zhao
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2511.04243v2  pdf=https://arxiv.org/pdf/2511.04243v2.pdf

Abstract:
Symmetry is a strong inductive bias in geometric deep learning and its quantum counterpart, and has attracted increasing attention for improving the trainability of QML models. Yet incorporating symmetries into quantum machine learning (QML) ansatzes is not free: symmetrization often adds gates and constrains the circuits. To understand these effects, we present Twirlator, which is an automated pipeline that symmetrizes parameterized QML ansatzes and quantifies the trade-offs as the amount of symmetry increases. Twirlator models partial symmetries by the size of a subgroup of the symmetric group, enabling analysis between the ``no symmetry'' and ``full symmetry'' extremes. Across 19 common ansatz patterns, Twirlator symmetrizes circuits with respect to any subgroup of $S_n$ and measures (1) generator drift, (2) circuit overhead (depth and size), and (3) expressibility and entangling capability. The experimental evaluation focuses on subgroups of $S_4$ and $S_5$. Twirlator reveals that larger subgroups typically increase circuit overhead, reduce expressibility, and often increase entangling capability. The pipeline and results provide practical guidance for selecting ansatz patterns and symmetry levels that balance hardware cost and model performance in symmetry-aware QML applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2511.06672v2
- Title: GCAMPS: A Scalable Classical Simulator for Qudit Systems
- Authors: Ben Harper, Azar C. Nakhl, Thomas Quella, Martin Sevior, Muhammad Usman
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.06672v2  pdf=https://arxiv.org/pdf/2511.06672v2.pdf

Abstract:
Classical simulations of quantum systems are notoriously difficult computational problems, with conventional state vector and tensor network methods restricted to quantum systems that feature only a small number of qudits. The recently introduced Clifford Augmented Matrix Product State (CAMPS) method offer scalability and efficiency by combining both tensor network and stabilizer simulation techniques and leveraging their complementary advantages. This hybrid simulation method has indeed demonstrated significant improvements in simulation performance for qubit circuits. Our work generalises the CAMPS method to higher quantum degrees of freedom -- qudit simulation, resulting in a generalised CAMPS (GCAMPS). Benchmarking this extended simulator on quantum systems with three degrees of freedom, i.e. qutrits, we show that similar to the case of qubits, qutrit systems also benefit from a comparable speedup using these techniques. Indeed, we see a greater improvement with qutrit simulation compared to qubit simulation on the same $T$-doped random Clifford benchmarking circuit as a result of the increased difficulty of conventional qutrit simulation using tensor networks. This extension allows for the classical simulation of problems that were previously intractable without access to a quantum device and will open new avenues to study complex many-body physics and to develop efficient methods for quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2511.10253v2
- Title: Lévy-Khintchine Structure Enables Fast-Forwardable Lindbladian Simulation
- Authors: Minbo Gao, Zhengfeng Ji, Chenghua Liu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.10253v2  pdf=https://arxiv.org/pdf/2511.10253v2.pdf

Abstract:
Simulation of open quantum systems is an area of active research in quantum algorithms. In this work, we revisit the connection between Markovian open-system dynamics and averages of Hamiltonian real-time evolutions, which we refer to as Hamiltonian twirling channels. By applying the Lévy-Khintchine representation theorem, we clarify when and how a dissipative dynamics can be realized using Hamiltonian twirling channels. Guided by the general theory, we explore Hamiltonian twirling with Gaussian, compound Poisson and symmetric stable distributions and their algorithmic implications. These give wide classes of Lindbladians that can be simulated in $Θ(t^{1/α})$ Hamiltonian simulation time without any extra ancilla or other quantum gates for $1\le α\le 2$. Moreover, we prove that these time complexities are asymptotically optimal using an information theoretic approach, which, to the best of our knowledge, is the first result of lower bounds on fast-forwarding simulation algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2512.04173v5
- Title: A contextual advantage for conclusive exclusion: repurposing the Pusey-Barrett-Rudolph construction
- Authors: Yìlè Yīng, David Schmid, Robert W. Spekkens
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.04173v5  pdf=https://arxiv.org/pdf/2512.04173v5.pdf

Abstract:
The task of conclusive exclusion for a set of quantum states is to find a measurement such that for each state in the set, there is an outcome that allows one to conclude with certainty that the state in question was not prepared. Defining classicality of statistics as realizability by a generalized-noncontextual ontological model, we show that there is a quantum-over-classical advantage for how well one can achieve conclusive exclusion. This is achieved in an experimental scenario motivated by the construction appearing in the Pusey-Barrett-Rudolph theorem. We derive noise-robust noncontextuality inequalities bounding the conclusiveness of exclusion, and describe a quantum violation of these. Finally, we show that this bound also constitutes a classical causal compatibility inequality within the bilocality scenario, and that its violation in quantum theory yields a novel possibilistic proof of a quantum-classical gap in that scenario.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2303.01655v2
- Title: Atomtronic superconducting quantum interference device in synthetic dimensions
- Authors: Wenxi Lai, Yu-Quan Ma, Yi-Wen Wei
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2303.01655v2  pdf=https://arxiv.org/pdf/2303.01655v2.pdf

Abstract:
Coherence and scalability are essential properties of quantum systems required in quantum computers. This study presents a high coherent and scalable qubit system with atomtronics in synthetic dimensions. It is atomtronic counterpart of superconducting quantum interference device. Comparing with traditional superconducting quantum interference device which requires at least $2$-dimensional circuits, the synthetic dimensional superconducting quantum interference device can be realized only in $1$-dimensional circuits. The synthetic dimensional system is composed of Bose-Einstein condensate in two neighboring optical wells which is coupled to an external coherent light. Control parameter for the qubit is naturally provided by artificial magnetic flux originated from the coherent atom-light coupling. It should be a great advantage for the scalability and integration feature of quantum logic gates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2304.14306v2
- Title: Dynamical symmetries of the anisotropic oscillator
- Authors: Akash Sinha, Aritra Ghosh, Bijan Bagchi
- Categories: math-ph (primary); math-ph; hep-th; physics.class-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2304.14306v2  pdf=https://arxiv.org/pdf/2304.14306v2.pdf

Abstract:
It is well known that the Hamiltonian of an $n$-dimensional isotropic oscillator admits an $SU(n)$ symmetry, making the system maximally superintegrable. However, the dynamical symmetries of the anisotropic oscillator are much more subtle. We introduce a novel set of canonical transformations that map an $n$-dimensional anisotropic oscillator to the corresponding isotropic problem. Consequently, the anisotropic oscillator is found to possess the same number of conserved quantities as the isotropic oscillator, making it maximally superintegrable too (commensurate case). The first integrals are explicitly calculated in the case of a two-dimensional anisotropic oscillator and remarkably, they admit closed-form expressions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2312.09666v4
- Title: Involutive Markov categories and the quantum de Finetti theorem
- Authors: Tobias Fritz, Antonio Lorenzin
- Categories: math.CT (primary); math.CT; math.OA; quant-ph
- Links: abs=https://arxiv.org/abs/2312.09666v4  pdf=https://arxiv.org/pdf/2312.09666v4.pdf

Abstract:
Markov categories have recently emerged as a powerful high-level framework for probability theory and theoretical statistics. Here we study a quantum version of this concept, called involutive Markov categories. These are equivalent to Parzygnat's quantum Markov categories, but we argue that they offer a simpler and more practical approach. Our main examples of involutive Markov categories have pre-C*-algebras, including infinite-dimensional ones, as objects, together with completely positive unital maps as morphisms in the picture of interest. In this context, we prove a quantum de Finetti theorem for both the minimal and the maximal C*-tensor norms, and we develop a categorical description of such quantum de Finetti theorems which amounts to a universal property of state spaces.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2406.19444v2
- Title: Kramers Dichroism in PT Symmetric Magnets
- Authors: Oles Matsyshyn, Ying Xiong, Justin C. W. Song
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2406.19444v2  pdf=https://arxiv.org/pdf/2406.19444v2.pdf

Abstract:
Superpositions between states in doubly degenerate Kramers pairs can act as an internal degree of freedom. Here we uncover a Kramers dichroism in PT symmetric magnets: interband transitions induced by circularly polarized light irradiation produce a coherent superposition between Kramers partnered states. This allows to optically control the Kramers degree of freedom. In contrast, Kramers pairs optically excited by linearly polarized light remain in a completely mixed state. Strikingly, we find a class of second-order nonlinear responses that directly track the coherence between Kramers partnered states. Such Kramers nonlinearities can be pronounced producing large second-order nonlinear layer polarization responses activated by Kramers degeneracy in layered antiferromagnets. Together with Kramers dichroism, these render optical responses a novel means for accessing the Kramers degree of freedom and diagnosing their quantum coherent state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2410.16355v3
- Title: Integer Factorization via Tensor Network Schnorr's Sieving
- Authors: Marco Tesoro, Ilaria Siloi, Daniel Jaschke, Giuseppe Magnifico, Simone Montangero
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2410.16355v3  pdf=https://arxiv.org/pdf/2410.16355v3.pdf

Abstract:
Classical public-key cryptography standards rely on the Rivest-Shamir-Adleman (RSA) encryption protocol. The security of this protocol is based on the exponential computational complexity of the most efficient classical algorithms for factoring large semiprime numbers into their two prime components. Here, we address RSA factorization building on Schnorr's mathematical framework where factorization translates into a combinatorial optimization problem. We solve the optimization task via tensor network methods, a quantum-inspired classical numerical technique. This tensor network Schnorr's sieving algorithm displays numerical evidence of polynomial scaling of resources with the bit-length of the semiprime. We factorize RSA numbers up to 100 bits and assess how computational resources scale through numerical simulations up to 130 bits, encoding the optimization problem in quantum systems with up to 256 qubits. Only the high-order polynomial scaling of the required resources limits the factorization of larger numbers. Although these results do not currently undermine the security of the present communication infrastructure, they strongly highlight the urgency of implementing post-quantum cryptography or quantum key distribution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2501.12699v5
- Title: Achronal localization and representation of the causal logic from a conserved current, application to the massive scalar boson
- Authors: Domenico P. L. Castrigiano, Carmine De Rosa, Valter Moretti
- Categories: math-ph (primary); math-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2501.12699v5  pdf=https://arxiv.org/pdf/2501.12699v5.pdf

Abstract:
Only recently the concept of achronal localization has been developed as the adequate frame for the description of the localizability of a relativistic quantum mechanical system. Here covariant achronal localizations are gained out of covariant conserved currents computing their flux passing through achronal surfaces. This general method is applied to the probability density currents with causal kernel regarding the massive scalar boson. As (covariant) achronal localizations correspond one-to-one to (covariant) representations of the causal logic, thus, apparently for the first time, a covariant representation of the causal logic for an elementary relativistic quantum mechanical system has been achieved. Similarly a covariant family of representations of the causal logic is derived from the stress-energy tensor of the massive scalar boson. The construction of an achronal localization from a conserved current relies on a version of the divergence theorem for open sets with almost Lipschitz boundary. This result is stated and proved in this work.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2501.14410v4
- Title: Bipartite Fluctuations and Charge Fractionalization in Quantum Wires
- Authors: Magali Korolev, Karyn Le Hur
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2501.14410v4  pdf=https://arxiv.org/pdf/2501.14410v4.pdf

Abstract:
We introduce a quantum information method for measuring fractional charges in ballistic quantum wires generalizing bipartite fluctuations to the chiral quasiparticles in Luttinger liquids, i.e. analyzing and summing charge and current fluctuations in a region of the wire. Bipartite fluctuations at equilibrium are characterized through a logarithmic scaling with distance encoding the entangled nature of these fractional charges in one-dimensional (1D) fluids. This approach clarifies the physical meaning of the dephasing factor of electronic interferences in a ballistic ring geometry at zero temperature, as a result of charge fractionalization. We formulate an analogy towards ground-state energetics. We show how bipartite current fluctuations represent a useful tool to locate quantum phase transitions associated to Mott physics. We address a spin chain equivalence and verify the fractional charges through an algorithm such as Density Matrix Renormalization Group (DMRG). Adding a potential difference between the two sides (parties) of the wire, bipartite fluctuations can detect a bound state localized at the interface through the Jackiw-Rebbi model coexisting with fractional charges.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2502.08702v2
- Title: Absorbing state transitions with discrete symmetries
- Authors: Hyunsoo Ha, David A. Huse, Rhine Samajdar
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2502.08702v2  pdf=https://arxiv.org/pdf/2502.08702v2.pdf

Abstract:
Robust phases of matter, which remain stable under small perturbations, are of fundamental importance in statistical physics and quantum information. Recent advances in interactive quantum dynamics have led to renewed interest in out-of-equilibrium dynamical phases and associated phase transitions in both classical and quantum many-body systems. Motivated by these developments, we investigate whether a stable absorbing phase can exist in one-dimensional classical stochastic systems, with local update rules, in the presence of fluctuations. We study models with multiple absorbing states related by discrete symmetries, such as Z2 for two-state systems, and Z3 or S3 for three-state systems. In these models, domain walls perform random walks and coarsen under local rules, which, if perfect, eventually bring the system to an absorbing state in polynomial time. However, imperfect feedback can cause domain walls to branch, potentially leading to an opposing active phase. While two-state models exhibit a well-known transition between absorbing and active phases as the branching rate increases, in three-state models with only local dynamics, branching is a relevant perturbation, ruling out a robust absorbing phase under purely local rules. However, we discover that by incorporating nonlocal information into the feedback, the absorbing phase can be stabilized, with the transition between the active and absorbing phases belonging to a new universality class. Finally, we outline how these classical rules can be implemented using deterministic quantum circuits and discuss their connections to passive error correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2504.05549v4
- Title: Fast and direct preparation of a genuine lattice BEC via the quantum Mpemba effect
- Authors: Philipp Westhoff, Sebastian Paeckel, Mattia Moroder
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2504.05549v4  pdf=https://arxiv.org/pdf/2504.05549v4.pdf

Abstract:
We demonstrate that dissipative state preparation protocols in many-body systems can be substantially accelerated via the quantum Mpemba effect. Our approach exploits weak symmetries to analytically identify a class of simple, experimentally-realizable states that converge exponentially faster to the steady state than typical random initializations. In particular, we study the preparation of a lattice Bose-Einstein condensate (BEC), where the depletion can be controlled via the dissipation strength. We also show how to tune the momentum of the created high-fidelity BEC by combining superfluid immersion with lattice shaking. Our theoretical predictions are confirmed by numerical simulations of the dissipative dynamics. This protocol paves the way to unlock the enormous potential of the dissipative preparation of highly entangled states in analog quantum simulators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2504.13708v2
- Title: Categories of abstract and noncommutative measurable spaces
- Authors: Tobias Fritz, Antonio Lorenzin
- Categories: math.OA (primary); math.OA; math.CT; math.PR; quant-ph
- Links: abs=https://arxiv.org/abs/2504.13708v2  pdf=https://arxiv.org/pdf/2504.13708v2.pdf

Abstract:
Gelfand duality is a fundamental result that justifies thinking of general unital $C^*$-algebras as noncommutative versions of compact Hausdorff spaces. Inspired by this perspective, we investigate what noncommutative measurable spaces should be. This leads us to consider categories of monotone $σ$-complete $C^*$-algebras as well as categories of Boolean $σ$-algebras, which can be thought of as abstract measurable spaces. Motivated by the search for a good notion of noncommutative measurable space, we provide a unified overview of these categories, alongside those of measurable spaces, and formalize their relationships through functors, adjunctions and equivalences. This includes an equivalence between Boolean $σ$-algebras and commutative monotone $σ$-complete $C^*$-algebras, as well as a Gelfand-type duality adjunction between the latter category and the category of measurable spaces. This duality restricts to two equivalences: one involving standard Borel spaces, which are widely used in probability theory, and another involving the more general Baire measurable spaces. Moreover, this result admits a probabilistic version, where the morphisms are $σ$-normal cpu maps and Markov kernels, respectively. We hope that these developments can also contribute to the ongoing search for a well-behaved Markov category for measure-theoretic probability beyond the standard Borel setting - an open problem in the current state of the art.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2504.19159v2
- Title: Spectral form factor of quadratic $R$-para-particle SYK model with Random Matrix Coupling
- Authors: Tingfei Li
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2504.19159v2  pdf=https://arxiv.org/pdf/2504.19159v2.pdf

Abstract:
This paper investigates the spectral form factor (SFF) of the quadratic $R$-para-particle Sachdev-Ye-Kitaev ($R$-PSYK$_2$) model with various random matrix ensemble couplings. We generalize previous work on Gaussian Unitary Ensemble (GUE) couplings to all three Gaussian ensembles (GUE, GOE, GSE) and three circular ensembles (CUE, COE, CSE). Through analytical and numerical methods, we establish precise correspondences between GUE and CUE results, demonstrating their SFFs satisfy $\mathcal{K}_{\text{GUE}}(2t) \approx \mathcal{K}_{\text{CUE}}(t)$ in the time regime $1 \ll t \ll N$. For the symplectic ensembles, we observe similar behavior with appropriate time rescaling, while we only provide the calculation method for the orthogonal ensembles.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2506.00090v3
- Title: Quantum theory of fractional topological pumping of lattice solitons
- Authors: Julius Bohm, Hugo Gerlitz, Christina Jörg, Michael Fleischhauer
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.other; quant-ph
- Links: abs=https://arxiv.org/abs/2506.00090v3  pdf=https://arxiv.org/pdf/2506.00090v3.pdf

Abstract:
One of the hallmarks of topological systems is the robust quantization of particle transport. It is the origin of the integer-valued quantum Hall conductivity and a potential tool for quantum information technology. Recent experiments on topological pumps constructed by using arrays of photonic waveguides and described by the (lattice-translational invariant) Aubry-André-Harper (AAH) model, have demonstrated both integer and fractional transport of lattice solitons. In these systems, a background medium mediates interactions between photons via a Kerr nonlinearity and leads to the formation of self-bound multi-photon states. Upon increasing the interaction strength a sequence of transitions was observed from a phase with integer transport in a pump cycle through different phases of fractional transport to a phase with no transport. We here present a quantum description of topological pumps of self-bound many-particle states in terms of an effective Hamiltonian of their center-of-mass (COM) motion, which allows to introduce an effective band structure $E_μ(K)$ with $K$ being the COM momentum, and to classify topological phases in terms of generalized symmetries. We provide an explicit analytic expression of the effective Hamiltonian for few particles in the strong interaction limit and present numerical results in the more general case. We identify a topological invariant, an effective single-particle Chern number, which fully governs the soliton transport. Increasing the interaction strength in the AAH model leads to a successive merging of COM bands, which is the origin of the observed sequence of topological phase transitions and also the potential breakdown of topological quantization for some interaction strength.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2506.18059v2
- Title: Towards Quantum Simulation of Rotating Nuclei using Quantum Variational Algorithms
- Authors: Dhritimalya Roy, Somnath Nag
- Categories: nucl-th (primary); nucl-th; hep-ph; nucl-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2506.18059v2  pdf=https://arxiv.org/pdf/2506.18059v2.pdf

Abstract:
Quantum variational algorithms (QVAs) are increasingly potent tools for simulating quantum many-body systems on noisy intermediate-scale quantum (NISQ) devices. This work examines the application of the Variational Quantum Eigensolver (VQE) to four progressively complex models based on the cranked Nilsson-Strutinsky (CNS) framework. By incorporating single-particle spacings, pairing correlations, and rotational cranking terms, we evaluate VQE performance against exact diagonalization (ED) benchmarks. Our results demonstrate that while simpler models achieve high precision (errors $<0.005$), the transition to 8-spin-orbital Hamiltonians reveals significant scaling and optimization challenges. Notably, we show that Model IV, which employs a more expressive RealAmplitudes ansatz, successfully captures the qualitative physics of rotational alignment and reduces energy deviations compared to intermediate benchmarks. These results establish a systematic methodological baseline, identifying the breaking points of hardware-efficient ansatz while validating the potential of QVAs to model the complex competition between pairing and rotation in deformed nuclei.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2507.02765v2
- Title: Spin caloritronics in collinear ferromagnetic helical structures under irradiation
- Authors: Sudin Ganguly, Moumita Dey, Santanu K. Maiti
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.dis-nn; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2507.02765v2  pdf=https://arxiv.org/pdf/2507.02765v2.pdf

Abstract:
We study the charge and spin-dependent thermoelectric response of a ferromagnetic helical system irradiated by arbitrarily polarized light, using a tight-binding framework and the Floquet-Bloch formalism. Transport properties for individual spin channels are determined by employing the non-equilibrium Green's function technique, while phonon thermal conductance is evaluated using a mass-spring model with different lead materials. The findings reveal that that light irradiation induces spin-split transmission features, suppresses thermal conductance, and yields favorable spin thermopower and figure of merit (FOM). The spin FOM consistently outperforms its charge counterpart under various light conditions. Moreover, long-range hopping is shown to enhance the spin thermoelectric performance, suggesting a promising strategy for efficient energy conversion in related ferromagnetic systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2509.17512v2
- Title: Investigating Roles of Triple Excitations for High-precision Determination of Clock Properties of Alkaline Earth Metal Singly Charged Ions
- Authors: A. Chakraborty, Vaibhav Katyal, B. K. Sahoo
- Categories: physics.atom-ph (primary); physics.atom-ph; nucl-th; quant-ph
- Links: abs=https://arxiv.org/abs/2509.17512v2  pdf=https://arxiv.org/pdf/2509.17512v2.pdf

Abstract:
High-accuracy calculations of electric dipole polarizabilities and quadrupole moments ($Θ$) of the clock states of the singly charged calcium (Ca$^+$), strontium (Sr$^+$) and barium (Ba$^+$) alkaline-earth ions are estimated by employing relativistic coupled-cluster (RCC) theory. It demonstrates importance of the triple excitations in the RCC method for precise determination of the above quantities. We also observe a different trend of correlations in the $Θ$ values than an earlier study with respect to orbitals from higher angular momenta. Reliability of the results is verified by comparing the calculated energies, magnetic dipole hyperfine structure constants, and lifetimes of the atomic states with the experimental values of the $^{43}$Ca$^+$, $^{87}$Sr$^+$ and $^{137}$Ba$^+$ ions. Nuclear quadrupole moments of these isotopes are also estimated by combining calculations with the measured electric quadrupole hyperfine structure constants, showing large deviations from the literature values.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2510.26009v3
- Title: A Zero Added Loss Multiplexing (ZALM) Source Simulation
- Authors: Jerry Horgan, Alexander Nico-Katz, Shelbi L. Jenkins, Ashley N. Tittelbaugh, Vivek Visan, Rohan Bali, Marco Ruffini, Boulat A. Bash, et al.
- Categories: cs.NI (primary); cs.NI; quant-ph
- Links: abs=https://arxiv.org/abs/2510.26009v3  pdf=https://arxiv.org/pdf/2510.26009v3.pdf

Abstract:
Zero Added Loss Multiplexing (ZALM) offers broadband, per channel heralded EPR pairs, with a rich parameter space that allows its performance to be tailored for specific applications. We present a modular ZALM simulator that demonstrates how design choices affect output rate and fidelity. Built in NetSquid with QSI controllers, it exposes 20+ tunable parameters, supports IDEAL and REALISTIC modes, and provides reusable components for Spontaneous Parametric Down Conversion (SPDC) sources, interference, Dense Wavelength Division Multiplexing (DWDM) filtering, fiber delay, active polarization gates, detectors, and lossy fiber. Physics based models capture Hong Ou Mandel (HOM) visibility, insertion loss, detector efficiency, gate errors, and attenuation. Using this tool, we map trade offs among fidelity, link distance, and entangled pairs per use, and show how SPDC bandwidth and DWDM grid spacing steer performance. Using the default configuration settings, average fidelity remains constant at 0.83 but the ebit rate decreases from 0.0175 at the source to 0.0 at 50 km; narrowing the SPDC degeneracy bandwidth increases the ebit rate significantly without affecting fidelity. The simulator enables codesign of source, filtering, and feedforward settings for specific quantum memories and integrates as a building block for end to end quantum network studies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2511.11173v2
- Title: Quantum Electron Clouds near Black Holes: Black Atoms and Molecules
- Authors: Hinako Iseki, Shin Sasaki, Kenta Shiozawa
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2511.11173v2  pdf=https://arxiv.org/pdf/2511.11173v2.pdf

Abstract:
We study quantum mechanical wavefunctions near highly curved spaces, i.e., black holes. By utilizing the formalism developed by DeWitt, we derive the Schrödinger equations in the vicinity of the Schwarzschild and the Reissner-Nordström black hole geometries. The quantum electron cloud for the "black hydrogen atom" - an electron trapped by black holes - is particularly studied. We solve the equations and find that black holes generally attract the wavefunctions, localizing them near the horizon where the electrons are most likely to be trapped. These results imply that not only classical objects but also the quantum material and even the chemical properties of the atoms are affected by strong gravity. We also discuss black hydrogen molecules composed of multi-centered Majumdar-Papapetrou black holes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2512.14493v2
- Title: Graphene-Insulator-Superconductor junctions as thermoelectric bolometers
- Authors: Leonardo Lucchesi, Federico Paolucci
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2512.14493v2  pdf=https://arxiv.org/pdf/2512.14493v2.pdf

Abstract:
We design a superconducting thermoelectric bolometer made of a Graphene-Insulator-Superconductor tunnel junction. Our detector has the advantage of being passive, as it directly transduces input power to a voltage without the need to modulate an external bias. We characterize the device via numerical simulation of the full nonlinear thermal dynamical model of the junction, considering heating of both sides of the junction. While estimating noise contributions, we found novel expressions due to the temperatures of both sides being different than the bath temperature. Numerical simulations show a Noise Equivalent Power ${\rm NEP}\sim 4\times 10^{-17}\,{\rm W}/\sqrt{\rm Hz}$ for an input power of $\sim10^{-16}\,{\rm W}$, a response time of $τ_{th}\sim 200\, {\rm ns}$ and an integration time to obtain a Signal-to-Noise Ratio ${\rm SNR}=1$ of $τ_{\rm SNR=1}\sim 100\,μ{\rm s}$ for an input power $\sim 10^{-13}\,{\rm W}$. Therefore, the device shows promise for large-array cosmological experiment applications, also considering its advantages for fabrication and heat budget.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2512.19358v2
- Title: Talking with a ghost: semi-virtual coupled levitated oscillators
- Authors: Ronghao Yin, Yugang Ren, Deok Young Seo, Anoushka Sinha, Jonathan D. Pritchett, Qiongyuan Wu, James Millen
- Categories: physics.ins-det (primary); physics.ins-det; quant-ph
- Links: abs=https://arxiv.org/abs/2512.19358v2  pdf=https://arxiv.org/pdf/2512.19358v2.pdf

Abstract:
Mesoscopic particles levitated by optical, electrical or magnetic fields act as mechanical oscillators with a range of surprising properties, such as tuneable oscillation frequencies, access to rotational motion, and remarkable quality factors. Coupled levitated particles display rich dynamics and non-reciprocal interactions, with applications in sensing and the exploration of non-equilibrium and quantum physics. In this work, we present a single levitated particle displaying coupled-oscillator dynamics by generating an interaction with a virtual or ``ghost'' particle. This ghost levitated particle is simulated on an analogue computer, and its properties can thus be dynamically varied. Our work represents a new angle on measurement-based bath engineering and physical simulation and, in the future, could lead to the generation of novel cooling mechanisms and complex physical simulation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-29 09:51
- arXiv: 2512.19690v2
- Title: Orbital Magnetization Reveals Multiband Topology
- Authors: Chun Wang Chau, Robert-Jan Slager, Wojciech J. Jankowski
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2512.19690v2  pdf=https://arxiv.org/pdf/2512.19690v2.pdf

Abstract:
We demonstrate that nontrivial multiband topological invariants of electronic wavefunctions can be revealed through orbital magnetization responses to external magnetic fields. We find that decomposing orbital magnetization into energetic and quantum-geometric contributions allows one to deduce nontrivial multiband topology, provided knowledge of the energy spectrum. We showcase our findings in general effective models with multiband Euler topology. We moreover identify such multiband topological invariants in effective models of strontium ruthenate ($\text{Sr}_2 \text{Ru} \text{O}_4$), which may in principle be verified in the state-of-the-art doping-dependent magnetization measurements. Our reconstruction scheme for multiband invariants sheds a topological perspective on the multiorbital effects in materials realizing unconventional phenomenologies of orbital currents or multiband superconductivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.19976v1
- Title: A Surface-Scaffolded Molecular Qubit
- Authors: Tian-Xing Zheng, M. Iqbal Bakti Utama, Xingyu Gao, Moumita Kar, Xiaofei Yu, Sungsu Kang, Hanyan Cai, Tengyang Ruan, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2601.19976v1  pdf=https://arxiv.org/pdf/2601.19976v1.pdf

Abstract:
Fluorescent spin qubits are central building blocks of quantum technologies. Placing these qubits at surfaces maximizes coupling to nearby spins and fields, enabling nanoscale sensing and facilitating integration with photonic and superconducting devices. However, reducing the dimensions or size of established qubit systems without sacrificing the qubit performance or degrading the coherence lifetime remains challenging. Here, we introduce a surface molecular qubit formed by pentacene molecules scaffolded on a two-dimensional (2D) material, hexagonal boron nitride (hBN). The qubit exhibits stable fluorescence and optically detected magnetic resonance (ODMR) from cryogenic to ambient conditions. With fully deuterated pentacene, the Hahn-echo coherence reaches 22 $μ$s and further extends to 214 $μ$s under dynamical decoupling, outperforming state-of-the-art shallow NV centers in diamond, despite being positioned directly on the surface. We map the local spin environment, resolving couplings to nearby nuclear and electron spins that can serve as auxiliary quantum resources. This platform combines true surface integration, long qubit coherence, and scalable fabrication, opening routes to quantum sensing, quantum simulation, and hybrid quantum devices. It also paves the way for a broader family of 2D material-supported molecular qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.19986v1
- Title: The superradiant phase is a finite size effect in two-photon processes
- Authors: Fabrizio Ramírez, David Villaseñor, Nahum Vázquez, Jorge G. Hirsch
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2601.19986v1  pdf=https://arxiv.org/pdf/2601.19986v1.pdf

Abstract:
Two-photon light-matter interactions exhibit distinctive features such as spectral collapse. The two-photon Dicke model has been reported to exhibit a superradiant phase which could be useful in quantum applications. Here we show that this superradiant phase is not a genuine thermodynamic phase but a finite-size effect. Combining analytical and numerical analyses, we demonstrate that the superradiant region shrinks with increasing system size and disappears in the thermodynamic limit, while spectral collapse remains. Our results clarify the nature of superradiant conditions in two-photon systems and constrain its realization in quantum platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.19988v1
- Title: Optically Addressable Molecular Spins at 2D Surfaces
- Authors: Xuankai Zhou, Yan-Tung Kong, Cheuk Kit Cheung, Guodong Bian, Reda Moukaouine, King Cho Wong, Yumeng Sun, Cheng-I Ho, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2601.19988v1  pdf=https://arxiv.org/pdf/2601.19988v1.pdf

Abstract:
Optically addressable spins at material surfaces have represented a long-standing ambition in quantum sensing, providing atomic resolution and quantum-limited sensitivity. However, they are constrained by a finite depth at which the quantum spins can be stabilized. Here, we demonstrate a hybrid molecular-2D architecture that realizes quantum spin sensors directly on top of the surface. By anchoring spin-active molecules onto hexagonal boron nitride (hBN), we eliminate the depth of the quantum sensor while also exhibiting robust spin properties from 4~K to room temperature (RT). The Hahn-echo spin coherence time exceeds \(T_2 = 3.4~\upmu\text{s}\) at 4~K, outperforming values in bulk organic crystals and overturning the prevailing expectation that spin inevitably deteriorates upon approaching the surface. By chemically tuning the molecule through deuteration, \(T_2\) improves by more than 10-fold, and under dynamic decoupling, coherence is prolonged to the intrinsic lifetime limit, exceeding 300~\(\upmu\text{s}\). Proximal proton spins and the magnetic response of two-dimensional magnets beneath the hBN layer have been detected at RT. These molecular spins form surface quantum sensors with long coherence, optical addressability, and interfacial versatility, enabling a scalable, adaptable architecture beyond what conventional solid-state platforms offer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20007v1
- Title: Alternating ZX Circuit Extraction for Hardware-Adaptive Compilation
- Authors: Ludwig Schmid, Korbinian Staudacher, Robert Wille
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20007v1  pdf=https://arxiv.org/pdf/2601.20007v1.pdf

Abstract:
We present a novel quantum circuit extraction scheme that tightly integrates graph-like ZX diagrams with hardware-adaptive routing. The method utilizes the degrees of freedom during the conversion from a ZX diagram to a quantum circuit (extraction). It alternates between generating multiple extraction options and evaluating them based on hardware constraints, allowing the routing algorithm to inform and guide the extraction process. This feedback loop extends existing graph-like ZX extraction and supports modular integration of different extraction algorithms, routing strategies, and target hardware, making it a versatile building block during compilation. To perform numerical evaluations, a reference instance of the scheme is implemented with SWAP-based routing for neutral atom hardware and evaluated using various benchmark collections on small-to mid-scale circuits. The reference code is available as open-source, allowing fast integration of other extraction and/or routing tools to stimulate further research and foster improvements of the proposed scheme.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20025v1
- Title: Foundry-Enabled Patterning of Diamond Quantum Microchiplets for Scalable Quantum Photonics
- Authors: Jawaher Almutlaq, Alessandro Buzzi, Anders Khaykin, Linsen Li, William Yzaguirre, Maxim Sirotin, Gerald Gilbert, Genevieve Clark, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20025v1  pdf=https://arxiv.org/pdf/2601.20025v1.pdf

Abstract:
Quantum technologies promise secure communication networks and powerful new forms of information processing, but building these systems at scale remains a major challenge. Diamond is an especially attractive material for quantum devices because it can host atomic-scale defects that emit single photons and store quantum information with exceptional stability. However, fabricating the optical structures needed to control light in diamond typically relies on slow, bespoke processes that are difficult to scale. In this work, we introduce a manufacturing approach that brings diamond quantum photonics closer to industrial production. Instead of sequentially defining each device by lithography written directly on diamond, we fabricate high-precision silicon masks using commercial semiconductor foundries and transfer them onto diamond via microtransfer printing. These masks define large arrays of nanoscale optical structures, shifting the most demanding pattern-definition steps away from the diamond substrate, improving uniformity, yield, and throughput. Using this method, we demonstrate hundreds of diamond "quantum microchiplets" with improved optical performance and controlled interaction with quantum emitters. The chiplet format allows defective devices to be replaced and enables integration with existing photonic and electronic circuits. Our results show that high-quality diamond quantum devices can be produced using scalable, foundry-compatible techniques. This approach provides a practical pathway toward large-scale quantum photonic systems and hybrid quantum-classical technologies built on established semiconductor manufacturing infrastructure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20029v1
- Title: A Cyclic Layerwise QAOA Training
- Authors: Enhyeok Jang, Zihan Chen, Dongho Ha, Seungwoo Choi, Yongju Lee, Jaewon Kwon, Eddy Z. Zhang, Yipeng Huang, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20029v1  pdf=https://arxiv.org/pdf/2601.20029v1.pdf

Abstract:
The quantum approximate optimization algorithm (QAOA) is a hybrid quantum-classical algorithm for solving combinatorial optimization problems. Multi-angle QAOA (MA-QAOA), which assigns independent parameters to each Hamiltonian operator term, achieves superior approximation performance even with fewer layers than standard QAOA. Unfortunately, this increased expressibility can raise the classical computational cost due to a greater number of parameters. The recently proposed Layerwise MA-QAOA (LMA-QAOA) reduces this overhead by training one layer at a time, but it may suffer from obtaining the precise solution due to the previously fixed parameters. This work addresses two questions for efficient MA-QAOA training: (i) What is the optimal granularity for parameter updates per epoch, and (ii) How can we get precise final cost function results while only partially updating the parameters per epoch? Despite the benefit of reducing the parameters that update per epoch can reduce the classical computation overhead, too fine or coarse a granularity of Hamiltonian update can degrade the MA-QAOA training efficiency. We find that optimizing one complete layer per epoch is an efficient granularity. Moreover, selectively retraining each layer by tracking gradient variations can achieve a final cost function equivalent to the standard MA-QAOA while lowering the parameter update overhead. Based on these insights, we propose Orbit-QAOA, which cyclically revisits layers and selectively freezes stabilized parameters. Across diverse graph benchmarks, Orbit-QAOA reduces training steps by up to 81.8%, reduces approximation ratio error by up to 72x compared to the unified stop condition-applied enhanced LMA-QAOA, and achieves equivalent approximation performance compared to the standard MA-QAOA.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20044v1
- Title: Quantum Channels on Graphs: a Resonant Tunneling Perspective
- Authors: Giuseppe Catalano, Farzad Kianvash, Vittorio Giovannetti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20044v1  pdf=https://arxiv.org/pdf/2601.20044v1.pdf

Abstract:
Quantum transport on structured networks is strongly influenced by interference effects, which can dramatically modify how information propagates through a system. We develop a quantum-information-theoretic framework for scattering on graphs in which a full network of connected scattering sites is treated as a quantum channel linking designated input and output ports. Using the Redheffer star product to construct global scattering matrices from local ones, we identify resonant concatenation, a nonlinear composition rule generated by internal back-reflections. In contrast to ordinary channel concatenation, resonant concatenation can suppress noise and even produce super-activation of the quantum capacity, yielding positive capacity in configurations where each constituent channel individually has zero capacity. We illustrate these effects through models exhibiting resonant-tunneling-enhanced transport. Our approach provides a general methodology for analyzing coherent information flow in quantum graphs, with relevance for quantum communication, control, and simulation in structured environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20062v1
- Title: Comment on "Determining angle of arrival of radio-frequency fields using subwavelength, amplitude-only measurements of standing waves in a Rydberg atom sensor"
- Authors: M. Chilcott, N. Kjærgaard
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2601.20062v1  pdf=https://arxiv.org/pdf/2601.20062v1.pdf

Abstract:
We discuss the consequence of excluding allowed RF-transition between substates of a field-dressed Rydberg manifold when predicting the spectrum that will be observed if the dressed system is probed in an optical EIT scheme.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20073v1
- Title: Ensemble-Based Quantum Signal Processing for Error Mitigation
- Authors: Suying Liu, Yulong Dong, Dong An, Murphy Yuezhen Niu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20073v1  pdf=https://arxiv.org/pdf/2601.20073v1.pdf

Abstract:
Despite rapid advances in quantum hardware, noise remains a central obstacle to deploying quantum algorithms on near-term devices. In particular, random coherent errors that accumulate during circuit execution constitute a dominant and fundamentally challenging noise source. We introduce a noise-resilient framework for Quantum Signal Processing (QSP) that mitigates such coherent errors without increasing circuit depth or ancillary qubit requirements. Our approach uses ensembles of noisy QSP circuits combined with measurement-level averaging to suppress random phase errors in Z rotations. Building on this framework, we develop robust QSP algorithms for implementing polynomial functions of Hermitian matrices and for estimating observables, with applications to Hamiltonian simulation, quantum linear systems, and ground-state preparation. We analyze the trade-off between approximation error and hardware noise, which is essential for practical implementation under the stringent depth and coherence constraints of current quantum hardware. Our results establish a practical pathway for integrating error mitigation seamlessly into algorithmic design, advancing the development of robust quantum computing, and enabling the discovery of scientific applications with near- and mid-term quantum devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20074v1
- Title: Local Distinguishability of Multipartite Orthogonal Quantum States: Generalized and Simplified
- Authors: Ian George, Mohammad A. Alhejji
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20074v1  pdf=https://arxiv.org/pdf/2601.20074v1.pdf

Abstract:
In a seminal work [PRL85.4972], Walgate, Short, Hardy, and Vedral prove in finite dimensions that for every pair of pure multipartite orthogonal quantum states, there exists a one-way local operations and classical communication (LOCC) protocol that perfectly distinguishes the pair. We extend this result to infinite dimensions with a simpler proof. For states on $\mathbb{C}^{d_A \times d_A} \otimes \mathbb{C}^{d_B \times d_B}$, we strengthen this existence result by constructing an $O(d_A^2 d_B^2)$-time algorithm that specifies such a perfect one-way LOCC protocol. Finally, we establish the equivalence between Walgate et al.'s result and the fact that the one-shot environment-assisted classical capacity of every quantum channel is at least 1 bit per channel use, thereby clarifying the literature on these notions. At the core of all of these results is the fact that every operator with vanishing trace admits a basis where its diagonal entries are all zero.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20081v1
- Title: Spectral Transitions and Singular Continuous Spectrum in A New Family of Quasi-periodic Quantum Walks
- Authors: Xinyu Yang, Long Li, Qi Zhou
- Categories: quant-ph (primary); quant-ph; math.SP
- Links: abs=https://arxiv.org/abs/2601.20081v1  pdf=https://arxiv.org/pdf/2601.20081v1.pdf

Abstract:
This paper introduces and rigorously analyzes a new class of one-dimensional discrete-time quantum walks whose dynamics are governed by a parametrized family of extended CMV matrices. The model generalizes the unitary almost Mathieu operator (UAMO) and exhibits a richer spectral phase diagram, closely resembling the extended Harper's model. It provides the first example of a solvable quasi-periodic quantum walk that exhibits a stable region of purely singular continuous spectrum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20091v1
- Title: Krypton-sputtered tantalum films for scalable high-performance quantum devices
- Authors: Maciej W. Olszewski, Lingda Kong, Simon Reinhardt, Daniel Tong, Xinyi Du, Gabriele Di Gianluca, Haoran Lu, Saswata Roy, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2601.20091v1  pdf=https://arxiv.org/pdf/2601.20091v1.pdf

Abstract:
Superconducting qubits based on tantalum (Ta) thin films have demonstrated the highest-performing microwave resonators and qubits. This makes Ta an attractive material for superconducting quantum computing applications, but, so far, direct deposition has largely relied on high substrate temperatures exceeding \SI{400}{\celsius} to achieve the body-centered cubic phase, BCC (\textalpha-Ta). This leads to compatibility issues for scalable fabrication leveraging standard semiconductor fabrication lines. Here, we show that changing the sputter gas from argon (Ar) to krypton (Kr) promotes BCC Ta synthesis on silicon (Si) at temperatures as low as \SI{200}{\celsius}, providing a wide process window compatible with back-end-of-the-line fabrication standards. Furthermore, we find these films to have substantially higher electronic conductivity, consistent with clean-limit superconductivity. We validated the microwave performance through coplanar waveguide resonator measurements, finding that films deposited at \SI{250}{\celsius} and \SI{350}{\celsius} exhibit a tight performance distribution at the state of the art. Higher temperature-grown films exhibit higher losses, in correlation with the degree of Ta/Si intermixing revealed by cross-sectional transmission electron microscopy. Finally, with these films, we demonstrate transmon qubits with a relatively compact, \SI{20}{\micro\meter} capacitor gap, achieving a median quality factor up to 14 million.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20114v1
- Title: Engineering the non-Hermitian SSH model with skin effects in Rydberg atom arrays
- Authors: J. N. Bai, F. Yang, D. Yan, Weibin Li, X. Q. Shao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20114v1  pdf=https://arxiv.org/pdf/2601.20114v1.pdf

Abstract:
We propose and systematically analyze a practical scheme for implementing a one-dimensional non-Hermitian Su-Schrieffer-Heeger model using individually addressable Rydberg atom arrays. Our setup consists of an atomic chain with three-atom unit cells, in which a synthetic gauge field is generated by applying multi-color laser fields. By engineering fast dissipative channels for one auxiliary atom in each unit cell, the adiabatic elimination effectively gives rise to a non-Hermitian skin effect. We examine how fluctuations in the experimental parameters influence both the skin effect and the topological invariant under open and periodic boundary conditions in real space and find that both features remain highly robust. This work establishes a versatile, controllable, and programmable open-system quantum simulator with neutral atoms, providing a clear route for exploring rich non-Hermitian topological phenomena.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20155v1
- Title: Universal thermodynamic implementation of a process with a variable work cost
- Authors: Philippe Faist
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20155v1  pdf=https://arxiv.org/pdf/2601.20155v1.pdf

Abstract:
The minimum amount of thermodynamic work required in order to implement a quantum computation or a quantum state transformation can be quantified using frameworks based on the resource theory of thermodynamics, deeply rooted in the works of Landauer and Bennett. For instance, the work we need to invest in order to implement $n$ independent and identically distributed (i.i.d.) copies of a quantum channel is quantified by the thermodynamic capacity of the channel when we require the implementation's accuracy to be guaranteed in diamond norm over the $n$-system input. Recent work showed that work extraction can be implemented universally, meaning the same implementation works for a large class of input states, while achieving a variable work cost that is optimal for each individual i.i.d. input state. Here, we revisit some techniques leading to derivation of the thermodynamic capacity, and leverage them to construct a thermodynamic implementation of $n$ i.i.d. copies of any time-covariant quantum channel, up to some process decoherence that is necessary because the implementation reveals the amount of consumed work. The protocol uses so-called thermal operations and achieves the optimal per-input work cost for any i.i.d. input state; it relies on the conditional erasure protocol in our earlier work, adjusted to yield variable work. We discuss the effect of the work-cost decoherence. While it can significantly corrupt the correlations between the output state and any reference system, we show that for any time-covariant i.i.d. input state, the state on the output system faithfully reproduces that of the desired process to be implemented. As an immediate consequence of our results, we recover recent results for optimal work extraction from i.i.d. states up to the error scaling and implementation specifics, and propose an optimal preparation protocol for time-covariant i.i.d. states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20167v1
- Title: Contextuality as an Information-Theoretic Obstruction to Classical Probability
- Authors: Song-Ju Kim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20167v1  pdf=https://arxiv.org/pdf/2601.20167v1.pdf

Abstract:
Contextuality is a central feature distinguishing quantum from classical probability theories, yet its operational meaning remains subject to interpretation. We reconsider contextuality from an information-theoretic perspective, focusing on operational models constrained to maintain a single internal state with fixed semantics across multiple contexts. Under this constraint, we show that contextual statistics certify an unavoidable obstruction to classical probabilistic descriptions. Specifically, any classical model that reproduces such statistics must either embed contextual dependence into the internal state or introduce additional external labels carrying nonzero information. This result identifies contextuality as a witness of irreducible information cost in classical representations, rather than as a purely nonclassical anomaly. From this viewpoint, quantum probability emerges as a canonical framework that accommodates contextual operations without requiring explicit contextual encoding.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20186v1
- Title: A general interpretation of nonlinear connected time crystals: quantum self-sustaining combined with quantum synchronization
- Authors: Song-hai Li, Najmeh Es'haqi-Sani, Xingli Li, Wenlin Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20186v1  pdf=https://arxiv.org/pdf/2601.20186v1.pdf

Abstract:
Although classical nonlinear dynamics suggests that sufficiently strong nonlinearity can sustain oscillations, quantization of such model typically yields a time-independent steady state that respects time-translation symmetry and thus precludes time-crystal behavior. We identify dephasing as the primary mechanism enforcing this symmetry, which can be suppressed by intercomponent phase correlations. Consequently, a sufficient condition for realizing a continuous time crystal is a nonlinear quantum self-sustaining system exhibiting quantum synchronization among its constituents. As a concrete example, we demonstrate spontaneous oscillations in a synchronized array of van der Pol oscillators, corroborated by both semiclassical dynamics and the quantum Liouville spectrum. These results reduce the identification of time crystals in many-body systems to the evaluation of only two-body correlations and provide a framework for classifying uncorrelated time crystals as trivial.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20237v1
- Title: Fast state transfer via loop weights
- Authors: Gabor Lippner, Yujia Shi
- Categories: quant-ph (primary); quant-ph; math.CO
- Links: abs=https://arxiv.org/abs/2601.20237v1  pdf=https://arxiv.org/pdf/2601.20237v1.pdf

Abstract:
We prove that almost-linear-time high-fidelity state transfer is achievable in a quantum spin chain using loop weights at the second and second-to-last nodes. We provide specific parameter values, and using a careful analysis of the eigenvectors we make precise quantitative estimates of the transfer time and strength.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20247v1
- Title: Computer Science Challenges in Quantum Computing: Early Fault-Tolerance and Beyond
- Authors: Jens Palsberg, Jason Cong, Yufei Ding, Bill Fefferman, Moinuddin Qureshi, Gokul Subramanian Ravi, Kaitlin N. Smith, Hanrui Wang, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20247v1  pdf=https://arxiv.org/pdf/2601.20247v1.pdf

Abstract:
Quantum computing is entering a period in which progress will be shaped as much by advances in computer science as by improvements in hardware. The central thesis of this report is that early fault-tolerant quantum computing shifts many of the primary bottlenecks from device physics alone to computer-science-driven system design, integration, and evaluation. While large-scale, fully fault-tolerant quantum computers remain a long-term objective, near- and medium-term systems will support early fault-tolerant computation with small numbers of logical qubits and tight constraints on error rates, connectivity, latency, and classical control. How effectively such systems can be used will depend on advances across algorithms, error correction, software, and architecture. This report identifies key research challenges for computer scientists and organizes them around these four areas, each centered on a fundamental question.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20263v1
- Title: A Quantum Photonic Approach to Graph Coloring
- Authors: Jesua Epequin, Pascale Bendotti, Joseph Mikael
- Categories: quant-ph (primary); quant-ph; cs.DM
- Links: abs=https://arxiv.org/abs/2601.20263v1  pdf=https://arxiv.org/pdf/2601.20263v1.pdf

Abstract:
Gaussian Boson Sampling (GBS) is a quantum computational model that leverages linear optics to solve sampling problems believed to be classically intractable. Recent experimental breakthroughs have demonstrated quantum advantage using GBS, motivating its application to real-world combinatorial optimization problems.   In this work, we reformulate the graph coloring problem as an integer programming problem using the independent set formulation. This enables the use of GBS to identify cliques in the complement graph, which correspond to independent sets in the original graph. Our method is benchmarked against classical heuristics and exact algorithms on two sets of instances: Erdős-Rényi random graphs and graphs derived from a smart-charging use case. The results demonstrate that GBS can provide competitive solutions, highlighting its potential as a quantum-enhanced heuristic for graph-based optimization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20287v1
- Title: Fingerprints of classical memory in quantum hysteresis
- Authors: Francesco Caravelli
- Categories: quant-ph (primary); quant-ph; cond-mat.other
- Links: abs=https://arxiv.org/abs/2601.20287v1  pdf=https://arxiv.org/pdf/2601.20287v1.pdf

Abstract:
We present a simple framework for classical and quantum ``memory'' in which the Hamiltonian at time $t$ depends on past values of a control Hamiltonian through a causal kernel. This structure naturally describes finite-bandwidth or filtered control channels and provides a clean way to distinguish between memory in the control and genuine non-Markovian dynamics of the state. We focus on models where $H(t)=H_0+\int_{-\infty}^{t}K(t-s)\,H_1(s)\,ds$, and illustrate the framework on single-qubit examples such as $H(t)=σ_z+Φ(t)σ_x$ with $Φ(t)=\int_{-\infty}^{t}K(t-s)\,u(s)\,ds$. We derive basic properties of such dynamics, discuss conditions for unitarity, give an equivalent time-local description for exponential kernels, and show explicitly how hysteresis arises in the response of a driven qubit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20296v1
- Title: Electromagnetically Induced Transparency Spectra of Ladder Four-Level System with Quantum Frequency Mixing
- Authors: Sheng-Xian Xiao, Tao Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20296v1  pdf=https://arxiv.org/pdf/2601.20296v1.pdf

Abstract:
In this paper, we generalized the quantum frequency mixing technology to a ladder-type four-level system and studied its effect on electromagnetically induced transparency spectra. We found a secondary splitting of Autler-Townes splitting in the probing field transmission spectra, which could be understood by the effective Hamiltonian derived with multi-mode Floquet theory. The Frequency mixing scheme developed here enables continuous tunablity of the resonant frequency between upper levels, which facilitates the broad band sensing of AC field. Furthermore, by introducing an additional periodic driving, we realize an effective model that two distinct quantum interference effects coexist: interference among Floquet channels and loop interference arising from closed coherent pathways. Both interference effects could be read out from the transmission spectra independently. The changing of the distance between double splitting peaks represents the interference of Floquet channels, while their asymmetric linewidth broadening is linked with the total effective phase of the loop. This not only provides complementary readout for extracting the phase of AC field, but also establishes a new paradigm for coherent control in multi-level quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20393v1
- Title: Scalable Multi-QPU Circuit Design for Dicke State Preparation: Optimizing Communication Complexity and Local Circuit Costs
- Authors: Ziheng Chen, Junhong Nie, Xiaoming Sun, Jialin Zhang, Jiadong Zhu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20393v1  pdf=https://arxiv.org/pdf/2601.20393v1.pdf

Abstract:
Preparing large-qubit Dicke states is of broad interest in quantum computing and quantum metrology. However, the number of qubits available on a single quantum processing unit (QPU) is limited -- motivating the distributed preparation of such states across multiple QPUs as a practical approach to scalability. In this article, we investigate the distributed preparation of $n$-qubit $k$-excitation Dicke states $D(n,k)$ across a general number $p$ of QPUs, presenting a distributed quantum circuit (each QPU hosting approximately $\lceil n/p \rceil$ qubits) that prepares the state with communication complexity $O(p \log k)$, circuit size $O(nk)$, and circuit depth $O\left(p^2 k + \log k \log (n/k)\right)$. To the best of our knowledge, this is the first construction to simultaneously achieve logarithmic communication complexity and polynomial circuit size and depth. We also establish a lower bound on the communication complexity of $p$-QPU distributed state preparation for a general target state. This lower bound is formulated in terms of the canonical polyadic rank (CP-rank) of a tensor associated with the target state. For the special case $p = 2$, we explicitly compute the CP-rank corresponding to the Dicke state $D(n,k)$ and derive a lower bound of $\lceil\log (k + 1)\rceil$, which shows that the communication complexity of our construction matches this fundamental limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20403v1
- Title: Network Nonlocality Sharing in Generalized Star Network from Bipartite Bell Inequalities
- Authors: Hao-Miao Jiang, Xiang-Jiang Chen, Liu-Jun Wang, Qing Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20403v1  pdf=https://arxiv.org/pdf/2601.20403v1.pdf

Abstract:
This work investigates network nonlocality sharing for a broad class of bipartite Bell inequalities in a generalized star network with an $(n,m,k)$ configuration, comprising $n$ independent branches, $m$ sequential Alices per branch, and $k$ measurement settings per party. On each branch, the intermediate Alices implement optimal weak measurements, whereas the final Alice and the central Bob perform sharp projective measurements. Network nonlocality sharing is witnessed when the quantum values of the network correlations associated with relevant parties simultaneously violate a star-network Bell inequality generated from the given class of bipartite Bell inequalities. We streamline the calculation of the quantum values of the network correlations and derive an analytical expression for the bipartite quantum correlator, valid for arbitrary measurement settings and weak-measurement strengths. The network nonlocality sharing for Vértesi inequalities has been studied within the framework, and simultaneous violations are found in $(2,2,6)$ and $(2,2,465)$ cases, with the latter exhibiting greater robustness. Our approach suggests a practical route to studying network nonlocality sharing by utilizing diverse bipartite Bell inequalities beyond the commonly used CHSH-type constructions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20458v1
- Title: Echo Cross Resonance gate error budgeting on a superconducting quantum processor
- Authors: Travers Ward, Russell P. Rundle, Richard Bounds, Norbert Deak, Gavin Dold, Apoorva Hegde, William Howard, Ailsa Keyser, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20458v1  pdf=https://arxiv.org/pdf/2601.20458v1.pdf

Abstract:
High fidelity quantum operations are key to enabling fault-tolerant quantum computation. Superconducting quantum processors have demonstrated high-fidelity operations, but on larger devices there is commonly a broad distribution of qualities, with the low-performing tail affecting near-term performance and applications. Here we present an error budgeting procedure for the native two-qubit operation on a 32-qubit superconducting-qubit-based quantum computer, the OQC Toshiko gen-1 system. We estimate the prevalence of different forms of error such as coherent error and control qubit leakage, then apply error suppression strategies based on the most significant sources of error, making use of pulse-shaping and additional compensating gates. These techniques require no additional hardware overhead and little additional calibration, making them suitable for routine adoption. An average reduction of 3.7x in error rate for two qubit operations is shown across a chain of 16 qubits, with the median error rate improving from 4.6$\%$ to 1.2$\%$ as measured by interleaved randomized benchmarking. The largest improvements are seen on previously under-performing qubit pairs, demonstrating the importance of practical error suppression in reducing the low-performing tail of gate qualities and achieving consistently good performance across a device.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20479v1
- Title: Multiple mobility rings in non-Hermitian Su-Schrieffer-Heeger chain with quasiperiodic potentials
- Authors: Guan-Qiang Li, Zhi-Yu Lin, You-Jiao Dong, Ya-Feng Xue, Chun-Yang Ren, Ping Peng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20479v1  pdf=https://arxiv.org/pdf/2601.20479v1.pdf

Abstract:
The localization property of a non-Hermitian Su-Schrieffer-Heeger (SSH) chain with quasi-periodic on-site potential is investigated. In contrast to the preceding investigations, the quantum phase transition between localized state and extended one is achieved by adjusting the strength of intracellular or intercellular hopping. The energy spectra and eigenstate distributions of the system's Hamiltonian near the boundary of the phase transition exhibit different behaviors when the Hermiticity, non-Hermiticity and mosaic modulation of the quasi-periodic potential are considered, respectively. The existence of the mobility ring is revealed in the non-Hermitian SSH chain by studying of the critical behaviors near the boundary. More interestingly, the multiple mobility rings emerge when the period number of the mosaic modulation is increased. The result is helpful for the investigation of the localization-delocalization transition in the SSH-type system under the combined action of the non-Hermiticity and quasi-periodicity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20488v1
- Title: Revisiting the Interpretations of Quantum Mechanics: From FAPP Solutions to Contextual Ontologies
- Authors: Philippe Grangier
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2601.20488v1  pdf=https://arxiv.org/pdf/2601.20488v1.pdf

Abstract:
This note presents a concise and non-polemical comparison of several major interpretations of quantum mechanics, with a particular emphasis on the distinction between FAPP-solutions ("For All Practical Purposes'') versus ontological solutions to the measurement problem. Building on this distinction, we argue that the Contexts-Systems-Modalities (CSM) framework, supplemented by the operator-algebraic description of macroscopic contexts, provides a conceptually complete, non-FAPP ontology that naturally incorporates irreversibility and the physical structure of measurement devices. This approach differs significantly from other ontological interpretations such as Bohmian mechanics, spontaneous collapse, or many-worlds, and highlights the major role of contextual quantization in shaping quantum theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20525v1
- Title: Will we ever quantize the center of mass of macroscopic systems? A case for a Heisenberg cut in quantum mechanics
- Authors: George E. A. Matsas, Gabriel H. S. Aguiar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20525v1  pdf=https://arxiv.org/pdf/2601.20525v1.pdf

Abstract:
The concept of quantum particles derives from quantum field theory. Accepting that quantum mechanics is valid all the way implies that not only composite particles (such as protons and neutrons) would be derived from a field theory, but also the center of mass of bodies as heavy as rocks. Despite the fabulous success of quantum mechanics, it is unreasonable to assume the existence of annihilation and creation operators for rocks, and so on. Fortunately, there are strong reasons to doubt that wave mechanics can describe the center of mass of systems at or above the Planck scale, thereby jeopardizing the construction of the corresponding Fock space. As a result, systems with masses exceeding the Planck mass would have their center of mass described through classical mechanics, regardless of being able to harbor macroscopic quantum phenomena as observed in the laboratory. Here, we briefly revisit (i) the arguments for the need for a Heisenberg cut delimitating the boundary between the quantum and classical realms and (ii) the kind of new physics expected at (the uncharted region of) the Heisenberg cut.''

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20557v1
- Title: Detector's response to coherent Rindler and Minkowski photons
- Authors: Pradeep Kumar Kumawat, Dipankar Barman, Bibhas Ranjan Majhi
- Categories: quant-ph (primary); quant-ph; gr-qc; hep-th
- Links: abs=https://arxiv.org/abs/2601.20557v1  pdf=https://arxiv.org/pdf/2601.20557v1.pdf

Abstract:
We observe that the transition probability in a static two-level quantum detector interacting with a coherent Rindler photon is different from the same of the Rindler detector which is in interaction with a coherent Minkowski photon. Situation does not change in the response of quantum detector for the classical limit of the photon state. This we investigate in $(1+1)$ and $(3+1)$-spacetime dimensions. Interestingly, the transition probabilities of the ``classical'' detector in the classical limit of the photon state in $(1+1)$-dimensions, for these two scenarios, appear to be identical when the frequencies of photon mode and detector are taken to be same. However, our obtained detector's transition probabilities in $(3+1)$-dimensions, which are calculated under the large acceleration condition, do not show such signature. The implications of these observations are discussed as well.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20560v1
- Title: Time complexity of a monitored quantum search with resetting
- Authors: Emma C. King, Sayan Roy, Francesco Mattiotti, Maximilian Kiefer-Emmanouilidis, Markus Bläser, Giovanna Morigi
- Categories: quant-ph (primary); quant-ph; cond-mat.other; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2601.20560v1  pdf=https://arxiv.org/pdf/2601.20560v1.pdf

Abstract:
Searching a database is a central task in computer science and is paradigmatic of transport and optimization problems in physics. For an unstructured search, Grover's algorithm predicts a quadratic speedup, with the search time $τ(N)=Θ(\sqrt{N})$ and $N$ the database size. Numerical studies suggest that the time complexity can change in the presence of feedback, injecting information during the search. Here, we determine the time complexity of the quantum analog of a randomized algorithm, which implements feedback in a simple form. The search is a continuous-time quantum walk on a complete graph, where the target is continuously monitored by a detector. Additionally, the quantum state is reset if the detector does not click within a specified time interval. This yields a non-unitary, non-Markovian dynamics. We optimize the search time as a function of the hopping amplitude, detection rate, and resetting rate, and identify the conditions under which time complexity could outperform Grover's scaling. The overall search time does not violate Grover's optimality bound when including the time budget of the physical implementation of the measurement. For databases of finite sizes monitoring can warrant rapid convergence and provides a promising avenue for fault-tolerant quantum searches.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20587v1
- Title: A Hybrid Jump-Diffusion Model for Coherent Optical Control of Quantum Emitters in hBN
- Authors: Saifian Farooq Bhat, Michael K. Koch, Sachin Negi, Alexander Kubanek, Vibhav Bharadwaj
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.20587v1  pdf=https://arxiv.org/pdf/2601.20587v1.pdf

Abstract:
Hexagonal boron nitride (hBN) has emerged as a promising two-dimensional host for stable single-photon emission owing to its wide bandgap, high photostability, and compatibility with nanophotonic integration. We present a simulation-based study of temperature-dependent spectral dynamics and optical coherence in a mechanically decoupled quantum emitter in hBN. Employing a hybrid stochastic framework that combines Ornstein--Uhlenbeck detuning fluctuations with temperature-dependent, Gaussian-distributed discrete frequency jumps, motivated by experimentally observed spectral diffusion and blinking, we reproduce the measured evolution of inhomogeneous linewidth broadening and the progressive degradation of photon coherence across the relevant cryogenic range (5-30K). The model captures phonon-related spectral diffusion with a cubic temperature dependence and the onset of jump-like spectral instabilities at higher temperatures. By calibrating the hybrid diffusion, jump parameters to the experimentally measured full width at half maximum (FWHM) of the emission line and analyzing the second-order correlation function $g^{(2)}(τ)$ under resonant driving, we establish a unified phenomenological description that links stochastic detuning dynamics to the decay of optical coherence in a resonantly driven emitter. Analysis of $g^{(2)}(τ)$ under resonant driving reveals an additional dephasing rate $γ_{\mathrm{sd+j}}$ that rises monotonically with temperature and drive strength, leading to a predicted critical crossover to overdamped dynamics at $T_{\mathrm{crit}} \approx 25.91$~K. This hybrid framework provides a quantitative connection between accessible spectroscopic observables and the dominant noise mechanisms limiting coherent optical control in mechanically decoupled quantum emitters, exemplified in hBN and generalizable to similar emitters in other materials.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20602v1
- Title: Enhanced quantum parameter estimation based on the Hardy paradox
- Authors: Ming Ji, Yuxiang Yang, Holger F. Hofmann
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20602v1  pdf=https://arxiv.org/pdf/2601.20602v1.pdf

Abstract:
Statistical paradoxes such as the Hardy paradox and the enhancement of phase estimation via post-selection both draw upon the same non-classical features of quantum statistics described by non-positive quasi-probabilities. In this paper, we introduce a post-selected quantum metrology scenario where the initial state, the dynamics associated with the phase shift, and the post-selection are all inspired by the Hardy paradox. Specifically, we identify an anomalous weak value that is characteristic of both the Hardy paradox and the potential enhancement of sensitivity by the post-selection. We find that the efficiency of the enhancement is reduced when the expectation value associated with the anomalous weak value is different from the inverse of this value. We conclude that the relation between enhanced phase estimation and the Hardy paradox requires a detailed understanding of the relation between weak values and expectation values.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20619v1
- Title: Foundations of Quantum Optics for Quantum Information: Crash Course on Nonclassical States and Quantum Correlations
- Authors: Jhoan Eusse, Esteban Vasquez, Tom Rivlin, Elizabeth Agudelo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20619v1  pdf=https://arxiv.org/pdf/2601.20619v1.pdf

Abstract:
Nonclassical states of light and their correlations lie at the heart of quantum optics, serving as fundamental resources that underpin both the exploration of quantum phenomena and the realisation of quantum information protocols. These lecture notes provide an accessible yet rigorous introduction to the foundations of quantum optics, emphasising their relevance to quantum information science and technology. Starting from the quantisation of the electromagnetic field and the bosonic formalism of Fock space, the notes develop a unified framework for describing and analysing quantum states of light. Key families of states -- thermal, coherent, and squeezed -- are introduced as paradigmatic examples illustrating the transition from classical to nonclassical behaviour. The concepts of convexity, classicality, and quasiprobability representations are presented as complementary tools for characterising quantumness and defining operational notions such as P-nonclassicality. The discussion extends naturally to Gaussian states, composite systems, and continuous-variable entanglement, highlighting how nonclassicality serves as a resource for generating and quantifying quantum correlations. Theoretical developments are complemented by computational and experimental perspectives, including simulations of optical states using the Python library Strawberry Fields and data analysis from simulated data. Together, these notes aim to bridge the foundational concepts of quantum optics and modern quantum information, offering both conceptual insight and practical tools for students and researchers entering the field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20631v1
- Title: Rydberg Receivers for Space Applications
- Authors: Gianluca Allinson, Mark Bason, Alexis Bonnin, Sebastian Borówka, Petronilo Martin-Iglesias, Manuel Martin Neira, Mateusz Mazelanik, Richard Murchie, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20631v1  pdf=https://arxiv.org/pdf/2601.20631v1.pdf

Abstract:
Rydberg-atom sensors convert radiofrequency, microwave and terahertz fields into optical signals with SI-traceable calibration, high sensitivity, and broad tunability. This review assesses their potential for space applications by comparing five general architectures (Autler-Townes, AC-Stark, superheterodyne, radiofrequency-to-optical conversion, and fluorescence) against space application needs. We identify promising roles in radiometry, radar, terahertz sensing, and in-orbit calibration, and outline key limitations, including shot noise, sparse terahertz transitions, and currently large Size, Weight, Power and Cost. A staged roadmap highlights which uncertainties should be resolved first and how research organisations, industry and space agencies could take the lead for the different aspects.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20681v1
- Title: Co-Designed Adaptive Quantum State Preparation Protocols
- Authors: Mafalda Ramôa, Luis Paulo Santos, Nicholas J. Mayhall, Edwin Barnes, Sophia E. Economou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20681v1  pdf=https://arxiv.org/pdf/2601.20681v1.pdf

Abstract:
We propose a co-designed variant of ADAPT-VQE (Co-ADAPT-VQE) where the quantum hardware is taken into account in the construction of the ansatz. This framework can be readily used to optimize state preparation circuits for any device, addressing shortcomings such as limited connectivity, short coherence times, and variable gate errors. We exemplify the impact of Co-ADAPT-VQE by creating state preparation circuits for devices with linear nearest-neighbor (LNN) connectivity. We show a reduction of the CNOT count of the final circuits by up to 97% for 12-14 qubit systems, with the impact being greater for larger and more strongly correlated systems. Surprisingly, the circuits created by Co-ADAPT-VQE provide an over 70% CNOT count reduction with respect to the original ADAPT-VQE in all-to-all connectivity, despite being restricted to LNN qubit interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20700v1
- Title: Entangled photon pair excitation and time-frequency filtered multidimensional photon correlation spectroscopy as a probe for dissipative exciton kinetics
- Authors: Arunangshu Debnath, Shaul Mukamel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20700v1  pdf=https://arxiv.org/pdf/2601.20700v1.pdf

Abstract:
In molecular aggregates, multiple delocalized exciton states interact with phonons, making the state-resolved spectroscopic monitoring of dynamics challenging. We propose a protocol that combines photon-entanglement-enhanced narrowband excitation of two-exciton states with time-frequency-filtered two-photon coincidence counting. It can alleviate bottlenecks associated with probing exciton dynamics spread across multiple spectral and temporal windows. We demonstrate that non-classical correlations of entangled photon pairs can be used to prepare narrowband two-exciton population distributions, circumventing transport in mediating states. The distributions thus created can be monitored using time-frequency-filtered photon coincidence counting, and the pathways contributing to photon emission events can be classified by tuning filtering parameters. Numerical simulations for a light-harvesting aggregate highlight the ability of this protocol to achieve selectivity by suppressing or amplifying specific pathways. Combining entangled photonic sources and multidimensional photon counting allow promising applications to spectroscopy and sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20752v1
- Title: Spectrum-generating algebra and intertwiners of the resonant Pais-Uhlenbeck oscillator
- Authors: Andreas Fring, Ian Marquette, Takano Taira
- Categories: quant-ph (primary); quant-ph; hep-th; math-ph
- Links: abs=https://arxiv.org/abs/2601.20752v1  pdf=https://arxiv.org/pdf/2601.20752v1.pdf

Abstract:
We study the quantum Pais-Uhlenbeck oscillator at the resonant (equal-frequency) point, where the dynamics becomes non-diagonalisable and the conventional Fock-space construction collapses. At the classical level, the degenerate system admits more than one Hamiltonian formulation generating the same equations of motion, leading to a nontrivial quantisation ambiguity. Working first in the ghostly two-dimensional Hamiltonian formulation, we construct differential intertwiners that generate a spectrum-generating algebra acting on the generalised eigenspaces of the Hamiltonian. This algebra organises the generalised eigenvectors into finite Jordan chains and closes into a hidden $su(2)$ Lie algebra that exists only at resonance.   We then show that quantising a classically equivalent Hamiltonian yields a radically different quantum theory, with a fully diagonalisable spectrum and genuine degeneracies. Our results demonstrate that the resonant Pais-Uhlenbeck oscillator provides a concrete example in which classically equivalent Hamiltonians define inequivalent quantum theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20782v1
- Title: Neural Quantum States in Mixed Precision
- Authors: Massimo Solinas, Agnes Valenti, Nawaf Bou-Rabee, Roeland Wiersema
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; cs.LG
- Links: abs=https://arxiv.org/abs/2601.20782v1  pdf=https://arxiv.org/pdf/2601.20782v1.pdf

Abstract:
Scientific computing has long relied on double precision (64-bit floating point) arithmetic to guarantee accuracy in simulations of real-world phenomena. However, the growing availability of hardware accelerators such as Graphics Processing Units (GPUs) has made low-precision formats attractive due to their superior performance, reduced memory footprint, and improved energy efficiency. In this work, we investigate the role of mixed-precision arithmetic in neural-network based Variational Monte Carlo (VMC), a widely used method for solving computationally otherwise intractable quantum many-body systems. We first derive general analytical bounds on the error introduced by reduced precision on Metropolis-Hastings MCMC, and then empirically validate these bounds on the use-case of VMC. We demonstrate that significant portions of the algorithm, in particular, sampling the quantum state, can be executed in half precision without loss of accuracy. More broadly, this work provides a theoretical framework to assess the applicability of mixed-precision arithmetic in machine-learning approaches that rely on MCMC sampling. In the context of VMC, we additionally demonstrate the practical effectiveness of mixed-precision strategies, enabling more scalable and energy-efficient simulations of quantum many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20787v1
- Title: Semiclassical effective description of a quantum particle on a sphere with non-central potential
- Authors: Guillermo Chacon-Acosta, H. Hernandez-Hernandez, J. Ruvalcaba-Rascon
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20787v1  pdf=https://arxiv.org/pdf/2601.20787v1.pdf

Abstract:
We develop a semiclassical framework for studying quantum particles constrained to curved surfaces using the momentous quantum mechanics formalism, which extends classical phase-space to include quantum fluctuation variables (moments). In a spherical geometry, we derive quantum-corrected Hamiltonians and trajectories that incorporate quantum back-reaction effects absent in classical descriptions. For the free particle, quantum fluctuations induce measurable phase shifts in azimuthal precession of approximately 8-12%, with uncertainty growth rates proportional to initial moment correlations. When a non-central Makarov potential is introduced, quantum corrections dramatically amplify its asymmetry. For strong coupling ($γ$ = -1.9), the quantum-corrected force drives trajectories preferentially toward the southern hemisphere on timescales 40% shorter than classical predictions, with trajectory densities exhibiting up to 3-fold enhancement in the preferred region. Throughout evolution, the solutions rigorously satisfy Heisenberg uncertainty relations, validating the truncation scheme. These results demonstrate that quantum effects fundamentally alter semiclassical dynamics in curved constrained systems, with direct implications for charge transport in carbon nanostructures, exciton dynamics in curved quantum wells, and reaction pathways in cyclic molecules.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20818v1
- Title: Quantum Memory and Autonomous Computation in Two Dimensions
- Authors: Gesa Dünnweber, Georgios Styliaris, Rahul Trivedi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20818v1  pdf=https://arxiv.org/pdf/2601.20818v1.pdf

Abstract:
Standard approaches to quantum error correction (QEC) require active maintenance using measurements and classical processing. The possibility of passive QEC has so far only been established in an unphysical number of spatial dimensions. In this work, we present a simple method for autonomous QEC in two spatial dimensions, formulated as a quantum cellular automaton with a fixed, local and translation-invariant update rule. The construction uses hierarchical, self-simulating control elements based on the classical schemes from the seminal results of Gács (1986, 1989) together with a measurement-free concatenated code. We analyze the system under a local noise model and prove a noise threshold below which the logical errors are suppressed arbitrarily with increasing system size and the memory lifetime diverges in the thermodynamic limit. The scheme admits a continuous-time implementation as a time-independent, translation-invariant local Lindbladian with engineered dissipative jump operators. Further, the recursive nature of our protocol allows for the fault-tolerant encoding of arbitrary quantum circuits and thus constitutes a self-correcting universal quantum computer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20832v1
- Title: Symplectic Optimization on Gaussian States
- Authors: Christopher Willby, Tomohiro Hashizume, Jason Crain, Dieter Jaksch
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20832v1  pdf=https://arxiv.org/pdf/2601.20832v1.pdf

Abstract:
Computing Gaussian ground states via variational optimization is challenging because the covariance matrices must satisfy the uncertainty principle, rendering constrained or Riemannian optimization costly, delicate, and thus difficult to scale, particularly in large and inhomogeneous systems. We introduce a symplectic optimization framework that addresses this challenge by parameterizing covariance matrices directly as positive-definite symplectic matrices using unit-triangular factorizations. This approach enforces all physical constraints exactly, yielding a globally unconstrained variational formulation of the bosonic ground-state problem. The unconstrained structure also naturally supports solution reuse across nearby Hamiltonians: warm-starting from previously optimized covariance matrices substantially reduces the number of optimization steps required for convergence in families of related configurations, as encountered in crystal lattices, molecular systems, and fluids. We demonstrate the method on weakly dipole-coupled lattices, recovering ground-state energies, covariance matrices, and spectral gaps accurately. The framework further provides a foundation for large-scale approximate treatments of weakly non-quadratic interactions and offers potential scaling advantages through tensor-network enhancements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20860v1
- Title: Quantum teleportation in expanding FRW universe
- Authors: Babak Vakili
- Categories: quant-ph (primary); quant-ph; gr-qc; hep-th
- Links: abs=https://arxiv.org/abs/2601.20860v1  pdf=https://arxiv.org/pdf/2601.20860v1.pdf

Abstract:
We investigate the process of quantum teleportation in an expanding universe modeled by Friedmann-Robertson-Walker spacetime, focusing on two cosmologically relevant scenarios: a power-law expansion and the de Sitter universe. Adopting a field-theoretical approach, we analyze the quantum correlations between two comoving observers who share an entangled mode of a scalar field. Using the Bogoliubov transformation, we compute the teleportation fidelity and examine its dependence on the expansion rate, initial entanglement, and the mode frequency. Our findings indicate that spacetime curvature and the underlying cosmological background significantly affect the efficiency of quantum teleportation, particularly through mode mixing and vacuum structure. We also compare our results with the flat Minkowski case to highlight the role of cosmic expansion in degrading or preserving quantum information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.11738v1
- Title: Multiary gradings
- Authors: Steven Duplij
- Categories: math.RA (primary); math.RA; hep-th; math-ph; math.GR; quant-ph
- Links: abs=https://arxiv.org/abs/2601.11738v1  pdf=https://arxiv.org/pdf/2601.11738v1.pdf

Abstract:
This article develops a comprehensive theory of multiary graded polyadic algebras, extending the classical concept of group-graded algebras to higher-arity structures. We introduce the notion of grading by multiary groups and investigate various compatibility conditions between the arity of algebra operations and grading group operations. Key results include quantization rules connecting arities, classification of graded homomorphisms, and concrete examples including ternary superalgebras and polynomial algebras over $n$-ary matrices. The theory reveals fundamentally new phenomena not present in the binary case, such as the existence of higher power gradings and nontrivial constraints on arity compatibility.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.19979v1
- Title: Exploring the holographic entropy cone via reinforcement learning
- Authors: Temple He, Jaeha Lee, Hirosi Ooguri
- Categories: hep-th (primary); hep-th; cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19979v1  pdf=https://arxiv.org/pdf/2601.19979v1.pdf

Abstract:
We develop a reinforcement learning algorithm to study the holographic entropy cone. Given a target entropy vector, our algorithm searches for a graph realization whose min-cut entropies match the target vector. If the target vector does not admit such a graph realization, it must lie outside the cone, in which case the algorithm finds a graph whose corresponding entropy vector most nearly approximates the target and allows us to probe the location of the facets. For the $\sf N=3$ cone, we confirm that our algorithm successfully rediscovers monogamy of mutual information beginning with a target vector outside the holographic entropy cone. We then apply the algorithm to the $\sf N=6$ cone, analyzing the 6 "mystery" extreme rays of the subadditivity cone from arXiv:2412.15364 that satisfy all known holographic entropy inequalities yet lacked graph realizations. We found realizations for 3 of them, proving they are genuine extreme rays of the holographic entropy cone, while providing evidence that the remaining 3 are not realizable, implying unknown holographic inequalities exist for $\sf N=6$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.19981v1
- Title: Timelike Entanglement Signatures of Ergodicity and Spectral Chaos
- Authors: Rathindra Nath Das, Arnab Kundu, Nemai Chandra Sarkar
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19981v1  pdf=https://arxiv.org/pdf/2601.19981v1.pdf

Abstract:
We investigate timelike entanglement measures derived from the spacetime density kernel in the Rosenzweig-Porter model and show that they sharply diagnose both eigenvector ergodicity and spectral chaos. For several Hilbert-space bipartitions, we compute the second Tsallis entropy, the entanglement imagitivity that quantifies non-Hermiticity, and Schatten-norm diagnostics of the kernel. The imagitivity and Frobenius norm exhibit rapid growth and high late-time plateaus in the ergodic regime, are suppressed in the localized regime, and show intermediate behavior in the fractal phase. The real part of the second Tsallis entropy displays a spectral form factor-like dip-ramp-plateau throughout the chaotic window and a suppressed ramp in the localized regime. We further introduce a kernel negativity, defined as the negative spectral weight of the Hermitian part of the kernel. This negativity equals the trace-norm distance to the set of positive semidefinite operators and the maximal witnessable negative quasiprobability, and its time-averaged value decreases across the ergodic-fractal-localized crossover in close correspondence with the fractal dimension.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.19987v1
- Title: Stability and Decay of Macrovortices in Rotating Bose Gases Beyond Mean Field
- Authors: Paolo Molignini, M. A. Caracanhas, V. S. Bagnato, Barnali Chakrabarti
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.other; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19987v1  pdf=https://arxiv.org/pdf/2601.19987v1.pdf

Abstract:
We study the formation, stability, and decay of macrovortices in a rotating Bose gas confined by a Mexican-hat potential with a multiconfigurational ansatz. By systematically including correlations beyond the mean-field level, we map the equilibrium phase diagram and identify regimes of coexistence between vortex lattices and multiply charge central vortices. Quench dynamics reveals that macrovortices are robust under changes in rotation or interaction strength, sustaining clean monopole oscillations with well-separated, vorticity-dependent breathing frequencies. In contrast, trap quenches trigger a universal decay process mediated by vortex-phonon coupling, in which rotational energy is progressively transferred to compressible modes until the macrovortex splits into singly quantized vortices. Our results demonstrate that macrovortex lifetimes and decay pathways can be tuned by trap confinement, providing experimentally accessible signatures of vortex-phonon interactions and collective energy transfer in correlated quantum fluids.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.19991v1
- Title: Scattering State Theory for One-dimensional Floquet Lattices
- Authors: Ren Zhang, Xiao-Yu Ouyang, Xu-Dong Dai, Xi Dai
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2601.19991v1  pdf=https://arxiv.org/pdf/2601.19991v1.pdf

Abstract:
We develop a Floquet transfer matrix method to solve scattering in extended 1D Floquet lattices, uncovering an underlying conjugate symplectic structure that enforces current conservation across sidebands. By engineering a spatial adiabatic boundary, we suppress multi-channel sideband interference, allowing us to establish a direct mapping between the bulk winding number $C$ and a rigid shift in the transmission energy windows--quantified as $C\hbarω$. We further propose two experimental realizations: cold-atom Bragg scattering to directly verify the transmission shift, and surface-acoustic-wave-induced transport demonstrating the quantized zero-bias current plateau.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20042v1
- Title: Correlated dynamics of three-particle bound states induced by emergent impurities in Bose-Hubbard model
- Authors: Wenduo Zhao, Boning Huang, Yongguan Ke, Chaohong Lee
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20042v1  pdf=https://arxiv.org/pdf/2601.20042v1.pdf

Abstract:
Bound states, known as particles tied together and moving as a whole, are profound correlated effects induced by particle-particle interactions. While dimer-monomer bound states are manifested as a single particle attached to dimer bound pair, it is still unclear about quantum walks and Bloch oscillations of dimer-monomer bound states. Here, we revisit three-particle bound states in the Bose-Hubbard model and find that interaction-induced impurities adjacent to bound pair and boundaries cause two kinds of bound states: one is dimer-monomer bound state and the other is bound edge states. In quantum walks, the spread velocity of dimer-monomer bound state is determined by the maximal group velocity of their energy band, which is much smaller than that in the single-particle case. In Bloch oscillations, the period of dimer-monomer bound states is one third of that in the single-particle case. Our works provide new insights to the collective dynamics of three-particle bound states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20058v1
- Title: Superfluidity in the spin-1/2 XY model with power-law interactions
- Authors: Muhammad Shaeer Moeed, Costanza Pennaforti, Adrian Del Maestro, Roger G. Melko
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.stat-mech; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20058v1  pdf=https://arxiv.org/pdf/2601.20058v1.pdf

Abstract:
In trapped-ion quantum simulators, effective spin-1/2 XY interactions can be engineered via laser-induced coupling between internal atomic states and collective phonon modes. In the simplest one-dimensional ($1d$) traps, these interactions decay as a power-law with distance $1/r^α$, with a tunable exponent $α$. For small $α$, the resulting long-range $1d$ XY model exhibits continuous symmetry breaking, in marked contrast to its nearest neighbor counterpart. In this paper, we examine this model near the phase transition at $α_c$ from the lens of the spin stiffness, or superfluid density. We develop a stochastic series expansion (SSE) quantum Monte Carlo (QMC) simulation and a generalized winding number estimator to measure the superfluid density in the presence of power-law interactions, which we test against exact diagonalization for small lattice sizes. Our results show how conventional superfluidity in the $1d$ XY model is enhanced in the long-range interacting regime. This is observed as a diverging superfluid density as $α\rightarrow 0$ in the thermodynamic limit, which we show is consistent with linear spin-wave theory. Finally, we define a normalized superfluid density estimator that clearly distinguishes the short, medium, and long-range interacting regimes, providing a novel QMC probe of the critical value $α_c$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20166v1
- Title: Complex nonlinear sigma model
- Authors: Kazuki Yamamoto, Kohei Kawabata
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20166v1  pdf=https://arxiv.org/pdf/2601.20166v1.pdf

Abstract:
Motivated by the recent interest in the criticality of open quantum many-body systems, we study nonlinear sigma models with complexified couplings as a general framework for nonunitary field theory. Applying the perturbative renormalization-group analysis to the tenfold symmetric spaces, we demonstrate that fixed points with complex scaling dimensions and critical exponents arise generically, without counterparts in conventional nonlinear sigma models with real couplings. We further clarify the global phase diagrams in the complex-coupling plane and identify both continuous and discontinuous phase transitions. Our work elucidates universal aspects of critical phenomena in complexified field theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20373v1
- Title: Miniatures on Open Quantum Systems
- Authors: Jan Derezinski, Vojkan Jaksic, Claude-Alain Pillet
- Categories: math-ph (primary); math-ph; math.OA; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20373v1  pdf=https://arxiv.org/pdf/2601.20373v1.pdf

Abstract:
We presents a unified and concise exposition of key topics in the mathematical theory of open quantum systems, developed within the framework of operator algebras. The manuscript consolidates and extends a series of invited articles originally prepared for the Modern Encyclopedia of Mathematical Physics, combining foundational material with modern perspectives on non-equilibrium quantum statistical mechanics. After introducing the C*- and W*-algebraic formulation of quantum mechanics, the paper reviews quantum dynamical systems, KMS states, and Tomita-Takesaki modular theory, as well as CCR and CAR algebras for bosonic and fermionic systems. Particular emphasis is placed on infinite systems, non-equilibrium steady states, entropy production, and linear response theory. The later sections develop a systematic treatment of small systems coupled to reservoirs, open lattice quantum spin systems, culminating in a detailed discussion of competing notions of quantum entropy production. The presentation highlights structural insights, conceptual clarity, and connections between equilibrium and non-equilibrium phenomena, providing a self-contained reference for researchers and graduate students in mathematical physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20436v1
- Title: Violation of the Leggett-Garg inequality in photon-graviton conversion
- Authors: Kimihiro Nomura, Akira Taniguchi, Kazushige Ueda
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20436v1  pdf=https://arxiv.org/pdf/2601.20436v1.pdf

Abstract:
The Leggett-Garg inequality (LGI) is a temporal analogue of Bell's inequality and provides a quantitative test of the nonclassicality of a system through its violation. We analytically investigate the violation of the LGI in the context of photon-graviton conversion in a magnetic field background, motivated by its potential applications to testing the nonclassicality of gravity. When gravitational perturbations are quantized as gravitons, the conversion of an initial single photon state gives rise to a superposition of photon and graviton states. We show that the temporal correlations obtained from successive projective measurements on the photon-graviton system violate the LGI. Observation of such a violation would provide a novel avenue for probing the quantum nature of gravity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20474v1
- Title: Critical Charge and Current Fluctuations across a Voltage-Driven Phase Transition
- Authors: José F. B. Afonso, Stefan Kirchner, Pedro Ribeiro
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.mes-hall; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20474v1  pdf=https://arxiv.org/pdf/2601.20474v1.pdf

Abstract:
We investigate bias-driven non-equilibrium quantum phase transitions in a paradigmatic quantum-transport setup: an interacting quantum dot coupled to non-interacting metallic leads. Using the Random Phase Approximation, which is exact in the limit of a large number of dot levels, we map out the zero-temperature non-equilibrium phase diagram as a function of interaction strength and applied bias. We focus our analysis on the behavior of the charge susceptibility and the current noise in the vicinity of the transition. Remarkably, despite the intrinsically non-equilibrium nature of the steady state, critical charge fluctuations admit an effective-temperature description, $T_{\text{eff}}(T,V)$, that collapses the steady-state behavior onto its equilibrium form. In sharp contrast, current fluctuations exhibit genuinely non-equilibrium features: the fluctuation-dissipation ratio becomes negative in the ordered phase, corresponding to a negative effective temperature for the current degrees of freedom. These results establish current noise as a sensitive probe of critical fluctuations at non-equilibrium quantum phase transitions and open new directions for exploring voltage-driven critical phenomena in quantum transport systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20509v1
- Title: Three-body scattering area of identical bosons in two dimensions
- Authors: Junjie Liang, Hongye Yu, Shina Tan
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20509v1  pdf=https://arxiv.org/pdf/2601.20509v1.pdf

Abstract:
We study the wave function $φ^{(3)}$ of three identical bosons scattering at zero energy, zero total momentum, and zero orbital angular momentum in two dimensions, interacting via short-range potentials with a finite two-body scattering length $a$. We derive asymptotic expansions of $φ^{(3)}$ in two regimes: the 111-expansion, where all three pairwise distances are large, and the 21-expansion, where one particle is far from the other two. In the 111-expansion, the leading term grows as $\ln^3(B/a)$ at large hyperradius $B=\sqrt{(s_1^2+s_2^2+s_3^2)/2}$. At order $B^{-2}\ln^{-3}(B/a)$, we identify a three-body parameter $D$ with dimension of length squared, which we term the three-body scattering area. This quantity should be contrasted with the three-body scattering area previously studied for infinite or vanishing two-body scattering length. If the two-body interaction is attractive and supports bound states, $D$ acquires a negative imaginary part, and we derive its relation to the probability amplitudes for the production of two-body bound states in three-body collisions. Under weak modifications of the interaction potentials, we derive the corresponding shift of $D$ in terms of $φ^{(3)}$ and the changes of the two-body and three-body potentials. We also study the effects of $D$ and $φ^{(3)}$ on three-body and many-body physics, including the three-body ground-state energy in a large periodic volume, the many-body energy and the three-body correlation function of the dilute two-dimensional Bose gas, and the three-body recombination rates of two-dimensional ultracold atomic Bose gases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20532v1
- Title: A Unified Symmetry Classification of Many-Body Localized Phases
- Authors: Yucheng Wang
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; cond-mat.quant-gas; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20532v1  pdf=https://arxiv.org/pdf/2601.20532v1.pdf

Abstract:
Anderson localization admits a complete symmetry classification given by the Altland-Zirnbauer (AZ) tenfold scheme, whereas an analogous framework for interacting many-body localization (MBL) has remained elusive. Here we develop a symmetry-based classification of static MBL phases formulated at the level of local integrals of motion (LIOMs). We show that a symmetry is compatible with stable MBL if and only if its action can be consistently represented within a quasi-local LIOM algebra, without enforcing extensive degeneracies or nonlocal operator mixing. This criterion sharply distinguishes symmetry classes: onsite Abelian symmetries are compatible with stable MBL and can host distinct symmetry-protected topological MBL phases, whereas continuous non-Abelian symmetries generically preclude stable MBL. By systematically combining AZ symmetries with additional onsite symmetries, we construct a complete classification table of MBL phases, identify stable, fragile, and unstable classes, and provide representative lattice realizations. Our results establish a unified and physically transparent framework for understanding symmetry constraints on MBL.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20553v1
- Title: Gravitational wave detection via photon-graviton scattering and quantum interference
- Authors: K. Hari, S. Shankaranarayanan
- Categories: gr-qc (primary); gr-qc; hep-th; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20553v1  pdf=https://arxiv.org/pdf/2601.20553v1.pdf

Abstract:
We present a fully quantum field-theoretic framework for gravitational wave (GW) detection in which the interaction is described as photon-graviton scattering. In this picture, the GW acts as a coherent background that induces inelastic energy exchanges with the electromagnetic field - analogous to the Stokes and anti-Stokes shifts in Raman spectroscopy. We propose a detection scheme sensitive to this microscopic mechanism based on Hong-Ou-Mandel interference. We show that the scattering-induced phase shifts render frequency-entangled photon pairs distinguishable, spoiling their destructive quantum interference. GW signal is thus encoded in the modulation of photon coincidence rates rather than classical field intensity, offering a complementary quantum probe of the gravitational universe that recovers the standard classical response in the macroscopic limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20632v1
- Title: Quantum Squeezing Enhanced Photothermal Microscopy
- Authors: Pengcheng Fu, Xiao Liu, Siming Wang, Nan Li, Chenran Xu, Han Cai, Huizhu Hu, Vladislav V. Yakovlev, et al.
- Categories: physics.optics (primary); physics.optics; physics.bio-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20632v1  pdf=https://arxiv.org/pdf/2601.20632v1.pdf

Abstract:
Label-free optical microscopy through absorption or scattering spectroscopy provides fundamental insights across biology and materials science, yet its sensitivity remains fundamentally limited by photon shot noise. While recent demonstrations of quantum nonlinear microscopy show sub-shot-limited sensitivity, they are intrinsically limited by availability of high peak-power squeezed light sources. Here, we introduce squeezing-enhanced photothermal (SEPT) microscopy, a quantum imaging technique that leverages twin-beam quantum correlations to detect absorption induced signals with unprecedented sensitivity. SEPT achieves 3.5 dB noise suppression beyond the standard quantum limit, enabling a 2.5-fold increase in imaging throughput or 31% reduction in pump power, while providing an unmatched versatility through the intrinsic compatibility between continuous-wave squeezing and photothermal modulation. We showcase SEPT applications by providing high-precision characterization of nanoparticles and revealing subcellular structures, such as cytochrome c, that remain undetectable under shot-noise-limited imaging. By combining label-free contrast, quantum-enhanced sensitivity, and compatibility with existing microscopy platforms, SEPT establishes a new paradigm for molecular absorption imaging with far-reaching implications in cellular biology, nanoscience, and materials characterization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20762v1
- Title: A Zero-Range Model for the Efimov Effect in the Born-Oppenheimer Approximation
- Authors: G. Basti, D. Ferretti, A. Teta
- Categories: math-ph (primary); math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20762v1  pdf=https://arxiv.org/pdf/2601.20762v1.pdf

Abstract:
In this note we discuss the Efimov effect emerging in a three-particle quantum system with zero-range interactions. In particular, we consider two non-interacting identical bosons plus a different lighter particle such that the interaction between a boson and the light particle is resonant. We also assume the validity of the Born-Oppenheimer approximation. Under these conditions, we show that the three-particle system exhibits infinitely many negative eigenvalues which accumulate at zero and satisfy the universal geometrical law characterising the Efimov effect. The result we find is a generalisation of previous results recently obtained in [13, 24].

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2601.20768v1
- Title: Millisecond spin coherence of electrons in semiconducting perovskites revealed by spin mode locking
- Authors: Sergey R. Meliakov, Evgeny A. Zhukov, Vasilii V. Belykh, Dmitri R. Yakovlev, Bekir Turedi, Maksym V. Kovalenko, Manfred Bayer
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20768v1  pdf=https://arxiv.org/pdf/2601.20768v1.pdf

Abstract:
Long spin coherence times of carriers are essential for implementing quantum technologies using semiconductor devices for which, however, a possible obstacle is spin relaxation. For the spin dynamics, decisive features are the band structure, crystal symmetry, and quantum confinement. Perovskite semiconductors recently have come into focus of studies of their spin states, notivated by efficient optical access and potentially long-living coherence. Here, we report an electron spin coherence time $T_2$ of the order of 1 ms, measured for a bulk FA$_{0.95}$Cs$_{0.05}$PbI$_3$ lead halide perovskite crystal. Using periodic laser pulses, we synchronize the electron spin Larmor precession about an external magnetic field in an inhomogeneous ensemble, the effect known as spin mode locking. It appears as a decay of the optically created ensemble spin polarization within the dephasing time $T_2^*$ of up to 20 ns and its revival during the spin coherence time $T_2$ reaching the millisecond range. This exceptionally long spin coherence time in a bulk crystal is complemented by millisecond-long longitudinal spin relaxation times $T_1$ for electrons and holes, measured by optically-detected magnetic resonance. These long-lasting spin dynamics highlight perovskites as promising platform for the quantum devices with all-optical control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2407.18087v2
- Title: Stabilization of cat-state manifolds using nonlinear reservoir engineering
- Authors: Ivan Rojkov, Matteo Simoni, Elias Zapusek, Florentin Reiter, Jonathan Home
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2407.18087v2  pdf=https://arxiv.org/pdf/2407.18087v2.pdf

Abstract:
We introduce a novel reservoir engineering approach for stabilizing multi-component Schrödinger's cat manifolds. The fundamental principle of the method lies in the destructive interference at crossings of gain and loss Hamiltonian terms in the coupling of an oscillator to a zero-temperature auxiliary system, which are nonlinear with respect to the oscillator's energy. The nature of these gain and loss terms is found to determine the rotational symmetry, energy distributions, and degeneracy of the resulting stabilized manifolds. Considering these systems as bosonic error-correction codes, we analyze their properties with respect to a variety of errors, including both autonomous and passive error correction, where we find that our formalism gives straightforward insights into the nature of the correction. We give example implementations using the anharmonic laser-ion coupling of a trapped ion outside the Lamb-Dicke regime as well as nonlinear superconducting circuits. Beyond the dissipative stabilization of standard cat manifolds and novel rotation symmetric codes, we demonstrate that our formalism allows for the stabilization of bosonic codes linked to cat states through unitary transformations, such as quadrature-squeezed cats. Our work establishes a design approach for creating and utilizing codes using nonlinearity, providing access to novel quantum states and processes across a range of physical systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2410.13740v4
- Title: Solving Helmholtz problems with finite elements on a quantum annealer
- Authors: Arnaud Rémi, François Damanet, Christophe Geuzaine
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2410.13740v4  pdf=https://arxiv.org/pdf/2410.13740v4.pdf

Abstract:
Solving Helmholtz problems using finite elements leads to the resolution of a linear system which is challenging to solve for classical computers. In this paper, we investigate how quantum annealers could address this challenge. We first express the linear system arising from the Helmholtz problem as a generalized eigenvalue problem (gEVP). The obtained gEVP is mapped into quadratic unconstrained binary optimization problems (QUBOs) which we solve using an adaptive quantum annealing eigensolver (AQAE) and its classical equivalent. We identify two key parameters in the success of AQAE for solving Helmholtz problems: the system condition number and the integrated control errors (ICE) in the quantum hardware. Our results show that a large system condition number implies a finer discretization grid for AQAE to converge, leading to a variable overhead, and that AQAE is either tolerant or not with respect to ICE depending on the gEVP. Finally, we establish lower bounds on the annealing time, narrowing the possibility of a quantum advantage for solving Helmholtz problems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2410.22630v3
- Title: Multipartite quantum states over time from two fundamental assumptions
- Authors: Seok Hyung Lie, James Fullwood
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2410.22630v3  pdf=https://arxiv.org/pdf/2410.22630v3.pdf

Abstract:
The theory of quantum states over time extends the density operator formalism into the temporal domain, providing a unified of treatment of timelike and spacelike separated systems in quantum theory. Although recent results have characterized quantum states over time involving two timelike separated systems, it remains unclear how to consistently extend the notion of quantum states over time to multipartite temporal scenarios, such as those considered in studies of Leggett-Garg inequalities. In this Letter, we show that two simple assumptions uniquely single out the Markovian multipartite extension of bipartite quantum states over time, namely, linearity in the initial state and a quantum analog of conditionability for multipartite probability distributions. As a direct consequence of our result, we establish a canonical correspondence between multipartite QSOTs and Kirkwood-Dirac type quasiprobability distributions, which we show opens up the possibility of experimentally verifying the temporal correlations encoded in QSOTs via the recent experimental technique of simulating quasiprobability known as quantum snapshotting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2501.05355v3
- Title: Blind calibration of a quantum computer
- Authors: Liam M. Jeanette, Jadwiga Wilkens, Ingo Roth, Anton Than, Alaina M. Green, Dominik Hangleiter, Norbert M. Linke
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2501.05355v3  pdf=https://arxiv.org/pdf/2501.05355v3.pdf

Abstract:
The calibration of quantum measurements is limited by the ability to accurately prepare quantum states under unknown device errors. We develop an accurate calibration protocol for the measurement apparatus of a quantum computer that is `blind' to the state preparation. Blind calibration quantifies and corrects measurement errors from simple tomographic data on a noisy quantum state. Importantly, it calibrates multiple error mechanisms in a single experiment, eliminating the need for bespoke, separate calibration experiments. Using a trapped-ion quantum computer, we systematically demonstrate the accuracy of the method. We use blind calibration to estimate the native calibration parameters of the experimental system. The recovered calibrations are consistent with directly measured values and perform similarly in predicting the state properties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2503.09333v3
- Title: Unification of stochastic matrices and quantum operations for N-level systems
- Authors: Bilal Canturk
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.09333v3  pdf=https://arxiv.org/pdf/2503.09333v3.pdf

Abstract:
The time evolution of the one-point probability vector of stochastic processes and quantum processes for $N$-level systems have been unified. Hence, quantum states and quantum operations can be regarded as generalizations of the one-point probability vectors and stochastic matrices, respectively. More essentially, based on the unification, it has been proven that completely positive divisibility (CP-divisibility) for quantum operations is the natural extension of the Chapman-Kolmogorov equation. It is thus shown that CP-divisibility is a necessary but insufficient condition for a quantum process to be specified as Markovian. The main results have been illustrated through a dichotomic Markov process.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2504.08174v2
- Title: Downloading many-qubit entanglement from continuous-variable cluster states
- Authors: Zhihua Han, Hoi-Kwan Lau
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.08174v2  pdf=https://arxiv.org/pdf/2504.08174v2.pdf

Abstract:
Many-body entanglement is an essential resource for many quantum technologies, but its scalable generation has been challenging on qubit platforms. However, the generation of continuous-variable (CV) entanglement can be extremely efficient, but its utility is rather limited. In this work, we propose a scheme to combine the best of both qubit and CV approaches: a systematic method to download useful many-qubit entanglement from the efficiently generated CV cluster states. Our protocol is based on one-bit teleportation of the qubit correlation encoded in the displaced Gottesman-Kitaev-Preskill basis. To characterize the practical performance of our scheme, we develop an equivalent circuit to map dominant CV errors to single-qubit preparation errors. Particularly, we relate finite squeezing error to qubit erasure, and show that only 5.4 dB squeezing is sufficient to implement robust qubit memory or quantum computation (QC), and 11.9 dB for fault-tolerant QC. Our protocol can be implemented with the operations that are common in many bosonic platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2504.10349v2
- Title: Trapping potentials and quantum gates for microwave-dressed Rydberg atoms on an atom chip
- Authors: Iason Tsiamis, Georgios Doultsinos, Andreas F. Tzortzakakis, Manuel Kaiser, Dominik Jakab, Andreas Günther, József Fortágh, David Petrosyan
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2504.10349v2  pdf=https://arxiv.org/pdf/2504.10349v2.pdf

Abstract:
Rydberg atoms in dc electric fields acquire static dipole moments. When the atoms are close to a surface producing an inhomogeneous electric field, such as by the adsorbates on an atom chip, depending on the sign of the dipole moment of the Rydberg-Stark eigenstate, the atoms may experience a force toward or away from the surface. We show that by applying a bias electric field and coupling a desired Rydberg state by a microwave field of proper frequency to another Rydberg state with opposite sign of the dipole moment, we can create a trapping potential for the atom at a prescribed distance from the surface. Perfectly overlapping trapping potentials for several Rydberg states can also be created by multicomponent microwave fields. A pair of such trapped Rydberg states of an atom can represent a qubit. Finally, we discuss an optimal realization of the SWAP gate between pairs of such atomic Rydberg qubits separated by a large distance but interacting with a common mode of a planar microwave resonator at finite temperature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2505.22734v2
- Title: Connectivity determines the capability of sparse neural network quantum states
- Authors: Brandon Barton, Juan Carrasquilla, Christopher Roth, Agnes Valenti
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2505.22734v2  pdf=https://arxiv.org/pdf/2505.22734v2.pdf

Abstract:
The Lottery Ticket Hypothesis (LTH) posits that within overparametrized neural networks, there exist sparse subnetworks that are capable of matching the performance of the original model when trained in isolation from the original initialization. We extend this hypothesis to the unsupervised task of approximating the ground state of quantum many-body Hamiltonians, a problem equivalent to finding a neural-network compression of the lowest-lying eigenvector of an exponentially large matrix. Focusing on two representative quantum Hamiltonians, the transverse field Ising model (TFIM) and the toric code (TC), we demonstrate that sparse neural networks can reach accuracies comparable to their dense counterparts, even when pruned by more than an order of magnitude in parameter count. Crucially, and unlike the original LTH, we find that performance depends only on the structure of the sparse subnetwork, not on the specific initialization, when trained in isolation. Moreover, we identify universal scaling behavior that persists across network sizes and physical models, where the boundaries of scaling regions are determined by the underlying Hamiltonian. At the onset of high-error scaling, we observe signatures of a sparsity-induced quantum phase transition that is first-order in shallow networks. Finally, we demonstrate that pruning enhances interpretability by linking the structure of sparse subnetworks to the underlying physics of the Hamiltonian.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2506.12946v2
- Title: Robust certification of quantum instruments through a sequential communication game
- Authors: Pritam Roy, Subhankar Bera, A. S. Majumdar, Shiladitya Mal
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.12946v2  pdf=https://arxiv.org/pdf/2506.12946v2.pdf

Abstract:
We propose a communication game in the sequential measurement scenario, involving a sender and two receivers with restricted communication among the latter parties. In the framework of the prepare-transform-measure scenario, we find a prominent quantum advantage in the receiver's decoding of the message originally encoded by the sender. We show that an optimal trade-off between the success probabilities of the two receivers enables self-testing of the sender's state preparation, the first receiver's instruments, and the measurement device of the second receiver in a semi-device-independent way. Our protocol enables a more robust certification of the unsharp measurement parameter of the first receiver compared to an earlier protocol. We further generalize our game to higher-dimensional systems, revealing greater quantum advantage with an increase in dimensions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2506.21707v2
- Title: Optimizing continuous-time quantum error correction for arbitrary noise
- Authors: Anirudh Lanka, Shashank Hegde, Todd A. Brun
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.21707v2  pdf=https://arxiv.org/pdf/2506.21707v2.pdf

Abstract:
We present a protocol using machine learning (ML) to simultaneously optimize the quantum error-correcting code space and the corresponding recovery map in the framework of continuous-time quantum error correction. Given a Hilbert space and a noise process -- potentially correlated across both space and time -- the protocol identifies the optimal recovery strategy, measured by the average logical state fidelity. This approach enables the discovery of recovery schemes tailored to arbitrary device-level noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2507.01720v4
- Title: Laser cooling and qubit measurements on a forbidden transition in neutral Cs atoms
- Authors: J. Scott, H. M. Lim, U. Singla, Q. Meece, C. Fang, J. T. Choy, S. Kolkowitz, T. M. Graham, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.01720v4  pdf=https://arxiv.org/pdf/2507.01720v4.pdf

Abstract:
We experimentally demonstrate background-free, hyperfine-level-selective measurements of individual Cs atoms by simultaneous cooling to $5.3~μ\rm K$ and imaging on the $6s_{1/2}\rightarrow 5d_{5/2}$ electric-quadrupole transition. We achieve hyperfine resolved detection with fidelity 0.9993(4) and atom retention of 0.9954(5), limited primarily by vacuum lifetime. Performing state measurements in a 3D cooling configuration enables repeated low loss measurements. A theoretical analysis of an extension of the demonstrated approach based on quenching of the excited state with an auxiliary field, identifies parameters for hyperfine-resolved measurements with a projected fidelity of $\sim 0.9995 $ in $\sim 60~μ\rm s$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2507.07904v3
- Title: Testing time order and Leggett-Garg inequalities with noninvasive measurements on public quantum computers
- Authors: Tomasz Rybotycki, Tomasz Białecki, Josep Batle, Bartłomiej Zglinicki, Adam Szereszewski, Wolfgang Belzig, Adam Bednorz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.07904v3  pdf=https://arxiv.org/pdf/2507.07904v3.pdf

Abstract:
We demonstrate the first violation of the Leggett-Garg inequality and time-order noninvariance on public quantum computers using genuine noninvasive measurements. By gathering sufficiently large statistics, we have been able to violate Leggett-Garg inequality and time-order invariance. The detailed analysis of the data on 10 qubit sets from 5 devices available on IBM Quantum and one on IonQ reveals violations beyond 5 standard deviations in almost all cases. We implemented our protocols using fractional gates, newly available on the IBM Heron devices, allowing us to benchmark them in application to weak measurements. The noninvasiveness is supported by a qualitative and quantitative agreement with the model of weak disturbance. Moreover, our data expose statistically significant deviations from theoretical predictions that exceed declared device error rates, establishing weak measurement protocols as a sensitive benchmark for quantum hardware. These advances transform public quantum computers into practical testbeds for probing foundational questions of realism and temporal order with unprecedented accessibility and precision.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2508.11765v2
- Title: The Role of Quantum Computing in Advancing Scientific High-Performance Computing: A perspective from the ADAC Institute
- Authors: Gilles Buchs, Thomas Beck, Ryan Bennink, Daniel Claudino, Andrea Delgado, Nur Aiman Fadel, Peter Groszkowski, Kathleen Hamilton, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.11765v2  pdf=https://arxiv.org/pdf/2508.11765v2.pdf

Abstract:
Quantum computing (QC) has gained significant attention over the past two decades due to its potential for speeding up classically demanding tasks. This transition from an academic focus to a thriving commercial sector is reflected in substantial global investments. While advancements in qubit counts and functionalities continues at a rapid pace, current quantum systems still lack the scalability for practical applications, facing challenges such as too high error rates and limited coherence times. This perspective paper examines the relationship between QC and high-performance computing (HPC), highlighting their complementary roles in enhancing computational efficiency. It is widely acknowledged that even fully error-corrected QCs will not be suited for all computational task. Rather, future compute infrastructures are anticipated to employ quantum acceleration within hybrid systems that integrate HPC and QC. While QCs can enhance classical computing, traditional HPC remains essential for maximizing quantum acceleration. This integration is a priority for supercomputing centers and companies, sparking innovation to address the challenges of merging these technologies. The Accelerated Data Analytics and Computing Institute (ADAC) is comprised of globally leading HPC centers. ADAC has established a Quantum Computing Working Group to promote and catalyze collaboration among its members. This paper synthesizes insights from the QC Working Group, supplemented by findings from a member survey detailing ongoing projects and strategic directions. By outlining the current landscape and challenges of QC integration into HPC ecosystems, this work aims to provide HPC specialists with a deeper understanding of QC and its future implications for computationally intensive endeavors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2508.16382v2
- Title: Parrondo paradox in quantum image encryption
- Authors: Łukasz Pawela
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.16382v2  pdf=https://arxiv.org/pdf/2508.16382v2.pdf

Abstract:
We present a quantum image encryption protocol that harnesses discrete-time quantum walks (DTQWs) on cycles and explicitly examines the role of the Parrondo paradox in security. Using the NEQR representation, a DTQW-generated probability mask is transformed into a quantum key image and applied via CNOT to encrypt grayscale images. We adopt an efficient circuit realization of DTQWs based on QFT-diagonalization and coin-conditioned phase layers, yielding low depth for \(N=2^n\) positions and \(t\) steps. On \(64\times 64\) benchmark images, the scheme suppresses adjacent-pixel correlations to near zero after encryption (e.g., \(|C_H|, |C_V|, |C_D| \approx 10^{-2}\)), produces nearly uniform histograms, and achieves high ciphertext entropy close to the 8-bit ideal. Differential analyses further indicate strong diffusion and confusion: NPCR exceeds \(99\%\) and UACI is around \(30\%\), consistent with robust sensitivity to small plaintext changes. Crucially, we investigate the impact of the Parrondo paradox on encryption quality and demonstrate that our fully unitary protocol remains robust even in paradoxical regimes. We show that while the paradox can introduce biases in simpler measurement-based schemes, our integrated approach -- incorporating spatial diffusion and position-color entanglement -- effectively leverages the complex interference patterns of the Parrondo walk to enhance substitution, maintaining high entropy and low correlations. Our results provide a performant DTQW-based quantum image cipher and confirm the suitability of paradoxical dynamics for secure quantum image processing. We discuss implications for hardware implementations and extensions to higher-dimensional walks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2509.02674v2
- Title: The Munich Quantum Software Stack: Connecting End Users, Integrating Diverse Quantum Technologies, Accelerating HPC
- Authors: Lukas Burgholzer, Jorge Echavarria, Patrick Hopf, Yannick Stade, Damian Rovara, Ludwig Schmid, Ercüment Kaya, Burak Mete, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.02674v2  pdf=https://arxiv.org/pdf/2509.02674v2.pdf

Abstract:
Quantum computing is advancing rapidly in hardware and algorithms, but broad accessibility demands a comprehensive, efficient, unified software stack. Such a stack must flexibly span diverse hardware and evolving algorithms, expose usable programming models for experts and non-experts, manage resources dynamically, and integrate seamlessly with classical High-Performance Computing (HPC). As quantum systems increasingly act as accelerators in hybrid workflows -- ranging from loosely to tightly coupled -- few full-featured implementations exist despite many proposals.   We introduce the Munich Quantum Software Stack (MQSS), a modular, open-source, community-driven ecosystem for hybrid quantum-classical applications. MQSS's multi-layer architecture executes high-level applications on heterogeneous quantum back ends and coordinates their coupling with classical workloads. Core elements include front-end adapters for popular frameworks and new programming approaches, an HPC-integrated scheduler, a powerful MLIR-based compiler, and a standardized hardware abstraction layer, the Quantum Device Management Interface (QDMI). While under active development, MQSS already provides mature concepts and open-source components that form the basis of a robust quantum computing software stack, with a forward-looking design that anticipates fault-tolerant quantum computing, including varied qubit encodings and mid-circuit measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2510.08687v3
- Title: False Positives Raised by Quantum Readout Error Mitigation
- Authors: Yibin Guo, Yi Fan, Pei Liu, Shoukuan Zhao, Yirong Jin, Xiaoxia Cai, Xiongzhi Zeng, Zhenyu Li, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.08687v3  pdf=https://arxiv.org/pdf/2510.08687v3.pdf

Abstract:
Quantum readout error mitigation is essential for noisy intermediate-scale quantum devices to achieve reliable data. The conventional approaches, conflating initialization errors with measurement errors, not only suppress the influence of measurement errors, but also strengthen that of initialization errors, which is a systematic bias grows exponentially with the qubit number. Here, we have proved that this effect causes severe fidelity overestimation for all stabilizer states and might lead to false positives in large-scale entangled state characterization. Similarly, the results from algorithms like the variational quantum eigensolver and time evolution also deviate negatively, and cover up other errors in the quantum circuit. These findings highlight the critical need for rigorous benchmarking and careful management of initialization errors. Consequently, we establish an upper bound for the tolerable initialization error rate to ensure effective error mitigation at a given system scale.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2510.09765v2
- Title: Bounds in the Projective Unitary Group with Respect to Global Phase Invariant Metric
- Authors: Bhanu Pratap Yadav, Mahdi Bayanifar, Olav Tirkkonen
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2510.09765v2  pdf=https://arxiv.org/pdf/2510.09765v2.pdf

Abstract:
We consider a global phase-invariant metric in the projective unitary group PUn, relevant for universal quantum computing. We obtain the volume and measure of small metric ball in PUn and derive the Gilbert-Varshamov and Hamming bounds in PUn. In addition, we provide upper and lower bounds for the kissing radius of the codebooks in PUn as a function of the minimum distance. Using the lower bound of the kissing radius, we find a tight Hamming bound. Also, we establish bounds on the distortion-rate function for quantizing a source uniformly distributed over PUn. As example codebooks in PUn, we consider the projective Pauli and Clifford groups, as well as the projective group of diagonal gates in the Clifford hierarchy, and find their minimum distances. For any code in PUn with given cardinality we provide a lower bound of covering radius. Also, we provide expected value of the covering radius of randomly distributed points on PUn, when cardinality of code is sufficiently large. We discuss codebooks at various stages of the projective Clifford + T and projective Clifford + S constructions in PU2, and obtain their minimum distance, distortion, and covering radius. Finally, we verify the analytical results by simulation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2512.05440v2
- Title: Concentrated Monte Carlo sampling for local observables in quantum spin chains
- Authors: Wenxuan Zhang, Dingzu Wang, Dario Poletti
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2512.05440v2  pdf=https://arxiv.org/pdf/2512.05440v2.pdf

Abstract:
Monte Carlo methods are widely used to estimate observables in many-body quantum systems. However, conventional sampling schemes often require a large number of samples to achieve sufficient accuracy. In this work we propose the concentrated Monte Carlo sampling approach, which builds on the idea that in systems with only short range correlations, to obtain accurate expectation values for local observables, one would favor detailed information in the surroundings of this observable compared to far away from it. In this approach we consider all possible configurations in the surroundings of a local observable, and unique samples from the remaining of the setup drawn using Markov chain Monte Carlo. We have tested the performance of this approach for ground states of the spin-1/2 tilted Ising model in different phases, and also for thermal states in the a spin-1 bilinear-biquadratic model. Our results demonstrate that CMCS yields higher accuracy for local observables in short-range correlated states while requiring substantially fewer samples, showcasing in which regimes one can obtain acceleration for the evaluation of expectation values.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2512.15838v2
- Title: Low-Latency FPGA Control System for Real-Time Neural Network Processing in CCD-Based Trapped-Ion Qubit Measurement
- Authors: Binglei Lou, Gautham Duddi Krishnaswaroop, Filip Wojcicki, Ruilin Wu, Richard Rademacher, Zhiqiang Que, Wayne Luk, Philip H. W. Leong
- Categories: quant-ph (primary); quant-ph; cs.AR
- Links: abs=https://arxiv.org/abs/2512.15838v2  pdf=https://arxiv.org/pdf/2512.15838v2.pdf

Abstract:
Accurate and low-latency qubit state measurement is critical for trapped-ion quantum computing. While deep neural networks (DNNs) have been integrated to enhance detection fidelity, their latency performance on specific hardware platforms remains underexplored. This work benchmarks the latency of DNN-based qubit detection on field-programmable gate arrays (FPGAs) and graphics processing units (GPUs). The FPGA solution directly interfaces an electron-multiplying charge-coupled device (EMCCD) with the subsequent data processing logic, eliminating buffering and interface overheads. As a baseline, the GPU-based system employs a high-speed PCIe image grabber for image input and I/O card for state output. We deploy Multilayer Perceptron (MLP) and Vision Transformer (ViT) models on hardware to evaluate measurement performance. Compared to conventional thresholding, DNNs reduce the mean measurement fidelity (MMF) error by factors of 1.8-2.5x (one-qubit case) and 4.2-7.6x (three-qubit case). FPGA-based MLP and ViT achieve nanosecond- and microsecond-scale inference latencies, while the complete single-shot measurement process achieves over 100x speedup compared to the GPU implementation. Additionally, clock-cycle-level signal analysis reveals inefficiencies in EMCCD data transmission via Cameralink, suggesting that optimizing this interface could further leverage the advantages of ultra-low-latency DNN inference, guiding the development of next-generation qubit detection systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2512.24950v2
- Title: An uncertainty relation in the case of four observables
- Authors: Minyi Huang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.24950v2  pdf=https://arxiv.org/pdf/2512.24950v2.pdf

Abstract:
Uncertainty is a fundamental and important concept in quantum mechanics. In this work, using the technique in matrix theory, we propose an uncertainty relation of four observables and show that the uncertainty constant is tight. It is argued that this method can deal with the several known uncertainty relations for two, three and four observables in a unified way. The result is also compared with other uncertainty relations of four observables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2411.03564v2
- Title: Optimization-based hologram design for fine optical tweezer arrays and extension of super-resolution criteria
- Authors: Keisuke Nishimura, Hiroto Sakai, Takafumi Tomita, Sylvain de Léséleuc, Taro Ando
- Categories: physics.optics (primary); physics.optics; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2411.03564v2  pdf=https://arxiv.org/pdf/2411.03564v2.pdf

Abstract:
Aligning light spots into arbitrary shapes is a fundamental challenge in holography, leading to various applications across diverse fields in science and engineering. However, as the spot interval approaches the wavelength of light, interference effects among the spots become prominent, which complicates the generation of a distortion-free alignment. Herein, we introduce a hologram design method based on the optimisation of a nonlinear cost function using a holographic phase pattern as the optimisation parameter. We confirmed a spot interval of 0.952(1) $μ$m in a $5 \times 5$ multispot pattern on the focal plane of a high-numerical-aperture (0.75) objective by observing the near-infrared (wavelength: 820 nm) holographic output light from a spatial light modulator device, a result which overcomes the limitation of a few micrometres under similar conditions. Furthermore, the definition of the Rayleigh diffraction limit is refined by considering the separation of spots and the spot interval, thereby concluding the achievement of "super-resolution." The proposed method is expected to advance laser fabrication, scanning laser microscopy, and cold atom physics, among other fields.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2411.09409v4
- Title: Post-Newtonian Effective Field Theory Approach to Entanglement Harvesting, Quantum Discord and Bell's Nonlocality Bound Near a Black Hole
- Authors: Feng-Li Lin, Sayid Mondal
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2411.09409v4  pdf=https://arxiv.org/pdf/2411.09409v4.pdf

Abstract:
Black holes, as characterized by the Hawking effect and Bekenstein-Hawking entropy, can be treated as a compact object carrying nontrivial quantum information obscured behind the event horizon. Thus, the black hole may convey and retract its quantum information to the nearby quantum probes via the surrounding mediator fields. In this paper, we investigate the effects of a quantum black hole on the reduced states of a pair of static qubit-type Unruh-DeWitt (UDW) detectors acting as a probe, using three complementary quantum information measures: concurrence characterizing entanglement harvesting, quantum discord, and Bell's nonlocality bound. This sheds light on the nature of the quantum state of the black holes. By treating the black hole as a tidally deformable thermal body under the quantum fluctuation of the mediator fields as observed in \cite{Goldberger:2019sya, goldberger2020virtual, biggs2024comparing}, we employ a post-Newtonian effective field theory (PN-EFT) to derive the reduced states of the UDW probes analytically. Based on this, we can easily obtain all three quantum information measures without encountering the complicated Matsubara sum of infinite thermal poles, as in the conventional approach based on quantum fields in curved spacetime. By tuning the relative strengths in the action of PN-EFT, we can extract the effects of the black hole on the entanglement, quantum correlation, and nonlocality bound of the UDW probe systems. Our PN-EFT approach can be extended to include the backreaction on the black holes in future studies by taking the higher-order PN corrections into account.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2412.17801v2
- Title: Observation of emergent scaling of spin-charge correlations at the onset of the pseudogap
- Authors: Thomas Chalopin, Petar Bojović, Si Wang, Titus Franz, Aritra Sinha, Zhenjiu Wang, Dominik Bourgund, Johannes Obermeyer, et al.
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2412.17801v2  pdf=https://arxiv.org/pdf/2412.17801v2.pdf

Abstract:
In strongly correlated materials, interacting electrons are entangled and form collective quantum states, resulting in rich low-temperature phase diagrams. Notable examples include cuprate superconductors, in which superconductivity emerges at low doping out of an unusual "pseudogap" metallic state above the critical temperature. The Fermi-Hubbard model, describing a wide range of phenomena associated with strong electron correlations, still offers major computational challenges despite its simple formulation. In this context, ultracold atoms quantum simulators have provided invaluable insights into the microscopic nature of correlated quantum states. Here, we use a quantum gas microscope Fermi-Hubbard simulator to explore a wide range of dopings and temperatures in a regime where a pseudogap is known to develop. By measuring multi-point correlation functions up to fifth order, we uncover a novel universal scaling behaviour in magnetic and higher-order spin-charge correlations characterised by a doping-dependent temperature scale. Accurate comparisons with determinant Quantum Monte Carlo and Minimally Entangled Typical Thermal States simulations confirm that this temperature scale is comparable to the pseudogap temperature T*. Our quantitative findings reveal a novel qualitative behaviour of magnetic properties and spin-charge correlations in an emergent pseudogap and pave the way towards the exploration of charge pairing and collective phenomena expected at lower temperatures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2501.08839v3
- Title: Classical and quantum chaos in bean- and peanut-shaped billiards
- Authors: Pranaya Pratik Das, Tanmayee Patra, Biplab Ganguli
- Categories: nlin.CD (primary); nlin.CD; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2501.08839v3  pdf=https://arxiv.org/pdf/2501.08839v3.pdf

Abstract:
The boundary of a billiard system plays a crucial role in shaping its dynamics, which may be integrable, mixed, or fully chaotic. When a boundary has varying curvature, it offers a unique setting to study the relation between classical chaos and quantum behaviour. In this study, we introduce two geometrically distinct billiards: a bean- and a peanut-shaped billiard. These systems incorporate both focusing and defocusing walls with no neutral segments. Our study reveals a strong correlation between classical and quantum dynamics. Analysis of billiard flow diagrams confirms sensitivity to initial conditions-a defining feature of chaos. Poincaré maps further show the phase space intricately woven with regions of chaotic motion and stability islands. We employ both statistical and dynamical measures to characterise quantum chaos. Statistical indicator includes nearest-neighbour spacing distribution, level spacing ratios, and spectral staircase function, while dynamical measures includes out-of-time-order correlators and spectral complexity. We also observe eigenfunction scarring in both the billiards.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2503.07804v5
- Title: Achievable Rate Regions for Multi-terminal Quantum Channels via Coset Codes
- Authors: Fatma Gouiaa, Arun Padakandla
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2503.07804v5  pdf=https://arxiv.org/pdf/2503.07804v5.pdf

Abstract:
We undertake a Shannon theoretic study of the problem of communicating bit streams over a 3-user quantum interference channel (QIC) and focus on characterizing inner bounds. Adopting the powerful technique of tilting, smoothing, and augmentation discovered by Sen recently, and combining with our coset code strategy, we derive a new inner bound to the classical-quantum capacity region of a 3-user QIC. The derived inner bound subsumes all currently known bounds and is proven to be strictly larger for identified examples.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2504.09610v4
- Title: Q-ball mechanism of electron transport properties of high-T$_c$ superconductors
- Authors: S. I. Mukhin
- Categories: cond-mat.supr-con (primary); cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2504.09610v4  pdf=https://arxiv.org/pdf/2504.09610v4.pdf

Abstract:
A theory is presented of a mechanism of high-Tc superconductivity in cuprates, based on the fact that 'nested' fermionic states near the Fermi surface of electrons/holes cause instability with respect to formation of the Q-balls (nontopological solitons) of coherently condensed spin/charge density wave fluctuations (SDW/CDW) with the wave-vector that matches the 'nesting' one. Simultaneously, the 'nested' fermions form superconducting condensate of Cooper/local pairs inside the Q-balls, with Q-ball SDW/CDW field being a 'pairing glue'. Thus, Q-balls possess lower total energy with respect to not condensed thermal SDW/CDW fluctuations and form a Q-balls 'gas' via first order phase transition below a temperature T$^*$. Besides, superconducting condensates inside the Q-balls induce a spectral gap on the nested parts of the Fermi surface, thus creating pseudogap phase. The Q-ball semiclassical field breaks chiral symmetry along the Matsubara time axis in Euclidean space-time possessing conserved Noether "charge" Q that makes the Q-ball volume finite. Prediction of the Q-ball scenario in cuprates is supported by micro X-ray diffraction data in HgBa$_2$CuO$_{4+y}$ in the pseudogap phase. The Q-balls of baryonic fields were originally predicted in Minkowski space-time by Sidney Coleman. In this paper it is demonstrated analytically that scattering of itinerant fermions on the Q-balls causes linear temperature dependence of electrical resistivity, that may explain famous 'Plankian' behavior in the 'strange metal' phase of high-Tc cuprates. Calculated diamagnetic response of Q-balls gas in the 'strange metal' phase and the phase diagram of high-Tc cuprates, with superconducting dome touching the 'strange metal' area at the optimal (holes)doping, are also in qualitative accord with experimental data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2504.19512v3
- Title: Gapped Boundaries of Kitaev's Quantum Double Models: A Lattice Realization of Anyon Condensation from Lagrangian Algebras
- Authors: Mu Li, Xiao-Han Yang, Xiao-Yu Dong
- Categories: cond-mat.str-el (primary); cond-mat.str-el; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2504.19512v3  pdf=https://arxiv.org/pdf/2504.19512v3.pdf

Abstract:
The macroscopic theory of anyon condensation, rooted in the categorical structure of topological excitations, provides a complete classification of gapped boundaries in topologically ordered systems, where distinct boundaries correspond to the condensation of different Lagrangian algebras. However, an intrinsic and direct understanding of anyon condensation in lattice models, grounded in the framework of Lagrangian algebras, remains undeveloped. In this paper, we propose a systematic framework for constructing all gapped boundaries of Kitaev's quantum double models directly from the data of Lagrangian algebras. Central to our approach is the observation that bulk interactions in the quantum double models admit two complementary interpretations: the anyon-creating picture and the anyon-probing picture. Generalizing this insight to the boundary, we derive the consistency condition for boundary ribbon operators that respect the mathematical axiomatic structure of Lagrangian algebras. Solving these conditions yields explicit expressions for the local boundary interactions required to realize gapped boundaries. We also provide three families of solutions that cover a broad range of cases. Our construction provides a microscopic characterization of the bulk-to-boundary anyon condensation dynamics via the action of ribbon operators. Moreover, all these boundary terms are supported within a common effective Hilbert space, making further studies on pure boundary phase transitions natural and convenient. Given the broad applicability of anyon condensation theory, we believe that our approach can be generalized to planar topological codes, extended string-net models, or higher-dimensional topologically ordered systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2506.17385v2
- Title: Magnetic Levitation as a New Probe of Non-Newtonian Gravity
- Authors: Dorian W. P. Amaral, Tim M. Fuchs, Hendrik Ulbricht, Christopher D. Tunnell
- Categories: hep-ph (primary); hep-ph; gr-qc; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2506.17385v2  pdf=https://arxiv.org/pdf/2506.17385v2.pdf

Abstract:
We present MORRIS (Magnetic Oscillatory Resonator for Rare-Interaction Studies) and propose the first tabletop search for non-Newtonian gravity due to a Yukawa-like fifth force using a magnetically levitated particle. Our experiment comprises a levitated sub-millimeter magnet in a superconducting trap that is driven by a time-periodic source. Featuring short-, medium-, and long-term stages, MORRIS will admit increasing sensitivities to the force coupling strength $α$, optimally probing screening lengths of $λ\sim 1\,\mathrm{mm}$. Our short-term setup provides a proof-of-principle study, with our medium- and long-term stages respectively constraining $α\lesssim 10^{-4}$ and $α\lesssim 10^{-5}$, leading over existing bounds. Our projections are readily recastable to concrete models predicting the existence of fifth forces, and our statistical analysis is generally applicable to well-characterized sinusoidal driving forces. By leveraging ultralow dissipation and heavy test masses, MORRIS opens a new window onto tests of small-scale gravity and searches for physics beyond the Standard Model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2507.16911v2
- Title: Effects of quantum geometry on the decoherence induced by black holes
- Authors: Max Joseph Fahn, Alessandro Pesci
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2507.16911v2  pdf=https://arxiv.org/pdf/2507.16911v2.pdf

Abstract:
Recently, it has been shown that a quantum system held in spatial superposition and then eventually recombined does experience decoherence from black hole horizons, at a level increasing linearly with the time the superposition has been kept open. In this, the effects of the horizon have been derived using a classical spacetime picture for the latter. In the present note we point out that quantum aspects of the geometry itself of the quantum black hole could significantly affect the results. In a specific effective implementation of the quantum geometry in terms of a minimal length and ensuing minimal area, it appears in particular that, for selected values of the quantum of area proposed on various grounds in the literature, the decoherence induced by the horizon turns out to be limited to negligibly small values.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2507.18709v2
- Title: Horizon quantum geometries and decoherence
- Authors: Max Joseph Fahn, Alessandro Pesci
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2507.18709v2  pdf=https://arxiv.org/pdf/2507.18709v2.pdf

Abstract:
There is mounting theoretical evidence that black hole horizons induce decoherence on a quantum system, say a particle, put in a superposition of locations, with the decoherence functional, evaluated after closure of the superposition, increasing linearly with the time the superposition has been kept open. This phenomenon has been shown to owe its existence to soft modes, that is modes with very low frequencies, of the quantum fields -- sourced by the particle -- which pierce through the horizon, or also can be understood as coming from the interaction with the black hole described as a thermodynamic quantum system at Hawking's temperature. Here we investigate the effects of ensuing quantum aspects of the geometry itself of the horizon, in an effective perspective in which the quantum geometry of the horizon is captured by existence of a limit length or by horizon area quantisation. We show that the discreteness of the energy levels associated to the different geometric configurations might have strong impact on the results, in particular reducing the decoherence effects even to a negligible level in case of quanta of area $A_0 = \mathcal{O}(1) \, \, l_p^2$ or larger, with $l_p$ the Planck length.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2508.12797v2
- Title: Unified theory of classical and quantum ergotropy
- Authors: Michele Campisi
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; physics.plasm-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2508.12797v2  pdf=https://arxiv.org/pdf/2508.12797v2.pdf

Abstract:
Quantifying the ergotropy (a.k.a. available energy), namely the maximal amount of energy that can be extracted from a thermally isolated system, is a central problem in quantum thermodynamics. Notably, the same problem has been long studied for classical systems as well, e.g. in plasma physics and astrophysics, where the basic principles for its solution are known for the case of collisionless fluids. Here we provide the general analytical expression of ergotropy of classical systems valid regardless of their size and the type of interparticle interactions, and show that it emerges as the classical limit of the quantum expression of ergotropy, for quantum systems that are classically ergodic. We thus establish a unified theory of classical and quantum ergotropy, whose applicability ranges from atomic to galactic scale. Such unified theory is indispensable for studying the genuine quantum signatures of ergotropy: We show that the celebrated decomposition of quantum ergotropy into coherent ant inchoherent parts survives in the classical regime, indicating that coherences do not necessarily reveal quantumness. The unified theory also allows to port tools and methods across the classical-quantum boundary to unlock the solution of standing problems. We apply this to swiftly solve the open problem of ergotropy extraction in the classical regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2508.17977v2
- Title: Ab initio study of anomalous temperature dependence of resistivity in V-Al alloys
- Authors: Gabor Csire, Oleg E. Peil
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; cond-mat.dis-nn; cond-mat.mes-hall; cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2508.17977v2  pdf=https://arxiv.org/pdf/2508.17977v2.pdf

Abstract:
V$_{1-x}$Al$_x$ is a representative example of highly resistive metallic alloys exhibiting a crossover to a negative temperature coefficient of resistivity (TCR), known as the Mooij correlation. Despite numerous proposals to explain this anomalous behavior,none have provided a satisfactory quantitative explanation thus far. In this work, we calculate the electrical conductivity using an ab initio methodology that combines the Kubo-Greenwood formalism with the coherent potential approximation (CPA). The temperature dependence of the conductivity is obtained within a CPA-based model of thermal atomic vibrations. Using this approach, we observe the crossover to the negative TCR behavior in V$_{1-x}$Al$_x$, with the temperature coefficient following the Mooij correlation, which matches experimental observations in the intermediate-to-high temperature range. Analysis of the results allows us to clearly identify a non-Boltzmann contribution responsible for this behavior and describe it as a function of temperature and composition.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2509.19704v2
- Title: Holographic Aspects of Dynamical Mean-Field Theory
- Authors: Kouichi Okunishi, Akihisa Koga
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-lat; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2509.19704v2  pdf=https://arxiv.org/pdf/2509.19704v2.pdf

Abstract:
Dynamical mean-field theory (DMFT) is one of the most standard theoretical frameworks for addressing strongly correlated electron systems. Meanwhile, the concept of holography, developed in the field of quantum gravity, provides an intrinsic relationship between quantum many-body systems and space-time geometry. In this study, we demonstrate that these two theories are closely related to each other by shedding light on holographic aspects of DMFT, particularly for electrons with a semicircle density of states. We formulate a holographic renormalization group for the branch Green's function from the outer edge to the interior of the Bethe lattice network, and then find that its fixed point can be interpreted as a self-consistent solution of Green's function in DMFT. By introducing an effective two-dimensional anti-de Sitter space, moreover, we clarify that the scaling dimensions for the branch Green's function and the boundary correlation functions of electrons at the outer edge of the Bethe lattice network are characterized by the fixed-point Green's function. We also perform DMFT computations for the Bethe-lattice Hubbard model, which illustrate that the scaling dimensions capture the Mott transition in the deep interior.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2512.05477v2
- Title: Quantum geometry and $X$-wave magnets with $X=p,d,f,g,i$
- Authors: Motohiko Ezawa
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.mtrl-sci; math-ph; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2512.05477v2  pdf=https://arxiv.org/pdf/2512.05477v2.pdf

Abstract:
Quantum geometry is a differential geometry based on quantum mechanics. It is related to various transport and optical properties in condensed matter physics. The Zeeman quantum geometry is a generalization of quantum geometry including the spin degrees of freedom. It is related to electromagnetic cross responses. Quantum geometry is generalized to non-Hermitian systems and density matrices. Especially, the latter is quantum information geometry, where the quantum Fisher information naturally arises as quantum metric. We apply these results to the $X$-wave magnets, which include $d$% -wave, $g$-wave and $i$-wave altermagnets as well as $p$-wave and $f$-wave magnets. They have universal physics for anomalous Hall conductivity, tunneling magneto-resistance and planar Hall effect. We also study magneto-optical conductivity, magnetic circular dichroism and Friedel oscillations in the $X$-wave magnets. Various analytic formulas are derived in the case of two-band Hamiltonians. This paper presents a review of recent progress together with some original results.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2512.06768v4
- Title: Real-Time Dynamics in Two Dimensions with Tensor Network States via Time-Dependent Variational Monte Carlo
- Authors: Yantao Wu, Jannes Nys
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2512.06768v4  pdf=https://arxiv.org/pdf/2512.06768v4.pdf

Abstract:
Reliably simulating two-dimensional many-body quantum dynamics with projected entangled pair states (PEPS) has long been a difficult challenge. In this work, we overcome this barrier for low-energy quantum dynamics by developing a stable and efficient time-dependent variational Monte Carlo (tVMC) framework for PEPS. By analytically removing all gauge redundancies of the PEPS manifold and exploiting tensor locality, we obtain a numerically well-conditioned stochastic reconfiguration (SR) equation amenable to robust solution using the efficient Cholesky decomposition, enabling long-time evolution in previously inaccessible regimes. We demonstrate the power and generality of the method through four representative real-time problems in two dimensions: (I) chiral edge propagation in a free-fermion Chern insulator; (II) fractionalized charge transport in a fractional Chern insulator; (III) vison confinement dynamics in the Higgs phase of a Z2 lattice gauge theory; and (IV) superfluidity and critical velocity in interacting bosons. All simulations are performed on 12x12 or 13x13 lattices with evolution times T = 10 to 12 using modest computational resources (1 to 5 days on a single GPU card). Where exact benchmarks exist (case I), PEPS-tVMC matches free-fermion dynamics with high accuracy up to T = 12. These results establish PEPS-tVMC as a practical and versatile tool for real-time quantum dynamics in two dimensions. The method extends the reach of classical tensor-network simulations for studying elementary excitations in quantum many-body systems and provides a valuable computational counterpart to emerging quantum simulators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-30 09:51
- arXiv: 2512.19511v3
- Title: Spin Response of a Magnetic Monopole and Quantum Hall Response in Topological Lattice Models through Local Invariants and Light
- Authors: Karyn Le Hur, Andrea Baldanza
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2512.19511v3  pdf=https://arxiv.org/pdf/2512.19511v3.pdf

Abstract:
Here, we elaborate on and develop the geometrical approach introduced in K. Le Hur, Physics Reports 1104 1-42 (2025) between the magnetic monopole created from a radial field, quantum physics and topological lattice models through quantum phase transitions. We introduce an effective magnetic moment for a monopole when applying an additional source field along z-direction which also mediates the quantum phase transition. We present its relation with the transverse pumped quantum Hall current. The magnetic susceptibility can be introduced as a measure of the topological invariant i.e. it remains quantized within the topological phase until the transition. We show the relation with two-dimensional topological lattice models such as a honeycomb Haldane model in real space. We develop the theory and present a numerical analysis between local invariants in momentum space introduced from Dirac points, correlation functions and the responses to circularly polarized light. We develop the formalism for coupled-planes materials including the possibility of quantum spin Hall effect and address a relation between the Ramanujan infinite alternating series and an interface in real space with a topological number one-half.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20871v1
- Title: End-to-End Fidelity Analysis of Quantum Circuit Optimization: From Gate-Level Transformations to Pulse-Level Control
- Authors: Rylan Malarchick
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20871v1  pdf=https://arxiv.org/pdf/2601.20871v1.pdf

Abstract:
We present a comprehensive analysis of quantum circuit fidelity across the full compilation stack, from high-level gate optimization through pulse-level control. Using a modular integration framework connecting a C++ circuit optimizer with Lindblad-based pulse simulation, we systematically evaluate the fidelity impact of four optimization passes: gate cancellation, commutation, rotation merging, and identity elimination, on IQM Garnet hardware parameters. Our simulation campaign spanning 371 circuit runs reveals that gate cancellation provides the most significant improvement (68\% of circuits improved, 14,024 gates eliminated), while pulse duration exhibits the strongest negative correlation with process fidelity ($r = -0.74$, $R^2 = 0.55$). We validate these findings through hardware execution on the IQM Resonance Garnet 20-qubit processor, demonstrating 70\% gate reduction on QFT circuits with 100\% job success rate (8 executions). Our open-source framework enables reproducible benchmarking of quantum compilation pipelines.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20872v1
- Title: An Ontological Interpretation of Photon Wave-Particle Duality via Complex-Space Trajectories
- Authors: Shiang-Yi Han, Ciann-Dong Yang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20872v1  pdf=https://arxiv.org/pdf/2601.20872v1.pdf

Abstract:
Wave particle duality remains a central interpretational challenge in quantum theory. In this work, we develop a trajectory-based description of photon dynamics formulated in an extended complex space within the relativistic quantum Hamilton Jacobi framework. In this approach, photon motion is represented by complex trajectories whose real projections describe propagation, while imaginary components encode oscillatory structure. We show that momentum eigenstates correspond to straight line trajectories with uniform propagation at the speed of light, whereas superposition states lead to nontrivial quantum potentials and oscillatory motion in the complex plane. Extending the analysis to complex two dimensional space reveals richer dynamical behavior, including propagating wave like trajectories and standing wave like patterns in real projections. Energy momentum consistency is verified through an internal coherence analysis based on projected standing wave wavelengths. Rather than introducing new dynamical laws or additional physical dimensions, the complex space is employed as an interpretational framework that renders wave like and particle like aspects as complementary projections of a single underlying motion. The results suggest a unified geometric perspective on wave particle duality, while remaining fully compatible with standard quantum mechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20873v1
- Title: Novel method for evaluating the eigenvalues of the Heun differential equation with an application to the Breit equation
- Authors: P. J. Rijken, Th. A. Rijken
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20873v1  pdf=https://arxiv.org/pdf/2601.20873v1.pdf

Abstract:
Eigenvalues of the Breit equation, in which only the static Coulomb potential is considered, have been found. Over the past decades several authors have analyzed the Breit equation to obtain numerically or by approximation an estimation of the energy levels. Various approaches have been used and no determination of the energy levels currently exists that is directly based on the second order Heun differential equation derived.   The aim of this work is to provide a method of calculation that can be used to numerically calculate the energy levels for various spin states to high accuracy.   From the Breit equation, we derive the corresponding second-order Heun differential equation and continued fraction from which the eigenvalues can be determined very accurately. Next, we present a novel method based on the Green function method, which leads to a semi-infinite determinant from which we are able to obtain the numerical values of the eigenvalues by direct calculation.   Using suitable numerical methods for the direct calculation of the continued fraction and the semi-infinite determinant, we show that both methods are consistent within 25 digits of accuracy. We show that the correct energy levels for the Dirac equation follow from our results by a suitable mapping of the variables.   The results are in total agreement with earlier calculations found in the literature and extend this by several digits of additional accuracy. The condition on the determinant giving the energy levels provides a rich structure that is promising in extending the results of this work.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20877v1
- Title: AI Optimized Routing and Resource Allocation for Quantum Enabled Non Terrestrial Industrial Networks
- Authors: Sathish Krishna Anumula, Harinatha Reddy Chennam, Ranganath Nagesh Taware, Balakumar Ravindranath Kunthu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20877v1  pdf=https://arxiv.org/pdf/2601.20877v1.pdf

Abstract:
The industrial transformation of Industry 4 and 5 results in cyber physical production systems that require secure resilient and energy efficient connectivity over integrated terrestrial and nonterrestrial networks NTNs Since its operation over fiber spans over 5G or 6G infrastructures to Low Earth Orbit LEO satellites quantum communication techniques enabled by Quantum Key Distribution QKD together with entanglement assisted links have the potential for high assurance security as well as synchronization But quantum channels are extremely vulnerable to any kind of impairment be it environmental or physicalsuch as effects induced by atmospheric turbulence pointing errors Doppler shifts satellite motion restricted optical power and limited quantum memory All these factors make for a tightly coupled routing and resource allocation problem that unfortunately cannot be addressed at scale by existing approaches to network control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20887v1
- Title: Micro-mobility dispatch optimization via quantum annealing incorporating historical data
- Authors: Takeru Goto, Masayuki Ohzeki
- Categories: quant-ph (primary); quant-ph; cs.MA
- Links: abs=https://arxiv.org/abs/2601.20887v1  pdf=https://arxiv.org/pdf/2601.20887v1.pdf

Abstract:
This paper proposes a novel dispatch formulation for micro-mobility vehicles using a Quantum Annealer (QA). In recent years, QA has gained increasing attention as a high-performance solver for combinatorial optimization problems. Meanwhile, micro-mobility services have been rapidly developed as a promising means of realizing efficient and sustainable urban transportation. In this study, the dispatch problem for such micro-mobility services is formulated as a Quadratic Unconstrained Binary Optimization (QUBO) problem, enabling efficient solving through QA. Furthermore, the proposed formulation incorporates historical usage data to enhance operational efficiency. Specifically, customer arrival frequencies and destination distributions are modeled into the QUBO formulation through a Bayesian approach, which guides the allocation of vacant vehicles to designated stations for waiting and charging. Simulation experiments are conducted to evaluate the effectiveness of the proposed method, with comparisons to conventional formulations such as the vehicle routing problem. Additionally, the performance of QA is compared with that of classical solvers to reveal its potential advantages for the proposed dispatch formulation. The effect of reverse annealing on improving solution quality is also investigated.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20922v1
- Title: The quantum sky of Majorana stars
- Authors: L. L. Sanchez-Soto, A. B. Klimov, A. Z. Goldberg, G. Leuchs
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20922v1  pdf=https://arxiv.org/pdf/2601.20922v1.pdf

Abstract:
Majorana stars, the $2S$ spin coherent states that are orthogonal to a spin-$S$ state, offer an elegant method to visualize quantum states. This representation offers deep insights into the structure, symmetries, and entanglement properties of quantum states, bridging abstract algebraic formulations with intuitive geometrical intuition. In this paper, we briefly survey the development and applications of the Majorana constellation, exploring its relevance in modern areas of quantum information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20925v1
- Title: Double-Bracket Master Equations: Phase-Space Representation and Classical Limit
- Authors: Ankit W. Shrestha, Budhaditya Bhattacharjee, Adolfo del Campo
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2601.20925v1  pdf=https://arxiv.org/pdf/2601.20925v1.pdf

Abstract:
We investigate the classical limit of quantum master equations featuring double-bracket dissipators. Specifically, we consider dissipators defined by double commutators, which describe dephasing dynamics, as well as dissipators involving double anticommutators, associated with fluctuating anti-Hermitian Hamiltonians. The classical limit is obtained by formulating the open quantum dynamics in phase space using the Wigner function and Moyal products, followed by a systematic $\hbar$-expansion. We begin with the well-known model of energy dephasing, associated with energy diffusion. We then turn to master equations containing a double anticommutator with the system Hamiltonian, recently derived in the context of noisy non-Hermitian systems. For both classes of double-bracket equations, we provide a gradient-flow representation of the dynamics. We analyze the classical limit of the resulting evolutions for harmonic and driven anharmonic quantum oscillators, considering both classical and nonclassical initial states. The dynamics is characterized through the evolution of several observables as well as the Wigner logarithmic negativity. We conclude by extending our analysis to generalized master equations involving higher-order nested brackets, which provide a time-continuous description of spectral filtering techniques commonly used in the numerical analysis of quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20927v1
- Title: Entangling logical qubits without physical operations
- Authors: Jin Ming Koh, Anqi Gong, Andrei C. Diaconu, Daniel Bochen Tan, Alexandra A. Geim, Michael J. Gullans, Norman Y. Yao, Mikhail D. Lukin, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20927v1  pdf=https://arxiv.org/pdf/2601.20927v1.pdf

Abstract:
Fault-tolerant logical entangling gates are essential for scalable quantum computing, but are limited by the error rates and overheads of physical two-qubit gates and measurements. To address this limitation, we introduce phantom codes-quantum error-correcting codes that realize entangling gates between all logical qubits in a code block purely through relabelling of physical qubits during compilation, yielding perfect fidelity with no spatial or temporal overhead. We present a systematic study of such codes. First, we identify phantom codes using complementary numerical and analytical approaches. We exhaustively enumerate all $2.71 \times 10^{10}$ inequivalent CSS codes up to $n=14$ and identify additional instances up to $n=21$ via SAT-based methods. We then construct higher-distance phantom-code families using quantum Reed-Muller codes and the binarization of qudit codes. Across all identified codes, we characterize other supported fault-tolerant logical Clifford and non-Clifford operations. Second, through end-to-end noisy simulations with state preparation, full QEC cycles, and realistic physical error rates, we demonstrate scalable advantages of phantom codes over the surface code across multiple tasks. We observe a one-to-two order-of-magnitude reduction in logical infidelity at comparable qubit overhead for GHZ-state preparation and Trotterized many-body simulation tasks, given a modest preselection acceptance rate. Our work establishes phantom codes as a viable architectural route to fault-tolerant quantum computation with scalable benefits for workloads with dense local entangling structure, and introduces general tools for systematically exploring the broader landscape of quantum error-correcting codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20938v1
- Title: Non-Equilibrium Phase Transition in a Boundary-Driven Dissipative Fermionic Chain
- Authors: Hao Chen, Wucheng Zhang, Manas Kulkarni, Abhinav Prem
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2601.20938v1  pdf=https://arxiv.org/pdf/2601.20938v1.pdf

Abstract:
We demonstrate that a boundary-localized periodic (Floquet) drive can induce nontrivial long-range correlations in a non-interacting fermionic chain which is additionally subject to boundary dissipation. Surprisingly, we find that this phenomenon occurs even when the corresponding isolated bulk is in a trivial gapped phase with exponentially decaying correlations. We argue that this boundary-drive induced non-equilibrium transition (as witnessed through the correlation matrix) is driven by a resonance mechanism whereby the drive frequency bridges bulk energy gaps, allowing boundary-injected particles and holes to propagate and mediate long-range correlations into the bulk. We also numerically establish that when the drive bridges a particle-hole gap, the induced long-range order scales as a power law with the bulk pairing potential ($χ\sim γ^2$). Our results highlight the potential of localized coherent driving for generating macroscopic order in open quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20949v1
- Title: Spatial superposition for a two-dimensional matter-wave interferometer in an inverted harmonic potential with gyroscopic rotational stability
- Authors: Ryan Rizaldy, Tian Zhou, Run Zhou, Anupam Mazumdar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20949v1  pdf=https://arxiv.org/pdf/2601.20949v1.pdf

Abstract:
This study presents a mathematical model of the spatial and rotational motion of a nanodiamond in an inverted harmonic potential to create a macroscopic quantum spatial superposition. The model is based on the Stern-Gerlach Interferometer (SGI) scheme, which utilises linear and quadratic magnetic fields to generate a harmonic potential (linear magnetic field) and a non-linear potential (non-linear/quadratic magnetic field). By incorporating two-dimensional dynamics into the model, we provide a more realistic and accurate depiction of nanoparticle dynamics in linear and inverted harmonic potentials and explore the interaction between motion in a two-dimensional plane. Importantly, we derive the equations of motion for the rotational degrees of freedom, i.e. libration, precession, and rotation. The results show that adding a magnetic-field bias term to the magnetic-field profile in the linear stage affects the classical equations of motion but does not affect the width of the wave packet. Moreover, the libration mode always forms a harmonic potential at each stage because the applied initial angular velocity is dominated by the nanoparticle's defect axis, making it more stable in the presence of the trap frequency in the orthogonal direction along the axis that enables the creation of a macroscopic quantum superposition.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20950v1
- Title: Parametric Quantum State Tomography with HyperRBMs
- Authors: Simon Tonner, Viet T. Tran, Richard Kueng
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2601.20950v1  pdf=https://arxiv.org/pdf/2601.20950v1.pdf

Abstract:
Quantum state tomography (QST) is essential for validating quantum devices but suffers from exponential scaling in system size. Neural-network quantum states, such as Restricted Boltzmann Machines (RBMs), can efficiently parameterize individual many-body quantum states and have been successfully used for QST. However, existing approaches are point-wise and require retraining at every parameter value in a phase diagram. We introduce a parametric QST framework based on a hypernetwork that conditions an RBM on Hamiltonian control parameters, enabling a single model to represent an entire family of quantum ground states. Applied to the transverse-field Ising model, our HyperRBM achieves high-fidelity reconstructions from local Pauli measurements on 1D and 2D lattices across both phases and through the critical region. Crucially, the model accurately reproduces the fidelity susceptibility and identifies the quantum phase transition without prior knowledge of the critical point. These results demonstrate that hypernetwork-modulated neural quantum states provide an efficient and scalable route to tomographic reconstruction across full phase diagrams.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20952v1
- Title: Quantum metrology enhanced by effective time reversal
- Authors: Yu-Xin Wang, Flavio Salvati, David R. M. Arvidsson Shukur, William F. Braasch, Kater Murch, Nicole Yunger Halpern
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20952v1  pdf=https://arxiv.org/pdf/2601.20952v1.pdf

Abstract:
Quantum metrology involves the application of quantum resources to enhance measurements. Several communities have developed quantum-metrology strategies that leverage effective time reversals. These strategies, we posit, form four classes. First, echo metrology begins with a preparatory unitary and ends with that unitary's time-reverse. The protocol amplifies the visibility of a small parameter to be sensed. Similarly, weak-value amplification enhances a weak coupling's detectability. The technique exhibits counterintuitive properties captured by a retrocausal model. Using the third strategy, one simulates closed timelike curves, worldlines that loop back on themselves in time. The fourth strategy involves indefinite causal order, which characterises channels applied in a superposition of orderings. We review these four strategies, which we unify under the heading of time-reverse metrology. We also outline opportunities for this toolkit in quantum metrology; quantum information science; quantum foundations; atomic, molecular, and optical physics; and solid-state physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20956v1
- Title: Universal Topological Gates from Braiding and Fusing Anyons on Quantum Hardware
- Authors: Chiu Fan Bowen Lo, Anasuya Lyons, Dan Gresh, Michael Mills, Peter E. Siegfried, Maxwell D. Urmey, Nathanan Tantivasadakarn, Henrik Dreyer, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2601.20956v1  pdf=https://arxiv.org/pdf/2601.20956v1.pdf

Abstract:
Topological quantum computation encodes quantum information in the internal fusion space of non-Abelian anyonic quasiparticles, whose braiding implements logical gates. This goes beyond Abelian topological order (TO) such as the toric code, as its anyons lack internal structure. However, the simplest non-Abelian generalizations of the toric code do not support universality via braiding alone. Here we demonstrate that such minimally non-Abelian TOs can be made universal by treating anyon fusion as a computational primitive. We prepare a 54-qubit TO wavefunction associated with the smallest non-Abelian group, $S_3$, on Quantinuum's H2 quantum processor. This phase of matter exhibits cyclic anyon fusion rules, known to underpin universality, which we evidence by trapping a single non-Abelian anyon on the torus. We encode logical qutrits in the nonlocal fusion space of non-Abelian fluxes and, by combining an entangling braiding operation with anyon charge measurements, realize a universal topological gate set and read-out, which we further demonstrate by topologically preparing a magic state. This work establishes $S_3$ TO as simple enough to be prepared efficiently, yet rich enough to enable universal topological quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20991v1
- Title: Active polarization stabilization of fields in an optical fiber for protective measurements
- Authors: E. Pascoe, A. Catalan, J. Sharkansky, M. Beck
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.20991v1  pdf=https://arxiv.org/pdf/2601.20991v1.pdf

Abstract:
We have performed Zeno protective measurements of quantum polarization states by coupling the polarization to a temporal pointer (arrival time) in a birefringent optical fiber. It is necessary to actively stabilize the polarization, and we do this by using the signal photon counts themselves as the error signal in a feedback loop. We compare these measurements to a stabilization scheme using a classical reference beam as the error signal. The method using photon counts has higher signal levels and significantly reduced background. These improvements allow us to increase the number of Zeno stages in our measurements from 9 to 13, with a corresponding decrease in the measurement uncertainty.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21062v1
- Title: Polaron-Polaritons in Subwavelength Arrays of Trapped Atoms
- Authors: Kristian Knakkergaard Nielsen, Lukas Wangler, David Castells-Graells, J. Ignacio Cirac, Ana Asenjo-Garcia, Daniel Malz, Cosimo C. Rusconi
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2601.21062v1  pdf=https://arxiv.org/pdf/2601.21062v1.pdf

Abstract:
Subwavelength arrays of atoms trapped in optical lattices or tweezers are inherently susceptible to deformations: Optomechanical forces produce lattice distortions, which, in turn, modify the optical response of the array. We show that this coupling hybridizes collective atomic excitations (polaritons) with phonons, forming polaron-polaritons -- the fundamental quasiparticles governing light-matter interactions in arrays of trapped atoms. Using analytical polaron theory and numerical simulations, we show that: (1) phonons can strongly enhance the decay of subradiant states, but also enable their efficient excitation; (2) transport of dark excitations remains remarkably robust even at low trap frequencies, except when a polariton can resonantly scatter phonons; and (3) motion reduces the reflectivity of a two-dimensional atomic mirror, however, we identify mechanisms that mitigate this degradation and restore reflectivity above 99% in some cases. Our findings lay the foundation for analyzing motional effects in key applications and suggest new ways to harness them in state-of-the-art experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21065v1
- Title: Building Holographic Entanglement by Measurement
- Authors: Jonathan Jeffrey, Lucien Gandarias, Monika Schleier-Smith, Brian Swingle
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2601.21065v1  pdf=https://arxiv.org/pdf/2601.21065v1.pdf

Abstract:
We propose a framework for preparing quantum states with a holographic entanglement structure, in the sense that the entanglement entropies are governed by minimal surfaces in a chosen bulk geometry. We refer to such entropies as holographic because they obey a relation between entropies and bulk minimal surfaces, known as the Ryu-Takayanagi formula, that is a key feature of holographic models of quantum gravity. Typically in such models, the bulk geometry is determined by solving Einstein's equations. Here, we simply choose a bulk geometry, then discretize the geometry into a coupling graph comprising bulk and boundary nodes. Evolving under this graph of interactions and measuring the bulk nodes leaves behind the desired pure state on the boundary. We numerically demonstrate that the resulting entanglement properties approximately reproduce the predictions of the Ryu-Takayanagi formula in the chosen bulk geometry. We consider graphs associated with hyperbolic disk and wormhole geometries, but the approach is general. The minimal ingredients in our proposal involve only Gaussian operations and measurements and are readily implementable in photonic and cold-atom platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21075v1
- Title: Dynamical Casimir effect under the action of gravitational waves
- Authors: Gustavo de Oliveira, Thiago Henrique Moreira, Lucas Chibebe Céleri
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2601.21075v1  pdf=https://arxiv.org/pdf/2601.21075v1.pdf

Abstract:
Several nontrivial phenomena emerge when a quantum field is subjected to dynamical perturbations, with prominent examples including the Hawking and Unruh effects, as well as the dynamical Casimir effect. In this work, we compute the number of particles produced via the dynamical Casimir effect in an ideal cavity, where one of the mirrors is allowed to move under the influence of a gravitational wave. Assuming an oscillatory mirror motion and a plane gravitational wave, we identify the resonance conditions that lead to an exponential increase in the number of created particles through parametric amplification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21119v1
- Title: A levitated nano-accelerometer sensitized by quantum quench
- Authors: M. Kamba, S. Otabe, K. Funo, T. Sagawa, K. Aikawa
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.21119v1  pdf=https://arxiv.org/pdf/2601.21119v1.pdf

Abstract:
We realize a nanoscale accelerometer exploiting the nonequilibrium dynamics of a nanoparticle near the quantum ground state. We explore the dynamics after quenching the trapping potential and find that rapid quenching provides an instance at which the sensitivity is enhanced due to the minimized uncertainty in the position. With rapid quenching, the observed sensitivity is in good agreement with a numerical simulation based on the quantum Langevin equation and approaches to the limit given by the quantum Fisher information. Our results open up a pathway to quantum inertial sensing sensitized by exploiting quench dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21139v1
- Title: Hidden-Field Coordination Reveals Payoff-Free Quantum Correlation Structure in Decentralized Coordination
- Authors: Sinan Bugu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21139v1  pdf=https://arxiv.org/pdf/2601.21139v1.pdf

Abstract:
We study decentralized multi-agent coordination where agents must correlate actions against an unobserved field and cannot communicate. To isolate correlation geometry from payoff optimization, we introduce the Hidden-Field Coordination (HFC) model, which enforces identical information access and no-signaling constraints across strategies. Using information-theoretic diagnostics, we compare classical shared-randomness baselines with an entanglement-mediated strategy based on multipartite W states and a strictly local Spontaneous Leader Election rule. Within the restricted symmetric shared-latent baseline studied here, increasing total correlation is achieved primarily by driving actions toward alignment (copying), which also increases pairwise coincidence (collisions). By contrast, the quantum strategy realizes a collision-suppressing coordination regime: it preserves global dependence while reducing pairwise coincidence below the independent (product) baseline induced by the common marginal distribution. This produces a geometric separation in the joint-action distribution. Classical baselines concentrate probability near the diagonal of action equality, whereas the entanglement-mediated mapping occupies an offset-diagonal region associated with relational roles. Accordingly, the entanglement signature in this setting is not higher correlation magnitude; total-correlation differentials can be negative relative to the classical copying optimum. Instead, it reflects a change in dependence geometry that supports robust anti-coordination.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21140v1
- Title: Efficient Algorithms for Weakly-Interacting Quantum Spin Systems
- Authors: Ryan L. Mann, Gabriel Waite
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.DS; math.CO
- Links: abs=https://arxiv.org/abs/2601.21140v1  pdf=https://arxiv.org/pdf/2601.21140v1.pdf

Abstract:
We establish efficient algorithms for weakly-interacting quantum spin systems at arbitrary temperature. In particular, we obtain a fully polynomial-time approximation scheme for the partition function and an efficient approximate sampling scheme for the thermal distribution over a classical spin space. Our approach is based on the cluster expansion method and a standard reduction from approximate sampling to approximate counting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21152v1
- Title: Community detection in network using Szegedy quantum walk
- Authors: Md Samsur Rahaman, Supriyo Dutta
- Categories: quant-ph (primary); quant-ph; cs.SI; math.CO; physics.soc-ph
- Links: abs=https://arxiv.org/abs/2601.21152v1  pdf=https://arxiv.org/pdf/2601.21152v1.pdf

Abstract:
In a network, the vertices with similar characteristics construct communities. The vertices in a community are well-connected. Detecting the communities in a network is a challenging and important problem in the theory of complex networks. One approach to solve this problem uses the classical random walks on the graphs. In quantum computing, quantum walks are the quantum mechanical counterparts of classical random walks. In this article, we employ a variant of Szegedy's quantum walk to develop a procedure for discovering the communities in networks. The limiting probability distribution of quantum walks assists us in determining the inclusion of a vertex in a community. We apply our procedure of community detection on a number of graphs and social networks, such as the relaxed caveman graph, $l$-partition graph, Karate club graph, dolphin's social network, etc.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21240v1
- Title: Reflecting boundary induced modulation of tripartite coherence harvesting
- Authors: Shu-Min Wu, Xiao-Ying Jiang, Xiang-Yue Yu, Zhihong Liu, Xiao-Li Huang
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2601.21240v1  pdf=https://arxiv.org/pdf/2601.21240v1.pdf

Abstract:
We study the extraction of quantum coherence by three static Unruh-DeWitt (UDW) detectors that interact locally with a massless scalar vacuum field in the vicinity of an infinite perfectly reflecting boundary. Depending on the setup, the detectors are positioned either parallel or orthogonal to the boundary, with their energy gaps chosen to satisfy the hierarchy $Ω_C\geq Ω_B\geq Ω_A$. Our analysis reveals that decreasing the detector-boundary separation leads to a monotonic degradation of quantum coherence, whereas the same boundary effect can simultaneously preserve and even amplify the harvested quantum entanglement. Moreover, when the detectors possess distinct energy gaps, coherence extraction is further inhibited; strikingly, such non-identical configurations substantially enhance the efficiency of entanglement harvesting and markedly extend the range of detector separations over which non-negligible entanglement can be generated. Nevertheless, the harvesting of nonlocal quantum coherence is achievable over a significantly broader range of detector separations than that of quantum entanglement. Despite exhibiting similar overall behavior, orthogonal detector configurations outperform parallel ones in coherence harvesting, highlighting the quantitative influence of detector geometry. Overall, our study reveals a hierarchical distinction between quantum coherence and entanglement as operational resources in structured vacuum fields: quantum coherence is not only more readily accessible across space but also more robust than entanglement, whereas entanglement exhibits richer features and can be selectively activated and enhanced through boundary effects and detector non-uniformity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21250v1
- Title: 3D imaging of the biphoton spatiotemporal wave packet
- Authors: Yang Xue, Ze-Shan He, Hao-Shu Tian, Qin-Qin Wang, Bin-Tong Yin, Jun Zhong, Xiao-Ye Xu, Chuan-Feng Li, et al.
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.21250v1  pdf=https://arxiv.org/pdf/2601.21250v1.pdf

Abstract:
Photons are among the most important carriers of quantum information owing to their rich degrees of freedom (DoFs), including various spatiotemporal structures. The ability to characterize these DoFs, as well as the hidden correlations among them, directly determines whether they can be exploited for quantum tasks. While various methods have been developed for measuring the spatiotemporal structure of classical light fields, owing to the technical challenges posed by weak photon flux, there have so far been no reports of observing such structures in their quantum counterparts, except for a few studies limited to correlations within individual DoFs. Here, we propose and experimentally demonstrate a self-referenced, high-efficiency, and all-optical method, termed 3D imaging of photonic wave packets, for comprehensive characterization of the spatiotemporal structure of a quantum light field, i.e., the biphoton spatiotemporal wave packet. Benefiting from this developed method, we successfully observe the spatial-spatial, spectral-spectral, and spatiotemporal correlations of biphotons generated via spontaneous parametric down-conversion, revealing rich local and nonlocal spatiotemporal structure in quantum light fields. This method will further advance the understanding of the dynamics in nonlinear quantum optics and expand the potential of photons for applications in quantum communication and quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21254v1
- Title: Sampling methods to describe superradiance in large ensembles of quantum emitters
- Authors: Daniel Eyles, Emmanuel Lassalle, Adam Stokes, Ramón Paniagua-Domínguez, Ahsan Nazir
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21254v1  pdf=https://arxiv.org/pdf/2601.21254v1.pdf

Abstract:
Superradiance is a quantum phenomenon in which coherence between emitters results in enhanced and directional radiative emission. Many quantum optical phenomena can be characterized by the two-time quantum correlation function $g^{(2)}(t,τ)$, which describes the photon statistics of emitted radiation. However, the critical task of determining $g^{(2)}(t,τ)$ becomes intractable for large emitter ensembles due to the exponential scaling of the Hilbert space dimension with the number of emitters. Here, we analyse and benchmark two approximate numerical sampling methods applicable to emitter arrays embedded within electromagnetic environments, which generally provide upper and lower bounds for $g^{(2)}(t,0)$. We also introduce corrections to these methods (termed offset corrections) that significantly improve the quality of the predictions. The optimal choice of method depends on the total number of emitters, such that taken together, the two approaches provide accurate descriptions across a broad range of important regimes. This work therefore provides new theoretical tools for studying the well-known yet complex phenomenon of superradiance in large ensembles of quantum emitters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21263v1
- Title: Localization and scattering of a photon in quasiperiodic qubit arrays
- Authors: Xinyin Zhang, Yongguan Ke, Zhengzhi Peng, Zuorui Chen, Wenjie Liu, Li Zhang, Chaohong Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21263v1  pdf=https://arxiv.org/pdf/2601.21263v1.pdf

Abstract:
We study the localization and scattering of a single photon in a waveguide coupled to qubit arrays with quasiperiodic spacings. As the quasiperiodic strength increases, localized subradiant states with extremely long lifetime appear around the resonant frequency and form a continuum band. In stark contrast to the fully disordered waveguide QED where all states are localized, we analytically find that the fraction of localized states is up to $(3-\sqrt{5})/2$ when the modulation frequency is $(1+\sqrt{5})/2$. The localized and delocalized states can be related to excitation in flat and curved inverse energy bands under the approximation of large-period modulation. When the quasiperiodic strength is weak, an extended subradiant state can support the transmission of a photon. However, as the quasiperiodic strength increases, localized subradiant states can completely block the transmission of a single photon in resonance with the subradiant states, and enhance the overall reflection. At a fixed quasiperiodic strength, we also find mobility edge in transmission spectrum, below and above which the transmission is either turned on and off as system size increases. Our work give new insights into the localization in non-Hermitian systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21265v1
- Title: A Quantum-Memory-Free Quantum Secure Direct Communication Protocol Based on Privacy Amplification of Coded Sequences
- Authors: Shang-Jen Su, Shi-Yuan Wang, Matthieu R. Bloch
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21265v1  pdf=https://arxiv.org/pdf/2601.21265v1.pdf

Abstract:
We develop an information-theoretic analysis of Quantum-Memory-Free (QMF) Quantum Secure Direct Communication (QSDC) under collective attacks as an alternative to the conventional Quantum Key Distribution (QKD) protocol with one-time pads. Our main contributions are: 1) a QMF-QSDC protocol that only relies on universal hashing of coded sequences without wiretap coding; 2) a set of privacy amplification theorems for extracting secrecy from coded classical sequences against quantum side-information. These tools open the way to the design of robust QMF-QSDC protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21313v1
- Title: Dispersive Microwave Sensing for Quantum Computing with Floating Electrons
- Authors: Yiran Tian
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2601.21313v1  pdf=https://arxiv.org/pdf/2601.21313v1.pdf

Abstract:
In this dissertation, resonator-based readout techniques were developed for floating electrons as qubits on cryogenic substrates, using two platforms: electrons on liquid helium and electrons on solid neon. In addition, a cryogenic microwave source was developed to enable low-noise measurement for qubit readout.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21318v1
- Title: QCL-IDS: Quantum Continual Learning for Intrusion Detection with Fidelity-Anchored Stability and Generative Replay
- Authors: Zirui Zhu, Xiangyang Li
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2601.21318v1  pdf=https://arxiv.org/pdf/2601.21318v1.pdf

Abstract:
Continual intrusion detection must absorb newly emerging attack stages while retaining legacy detection capability under strict operational constraints, including bounded compute and qubit budgets and privacy rules that preclude long-term storage of raw telemetry. We propose QCL-IDS, a quantum-centric continual-learning framework that co-designs stability and privacy-governed rehearsal for NISQ-era pipelines. Its core component, Q-FISH (Quantum Fisher Anchors), enforces retention using a compact anchor coreset through (i) sensitivity-weighted parameter constraints and (ii) a fidelity-based functional anchoring term that directly limits decision drift on representative historical traffic. To regain plasticity without retaining sensitive flows, QCL-IDS further introduces privacy-preserved quantum generative replay (QGR) via frozen, task-conditioned generator snapshots that synthesize bounded rehearsal samples. Across a three-stage attack stream on UNSW-NB15 and CICIDS2017, QCL-IDS consistently attains the best retention-adaptation trade-off: the gradient-anchor configuration achieves mean Attack-F1 = 0.941 with forgetting = 0.005 on UNSW-NB15 and mean Attack-F1 = 0.944 with forgetting = 0.004 on CICIDS2017, versus 0.800/0.138 and 0.803/0.128 for sequential fine-tuning, respectively.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21332v1
- Title: Robust Floquet Topological Phases and Anomalous $π$-Modes in Quasiperiodic Quantum Walks
- Authors: F. Iwase
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21332v1  pdf=https://arxiv.org/pdf/2601.21332v1.pdf

Abstract:
We uncover the global topological phase diagram of one-dimensional discrete-time quantum walks driven by Fibonacci-modulated coin parameters. Utilizing the mean chiral displacement (MCD) as dynamical probe, we identify robust topological phases defined by a strictly quantized winding number $ν=-1$ and exponentially localized edge states. Crucially, we discover that these topological edge modes emerges not only at zero energy but also at the quasienergy zone boundary $E=π$, exhibiting identical localization robustness despite the fractal nature of the bulk spectrum. These results demonstrate that Floquet topological protection remains intact amidst quasiperiodic disorder, offering a concrete route to observing exotic non-equilibrium phases in photonic experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21385v1
- Title: A general framework for interactions between electron beams and quantum optical systems
- Authors: Jakob M. Grzesik, Aviv Karnieli, Charles Roques-Carmes, Dylan S. Black, Trung Kiên Lê, Olav Solgaard, Shanhui Fan, Jelena Vučković
- Categories: quant-ph (primary); quant-ph; physics.acc-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2601.21385v1  pdf=https://arxiv.org/pdf/2601.21385v1.pdf

Abstract:
We provide a theoretical framework to describe the dynamics of a free-electron beam interacting with quantized bound systems in arbitrary electromagnetic environments. This expands the quantum optics toolbox to incorporate free-electron beams for applications in highly tunable quantum control, imaging, and spectroscopy at the nanoscale. The framework recovers previously studied results and shows that electromagnetic environments can amplify the intrinsically weak coupling between a free-electron and a bound electron to reach previously inaccessible interaction regimes. We leverage this enhanced coupling for experimentally feasible protocols in coherent qubit control and towards the nondestructive readout and projective control of the electron beam's quantum-number statistics. Our framework is broadly applicable to microwave-frequency qubits, optical nanophotonics, cavity quantum electrodynamics, and emerging platforms at the interface of electron microscopy and quantum information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21398v1
- Title: Quantum steering probes energy transfer in quantum batteries
- Authors: Meng-Long Song, Zan Cao, Xue-Ke Song, Liu Ye, Dong Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21398v1  pdf=https://arxiv.org/pdf/2601.21398v1.pdf

Abstract:
This study investigates the role of EPR steering in characterizing the energy dynamics of quantum batteries (QBs) within \textcolor{black}{a charging system that features shared reservoirs. After optimizing parameter configurations to achieve high-energy systems, we observe across a variety of charging scenarios with low-dissipation regimes that steering serves as a vital resource: it is initially stored until the system reaches energy equilibrium, and then subsequently utilized to sustain the enhancement of energy storage. Furthermore, steering acts as a witness to battery population balance and a consumable that enhances extractable work. Additionally, we discuss the contribution of the steering potential to energy upon high-dissipation charging in details. These findings establish a novel indicator for monitoring QB energy variations, which will be beneficial to achieve the high-performance quantum batteries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21435v1
- Title: Optimized adiabatic-impulse protocol preserving Kibble-Zurek scaling with attenuated anti-Kibble-Zurek behavior
- Authors: Han-Chuan Kou, Zhi-Han Zhang, Xin-Hui Wu, Yan Zhou, Gang Chen, Peng Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21435v1  pdf=https://arxiv.org/pdf/2601.21435v1.pdf

Abstract:
We propose an optimized adiabatic-impulse (OAI) protocol that achieves much shorter evolution time while preserving the Kibble-Zurek scaling. Near the critical regime, the control field is linearly ramped across the quantum critical point at a rate characterized by a quench time $τ_Q$. Away from the critical regime, the evolution is designed to follow the threshold of adiabatic breakdown, which we characterize by an adiabatic coefficient $ζ\proptoτ_Q^α$. As a consequence, the total evolution time exhibits a sublinear power-law dependence on $τ_Q$, and the conventional linear quench protocol is recovered in the limit $α\rightarrow\infty$. We apply the OAI protocol to the transverse Ising chain and numerically determine the minimum value of $ζ$. We further investigate the nonequilibrium dynamics in the presence of a noisy field that can induce anti-Kibble-Zurek behavior, leading to more defects for slower ramps. Within the OAI protocol, the optimal quench time that minimizes defects obeys an altered universal power-law scaling with the noise strength. Finally, we generalize the OAI protocol to incorporate nonlinear Kibble-Zurek scaling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21472v1
- Title: In-situ benchmarking of fault-tolerant quantum circuits. I. Clifford circuits
- Authors: Xiao Xiao, Dominik Hangleiter, Dolev Bluvstein, Mikhail D. Lukin, Michael J. Gullans
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21472v1  pdf=https://arxiv.org/pdf/2601.21472v1.pdf

Abstract:
Benchmarking physical devices and verifying logical algorithms are important tasks for scalable fault-tolerant quantum computing. Numerous protocols exist for benchmarking devices before running actual algorithms. In this work, we show that both physical and logical errors of fault-tolerant circuits can even be characterized in-situ using syndrome data. To achieve this, we map general fault-tolerant Clifford circuits to subsystem codes using the spacetime code formalism and develop a scheme for estimating Pauli noise in Clifford circuits using syndrome data. We give necessary and sufficient conditions for the learnability of physical and logical noise from given syndrome data, and show that we can accurately predict logical fidelities from the same data. Importantly, our approach requires only a polynomial sample size, even when the logical error rate is exponentially suppressed by the code distance, and thus gives an exponential advantage against methods that use only logical data such as direct fidelity estimation. We demonstrate the practical applicability of our methods in various scenarios using synthetic data as well as the experimental data from a recent demonstration of fault-tolerant circuits by Bluvstein et al. [Nature 626, 7997 (2024)]. Our methods provide an efficient, in-situ way of characterizing a fault-tolerant quantum computer to help gate calibration, improve decoding accuracy, and verify logical circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21499v1
- Title: RF-free driving of nuclear spins with color centers in silicon carbide
- Authors: Raphael Wörnle, Jonathan Körber, Timo Steidl, Georgy V. Astakhov, Durga B. R. Dasari, Florian Kaiser, Vadim Vorobyov, Jörg Wrachtrup
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21499v1  pdf=https://arxiv.org/pdf/2601.21499v1.pdf

Abstract:
Color centers that enable nuclear-spin control without RF fields offer a powerful route towards simplified and scalable quantum devices. Such capabilities are especially valuable for quantum sensing and computing platforms that already find applications in biology, materials science, and geophysics. A key challenge is the coherent manipulation of nearby nuclear spins, which serve as quantum memories and auxiliary qubits but conventionally require additional high-power RF fields which increase the experimental complexity and overall power consumption. Finding systems where both electron and nuclear spins can be controlled using a single MW source is therefore highly desirable. Here, using a modified divacancy center in silicon carbide, we show that coherent control of a coupled nuclear spin is possible without any RF fields. Instead, MW pulses driving the electron spin also manipulate the nuclear spin through hyperfineenhanced effects, activated by a precisely tilted external magnetic field. We demonstrate high-fidelity nuclear-spin control, achieving 89% two-qubit tomography fidelity and nearly T1-limited nuclear coherence times. This approach offers a simplified and scalable route for future quantum applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21507v1
- Title: Quantum Simulation with Fluxonium Qutrit Arrays
- Authors: Ivan Amelio, Quentin Ficheux, Nathan Goldman
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21507v1  pdf=https://arxiv.org/pdf/2601.21507v1.pdf

Abstract:
Fluxonium superconducting circuits were originally proposed to realize highly coherent qubits. In this work, we explore how these circuits can be used to implement and harness qutrits, by tuning their energy levels and matrix elements via an external flux bias. In particular, we investigate the distinctive features of arrays of fluxonium qutrits, and their potential for the quantum simulation of exotic quantum matter. We identify four different operational regimes, classified according to the plasmon-like versus fluxon-like nature of the qutrit excitations. Highly tunable on-site interactions are complemented by correlated single-particle hopping, pair hopping and non-local interactions, which naturally emerge and have different weights in the four regimes. Dispersive corrections and decoherence are also analyzed. We investigate the rich ground-state phase diagram of qutrit arrays and propose practical dynamical experiments to probe the different regimes. Altogether, fluxonium qutrit arrays emerge as a versatile and experimentally accessible platform to explore strongly correlated bosonic matter beyond the Bose-Hubbard paradigm, and with a potential toward simulating lattice gauge theories and non-Abelian topological states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21528v1
- Title: High-Coherence and High-frequency Quantum Computing: The Design of a High-Frequency, High-Coherence and Scalable Quantum Computing Architecture
- Authors: Masroor H. S. Bukhari
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21528v1  pdf=https://arxiv.org/pdf/2601.21528v1.pdf

Abstract:
High-coherence, fault-tolerant and scalable quantum computing architectures with unprecedented long coherence times, faster gates, low losses and low bit-flip errors may be one of the only ways forward to achieve the true quantum advantage. In this context, high-frequency high-coherence (HCQC) qubits with new high-performance topologies could be a significant step towards efficient and high-fidelity quantum computing by facilitating compact size, higher scalability and higher than conventional operating temperatures. Although transmon type qubits are designed and manufactured routinely in the range of a few Giga-Hertz, normally from 4 to 6 GHz (and, at times, up to around 10GHz), achieving higher-frequency operation has challenges and entails special design and manufacturing considerations. This report presents the proposal and preliminary design of an 8-qubit transmon (with possible upgrade to up to 72 qubits on a chip) architecture working beyond an operation frequency of 10GHz, as well as presents a new connection topology. The current design spans a range of around 11 to 13.5 GHz (with a possible full range of 9-12GHz at the moment), with a central optimal operating frequency of 12.0 GHz, with the aim to possibly achieve a stable, compact and low-charge-noise operation, as lowest as possible as per the existing fabrication techniques. The aim is to achieve average relaxation times of up to 1.9ms with average quality factors of up to 2.75 x 10^7 after trials, while exploiting the new advances in superconducting junction manufacturing using tantalum and niobium/aluminum/aluminum oxide tri-layer structures on high-resistivity silicon substrates (carried out elsewhere by other groups and referred in this report).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21544v1
- Title: Cooperative Emission from Quantum Emitters in Hexagonal Boron Nitride Layers
- Authors: Igor Khanonkin, Amir Sivan, Le Liu, Johannes Eberle, Kenji Watanabe, Takashi Taniguchi, Gadi Eisenstein, Meir Orenstein
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21544v1  pdf=https://arxiv.org/pdf/2601.21544v1.pdf

Abstract:
Collective light emission from many-body quantum systems is a cornerstone of quantum optics, yet its implementation in solid-state platforms operating under ambient conditions remains highly challenging. Large-bandgap van der Waals materials such as hexagonal boron nitride (hBN) host stable room-temperature single-photon emitters with narrow linewidths across a broad spectral range. However, cooperative radiative effects in this system have not been previously explored. Here we demonstrate collective emission from quantum-emitter ensembles in hBN layers when the emitters are nearly indistinguishable and positioned within a sub-wavelength proximity. Using confocal microscopy and a Hanbury Brown-Twiss (HBT) configuration, we identify both isolated emitters and ensembles activated by localized electron-beam irradiation. Time-resolved photoluminescence measurements reveal a superlinear intensity enhancement and a pronounced acceleration of the radiative decay in tightly confined ensembles, with lifetimes approaching the temporal resolution of our experimental system (about 500 ps), compared to approximately 1.85 ns for single emitters or large, spatially extended ensembles. Complementary second-order photon-correlation measurements exhibit sub-Poissonian antidip consistent with emission from a few indistinguishable emitters. The simultaneous observation of lifetime shortening and enhanced emission provides direct evidence of cooperative emission at room temperature, achieved without optical cavities or cryogenic cooling. These results establish optically active defect ensembles in hBN as a scalable solid-state platform for engineered collective quantum optics in two-dimensional materials, opening avenues toward ultrabright superradiant light sources and nonclassical photonic states for quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21555v1
- Title: Entanglement of quantum systems via a classical mediator in hybrid van Hove theory
- Authors: Sebastian Ulbricht, Andrés Darío Bermúdez Manjarres, Marcel Reginatto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21555v1  pdf=https://arxiv.org/pdf/2601.21555v1.pdf

Abstract:
It is a matter of ongoing discussion whether quantum states can become entangled while only interacting via a classical mediator. This lively debate is deeply interwoven with the question of whether entanglement studies can prove the quantum nature of gravity. However, the answer to this fundamental question depends crucially on which hybrid quantum-classical theory is used. In this letter, we demonstrate that entanglement by a classical mediator is possible within the framework of hybrid van Hove theory, showing that existing no-go theorems on that matter do not universally apply to hybrid theories in general. After briefly recapitulating the key features of the hybrid van Hove theory, we show this using the example of two quantum spins coupled by a classical harmonic oscillator. By deriving the spin density matrix for this scenario and comparing it to its equivalent for a pure quantum system, we show that entanglement between the two spins is generated in both cases. Conclusively, this is illustrated by presenting the purity and concurrence of the spin-spin system as a decisive measure for entanglement. Our results further imply that quantum entanglement studies cannot rule out consistent quantum theories featuring classical gravity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21616v1
- Title: A biased-erasure cavity qubit with hardware-efficient quantum error detection
- Authors: Jiasheng Mai, Qiyu Liu, Xiaowei Deng, Yanyan Cai, Zhongchu Ni, Libo Zhang, Ling Hu, Pan Zheng, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21616v1  pdf=https://arxiv.org/pdf/2601.21616v1.pdf

Abstract:
Erasure qubits are beneficial for quantum error correction due to their relaxed threshold requirements. While dual-rail erasure qubits have been demonstrated with a strong error hierarchy in circuit quantum electrodynamics, biased-erasure qubits -- where erasures originate predominantly from one logical basis state -- offer further advantages. Here, we realize a hardware-efficient biased-erasure qubit encoded in the vacuum and two-photon Fock states of a single microwave cavity. The qubit exhibits an erasure bias ratio of over 265. By using a transmon ancilla for logical measurements and mid-circuit erasure detections, we achieve logical state assignment errors below 1% and convert over 99.3% leakage errors into detected erasures. After postselection against erasures, we achieve effective logical relaxation and dephasing rates of $(6.2~\mathrm{ms})^{-1}$ and $(3.1~\mathrm{ms})^{-1}$, respectively, which exceed the erasure error rate by factors of 31 and 15, establishing a strong error hierarchy within the logical subspace. These postselected error rates indicate a coherence gain of about 6.0 beyond the break-even point set by the best physical qubit encoded in the two lowest Fock states in the cavity. Moreover, randomized benchmarking with interleaved erasure detections reveals a residual logical gate error of 0.29%. This work establishes a compact and hardware-efficient platform for biased-erasure qubits, promising concatenations into outer-level stabilizer codes toward fault-tolerant quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21629v1
- Title: Reinforcement Learning for Adaptive Composition of Quantum Circuit Optimisation Passes
- Authors: Daniel Mills, Ifan Williams, Jacob Swain, Gabriel Matos, Enrico Rinaldi, Alexander Koziell-Pipe
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2601.21629v1  pdf=https://arxiv.org/pdf/2601.21629v1.pdf

Abstract:
Many quantum software development kits provide a suite of circuit optimisation passes. These passes have been highly optimised and tested in isolation. However, the order in which they are applied is left to the user, or else defined in general-purpose default pass sequences. While general-purpose sequences miss opportunities for optimisation which are particular to individual circuits, designing pass sequences bespoke to particular circuits requires exceptional knowledge about quantum circuit design and optimisation. Here we propose and demonstrate training a reinforcement learning agent to compose optimisation-pass sequences. In particular the agent's action space consists of passes for two-qubit gate count reduction used in default PyTKET pass sequences. For the circuits in our diverse test set, the (mean, median) fraction of two-qubit gates removed by the agent is $(57.7\%, \ 56.7 \%)$, compared to $(41.8 \%, \ 50.0 \%)$ for the next best default pass sequence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21715v1
- Title: Hierarchical quantum decoders
- Authors: Nirupam Basak, Ankith Mohan, Andrew Tanggara, Tobias Haug, Goutam Paul, Kishor Bharti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21715v1  pdf=https://arxiv.org/pdf/2601.21715v1.pdf

Abstract:
Decoders are a critical component of fault-tolerant quantum computing. They must identify errors based on syndrome measurements to correct quantum states. While finding the optimal correction is NP-hard and thus extremely difficult, approximate decoders with faster runtime often rely on uncontrolled heuristics. In this work, we propose a family of hierarchical quantum decoders with a tunable trade-off between speed and accuracy while retaining guarantees of optimality. We use the Lasserre Sum-of-Squares (SOS) hierarchy from optimization theory to relax the decoding problem. This approach creates a sequence of Semidefinite Programs (SDPs). Lower levels of the hierarchy are faster but approximate, while higher levels are slower but more accurate. We demonstrate that even low levels of this hierarchy significantly outperform standard Linear Programming relaxations. Our results on rotated surface codes and honeycomb color codes show that the SOS decoder approaches the performance of exact decoding. We find that Levels 2 and 3 of our hierarchy perform nearly as well as the exact solver. We analyze the convergence using rank-loop criteria and compare the method against other relaxation schemes. This work bridges the gap between fast heuristics and rigorous optimal decoding.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21746v1
- Title: Quantum Random Features: A Spectral Framework for Quantum Machine Learning
- Authors: Akitada Sakurai, Aoi Hayashi, William John Munro, Kae Nemoto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21746v1  pdf=https://arxiv.org/pdf/2601.21746v1.pdf

Abstract:
Quantum machine learning (QML) models often require deep, parameterized circuits to capture complex frequency components, limiting their scalability and near-term implementation. We introduce \textit{Quantum Random Features} (QRF) and \textit{Quantum Dynamical Random Features} (QDRF), lightweight quantum reservoir models inspired by classical random Fourier features (RFF) that generate high-dimensional spectral representations without variational optimization. Using $Z$-rotation encoding combined with random permutations or Hamiltonian dynamics, these models achieve $N_f$-dimensional feature maps at preprocessing cost $O(\log(N_f))$. Spectral analysis shows that QRF and QDRF reproduce the behavior of RFF, while simulations on Fashion-MNIST reach up to 89.3\% accuracy-matching or surpassing classical baselines with scalable qubit requirements. By linking spectral theory with experimentally feasible quantum dynamics, this work provides a compact and hardware-compatible route to scalable quantum learning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21801v1
- Title: A geometric criterion for optimal measurements in multiparameter quantum metrology
- Authors: Jing Yang, Satoya Imai, Luca Pezzè
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21801v1  pdf=https://arxiv.org/pdf/2601.21801v1.pdf

Abstract:
Determining when the multiparameter quantum Cramér--Rao bound (QCRB) is saturable with experimentally relevant single-copy measurements is a central open problem in quantum metrology. Here we establish an equivalence between QCRB saturation and the simultaneous hollowization of a set of traceless operators associated with the estimation model, i.e., the existence of complete (generally nonorthogonal) bases in which all corresponding diagonal matrix elements vanish. This formulation yields a geometric characterization: optimal rank-one measurement vectors are confined to a subspace orthogonal to a state-determined Hermitian span. This provides a direct criterion to construct optimal Positive Operator-Valued Measures(POVMs). We then identify conditions under which the partial commutativity condition proposed in [Phys. Rev. A 100, 032104(2019)] becomes necessary and sufficient for the saturation of the QCRB, demonstrate that this condition is not always sufficient, and prove the counter-intuitive uselessness of informationally-complete POVMs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21806v1
- Title: Schroedinger's principle eliminates the EPR-locality paradox
- Authors: Walter F. Wreszinski
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2601.21806v1  pdf=https://arxiv.org/pdf/2601.21806v1.pdf

Abstract:
We introduce a principle, implicitly contained in Schroedinger's paper (Schr35), which allows a proof of the non-existence of the EPR-locality paradox in the Copenhagen interpretation of quantum mechanics. The paradox is shown to be well-posed already in the simplest example of an entangled state of two spins one-half, independently of the (well-taken) objections by Araki and Yanase that the measurement of spin is not a local measurement. We assume that any measurement results in the collapse of the wave-packet.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21838v1
- Title: Error-detectable Universal Control for High-Gain Bosonic Quantum Error Correction
- Authors: Weizhou Cai, Zi-Jie Chen, Ming Li, Qing-Xuan Jie, Xu-Bo Zou, Guang-Can Guo, Luyan Sun, Chang-Ling Zou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21838v1  pdf=https://arxiv.org/pdf/2601.21838v1.pdf

Abstract:
Protecting quantum information through quantum error correction (QEC) is a cornerstone of future fault-tolerant quantum computation. However, current QEC-protected logical qubits have only achieved coherence times about twice those of their best physical constituents. Here, we show that the primary barrier to higher QEC gains is ancilla-induced operational errors rather than intrinsic cavity coherence. To overcome this bottleneck, we introduce error-detectable universal control of bosonic modes, wherein ancilla relaxation events are detected and the corresponding trajectories discarded, thereby suppressing operational errors on logical qubits. For binomial codes, we demonstrate universal gates with fidelities exceeding $99.6\%$ and QEC gains of $8.33\times$ beyond break-even. Our results establish that gains beyond $10\times$ are achievable with state-of-the-art devices, establishing a path toward fault-tolerant bosonic quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21863v1
- Title: A Bravyi-König theorem for Floquet codes generated by locally conjugate instantaneous stabiliser groups
- Authors: Jelena Mackeprang, Jonas Helsen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21863v1  pdf=https://arxiv.org/pdf/2601.21863v1.pdf

Abstract:
The Bravyi-König (BK) theorem is an important no-go theorem for the dynamics of topological stabiliser quantum error correcting codes. It states that any logical operation on a $D$-dimensional topological stabiliser code that can be implemented by a short-depth circuit acts on the codespace as an element of the $D$-th level of the Clifford hierarchy. In recent years, a new type of quantum error correcting codes based on Pauli stabilisers, dubbed Floquet codes, has been introduced. In Floquet codes, syndrome measurements are arranged such that they dynamically generate a codespace at each time step. Here, we show that the BK theorem holds for a definition of Floquet codes based on locally conjugate stabiliser groups. Moreover, we introduce and define a class of generalised unitaries in Floquet codes that need not preserve the codespace at each time step, but that combined with the measurements constitute a valid logical operation. We derive a canonical form of these generalised unitaries and show that the BK theorem holds for them too.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21869v1
- Title: Entanglement-Assisted Bosonic MAC: Achievable Rates and Covert Communication
- Authors: Yu-Chen Shen, Matthieu R. Bloch
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2601.21869v1  pdf=https://arxiv.org/pdf/2601.21869v1.pdf

Abstract:
We consider the problem of covert communication over the entanglement-assisted (EA) bosonic multiple access channel (MAC). We derive a closed-form achievable rate region for the general EA bosonic MAC using high-order phase-shift keying (PSK) modulation. Specifically, we demonstrate that in the low-photon regime the capacity region collapses into a rectangle, asymptotically matching the point-to-point capacity as multi-user interference vanishes. We also characterize an achievable covert throughput region, showing that entanglement assistance enables an aggregate throughput scaling of \(O(\sqrt{n} \log n)\) covert bits with the block length $n$ for both senders, surpassing the square-root law as in the point-to-point case. Our analysis reveals that the joint covertness constraint imposes a linear trade-off between the senders throughput.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21880v1
- Title: Rapid high-temperature initialisation and readout of spins in silicon with 10 THz photons
- Authors: Aidan G. McConnell, Nils Dessmann, Wojciech Adamczyk, Benedict N. Murdin, Lorenzo Amato, Nikolay V. Abrosimov, Sergey G. Pavlov, Gabriel Aeppli, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.optics
- Links: abs=https://arxiv.org/abs/2601.21880v1  pdf=https://arxiv.org/pdf/2601.21880v1.pdf

Abstract:
Each cycle of a quantum computation requires a quantum state initialisation. For semiconductor-based quantum platforms, initialisation is typically performed via slow microwave processes and usually requires cooling to temperatures where only the lowest quantum level is occupied. In silicon, boron atoms are the most common impurities. They bind holes in orbitals including an effective spin-3/2 ground state as well as excited states analogous to the Rydberg series for hydrogen. Here we show that initialisation temperature demands may be relaxed and speeds increased over a thousand-fold by importing, from atomic physics, the procedure of optical pumping via excited orbital states to preferentially occupy a target ground state spin. Spin relaxation within the orbital ground state of unstrained silicon is too fast to measure for conventional pulsed microwave technology, except at temperatures below 2 K, implying a need not only for fast state preparation but also fast state readout. Circularly polarised ~10 THz photon pulses from a free electron laser meet both needs at temperatures above 3 K: a 9 ps pulse enhances the population of one spin eigenstate for the "1s"-like ground state orbital, and the second interrogates this imbalance in spin population. Using parameters given by our data, we calculate that it should be possible to initialise 99% of spins for boron in strained silicon within 250 ps at 3 K. The speedup of both state preparation and measurement gained for THz rather than microwave photons should be explored for the many other solid state quantum systems hosting THz excitations potentially useful as intermediate states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21923v1
- Title: A scalable quantum-enhanced greedy algorithm for maximum independent set problems
- Authors: Elisabeth Wybo, Jami Rönkkö, Olli Hirviniemi, Jernej Rudi Finžgar, Martin Leib
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21923v1  pdf=https://arxiv.org/pdf/2601.21923v1.pdf

Abstract:
We investigate a hybrid quantum-classical algorithm for solving the Maximum Independent Set (MIS) problem on regular graphs, combining the Quantum Approximate Optimization Algorithm (QAOA) with a minimal degree classical greedy algorithm. The method leverages pre-computed QAOA angles, derived from depth-$p$ QAOA circuits on regular trees, to compute local expectation values and inform sequential greedy decisions that progressively build an independent set. This hybrid approach maintains shallow quantum circuit and avoids instance-specific parameter training, making it well-suited for implementation on current quantum hardware: we have implemented the algorithm on a 20 qubit IQM superconducting device to find independent sets in graphs with thousands of nodes. We perform tensor network simulations to evaluate the performance of the algorithm beyond the reach of current quantum hardware and compare to established classical heuristics. Our results show that even at low depth ($p=4$), the quantum-enhanced greedy method significantly outperforms purely classical greedy baselines as well as more sophisticated approximation algorithms. The modular structure of the algorithm and relatively low quantum resource requirements make it a compelling candidate for scalable, hybrid optimization in the NISQ era and beyond.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21930v1
- Title: Entropy production versus memory effects in two-level open quantum systems
- Authors: Guillaume Théret, Dominique Sugny, Camille L. Latune
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.21930v1  pdf=https://arxiv.org/pdf/2601.21930v1.pdf

Abstract:
We compare several definitions of entropy production rate introduced in the literature from a large variety of situations and motivations, and then analyze their relations with memory effects. Considering a relevant experimental example of a qubit interacting with a single bosonic mode playing the role of a finite bath, we show that all definitions of entropy production coincide at weak coupling. In the strong coupling regime, significant discrepancies emerge between the different entropy production rates, although some similarities in the overall behaviour remain. However, surprisingly, two of these definitions -- one based on local quantities of the system and the other on non-local quantities -- coincide exactly, even in the case of strong coupling. Finally, a high degree of correspondence is observed when memory effects characterized by P-divisibility are compared with the sign of all entropy production rates in the case of weak coupling. Such correspondence degrades at strong coupling, leading us to extend the concept of entropy production to the dynamical map. We show a perfect equivalence between the sign of this enlarged concept of entropy production and P-divisibility, both numerically and analytically, in the case of phase-covariant master equations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.22005v1
- Title: Hierarchy of discriminative power and complexity in learning quantum ensembles
- Authors: Jian Yao, Pengtao Li, Xiaohui Chen, Quntao Zhuang
- Categories: quant-ph (primary); quant-ph; math.ST; stat.ML
- Links: abs=https://arxiv.org/abs/2601.22005v1  pdf=https://arxiv.org/pdf/2601.22005v1.pdf

Abstract:
Distance metrics are central to machine learning, yet distances between ensembles of quantum states remain poorly understood due to fundamental quantum measurement constraints. We introduce a hierarchy of integral probability metrics, termed MMD-$k$, which generalizes the maximum mean discrepancy to quantum ensembles and exhibit a strict trade-off between discriminative power and statistical efficiency as the moment order $k$ increases. For pure-state ensembles of size $N$, estimating MMD-$k$ using experimentally feasible SWAP-test-based estimators requires $Θ(N^{2-2/k})$ samples for constant $k$, and $Θ(N^3)$ samples to achieve full discriminative power at $k = N$. In contrast, the quantum Wasserstein distance attains full discriminative power with $Θ(N^2 \log N)$ samples. These results provide principled guidance for the design of loss functions in quantum machine learning, which we illustrate in the training quantum denoising diffusion probabilistic models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.22006v1
- Title: Machine learning with minimal use of quantum computers: Provable advantages in Learning Under Quantum Privileged Information (LUQPI)
- Authors: Vasily Bokov, Lisa Kohl, Sebastian Schmitt, Vedran Dunjko
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.22006v1  pdf=https://arxiv.org/pdf/2601.22006v1.pdf

Abstract:
Quantum machine learning (QML) is often listed as a promising candidate for useful applications of quantum computers, in part due to numerous proofs of possible quantum advantages. A central question is how small a role quantum computers can play while still enabling provable learning advantages over classical methods. We study an especially restricted setting in which a quantum computer is used only as a feature extractor: it acts independently on individual data points, without access to labels or global dataset information, is available only to augment the training set, and is not available at deployment. Training and deployment are therefore carried out by fully classical learners on a dataset augmented with quantum-generated features. We formalize this model by adapting the classical framework of Learning Under Privileged Information (LUPI) to the quantum case, which we call Learning Under Quantum Privileged Information (LUQPI). Within this framework, we show that even such minimally involved quantum feature extraction, available only during training, can yield exponential quantum-classical separations for suitable concept classes and data distributions under reasonable computational assumptions. We further situate LUQPI within a taxonomy of related quantum and classical learning settings and show how standard classical machinery, most notably the SVM+ algorithm, can exploit quantum-augmented data. Finally, we present numerical experiments in a physically motivated many-body setting, where privileged quantum features are expectation values of observables on ground states, and observe consistent performance gains for LUQPI-style models over strong classical baselines.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.22011v1
- Title: Photonic Links for Spin-Based Quantum Sensors
- Authors: M. Reefaz Rahman, Karsten Schnier, Ryan Goldsmith, Benjamin J. Lawrie, Joseph M. Lukens, Seongsin M. Kim, Patrick Kung
- Categories: quant-ph (primary); quant-ph; physics.app-ph
- Links: abs=https://arxiv.org/abs/2601.22011v1  pdf=https://arxiv.org/pdf/2601.22011v1.pdf

Abstract:
A growing variety of optically accessible spin qubits have emerged in recent years as key components for quantum sensors, qubits, and quantum memories. However, the scalability of conventional spin-based quantum architectures remains limited by direct microwave delivery, which introduces thermal noise, electromagnetic cross-talk, and design constraints for cryogenic, high-field, and distributed systems. In this work, we present a unified framework for RF-over-fiber (RFoF) control of optically accessible spins through RFoF optically detected magnetic resonance (ODMR) spectroscopy of nitrogen-vacancy (NV) centers in diamond. The RFoF platform relies on an electro-optically modulated telecom-band laser that transmits microwave signals over fiber and a high-speed photodiode that recovers the RF waveform to drive NV center spin transitions. We obtain an RFoF efficiency of 1.81\% at 2.90~GHz, corresponding to $P_{\mathrm{RF,out}}=-0.7$~dBm. The RFoF architecture provides a path toward low-noise, thermally isolated, and cryo-compatible ODMR systems bridging conventional spin-based quantum sensing protocols with emerging distributed quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.22064v1
- Title: Thermodynamics of linear open quantum walks
- Authors: Pedro Linck Maciel, Nadja Kolb Bernardes
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.22064v1  pdf=https://arxiv.org/pdf/2601.22064v1.pdf

Abstract:
Open quantum systems interact with their environment, leading to nonunitary dynamics. We investigate the thermodynamics of linear Open Quantum Walks (OQWs), a class of quantum walks whose dynamics is entirely driven by the environment. We define an equilibrium temperature, identify a population inversion near a finite critical value of a control parameter, analyze the thermalization process, and develop the statistical mechanics needed to describe the thermodynamical properties of linear OQWs. We also study nonequilibrium thermodynamics by analyzing the time evolution of entropy, energy, and temperature, while providing analytical tools to understand the system's evolution as it converges to the thermalized state. We examine the validity of the second and third laws of thermodynamics in this setting. Finally, we employ these developments to shed light on dissipative quantum computation within the OQW framework.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.22091v1
- Title: Designing quantum technologies with a quantum computer
- Authors: Juan Naranjo, Thi Ha Kyaw, Gaurav Saxena, Kevin Ferreira, Jack S. Baker
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2601.22091v1  pdf=https://arxiv.org/pdf/2601.22091v1.pdf

Abstract:
Interacting spin systems in solids underpin a wide range of quantum technologies, from quantum sensors and single-photon sources to spin-defect-based quantum registers and processors. We develop a quantum-computer-aided framework for simulating such devices using a general electron spin resonance Hamiltonian incorporating zero-field splitting, the Zeeman effect, hyperfine interactions, dipole-dipole spin-spin terms, and electron-phonon decoherence. Within this model, we combine Gray-encoded qudit-to-qubit mappings, qubit-wise commuting aggregation, and a multi-reference selected quantum Krylov fast-forwarding (sQKFF) hybrid algorithm to access long-time dynamics while remaining compatible with NISQ and early fault-tolerant hardware constraints. Numerical simulations demonstrate the computation of autocorrelation functions up to $\sim100$ ns, together with microwave absorption spectra and the $\ell_1$-norm of coherence, achieving 18-30$\%$ reductions in gate counts and circuit depth for Trotterized time-evolution circuits compared to unoptimized implementations. Using the nitrogen vacancy center in diamond as a testbed, we benchmark the framework against classical simulations and identify the reference-state selection in sQKFF as the primary factor governing accuracy at fixed hardware cost. This methodology provides a flexible blueprint for using quantum computers to design, compare, and optimize solid-state spin-qubit technologies under experimentally realistic conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20924v1
- Title: Resource-Theoretic Quantifiers of Weak and Strong Symmetry Breaking: Strong Entanglement Asymmetry and Beyond
- Authors: Yuya Kusuki, Sridip Pal, Hiroyasu Tajima
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20924v1  pdf=https://arxiv.org/pdf/2601.20924v1.pdf

Abstract:
Quantifying how much a quantum state breaks a symmetry is essential for characterizing phases, nonequilibrium dynamics, and open-system behavior. Quantum resource theory provides a rigorous operational framework to define and characterize such quantifiers of symmetry-breaking. As a starter, we exemplify the usefulness of resource theory by noting that second-Rényi entanglement asymmetry can increase under symmetric operations, and hence is not a resource monotone, and should not solely be used to capture Quantum Mpemba effect. More importantly, motivated by mixed-state physics where weak and strong symmetries are inequivalent, we formulate a new resource theory tailored to strong symmetry, identifying free states and strong-covariant operations. This framework systematically identifies quantifiers of strong symmetry breaking for a broad class of symmetry groups, including a strong entanglement asymmetry. A particularly transparent structure emerges for U(1) symmetry, where the resource theory for the strong symmetry breaking has a completely parallel structure to the entanglement theory: the variance of the conserved quantity fully characterizes the asymptotic manipulation of strong symmetry breaking. By connecting this result to the knowledge of the geometry of quantum state space, we obtain a quantitative framework to track how weak symmetry breaking is irreversibly converted into strong symmetry breaking in open quantum systems. We further propose extensions to generalized symmetries and illustrate the qualitative impact of strong symmetry breaking in analytically tractable QFT examples and applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20926v1
- Title: Quench spectroscopy of amplitude modes in a one-dimensional critical phase
- Authors: Hyunsoo Ha, David A. Huse, Rhine Samajdar
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.quant-gas; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20926v1  pdf=https://arxiv.org/pdf/2601.20926v1.pdf

Abstract:
We investigate the emergence of an amplitude (Higgs-like) mode in the gapless phase of the $(1+1)$D XXZ spin chain. Unlike conventional settings where amplitude modes arise from spontaneous symmetry breaking, here, we identify a symmetry-preserving underdamped excitation on top of a Luttinger-liquid ground state. Using nonequilibrium quench spectroscopy, we demonstrate that this mode manifests as oscillations of U(1)-symmetric observables following a sudden quench. By combining numerical simulations with Bethe-ansatz analyses, we trace its microscopic origin to specific families of string excitations. We further discuss experimental pathways to detect this mode in easy-plane quantum magnets and programmable quantum simulators. Our results showcase the utility of quantum quenches as a powerful tool to probe collective excitations, beyond the scope of linear response.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20951v1
- Title: Topological Acoustic Diode
- Authors: Ashwat Jain, Wojciech J. Jankowski, M. Mehraeen, Robert-Jan Slager
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20951v1  pdf=https://arxiv.org/pdf/2601.20951v1.pdf

Abstract:
We show that certain three-dimensional topological phases can act as acoustic diodes realizing nonlinear odd acoustoelastic effects. Beyond uncovering topologically-induced anomalous acoustic second-harmonic generation and rectification, we demonstrate how such nonlinear responses are uniquely captured by the momentum-space nonmetricity tensor in the quantum state Hilbert-space geometry. In addition to completing the classification of quantum geometric observables in the quadratic response regime, our findings reveal unexplored avenues for experimental realizations of acoustic diodes using effective $θ$ vacua of axion insulators adaptable for topological engineering applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.20954v1
- Title: Spectral Form Factor of Gapped Random Matrix Systems
- Authors: Krishan Saraswat
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2601.20954v1  pdf=https://arxiv.org/pdf/2601.20954v1.pdf

Abstract:
In this work, we study the spectral form factor of random matrix models which exhibit a large number of degenerate ground states accompanied by a macroscopic gap in the spectrum. The central aim of this work is to understand how the standard narrative about the behavior of the spectral form factor is modified in the presence of these parametrically large number of ground states. We show that, at sufficiently low temperatures, the spectral form factor is dominated by the disconnected contribution, even at arbitrarily late times. Moreover, we demonstrate that the connected form factor only depends on the eigenvalues of the non-degenerate sector. Using the Christoffel-Darboux kernel, we analyze a number of examples including the Bessel model and $\mathcal{N}=2$ Jackiw-Teitelboim supergravity. In these examples, we find damped oscillations in the disconnected form factor, with a period set by the inverse size of the gap. Furthermore, we demonstrate that the slope of the ramp in the connected form factor arises from a universal sine-kernel, which emerges from a truncation of the full non-perturbative kernel in the $\hbar \to 0$ limit, and find agreement with the leading double trumpet result. Finally, we present predictions for how the ramp will transition to a plateau in the connected form factor and demonstrate how the transition depends on the details of the leading spectral density of states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21134v1
- Title: Continuum mechanics of entanglement in noisy interacting fermion chains
- Authors: Tobias Swann, Adam Nahum
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.dis-nn; cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21134v1  pdf=https://arxiv.org/pdf/2601.21134v1.pdf

Abstract:
We develop an effective continuum description for information scrambling in a chain of randomly interacting Majorana fermions. The approach is based on the semiclassical treatment of the path integral for an effective spin chain that describes "two-replica" observables such as the entanglement purity and the OTOC. This formalism gives exact results for the entanglement membrane and for operator spreading in the limit of weak interactions. In this limit there is a large crossover lengthscale between free and interacting behavior, and this large lengthscale allows for a continuum limit and a controlled saddle-point calculation. The formalism is also somewhat different from that known from random unitary circuits. The entanglement membrane emerges as a kind of bound state of two travelling waves, and shows an interesting unbinding phenomenon as the velocity of the entanglement membrane approaches the butterfly velocity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21144v1
- Title: Generating persistent-current superpositions in Bose-Einstein condensates using dynamic optical potentials
- Authors: Renzo Testa, Donatella Cassettari
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21144v1  pdf=https://arxiv.org/pdf/2601.21144v1.pdf

Abstract:
Precise and flexible manipulation of the motional state of ultracold atoms is a fundamental enabling technology for diverse applications such as quantum sensing and quantum computation. In this paper we propose a general, simple and highly efficient method to engineer the motional state of a Bose-Einstein condensate with time-dependent optical fields, which can be realized experimentally with existing light sculpting techniques. We demonstrate numerically how to engineer superpositions of persistent currents in a toroidal trap, achieving very high fidelity. We also study in detail the stability of the state over time, and we present an analytical two-state model that approximates well the evolution of the state in presence of self-interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21145v1
- Title: On the quantum nature of strong gravity
- Authors: Felipe Sobrero, Luca Abrahão, Thiago Guerreiro
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21145v1  pdf=https://arxiv.org/pdf/2601.21145v1.pdf

Abstract:
Belenchia et al. [Phys. Rev. D 98, 126009 (2018)] have analyzed a gedankenexperiment where two observers, Alice and Bob, attempt to communicate via superluminal signals using a superposition of massive particles dressed by Newtonian fields and a test particle as field detector. Quantum fluctuations in the particle motion and in the field prevent signaling or violations of quantum mechanics in this setup. We reformulate this thought experiment by considering gravitational waves emitted by an extended quadrupolar object as a detector for Newtonian tidal fields. We find that quantum fluctuations in the gravitational waves prevent signaling. In the Newtonian limit, rotating black holes behave as extended quadrupolar objects, as consequence of the strong equivalence principle. It follows that consistency of the Newtonian limit of general relativity with quantum mechanics requires the quantization of gravitational radiation, even when the waves originate in strong gravity sources.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21310v1
- Title: A Deterministic Framework for Neural Network Quantum States in Quantum Chemistry
- Authors: Zheng Che
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21310v1  pdf=https://arxiv.org/pdf/2601.21310v1.pdf

Abstract:
Stochastic optimization of Neural Network Quantum States (NQS) in discrete Fock spaces is limited by sampling variance and slow mixing. We present a deterministic framework that optimizes a neural backflow ansatz within dynamically adaptive configuration subspaces, corrected by second-order perturbation theory. This approach eliminates Monte Carlo noise and, through a hybrid CPU-GPU implementation, exhibits sub-linear scaling with respect to subspace size. Benchmarks on bond dissociation in H2O and N2, and the strongly correlated chromium dimer Cr2, validate the method's accuracy and stability in large Hilbert spaces.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21330v1
- Title: Belief Propagation with Quantum Messages for Symmetric Q-ary Pure-State Channels
- Authors: Avijit Mandal, Henry D. Pfister
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21330v1  pdf=https://arxiv.org/pdf/2601.21330v1.pdf

Abstract:
Belief propagation with quantum messages (BPQM) provides a low-complexity alternative to collective measurements for communication over classical--quantum channels. Prior BPQM constructions and density-evolution (DE) analyses have focused on binary alphabets. Here, we generalize BPQM to symmetric q-ary pure-state channels (PSCs) whose output Gram matrix is circulant. For this class, we show that bit-node and check-node combining can be tracked efficiently via closed-form recursions on the Gram-matrix eigenvalues, independent of the particular physical realization of the output states. These recursions yield explicit BPQM unitaries and analytic bounds on the fidelities of the combined channels in terms of the input-channel fidelities. This provides a DE framework for symmetric q-ary PSCs that allows one to estimate BPQM decoding thresholds for LDPC codes and to construct polar codes on these channels.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21514v1
- Title: Transversal gates for quantum CSS codes
- Authors: Eduardo Camps-Moreno, Hiram H. López, Gretchen L. Matthews, Narayanan Rengaswamy, Rodrigo San-José
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21514v1  pdf=https://arxiv.org/pdf/2601.21514v1.pdf

Abstract:
In this paper, we focus on the problem of computing the set of diagonal transversal gates fixing a CSS code. We determine the logical actions of the gates as well as the groups of transversal gates that induce non-trivial logical gates and logical identities. We explicitly declare the set of equations defining the groups, a key advantage and differentiator of our approach. We compute the complete set of transversal stabilizers and transversal gates for any CSS code arising from monomial codes, a family that includes decreasing monomial codes and polar codes. As a consequence, we recover and extend some results in the literature on CSS-T codes, triorthogonal codes, and divisible codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21546v1
- Title: Quantum Otto cycle in the Anderson impurity model
- Authors: Salvatore Gatto, Alessandra Colla, Heinz-Peter Breuer, Michael Thoss
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21546v1  pdf=https://arxiv.org/pdf/2601.21546v1.pdf

Abstract:
We study the thermodynamic performance of a periodic quantum Otto cycle operating on the single-impurity Anderson model. Using a decomposition of the time-evolution generator based on the principle of minimal dissipation, combined with the numerically exact hierarchical equations of motion (HEOM) method, we analyze the operating regimes of the quantum thermal machine and investigate effects of Coulomb interactions, strong system-reservoir coupling, and energy level alignments. Our results show that Coulomb interaction can change the operating regimes and may lead to an enhancement of the efficiency.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21553v1
- Title: Strassen's support functionals coincide with the quantum functionals
- Authors: Keiya Sakabe, Mahmut Levent Doğan, Michael Walter
- Categories: cs.CC (primary); cs.CC; math.OC; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21553v1  pdf=https://arxiv.org/pdf/2601.21553v1.pdf

Abstract:
Strassen's asymptotic spectrum offers a framework for analyzing the complexity of tensors. It has found applications in diverse areas, from computer science to additive combinatorics and quantum information. A long-standing open problem, dating back to 1991, asks whether Strassen's support functionals are universal spectral points, that is, points in the asymptotic spectrum of tensors.   In this paper, we answer this question in the affirmative by proving that the support functionals coincide with the quantum functionals - universal spectral points that are defined via entropy optimization on entanglement polytopes. We obtain this result as a special case of a general minimax formula for convex optimization on entanglement polytopes (and other moment polytopes) that has further applications to other tensor parameters, including the asymptotic slice rank. Our proof is based on a recent Fenchel-type duality theorem on Hadamard manifolds due to Hirai.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21597v1
- Title: Non-secular polariton leakage and dark-state protection in hybrid plasmonic cavities
- Authors: Marco Vallone
- Categories: physics.optics (primary); physics.optics; cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21597v1  pdf=https://arxiv.org/pdf/2601.21597v1.pdf

Abstract:
A major issue in exploiting plasmonic cavities as key components in nanotechnology is the effect of radiative and absorption losses on their electrodynamic behavior. Treating them as open-systems, we derive a time-local, completely positive master equation that retains non-secular interference between decay pathways and reduces to the standard secular description when the environment resolves polariton splitting. When it does not, the theory predicts order-one deviations from secular leakage dynamics, including bath-induced coherences and stabilization of dark polaritons, and provides a simple design criterion based on the ratio of polariton splitting to reservoir linewidth. A time-resolved leakage measurement, such as transmission, reflectivity, or photoluminescence, can be used to observe these effects.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21604v1
- Title: Holographic Entanglement Propagation Through Wormholes
- Authors: Kazuki Doi, Liang Li, Ung Nguyen, Tadashi Takayanagi
- Categories: hep-th (primary); hep-th; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21604v1  pdf=https://arxiv.org/pdf/2601.21604v1.pdf

Abstract:
We study how energy and quantum entanglement are transferred when two identical CFTs are entangled locally. This is probed by considering a local operator insertion in one of the CFTs. When the CFTs have holographic duals via the AdS/CFT correspondence, the transfer happens through an AdS wormhole that allows signal propagation even beyond the horizon from one AdS boundary to the other; we demonstrate this in explicit CFT calculations. We argue that this transmission is possible because the insertion of a local operator is not a unitary process but a regularized version of projection measurement, and that this is interpreted as quantum teleportation. We also find that this leads to a phenomenon opposite to scrambling, where mutual information, instead of being suppressed, gets enhanced by the insertion of a local operator excitation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21625v1
- Title: Non-invertible translation from Lieb-Schultz-Mattis anomaly
- Authors: Tsubasa Oishi, Takuma Saito, Hiromi Ebisu
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21625v1  pdf=https://arxiv.org/pdf/2601.21625v1.pdf

Abstract:
Symmetry provides powerful non-perturbative constraints in quantum many-body systems. A prominent example is the Lieb-Schultz-Mattis (LSM) anomaly -- a mixed 't Hooft anomaly between internal and translational symmetries that forbids a trivial symmetric gapped phase. In this work, we investigate lattice translation operators in systems with an LSM anomaly. We construct explicit lattice models in two and three spatial dimensions and show that, after gauging the full internal symmetry, translation becomes non-invertible and fuses into defects of the internal symmetry. The result is supported by the anomaly-inflow in view of topological field theory. Our work extends earlier one-dimensional observations to a unified higher-dimensional framework and clarifies their origin in mixed anomalies and higher-group structures, highlighting a coherent interplay between internal and crystalline symmetries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21780v1
- Title: Quantum LEGO Learning: A Modular Design Principle for Hybrid Artificial Intelligence
- Authors: Jun Qi, Chao-Han Huck Yang, Pin-Yu Chen, Min-Hsiu Hsieh, Hector Zenil, Jesper Tegner
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21780v1  pdf=https://arxiv.org/pdf/2601.21780v1.pdf

Abstract:
Hybrid quantum-classical learning models increasingly integrate neural networks with variational quantum circuits (VQCs) to exploit complementary inductive biases. However, many existing approaches rely on tightly coupled architectures or task-specific encoders, limiting conceptual clarity, generality, and transferability across learning settings. In this work, we introduce Quantum LEGO Learning, a modular and architecture-agnostic learning framework that treats classical and quantum components as reusable, composable learning blocks with well-defined roles. Within this framework, a pre-trained classical neural network serves as a frozen feature block, while a VQC acts as a trainable adaptive module that operates on structured representations rather than raw inputs. This separation enables efficient learning under constrained quantum resources and provides a principled abstraction for analyzing hybrid models. We develop a block-wise generalization theory that decomposes learning error into approximation and estimation components, explicitly characterizing how the complexity and training status of each block influence overall performance. Our analysis generalizes prior tensor-network-specific results and identifies conditions under which quantum modules provide representational advantages over comparably sized classical heads. Empirically, we validate the framework through systematic block-swap experiments across frozen feature extractors and both quantum and classical adaptive heads. Experiments on quantum dot classification demonstrate stable optimization, reduced sensitivity to qubit count, and robustness to realistic noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21874v1
- Title: Quotient geometry of tensor ring decomposition
- Authors: Bin Gao, Renfeng Peng, Ya-xiang Yuan
- Categories: math.NA (primary); math.NA; math.OC; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21874v1  pdf=https://arxiv.org/pdf/2601.21874v1.pdf

Abstract:
Differential geometries derived from tensor decompositions have been extensively studied and provided the foundations for a variety of efficient numerical methods. Despite the practical success of the tensor ring (TR) decomposition, its intrinsic geometry remains less understood, primarily due to the underlying ring structure and the resulting nontrivial gauge invariance. We establish the quotient geometry of TR decomposition by imposing full-rank conditions on all unfolding matrices of the core tensors and capturing the gauge invariance. Additionally, the results can be extended to the uniform TR decomposition, where all core tensors are identical. Numerical experiments validate the developed geometries via tensor ring completion tasks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21875v1
- Title: Defect Relative Entropy
- Authors: Mostafa Ghasemi
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21875v1  pdf=https://arxiv.org/pdf/2601.21875v1.pdf

Abstract:
We introduce the concept of \textit{defect relative entropy} as a measure of distinguishability within the space of defects. We compute the defect relative entropy for conformal/topological defects, deriving a universal formula in conformal field theories (CFTs) on a circle. This formula reduces to the Kullback-Leibler divergence. Furthermore, we provide a detailed expression of the defect relative entropy for diagonal CFTs with specific topological defect choices, utilizing the theory's modular $\mathcal{S}$ matrix. We also present a general formula for the \textit{ defect sandwiched Rényi relative entropy} and the \textit{defect fidelity}. Through explicit calculations in specific models, including the Ising model, the tricritical Ising model, and the $\widehat{su}(2)_{k}$ WZW model, we have made an intriguing finding: zero defect relative entropy between reduced density matrices associated with certain topological defect. Notably, we introduce the concept of the \textit{defect relative sector}, representing the set of topological defects with zero defect relative entropy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21928v1
- Title: Bound-state-free Förster resonant shielding of strongly dipolar ultracold molecules
- Authors: Reuben R. W. Wang
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21928v1  pdf=https://arxiv.org/pdf/2601.21928v1.pdf

Abstract:
We propose a method to suppress collisional loss in strongly dipolar, rotationally excited ultracold molecules using a combination of static (dc) and microwave (ac) electric fields. By tuning two excited pair molecular rotational states into a Förster resonance with a dc field, simultaneously driving excited rotational transitions with an ac field removes all long-range bound states, allowing near complete suppression of all two- and three-body collisional loss channels. While permitting tunable dipolar and anti-dipolar interactions, this bound-state-free ac/dc scheme is not subject to photon-changing collisions that are the primary source of two-body loss in shielding with two microwave fields, used to achieve the first molecular Bose-Einstein condensate [Bigagli et al., Nature 631, 289 (2024)]. Using NaCs as a representative example for strongly dipolar molecules, close-coupling calculations are performed to show that bound-state-free shielding can achieve ratios of elastic-to-loss rates $\gtrsim 10^{6}$ at 100 nK, with currently accessible ac and dc field generation technologies. This work opens new opportunities for realizing large, long-lived samples of strongly interacting degenerate molecular gases with tunable long-range interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.21953v1
- Title: Fabrication effects on Niobium oxidation and surface contamination in Niobium-metal bilayers using X-ray photoelectron spectroscopy
- Authors: Tathagata Banerjee, Maciej W. Olszewski, Valla Fatemi
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2601.21953v1  pdf=https://arxiv.org/pdf/2601.21953v1.pdf

Abstract:
Superconducting resonators and qubits are limited by dielectric losses from surface oxides. Surface oxides are mitigated through various strategies such as the addition of a metal capping layer, surface passivation, and acid processing. In this study, we demonstrate the use of X-ray photoelectron spectroscopy (XPS) as a rapid characterization tool to study the effectiveness cap layers for niobium for further device fabrication. We non-destructively evaluate 17 capping layers to characterize their ability to prevent oxygen diffusion, and the effects of standard fabrication processes -- annealing, resist stripping, and acid cleaning. We downselect for resilient capping layers and test their microwave resonator performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.22140v1
- Title: Quantum fluctuations in hydrodynamics and quantum long-time tails
- Authors: Akash Jain
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; hep-ph; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2601.22140v1  pdf=https://arxiv.org/pdf/2601.22140v1.pdf

Abstract:
We construct a quantum Schwinger-Keldysh (SK) effective field theory for the diffusive hydrodynamics of a conserved scalar field. Quantum corrections within the SK framework are guided by fluctuation-dissipation relations, enforced via a dynamical Kubo-Martin-Schwinger (KMS) symmetry. We find that the KMS symmetry necessarily generates fluctuation contributions in the SK effective action at all orders in the noise field, thereby giving rise to intrinsically non-Gaussian noise. We use our results to compute one-loop quantum corrections to the two-point density-density retarded correlation function, leading to a quantum generalization of hydrodynamic long-time tails. Our results apply at arbitrarily high orders in $\hbar$. The one-loop results for retarded correlation functions have been expressed in terms of a family of polynomials. We also provide a closed-form expression for the one-loop results at leading order in the wavevector expansion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2309.12290v2
- Title: Compatibility of Generalized Noisy Qubit Measurements
- Authors: Martin J. Renner
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2309.12290v2  pdf=https://arxiv.org/pdf/2309.12290v2.pdf

Abstract:
It is a crucial feature of quantum mechanics that not all measurements are compatible with each other. However, if measurements suffer from noise they may lose their incompatibility. Here, we consider the effect of white noise and determine the critical visibility such that all qubit measurements, i.e. all positive operator-valued measures (POVMs), become compatible, i.e. jointly measurable. In addition, we apply our methods to quantum steering and Bell nonlocality. We obtain a tight local hidden state model for two-qubit Werner states of visibility $1/2$. This determines the exact steering bound for two-qubit Werner states and also provides a local hidden variable model that improves on previously known models. Interestingly, this proves that POVMs are not more powerful than projective measurements to demonstrate quantum steering for these states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2405.03261v2
- Title: Characterizing high-dimensional multipartite entanglement beyond Greenberger-Horne-Zeilinger fidelities
- Authors: Shuheng Liu, Qiongyi He, Marcus Huber, Giuseppe Vitagliano
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2405.03261v2  pdf=https://arxiv.org/pdf/2405.03261v2.pdf

Abstract:
Characterizing entanglement of systems composed of multiple particles is a very complex problem that is attracting increasing attention across different disciplines related to quantum physics. The task becomes even more complex when the particles have many accessible levels, i.e., they are of high dimension, which leads to a potentially high-dimensional multipartite entangled state. These are important resources for an ever-increasing number of tasks, especially when a network of parties needs to share highly entangled states, e.g., for communicating more efficiently and securely. For these applications, as well as for purely theoretical arguments, it is important to be able to certify both the high-dimensional and the genuine multipartite nature of entangled states, possibly based on simple measurements. Here we derive a novel method that achieves this and improves over typical entanglement witnesses like the fidelity with respect to states of a Greenberger-Horne-Zeilinger (GHZ) form, without needing more complex measurements. We test our condition on paradigmatic classes of high-dimensional multipartite entangled states like imperfect GHZ states with random noise, as well as on purely randomly chosen ones and find that, in comparison with other available criteria our method provides a significant advantage and is often also simpler to evaluate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2412.07653v5
- Title: Statistics of Abelian topological excitations
- Authors: Hanyu Xue
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; math-ph
- Links: abs=https://arxiv.org/abs/2412.07653v5  pdf=https://arxiv.org/pdf/2412.07653v5.pdf

Abstract:
In this paper, we develop a novel theory that generalizes the concept of anyon statistics to Abelian topological excitations of any dimension. We axiomatize excitations as a selected collection of states and operators satisfying the configuration axiom and the locality axiom, purely based on many-body quantum mechanics. Upon these axioms, we define a rigorous and self-contained theory of statistics using only basic algebra and can be implemented on a computer. While our theory is developed independently, the results align with existing physical theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2412.09781v2
- Title: A 3D lattice defect and efficient computations in topological MBQC
- Authors: Gabrielle Tournaire, Marvin Schwiering, Robert Raussendorf, Sven Bachmann
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2412.09781v2  pdf=https://arxiv.org/pdf/2412.09781v2.pdf

Abstract:
We describe an efficient, fully fault-tolerant implementation of Measurement-Based Quantum Computation (MBQC) in the 3D cluster state. The two key novelties are (i) the introduction of a lattice defect in the underlying cluster state and (ii) the use of the Rudolph-Grover rebit encoding. Concretely, (i) allows for a topological implementation of the Hadamard gate, while (ii) does the same for the phase gate. Furthermore, we develop general ideas towards circuit compaction and algorithmic circuit verification, which we implement for the Reed-Muller code used for magic state distillation. Our performance analysis highlights the overall improvements provided by the new methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2501.03194v2
- Title: Estimating shots and variance on noisy quantum circuits
- Authors: Manav Seksaria, Anil Prabhakar
- Categories: quant-ph (primary); quant-ph; stat.AP
- Links: abs=https://arxiv.org/abs/2501.03194v2  pdf=https://arxiv.org/pdf/2501.03194v2.pdf

Abstract:
We present a method for estimating the number of shots required to achieve a desired variance in the results of a quantum circuit. First, we establish a baseline for single-qubit characterisation of individual noise sources. We then move on to multi-qubit circuits, focusing on expectation-value circuits. We decompose the variance of the estimator into a sum of a statistical term and a bias floor. These are independently estimated with one additional run of the circuit. We test our method on a Variational Quantum Eigensolver for $H_2$ and show that we can predict the variance to within known error bounds. We go on to show that for IBM Pittsburgh's noise characteristics, at that instant, 7000 shots for the given circuit would have achieved a $σ^2 \approx 0.01$

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2501.06484v2
- Title: Resilience of Quantum Teleportation Fidelity for Bipartite Mixed States near Schwarzschild and Dilaton Black Holes
- Authors: Abhijit Mandal, Sovik Roy
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2501.06484v2  pdf=https://arxiv.org/pdf/2501.06484v2.pdf

Abstract:
We investigate the robustness of quantum teleportation in the presence of strong gravitational fields by analysing bipartite mixed states derived from tripartite GHZ and W-class states near black hole event horizons. Considering a scenario where two observers approach the horizon of either a Schwarzschild or a Garfinkle Horowitz Strominger (GHS) Dilaton black hole while a third remains in flat space, we quantify the teleportation fidelity of the resulting bipartite channels after tracing out one party. Through the quantization of Dirac fields and Bogoliubov transformations, we compute the teleportation fidelity under the influence of Hawking radiation and spacetime curvature. Our results show that while entanglement degrades, teleportation fidelity remains above the classical threshold of $f>\frac{2}{3}$ for channels derived from W-class states, but not for GHZ-derived states. This indicates that quantum teleportation can remain feasible near black holes provided the initial entangled state retains useful bipartite entanglement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2501.11489v2
- Title: Independent stabilizer Rényi entropy and entanglement fluctuations in random unitary circuits
- Authors: Dominik Szombathy, Angelo Valli, Cătălin Paşcu Moca, Lóránt Farkas, Gergely Zaránd
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2501.11489v2  pdf=https://arxiv.org/pdf/2501.11489v2.pdf

Abstract:
We investigate numerically the joint distribution of magic ($M$) and entanglement ($S$) in $N$-qubit Haar-random quantum states. The distribution $P_N(M,S)$ as well as the marginals become exponentially localized, and centered around the values $\tilde{M_2} \to N-2$ and $\tilde{S} \to N/2$ as $N\to\infty$. Magic and entanglement fluctuations are, however, found to become exponentially uncorrelated. Although exponentially many states with magic $M_2=0$ and entropy $S\approx S_\text{Haar}$ exist, they represent an exponentially small fraction compared to typical quantum states, which are characterized by large magic and entanglement entropy, and uncorrelated magic and entanglement fluctuations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2503.08242v2
- Title: Geometric quantum drives and topological dynamical responses: hyperbolically-driven quantum systems and beyond
- Authors: Jihong Wu, Chuan Liu, Daniel Bulmash, Wen Wei Ho
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2503.08242v2  pdf=https://arxiv.org/pdf/2503.08242v2.pdf

Abstract:
We introduce a geometrical framework to construct a large class of time-dependent quantum systems, in which the position of a classical particle moving autonomously on a smooth connected manifold is used to steer a quantum Hamiltonian over time. This results in quantum drives with structured temporal profiles and properties dependent on the local and global nature of the underlying choice of manifold. We show that our construction recovers the well-known classes of periodically-driven and quasiperiodically-driven quantum systems, but also unveils fundamentally new classes of quantum dynamics: by utilizing a compact 2d hyperbolic Bolza surface and a nonorientable Klein-bottle surface, we demonstrate examples of a hyperbolically-driven quantum system and a nonorientably-driven quantum system respectively. Furthermore, we demonstrate that these driven systems exhibit unusual quantized dynamical responses reflecting their different underlying topologies, under the condition of being fully gapped and in the adiabatic limit, and which have interpretations as quantized crystalline electromagnetic responses in certain exotic effective tight-binding lattice models. We envision geometric quantum driving as a general framework to chart the landscape of time-dependent quantum systems and investigate the universal phase structures they exhibit, as well as a useful tool to enhance the capabilities of modern day quantum simulators.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2504.05353v2
- Title: Timelike Quantum Energy Teleportation
- Authors: Kazuki Ikeda
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2504.05353v2  pdf=https://arxiv.org/pdf/2504.05353v2.pdf

Abstract:
We establish a novel quantum protocol called Timelike Quantum Energy Teleportation (TQET) between two separated parties $A$ and $B$, designed for transporting quantum energy across spacetime. The amount of energy gained through TQET is always greater than or equal to that obtained via natural time evolution for any spin chain where $A$ and $B$ are distinguishable. This protocol uses temporal and spatial quantum correlations between agents separated by space and time. The energy supplier injects energy into the system by measuring the ground state of a many-body system that evolves over time, while the distant recipient performs a conditional operation using feedback from the supplier. When Bob acts immediately after receiving Alice's outcome, the protocol reduces to conventional QET. We present a proof-of-concept demonstration in the Ising model using quantum simulations. TQET increases energy efficiency from approximately 3\% to around 40\%, representing over a 13-fold improvement compared to QET. Furthermore, we analyzed the relationship between entanglement in time and TQET, validating the role of temporal correlations in energy activation between agents across spacetime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2504.10186v5
- Title: On the Efficient Extraction of Entangled Resources
- Authors: Si-Yi Chen, Angela Sara Cacciapuoti, Marcello Caleffi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.10186v5  pdf=https://arxiv.org/pdf/2504.10186v5.pdf

Abstract:
In the Quantum Internet, multipartite entanglement enables a rich and dynamic overlay topology, referred to as artificial topology, upon the physical one, that can be exploited for communication purposes. In fact, the ability to extract $n$-qubits GHZ states and EPR pairs from the original multipartite entangled state constitutes the resource primitives for end-to-end and on-demand quantum communications. Thus, in this paper, we theoretically determine upper and lower bounds for the number of extractable $n$-qubits GHZ states and EPR pairs involving nodes remote in the artificial topology, as well as the achievable size $n$ of remote GHZ states. The theoretical analysis is then complemented by the proposal of a novel algorithm, which provides in polynomial-time a heuristic solution to the above problem. This is remarkable, since the theoretical problem is NP-complete. The performance analysis demonstrates the proposed algorithm is able to effectively manipulate the original and arbitrary graph state for extracting entanglement resources across remote nodes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2505.08276v2
- Title: Quantum Time Crystal Clock and its Performance
- Authors: Ludmila Viotti, Marcus Huber, Rosario Fazio, Gonzalo Manzano
- Categories: quant-ph (primary); quant-ph; cond-mat.other; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2505.08276v2  pdf=https://arxiv.org/pdf/2505.08276v2.pdf

Abstract:
Understanding different aspects of time is at the core of many areas in theoretical physics. Minimal models of continuous stochastic and quantum clocks have been proposed to explore fundamental limitations on the performance of timekeeping devices. Owing to the level of complexity in the clock structure and its energy consumption, such devices show trade-offs whose characterization remains an open challenge. Indeed, even conceptual designs for thermodynamically efficient quantum clocks are not yet well understood. In condensed matter theory, time-crystals were found as an exciting new phase of matter, featuring oscillations in (pseudo)-equilibrium with first experimental observations appearing recently. This naturally prompts the question: can time crystals be used as quantum clocks and what is their performance from a thermodynamic perspective? We answer this question and find that quantum time crystals are indeed genuine quantum clocks with a performance enhanced by the spontaneous breaking of time-translation symmetry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2506.06700v5
- Title: Quantum accessible information and classical entropy inequalities
- Authors: A. S. Holevo, A. V. Utkin
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2506.06700v5  pdf=https://arxiv.org/pdf/2506.06700v5.pdf

Abstract:
Computing accessible information for an ensemble of quantum states is a basic problem in quantum information theory. We show that the recently obtained optimality criterion (A.S. Holevo, Lobachevskii J. Math., \textbf{43}:7 (2022), 1646-1650), when applied to specific ensembles of states leads to nontrivial tight entropy inequalities that are discrete relatives of the famous log-Sobolev inequality. In this light, the hypothesis of globally information-optimal measurement for an ensemble of equiangular equiprobable states (quantum pyramids) (B.-G. Englert and J. Řeháček, J. Mod. Optics \textbf{57 }N3 (2010) 218-226) is reconsidered and the corresponding entropy inequalities are proposed. Via the optimality criterion, this suggests also an approach to the proof of the conjectures concerning globally information-optimal observables for quantum pyramids.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2506.23968v2
- Title: Finite Gaussian assistance protocols and a conic metric for extremizing spacelike vacuum entanglement
- Authors: Boyu Gao, Natalie Klco
- Categories: quant-ph (primary); quant-ph; hep-lat; nucl-th
- Links: abs=https://arxiv.org/abs/2506.23968v2  pdf=https://arxiv.org/pdf/2506.23968v2.pdf

Abstract:
In a pure Gaussian tripartition, a range of entanglement between two parties ($AB$) can be purified through classical communication of Gaussian measurements performed within the third ($C$). To begin, this work introduces a direct method to calculate a hierarchic series of projective $C$ measurements for the removal of any $AB$ Gaussian noise, circumventing divergences in prior protocols. Next, a multimode conic framework is developed for pursuing the maximum (Gaussian entanglement of assistance, GEOA) or minimum (Gaussian entanglement of formation, GEOF) pure entanglement that may be revealed or required between $AB$. Within this framework, a geometric necessary and sufficient entanglement condition emerges as a doubly-enclosed conic volume, defining a novel distance metric for conic optimization. Extremizing this distance for spacelike vacuum entanglement in the massless and massive free scalar fields yields (1) the highest known lower bound to GEOA, the first that decays slower than the two-point correlation functions and (2) the lowest known upper bound to GEOF, the first that decays exponentially mirroring the mixed $AB$ negativity. Furthermore, combination of the above with a generalization of previous partially-transposed noise filtering techniques allows calculation of a single $C$ measurement that maximizes the purified $AB$ entanglement. Beyond expectation that these behaviors of spacelike GEOA and GEOF persist in interacting theories, the present measurement and optimization techniques are applicable to physical many-body Gaussian states beyond quantum fields.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2507.13735v2
- Title: Impact of quadrature measurement on quantum coherence
- Authors: Lucía Álvarez, Alfredo Luis
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.13735v2  pdf=https://arxiv.org/pdf/2507.13735v2.pdf

Abstract:
We examine the behavior of quadrature coherence under the measurement of the same field quadrature. This is carried out with the help of a beam splitter, which implies the contribution of an auxiliary field state impinging at the other input port. To this end we consider the linear input-output transformation of a lossless beam splitter to relate input and output coherences, measured in terms of the $l_1$-norm. After obtaining a general input-output relation between coherences we apply the result to Gaussian and number states. For Gaussian states we obtain that coherence does not depend on the measurement outcome, and that the average coherence always equals the coherence of the reduced state, showing no average effect on coherence of the measurement. On the other hand, for number states the output coherence depends on the measurement, decreasing the relative coherence with increasing photon number. Finally, we consider relative-entropy as a measure of coherence to show that for number states and coherence measures other than the $l_1$-norm the average coherence no longer equals the coherence of the output reduced state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2508.01066v2
- Title: Cryogenic rf-to-microwave transducer based on a dc-Biased electromechanical system
- Authors: Himanshu Patange, Kyrylo Gerashchenko, Rémi Rousseau, Paul Manset, Léo Balembois, Thibault Capelle, Samuel Deléglise, Thibaut Jacqmin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.01066v2  pdf=https://arxiv.org/pdf/2508.01066v2.pdf

Abstract:
We report a two-stage, heterodyne rf-to-microwave transducer that combines a tunable electrostatic pre-amplifier with a superconducting electromechanical cavity. A metalized Si$_3$N$_4$ membrane (3 MHz frequency) forms the movable plate of a vacuum-gap capacitor in a microwave LC resonator. A dc bias across the gap converts any small rf signal into a resonant electrostatic force proportional to the bias, providing a voltage-controlled gain that multiplies the cavity's intrinsic electromechanical gain. In a flip-chip device with a 1.5 $\mathrmμ$m gap operated at 10 mK we observe dc-tunable anti-spring shifts, and rf-to-microwave transduction at 49 V bias, achieving a charge sensitivity of 87 $\mathrmμ$e/$\sqrt{\mathrm{Hz}}$ (0.9 nV/$\sqrt{\mathrm{Hz}}$). Extrapolation to sub-micron gaps and state-of-the-art $Q>10^8$ membrane resonators predicts sub-200 fV/$\sqrt{\mathrm{Hz}}$ sensitivity, establishing dc-biased electromechanics as a practical route towards quantum-grade rf electrometers and low-noise modular heterodyne links for superconducting microwave circuits and charge or voltage sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2508.08191v2
- Title: Single-Shot Decoding and Fault-tolerant Gates with Trivariate Tricycle Codes
- Authors: Abraham Jacob, Campbell McLauchlan, Dan E. Browne
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.08191v2  pdf=https://arxiv.org/pdf/2508.08191v2.pdf

Abstract:
While quantum low-density parity check (qLDPC) codes are a low-overhead means of quantum information storage, it is valuable for quantum codes to possess fault-tolerant features beyond this resource efficiency. In this work, we introduce trivariate tricycle (TT) codes, qLDPC codes that combine several desirable features: high thresholds under a circuit-level noise model, partial single-shot decodability for low-time-overhead decoding, a large set of transversal Clifford gates and automorphisms within and between code blocks, and (for several sub-constructions) constant-depth implementations of a (non-Clifford) $CCZ$ gate. TT codes are CSS codes based on a length-3 chain complex, and are defined from three trivariate polynomials, with the 3D toric code (3DTC) belonging to this construction. We numerically search for TT codes and find several candidates with improved parameters relative to the 3DTC, using up to 48$\times$ fewer data qubits as equivalent 3DTC encodings. We construct syndrome-extraction circuits for these codes and numerically demonstrate single-shot decoding in the X error channel in both phenomenological and circuit-level noise models. Under circuit-level noise, TT codes have a threshold of $0.3\%$ in the Z error channel and $1\%$ in the X error channel (with single-shot decoding). All TT codes possess several transversal $CZ$ gates that can partially address logical qubits between two code blocks. Additionally, the codes possess a large set of automorphisms that can perform Clifford gates within a code block. Finally, we establish several TT code polynomial constructions that allows for a constant-depth implementation of logical $CCZ$ gates. We find examples of error-correcting and error-detecting codes using these constructions whose parameters out-perform those of the 3DTC, using up to $4\times$ fewer data qubits for equivalent-distance 3DTC encodings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2508.20992v2
- Title: How many qubits does a machine learning problem require?
- Authors: Sydney Leither, Michael Kubal, Sonika Johri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.20992v2  pdf=https://arxiv.org/pdf/2508.20992v2.pdf

Abstract:
For a machine learning paradigm to be generally applicable, it should have the property of universal approximation, that is, it should be able to approximate any target function to any desired degree of accuracy. In variational quantum machine learning, the class of functions that can be learned depend on both the data encoding scheme as well as the architecture of the optimizable part of the model. Here, we show that the property of universal approximation is constructively and efficiently realized by the recently proposed bit-bit data encoding scheme. Further, we show that this construction allows us to calculate the number of qubits required to solve a learning problem on a dataset to a target accuracy, giving rise to the first resource estimation framework for variational quantum machine learning. We apply bit-bit encoding to a number of medium-sized classical benchmark datasets and find that they require only 27 qubits on average for encoding. We extend the basic bit-bit encoding scheme to a variant that efficiently supports batched processing of large datasets. As a demonstration, we apply this new scheme to subsets of a giga-scale transcriptomic dataset. This work establishes bit-bit encoding not only as a universally expressive quantum data representation, but also as a practical foundation for resource estimation and benchmarking in quantum machine learning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2509.14314v2
- Title: Anyonic membranes and Pontryagin statistics
- Authors: Yitao Feng, Hanyu Xue, Yuyang Li, Meng Cheng, Ryohei Kobayashi, Po-Shen Hsin, Yu-An Chen
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; hep-th; math-ph; math.QA
- Links: abs=https://arxiv.org/abs/2509.14314v2  pdf=https://arxiv.org/pdf/2509.14314v2.pdf

Abstract:
Anyons, unique to two spatial dimensions, underlie extraordinary phenomena such as the fractional quantum Hall effect, but their generalization to higher dimensions has remained elusive. The topology of Eilenberg-MacLane spaces constrains the loop statistics to be only bosonic or fermionic in any dimension. In this work, we introduce the novel anyonic statistics for membrane excitations in four dimensions. Analogous to the $\mathbb{Z}_N$-particle exhibiting $\mathbb{Z}_{N\times \gcd(2,N)}$ anyonic statistics in two dimensions, we show that the $\mathbb{Z}_N$-membrane possesses $\mathbb{Z}_{N\times \gcd(3,N)}$ anyonic statistics in four dimensions. Given unitary volume operators that create membrane excitations on the boundary, we propose an explicit 56-step unitary sequence that detects the membrane statistics. We further analyze the boundary theory of $(5{+}1)$D 1-form $\mathbb{Z}_N$ symmetry-protected topological phases and demonstrate that their domain walls realize all possible anyonic membrane statistics. We then show that the $\mathbb{Z}_3$ subgroup persists in all higher dimensions. In addition to the standard fermionic $\mathbb{Z}_2$ membrane statistics arising from Stiefel-Whitney classes, membranes also exhibit $\mathbb{Z}_3$ statistics associated with Pontryagin classes. We explicitly verify that the 56-step process detects the nontrivial $\mathbb{Z}_3$ statistics in 5, 6, and 7 spatial dimensions. Moreover, in 7 and higher dimensions, the statistics of membrane excitations stabilize to $\mathbb{Z}_{2} \times \mathbb{Z}_{3}$, with the $\mathbb{Z}_3$ sector consistently captured by this process.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2510.07658v2
- Title: Photon triplets from integrated microrings: A path towards deterministic non-Gaussianity on a chip
- Authors: Samuel E. Fontaine, J. E. Sipe, Marco Liscidini, Milica Banic
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2510.07658v2  pdf=https://arxiv.org/pdf/2510.07658v2.pdf

Abstract:
We propose cascaded spontaneous four-wave mixing (SFWM) in microring resonators as a scalable and efficient approach for directly generating non-Gaussian states of light. Focusing on the well-understood "low-gain" regime, we demonstrate that triplet generation through cascaded SFWM can be achieved with high efficiency and favorable spectral characteristics using realistic microring sources in AlGaAs. The ability to achieve the generation of light in a single set of supermodes -- and the predicted accessibility of the "high-gain" regime at realistic pump powers -- makes this source a promising candidate as a direct and deterministic source of non-Gaussian light for photonic quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2510.07802v2
- Title: Near-limit quantum control beyond analytic tractability in many-body spin systems
- Authors: Jixing Zhang, Bo Peng, Yang Wang, Cheuk Kit Cheung, Guodong Bian, Hualuo Pang, Andrew M. Edmonds, Matthew Markham, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.07802v2  pdf=https://arxiv.org/pdf/2510.07802v2.pdf

Abstract:
As quantum control approaches hardware-imposed performance limits, weak effects omitted by reduced models become consequential. Assumptions required for analytic tractability then cease to guide control design and instead constrain further improvement. Here, we relax such assumptions and use simulation-guided stochastic tree search to navigate combinatorially large, discrete pulse-sequence spaces for robust many-body spin control. Experimentally, in a solid-state spin ensemble, the resulting computationally discovered pulse sequences substantially outperform analytically optimized baselines, despite being excluded by construction from analytic design criteria. Importantly, these unconventional sequences expose predictive structural features that enable rapid neural network--based performance evaluation. This efficiency gain makes the combinatorial scaling tractable and expands the control alphabet from 8 symmetry-restricted pulses to over 26,000 hardware-resolved options. The resulting fine-grained design freedom provides the control resolution required to reliably address weak, performance-limiting effects, unlocking qualitatively different spin-control capabilities beyond decades of traditional sequence design. Together, these results show that near performance limits, simplifying assumptions can become a primary constraint on quantum control in realistic hardware, and must be repurposed to guide computational discovery.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2510.15506v3
- Title: Adaptive quantum channel discrimination using methods of quantum metrology
- Authors: Stanisław Sieniawski, Rafał Demkowicz-Dobrzański
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.15506v3  pdf=https://arxiv.org/pdf/2510.15506v3.pdf

Abstract:
We present an efficient tensor-network based algorithm for finding the optimal adaptive quantum channel discrimination strategies inspired by recently developed numerical methods in quantum metrology to find the optimal adaptive channel estimation protocols. We examine the connection between channel discrimination and estimation problems, highlighting in particular an appealing structural similarity between models that admit Heisenberg scaling estimation performance, and models that admit perfect channel discrimination in finite--number of channel uses.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2510.15590v2
- Title: A single optically detectable tumbling spin in silicon
- Authors: Félix Cache, Yoann Baron, Baptiste Lefaucher, Jean-Baptiste Jager, Frédéric Mazen, Frédéric Milési, Sébastien Kerdilès, Isabelle Robert-Philip, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.15590v2  pdf=https://arxiv.org/pdf/2510.15590v2.pdf

Abstract:
We demonstrate single spin spectroscopy of a fluorescent tumbling defect in silicon called the G center, behaving as a pseudo-molecule randomly reorienting itself in the crystalline matrix. Using high-resolution spin spectroscopy, we reveal a fine magnetic structure resulting from the spin principal axes jumping between discrete orientations in the crystal. Modeling the atomic reorientation of the defect shows that spin tumbling induces variations in the coupling to the microwave magnetic field, enabling position-dependent Rabi frequencies to be detected in coherent spin control experiments. By virtue of its pseudo-molecule configuration, the G center in silicon is a unique quantum system to investigate the mutual interaction between optical, spin and rotation properties in a highly versatile material.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2510.19598v2
- Title: Zero-field identification and control of hydrogen-related electron-nuclear spin registers in diamond
- Authors: Alexander Ungar, Hao Tang, Andrew Stasiuk, Bo Xing, Boning Li, Ju Li, Alexandre Cooper, Paola Cappellaro
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.19598v2  pdf=https://arxiv.org/pdf/2510.19598v2.pdf

Abstract:
Spin defects in diamond serve as powerful building blocks for quantum technologies, especially for applications in quantum sensing and quantum networking. Electron-nuclear defects formed in the environment of optically active spins, such as the nitrogen-vacancy (NV) center, can be harnessed as qubits to construct larger hybrid quantum registers. However, many of these defects have yet to be characterized, limiting their integration into scalable devices. Here, we apply two hybrid electron-nuclear spin control schemes to self-consistently characterize unknown spin defects at the single-spin level. We perform double electron-electron resonance at zero field (ZF-DEER) to extract hyperfine components and introduce a nuclear-electron-electron triple resonance (NEETR) protocol to control and identify the nuclear spin through the stronger electronic spin interaction. These results provide a guide to resolving the defect structures using ab initio calculations, leading to the identification of a new hydrogen-related defect structure as well as an accurate match to a previously identified nitrogen-related defect. We further apply our NEETR protocol to demonstrate initialization, unitary control, and long-lived coherence of the nuclear spin qubit of the hydrogen defect with $T_2 = 1.0(3)\,\mathrm{ms}$. Our characterization and control tools establish a framework to expand the accessible defect landscape for electron-nuclear registers with hydrogen-related defects and enable applications in quantum sensing, networks, and atomic-scale magnetic resonance imaging at room temperature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2511.04967v3
- Title: Hybrid Action Reinforcement Learning for Quantum Architecture Search
- Authors: Jiayang Niu, Yan Wang, Jie Li, Ke Deng, Azadeh Alavi, Muhammad Usman, Yongli Ren
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.04967v3  pdf=https://arxiv.org/pdf/2511.04967v3.pdf

Abstract:
Reinforcement learning-based Quantum Architecture Search (QAS) offers a promising avenue for automating the design of variational quantum circuits, but existing methods typically decouple discrete structure search from continuous parameter optimization, resulting in inefficient or brittle solutions. We propose HyRLQAS (Hybrid-Action Reinforcement Learning for Quantum Architecture Search), a unified reinforcement learning framework that jointly learns gate placement and parameter initialization within a hybrid discrete-continuous action space, while enabling dynamic refinement of previously placed gates. Trained in a variational quantum eigensolver setting, the agent constructs circuits that directly optimize molecular ground-state energies. Across multiple molecular benchmarks, HyRLQAS demonstrates strong and competitive performance against state-of-the-art QAS methods, achieving lower energy errors with fewer gates. Notably, HyRLQAS reaches chemical-accuracy-level convergence down to 1e-8 energy error after classical optimization, and policy-guided initialization reduces the iteration count of downstream classical optimizers. These results demonstrate that hybrid-action reinforcement learning provides a principled and effective mechanism for coupling circuit topology design with optimization-aware parameterization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2512.01502v2
- Title: Formal Verification of Noisy Quantum Reinforcement Learning Policies
- Authors: Dennis Gross
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.FL
- Links: abs=https://arxiv.org/abs/2512.01502v2  pdf=https://arxiv.org/pdf/2512.01502v2.pdf

Abstract:
Quantum reinforcement learning (QRL) aims to use quantum effects to create sequential decision-making policies that achieve tasks more effectively than their classical counterparts. However, QRL policies face uncertainty from quantum measurements and hardware noise, such as bit-flip, phase-flip, and depolarizing errors, which can lead to unsafe behavior. Existing work offers no systematic way to verify whether trained QRL policies meet safety requirements under specific noise conditions. We introduce QVerifier, a formal verification method that applies probabilistic model checking to analyze trained QRL policies with and without modeled quantum noise. QVerifier builds a complete model of the policy-environment interaction, incorporates quantum uncertainty directly into the transition probabilities, and then checks safety properties using the Storm model checker. Experiments across multiple QRL environments show that QVerifier precisely measures how different noise models influence safety, revealing both performance degradation and cases where noise can help. By enabling rigorous safety verification before deployment, QVerifier addresses a critical need: because access to quantum hardware is expensive, pre-deployment verification is essential for any safety-critical use of QRL. QVerifier targets a potential sweet spot between classical and quantum computation, where trained QRL policies could still be modeled classically for probabilistic model checking. When the policy was trained under matching noise conditions, this formal model is exact; when trained on physical hardware, it constitutes an idealized approximation, as unknown hardware noise prevents exact policy modeling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2601.02064v2
- Title: Cutting Quantum Circuits Beyond Qubits
- Authors: Manav Seksaria, Anil Prabhakar
- Categories: quant-ph (primary); quant-ph; cs.DC
- Links: abs=https://arxiv.org/abs/2601.02064v2  pdf=https://arxiv.org/pdf/2601.02064v2.pdf

Abstract:
We extend quantum circuit cutting to heterogeneous registers comprising mixed-dimensional qudits. By decomposing non-local interactions into tensor products of local generalised Gell-Mann matrices, we enable the simulation and execution of high-dimensional circuits on disconnected hardware fragments. We validate this framework on qubit--qutrit ($2$--$3$) interfaces, achieving exact state reconstruction with a Total Variation Distance of 0 within single-precision floating-point tolerance. Furthermore, we demonstrate the memory advantage in an 8-particle, dimension-8 system, reducing memory usage from 128 MB to 64 KB per circuit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2408.03924v3
- Title: A universal black-box quantum Monte Carlo approach to quantum phase transitions
- Authors: Nic Ezzell, Lev Barash, Itay Hen
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2408.03924v3  pdf=https://arxiv.org/pdf/2408.03924v3.pdf

Abstract:
We derive exact, universal, closed-form quantum Monte Carlo estimators for finite-temperature energy susceptibility and fidelity susceptibility, applicable to essentially arbitrary Hamiltonians. Combined with recent advancements in Monte Carlo, our approach enables a black-box framework for studying quantum phase transitions--without requiring prior knowledge of an order parameter or the manual design of model-specific ergodic quantum Monte Carlo update rules. We demonstrate the utility of our method by applying a single implementation to the transverse-field Ising model, the XXZ model, and an ensemble of models related by random unitaries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2504.02824v2
- Title: Observation of dislocation bound states and skin effects in non-Hermitian Chern insulators
- Authors: Jia-Xin Zhong, Bitan Roy, Yun Jing
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; physics.class-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2504.02824v2  pdf=https://arxiv.org/pdf/2504.02824v2.pdf

Abstract:
The confluence of non-Hermitian (NH) topology and crystal defects has culminated significant interest, yet its experimental exploration has been limited due to the challenges involved in design and measurements. Here, we showcase experimental observation of NH dislocation bound states (NHDS) and the dislocation-induced NH skin effect in two-dimensional acoustic NH Chern lattices. By embedding an edge dislocations-antidislocation pair in such acoustic lattices and implementing precision-controlled hopping and onsite gain/loss via active meta-atoms, we reveal robust defect-bound states localized at dislocation cores within the line gap of the complex energy spectrum. We experimentally identify the emergence of bulk exceptional points (EPs) via spectral coalescence and phase rigidity analysis. We demonstrate that the NHDS survive against moderate NH perturbations but gradually delocalize and merge with the bulk (skin) states driven by these EPs under periodic (open) boundary conditions. Furthermore, our experiments demonstrate that the dislocation core can feature weak NH skin effects when its direction is perpendicular to the Burgers vector in periodic systems. Our findings, therefore, pave an experimental pathway for probing NH topology via lattice defects and open new avenues for defect-engineered topological devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2504.05375v2
- Title: Neutrino Oscillations as a Probe of Macrorealism
- Authors: Kathrine Mørch Groth, Johann Ioannou-Nikolaides, D. Jason Koskinen, Markus Ahlers
- Categories: hep-ph (primary); hep-ph; astro-ph.HE; quant-ph
- Links: abs=https://arxiv.org/abs/2504.05375v2  pdf=https://arxiv.org/pdf/2504.05375v2.pdf

Abstract:
The correlations between successive measurements of a quantum system can violate a family of Leggett-Garg Inequalities (LGIs) that are analogous to the violation of Bell's inequalities of measurements performed on spatially separated quantum systems. These LGIs follow from a macrorealistic point of view, imposing that a classical system is at all times in a definite state and that a measurement can, at least in principle, leave this state undisturbed. Violations of LGIs can be probed by neutrino flavour oscillations if the correlators of consecutive flavour measurements are approximately stationary. We discuss here several improvements of the methodology used in previous analyses based on accelerator and reactor neutrino data. We argue that the strong claims of LGI violations made in previous studies are based on an unsuitable modelling of macrorealistic systems in statistical hypothesis tests. We illustrate our improved methodology via the example of the MINOS muon-neutrino survival data, where we find revised statistical evidence for violations of LGIs at the $(2-3)σ$ level, depending on macrorealistic background models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2504.07295v2
- Title: Advanced measurement techniques in quantum Monte Carlo: The permutation matrix representation approach
- Authors: Nic Ezzell, Itay Hen
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2504.07295v2  pdf=https://arxiv.org/pdf/2504.07295v2.pdf

Abstract:
In a typical finite temperature quantum Monte Carlo (QMC) simulation, estimators for simple static observables such as specific heat and magnetization are known. With a great deal of system-specific manual labor, one can sometimes also derive more complicated non-local or even dynamic observable estimators. Within the permutation matrix representation (PMR) flavor of QMC, however, we show that one can derive formal estimators for arbitrary static observables. We also derive exact, explicit estimators for general imaginary-time correlation functions and non-trivial integrated susceptibilities thereof. We demonstrate the practical versatility of our method by estimating various non-local, random observables for the transverse-field Ising model on a square lattice.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2504.18129v2
- Title: Entanglement Harvesting from Quantum Field: Insights via the Partner Formula
- Authors: Yuki Osawa, Yasusada Nambu, Riku Yoshimoto
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2504.18129v2  pdf=https://arxiv.org/pdf/2504.18129v2.pdf

Abstract:
We examine the condition necessary for extracting entanglement from a quantum field through the use of two local modes A and B (detector modes). We show that Simon's entanglement criterion for the bipartite Gaussian state can be reformulated in terms of commutators between the canonical operators of the detector mode B and the partner mode P of the detector mode A. Using the profile representation of detector modes, we identify that harvesting is prohibited under certain specific conditions. According to analyses based on moving mirror models, Hawking radiation originates from the Milne modes at past null infinity, that reflect off at the mirror and ultimately transform into real particle modes. Drawing parallels between the Unruh effect and Hawking radiation, our findings indicate an absence of quantum correlations between ``real particles" emitted as Hawking radiation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2505.11766v3
- Title: Redefining Neural Operators in $d+1$ Dimensions for Embedding Evolution
- Authors: Haoze Song, Zhihao Li, Xiaobo Zhang, Zecheng Gan, Zhilu Lai, Wei Wang
- Categories: cs.LG (primary); cs.LG; cs.AI; quant-ph
- Links: abs=https://arxiv.org/abs/2505.11766v3  pdf=https://arxiv.org/pdf/2505.11766v3.pdf

Abstract:
Neural Operators (NOs) have emerged as powerful tools for learning mappings between function spaces. Among them, the kernel integral operator has been widely used in universally approximating architectures. Following the original formulation, most advancements focus on designing better parameterizations for the kernel over the original physical domain (with $d$ spatial dimensions, $d\in{1,2,3,\ldots}$). In contrast, embedding evolution remains largely unexplored, which often drives models toward brute-force embedding lengthening to improve approximation, but at the cost of substantially increased computation.   In this paper, we introduce an auxiliary dimension that explicitly models embedding evolution in operator form, thereby redefining the NO framework in $d+1$ dimensions (the original $d$ dimensions plus one auxiliary dimension). Under this formulation, we develop a Schrödingerised Kernel Neural Operator (SKNO), which leverages Fourier-based operators to model the $d+1$ dimensional evolution. Across more than ten increasingly challenging benchmarks, ranging from the 1D heat equation to the highly nonlinear 3D Rayleigh-Taylor instability, SKNO consistently outperforms other baselines. We further validate its resolution invariance under mixed-resolution training and super-resolution inference, and evaluate zero-shot generalization to unseen temporal regimes. In addition, we present a broader set of design choices for the lifting and recovery operators, demonstrating their impact on SKNO's predictive performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2505.21508v3
- Title: Visualization enhances Problem Solving in multi-Qubit Systems
- Authors: Jonas Bley, Eva Rexigel, Alda Arias, Lars Krupp, Nikolas Longen, Paul Lukowicz, Stefan Küchemann, Jochen Kuhn, et al.
- Categories: physics.ed-ph (primary); physics.ed-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2505.21508v3  pdf=https://arxiv.org/pdf/2505.21508v3.pdf

Abstract:
Quantum Information Science (QIS) is a vast, diverse, and abstract field. In consequence, learners face many challenges. Science, Technology, Engineering, and Mathematics (STEM) education research has found that visualizations are valuable to aid learners in complex matters. The conditions under which visualizations pose benefits are largely unexplored in QIS education. In this eye-tracking study, we examine the conditions under which the visualization of multi-qubit systems with the Dimensional Circle Notation (DCN) in addition to the mathematical symbolic Dirac Notation (DN) is associated with a benefit for solving problems on the ubiquitously used Hadamard gate operation in terms of performance, Extraneous Cognitive Load (ECL) and Intrinsic Cognitive Load (ICL). We find that DCN increases performance and reduces cognitive load for participants with little experience in quantum physics. In addition, representational competence is able to predict reductions in ECL with DCN, but not performance or ICL. Analysis of the eye-tracking results indicates that task solvers with more transitions between DN and DCN benefit less from the visualization. We discuss the generalizability of the results and practical implications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2511.00905v2
- Title: Symmetry-resolved genuine multi-entropy: Haar random and graph states
- Authors: Norihiro Iizuka, Simon Lin
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2511.00905v2  pdf=https://arxiv.org/pdf/2511.00905v2.pdf

Abstract:
We study the symmetry-resolved genuine multi-entropy, a measure that captures genuine multi-partite entanglement, in Haar random states and random graph states in the presence of a conserved quantity. For Haar random states, we derive explicit formulae for the genuine multi-entropy under a global $U(1)$ symmetry in the thermodynamic limit, and find that its dependence on subsystem sizes closely resembles that of fully Haar random states without a conserved charge. We also perform numerical analyses, focusing on spin systems for both Haar random and graph states. For random graph states, our numerical analyses reveal distinctive features of their multi-partite entanglement structure and we contrast them with the Haar random case.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2511.01918v2
- Title: Superpositional Gradient Descent: Harnessing Quantum Principles for Model Training
- Authors: Ahmet Erdem Pamuk, Emir Kaan Özdemir, Şuayp Talha Kocabay
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2511.01918v2  pdf=https://arxiv.org/pdf/2511.01918v2.pdf

Abstract:
Large language models (LLMs) are increasingly trained with classical optimization techniques like AdamW to improve convergence and generalization. However, the mechanisms by which quantum-inspired methods enhance classical training remain underexplored. We introduce Superpositional Gradient Descent (SGD), a novel optimizer linking gradient updates with quantum superposition by injecting quantum circuit perturbations. We present a mathematical framework and implement hybrid quantum-classical circuits in PyTorch and Qiskit. On synthetic sequence classification and large-scale LLM fine-tuning, SGD converges faster and yields lower final loss than AdamW. Despite promising results, scalability and hardware constraints limit adoption. Overall, this work provides new insights into the intersection of quantum computing and deep learning, suggesting practical pathways for leveraging quantum principles to control and enhance model behavior.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2512.17333v2
- Title: Quantum quenches across continuous and first-order quantum transitions in one-dimensional quantum Ising models
- Authors: Andrea Pelissetto, Davide Rossini, Ettore Vicari
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2512.17333v2  pdf=https://arxiv.org/pdf/2512.17333v2.pdf

Abstract:
We investigate the quantum dynamics generated by quantum quenches (QQs) of the Hamiltonian parameters in many-body systems, focusing on protocols that cross first-order and continuous quantum transitions, both in finite-size systems and in the thermodynamic limit. As a paradigmatic example, we consider the quantum Ising chain in the presence of homogeneous transverse ($g$) and longitudinal ($h$) magnetic fields. This model exhibits a continuous quantum transition (CQT) at $g=g_c$ and $h=0$, and first-order quantum transitions (FOQTs) driven by $h$ along the line $h=0$ ($g<g_c$). In the integrable limit $h=0$, the system can be mapped onto a quadratic fermionic theory; however, any nonvanishing longitudinal field breaks integrability and the spectrum of the resulting Hamiltonian is generally expected to enter a chaotic regime. We analyze QQs in which the longitudinal field is suddenly changed from a negative value $h_i < 0$ to a positive value $h_f>0$. We focus on values of $h_f$ such that the spectrum of the post-QQ Hamiltonian $H(g,h_f)$ lies in the chaotic regime, where thermalization may emerge at asymptotically long times. We study the out-of-equilibrium dynamics for different values of $g$, finding qualitatively distinct behaviors for $g > g_c$ (where the chain is in the disordered phase), for $g = g_c$ (QQ across the CQT), and for $g<g_c$ (QQ across the FOQT line).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-01-31 09:49
- arXiv: 2512.20519v2
- Title: Run-and-Tumble Dynamics and Zeno--Anti-Zeno Transition in Biased Quantum Trajectories
- Authors: Aritra Kundu
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2512.20519v2  pdf=https://arxiv.org/pdf/2512.20519v2.pdf

Abstract:
We identify the transition from the oscillatory Rabi regime to the localized Zeno/Anti-Zeno regime in continuous measurement and feedback of a qubit as a quantum analogue of Motility-Induced Phase Separation (MIPS). A mapping between a biased monitored qubit and a classical ``Run-and-Tumble" active particle is studied. We demonstrate that the competition between coherent Rabi driving (analogous to active motility) and measurement-induced feedback bias (analogous to persistence) mimics the behavior of biological swimmers. This framework provides a picture of measurement-induced phase transitions using the language of active matter and offering a novel pathway for designing dissipative noisy quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

