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

