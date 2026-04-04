- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25757v1
- Title: Decoder Dependence in Surface-Code Threshold Estimation with Native Gottesman-Kitaev-Preskill Digitization and Parallelized Sampling
- Authors: Dennis Delali Kwesi Wayo, Chinonso Onah, Vladimir Milchakov, Leonardo Goliatt, Sven Groppe
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2603.25757v1  pdf=https://arxiv.org/pdf/2603.25757v1.pdf

Abstract:
We quantify decoder dependence in surface-code threshold studies under two matched regimes: Pauli noise and native GKP-style Gaussian displacement digitization. Using LiDMaS+ v1.1.0, we benchmark MWPM, Union-Find (UF), Belief Propagation (BP), and neural-guided MWPM with fixed seeds, identical sweep grids, and unified reporting across runs 06--14. At $d=5$ and $σ=0.20$, MWPM and UF define the Pareto frontier, with (runtime, LER) = (1.341 s, 0.2273) and (1.332 s, 0.2303); neural-guided MWPM is slower and less accurate (1.396 s, 0.3730), and BP is dominated (7.640 s, 0.6107). Crossing-bootstrap diagnostics are stable only for MWPM, with median $σ^\star_{3,5}=0.10$ (1911/2000 valid) and $σ^\star_{5,7}=0.1375$ (1941/2000 valid), while other decoders show no valid crossing samples. Dense-window scanning over $σ\in [0.08,0.24]$ returns NaN crossings for all decoders, confirming estimator- and window-sensitive threshold localization. Rank-stability and effect-size bootstrap analyses reinforce ordering robustness: BP remains rank 4, neural-guided MWPM rank 3, and MWPM-UF differences are small ($Δ_{\mathrm{MWPM-UF}}=-0.00383$, 95\% interval $[-0.0104,0.00329]$) across $σ\in [0.05,0.35]$. Threaded execution preserves statistical fidelity while improving throughput: $1.34\times$ speedup in Pauli mode and $1.94\times$ in native GKP mode, with mean $|Δ\mathrm{LER}|$ $6.07\times10^{-3}$ and $5.20\times10^{-3}$, respectively. We therefore recommend estimator-conditional threshold reporting coupled to runtime-fidelity checks for reproducible hardware-facing practical future decoder benchmarking workflows.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25774v1
- Title: Catalytic Coherence Amplification for Quantum State Recovery: Theory, Numerical Validation, and Comparison with Conventional Error Correction
- Authors: Hikaru Wakaura
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.25774v1  pdf=https://arxiv.org/pdf/2603.25774v1.pdf

Abstract:
We present Catalytic Quantum Error Correction (CQEC), a quantum state recovery protocol based on the arbitrary amplification of coherence in catalytic covariant transformations. Unlike conventional quantum error correction, CQEC requires knowledge of the target state and multiple noisy copies, but operates without an error threshold: recovery succeeds whenever the coherent modes of the target state are contained within those of the noisy state (mode inclusion), regardless of the noise magnitude. A reusable catalyst state mediates the transformation and its reduced state is preserved exactly after each cycle (correlated catalysis). We validate CQEC numerically across four quantum algorithms -- qDRIFT, quantum Kolmogorov--Arnold networks, control-free phase estimation, and Regev factoring -- and a tree tensor network cryptographic protocol, under dephasing, depolarizing, and combined noise. In the asymptotic (infinite-copy) limit, CQEC recovers the known algorithmic output state from fidelity $F = 0.07$ to $F > 0.999$ across 200 configurations; at finite copy number $n$, the fidelity gap scales as $1 - F \leq O(1/\sqrt{n})$. We compare with Steane and surface codes under their respectively different operational assumptions. Our results establish coherence resource theory as a complementary foundation for quantum state recovery.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25789v1
- Title: Typical entanglement in anyon chains: Page curves beyond Lie group symmetries
- Authors: Yale Yauk, Lucas Hackl, Alexander Hahn
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; hep-th
- Links: abs=https://arxiv.org/abs/2603.25789v1  pdf=https://arxiv.org/pdf/2603.25789v1.pdf

Abstract:
We study bipartite entanglement statistics in one-dimensional anyon chains, whose Hilbert spaces are constrained by fusion rules of unitary pre-modular categories. Our setup generalizes previous frameworks on symmetry-resolved entanglement entropy for non-abelian Lie group symmetries to the setting of quantum groups. We derive analytical expressions for the average anyonic entanglement entropy and its variance. Surprisingly, despite the constrained Hilbert space structure, the large $L$ expansion has no universal $O(\sqrt{L})$ or $O(1)$ symmetry-type corrections except for a subleading topological correction term that produces a Page curve asymmetry. We further show that the variance decays exponentially with system size, establishing the typicality. Numerical simulations of the integrable and quantum-chaotic golden chain Hamiltonian show that chaotic mid-spectrum eigenstates match the Haar-random predictions, supporting the use of eigenstate entanglement as a diagnostic of quantum chaos. Our results establish the anyonic Page curve as an appropriate chaotic benchmark in topological many-body systems and connect anyonic entanglement to Page-type universality in quantum many-body physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25831v1
- Title: Theory of (Co)homological Invariants on Quantum LDPC Codes
- Authors: Zimu Li, Yuguo Shao, Fuchuan Wei, Yiming Li, Zi-Wen Liu
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2603.25831v1  pdf=https://arxiv.org/pdf/2603.25831v1.pdf

Abstract:
With recent breakthroughs in the construction of good qLDPC codes and nearly good qLTCs, the study of (co)homological invariants of quantum code complexes, which fundamentally underlie their logical operations, has become evidently important. In this work, we establish a systematic framework for mathematically analyzing these invariants across a broad spectrum of constructions, from HGP codes to sheaf codes, by synthesizing advanced math tools. We generalize the notion of canonical logical representatives from HGP codes to the sheaf code setting, resolving a long-standing challenge in explicitly characterizing sheaf codewords. Building on this foundation, we present the first comprehensive computation of cup products within the intricate framework of sheaf codes. Given Artin's primitive root conjecture which holds under the generalized Riemann hypothesis, we prove that $\tildeΘ(N)$ independent cup products can be supported on almost good qLDPC codes and qLTCs of length N, opening the possibility of achieving linearly many parallel, nontrivial, constant-depth multi-controlled-Z gates. Moreover, by interpreting sheaf codes as covering spaces of HGP codes via graph lifts, we propose a scheme that inductively generates families of both HGP and sheaf codes in an interlaced fashion from a constant-size HGP code. Notably, the induction preserves all (co)homological invariants of the initial code. This provides a general framework for lifting invariants or logical gates from small codes to infinite code families, and enables efficient verification of such features by checking on small instances. Our theory provides a substantive methodology for studying invariants in HGP codes and extends it to sheaf codes. In doing so, we reveal deep and unexpected connections between qLDPC codes and math, thereby laying the groundwork for future advances in quantum coding, fault tolerance, and physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25876v1
- Title: Two-Gate Extensions of Free Axis and Free Quaternion Selection for Sequential Optimization of Parameterized Quantum Circuits
- Authors: Joona V. Pankkonen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.25876v1  pdf=https://arxiv.org/pdf/2603.25876v1.pdf

Abstract:
We propose two-gate extensions of the sequential single-qubit optimizers, Free Axis Selection (Fraxis) and Free Quaternion Selection (FQS), termed Two-Gate Fraxis (TGF) and Two-Gate FQS (TGFQS), respectively. In contrast to Fraxis and FQS, which update one single-qubit gate at a time via quadratic local cost function and matrix diagonalization, TGF and TGFQS optimize two parameterized single-qubit gates simultaneously by constructing an exact quartic local cost function and optimizing it using classical optimizers. We further investigate how different gate pairing strategies affect optimization performance. Using numerical experiments on spin Hamiltonians, molecular Hamiltonians, and quantum state preparation tasks, we find that TGF and TGFQS frequently achieve a lower final relative error to the ground state energy or infidelity than their single gate counterparts. We observe that the random and half-shifted gate pairing strategies for TGF and TGFQS perform best in many of the tested settings. In the additional finite-shot experiments on Fermi-Hubbard and transverse-field Ising model Hamiltonians, the best gate pairing strategies retain their advantage across the tested shot counts in shallow circuits. These improvements come at the cost of increased circuit evaluations per gate update, highlighting a trade-off between the power of local optimization and measurement overhead.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25920v1
- Title: Impact of Topology on Multipartite Entanglement Distribution Protocols in Quantum Networks
- Authors: Jazz E. Z. Ooi, Evan Sutcliffe, Alejandra Beghelli
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.25920v1  pdf=https://arxiv.org/pdf/2603.25920v1.pdf

Abstract:
Quantum networks will rely on entanglement distribution to enable multi-user applications such as distributed quantum computing and cryptography. While multipartite entanglement distribution routing protocols have been extensively studied on idealised grid topologies, less is understood about how real network structure shapes their performance and resource requirements.   We present a systematic study of four routing protocols for multipartite entanglement distribution, each characterised by the number of paths (single-path and multi-path) and routing strategy (star-based and tree-based), over 81 real network topologies. We identified four distinct topology-dependent performance regimes, where: (i) all protocols perform poorly, (ii) tree-based protocols dominate, (iii) multi-path protocols dominate, or (iv) all protocols perform well. By correlating clusters with graph metrics, we also provide structural explanations for the varied performance of specific protocols.   Additionally, motivated by the anticipated high cost of repeaters, we investigated the impact of repeater trimming on the performance of multi-path protocols. Topology strongly governs how far repeater nodes can be removed from the network while maintaining a given performance (distribution rate). For instance, in networks where only 80% of nodes operate as repeaters, well-performing topologies are able to retain over 90% of the distribution rate; whereas sparse, weakly connected graphs exhibit rapid performance degradation, retaining less than half of the distribution rate.   Our results provide a topology-aware framework for protocol selection and infrastructure optimisation in future quantum networks, bridging routing design with cost-aware deployment strategies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25952v1
- Title: Scalable topological quantum computing based on Sine-Cosine chain models
- Authors: A. Lykholat, G. F. Moreira, I. R. Martins, D. Sousa, A. M. Marques, R. G. Dias
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2603.25952v1  pdf=https://arxiv.org/pdf/2603.25952v1.pdf

Abstract:
This work proposes a scalable framework for topological quantum computing using Matryoshka-type Sine-Cosine chains. These chains support high-dimensional qudit encoding within single systems, reducing the physical resource overhead compared to conventional qubit arrays. We describe how these chains can be used in Y-junction braiding protocols for gate operations and in extended memory architectures capable of storing multiple qubits simultaneously. Fidelity analysis shows partial topological protection against disorder, suggesting this approach is a possible pathway toward low-overhead quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26039v1
- Title: Achieving double-logarithmic precision dependence in optimization-based quantum unstructured search
- Authors: Zhijian Lai, Dong An, Jiang Hu, Zaiwen Wen
- Categories: quant-ph (primary); quant-ph; math-ph; math.OC
- Links: abs=https://arxiv.org/abs/2603.26039v1  pdf=https://arxiv.org/pdf/2603.26039v1.pdf

Abstract:
Grover's algorithm is a fundamental quantum algorithm that achieves a quadratic speedup for unstructured search problems of size $N$. Recent studies have reformulated this task as a maximization problem on the unitary manifold and solved it via linearly convergent Riemannian gradient ascent (RGA) methods, resulting in a complexity of $O(\sqrt{N}\log (1/\varepsilon))$. In this work, we adopt the Riemannian modified Newton (RMN) method to solve the quantum search problem. We show that, in the setting of quantum search, the Riemannian Newton direction is collinear with the Riemannian gradient in the sense that the Riemannian gradient is always an eigenvector of the corresponding Riemannian Hessian. As a result, without additional overhead, the proposed RMN method numerically achieves a quadratic convergence rate with respect to error $\varepsilon$, implying a complexity of $O(\sqrt{N}\log\log (1/\varepsilon))$, which is double-logarithmic in precision. Furthermore, our approach remains Grover-compatible, namely, it relies exclusively on the standard Grover oracle and diffusion operators to ensure algorithmic implementability, and its parameter update process can be efficiently precomputed on classical computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26063v1
- Title: MoSAIC: Scalable Probabilistic Error Cancellation via Variational Blockwise Noise Aggregation
- Authors: Maya Ma, Rimika Jaiswal, Murphy Yuezhen Niu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26063v1  pdf=https://arxiv.org/pdf/2603.26063v1.pdf

Abstract:
Quantum error mitigation is essential for extracting trustworthy results from noisy intermediate-scale quantum (NISQ) processors. Yet, current approaches face a core scalability bottleneck: unbiased methods such as probabilistic error cancellation (PEC) incur exponential sampling overhead, while approximate techniques like zero-noise extrapolation trade accuracy for efficiency. We introduce and experimentally demonstrate MoSAIC (Modular Spatio-temporal Aggregation for Inverted Channels), a scalable quantum error mitigation framework that preserves the unbiasedness of PEC while dramatically reducing sampling costs. MoSAIC partitions a circuit into noise-aligned blocks, learns an effective block noise model using classical variational optimization, and applies quasi-probabilistic inversion once per block instead of after every layer. This blockwise aggregation reduces both sampling overhead and circuit-depth overhead, enabling mitigation far beyond the operating regime of standard PEC. We also experimentally validate MoSAIC on IBM's 156-qubit Heron processors, performing the largest PEC-based mitigation demonstration on hardware to date. As a physically meaningful benchmark, we prepare the critical one-dimensional transverse-field Ising (TFIM) ground state for system sizes up to 50 qubits. We show that MoSAIC can achieve at least 1 to 2 orders of magnitude better accuracy than standard PEC under identical sampling budgets. This enables MoSAIC to recover accurate observables for larger system sizes, even when standard PEC fails due to its prohibitive sampling overhead. We also present CUDA-Q accelerated simulations to validate performance trends under a range of different noise models. These results demonstrate that MoSAIC is not only theoretically scalable but also practically deployable for high-accuracy, large-scale quantum experiments on today's quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26075v1
- Title: Minimal noise in non-quantized gravity
- Authors: Giuseppe Fabiano, Tomohiro Fujita, Akira Matsumura, Daniel Carney
- Categories: quant-ph (primary); quant-ph; gr-qc; hep-th
- Links: abs=https://arxiv.org/abs/2603.26075v1  pdf=https://arxiv.org/pdf/2603.26075v1.pdf

Abstract:
An elementary prediction of the quantization of the gravitational field is that the Newtonian interaction can entangle pairs of massive objects. Conversely, in models of gravity in which the field is not quantized, the gravitational interaction necessarily comes with some level of noise, i.e., non-reversibility. Here, we give a systematic classification of all possible such models consistent with the basic requirements that the non-relativistic limit is Galilean invariant and reproduces the Newtonian interaction on average. We demonstrate that for any such model to be non-entangling, a quantifiable, minimal amount of noise must be injected into any experimental system. Thus, measuring gravitating systems at noise levels below this threshold would be equivalent to demonstrating that Newtonian gravity is entangling. As concrete examples, we analyze our general predictions in a number of experimental setups, and test it on the classical-quantum gravity models of Oppenheim et al., as well as on a recent model of Newtonian gravity as an entropic force.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26102v1
- Title: Enhanced quantum violation of a non-contextual inequality and witnessing quantum dimension
- Authors: Ritwija Roy, Anindya Biswas
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26102v1  pdf=https://arxiv.org/pdf/2603.26102v1.pdf

Abstract:
We consider a non-contextual inequality in the sequential measurement scenario and derive the optimal quantum violation of it without assuming the dimension of the system. Since the measurement is dichotomic and the dimension of the quantum system is arbitrary, we formulate the concept of degeneracy-breaking (DB) measurement depending on how many projectors are being used in the sequential measurement. We demonstrate that by increasing the number of projectors involved in the sequential measurement (thereby making the measurement more degeneracy breaking) the quantum violation of non-contextual inequality can be enhanced and can even reach up to its algebraic maximum. We demonstrate that the optimal quantum violations for different number of projectors serves as a quantum dimension witness.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26160v1
- Title: Distributed Quantum Discrete Logarithm Algorithm
- Authors: Renjie Xu, Daowen Qiu, Ligang Xiao, Le Luo, Xu Zhou
- Categories: quant-ph (primary); quant-ph; cs.DC
- Links: abs=https://arxiv.org/abs/2603.26160v1  pdf=https://arxiv.org/pdf/2603.26160v1.pdf

Abstract:
Solving the discrete logarithm problem (DLP) with quantum computers is a fundamental task with important implications. Beyond Shor's algorithm, many researchers have proposed alternative solutions in recent years. However, due to current hardware limitations, the scale of DLP instances that can be addressed by quantum computers remains insufficient. To overcome this limitation, we propose a distributed quantum discrete logarithm algorithm that reduces the required quantum register size for solving DLPs. Specifically, we design a distributed quantum algorithm to determine whether the solution is contained in a given set. Based on this procedure, our method solves DLPs by identifying the intersection of sets containing the solution. Compared with Shor's original algorithm, our approach reduces the register size and can improve the success probability, while requiring no quantum communication.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26278v1
- Title: Decomposition of Multi-Qubit Gates for Circuit Cutting
- Authors: Ryota Tamura, Tomoya Kashimata, Yohei Hamakawa, Kosuke Tatsumura, Hiroshi Imai
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2603.26278v1  pdf=https://arxiv.org/pdf/2603.26278v1.pdf

Abstract:
A large-scale quantum circuit can be partitioned into multiple subcircuits through circuit cutting, where each subcircuit is executed multiple times and the expectation value of the original circuit is reconstructed by classical post-processing from their measurement (sampling) results. In this process, appropriate cut locations are identified after the user-designed quantum circuit, including multi-qubit gates that act on three or more qubits, has been decomposed into single-qubit gates and two-qubit gates such as the CNOT gate. Here, we present a method for reducing the sampling overhead, which refers to the increase in the number of samples required due to the cutting process, by modifying the decomposition strategy of multi-qubit gates. Using MCX and CCCX gates as representatives of multi-qubit gates, we demonstrate that the proposed decomposition method, which introduces a small number of ancilla qubits according to the identified cut locations, effectively decreases the sampling overhead.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26311v1
- Title: Majorana-XYZ subsystem code
- Authors: Tobias Busse, Lauri Toikka
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2603.26311v1  pdf=https://arxiv.org/pdf/2603.26311v1.pdf

Abstract:
We present a new type of a quantum error correction code, termed Majorana-XYZ code, where the logical quantum information scales macroscopically yet is protected by topologically non-trivial degrees of freedom. It is a $[n,k,g,d]$ subsystem code with $n=L^2$ physical qubits, $k= \lfloor L/2 \rfloor$ logical qubits, $g \sim L^2$ gauge qubits, and distance $d = L$. The physical check operations, i.e. the measurements needed to obtain the error syndrome, are $3$-local and nearest-neighbour. The code detects every 1- and 2-qubit error, and every error of weight 3 and higher (constrained by the distance) that is not a product of the 3-qubit check operations, however, these products act only on the gauge qubits leaving the code space invariant. The undetected weight-3 and higher operators are confined to the gauge group and do not affect logical information. While the code does not have local stabiliser generators, the logical qubits cannot be modified locally by an undetectable error, and in this sense the Majorana-XYZ code combines notions of both topological and local gauge codes while providing a macroscopic number of topological logical qubits. Taken as a non-gauge stabiliser code we can encode $k \sim L^2 - 3L$ logical qubits into $L^2$ physical qubits; however, the check operators then become weight $2L$. The code is derived from an experimentally promising system of Majorana fermions on the honeycomb lattice with only nearest-neighbour interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26333v1
- Title: Conjugate measurements, equilibration and emergent classicality
- Authors: S. Adarsh, P. N. Bala Subramanian, Sreeraj T. P
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2603.26333v1  pdf=https://arxiv.org/pdf/2603.26333v1.pdf

Abstract:
Simultaneous decoherence of conjugate observables of an open quantum system leads to a classical statistical mechanical description with constant phase space probability density in terms of a uniform ensemble. We investigate a scenario where this may be realized by measurement of basic conjugate observables of a quantum system by the environment.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26345v1
- Title: Controlled-Z gates with giant atoms in structured waveguides
- Authors: Walter Rieck, Ariadna Soro, Anton Frisk Kockum, Guangze Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26345v1  pdf=https://arxiv.org/pdf/2603.26345v1.pdf

Abstract:
Giant atoms are quantum emitters coupled to waveguides at multiple, spatially separated points, enabling interference effects that fundamentally change their light-matter interactions. A notable consequence of the interference is the emergence of decoherence-free interaction (DFI), which allows coherent excitation exchange between giant atoms via the waveguide without radiative loss. Leveraging DFI offers a promising route to implementing two-qubit quantum gates without the need for additional resources, positioning giant atoms as a versatile platform for scalable universal quantum simulators. However, existing work has focused primarily on continuous, Markovian waveguides; in structured waveguides, where non-Markovian effects become significant, only iSWAP gates have been explored. To address this gap, we introduce and analyze a protocol for implementing controlled-Z (CZ) gates with giant atoms in structured waveguides. We first show that while a minimal two-point coupling scheme supports DFI, it also exhibits strong non-Markovian effects that substantially degrade gate fidelity. To overcome this limitation, we propose an extended design featuring a third coupling point. This configuration suppresses non-Markovian effects and enables CZ gates with fidelities up to $97.7\%$ (assuming typical values for experimental imperfections). Our results broaden the accessible gate set for giant atoms in structured waveguides to include both iSWAP and CZ gates, advancing these systems as a pathway toward universal quantum simulators operating in non-Markovian environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26355v1
- Title: High-Visibility Franson Interference Enabled by Passive Photonic Integrated Interferometers at Telecom Wavelengths
- Authors: Ramin Emadi, Domenico Ribezzo, Giulia Guarda, Davide Bacco, Alessandro Zavatta
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26355v1  pdf=https://arxiv.org/pdf/2603.26355v1.pdf

Abstract:
High-visibility Franson interference at telecom C-band wavelengths is achieved using a cascaded periodically poled lithium niobate (PPLN) waveguide photon-pair source combined with fully passive, path-imbalanced Mach-Zehnder interferometers implemented on photonic integrated circuits (PICs). The interferometers require neither on-chip phase shifters nor active stabilization; instead, the phase is scanned via thermal tuning of the chip. By employing a narrow-linewidth continuous-wave (CW) pump and dense wavelength-division multiplexing (DWDM) filtering, energy-time entangled photon pairs with high spectral indistinguishability are generated. We achieve a 4.8% heralding efficiency and a two-photon interference visibility of 97.1% from sinusoidal fringe fitting (raw visibility 95.2% and background-corrected visibility 95.6%), alongside a coincidence-to-accidental ratio (CAR) exceeding 1000 at only 1.7 mW of pump power. These results represent one of the highest Franson-interference visibilities reported for a PIC-based analyzer within a compact, fiber-integrated platform.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26359v1
- Title: Automated near-term quantum algorithm discovery for molecular ground states
- Authors: Fabian Finger, Frederic Rapp, Pranav Kalidindi, Kerry He, Kante Yin, Alexander Koziell-Pipe, David Zsolt Manrique, Gabriel Greene-Diniz, et al.
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2603.26359v1  pdf=https://arxiv.org/pdf/2603.26359v1.pdf

Abstract:
Designing quantum algorithms is a complex and counterintuitive task, making it an ideal candidate for AI-driven algorithm discovery. To this end, we employ the Hive, an AI platform for program synthesis, which utilises large language models to drive a highly distributed evolutionary process for discovering new algorithms. We focus on the ground state problem in quantum chemistry, and discover efficient quantum heuristic algorithms that solve it for molecules LiH, H2O, and F2 while exhibiting significant reductions in quantum resources relative to state-of-the-art near-term quantum algorithms. Further, we perform an interpretability study on the discovered algorithms and identify the key functions responsible for the efficiency gains. Finally, we benchmark the Hive-discovered circuits on the Quantinuum System Model H2 quantum computer and identify minimum system requirements for chemical precision. We envision that this novel approach to quantum algorithm discovery applies to other domains beyond chemistry, as well as to designing quantum algorithms for fault-tolerant quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26374v1
- Title: Low-energy spectrum of double-junction superconducting circuits in the Born-Oppenheimer approximation
- Authors: Leo Uhre Jakobsen, Ksenia Shagalov, David Feldstein-Bofill, Morten Kjaergaard, Karsten Flensberg, Svend Krøjer
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26374v1  pdf=https://arxiv.org/pdf/2603.26374v1.pdf

Abstract:
The superconductor-insulator-superconductor Josephson junction is the fundamental nonlinear element of superconducting circuits. Connecting two junctions in series gives rise to higher-harmonic content in the total energy-phase relation, enabling new design opportunities in multimode circuits. However, the double-junction element hosts an internal mode whose spectrum is set by the finite capacitances of the individual junctions. Using a Born-Oppenheimer approximation that treats the additional mode as fast compared to the qubit mode, we analyze the double-junction circuit element shunted by a large capacitor. Here, we derive an effective single-mode model of the qubit containing a correction term owing to the presence of the internal mode. We explore experimentally relevant parameter regimes and find that our model accurately describes the low-energy spectrum of the qubit. We further discuss how eliminating the internal degree of freedom affects the system's periodic boundary conditions and how this leads to non-uniqueness in performing the Born-Oppenheimer approximation. Finally, we analyze the harmonic content of the double-junction element and discuss its sensitivity to charge noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26432v1
- Title: Reconstructing Quantum Dot Charge Stability Diagrams with Diffusion Models
- Authors: Vinicius Hernandes, Joseph Rogers, Rouven Koch, Thomas Spriggs, Brennan Undseth, Anasua Chatterjee, Lieven M. K. Vandersypen, Eliska Greplova
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cs.LG
- Links: abs=https://arxiv.org/abs/2603.26432v1  pdf=https://arxiv.org/pdf/2603.26432v1.pdf

Abstract:
Efficiently characterizing quantum dot (QD) devices is a critical bottleneck when scaling quantum processors based on confined spins. Measuring high-resolution charge stability diagrams (or CSDs, data maps which crucially define the occupation of QDs) is time-consuming, particularly in emerging architectures where CSDs must be acquired with remote sensors that cannot probe the charge of the relevant dots directly. In this work, we present a generative approach to accelerate acquisition by reconstructing full CSDs from sparse measurements, using a conditional diffusion model. We evaluate our approach using two experimentally motivated masking strategies: uniform grid-based sampling, and line-cut sweeps. Our lightweight architecture, trained on approximately 9,000 examples, successfully reconstructs CSDs, maintaining key physically important features such as charge transition lines, from as little as 4\% of the total measured data. We compare the approach to interpolation methods, which fail when the task involves reconstructing large unmeasured regions. Our results demonstrate that generative models can significantly reduce the characterization overhead for quantum devices, and provides a robust path towards an experimental implementation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26488v1
- Title: Hong-Ou-Mandel test to verify indistinguishability of the states emitted from a quantum key distribution transmitter implementing decoy Bennett-Brassard 1984 protocol
- Authors: Toshiya Tajima, Akihisa Tomita, Atsushi Okamoto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26488v1  pdf=https://arxiv.org/pdf/2603.26488v1.pdf

Abstract:
Quantum Key Distribution (QKD) systems require rigorous verification of device properties to ensure implementation security. A critical requirement is the indistinguishability of transmitted pulses encoded by different modulation patterns, as distinguishability through non-encoded degrees of freedom could enable undetected eavesdropping. We present a practical method for testing pulse indistinguishability in QKD transmitters based on Hong-Ou-Mandel (HOM) interference. We establish the theoretical equivalence between the SWAP test and HOM measurement for characterizing quantum state fidelity, demonstrating that HOM visibility directly relates to the trace of density matrix products for phase-randomized weak coherent pulses. We experimentally validated this approach using a high-speed QKD transmitter implementing the decoy BB84 protocol with time-bin encoding at 1.25 GHz. HOM interference was measured between adjacent pulses prepared in different Bennett-Brassard 1984 states (X0, X1, Y0, Y1) using superconducting nanowire single-photon detectors. The observed HOM visibility was approximately 0.3 across all state combinations, with no statistically significant differences detected. These results confirm that modulation does not compromise pulse indistinguishability in our transmitter. The HOM test provides a practical, quantum-optical method for security certification of QKD systems without requiring assumptions about specific degrees of freedom, using only standard fiber-optic components and single-photon detectors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26494v1
- Title: Entanglement as Memory: Mechanistic Interpretability of Quantum Language Models
- Authors: Nathan Roll
- Categories: quant-ph (primary); quant-ph; cs.CL
- Links: abs=https://arxiv.org/abs/2603.26494v1  pdf=https://arxiv.org/pdf/2603.26494v1.pdf

Abstract:
Quantum language models have shown competitive performance on sequential tasks, yet whether trained quantum circuits exploit genuinely quantum resources -- or merely embed classical computation in quantum hardware -- remains unknown. Prior work has evaluated these models through endpoint metrics alone, without examining the memory strategies they actually learn internally. We introduce the first mechanistic interpretability study of quantum language models, combining causal gate ablation, entanglement tracking, and density-matrix interchange interventions on a controlled long-range dependency task. We find that single-qubit models are exactly classically simulable and converge to the same geometric strategy as matched classical baselines, while two-qubit models with entangling gates learn a representationally distinct strategy that encodes context in inter-qubit entanglement -- confirmed by three independent causal tests (p < 0.0001, d = 0.89). On real quantum hardware, only the classical geometric strategy survives device noise; the entanglement strategy degrades to chance. These findings open mechanistic interpretability as a tool for the science of quantum language models and reveal a noise-expressivity tradeoff governing which learned strategies survive deployment.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26519v1
- Title: Generating function for Hermitian and non-Hermitian models
- Authors: Hua-Yu Bai, Yang Chen, Guang-Can Guo, Ming Gong, Xi-Feng Ren
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26519v1  pdf=https://arxiv.org/pdf/2603.26519v1.pdf

Abstract:
It is well known that Hermitian and non-Hermitian models exhibit distinct physics and require different theoretical tools. In this work, we propose a unified generating-function framework for both classes with generic boundary conditions and local impurities. Within this framework, any finite lattice model can be mapped to a generating function of the form G(z)=P(z)/Q(z), where Q(z) and P(z) denote the bulk recurrence relation and boundary terms or impurities, respectively. The problem of solving for eigenstates reduces to a simple criterion based on the cancellation of zeros of Q(z) and P(z). Applying this method to the Hatano-Nelson (HN) model, we show how boundary conditions and impurities determine the location of the zeros, thereby demonstrating the boundary sensitivity of non-Hermitian systems. We further investigate topological edge states in the non-Hermitian Su-Schrieffer-Heeger (SSH) model and identify its topological phase transition. Inspired by generating-function techniques widely used in discrete mathematics, particularly in the study of the Fibonacci sequence, our results establish a direct connection between non-Hermitian physics and recurrence relations, providing a new perspective for analyzing non-Hermitian systems and exploring their connections with discrete mathematical structures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26540v1
- Title: Symmetry-resolved properties of the trace distance in thermalizing SU(2) systems
- Authors: Haojie Shen, Jie Chen, Xiaoqun Wang
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2603.26540v1  pdf=https://arxiv.org/pdf/2603.26540v1.pdf

Abstract:
We study diagnostics of thermalization in quantum many-body systems with global SU(2) symmetry, where the standard eigenstate thermalization hypothesis (ETH) is generalized to its non-Abelian form. As an eigenstate-level probe, we introduce a symmetry-resolved trace distance constructed from the block structure of the reduced density matrix. This block structure separates spin-sector probabilities from configurational fluctuations within each sector, naturally leading to a decomposition into a probability trace distance and a configurational trace distance. The microcanonical average of the former is bounded by fluctuations of the corresponding spin-sector probabilities within a microcanonical energy window, whereas the latter captures finer intra-sector fluctuations. In non-Abelian thermalizing systems, these spin-sector-probability fluctuations are constrained by the non-Abelian ETH and therefore become exponentially suppressed with system size. Numerical studies of the one-dimensional \(J_1\)--\(J_2\) Heisenberg chain are consistent with this picture and suggest that, in the thermal regime, the trace distance is asymptotically dominated by the configurational trace distance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26561v1
- Title: Complexity of Quadratic Bosonic Hamiltonian Simulation: $\mathsf{BQP}$-Completeness and $\mathsf{PostBQP}$-Hardness
- Authors: Lilith Zschetzsche, Refik Mansuroğlu, Norbert Schuch
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2603.26561v1  pdf=https://arxiv.org/pdf/2603.26561v1.pdf

Abstract:
The computational complexity of simulating the dynamics of physical quantum systems is a central question at the interface of quantum physics and computer science. In this work, we address this question for the simulation of exponentially large bosonic Hamiltonians with quadratic interactions. We present two results: First, we introduce a broad class of quadratic bosonic problems for which we prove that they are $\mathsf{BQP}$-complete. Importantly, this class includes two known $\mathsf{BQP}$-complete problems as special cases: Classical oscillator networks and continuous-time quantum walks. Second, we show that extending the aforementioned class to even more general quadratic Hamiltonians results in a $\mathsf{PostBQP}$-hard problem. This reveals a sharp transition in the complexity of simulating large quantum systems on a quantum computer, as well as in the difference in complexity between their simulation on classical and quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26602v1
- Title: An Online Approach for Entanglement Verification Using Classical Shadows
- Authors: Marwa Marso, Sabrina Herbst, Jadwiga Wilkens, Vincenzo De Maio, Ivona Brandic, Richard Kueng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26602v1  pdf=https://arxiv.org/pdf/2603.26602v1.pdf

Abstract:
Quantum measurements are slow, while classical processors are fast, yet existing hybrid protocols never exploit this asymmetry. In this work, we propose an alternative formulation of classical estimators as online algorithms that are updated incrementally upon obtaining a new sample. Classical shadows are the natural fit for this approach: designed around the principle of measuring first and asking questions later, each snapshot is a self-contained classical description that can be processed immediately and independently. As a first demonstration, we focus on mixed state entanglement verification via PT-moments, moments of the partially transposed density matrix that provide experimentally accessible sufficient conditions for entanglement. We construct two unbiased online estimators that together characterize the fundamental challenge between memory footprint and per-shot computational cost: one scales to large systems at low moment order, the other handles high moment orders at the expense of memory exponential in system size. The online estimator certifies entanglement reliably and, by exploiting all $\binom{T}{m}$ combinations of snapshots, requires fewer samples than state-of-the-art baselines, turning entanglement detection from a purely offline diagnostic into a protocol that runs concurrently with the experiment.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26606v1
- Title: Rotating-Wave and Secular Approximations for Open Quantum Systems
- Authors: Daniel Burgarth, Paolo Facchi, Giovanni Gramegna, Kazuya Yuasa
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2603.26606v1  pdf=https://arxiv.org/pdf/2603.26606v1.pdf

Abstract:
We derive a nonperturbative bound on the distance between evolutions of open quantum systems described by time-dependent generators. We show how this result can be employed to provide an explicit upper bound on the error of the rotating-wave approximation in the presence of dissipation and decoherence. We apply the derived bound to the strong-coupling limit in open quantum systems and to the secular approximation used to obtain a master equation from the Redfield equation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26619v1
- Title: Entanglement and Quantum Coherence in Krylov Space Dynamics
- Authors: Swati Choudhary, Sukrut Mondkar, Ujjwal Sen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26619v1  pdf=https://arxiv.org/pdf/2603.26619v1.pdf

Abstract:
The spreading of quantum states in Krylov space under unitary dynamics provides a natural framework for characterizing quantum complexity. Quantifiers of this spreading, such as the spread complexity and the inverse participation ratio, depend explicitly on both the Hamiltonian and the initial state, rendering their connection to fundamental quantum resources such as entanglement and quantum coherence subtle. We establish quantitative bounds relating Krylov-space spreading to the entanglement of the evolved state and to the quantum coherence of the initial state. For bipartite systems, we have shown that the entanglement of the evolved state is upper bounded in terms of the entanglement of the Krylov basis vectors and the spread complexity. In the case of multipartite systems, analogous bounds are obtained for the inverse participation ratio, a quantifier of the delocalization of a quantum state in the Krylov basis, in terms of the geometric measures. Furthermore, for qubit and qutrit systems, we derive relations between the quantum coherence of the initial state in the energy eigenbasis and the spread complexity, valid for arbitrary Hamiltonians. Our results provide quantitative constraints linking Krylov-space complexity growth to fundamental quantum resources.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26642v1
- Title: Massless Dirac Fermions in curved surfaces with localized curvature
- Authors: A. R. N. Lima, D. F. S. Veras, J. E. G. Silva
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2603.26642v1  pdf=https://arxiv.org/pdf/2603.26642v1.pdf

Abstract:
We investigate how a localized curvature affects the dynamics of massless Dirac fermions in a curved surface. We consider a smooth bump with axial symmetry, adopting two specific geometric models, namely a Gaussian and a volcano-like bumps. By considering a minimal coupling between the spinor and the surface geometry, described by the vielbeins and the spin connection, we study the behavior of the wave function over the surface. By using appropriate numerical methods, we find a linear discrete energy spectrum for the Dirac fermions and its corresponding wavefunctions when the Fermi velocity is considered. It turns out that, since the curvature vanishes asymptotically, the electron states are free waves far from the bumps, but around the curved points, the wave function increases its probability density.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26655v1
- Title: Autonomous Hamiltonian certification and changepoint detection
- Authors: Steven T. Flammia, Dmitrii Khitrin, Muzhou Ma, Jamie Sikora, Yu Tong, Alice Zheng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.26655v1  pdf=https://arxiv.org/pdf/2603.26655v1.pdf

Abstract:
Modern quantum devices require high-precision Hamiltonian dynamics, but environmental noise can cause calibrated Hamiltonian parameters to drift over time, necessitating expensive recalibration. Detecting when recalibration is needed is challenging, especially since the very gates required for sophisticated verification protocols may themselves be miscalibrated. While cloud quantum computing services implement heuristic routines for triggering recalibration, the fundamental limits of optimal recalibration are not yet known. We develop efficient Hamiltonian certification and changepoint detection protocols in the autonomous setting, where we cannot rely on an external noiseless device and use only single-qubit gates and measurements, making the protocols robust to the calibration issues for multi-qubit operations they aim to detect. For unknown $n$-qubit Hamiltonians $H$ and $H_0$ with operator norm bounded by $M$, our certification protocol distinguishes whether $\|H-H_0\|_F\geqε$ or $\|H-H_0\|_F\leq O(ε/\sqrt{n})$ with sample complexity $O(nM^2\ln(1/δ)/ε^2)$ and total evolution time $O(nM\ln(1/δ)/ε^2)$. We achieve this by evolving random stabilizer product states and performing adaptive single-qubit measurements based on a classically simulable hypothesis state. Extending this to continuous monitoring, we develop an online changepoint detection algorithm using the CUSUM procedure that achieves a detection delay time bound of $O(nM\ln(M\mathbb{E}_\infty[T])/ε^2)$, matching the known asymptotically optimal scaling with respect to false alarm run time $\mathbb{E}_\infty[T]$. Our approach enables quantum devices to autonomously monitor their own calibration status without requiring ancillary systems, entangling operations, or a trusted reference device, offering a practical solution for robust quantum computing with contemporary noisy devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2201.05640v1
- Title: Scattering Loss in Precision Metrology due to Mirror Roughness
- Authors: Yehonathan Drori, Johannes Eichholz, Tega Edo, Hiro Yamamoto, Yutaro Enomoto, Gautam Venugopalan, Koji Arai, Rana X Adhikari
- Categories: physics.optics (primary); physics.optics; physics.ins-det; quant-ph
- Links: abs=https://arxiv.org/abs/2201.05640v1  pdf=https://arxiv.org/pdf/2201.05640v1.pdf

Abstract:
Optical losses degrade the sensitivity of laser interferometric instruments. They reduce the number of signal photons and introduce technical noise associated with diffuse light. In quantum-enhanced metrology, they break the entanglement between correlated photons. Such decoherence is one of the primary obstacles in achieving high levels of quantum noise reduction in precision metrology. In this work, we compare direct measurements of cavity and mirror losses in the Caltech 40m gravitational-wave detector prototype interferometer with numerical estimates obtained from semi-analytic intra-cavity wavefront simulations using mirror surface profile maps. We show a unified approach to estimating the total loss in optical cavities (such as the LIGO gravitational detectors) that will lead towards the engineering of systems with minimum decoherence for quantum-enhanced precision metrology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2312.04258v1
- Title: Digital Discovery of interferometric Gravitational Wave Detectors
- Authors: Mario Krenn, Yehonathan Drori, Rana X Adhikari
- Categories: astro-ph.IM (primary); astro-ph.IM; gr-qc; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2312.04258v1  pdf=https://arxiv.org/pdf/2312.04258v1.pdf

Abstract:
Gravitational waves, detected a century after they were first theorized, are spacetime distortions caused by some of the most cataclysmic events in the universe, including black hole mergers and supernovae. The successful detection of these waves has been made possible by ingenious detectors designed by human experts. Beyond these successful designs, the vast space of experimental configurations remains largely unexplored, offering an exciting territory potentially rich in innovative and unconventional detection strategies. Here, we demonstrate the application of artificial intelligence (AI) to systematically explore this enormous space, revealing novel topologies for gravitational wave (GW) detectors that outperform current next-generation designs under realistic experimental constraints. Our results span a broad range of astrophysical targets, such as black hole and neutron star mergers, supernovae, and primordial GW sources. Moreover, we are able to conceptualize the initially unorthodox discovered designs, emphasizing the potential of using AI algorithms not only in discovering but also in understanding these novel topologies. We've assembled more than 50 superior solutions in a publicly available Gravitational Wave Detector Zoo which could lead to many new surprising techniques. At a bigger picture, our approach is not limited to gravitational wave detectors and can be extended to AI-driven design of experiments across diverse domains of fundamental physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2507.13867v2
- Title: Linear response and exact hydrodynamic projections in Lindblad equations with decoupled Bogoliubov hierarchies
- Authors: Patrik Penc, Fabian H. L. Essler
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2507.13867v2  pdf=https://arxiv.org/pdf/2507.13867v2.pdf

Abstract:
We consider a class of spinless-fermion Lindblad equations that exhibit decoupled BBGKY hierarchies. In the cases where particle number is conserved, their late time behaviour is characterized by diffusive dynamics, leading to an infinite temperature steady state. Some of these models are Yang-Baxter integrable, others are not. The simple structure of the BBGKY hierarchy makes it possible to map the dynamics of Heisenberg-picture operators on few-body imaginary-time Schrödinger equations with non-Hermitian Hamiltonians. We use this formulation to obtain exact hydrodynamic projections of operators quadratic in fermions, and to determine linear response functions in Lindbladian non-equilibrium dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2512.07742v1
- Title: Strong zero modes in integrable spin-S chains
- Authors: Fabian H. L. Essler, Paul Fendley, Eric Vernier
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2512.07742v1  pdf=https://arxiv.org/pdf/2512.07742v1.pdf

Abstract:
We derive exact strong zero mode (ESZM) operators for integrable spin-S chains with open boundary conditions and a boundary field. Their locality properties are generally weaker than in the previously known cases, but they still imply infinite coherence times in the vicinity of the edges. We explain how such integrable chains possess multiple ground states describing a first-order quantum phase transition, and that the odd number of such states for integer S makes the weaker locality properties necessary. We make contact with more traditional approaches by showing how the ESZM for S=1/2 acts on energy eigenstates given by solutions of the Bethe equations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25762v1
- Title: QHap: Quantum-Inspired Haplotype Phasing
- Authors: Rui Zhang, Xian-Zhe Tao, Yibo Chen, Jiawei Zhang, Lei He, Dongming Fang, Lin Yang, Yuhui Sun, et al.
- Categories: q-bio.GN (primary); q-bio.GN; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25762v1  pdf=https://arxiv.org/pdf/2603.25762v1.pdf

Abstract:
Haplotype phasing, the process of resolving parental allele inheritance patterns in diploid genomes, is critical for precision medicine and population genetics, yet the underlying optimization is NP-hard, posing a scalability challenge. To address this, we introduce QHap, a haplotype phasing tool that leverages quantum-inspired optimization. By reformulating haplotype phasing as a Max-Cut problem and deploying a GPU-accelerated ballistic simulated bifurcation solver, QHap accelerates phasing while maintaining accuracy comparable to established phasing tools. On the highly polymorphic human major histocompatibility complex region, QHap demonstrates 4- to 20-fold acceleration with zero switch error across multiple long read sequencing platforms. The framework implements two strategies: a read-based method for regional phasing, and a single nucleotide polymorphism-based method that, through quality-weighted probabilistic edge construction, efficiently scales to chromosome-scale tasks. Integration of chromatin conformation capture data extends phase block contiguity by up to 15-fold, enabling near-chromosome-spanning haplotype reconstruction. QHap demonstrates that quantum-inspired algorithms operating on classical hardware offer a promising approach to addressing the growing computational demands of sequencing data, establishing a new paradigm for applying physics-inspired optimization to fundamental challenges in computational genomics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25775v1
- Title: Detecting Complex-Energy Braiding Topology in a Dissipative Atomic Simulator with Transformer-Based Geometric Tomography
- Authors: Yang Yue, Nan Li, Xin Zhang, Chenhao Wang, Zeming Fang, Zhonghua Ji, Liantuan Xiao, Suotang Jia, et al.
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25775v1  pdf=https://arxiv.org/pdf/2603.25775v1.pdf

Abstract:
Machine learning (ML) is shaping our exploration of topological matter, whose existence is inherently tied to the geometry of quantum states or energy spectra. In non-Hermitian systems, distinctive spectral geometry can lead to topological braiding of complex-energy bands, yet directly probing this topology-geometry interplay remains challenging. Here, we introduce a Transformer-based ML framework to capture this interplay and experimentally demonstrate it in a dissipative cold-atom simulator. Using a Bose-Einstein condensate, we engineer tunable dissipative two-level systems whose complex eigenenergies form braids. Owing to the density-dependent dissipation, the instantaneous energy braids exhibit topologically distinct structures at short and long times. The Transformer not only accurately predicts topological invariants for diverse energy braids but also, through its self-attention mechanism, autonomously highlights band crossings as the governing underlying geometric feature. Our work paves the way for ML-guided exploration of non-Hermitian topological phases in cold atoms and beyond.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25781v1
- Title: Structured-Light Magnetometry in a Coherently Controlled Atomic Medium
- Authors: Parkhi Bhardwaj, Shubhrangshu Dasgupta
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25781v1  pdf=https://arxiv.org/pdf/2603.25781v1.pdf

Abstract:
A structured-light-based approach for detecting magneto-optical rotation is presented, in which polarization rotation is mapped onto a directly observable spatial degree of freedom. A radially polarized Laguerre-Gaussian beam interacts with cold $^{87}\mathrm{Rb}$ atoms in the presence of a longitudinal magnetic field, where magnetically induced circular birefringence introduces a relative phase shift between the $σ_+$ and $σ_-$ components of the field, manifesting as a rotation of the interference pattern. The MOR angle is extracted directly from the angular displacement of the petal-shaped intensity distribution, eliminating the need for polarizers or Stokes-parameter analysis. This method converts conventional polarization-based magnetometry into a topology-based spatial readout, enabling spatially resolved magnetic-field sensing with potential applications in optical magnetometry and quantum sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25782v1
- Title: Negative energies and the breakdown of bulk geometry
- Authors: John Preskill, Mykhaylo Usatyuk, Shreya Vardhan
- Categories: hep-th (primary); hep-th; gr-qc; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25782v1  pdf=https://arxiv.org/pdf/2603.25782v1.pdf

Abstract:
One central question in quantum gravity is to understand how and why predictions from semiclassical gravity can break down in regimes with low spacetime curvature. One diagnostic of such a breakdown is that states which are orthonormal at the semiclassical level can receive large corrections to their inner products from quantum fluctuations. We study this effect by examining inner products in pure 2D JT gravity. Previous work showed that black hole states with long interiors exhibit a breakdown at length scales of order $e^{S_0}$, where $S_0$ is a parameter analogous to $1/G_N$ in higher dimensions. This breakdown is caused by the discreteness of the spectrum of the dual boundary random matrix theory. We show that the full sum over quantum fluctuations indicates a more dramatic breakdown at parametrically shorter lengths of order $e^{S_0/3}$. In the dual boundary description, these corrections arise from negative energy states appearing in rare members of the random matrix ensemble. These results demonstrate that non-perturbative effects can invalidate the semiclassical description at much smaller length scales than previously expected, providing a new mechanism for the breakdown of effective gravitational theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25784v1
- Title: A Dipolar Chiral Spin Liquid on the Breathed Kagome Lattice
- Authors: Francisco Machado, Sabrina Chern, Michael P. Zaletel, Norman Y. Yao
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.str-el; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25784v1  pdf=https://arxiv.org/pdf/2603.25784v1.pdf

Abstract:
Continuous control over lattice geometry, when combined with long-range interactions, offers a powerful yet underexplored tool to generate highly frustrated quantum spin systems. By considering long-range dipolar antiferromagnetic interactions on a breathed Kagome lattice, we demonstrate how these tools can be leveraged to stabilize a chiral spin liquid. We support this prediction with large-scale density-matrix renormalization group calculations and explore the surrounding phase diagram, identifying a route to adiabatic preparation via a locally varying magnetic field. At the same time, we identify the relevant low-energy degrees of freedom in each unit cell, providing a complementary language to study the chiral spin liquid. Finally, we carefully analyze its stability and signatures in finite-sized clusters, proposing direct, experimentally viable measurements of the chiral edge mode in both Rydberg atom and ultracold polar molecule arrays.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25801v1
- Title: Ultrabroadband Passive Laser Noise Suppression to Quantum Noise Limit through on-chip Second Harmonic Generation
- Authors: Geun Ho Ahn, Ziyu Wang, Devin J. Dean, Hubert S. Stokowski, Taewon Park, Martin M. Fejer, Jonathan Simon, Amir H. Safavi-Naeini
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25801v1  pdf=https://arxiv.org/pdf/2603.25801v1.pdf

Abstract:
Laser intensity noise limits performance in quantum sensing, metrology, and computing. Existing stabilization methods face a trade-off between bandwidth and complexity: electronic feedback loops are speed-limited, while optical resonators are constrained by narrow linewidths and locking requirements. Here, we demonstrate an all-optical "noise eater" that passively suppresses intensity fluctuations from DC to >10 gigahertz. By leveraging high-efficiency second-harmonic generation in nanophotonic lithium niobate waveguides, we operate at a pump-depletion stationary point where input fluctuations are decoupled from the output to first order. This passive and nonresonant nanophotonic device suppresses relative intensity noise by 25 to 60 dB over the full measurement bandwidth and stabilizes a noisy fiber amplifier output to the shot-noise limit. Our results establish a scalable, wide-bandwidth paradigm for laser stabilization essential for high-throughput quantum technologies and deployable photonic sensing systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25873v1
- Title: Modular Theory and the Bell-CHSH inequality in relativistic scalar Quantum Field Theory
- Authors: J. G. A. Caribé, M. S. Guimaraes, I. Roditi, S. P. Sorella
- Categories: hep-th (primary); hep-th; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25873v1  pdf=https://arxiv.org/pdf/2603.25873v1.pdf

Abstract:
The Tomita-Takesaki modular theory is employed to discuss the Bell-CHSH inequality in wedge regions. By using the Bisognano-Wichmann results, the construction of a set of wedge localized vectors in the one-particle Hilbert space of a relativistic massive scalar field in $1+1$ dimensions is devised to establish whether violations of the Bell-CHSH inequality might occur for different choices of Bell's operators. In particular, the construction of the wedge localized vectors employed in the seminal work by Summers-Werner is scrutinized and applied to Weyl and other operators. We also outline a possible path towards the saturation of Tsirelson's bound.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.25908v1
- Title: Extreme (Rogue) Waves: From Theory to Experiments in Ultracold Gases and Beyond
- Authors: A. Chabchoub, P. Engels, P. G. Kevrekidis, S. I. Mistakidis, G. C. Katsimiga, M. E. Mossman, S. Mossman
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; nlin.PS; quant-ph
- Links: abs=https://arxiv.org/abs/2603.25908v1  pdf=https://arxiv.org/pdf/2603.25908v1.pdf

Abstract:
In this Chapter, we review key theoretical and experimental advances in the study of extreme nonlinear wave events, called rogue waves (RWs), in both single-component attractively interacting and two-component repulsive mixtures of ultracold quantum gases. Starting from the exact rational solutions of the integrable focusing nonlinear Schroedinger model, the hierarchy of RW solutions is exemplified. These range from the Peregrine soliton (PS) and, related to it, the destabilization into a multi-peak cascade of PSs dubbed "Christmas-tree", to the Akhmediev breather, and Kuznetsov-Ma soliton as well as higher-order RWs. Emphasis is placed on their controllable dynamical emergence and characteristics in non-integrable quantum many-body systems described by Gross-Pitaevskii models and extensions thereof through different protocols such as modulational instability, gradient catastrophe, and dam-break flows. We further discuss how immiscible particle-imbalanced repulsive mixtures can be cast into effective attractive single-component environments capable of hosting RWs. Next, state-of-the-art experimental techniques are summarized within the ultracold realm that can be utilized to realize solitary waves, modulational instability, dispersive shock waves and RWs including the very recent first experimental observation of the PS, enabled through engineered effective focusing interactions and precise dynamical triggering. Observations of these extreme events in water waves, nonlinear optics and beyond are also outlined, highlighting their broader relevance and potential of emergence in disparate physical settings. Our exposition aims at showcasing ultracold atomic gases as versatile platforms for controllably generating and probing extreme nonlinear events, among others, in the quantum realm across integrable and non-integrable settings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26090v1
- Title: Cosmological Correlators Using Tensor Networks
- Authors: Ujjwal Basumatary, Aninda Sinha, Xinan Zhou
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26090v1  pdf=https://arxiv.org/pdf/2603.26090v1.pdf

Abstract:
We develop a nonperturbative tensor-network framework for computing cosmological correlators in de Sitter space and use it to test the proposal that suitably defined in-in correlators can be obtained from an in-out formalism by gluing the expanding and contracting Poincaré patches. Focusing on interacting $1+1$-dimensional $φ^4$ theory, we formulate finite-time lattice observables using Matrix Product State (MPS) techniques and analyze the regulator subtleties associated with the singular behavior near the patching surface. Within this regulated framework, we find controlled nonperturbative evidence for the proposed relation between in-in and in-out correlators in several examples. We also find suggestive evidence that the perturbative obstructions present for sufficiently light fields can be softened nonperturbatively, albeit in a regime of substantially larger entanglement. A central outcome of our analysis is an entanglement-based picture of the computation: for in-in evolution the entanglement remains modest and can decrease toward late times, whereas in the patched in-out set-up it grows significantly after the gluing slice. Thus, although the in-out formalism is perturbatively economical, the in-in formulation is numerically more favorable. We briefly discuss how the same strategy extends to low-angular-momentum sectors in $3+1$ dimensions, and why regimes of rapid entanglement growth may eventually motivate quantum-computing implementations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26121v1
- Title: Probing Unruh Effect from Enhanced Decoherence
- Authors: Ran Li, Zhong-Xiao Man, Jin Wang
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26121v1  pdf=https://arxiv.org/pdf/2603.26121v1.pdf

Abstract:
We investigate the decoherence of an Unruh-DeWitt detector coupled to scalar, electromagnetic, and spinor fields in four-dimensional Minkowski spacetime. By employing the Schwinger-Keldysh influence functional formalism, we derive a universal scaling law relating the decoherence rate to the proper acceleration $a$ and the scaling dimension $Δ$ of the environmental field operator. By analyzing both sharp (top-hat) and smooth Gaussian switching functions, it is shown that the decoherence rate in the asymptotic long-time limit scales as $a^{2Δ-1}$. This scaling indicates that increasing scaling dimension of the coupling field operators can significantly enhance the decoherence, thereby providing a more sensitive probe of the Unruh effect.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26151v1
- Title: Geometric Phase Effect in Thermodynamic Properties and in the Imaginary-Time Multi-Electronic-State Path Integral Formulation
- Authors: Jian Liu
- Categories: physics.chem-ph (primary); physics.chem-ph; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26151v1  pdf=https://arxiv.org/pdf/2603.26151v1.pdf

Abstract:
The geometric phase (GP) is a fundamental quantum effect arising from conical intersections (CIs), with profound consequences for vibronic energy levels. Standard imaginary-time path integral molecular dynamics (PIMD) based on the Born-Oppenheimer approximation does not account for the GP, potentially leading to significant errors in low-temperature thermodynamic properties. In this Perspective, we demonstrate that the multi-electronic-state path integral (MES-PI) formulation in imaginary time (developed in J. Chem. Phys. 2018, 148, 102319) naturally captures the GP effect through the electronic trace of the product of statistically weighted overlap matrices between successive imaginary-time slices. This crucial capability was already implicit in the benchmark MES-PIMD simulations in that foundational work. To isolate this topological effect from other nonadiabatic effects, we introduce a geometric signature matrix (for the CI) and a winding-number-induced phase factor, constructing an ad hoc GP-excluded MES-PI method. Comparing this ad hoc baseline against the rigorous MES-PI approach allows us to unambiguously quantify the impact of the GP on thermodynamic properties. While simpler approximations exist when only the ground electronic-state is considered, MES-PIMD is the most general and accurate approach applicable to real complex systems where the location and topology of CI seams are often not known a priori.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26185v1
- Title: Multifractal Analysis of the Non-Hermitian Skin Effect: From Many-Body to Tree Models
- Authors: Shu Hamanaka
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; cond-mat.mes-hall; cond-mat.stat-mech; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26185v1  pdf=https://arxiv.org/pdf/2603.26185v1.pdf

Abstract:
The non-Hermitian skin effect is an anomalous localization phenomenon induced by nonreciprocal dissipation and has attracted considerable attention in recent years both theoretically and experimentally. In this article, we review the multifractal aspects of the non-Hermitian skin effect. In particular, we discuss how the many-body skin effect exhibits multifractality in many-body Hilbert space, unlike the trivial Hilbert-space occupation of the single-particle skin effect on crystalline lattices. We further highlight that the many-body skin effect can coexist with random-matrix spectral statistics, in contrast to the multifractality associated with many-body localization, which typically accompanies the absence of ergodicity. We also introduce a solvable model on a Cayley tree as an effective description of the many-body Hilbert space, in which the multifractal dimensions can be obtained analytically. This review provides a unified perspective on multifractal structures in the non-Hermitian skin effect across single-particle, many-body, and tree models, and clarifies their distinctive relation to ergodicity in open quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26209v1
- Title: Lieb-Robinson bounds for Bose-Hubbard Hamiltonians: A review with a simplified proof
- Authors: Marius Lemm, Carla Rubiliani
- Categories: math-ph (primary); math-ph; math.AP; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26209v1  pdf=https://arxiv.org/pdf/2603.26209v1.pdf

Abstract:
We review recent progress on state-dependent Lieb-Robinson bounds for Bose-Hubbard Hamiltonians. In particular, Kuwahara, Vu, and Saito established that, for general bounded-density initial states, the Lieb-Robinson velocity is bounded by $t^{d-1}$ for large times, where $d$ denotes the lattice dimension. We present a shorter proof of the weaker, but still polynomial velocity bound $t^{d+ε}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26232v1
- Title: ParaQAOA: Efficient Parallel Divide-and-Conquer QAOA for Large-Scale Max-Cut Problems Beyond 10,000 Vertices
- Authors: Po-Hsuan Huang, Xie-Ru Li, Chi Chuang, Chia-Heng Tu, Shih-Hao Hung
- Categories: cs.DC (primary); cs.DC; cs.PF; cs.SE; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26232v1  pdf=https://arxiv.org/pdf/2603.26232v1.pdf

Abstract:
Quantum Approximate Optimization Algorithm (QAOA) has emerged as a promising solution for combinatorial optimization problems using a hybrid quantum-classical framework. Among combinatorial optimization problems, the Maximum Cut (Max-Cut) problem is particularly important due to its broad applicability in various domains. While QAOA-based Max-Cut solvers have been developed, they primarily favor solution accuracy over execution efficiency, which significantly limits their practicality for large-scale problems. To address the limitation, we propose ParaQAOA, a parallel divide-and-conquer QAOA framework that leverages parallel computing hardware to efficiently solve large Max-Cut problems. ParaQAOA significantly reduces runtime by partitioning large problems into subproblems and solving them in parallel while preserving solution quality. This design not only scales to graphs with tens of thousands of vertices but also provides tunable control over accuracy-efficiency trade-offs, making ParaQAOA adaptable to diverse performance requirements. Experimental results demonstrate that ParaQAOA achieves up to 1,600x speedup over state-of-the-art methods on Max-Cut problems with 400 vertices while maintaining solution accuracy within 2% of the best-known solutions. Furthermore, ParaQAOA solves a 16,000-vertex instance in 19 minutes, compared to over 13.6 days required by the best-known approach. These findings establish ParaQAOA as a practical and scalable framework for large-scale Max-Cut problems under stringent time constraints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26243v1
- Title: Noise modelling of waveguide based squeezed light sources
- Authors: Erik Anders Torsten Svanberg, Daniel Voigt, Vaishali Adya
- Categories: physics.optics (primary); physics.optics; physics.ins-det; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26243v1  pdf=https://arxiv.org/pdf/2603.26243v1.pdf

Abstract:
Squeezed states of light are used for precision metrology and quantum-enhanced measurements, with applications spanning communication and sensing. State-of-the-art squeezed-light sources typically rely on optical cavities to achieve high, usable levels of squeezing. Recently, waveguide-based squeezed-light sources have demonstrated significant improvements in achievable squeezing, with performance currently limited by fabrication-induced losses. In this work, we present a detailed analysis of waveguide-based squeezers, examining the effects of phase noise, multiple loss mechanisms, and fundamental light leakage seeding the squeezer. We further investigate a cascaded squeezer architecture, in which a second waveguide operates as a phase-sensitive amplifier to mitigate out-coupling and detection losses. Owing to their ease of integration, robustness to high pump powers, and low intrinsic phase noise, we propose waveguide-based squeezed-light sources as a promising alternative for quantum noise reduction in future gravitational wave detectors, such as the Einstein Telescope.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26255v1
- Title: On the interpretation of Hahn echo measurements in electron spin resonance scanning tunneling microscopy
- Authors: Paul Greule, Wantong Huang, Máté Stark, Kwan Ho Au-Yeung, Christoph Wolf, Soo-hyon Phark, Andreas J. Heinrich, Philip Willke
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26255v1  pdf=https://arxiv.org/pdf/2603.26255v1.pdf

Abstract:
Electron spin resonance scanning tunneling microscopy (ESR-STM) has become a powerful tool for probing spin dynamics and coherence of individual atoms and molecules on surfaces. In this work, we perform Rabi oscillation and Hahn echo pulse protocols on individual iron phthalocyanine (FePc) molecules on MgO/Ag(001) using ESR-STM. While Hahn echo protocols are widely used to extract spin coherence times, we show that in ESR-STM they are particularly susceptible to misinterpretation due to tunneling electrons generated by the applied radio-frequency (RF) voltage. The RF voltage not only drives the spin, but simultaneously probes and relaxes it, which consequently leads to an exponential decay that reflects spin relaxation rather than intrinsic phase coherence. We moreover show that varying both delay times in the refocusing pulse sequence is a reliable way to ensure a coherent nature of the echo signal. The extracted decay for the latter protocol suggests that T2 is approximately 30 ns and is thus closer to the decoherence time observed in Rabi oscillation measurements. This is significantly shorter than values reported in previous echo measurements. Our findings underscore the need for caution in interpreting T2 times from Hahn echo and Carr-Purcell protocols in ESR-STM and provide practical criteria for distinguishing true spin echoes from tunneling-induced relaxometry signals.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26318v1
- Title: STN-GPR: A Singularity Tensor Network Framework for Efficient Option Pricing
- Authors: Dominic Gribben, Carolina Allende, Alba Villarino, Aser Cortines, Mazen Ali, Román Orús, Pascal Oswald, Noureddine Lehdili
- Categories: q-fin.PR (primary); q-fin.PR; cs.CE; cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26318v1  pdf=https://arxiv.org/pdf/2603.26318v1.pdf

Abstract:
We develop a tensor-network surrogate for option pricing, targeting large-scale portfolio revaluation problems arising in market risk management (e.g., VaR and Expected Shortfall computations). The method involves representing high-dimensional price surfaces in tensor-train (TT) form using TT-cross approximation, constructing the surrogate directly from black-box price evaluations without materializing the full training tensor. For inference, we use a Laplacian kernel and derive TT representations of the kernel matrix and its closed-form inverse in the noise-free setting, enabling TT-based Gaussian process regression without dense matrix factorization or iterative linear solves. We found that hyperparameter optimization consistently favors a large kernel length-scale and show that in this regime the GPR predictor reduces to multilinear interpolation for off-grid inputs; we also derive a low-rank TT representation for this limit. We evaluate the approach on five-asset basket options over an eight dimensional parameter space (asset spot levels, strike, interest rate, and time to maturity). For European geometric basket puts, the tensor surrogate achieves lower test error at shorter training times than standard GPR by scaling to substantially larger effective training sets. For American arithmetic basket puts trained on LSMC data, the surrogate exhibits more favorable scaling with training-set size while providing millisecond-level evaluation per query, with overall runtime dominated by data generation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26398v1
- Title: In-Situ Differential-Light-Shift Cancellation for Trapped-Atom Clocks
- Authors: Jan Simon Haase, Alexander Fieguth, Igor Bröckel, Jens Kruse, Carsten Klempt
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26398v1  pdf=https://arxiv.org/pdf/2603.26398v1.pdf

Abstract:
Differential light shifts (DLS) induced by optical trapping fields fundamentally limit the stability and accuracy of trapped-atom microwave clocks. We demonstrate an in-situ method to cancel DLS by simultaneously interrogating multiple spatially separated atomic ensembles at different trap intensities generated from a common light source. By operating the ensembles at set intensity ratios and performing Ramsey spectroscopy, the intensity-dependent frequency shifts are measured within each experimental cycle and extrapolated to the zero-intensity limit. This approach effectively enables shot-to-shot determination of a DLS-free frequency without requiring magic wavelengths or species-specific cancellation schemes. We validate the method for Rb atoms trapped in time-averaged potentials by introducing controlled variations of the total trap power and show that the extrapolated frequency remains insensitive to these fluctuations. The technique is general and can be extended to other systematic shifts, providing a scalable route toward improved stability and accuracy in compact trapped-atom clocks and related quantum sensors relying on optical dipole traps

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26477v1
- Title: Caloric Phenomena and Stirling-Cycle Performance in Heisenberg- Kitaev Magnon Systems
- Authors: Bastian Castorene, Martin HvE Groves, Francisco J. Peña, Nicolas Vidal-Silva, Miguel Letelier, Roberto E. Troncoso, Felipe Barra, Patricio Vargas
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26477v1  pdf=https://arxiv.org/pdf/2603.26477v1.pdf

Abstract:
We investigate the Stirling-cycle performance of a Heisenberg--Kitaev magnonic medium with Dzyaloshinskii--Moriya (DM) interactions. Using linear spin-wave theory, we show the DM interaction preserves spectral symmetry, yielding even caloric responses and symmetric Stirling engine efficiency. In contrast, bond-dependent Kitaev exchange asymmetrically distorts the magnonic density of states, enabling distinct direct and inverse caloric effects. Consequently, Kitaev-driven cycles achieve significantly higher efficiencies than DM-driven protocols, approaching a high-performance saturation regime for negative couplings. This establishes exchange-anisotropic magnets as highly tunable platforms for nanoscale solid-state energy conversion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26627v1
- Title: Stability of nonlinear dissipative systems with applications in fluid dynamics
- Authors: Javier Gonzalez-Conde, Daniel Isla, Sergiy Zhuk, Mikel Sanz
- Categories: physics.flu-dyn (primary); physics.flu-dyn; math.AP; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26627v1  pdf=https://arxiv.org/pdf/2603.26627v1.pdf

Abstract:
Nonlinear partial differential equations are central to physics, engineering, and finance. Except in a limited number of integrable cases, their solution generally requires numerical methods whose cost becomes prohibitive in high-dimensional regimes or at fine resolution. Nonlinear phenomena such as turbulence are notoriously difficult to predict because of their extreme sensitivity to small variations in initial conditions, except when certain stability conditions are fulfilled. Indeed, stability allows us to achieve reliable approximate dynamics, since it determines whether small perturbations remain bounded or are amplified, potentially leading to markedly different long-term behavior. Here, we investigate the stability of dissipative partial differential equations with second-order nonlinearities. By analyzing the time evolution of solution norms in Sobolev spaces, we establish a sufficient condition for stability that links the characteristics of the linear dissipative operator, the quadratic nonlinear term, and the external forcing. The resulting criterion is expressed as an explicit inequality that guarantees stability for a wide range of initial conditions. As an illustration, we apply the framework to fluid-dynamical models governed by nonlinear partial differential equations. In particular, for the Burgers equation, the condition admits a natural interpretation in terms of the Reynolds number, thereby directly linking the stability threshold to the competition between viscous dissipation and inertial advection. We further demonstrate the scope of the approach by extending the analysis to the KPP-Fisher and Kuramoto-Sivashinsky equations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.26651v1
- Title: Gigahertz-clocked Generation of Highly Indistinguishable Photons at C-band Wavelengths
- Authors: Robert Behrends, Lucas Rickert, Nils D. Kewitz, Martin v. Helversen, Partim K. Saha, Mareike Lach, Jochen Kaupp, Yorick Reum, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2603.26651v1  pdf=https://arxiv.org/pdf/2603.26651v1.pdf

Abstract:
High-performance single-photon sources at telecom C-band wavelentghs are key building blocks for applications in long-distance quantum communication. Here, we report the generation of highly indistinguishable, single photons at a clock-rate of 2.5\,GHz. This is achieved by coherently driving the biexciton transition ($T_1^\mathrm{XX}=64(1)\,$ps) of a semiconductor quantum dot embedded in a microcavity with strong asymmetric Purcell enhancement. Employing pulsed two-photon resonant excitation, strong multiphoton suppression with $g^{(2)}(0) < 4\%$ and high two-photon-interference visibility of $V_\mathrm{raw}> 85\%$ is observed. The observed photon indistinguishability is close to the theoretical limit expected for the photonically engineered radiative cascade and matches values obtained at lower repetition rates. Our results show a substantial advancement towards interference-based quantum information protocols at unprecedented data rates in the telecom C-Band.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2410.10518v2
- Title: Reference-frame-independent quantum metrology
- Authors: Satoya Imai, Otfried Gühne, Géza Tóth
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2410.10518v2  pdf=https://arxiv.org/pdf/2410.10518v2.pdf

Abstract:
How can we perform a metrological task if only limited control over a quantum system is given? Here, we present systematic methods for conducting nonlinear quantum metrology in scenarios lacking a common reference frame. Our approach involves preparing multiple copies of quantum systems and then performing local measurements with randomized observables. First, we derive the metrological precision using an error propagation formula based solely on local unitary invariants, which are independent of the chosen basis. Next, we provide analytical expressions for the precision scaling in various examples of nonlinear metrology involving two-body interactions, like the one-axis twisting Hamiltonian. Finally, we analyze our results in the context of local decoherence and discuss its influences on the observed scaling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2411.03979v3
- Title: Harnessing quantum back-action for time-series processing
- Authors: Giacomo Franceschetto, Marcin Płodzień, Maciej Lewenstein, Antonio Acín, Pere Mujal
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2411.03979v3  pdf=https://arxiv.org/pdf/2411.03979v3.pdf

Abstract:
Quantum measurements affect the state of the observed systems via back-action. While projective measurements extract maximal classical information, they drastically alter the system's configuration. In contrast, indirect measurements balance information extraction with the degree of disturbance. Considering the prevalent use of projective measurements in quantum computing and communication protocols, the potential benefits of indirect measurements in these fields remain largely unexplored. In this work, we demonstrate that incorporating indirect measurements into a quantum machine-learning protocol known as quantum reservoir computing provides advantages in both execution time scaling and overall performance. We analyze different measurement settings by varying the measurement strength across two benchmarking tasks. Our results reveal that carefully optimizing both the reservoir Hamiltonian parameters and the measurement strength can significantly improve the quantum reservoir computing algorithm performance. Furthermore, our approach demonstrates improved memory performance when compared with state-of-the-art classical feedback protocols. This work provides a comprehensive and practical recipe to promote the implementation of indirect measurement-based protocols in quantum reservoir computing. Moreover, our findings motivate further exploration of experimental protocols that leverage the back-action effects of indirect measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2411.17547v4
- Title: Distance-Security Tradeoffs for Repeaterless End-to-End QKD Networks
- Authors: Sumit Chaudhary, Davide Li Calsi, JinHyeock Choi, Marc Geitz, Janis Nötzel
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2411.17547v4  pdf=https://arxiv.org/pdf/2411.17547v4.pdf

Abstract:
Quantum Key Distribution (QKD) offers provably secure, information-theoretic key exchange, but in long-distance scenarios without quantum repeaters, Trusted Nodes (TNs) are commonly employed despite introducing critical security risks. We propose a redundant key management method for QKD network that combines Twin Field QKD (TF-QKD) (or Measurement-Device Independent (MDI)-QKD) with a novel key-routing scheme to eliminate the need for truly trusted TNs. Quantum measurements are handled entirely within the network, minimizing end-user hardware requirements. Multiple QKD links connect intermediate nodes such that a successful attack requires the collusion of multiple adversarial nodes, greatly enhancing security over the traditional TN model. In this contribution, we discuss the tradeoff between security, key rates, and distances supported by the new method. Our analysis reveals that the improved redundant key management system may enable true end-to-end connectivity over several thousand kilometers while maintaining high security standards.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2502.02836v3
- Title: Quantum theory of surface lattice resonances
- Authors: Michael Reitz, Stephan van den Wildenberg, Arghadip Koner, George C. Schatz, Joel Yuen-Zhou
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.optics
- Links: abs=https://arxiv.org/abs/2502.02836v3  pdf=https://arxiv.org/pdf/2502.02836v3.pdf

Abstract:
The collective interactions of nanoparticles arranged in periodic structures give rise to high-$Q$ in-plane diffractive modes known as surface lattice resonances. While these resonances and their broader implications have been extensively studied within the framework of classical electrodynamics and linear response theory, a quantum optical theory capable of describing the dynamics of these structures, especially in the presence of material nonlinearities beyond \textit{ad hoc} few-mode approximations, is largely missing. To this end, we consider a lattice of metallic nanoparticles coupled to the electromagnetic field and derive the quantum input--output relations within the electric dipole approximation. As applications, we analyze coupling between the nanoparticle array and external quantum emitters, and show how the formalism extends to molecular optomechanics, where the high $Q$-factors of SLRs enable coupling to collective vibrational modes. We further consider arrays composed of saturable excitonic emitters, demonstrating how emitter nonlinearities can be used to switch the SLR condition between electronic transitions. Using a perturbative approach that accounts for population dynamics, we show how these effects can be probed in pump--probe experiments and give rise to nonlinear phase-matching phenomena. Our work provides a microscopic framework for modeling SLRs interacting with quantum emitters without phenomenological descriptions of the electromagnetic environment.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2502.14950v2
- Title: Symmetric observations without symmetric causal explanations
- Authors: Christian William, Patrick Remy, Jean-Daniel Bancal, Yu Cai, Nicolas Brunner, Alejandro Pozas-Kerstjens
- Categories: quant-ph (primary); quant-ph; cs.LG; math.ST; stat.ML
- Links: abs=https://arxiv.org/abs/2502.14950v2  pdf=https://arxiv.org/pdf/2502.14950v2.pdf

Abstract:
Inferring causal models from observed correlations is a challenging task, crucial to many areas of science. In order to alleviate the computational effort when sifting through possible causal explanations for some given observations, it is important to know whether symmetries in the observations correspond to symmetries in the underlying realization so that one can quickly discard impossible explanations. Via an explicit example, we demonstrate that, in general, symmetries cannot be exploited to reduce the hypothesis space. We use a tripartite probability distribution over binary events that is realized by using three (different) independent sources of classical randomness. We prove that even removing the condition that the sources distribute systems described by classical physics, the requirements that (i) the sources distribute the same physical systems, (ii) these physical systems respect relativistic causality, and (iii) the correlations are the observed ones are incompatible.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2504.01936v2
- Title: Fermionic Averaged Circuit Eigenvalue Sampling
- Authors: Adrian Chapman, Steven T. Flammia
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2504.01936v2  pdf=https://arxiv.org/pdf/2504.01936v2.pdf

Abstract:
Fermionic averaged circuit eigenvalue sampling (FACES) is a protocol to simultaneously learn the averaged error rates of many fermionic linear optical (FLO) gates simultaneously and self-consistently from a suitable collection of FLO circuits. It is highly flexible, allowing for the in situ characterization of FLO-averaged gate-dependent noise under natural assumptions on a family of continuously parameterized one- and two-qubit gates. We rigorously show that our protocol has an efficient sampling complexity, owing in-part to useful properties of the Kravchuk transformations that feature in our analysis. We support our conclusions with numerical results. As FLO circuits become universal with access to certain resource states, we expect our results to inform noise characterization and error mitigation techniques on universal quantum computing architectures which naturally admit a fermionic description.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2505.05199v3
- Title: Integrability and Chaos via fractal analysis of Spectral Form Factors: Gaussian approximations and exact results
- Authors: Lorenzo Campos Venuti, Jovan Odavić, Alioscia Hamma
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th; math-ph; nlin.CD
- Links: abs=https://arxiv.org/abs/2505.05199v3  pdf=https://arxiv.org/pdf/2505.05199v3.pdf

Abstract:
It is well known that the spectral form factor (SFF) of a possibly degenerate many-body Hamiltonian can be identified with a planar random walk taking steps of unequal length. In this paper we push this identification further and propose to study the chaotic content of a Hamiltonian $H$ via its associated random walk seen as a fractal, using the tools of fractal geometry. In particular we conjecture that for chaotic Hamiltonians the Hausdorff dimension of the frontier of the corresponding random walk approaches the universal value $d_F=4/3$ -- the same value obtained when the random walk describes a Wiener process. Our numerical simulations for non-integrable models confirm this expectation while for quasi-free integrable models we obtain a value $d_F = 1$. Additionally, we numerically show that ``Bethe Ansatz walkers'' fall into a category similar to the non-integrable walkers. To motivate this conjecture we consider many-body Hamiltonians with degenerate but rationally independent eigenvalues. We prove that if the degeneracies satisfy certain Lyapunov conditions, the random walk becomes a Wiener process, $d_F=4/3$, and the distribution of the SFF becomes Gaussian. This is the familiar Gaussian approximation for the SFF which we show to be violated at very low temperature. We also compute the moments of the SFF exactly under milder hypotheses thus solving the classical problem of determining the moments of a random walker taking steps of unequal lengths. Finally, we consider quasi-free Fermionic models with possibly degenerate but rationally independent one-particle spectra. We show that in this case the distribution of the SFF becomes log-Normal and also give the exact form of the moments under milder hypotheses.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2506.11855v3
- Title: Exact requirements for battery-assisted qubit gates
- Authors: Riccardo Castellano, Vasco Cavina, Martí Perarnau-Llobet, Pavel Sekatski, Vittorio Giovannetti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.11855v3  pdf=https://arxiv.org/pdf/2506.11855v3.pdf

Abstract:
We consider the implementation of a unitary gate on a qubit system S via a global energy-preserving operation acting on S and an auxiliary system B that can be seen as a battery. We derive a simple, asymptotically exact expression for the implementation error as a function of the battery state, which we refer to as the it Unitary Defect. Remarkably, this quantity is independent of the specific gate being implemented, highlighting a universal property of the battery itself. We show that minimizing the unitary defect, under given physical constraints on the battery state, is mathematically equivalent to solving a Lagrangian optimization problem, often corresponding to finding the ground state of a one-dimensional quantum system. Using this mapping, we identify optimal battery states that achieve the highest precision under constraints on energy, squared energy, number of levels and Quantum Fisher Information. Overall, our results provide an efficient method for establishing bounds on the physical requirements needed to implement a unitary gate via energy-preserving operations and for determining the corresponding optimal protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2506.21988v2
- Title: Unifying communication paradigms in measurement-based delegated quantum computing
- Authors: Fabian Wiesner, Jens Eisert, Anna Pappa
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2506.21988v2  pdf=https://arxiv.org/pdf/2506.21988v2.pdf

Abstract:
Delegated quantum computing (DQC) allows clients with low quantum capabilities to outsource computations to a server hosting a quantum computer. This process is often envisioned within the measurement-based quantum computing framework, as it naturally facilitates blindness of inputs and computation. Hence, the overall process of setting up and conducting the computation encompasses a sequence of three stages: preparing the qubits, entangling the qubits to obtain the resource state, and measuring the qubits to run the computation. There are two primary approaches to distributing these stages between the client and the server that impose different constraints on cryptographic techniques and experimental implementations. In the prepare-and-send setting, the client prepares the qubits and sends them to the server, while in the receive-and-measure setting, the client receives the qubits from the server and measures them. Although these settings have been extensively studied independently, their interrelation and whether setting-dependent theoretical constraints are inevitable remain unclear. By implementing the key components of most DQC protocols in the respective missing setting, we provide a method to build prospective protocols in both settings simultaneously and to translate existing protocols from one setting into the other.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2507.05055v2
- Title: Disentangling strategies and entanglement transitions in unitary circuit games with matchgates
- Authors: Raúl Morral-Yepes, Marc Langer, Adam Gammon-Smith, Barbara Kraus, Frank Pollmann
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2507.05055v2  pdf=https://arxiv.org/pdf/2507.05055v2.pdf

Abstract:
In unitary circuit games, two competing parties, an "entangler" and a "disentangler", can induce an entanglement phase transition in a quantum many-body system. The transition occurs at a certain rate at which the disentangler acts. We analyze such games within the context of matchgate dynamics, which equivalently corresponds to evolutions of non-interacting fermions. We first investigate general entanglement properties of fermionic Gaussian states (FGS). We introduce a representation of FGS using a minimal matchgate circuit capable of preparing the state and derive an algorithm based on a generalized Yang-Baxter relation for updating this representation as unitary operations are applied. This representation enables us to define a natural disentangling procedure that reduces the number of gates in the circuit, thereby decreasing the entanglement contained in the system. We then explore different strategies to disentangle the systems and study the unitary circuit game in two different scenarios: with braiding gates, i.e., the intersection of Clifford gates and matchgates, and with generic matchgates. For each model, we observe qualitatively different entanglement transitions, which we characterize both numerically and analytically.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2508.14200v2
- Title: Flag at origin: a modular fault-tolerant preparation for CSS codes
- Authors: Diego Forlivesi, David Amaro
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.14200v2  pdf=https://arxiv.org/pdf/2508.14200v2.pdf

Abstract:
Fault-tolerant (FT) preparation of diverse logical stabilizer states in quantum error-correcting (QEC) codes is essential for FT computation. Existing constructions of these FT circuits are often constrained by classical computational resources or result in unnecessarily large quantum circuits. This work introduces a modular construction for FT preparation circuits in CSS codes of arbitrary distance, yielding significantly more resource-efficient circuits than previous approaches, especially for the largest codes studied. The key insight is that in bipartite CX circuits used to prepare CSS states, $X$ errors propagate in one direction across the qubit partition, while $Z$ errors propagate in the opposite direction. By appending $X$-detecting flag gadgets to the first partition and $Z$-detecting flag gadgets to the second, the circuit becomes FT. To manage the associated overhead, we propose an algorithm that discovers optimal (or near-optimal) flag gadgets at any distance. These gadgets are reusable across different QEC codes and FT subroutines, such as flag-based QEC. We estimate the logical state preparation error using subset-sampling Monte Carlo simulations at the circuit level, combined with approximate maximum-likelihood look-up table decoding. On Quantinuum's H2-1 device, preparation of the $\lvert\bar{0}\rangle$ state in the [[23,1,7]] Golay code achieves a logical SPAM error rate of $3.3_{-2.4}^{+8.6} \times 10^{-4}$ with an acceptance rate of $47.23(86)\%$. This surpasses (within $95\%$ confidence intervals) the minimum SPAM error rate of $6.0(1.6) \times 10^{-4}$ for a physical $\lvert 0\rangle$, as well as the best previously demonstrated logical state preparations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2509.05290v3
- Title: Excitable quantum systems: the bosonic avalanche laser
- Authors: Louis Garbe, Peter Rabl
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2509.05290v3  pdf=https://arxiv.org/pdf/2509.05290v3.pdf

Abstract:
We investigate the dynamics of a lasing system driven by a current of bosonic (quasi-)particles via a dissipative three-mode mixing process. A semi-classical analysis of this system predicts distinct dynamical regimes, where both the cavity mode and the gain medium can undergo lasing transitions. Of particular interest is an intermediate self-pulsing phase that exhibits the characteristics of an excitable system and converts random input signals into separated, quasi-periodic pulses at the output. By performing exact Monte-Carlo simulations, we extend this analysis into the quantum regime and show that despite being dominated by huge bosonic particle number fluctuations, this effect -- reminiscent of coherence resonance -- survives even for rather low average photon numbers. Our system thus represents an intriguing model of an excitable quantum many-body system, with practical relevance for quantum detectors or autonomous quantum machines. As an illustration, we discuss the realization of this system with superconducting quantum circuits and its application as a number-resolved avalanche detector for microwave photons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2509.24551v2
- Title: Broadband Magnetless Isolation in a Flux-Pumped, Dispersion-Engineered Transmission Line
- Authors: M. Demarets, A. M. Vadiraj, C. Caloz, K. De Greve
- Categories: quant-ph (primary); quant-ph; physics.ins-det
- Links: abs=https://arxiv.org/abs/2509.24551v2  pdf=https://arxiv.org/pdf/2509.24551v2.pdf

Abstract:
Isolators are commonly found in the amplification chain of microwave setups to shield sensitive devices such as superconducting qubits from noise and back-scattered signals. Conventional ferrite-based isolators are bulky, lossy and rely on strong magnetic fields, which pose challenges for their co-integration in large-scale superconducting devices. Although several magnetless approaches based on parametric modulation have been explored to overcome these limitations, none has yet experimentally demonstrated wideband isolation on par with ferrite devices. Here, we propose a compact modulation-based isolator that achieves large isolation bandwidth using a dispersion-engineered transmission line. The engineered line forms an effective two-mode system that enables broadband isolation by supporting adiabatic mode conversion over a wide instantaneous bandwidth. Numerical simulations show that this architecture can provide more than 20 dB isolation across 4 - 8 GHz, matching the performance of ferrite-based isolators. Moreover, we propose an on-chip superconducting device implementation that shows promise against parameter variations and enables a scalable path for co-integration with future large-scale superconducting systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2510.07240v2
- Title: Shedding light on classical shadows: learning photonic quantum states
- Authors: Hugo Thomas, Ulysse Chabaud, Pierre-Emmanuel Emeriau
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.07240v2  pdf=https://arxiv.org/pdf/2510.07240v2.pdf

Abstract:
Learning quantum state properties is both a fundamental and practical problem in quantum information theory. Classical shadows have emerged as an efficient method for estimating properties of unknown quantum states, with rigorous statistical guarantees, by performing randomized measurement on few copies of the state. With the advent of photonic technologies, formulating efficient learning algorithms for such platforms comes out as a natural problem. Here, we introduce a practical classical shadow protocol for learning photonic quantum states via randomized passive linear optical transformations and photon-number measurement. We provide rigorous theoretical guarantees showing that our scheme is sample- and time-efficient for measuring physical observables of interest. We experimentally demonstrate our photonic classical shadow protocol on both a twelve-mode and a twenty-four-mode integrated quantum processing unit, and showcase its versatility with five different applications, including Hamiltonian measurement and learning complex photonic states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2511.02569v2
- Title: Squeezing enhanced nonreciprocal quantum correlations via Barnett effect
- Authors: E. Kongkui Berinyuy, A. -H. Abdel-Aty, P. Djorwe, N. Alessa, K. S. Nisar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.02569v2  pdf=https://arxiv.org/pdf/2511.02569v2.pdf

Abstract:
Cavity optomagnonic platforms offer a promising route for exploring quantum phenomena, particularly quantum correlations, which are vital resources for modern quantum technologies. Here, we propose a theoretical scheme for achieving nonreciprocal quantum correlations such as entanglement, and quantum discord via Barnett effect in a molecular-optomagnonical system, where a yttrium iron garnet sphere is placed in a microwave cavity that is hosting molecules. We show optimal parameter regimes for achieving nonreciprocal quantum correlations through Barnett effect. The generated entanglements are robust against thermal fluctuations, persisting even at high temperatures. Our scheme suggests a new tool for engineering noise-tolerant quantum correlations, and paves a way toward realizing novel nonreciprocal quantum devices by integrating magnons with molecular ensembles.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2511.06620v2
- Title: Fault-Tolerant Encoding of Logical Qudits in Spin Systems
- Authors: Sumin Lim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.06620v2  pdf=https://arxiv.org/pdf/2511.06620v2.pdf

Abstract:
Universal quantum computers require fault-tolerant logical qudits, as qudits naturally align with the simulation of multi-level physical systems. Here, we present a general framework and working examples for encoding fault-tolerant logical qudits in finite-dimensional spin systems. We construct distance-$3$, distance-$5$ codewords, and general $2t+1$-distance codes that can be implemented using a single physical qudit or a small number of coupled qudits for higher distances, while requiring a Hilbert space dimension significantly smaller than conventional constructions based on multiple logical qubits. Logical operations and error correction protocols can be implemented with polynomial scaling in the number of elementary operations. We further discuss schematic designs for physical implementation and required single-gate fidelities, which are compatible with current spin qudit platforms. This strategy provides a resource-efficient path toward realizing fault-tolerant logical qudits in finite multi-level physical systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.23628v2
- Title: Optimal pure state cloning and transposition are complementary channels
- Authors: Vanessa Brzić, Dmitry Grinko, Michał Studziński, Marco Túlio Quintino
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.23628v2  pdf=https://arxiv.org/pdf/2603.23628v2.pdf

Abstract:
State cloning and state transposition are fundamental transformations which, despite being desirable, cannot be perfectly realised due to two conceptually distinct constraints of quantum theory: cloning is forbidden by linearity, while transposition is ruled out by complete positivity. In this work, we show that, despite these different constraints, the best physically allowed realisation of both transformations arises from a single physical process described by an isometry, which simultaneously implements their best possible approximations. We first determine the optimal fidelity for transforming $N$ qudits into $K$ copies of their transposition and show that, for pure input states, it is achieved by an estimation strategy, which is the unique optimal strategy under the worst-case fidelity figure of merit. We further prove that the corresponding $N \to K$ transposition map is the complementary channel of the optimal universal symmetric $N \to N + K$ quantum cloning machine on pure states. We then present an explicit quantum circuit that realises $N \to K$ transposition and $N \to N + K$ cloning in parallel and analyse its gate efficiency. Finally, we investigate mixed-state $N \to 1$ qudit transposition and determine its maximal performance in terms of white-noise visibility, yielding the structural physical approximation of transposition in the multicopy regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.24557v2
- Title: Geometric Curvature Governs Work in Open Quantum Steady States
- Authors: Eric R. Bittner
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2603.24557v2  pdf=https://arxiv.org/pdf/2603.24557v2.pdf

Abstract:
Classical thermodynamics admits a geometric formulation in which work is associated with areas enclosed by cycles in state space. Whether an analogous structure persists in driven, dissipative quantum systems remains an open question. Here we show that quasistatic work in open quantum steady states is governed by an emergent geometric curvature in control-parameter space arising from steady-state coherence. For a driven dissipative two-level system, we construct a work one-form whose curvature determines the work produced in cyclic processes. The work vanishes under strong dephasing, identifying coherence as a necessary condition for nontrivial geometry. However, its magnitude is set not by the coherence itself but by the spatial structure of the curvature: cycles enclosing comparable areas produce different work depending on their location in parameter space. Reversing the cycle orientation reverses the sign of the work, confirming its geometric origin. These results establish a geometric framework for open quantum thermodynamics and identify curvature as the organizing principle of thermodynamic response, with direct implications for driven light--matter systems in cavity quantum electrodynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2403.11358v2
- Title: Spin dissymmetry in optical cavities
- Authors: Priyanuj Bordoloi, Jefferson Dixon, Zachary N. Mauri, Christopher J. Ciccarino, Feng Pan, Tony Low, Felipe H. da Jornada, Jennifer A. Dionne
- Categories: physics.app-ph (primary); physics.app-ph; cond-mat.mtrl-sci; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2403.11358v2  pdf=https://arxiv.org/pdf/2403.11358v2.pdf

Abstract:
We introduce the spin dissymmetry factor, a measure of the spin-selectivity in the optical transition rate of quantum particles. This spin dissymmetry factor is valid locally, including at material interfaces and within optical cavities. We design and numerically demonstrate a metasurface optical cavity with three-fold rotational symmetry that maximizes spin dissymmetry, thereby maximizing the spin-selective radiative coupling of a cavity-coupled emitter. We also show the near-field and far-field response of spin and chiral dipoles to these cavities that preferentially enhance either spin or chirality. Our approach emphasizes the difference between spin and chirality in the near-field and reveals a compact parameter for designing more efficient quantum optical devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2503.04889v2
- Title: Exceptional topology on nonorientable manifolds
- Authors: J. Lukas K. König, Kang Yang, André Grossi Fonseca, Sachin Vaidya, Marin Soljačić, Emil J. Bergholtz
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; math-ph; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2503.04889v2  pdf=https://arxiv.org/pdf/2503.04889v2.pdf

Abstract:
We classify gapped phases and characteristic nodal points of non-Hermitian band structures on two-dimensional nonorientable parameter spaces. Such spaces arise in a wide range of physical systems in the presence of nonsymmorphic parameter space symmetries. For gapped phases, we find that nonorientable spaces provide a natural setting for exploring fundamental structural problems in braid group theory, such as torsion and conjugacy. Gapless systems, which host exceptional points (EPs), explicitly violate fermion doubling, even in two-band models. We demonstrate that EPs traversing the nonorientable parameter space exhibit non-Abelian charge inversion. These braided phases and their transitions leave distinct signatures in the form of bulk Fermi arc degeneracies, offering a concrete route toward experimental realization and verification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2512.11494v2
- Title: High magnetic field response of superconductivity dome in quantum artificial High Tc superlattices with variable geometry
- Authors: Gaetano Campi, Andrea Alimenti, Sang-Eon Lee, Luis Balicas, Fedor F. Balakirev, G. Alexander Smith, Gennady Logvenov, Antonio Bianconi
- Categories: cond-mat.supr-con (primary); cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2512.11494v2  pdf=https://arxiv.org/pdf/2512.11494v2.pdf

Abstract:
It is known that cuprate artificial high Tc superlattices (AHTS) with period d, composed of quantum wells confining interface space charge in stoichiometric Mott insulator layers (S), with thickness L, at the interface with overdoped normal metallic cuprate layers (N) show a superconducting dome by tuning the geometric L over d ratio of the SNSN superlattice with the top predicted by quantum material design engineering quantum size effects. Here we report high-field magneto transport measurements up to 41 Tesla of AHTS across the entire superconducting dome. The results show the universal upward-concave behavior of the temperature dependent upper critical magnetic field in low Tc samples at rising edge and drop edge of the dome providing strong evidence consistent with two-band superconductivity for two-band superconductivity in agreement with multigap theory used for quantum design of the SNSN superlattices. The measured superconducting coherence length demonstrates that atomic-scale engineering controls not only the critical temperature but also the intrinsic pair size at Fano-Feshbach resonances physics paving the way toward next generation quantum devices and shedding light on unconventional superconductivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.23505v2
- Title: The HyperFrog Cryptosystem: High-Genus Voxel Topology as a Trapdoor for Post-Quantum KEMs
- Authors: Victor Duarte Melo
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2603.23505v2  pdf=https://arxiv.org/pdf/2603.23505v2.pdf

Abstract:
HyperFrog is an experimental post-quantum Key Encapsulation Mechanism that explores a variant of the Learning With Errors (LWE) design space in which the secret is not sampled from an independent product distribution, but is deterministically derived from discrete topological structure. The scheme embeds a voxel grid in three dimensions and uses a topology mining procedure to search for connected subgraphs with prescribed complexity, measured by cyclomatic number (high genus). The resulting structure is encoded as a sparse binary secret vector, inducing strong geometric constraints on the secret distribution while retaining a large combinatorial search space. Encapsulation produces noisy linear relations over public parameters and derives the shared key via hashing; a Fujisaki-Okamoto style transform is used to target IND-CCA security in the random oracle model. We present the construction, parameterization, and serialization format, together with a reference implementation featuring self-tests and benchmarking on commodity CPUs. We also discuss how topology-derived secrets interact with known lattice and decoding attacks, and we outline open problems required for conservative parameter selection and for a full security analysis. HyperFrog is intended as a research vehicle rather than a production-ready KEM.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-03-31 09:59
- arXiv: 2603.24230v2
- Title: A material-agnostic platform to probe spin-phonon interactions using high-overtone bulk acoustic wave resonators
- Authors: Q. Greffe, A. Hugot, S. Zhang, J. Jarreau, L. Del-Rey, E. Bonet, F. Balestro, T. Chanelière, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2603.24230v2  pdf=https://arxiv.org/pdf/2603.24230v2.pdf

Abstract:
Spin-phonon interactions have a dual role in emerging spin-based quantum technologies. While they can be a limitation to device performance through decoherence, they also serve as a critical resource for coherent spin control, detection, and the realization of spin-based quantum networks. However, their direct characterization remains a challenge and is usually material-dependent. Here, we introduce a technique to probe spin-phonon coupling at millikelvin temperatures and gigahertz frequencies, using high-overtone bulk acoustic wave resonators (HBARs) integrated with arbitrary crystals via visco-elastic transfer of thin-film lithium niobate transducers. By tuning the Larmor frequency of dilute spin ensembles into resonance with HBAR modes, we extract the anisotropy and strength of spin-phonon interactions from acoustic dispersion and dissipation measurements. We demonstrate this approach in calcium tungstate (CaWO4) and yttrium orthosilicate (Y2SiO5), achieving cooperativities up to 0.5 for erbium dopant ensembles. Our method enables the study of spin-phonon interactions in complex crystalline materials, with minimal fabrication constraints. These results will facilitate the design of hybrid quantum systems and the quest for ion-matrix combination with enhanced spin-phonon coupling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28821v1
- Title: HAMMR-L: Noise Reduction in Quantum Outcomes Using a Richardson-Lucy Deconvolution Algorithm for Quantum State Graphs
- Authors: Jake Scally, Austin Myers, Ryan Carmichael, Phat Tran, Xiuwen Liu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28821v1  pdf=https://arxiv.org/pdf/2603.28821v1.pdf

Abstract:
Current quantum computers present significant noise, especially as circuit depth and qubit count increase. Prior work has demonstrated that erroneous outcomes exhibit some behavior in Hamming space, enabling improvements in the output distributions of NISQ-era computers. We present HAMMR-L: a principled post-processing technique for improving the fidelity of output distributions by applying Richardson-Lucy image deconvolution on a state graph of measurement results connected by Hamming distance. We show that this preliminary implementation of HAMMR-L outperforms existing cutting-edge Hamming-based post-processors such as QBEEP while being circuit and hardware agnostic, which QBEEP is not. HAMMR-L also demonstrates clear potential for future improvements and we discuss how such improvements might be realized while highlighting the strengths, limitations, and generality of the underlying concept.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28827v1
- Title: Quantum Coherence and Giant Enhancement of Positron Channeling Radiation
- Authors: Michael Shatnev
- Categories: quant-ph (primary); quant-ph; hep-ex; physics.acc-ph
- Links: abs=https://arxiv.org/abs/2603.28827v1  pdf=https://arxiv.org/pdf/2603.28827v1.pdf

Abstract:
We present a quantum-mechanical calculation of positron channeling radiation in a planar harmonic potential, explicitly accounting for the interference between transition amplitudes from different transverse energy levels. Because the planar channel potential for positrons in diamond~(110) is well approximated by a parabola, the transverse spectrum is equidistant, $\varepsilon_n = Ω(n+\tfrac{1}{2})$, and all $n \to n{-}j$ transitions radiate at the same Doppler-shifted frequency. The entry of the positron into the crystal under the sudden approximation creates a Glauber coherent state with population amplitudes $c_n$. Phase synchronization between the $c_n$ and the dipole matrix elements ensures that all occupied levels contribute constructively to the radiation amplitude, giving an intensity $I_{\rm coh} \propto |A_j|^2$ that exceeds the incoherent (Zhevago--Kumakhov) result by a factor $\mathcal{G} = 12\text{--}31$ for positron energies of $4\text{--}14$~GeV in diamond~(110). Numerical results agree with the experimental peak positions of Avakyan \emph{et al.}~\cite{Avakyan1982}. The enhancement is unique to positrons because their nearly harmonic channel potential is not replicated for electrons. We propose a decisive experimental test of the coherent model based on the predicted nonlinear angular dependence of the peak intensity. The transition from $N$- to $N^2$-scaling of the radiated intensity, driven by quantum coherence, opens a route toward high-intensity monochromatic gamma-ray sources for nuclear physics and materials science.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28836v1
- Title: Geometric structure of the relativistic quantum phase space
- Authors: Philippe Manjakasoa Randriantsoa, Ravo Tokiniaina Ranaivoson, Raoelina Andriambololona, Roland Raboanary, Wilfrid Chrysante Solofoarisina, Anjary Feno Hasina Rasamimanana
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28836v1  pdf=https://arxiv.org/pdf/2603.28836v1.pdf

Abstract:
The relativistic quantum phase space (QPS) formalism extends classical phase space by incorporating both mean values and variance-covariance matrices of quantum states, thereby providing a unified setting where the uncertainty principle and relativistic covariance coexist. In this work we explore the basic geometric structure of the QPS for the signature \((1,4)\). We construct a scalar invariant built from the mean values and the inverse variance-covariance matrix, and prove its invariance under linear canonical transformations. For quantum states that saturate the uncertainty relations, and define the QPS itself, the invariant takes a value that encodes two fundamental length scales: a large scale characterising maximal coordinate uncertainties and a small scale characterising minimal coordinate uncertainties. From this invariance we derive a geometric equation that unifies the mean values and the quantum fluctuations. Analysing two asymptotic regimes reveals two physically significant limits: one leads to a curved spacetime geometry, consistent with current cosmological observations; the other yields a curved momenta space structure. These limits suggest a direct connection between quantum phase space geometry, cosmology, and quantum gravity, offering new perspectives on the origin of the quantum structure of spacetime. The results also resonate with the principle of Born reciprocity, which posits a fundamental duality between coordinates and momenta, and align with recent works on the relation between QPS and neutrino physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28846v1
- Title: Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations
- Authors: Ryan Babbush, Adam Zalcman, Craig Gidney, Michael Broughton, Tanuj Khattar, Hartmut Neven, Thiago Bergamaschi, Justin Drake, et al.
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2603.28846v1  pdf=https://arxiv.org/pdf/2603.28846v1.pdf

Abstract:
This whitepaper seeks to elucidate implications that the capabilities of developing quantum architectures have on blockchain vulnerabilities and mitigation strategies. First, we provide new resource estimates for breaking the 256-bit Elliptic Curve Discrete Logarithm Problem, the core of modern blockchain cryptography. We demonstrate that Shor's algorithm for this problem can execute with either <1200 logical qubits and <90 million Toffoli gates or <1450 logical qubits and <70 million Toffoli gates. In the interest of responsible disclosure, we use a zero-knowledge proof to validate these results without disclosing attack vectors. On superconducting architectures with 1e-3 physical error rates and planar connectivity, those circuits can execute in minutes using fewer than half a million physical qubits. We introduce a critical distinction between fast-clock (such as superconducting and photonic) and slow-clock (such as neutral atom and ion trap) architectures. Our analysis reveals that the first fast-clock CRQCs would enable on-spend attacks on public mempool transactions of some cryptocurrencies. We survey major cryptocurrency vulnerabilities through this lens, identifying systemic risks associated with advanced features in some blockchains such as smart contracts, Proof-of-Stake consensus, and Data Availability Sampling, as well as the enduring concern of abandoned assets. We argue that technical solutions would benefit from accompanying public policy and discuss various frameworks of digital salvage to regulate the recovery or destruction of dormant assets while preventing adversarial seizure. We also discuss implications for other digital assets and tokenization as well as challenges and successful examples of the ongoing transition to Post-Quantum Cryptography (PQC). Finally, we urge all vulnerable cryptocurrency communities to join the ongoing migration to PQC without delay.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28852v1
- Title: Color code off-the-hook: avoiding hook errors with a single auxiliary per plaquette
- Authors: Gilad Kishony, Austin Fowler
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28852v1  pdf=https://arxiv.org/pdf/2603.28852v1.pdf

Abstract:
Syndrome extraction in the planar color code is complicated by high weight stabilizers and hook errors that can reduce the circuit-level distance. With a single auxiliary qubit per plaquette, any spatially uniform circuit halves the circuit-level distance. We propose a single-auxiliary syndrome extraction circuit with color-dependent gate schedules that avoids all malign hook errors in the bulk, thereby preserving the full circuit-level distance. The circuit has minimal depth: all stabilizers of the same Pauli type are measured in parallel in six time steps. Furthermore, this schedule can be readily applied to the XYZ color code circuit, yielding an improved temporal distance. We find that at the boundary, no single hook error alone reduces the distance; instead, only certain combinations of hook errors do, which we call fractional hook errors. We demonstrate through Monte Carlo simulations over a range of circuit-level noise models and physical error rates that our circuit outperforms the previous state of the art.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28869v1
- Title: Quantum Suicide in Many-Worlds Implies P=NP
- Authors: Veronika Baumann, Alberto Rolandi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28869v1  pdf=https://arxiv.org/pdf/2603.28869v1.pdf

Abstract:
In this paper we propose a totally serious algorithm to solve NP problems in polynomial time provided one is willing to wager the fate of all observers in the universe on the many-world interpretation of quantum theory being correct.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28870v1
- Title: Non-stabilizerness and U(1) symmetry in chaotic many-body quantum systems
- Authors: Daniele Iannotti, Angelo Russotto, Barbara Jasser, Jovan Odavić, Alioscia Hamma
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2603.28870v1  pdf=https://arxiv.org/pdf/2603.28870v1.pdf

Abstract:
We present exact, closed-form results for the non-stabilizerness of random pure states subject to a U(1) symmetry constraint. Using stabilizer entropy as our non-stabilizerness monotone, we derive the average and the variance for U(1)-constrained Haar random states. We show that the presence of a conserved charge leads to a substantial suppression of non-stabilizerness (magic) compared to the unconstrained case, and identify a qualitative difference between entanglement and magic response. In the thermodynamic limit, stabilizer entropy exhibits a different leading-order scaling close to a vanishing relative charge density, implying that magic is more robust to charge density fluctuations than entanglement entropy. We test our analytical predictions against midspectrum eigenstates of two chaotic many-body systems with conserved $U(1)$ charge: the complex-fermion Sachdev-Ye-Kitaev (cSYK) model and a Heisenberg XXZ chain with next-to-nearest-neighbour couplings and conserved magnetization. We find an excellent agreement for the non-local cSYK model and systematic deviations for the local XXZ chain, highlighting the role of interaction locality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28877v1
- Title: Effects of measurements on entanglement dynamics for $1+1$D $\mathbb Z_2$ lattice gauge theory
- Authors: Nilachal Chakrabarti, Nisa Ara, Neha Nirbhan, Arpan Bhattacharyya, Indrakshi Raychowdhury
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; hep-lat; hep-th
- Links: abs=https://arxiv.org/abs/2603.28877v1  pdf=https://arxiv.org/pdf/2603.28877v1.pdf

Abstract:
The $1+1$ dimensional $\mathbb Z_2$ gauge theory is the simplest model that allows for quantum simulation to probe the fundamental aspects of a gauge theory coupled with dynamical fermions. To reliably benchmark such a system, it is crucial to understand the non-unitary quantum dynamics arising from the underlying non-Hermitian evolution and to model the effects of quantum measurements. This work focuses on measuring physical observables for a $\mathbb Z_2$ gauge theory. Tensor network calculations are performed to probe the effect of measurement for larger lattice sizes (up to 256-site systems). Using Matrix Product State calculations, the dynamics of entanglement entropy are studied as a function of the measurement rate and the coupling constant. We find that, under both local and non-local measurements, the late-time saturation value of the bipartite entanglement entropy remains independent of system size, indicating the absence of a measurement-induced phase transition in the no-click limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28879v1
- Title: Quantum Optical Neuron for Image Classification via Multiphoton Interference
- Authors: Giorgio Minati, Simone Roncallo, Simone Scrofana, Angela Rosy Morgillo, Nicoló Spagnolo, Chiara Macchiavello, Lorenzo Maccone, Valeria Cimini, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28879v1  pdf=https://arxiv.org/pdf/2603.28879v1.pdf

Abstract:
The rapid growth of machine learning is increasingly constrained by the energy and bandwidth limits of classical hardware. Optical and quantum technologies offer an alternative route, enabling high-dimensional, parallel information processing directly in the physical layer, particularly suited for imaging tasks. In this context, quantum photonic platforms provide both a natural mechanism for computing inner products and a promising path to energy-efficient inference in photon-limited regimes. Here, we experimentally demonstrate a camera-free quantum-optical images classifier that performs inference directly at the measurement layer using Hong-Ou-Mandel (HOM) interference of spatially programmable single photons. Two-photon coincidences directly report the overlap between an input image mode and a learned template, replacing pixel-resolved acquisition with a single global measurement. We realize both a single-perceptron quantum optical neuron and a two-neuron shallow network, achieving high accuracy on benchmark datasets with strong robustness to experimental noise and minimal hardware complexity. With a fixed measurement budget, performance remains insensitive to input resolution, demonstrating intrinsic robustness to the number of pixels, which would be impossible in a classical framework. This approach paves the way toward neuromorphic quantum photonic processors capable of extracting task-relevant information directly from HOM interference, with promising applications in remote object recognition, low-signal sensing, and photon-starved biological microscopy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28892v1
- Title: Real Variance-Based Variational Quantum Eigensolver for Non-Hermitian Matrices
- Authors: Durgesh Pandey, Ankit Kumar Das, P. Arumugam
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28892v1  pdf=https://arxiv.org/pdf/2603.28892v1.pdf

Abstract:
Non-Hermitian operators naturally arise in the description of open quantum systems, which exhibit features such as resonances and decay processes, where the associated eigenvalues are complex. Standard quantum algorithms, including the Variational Quantum Eigensolver (VQE), are designed for Hermitian operators and are ineffective in recovering correct eigenvalues for non-Hermitian matrices. We present a systematic formulation based on a Real Variance-based Variational Quantum Eigensolver (RVVQE) for non-Hermitian operators. A correct cost function that guarantees convergence to the true eigenstates is identified. Our implementation utilizes Hermitian measurements only, rendering the algorithm easily deliverable. The performance and scalability of the proposed algorithm on a hierarchy of dense non-Hermitian matrices of increasing dimension are demonstrated with numerical results and computational metrics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28894v1
- Title: Process-tensor approach to full counting statistics of charge transport in quantum many-body circuits
- Authors: Hari Kumar Yadalam, Mark T. Mitchison
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2603.28894v1  pdf=https://arxiv.org/pdf/2603.28894v1.pdf

Abstract:
We introduce a numerical tensor-network method to compute the statistics of the charge transferred across an interface partitioning an interacting one-dimensional many-body lattice system with $U(1)$ symmetry. Our approach is based on a matrix-product state representation of the process tensor (also known as influence functional or influence matrix) describing the effect of the bulk system on the degrees of freedom at the interface, allowing us to evaluate a multi-time correlation function that yields the moment-generating function of charge transfer. We develop a scheme to truncate non-Markovian correlations which preserves the proper normalization of the process tensor and ensures the correct physical properties of the generating function. We benchmark our approach by simulating magnetization transport within the Heisenberg spin-$1/2$ XXZ brickwork circuit model at infinite temperature. Our results recover the correct transport exponent describing ballistic, superdiffusive, and diffusive transport in different regimes of the model. We also demonstrate anomalous transport encoded by a self-similar scaling form of the moment-generating function outside of the ballistic regime. In particular, we confirm the breakdown of Kardar-Parisi-Zhang universality in higher-order transport cumulants at the isotropic point. Our work paves the way for process-tensor descriptions of non-Markovian open quantum systems to address current fluctuations in strongly interacting systems far from equilibrium.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28933v1
- Title: Iterative Optimization with Partial Convergence Guarantees on Neutral Atom Quantum Computers
- Authors: Cédrick Perron, Yves Bérubé-Lauzière, Victor Drouin-Touchette
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28933v1  pdf=https://arxiv.org/pdf/2603.28933v1.pdf

Abstract:
Neutral atom quantum computers (NAQCs) have emerged as a promising platform for solving the maximum weighted independent set (MWIS) problem. However, analog quantum approaches face two key limitations: constraints of the atomic layout on realizable graph geometries and the absence of performance guarantees. We introduce Lp-Quts, a hybrid quantum-classical framework that integrates an NAQC sampler into a classical cutting-plane algorithm. At each iteration, a relaxed linear program (RLP) bounds the MWIS and induces a reduced graph from which independent sets are sampled using an analog quantum sampler. A novel sample-informed separation problem guides odd-cycle cut selection and accelerates convergence. For t-perfect graphs, Lp-Quts inherits polynomial-time convergence guarantees from the classical theory of cutting planes. We evaluate our approach on instances with up to 300 vertices -- a scale that exceeds the capabilities of current NAQC hardware. In this regime, Lp-Quts reaches solutions within 5--10\% of optimality, outperforming direct analog quantum protocols and greedy baselines under equal sampling budgets. As expected, simulated annealing remains the strongest sample-based solver at this scale. These results demonstrate how quantum samplers can be effectively embedded within classical optimization frameworks to deliver near-optimal solutions with reduced quantum resources while preserving formal guarantees.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28973v1
- Title: Bell's Inequality, Causal Bounds, and Quantum Bayesian Computation: A Unified Framework
- Authors: Nick Polson, Vadim Sokolov, Daniel Zantedeschi
- Categories: quant-ph (primary); quant-ph; stat.CO
- Links: abs=https://arxiv.org/abs/2603.28973v1  pdf=https://arxiv.org/pdf/2603.28973v1.pdf

Abstract:
Bell inequalities characterize the boundary of the local-realist correlation polytope -- the set of joint probability distributions achievable by classical hidden-variable models. Quantum mechanics exceeds this boundary through non-commutativity, reaching the Tsirelson bound $2\sqrt{2}$ for CHSH. We show that this polytope structure is not specific to quantum foundations: it appears identically in the causal inference literature, where the instrumental inequality, the Balke--Pearl linear programming bounds, and the Tian--Pearl probabilities of causation all arise as facets of the same marginal compatibility polytope. Fine's theorem -- that CHSH inequalities hold if and only if a joint distribution exists -- is precisely the pivot: the instrumental variable model in causal inference is structurally equivalent to the Bell local hidden-variable model, with the instrument playing the role of the measurement setting and the latent confounder playing the role of the hidden variable $λ$. We develop this correspondence in detail, extending it to algorithmic (Kolmogorov complexity) and entropic formulations of Bell inequalities, the NPA semidefinite programming hierarchy, and the MIP$^*$=RE undecidability result. We further show that the Born-rule / Bayes-rule duality underlying quantum Bayesian computation exploits the same non-commutativity that enables Bell violation, providing polynomial speedups for posterior inference. The framework yields a concrete dictionary between quantum information theory, causal econometrics, and Bayesian computation, and suggests new directions including NPA-based quantum causal inference algorithms and quantum architectures for function approximation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28983v1
- Title: Can Quantum Field Theory be Recovered from Time-Symmetric Stochastic Mechanics? Part II: Prospects for a Trajectory Interpretation
- Authors: Simon Friederich, Mritunjay Tyagi
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2603.28983v1  pdf=https://arxiv.org/pdf/2603.28983v1.pdf

Abstract:
In a companion paper we derived a unique time-reversal-invariant stochastic generalization of the Liouville equation and showed that it coincides with the evolution equation for the Husimi $Q$-function in a broad class of bosonic quantum field theories. Here we investigate the prospects for interpreting that evolution equation in terms of underlying stochastic trajectories. Drawing on Drummond's time-symmetric stochastic action formalism, we show that the traceless diffusion Fokker-Planck equation defines a natural measure over stochastic trajectories conditional on mixed-time boundary conditions. However, we identify a significant gap: it has not been established that every $Q$-function can be represented as a weighted average of these conditional probabilities over boundary values. The trajectory interpretation holds for ensembles with fixed boundary conditions but does not straightforwardly extend to arbitrary quantum states. Despite this limitation, we show that Drummond's trajectory dynamics are fundamentally non-Markovian -- a natural consequence of combining stochasticity with time-reversal invariance. This non-Markovianity places the dynamics outside the scope of the ontological models framework and thereby explains why the major no-go theorems for hidden-variable theories do not rule out the approach. These results clarify both the achievements and the remaining challenges in the project of understanding quantum field theory as the statistical mechanics of time-symmetric stochastic processes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29065v1
- Title: Oxide-nitride heteroepitaxy for low-loss dielectrics in superconducting quantum circuits
- Authors: David A. Garcia-Wetten, Mitchell J. Walker, Peter G. Lim, André Vallières, Maria G. Jimenez-Guillermo, Miguel A. Alvarado, Dominic P. Goronzy, Anna Grassellino, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2603.29065v1  pdf=https://arxiv.org/pdf/2603.29065v1.pdf

Abstract:
Superconducting qubits show great promise for the realization of fault-tolerant quantum computing, but lossy, amorphous dielectrics limit current technology. Identifying highly crystalline and stoichiometric dielectrics with intrinsically low microwave loss is therefore a central materials challenge, yet experimentally validated platforms remain scarce. In this work, we integrate a crystalline dielectric into a heteroepitaxial TiN/$γ$-Al$_2$O$_3$/TiN trilayer grown via pulsed laser deposition. Correlative high-resolution imaging, diffraction, and spectroscopy measurements confirm the single-crystal quality and chemical integrity of all layers, with minimal defects and limited anion interdiffusion across the oxide-nitride interfaces. Using microwave lumped-element resonators with parallel-plate capacitors, we report the first direct measurement of the dielectric loss of epitaxial $γ$-Al$_2$O$_3$, for which we find a low intrinsic two-level system loss, $δ_{\text{TLS}}^0 = (2.8 \pm 0.1) \times 10^{-5}$. These results establish heteroepitaxial oxides on transition metal nitrides as an attractive materials platform for superconducting quantum circuits, particularly for integration into compact device architectures such as merged-element transmons and microwave kinetic inductance detectors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29099v1
- Title: Scalable phonon-laser arrays with self-organized synchronization
- Authors: Hugo Molinares, Guillermo Romero, Victor Montenegro, Vitalie Eremeev
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29099v1  pdf=https://arxiv.org/pdf/2603.29099v1.pdf

Abstract:
Quantum mechanical oscillators operating at frequencies up to the GHz regime have been predicted to support phonon lasing -- self-sustained coherent vibrational motion emerging when the effective gain exceeds intrinsic losses. Current phonon-laser proposals face two key limitations, namely: they lack scalability and rely on coupling all oscillators to a common field, which significantly restricts flexibility and prevents selective, on-demand phonon lasing at specific locations. Given that numerous applications and theoretical insights naturally emerge from scalable many-body systems, addressing these limitations is timely. In this Letter, we demonstrate how scalable arrays of individually addressable phonon lasers can be generated through local driving in a quantum many-body Ising-like spin chain. We rigorously establish the resonance conditions under which mechanical oscillators transition from thermal motion to sustained coherent self-oscillation. Unlike previous approaches that rely on a common coupling bus, our proposal employs purely local driving, resulting in an inherently modular and scalable architecture ideally suited for integration into large-scale quantum systems. Additionally, our approach enables on-demand lasing of individual mechanical oscillators at specific sites by simply switching the spin-mechanical coupling interaction on and off, provided specific resonance conditions are satisfied. Notably, our phonon laser array is robust against resonance mismatches and naturally exhibits both pairwise self-organized synchronization and global phase locking near resonance. Finally, we outline an experimental implementation within current experimental capabilities.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29175v1
- Title: High-efficiency and noise-immune quantum battery
- Authors: Guohui Dong, Mengqi Yu, Yao Yao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29175v1  pdf=https://arxiv.org/pdf/2603.29175v1.pdf

Abstract:
Nowadays, quantum batteries (QBs) have been designed to outperform their classical counterparts by leveraging quantum advantages. For instance, the charging power greatly benefits from the entanglement generation of a collective charging scheme (e.g., the Dicke QB), especially in the ultrastrong coupling (USC) regime or even larger. However, apart from the fragility of the QB under intrinsic decoherence effects, another critical drawback emerges inevitably. Specifically, the non-negligible counter-rotating (CR) term in the USC regime would induce coherence in the energy basis of QB, thus remarkably degrading the charging efficiency. To tackle these challenges, we propose a high-efficiency and noise-immune QB boosted by dynamical modulation. It is demonstrated that the time-varying modulation can effectively reduce the CR coupling, resulting in a notable improvement in charging efficiency. Particularly, for a judicious choice of modulation parameters that entirely eliminate the CR interaction, the Dicke QB can be charged optimally, resembling the behavior of the Tavis-Cummings QB. In the subsequent storage process, beyond the natural robustness to pure dephasing noise, our scenario is also highly resilient to the dissipation noise and thus can achieve perfect energy storage by effective bath engineering. While feasible with current experimental platforms, our proposal offers a solid foundation for the implementation of a powerful QB and may drastically promote the development of energy storage and delivery techniques in the future.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29180v1
- Title: Quantum heat transport in nonequilibrium anisotropic Dicke model
- Authors: Kong Junran, Mao Mang, Liu Huan, Wang Chen
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2603.29180v1  pdf=https://arxiv.org/pdf/2603.29180v1.pdf

Abstract:
Nonequilibrium heat transport and quantum thermodynamics in light-matter interacting systems have received increasing attention. Quantum thermal devices, e.g., heat valve and head diode, have been realized. Recently, it has been discovered that the anisotropic light-matter interactions can greatly modify the eigenvalues and eigenvectors of hybrid quantum systems, leading to nontrivial quantum phase transitions, quantum metrology, and nonclassicality of photons. To explore the influences of anisotropic light-matter interactions on quantum transport, we investigate heat flow in the nonequilibrium anisotropic Dicke model. In this model, an ensemble of qubits collectively interacts with an anisotropic photon field. Each component interacts with bosonic thermal reservoirs. Quantum dressed master equation (DME) is included to properly study dissipative dynamics of the anisotropic Dicke model. Within the eigenbasis of the reduced anisotropic Dicke system, strong qubit-photon couplings can be properly handled. Our results demonstrate that anisotropic qubit-photon interactions are crucial for modulating steady-state heat flow. In particular, it is found that under strong coupling the heat flow is dramatically suppressed by a large anisotropic qubit-photon factor. While under moderate coupling, the anisotropic qubit-photon interactions enhance the heat flow. Moreover, the increase in the number of qubits amplifies the flow characteristics, with the peaks increasing and the valleys decreasing. Besides, we derive two analytical expressions of heat flows in thermodynamic limit approximation with limiting anisotropic factors. These heat currents exhibit the cotunneling heat transport pictures. They also serve as the upper boundaries for the heat flows in the finite-size anisotropic Dicke model. We also analyze the thermal rectification effect in the anisotropic Dicke model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29196v1
- Title: Calculating the quantum Fisher information via the truncated Wigner method
- Authors: Thakur G. M. Hiranandani, Joseph J. Hope, Simon A. Haine
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29196v1  pdf=https://arxiv.org/pdf/2603.29196v1.pdf

Abstract:
In this work, we propose new methods of parameter estimation using stochastic sampling quantum phase-space simulations. We show that it is possible to compute the quantum Fisher information (QFI) from semiclassical stochastic samples using the Truncated Wigner Approximation (TWA). This method extends the class of quantum systems whose fundamental sensitivity limit can be computed efficiently to any system that can be modelled using the TWA, allowing the analysis of more meteorologically useful quantum states. We illustrate this approach with examples, including a system that evolves outside the spin-squeezing regime, where the method of moments fails.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29229v1
- Title: Direct measurement of the energy spectrum of a quantum dot qubit
- Authors: J. Reily, Daniel J. King, Jonathan C. Marcks, M. A. Wolfe, Piotr Marciniec, E. S. Joseph, Tyler J. Kovach, Brighton X. Coe, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29229v1  pdf=https://arxiv.org/pdf/2603.29229v1.pdf

Abstract:
The mapping between gate voltages applied to a double quantum dot, and the parameters of a Hubbard-like Hamiltonian, is of utmost importance for understanding and operating spin qubits. State-of-the-art techniques for measuring Hamiltonian parameters (e.g., detuning axis pulsed spectroscopy, DAPS) provide details about energy levels; however, tunnel coupling estimates typically reveal only a small portion of the full Hamiltonian. Here, we demonstrate a Hamiltonian-agnostic technique for measuring the double dot energy spectrum over a wide energy range, at every value of the detuning, called delta-axis spectroscopy (DAXS). We apply the DAXS method to obtain the energy spectrum of a Si/SiGe double quantum dot and use this data to extract the diagonal and off-diagonal couplings of a 15-level Hubbard-like Hamiltonian, demonstrating very good agreement with the experimental measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29256v1
- Title: From Promises to Totality: A Framework for Ruling Out Quantum Speedups
- Authors: Thomas Huffstutler, Upendra Kapshikar, David Miloschewsky, Supartha Podder
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29256v1  pdf=https://arxiv.org/pdf/2603.29256v1.pdf

Abstract:
We study when partial Boolean functions can (and cannot) exhibit superpolynomial quantum query speedups, and develop a general framework for ruling out such speedups via two complementary lenses: promise-aware complexity measures and function completions.   First, we introduce promise versions of standard combinatorial measures (including block sensitivity and related variants) and prove that if the relevant promise and completion measures collapse, then deterministic and quantum query complexities are necessarily polynomially related, i.e., $D(f)=poly(Q(f))$. We then analyze structured families of promises, including symmetric partial functions and promises supported on Hamming slices, obtaining sharp (up to polynomial factors) characterizations in terms of a single gap parameter for the symmetric case and refined slice-dependent bounds for $k$-slice domains.   Next, we formalize completion complexity as the minimum of a measure over total completions of a partial function, and show that completability of a measure captures the possibility of superpolynomial quantum speedups. Finally, we apply this viewpoint to derive broad non-speedup criteria for some classes of functions admitting well-behaved completions, such as functions with low maximum influence on both the standard and $p$-biased hypercubes and functions with efficiently identifiable domains, and then show some hardness results for general completion techniques.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29290v1
- Title: Entanglement between an NV Center and Chiral Photons in a Topological SWCNT Plasmonic Microtoroid
- Authors: Fang-Yu Hong
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29290v1  pdf=https://arxiv.org/pdf/2603.29290v1.pdf

Abstract:
We present a theoretical proposal for a hybrid solid-state quantum node based on a single nitrogen-vacancy (NV) center coupled to a topological single-walled carbon nanotube (SWCNT) plasmonic microtoroid. The SWCNT ring supports deeply sub-wavelength whispering-gallery-like plasmonic modes that are naturally described within a Tomonaga-Luttinger liquid framework. Owing to the closed-ring topology, the cavity spectrum contains a zero-mode sector that is tunable by an external magnetic flux through an Aharonov-Bohm shift. We show that the strongly confined CNT near field can exhibit chiral spin-momentum locking, enabling the two circularly polarized NV transitions to couple selectively to clockwise and counter-clockwise cavity modes, while the parasitic linearly polarized $π$-transition is strongly suppressed by the pronounced anisotropy of the local Purcell enhancement. Based on a tripod stimulated Raman adiabatic passage (STIRAP) scheme, the system can in principle map the NV spin onto a spin-photon entangled state in a deterministic manner, which is then emitted into a side-coupled tapered optical fiber as a tunable flying qubit. We derive the cavity spectrum, the chiral selection rules, the effective tripod Hamiltonian, and the open-system master equation. Quantitative estimates indicate that, under cryogenic conditions and in the overcoupled regime, high-fidelity spin-photon entanglement and in situ magnetic tuning of the emitted photon frequency are in principle achievable. We also discuss a realistic fabrication route for the CNT resonator and deterministic positioning strategies for a single NV center in the CNT near field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29308v1
- Title: Change in bit-flip times of Kerr parametric oscillators caused by their interactions
- Authors: Yuya Kano, Yohei Kawakami, Shumpei Masuda, Tomohiro Yamaji, Aiko Yamaguchi, Tetsuro Satoh, Ayuka Morioka, Kiyotaka Endo, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29308v1  pdf=https://arxiv.org/pdf/2603.29308v1.pdf

Abstract:
We experimentally investigate how interactions between Kerr parametric oscillators (KPOs) degrade their bit-flip times, where a bit flip is defined as a transition between the two degenerate ground states of a KPO. Interactions between KPOs cause quantum states of KPOs to leak outside the computational subspace, leading to bit flips. Bit flips degrade fidelity and pose a significant problem for KPO-based quantum information processing. We performed an experiment in which a weak microwave signal is injected into one KPO to emulate photon injection from another KPO, and find that the bit-flip time decreases by an order of magnitude due to induced excitations, depending on the frequency and power of the injected signal. Methods to mitigate the decrease in bit-flip times caused by interactions between KPOs are discussed, including adjusting the pump frequencies, coherent-state amplitudes, and couplings between KPOs. These findings provide valuable insights for scaling up KPO-based quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29323v1
- Title: On the Entanglement Entropy Distribution of a Hybrid Quantum Circuit
- Authors: Jeonghyeok Park, Hyukjoon Kwon, Hyeonseok Jeong
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29323v1  pdf=https://arxiv.org/pdf/2603.29323v1.pdf

Abstract:
We investigate the distribution of entanglement entropy in hybrid quantum circuits consisting of random unitary gates and local measurements applied at a finite rate. We demonstrate that higher moments of the entanglement entropy distribution, such as a ratio between the variance and the mean and skewness, capture nontrivial features of the measurement-induced dynamics that are invisible to the mean entropy alone. We demonstrate that these quantities exhibit distinct and robust behaviors across the volume-law and area-law phases, and can serve as effective diagnostics of measurement-induced entanglement transitions. We propose a phenomenological model describing the effect of measurements in the area-law regime, which, when combined with the directed polymer in a random environment description of the volume-law phase, well matches numerical simulations across the entire phase diagram.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29349v1
- Title: Multipartite controlled-NOT gates using molecules and Rydberg atoms
- Authors: Yi-Han Bai, Yue Wei, Chi Zhang, Weibin Li, Xiao-Qiang Shao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29349v1  pdf=https://arxiv.org/pdf/2603.29349v1.pdf

Abstract:
We propose high-fidelity controlled-NOT (CNOT) gates in a hybrid system of polar molecules and Rydberg atoms based on the unconventional Rydberg pumping mechanism. By combining the rich internal structure of polar molecules with the strong dipole-dipole interactions of Rydberg atoms, we realize both two-to-one and one-to-two gate configurations. Numerical simulations show that the gate performance is robust against spontaneous emission from Rydberg states. The approach naturally extends to larger systems, as demonstrated by four-qubit implementations achieving three-to-one and one-to-three CNOT gates with fidelities exceeding 99\%. These results highlight hybrid molecule-Rydberg atom architectures as a promising platform for scalable quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29379v1
- Title: YZ-plane measurement-based quantum computation: Universality and Parity Architecture implementation
- Authors: Jaroslav Kysela, Katharina Ludwig, Nitica Sakharwade, Anette Messinger, Wolfgang Lechner
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29379v1  pdf=https://arxiv.org/pdf/2603.29379v1.pdf

Abstract:
We define the class of register-logic graphs and prove that any uniformly deterministic measurement-based quantum computation (MBQC) where the inputs coincide with the outputs must be driven on such graphs by measurements in the $YZ$ plane of the Bloch sphere. This observation is revisited in the context that goes beyond uniform determinism, where we present a universal $YZ$-plane-only measurement pattern and establish a connection between $YZ$-plane-only and $XZ$-plane-only patterns. These results conclude the line of research on universal patterns with measurements restricted to one of the principal planes of the Bloch sphere. We further demonstrate, within the framework of the Parity Architecture, that $YZ$-plane patterns with the register-logic graph can be embedded into another graph with purely local interactions, and we extend this case to the scenario of universal quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29439v1
- Title: PAEMS: Precise and Adaptive Error Model for Superconducting Quantum Processors
- Authors: Songhuan He, Yifei Cui, Cheng Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29439v1  pdf=https://arxiv.org/pdf/2603.29439v1.pdf

Abstract:
Superconducting quantum processor units (QPUs) are incapable of producing massive datasets for quantum error correction (QEC) because of hardware limitations. Thus, QEC decoders heavily depend on synthetic data from qubit error models. Classic depolarizing error models with polynomial complexity present limited accuracy. Coherent density matrix methods suffer from exponential complexity $\propto O(4^n)$ where $n$ represents the number of qubits. This paper introduces PAEMS: a precise and adaptive qubit error model. Its qubit-wise separation framework, incorporating leakage propagation, captures error evolvements crossing spatial and temporal domains. Utilizing repetition-code experiment datasets, PAEMS effectively identifies the intrinsic qubit errors through an end-to-end optimization pipeline. Experiments on IBM's QPUs have demonstrated a 19.5$\times$, 9.3$\times$, and 5.2$\times$ reduction in timelike, spacelike, and spacetime error correlation, respectively, surpassing all of the previous works. It also outperforms the accuracy of Google's SI1000 error model by 58$\sim$73\% on multiple quantum platforms, including IBM's Brisbane, Sherbrooke, and Torino, as well as China Mobile's Wuyue and QuantumCTek's Tianyan.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29489v1
- Title: Open Quantum Systems from Dynamical Constraints
- Authors: Yu Su, Yao Wang
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2603.29489v1  pdf=https://arxiv.org/pdf/2603.29489v1.pdf

Abstract:
Open quantum systems are traditionally described by decomposing the total Hilbert space into a system and an external environment, linked by an explicit interaction Hamiltonian. We propose an alternative framework in which the environment is not introduced as an independent sector a priori, but instead emerges from the dynamical activation of constraints in an initially constrained quantum system. Within Dirac quantization, the physical degrees of freedom define the system, whereas the constraint sector, once promoted to carry its own dynamics, functions as an environment. In this picture, the system-environment coupling is not added through a separate interaction term, but is encoded directly in the constraint structure. As an example, we study a quantum particle coupled to a Brownian-oscillator environment and show how the resulting environmental influence can be formulated in this constraint-based setting. Our results provide a new perspective on the origin of quantum environments and point toward a general framework for open quantum systems rooted in constrained quantization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29498v1
- Title: Junction-Intrinsic Dissipation in Hybrid Superconductor-Semiconductor Gatemon Qubits
- Authors: Zhenhai Sun, David Feldstein-Bofill, Ksenia Shagalov, Amalie T. J. Paulsen, Casper Wied, Shikhar Singh, Brian D. Isakov, Jacob Hastrup, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2603.29498v1  pdf=https://arxiv.org/pdf/2603.29498v1.pdf

Abstract:
Superconducting transmon qubits based on hybrid superconductor-semiconductor Josephson junctions (gatemons) offer gate tunability, but their relaxation times remain well below those of state-of-the-art transmons, and the origin of this discrepancy is not fully understood. Here, we co-fabricate gatemons and SIS-junction transmons with nominally identical circuit layouts, gate dielectrics, and control lines, so that the Josephson element is the only intentional distinction. Across multiple chips, transmons in this architecture reach relaxation times in the tens of microseconds, whereas gatemons saturate in the few-microsecond range. Using the transmons as on-chip references, we construct a loss budget including Purcell decay, spontaneous emission through the control line, and internal dielectric loss, and find that the corresponding T1 limits exceed all measured gatemon values by more than an order of magnitude. Temperature-dependent T1 measurements follow a common quasiparticle-activation model and yield similar superconducting gaps for S-Sm-S and SIS junctions, indicating that the reduced gatemon coherence is dominated by additional temperature-independent, junction-intrinsic dissipation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29525v1
- Title: Non-perturbative CPMG scaling and qutrit-driven breakdown under compiled superconducting-qubit control: a single-qubit study
- Authors: Jun Ye
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29525v1  pdf=https://arxiv.org/pdf/2603.29525v1.pdf

Abstract:
Decoherence in superconducting qubits emerges from the interplay of multilevel dynamics and structured environmental noise, yet perturbative models cannot capture all resulting signatures. Here, EmuPlat couples instruction-set-architecture-level waveform generation to the hierarchical equations of motion (HEOM) under $1/f$ non-Markovian pure dephasing. In the resulting non-perturbative regime -- where filter-function predictions become quantitatively uninformative -- CPMG scaling of a three-level superconducting transmon yields one calibration result, two physical findings, and one structural null. Y-CPMG exhibits axis-dependent scaling-law breakdown -- non-monotonic decoherence, partial coherence revival, and pronounced X--Y population asymmetry ($0.204$ vs ${<}\,0.01$) -- driven by third-level anharmonicity amplified by bath memory; X-CPMG maintains well-behaved power-law scaling with a finite-$n$ transient excess consistent with non-Markovian bath-memory effects. The structural null is equally informative: waveform-level differences -- Standard versus VPPU realizations -- remain undetectable across all coupling strengths, establishing that rotating-frame pure-dephasing coupling renders control-layer detail invisible to scaling observables. These findings define testable predictions, the most experimentally accessible requiring only qualitative verification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29536v1
- Title: Logical-to-Physical Compilation for Reducing Depth in Distributed Quantum Systems
- Authors: Folkert de Ronde, Stephan Wong, Sebastian Feld
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29536v1  pdf=https://arxiv.org/pdf/2603.29536v1.pdf

Abstract:
Quantum computing is expected to become a foundational technology for solving problems that exceed the capabilities of classical systems. As quantum algorithms and hardware technologies continue to advance, the need for scalable architectures becomes increasingly clear. Distributed quantum computing offers a promising path forward by interconnecting multiple smaller processors into a larger, more powerful system. However, distributed quantum computing introduces significant circuit depth overhead, as logical operations are typically decomposed into sequential physical procedures that require entanglement generation. These sequential operations limit the reliability of quantum algorithms in the NISQ era due to noise. In this work, we present a compiler that integrates logical-to-physical decomposition with depth-aware rescheduling to reduce the execution cost of distributed quantum circuits. The compiler identifies sequences of logical CNOT gates that share a control or target qubit, reschedules them into parallel instruction groups, and applies decompositions that allow multiple gates to be executed simultaneously using distributed shared entanglement resources. An algorithm is proposed that ensures parallelism is created when possible while keeping logical equivalence and that circuit depth is never increased. Benchmark results demonstrate that the compiler consistently reduces circuit depth for circuits containing inherently sequential CNOT structures, while leaving already-parallel circuits unchanged. These results highlight the value of combining scheduling and hardware-aware decomposition, and establish the compiler as a practical tool for improving the fidelity of distributed quantum computations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29543v1
- Title: Reducing Complexity for Quantum Approaches in Train Load Optimization
- Authors: Zhijie Tang, Albert Nieto-Morales, Arit Kumar Bishwas
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2603.29543v1  pdf=https://arxiv.org/pdf/2603.29543v1.pdf

Abstract:
Efficiently planning container loads onto trains is a computationally challenging combinatorial optimization problem, central to logistics and supply chain management. A primary source of this complexity arises from the need to model and reduce rehandle operations-unproductive crane moves required to access blocked containers. Conventional mathematical formulations address this by introducing explicit binary variables and a web of logical constraints for each potential rehandle, resulting in large-scale models that are difficult to solve. This paper presents a fundamental departure from this paradigm. We introduce an innovative and compact mathematical formulation for the Train Load Optimization (TLO) problem where the rehandle cost is calculated implicitly within the objective function. This novel approach helps prevent the need for dedicated rehandle variables and their associated constraints, leading to a dramatic reduction in model size. We provide a formal comparison against a conventional model to analytically demonstrate the significant reduction in the number of variables and constraints. The efficacy of our compact formulation is assessed through a simulated annealing metaheuristic, which finds high-quality loading plans for various problem instances. The results confirm that our model is not only more parsimonious but also practically effective, offering a scalable and powerful tool for modern rail logistics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29574v1
- Title: Adiabatic Ramsey Interferometry for Measuring Weak Nonlinearities with Super-Heisenberg Precision
- Authors: Venelin P. Pavlov, Bogomila S. Nikolova, Peter A. Ivanov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29574v1  pdf=https://arxiv.org/pdf/2603.29574v1.pdf

Abstract:
We propose an adiabatic Ramsey interferometry technique for detecting weak nonlinearities with trapped ions. The method relies on using the quantum Rabi model as a probe, which is sensitive to nonlinear symmetry-breaking perturbations. We show that the couplings which arise either from anharmonic terms of the trapping potential or due to higher order terms in the Coulomb interaction expansion can be efficiently estimated by measuring the spin state probabilities alone. We show that the spin signal is amplified by the mean-phonon excitations, which results in the estimation precision reaching the super-Heisenberg limit. Notably, achieving such high-precision estimation does not require specific entangled state preparation and can be reached even for initial thermal motion state. Furthermore, we show that the super-Heisenberg scaling can be observed even in the presence of weak spin-dephasing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29601v1
- Title: Quantum connectivity of quantum networks
- Authors: Md Sohel Mondal, Shashank Shekhar, Siddhartha Santra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29601v1  pdf=https://arxiv.org/pdf/2603.29601v1.pdf

Abstract:
The practical utility of a quantum network depends on its ability to establish entanglement between arbitrary node pairs with quality sufficient to execute entanglement enabled tasks. This capability can be assessed globally, through aggregate performance over all node pairs, as well as locally, at the level of individual nodes. Since entanglement-based connections form a layer above the underlying physical topology, quantum connectivity is not adequately captured by classical topological connectivity metrics. To enable characterisation of the quantum connectivity at the level of the network (or its subnetworks), we introduce the quantum connectivity measure (QCM), which quantifies the average connection quality between pairs of network nodes. Further, we describe two quantities, the quantum-connected fraction (QCF) and the quantum clustering coefficient (QCC), naturally derived from the QCM, which capture important features of the functional connectivity of the quantum network at the level of the network and an individual node, respectively. These metrics of quantum connectivity depend crucially on the entanglement distribution protocol and the quantum network parameters in addition to its physical topology. We demonstrate the crucial distinction between topological and quantum connectivity, showing that even a fully connected graph can be functionally disconnected for quantum tasks if average network edge-concurrence falls below a critical threshold. These quantum connectivity metrics thus provide important tools for the design, optimization, and benchmarking of future quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29625v1
- Title: Entanglement in prepare-and-measure scenarios without receiver inputs
- Authors: Elna Svegborn, Armin Tavakoli
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29625v1  pdf=https://arxiv.org/pdf/2603.29625v1.pdf

Abstract:
The most elementary prepare-and-measure scenarios have no independent measurement inputs. No inputs mean that quantum advantages require two indispensable ingredients: shared entanglement and measurements that can be adapted to the communicated messages. Understanding these scenarios is therefore conceptually natural, but also practically relevant, since they act as testbeds for black-box certification of adaptive one-way LOCC. Here, we study them systematically and reveal several of their basic features. For classical messages, we first identify the minimal scenario with a quantum advantage and show that it is maximised by high-dimensional entanglement. Then, we identify the next-to-minimal scenario, and show that quantum advantages can be propelled by nonlocality of the Clauser-Horne-Shimony-Holt type, which makes this an appropriate setting for certification experiments. Proceeding further, we replace classical messages with quantum messages, but require the receiver to read the message before measuring the entangled particle. We show that this leads to amplified quantum advantages, that are made possible only thanks to non-projective message read-out. This in dispensable role of non-projective measurements challenges the common wisdom that they play a secondary role in revealing the power of quantum correlations in black-box experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29650v1
- Title: Non-Equilibrium Sock Dynamics: Spontaneous Symmetry Breaking in the Agitated Wash
- Authors: Ahmad Darwish, Matteo Murdaca, Jami J. Kinnunen
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas
- Links: abs=https://arxiv.org/abs/2603.29650v1  pdf=https://arxiv.org/pdf/2603.29650v1.pdf

Abstract:
It is a universal empirical observation that socks become unpaired in the laundry. We propose a quasiparticle theory of sock dynamics in which individual socks are modelled as bosonic excitations of the agitated laundry condensate. The sock dispersion relation is material-dependent: nondispersive materials retain their shape, while dispersive materials give rise to the well-documented phenomenon of sock shrinkage. In the convex regions of the dispersive spectrum, socks undergo Beliaev decay and spontaneously split into two lower-momentum socks, while in the concave regions the dominant process is Landau-Khalatnikov scattering, which degrades socks into lint and loose threads. In addition, the rotating drum creates sock-antisock pairs from the laundry vacuum via the dynamical Casimir effect. The coexistence of these creation and destruction channels gives rise to a fundamental ambiguity: an unpaired sock at the end of a wash cycle is equally consistent with the destruction of its partner or the spontaneous creation of an entirely new sock.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29669v1
- Title: The Manipulate-and-Observe Attack on Quantum Key Distribution
- Authors: William Tighe, George Brumpton, Mark Carney, Benjamin T. H. Varcoe
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2603.29669v1  pdf=https://arxiv.org/pdf/2603.29669v1.pdf

Abstract:
Quantum key distribution is often regarded as an unconditionally secure method to exchange a secret key by harnessing fundamental aspects of quantum mechanics. Despite the robustness of key exchange, classical post-processing reveals vulnerabilities that an eavesdropper could target. In particular, many reconciliation protocols correct errors by comparing the parities of subsets between both parties. These communications occur over insecure channels, leaking information that an eavesdropper could exploit. Currently there is no holistic threat model that addresses how parity-leakage during reconciliation might be actively manipulated. In this paper we introduce a new form of attack, namely the Manipulate-and-Observe attack in which the adversary (1) partially intercepts a fraction $ρ$ of the qubits during key exchange, injecting the maximally tolerated amount of errors up to the 11 percent error threshold whilst remaining undetected and (2) probes the maximum amount of parity-leakage during reconciliation, and exploits it using a vectorised, parallel brute force filter to shrink the search space from 2n down to as few as a single candidate, for an n-bit reconciled key. We perform simulations of the attack, deploying it on the most widely used protocol, BB84, andthe benchmark reconciliation protocol, Cascade. Our simulation results demonstrate that the attack can significantly reduce the security below the theoretical bound and, in the worst case, fully recover the reconciled key material. The principles of the attack could threaten other parity-based reconciliation schemes, like Low Density Parity Check, which underscores the need for urgent consideration of the combined security of key exchange and post-processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29695v1
- Title: Probes of chaos over the Clifford group and approach to Haar values
- Authors: Stefano Cusumano, Gianluca Esposito, Alioscia Hamma
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29695v1  pdf=https://arxiv.org/pdf/2603.29695v1.pdf

Abstract:
Chaotic behavior of quantum systems can be characterized by the adherence of the expectation values of given probes to moments of the Haar distribution. In this work, we analyze the behavior of several probes of chaos using a technique known as Isospectral Twirling [1]. This consists in fixing the spectrum of the Hamiltonian and picking its eigenvectors at random. Here, we study the transition from stabilizer bases to random bases according to the Haar measure by T-doped random quantum circuits. We then compute the average value of the probes over ensembles of random spectra from Random Matrix Theory, the Gaussian Diagonal Ensemble and the Gaussian Unitary Ensemble, associated with non-chaotic and chaotic behavior respectively. We also study the behavior of such probes over the Toric Code Hamiltonian.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29737v1
- Title: Optimal Control of Spin Squeezing in 2D Finite-Range Interacting Systems
- Authors: Ang Li, Ling-Na Wu, Li You
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29737v1  pdf=https://arxiv.org/pdf/2603.29737v1.pdf

Abstract:
Spin squeezing serves as both a fundamental witness of quantum entanglement and a critical resource for quantum-enhanced metrology. While generating substantial spin squeezing in finite-range interacting systems remains challenging, such capability is important for advancing quantum technologies. In this work, we develop an optimal control strategy for achieving enhanced spin squeezing in a two-dimensional XX model with dipolar interactions. Leveraging rotor-spin-wave theory for periodic boundary conditions, we circumvent computational bottlenecks to explore control strategies at unprecedented scales. Remarkably, optimizing a single collective transverse field is sufficient to achieve substantial squeezing enhancement, exceeding the two-axis-twisting benchmark. The optimized control field achieves this breakthrough by dynamically suppressing inter-subspace mixing induced by the finite-range interactions, thereby confining the system evolution predominantly within the maximal spin subspace. We further extend rotor-spin-wave theory to open boundary conditions and incorporate dephasing noise, providing a scalable framework for realistic systems. Under these conditions, the optimized protocol remains effective, highlighting its robustness and suitability for experimental implementation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29754v1
- Title: Nonequilibrium energy transport in driven-dissipative quantum systems
- Authors: Junran Kong, Yuwei Lu, Huan Liu, Liwei Duan, Chen Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29754v1  pdf=https://arxiv.org/pdf/2603.29754v1.pdf

Abstract:
Nonequilibrium energy transport serves as one of fundamental problems in quantum thermodynamics and quantum technologies. Driven quantum master equation in the dressed picture provides an efficient way of investigating nonequilibrium energy flow in general driven-dissipative quantum systems, where the systems are simultaneously driven by the finite thermodynamic bias and coherent driving field. The validity and general applicability of driven quantum master equation is confirmed by comparing with Floquet master equation, by analyzing energy currents in generic spin and boson models. The additional driving phase reserved in system-reservoir interactions, will apparently modify microscopic energy exchange processes. The steady-state energy currents are dramatically enhanced, in particular near the resonant regimes. In contrast, the traditional dressed master equation yields distinct behaviors of the energy currents. We hope that the driven quantum master equation may provide an efficient utility for the control of quantum transport and thermodynamic performances in driven-dissipative nanodevices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29795v1
- Title: Topological sum rule for geometric phases of quantum gates
- Authors: Nadav Orion, Boris Rotstein, Nirron Miller, Eric Akkermans
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29795v1  pdf=https://arxiv.org/pdf/2603.29795v1.pdf

Abstract:
We establish a topological sum rule, $ν_U = \frac{1}{2π}\sum_nγ_n = 2mν_H$, connecting the geometric phases accumulated by a two-qubit system over a complete basis of initial states to the winding number $ν_H$ classifying its Hamiltonian. Implementations of the same gate from different topological classes must distribute these phases differently, making their distinction measurable through the Wootters concurrence. As a corollary, nontrivial topology is a necessary condition for entanglement: only Hamiltonians with access to $ν_H \neq 0$ can generate it.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29809v1
- Title: Certifying and learning local quantum Hamiltonians
- Authors: Andreas Bluhm, Matthias C. Caro, Francisco Escudero Gutiérrez, Junseo Lee, Aadil Oufkir, Cambyse Rouzé, Myeongjin Shin
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.DS
- Links: abs=https://arxiv.org/abs/2603.29809v1  pdf=https://arxiv.org/pdf/2603.29809v1.pdf

Abstract:
In this work, we study the problems of certifying and learning quantum $k$-local Hamiltonians, for a constant $k$. Our main contributions are as follows:   - Certification of Hamiltonians. We show that certifying a local Hamiltonian in normalized Frobenius norm via access to its time-evolution operator can be achieved with only $O(1/\varepsilon)$ evolution time. This is optimal, as it matches the Heisenberg-scaling lower bound of $Ω(1/\varepsilon)$. To our knowledge, this is the first optimal algorithm for testing a Hamiltonian property. A key ingredient in our analysis is the Bonami Hypercontractivity Lemma from Fourier analysis.   - Learning Gibbs states. We design an algorithm for learning Gibbs states of local Hamiltonians in trace norm that is sample-efficient in all relevant parameters. In contrast, previous approaches learned the underlying Hamiltonian (which implies learning the Gibbs state), and thus inevitably suffered from exponential sample complexity scaling in the inverse temperature.   - Certification of Gibbs states. We give an algorithm for certifying Gibbs states of local Hamiltonians in trace norm that is both sample and time-efficient in all relevant parameters, thereby solving a question posed by Anshu (Harvard Data Science Review, 2022).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29811v1
- Title: Floquet Codes from Derived Semi-Regular Hyperbolic Tessellations on Orientable and Non-Orientable Surfaces
- Authors: Douglas F. Copatti, Giuliano G. La Guardia, Waldir S. Soares, Edson D. Carvalho, Eduardo B. Silva
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2603.29811v1  pdf=https://arxiv.org/pdf/2603.29811v1.pdf

Abstract:
In this paper, we construct several new quantum Floquet codes on compact, orientable, as well as non-orientable surfaces. In order to obtain such codes, we identify these surfaces with hyperbolic polygons and examine hyperbolic semi-regular tessellations on such surfaces. The method of construction presented here generalizes similar constructions concerning hyperbolic Floquet codes on connected and compact surfaces with genus $g \geq 2$. A performance analysis and an investigation of the asymptotic behavior of these codes are also presented.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29857v1
- Title: Trotter Scars: Trotter Error Suppression in Quantum Simulation
- Authors: Bozhen Zhou, Qi Zhao, Pan Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29857v1  pdf=https://arxiv.org/pdf/2603.29857v1.pdf

Abstract:
Recent studies have shown that Trotter errors are highly initial-state dependent and that standard upper bounds often substantially overestimate them. However, the mechanism underlying anomalously small Trotter errors and a systematic route to identifying error-resilient states remain unclear. Using interaction-picture perturbation theory, we derive an analytical expression for the leading-order Trotter error in the eigenbasis of the Hamiltonian. Our analysis shows that initial states supported on spectrally commensurate energy ladders exhibit strongly suppressed error growth together with persistent Loschmidt revivals. We refer to such states as Trotter scars. To identify such states in practice, we further introduce a general variational framework for finding error-minimizing initial states for a given Hamiltonian. Applying this framework to several spin models, we find optimized states whose spectral support and dynamical behavior agree with the perturbative prediction. Our results reveal the spectral origin of Trotter-error resilience and provide a practical strategy for discovering error-resilient states in digital quantum simulation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29869v1
- Title: Weak-Field Expansion: A Time-Closed Solution of Quantum Three-Wave Mixing
- Authors: Hanzhong Zhang, Avi Pe'er
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29869v1  pdf=https://arxiv.org/pdf/2603.29869v1.pdf

Abstract:
We present a systematic derivation of the Heisenberg evolution of a trilinear bosonic Hamiltonian system in presence of a strong drive beyond the standard approximation of a classical, undepleted driving field. We employ a perturbative expansion of the Hamiltonian propagator in orders of the input field amplitudes, as opposed to the standard Baker-Campbell-Hausdorff (BCH) expansion of the propagator in orders of time. Our method automatically provides time-closed expressions; and converges considerably faster than BCH, especially in the regime of high parametric gain because the small parameter it uses is natural to the problem. We obtain the well-known quantum solution for optical parametric amplification of down-conversion simply as the first order of the expansion, and present the rigorous procedure to derive higher order corrections one by one. To demonstrate the utility of higher corrections, we discuss the 2nd order correction to the pump field as an ideal detector of time-energy entanglement in parametric down-conversion. We also use the 3rd order correction to calculate the limits on the fidelity of quantum state-transfer from one optical mode to another using sum/difference frequency generation, due to the quantum properties of the strong driving field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29894v1
- Title: LLM-Guided Evolutionary Search for Algebraic T-Count Optimization
- Authors: Daniil Fisher, Valentin Khrulkov, Mikhail Saygin, Ivan Oseledets, Stanislav Straupe
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29894v1  pdf=https://arxiv.org/pdf/2603.29894v1.pdf

Abstract:
Reducing the non-Clifford cost of fault-tolerant quantum circuits is a central challenge in quantum compilation, since T gates are typically far more expensive than Clifford operations in error-corrected architectures. For Clifford+T circuits, minimizing T-count remains a difficult combinatorial problem even for highly structured algebraic optimizers. We introduce VarTODD, a policy-parameterized variant of FastTODD in which the correctness-preserving algebraic transformations are left unchanged while candidate generation, pooling, and action selection are exposed as tunable heuristic components. This separates the quality of the algebraic rewrite system from the quality of the search policy. On standard arithmetic benchmarks, fixed hand-designed VarTODD policies already match or improve strong FastTODD baselines, including reductions from 147 to 139 for GF(2^9) and from 173 to 163 for GF(2^10) in the corresponding benchmark branches. As a proof of principle for automated tuning, we then optimize VarTODD policies with GigaEvo, an LLM-guided evolutionary framework, and obtain additional gains on harder instances, reaching 157 for GF(2^10) and 385 for GF(2^16). These results identify policy optimization as an independent and practical lever for improving algebraic T-count reduction, while LLM-guided evolution provides one viable way to exploit it.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29900v1
- Title: Dynamics of entanglement entropy for a locally monitored lattice gauge theory
- Authors: Nisa Ara, Arpan Bhattacharyya, Nilachal Chakrabarti, Neha Nirbhan, Indrakshi Raychowdhury
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29900v1  pdf=https://arxiv.org/pdf/2603.29900v1.pdf

Abstract:
The $1+1$ dimensional $Z_2$ gauge theory is the simplest model that allows for quantum computation or quantum simulation to probe the fundamental aspects of a gauge theory coupled with dynamical fermions. To reliably benchmark such a system, it is crucial to understand the non-unitary quantum dynamics arising from the underlying non-Hermitian evolution and to model the effects of quantum measurements. This work focuses on monitoring ultra-local physical observables for a $\mathbb Z_2$ gauge theory. Tensor network calculations are performed to dynamically probe entanglement entropy at larger lattice sizes. In this work, we report that continuously monitoring local and diagonal observables (electric and mass energy densities) in the computational basis demonstrates the absence of any measurement-induced phase transition, as indicated by the system-size independence of the late-time saturation value of the bipartite entanglement entropy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29944v1
- Title: Four Generations of Quantum Biomedical Sensors
- Authors: Xin Jin, Priyam Srivastava, Ronghe Wang, Yuqing Li, Jonathan Beaumariage, Tom Purdy, M. V. Gurudev Dutt, Kang Kim, et al.
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2603.29944v1  pdf=https://arxiv.org/pdf/2603.29944v1.pdf

Abstract:
Quantum sensing technologies offer transformative potential for ultra-sensitive biomedical sensing, yet their clinical translation remains constrained by classical noise limits and a reliance on macroscopic ensembles. We propose a unifying generational framework to organize the evolving landscape of quantum biosensors based on their utilization of quantum resources. First-generation devices utilize discrete energy levels for signal transduction but follow classical scaling laws. Second-generation sensors exploit quantum coherence to reach the standard quantum limit, while third-generation architectures leverage entanglement and spin squeezing to approach Heisenberg-limited precision. We further define an emerging fourth generation characterized by the end-to-end integration of quantum sensing with quantum learning and variational circuits, enabling adaptive inference directly within the quantum domain. By analyzing critical parameters such as bandwidth matching and sensor-tissue proximity, we identify key technological bottlenecks and propose a roadmap for transitioning from measuring physical observables to extracting structured biological information with quantum-enhanced intelligence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29971v1
- Title: High-fidelity entangled photon pairs from a quantum-dot-based single-photon source
- Authors: Malwina A. Marczak, Spencer J. Johnson, Mark R. Hogg, Timon L. Baltisberger, Nathan Arnold, Benjamin E. Nussbaum, Clotilde M. N. Pillot, Sascha R. Valentin, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29971v1  pdf=https://arxiv.org/pdf/2603.29971v1.pdf

Abstract:
Entangled photon pairs are a ubiquitous resource in quantum technologies, used in quantum key distribution and quantum networking as well as fundamental tests of non-locality. For scalable quantum networks, pairs that are indistinguishable in all unentangled degrees of freedom are essential, as they enable high-fidelity entanglement swapping across network nodes. To date the most-studied sources of "swappable" entangled photon pairs have been based on spontaneous parametric down-conversion (SPDC) in non-linear crystals. However, the probabilistic nature and unavoidable trade-off between brightness and unwanted multi-photon emission limits their performance in lossy channels. Here, we demonstrate a high-fidelity source of "swappable" entangled photon pairs using a semiconductor quantum dot (QD) coupled to a tunable microcavity. By actively modulating the QD emission between orthogonal polarisation states, delaying one path in a low-loss Herriott cell, and recombining the two on a balanced beam splitter, we generate entangled photon pairs with a fidelity of $96.1\pm0.5$ %. We identify and mitigate fidelity-limiting factors, achieving a maximum fidelity of $98.1\pm0.5$ % through time-resolved post-selection. The scheme suppresses residual multi-photon events concentrated near the excitation pulse and has only a modest impact on the rate. Furthermore, the photons are mutually indistinguishable, enabling efficient entanglement swapping. Our results establish semiconductor QDs as a viable platform for quantum network-compatible swappable entangled photon pair generation, with feasible entanglement generation rates exceeding 0.5 Gpairs/s.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29987v1
- Title: Strong converse bounds on the classical identification capacity of the qubit depolarizing channel
- Authors: Liuhang Ye, Bjarne Bergh, Nilanjana Datta
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.29987v1  pdf=https://arxiv.org/pdf/2603.29987v1.pdf

Abstract:
A strong converse bound for the classical identification capacity of a quantum channel is an upper bound on the asymptotic identification rate of classical messages sent through the channel, such that, above this rate, the probability of an identification error necessarily converges to one. Converse bounds for identification are notoriously difficult to obtain for fully quantum channels. The only previously known converse bound, due to Atif, Pradhan and Winter [Int.~J.~Quantum Inf.~22(5):2440013, 2024], has the unsatisfactory feature of remaining strictly positive even for a completely noisy channel, for which identification is clearly impossible. We derive strong (and hence also weak) converse bounds, for the qubit depolarizing channel with noise parameter $p$, that vanish as $p\to 1$, thereby yielding the correct behavior in the completely noisy limit. Moreover, in the setting of simultaneous classical identification under the constraint of complete product measurements, our converse bound matches the corresponding achievability bound, and establishes that in this case the identification capacity equals the classical capacity of the channel.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.30015v1
- Title: Noise Inference by Recycling Test Rounds in Verification Protocols
- Authors: Amit Saha, Harold Ollivier
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2603.30015v1  pdf=https://arxiv.org/pdf/2603.30015v1.pdf

Abstract:
Interactive verification protocols for quantum computations allow to build trust between a client and a service provider, ensuring the former that the instructed computation was carried out faithfully. They come in two variants, one without quantum communication that requires large overhead on the server side to coherently implement quantum-resistant cryptographic primitives, and one with quantum communication but with repetition as the only overhead on the service provider's side. Given the limited number of available qubits on current machines, only quantum communication-based protocols have yielded proof of concepts.   In this work, we show that the repetition overhead of protocols with quantum communication can be further mitigated if one examines the task of operating a quantum machine from the service provider's point of view. Indeed, we show that the test rounds data, whose collection is necessary to provide security, can indeed be recycled to perform continuous monitoring of noise model parameters for the service provider. This exemplifies the versatility of these protocols, whose template can serve multiple purposes and increases the interest in considering their early integration into development roadmaps of quantum machines.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.30023v1
- Title: LO-Free Phase and Amplitude Recovery of an RF Signal with a DC-Stark-Enabled Rydberg Receiver
- Authors: Vladislav Katkov, Nikola Zlatanov
- Categories: quant-ph (primary); quant-ph; cs.IT; eess.SP
- Links: abs=https://arxiv.org/abs/2603.30023v1  pdf=https://arxiv.org/pdf/2603.30023v1.pdf

Abstract:
We present a theoretical framework for recovering the amplitude and carrier phase of a single received RF field with a Rydberg-atom receiver, without injecting an RF local oscillator (LO) into the atoms. The key enabling mechanism is a static DC bias applied to the vapor cell: by Stark-mixing a near-degenerate Rydberg pair, the bias activates an otherwise absent upper optical pathway and closes a phase-sensitive loop within a receiver driven only by the standard probe/coupling pair and the received RF field. For a spatially uniform bias, we derive an effective four-level rotating-frame Hamiltonian of Floquet form and show that the periodic steady state obeys an exact harmonic phase law, so that the $n$th probe harmonic carries the factor $e^{inΦ_S}$. This yields direct estimators for the signal phase and amplitude from a demodulated probe harmonic, with amplitude recovery obtained by inverting an injective harmonic response map. In the high-SNR regime, we derive explicit RMSE laws and use them to identify distinct phase-optimal and amplitude-optimal bias-controlled mixing angles, together with a weighted joint-design criterion and a balanced compromise angle that equalizes the fractional phase and amplitude penalties. We then extend the analysis to nonuniform DC bias through quasistatic spatial averaging and show that bias inhomogeneity reduces coherent gain for phase readout while also reshaping the amplitude-response slope. Numerical examples validate the phase law, illustrate response-map inversion and mixing-angle trade-offs, and quantify the penalties induced by bias nonuniformity. The results establish a minimal route to coherent Rydberg reception of a single RF signal without an auxiliary RF LO in the atoms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2312.02597v2
- Title: Mitigating noise of residual electric fields for single Rydberg atoms with electron photodesorption
- Authors: Bahtiyar Mamat, Cheng Sheng, Xiaodong He, Jiayi Hou, Peng Xu, Kunpeng Wang, Jun Zhuang, Mingrui Wei, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2312.02597v2  pdf=https://arxiv.org/pdf/2312.02597v2.pdf

Abstract:
Rydberg atoms as versatile tools for quantum applications are extremely sensitive to electric fields. When utilizing these atoms, it becomes imperative to comprehensively characterize and mitigate any residual electric fields present in the environment. Particularly for single Rydberg atoms trapped in optical tweezers in a compact quartz vacuum cell, we have identified that a significant source of background electric fields originates from electrons bound to the cell surface. These electrons are generated by the 297-nm light used for single-photon Rydberg excitation. Furthermore, once the electrons are desorbed from the surface through exposure to ultraviolet light, the incoherent ground-Rydberg transition undergoes a transformation into coherent excitation, since the noise of residual electric fields are effectively mitigated. Our studies promote enhanced control and reliable performance of Rydberg atom-based systems, thereby paving the way for advancements in quantum information processing, the realization of high-fidelity quantum gates, and the development of precise quantum sensors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28820v1
- Title: A Schrödinger-like equation for the Thermodynamics of a particle in a box
- Authors: Adrian Faigon
- Categories: physics.class-ph (primary); physics.class-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28820v1  pdf=https://arxiv.org/pdf/2603.28820v1.pdf

Abstract:
The particle in an expanding/contracting 1-dimension box is revisited in action-angle like variables with direct thermodynamic interpretation. An angle dependent potential is proposed accurately describing the mechanical behavior while also capturing thermodynamic evolution -- entropy production -- within a canonical Hamiltonian framework. Heat transfer at constant volume is analyzed, and the derived thermal conductance matches the universal quantum of heat conductance $G_{Q}$ in the quantum limit. Having a Hamiltonian scheme interpretable in thermodynamic terms, a Schrödinger-like wave equation is formulated whose wavefunction solutions contain the information about the entropy evolution. The results show exact agreement with 'classical' results for non abrupt changes. Finally, comparisons with a pure quantum mechanical treatment of the wave function in an expanding box confirm consistency in quasi-static regimes and reveal adiabaticity breakdown under far-from-equilibrium conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28849v1
- Title: Symmetry-Fractionalized Skin Effects in Non-Hermitian Luttinger Liquids
- Authors: Christopher Ekman, Emil J. Bergholtz, Paolo Molignini
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28849v1  pdf=https://arxiv.org/pdf/2603.28849v1.pdf

Abstract:
In one dimension, strongly correlated gapless systems are highly constrained due to conformal invariance, leading to the decoupling of low energy degrees of freedom corresponding to different symmetry sectors. The most familiar example of this is spin-charge separation. Here, we extend this mechanism to the non-Hermitian realm by demonstrating that skin effects corresponding to different symmetry sectors exhibit an emergent decoupling. We establish this for $N$ flavor fermions and demonstrate it numerically for the special case of the Hubbard model, in which spin and charge skin effects separate at low energies. Finally, we construct an interaction-enabled $E_8$ skin effect with no free fermion counterpart.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28868v1
- Title: Higgs Boson Spookiness: Probing Quantum Nonlocality with Spacetime-Resolved $H\rightarrowτ^+τ^-$ Decays
- Authors: Lawrence Lee, John Lawless, Caroline Riggall
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28868v1  pdf=https://arxiv.org/pdf/2603.28868v1.pdf

Abstract:
We demonstrate that a future precision $ee$ Higgs factory would be able to perform a spacetime-resolved test of quantum nonlocality in Higgs boson decays. In simulated $ee\rightarrow ZH \rightarrow (μμ)(ττ)$ events at $\sqrt{s}=240$ GeV, we reconstruct $τ$ lepton decay vertices and measure spin correlations as a function of the spacetime interval between the two $τ$ decays. Such a measurement would be able to test Bell-inequality-violating correlations for spacelike-separated decays, enabling direct exclusion of superluminal, finite-speed entanglement signaling theories. With 0.75 ab$^{-1}$ of integrated luminosity, entanglement signal propagation speeds below $\approx2c$ can be excluded at 95$\%$ CL. Signals establishing any spin correlation can be excluded for speeds below $\approx9c$. This constitutes the first proposed spacetime-resolved measurement of electroweak quantum entanglement at a particle collider and demonstrates a unique capability of future Higgs factories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28893v1
- Title: Central Limit Theorems for Outcome Records in Disordered Quantum Trajectories
- Authors: Lubashan Pathirana
- Categories: math-ph (primary); math-ph; math.PR; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28893v1  pdf=https://arxiv.org/pdf/2603.28893v1.pdf

Abstract:
We prove annealed central limit theorems for finite pattern counts in the measurement record of discrete-time quantum trajectories generated by repeated measurements in a disordered environment. Under summable mixing assumptions on the environment and an annealed trace-norm forgetting property for the associated non-selective channel cocycle, we first establish the CLT under the annealed law determined by the dynamically stationary state. This part applies to general disordered quantum instruments and, in particular, is not restricted to the perfect-measurement regime; it complements both the corresponding law of large numbers for disordered measurement records and the homogeneous central limit theorem. We then introduce a coupling-based notion of admissibility for initial states and show that the same Gaussian limit extends to every admissible initial law, with unchanged centering and asymptotic variance. In the perfect-measurement setting, we further identify a general condition ensuring admissibility for every initial state, and hence obtain a universal annealed central limit theorem. We also provide practical sufficient criteria for this condition and verify the assumptions across a broad family of examples, including disordered walk-type models generated by finite group actions

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28975v1
- Title: Remarks on "Further comments on "Rebuttal of "Refutation of "Comment on "Reply to "Comments on "A genuinely natural information measure" " " " " " "
- Authors: Z. Sommer, A. Winter
- Categories: math-ph (primary); math-ph; cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28975v1  pdf=https://arxiv.org/pdf/2603.28975v1.pdf

Abstract:
It's a bit tedious, but as John Doe and Jean Roe have insisted on offering further comments on our comprehensive refutation of the former's already tiringly obstinate advances, we feel compelled to review their not even wrong opinions once again, hoping to put some sense back into the discourse.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28995v1
- Title: Hybrid Quantum-Classical AI for Industrial Defect Classification in Welding Images
- Authors: Akshaya Srinivasan, Xiaoyin Cheng, Jianming Yi, Alexander Geng, Desislava Ivanova, Andreas Weinmann, Ali Moghiseh
- Categories: cs.CV (primary); cs.CV; eess.IV; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28995v1  pdf=https://arxiv.org/pdf/2603.28995v1.pdf

Abstract:
Hybrid quantum-classical machine learning offers a promising direction for advancing automated quality control in industrial settings. In this study, we investigate two hybrid quantum-classical approaches for classifying defects in aluminium TIG welding images and benchmarking their performance against a conventional deep learning model. A convolutional neural network is used to extract compact and informative feature vectors from weld images, effectively reducing the higher-dimensional pixel space to a lower-dimensional feature space. Our first quantum approach encodes these features into quantum states using a parameterized quantum feature map composed of rotation and entangling gates. We compute a quantum kernel matrix from the inner products of these states, defining a linear system in a higher-dimensional Hilbert space corresponding to the support vector machine (SVM) optimization problem and solving it using a Variational Quantum Linear Solver (VQLS). We also examine the effect of the quantum kernel condition number on classification performance. In our second method, we apply angle encoding to the extracted features in a variational quantum circuit and use a classical optimizer for model training. Both quantum models are tested on binary and multiclass classification tasks and the performance is compared with the classical CNN model. Our results show that while the CNN model demonstrates robust performance, hybrid quantum-classical models perform competitively. This highlights the potential of hybrid quantum-classical approaches for near-term real-world applications in industrial defect detection and quality assurance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29028v1
- Title: The Contextual Modal Logic of a Wigner's Friend Generalization
- Authors: Felipe Dilho Alves, João Carlos Alves Barata
- Categories: math-ph (primary); math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29028v1  pdf=https://arxiv.org/pdf/2603.29028v1.pdf

Abstract:
Quantum mechanics has been subject to logical scrutiny since its inception. The behavior of quantum systems, which are fundamentally dissimilar from classical systems, often appears to point to a logical inconsistency in quantum mechanics, allegedly leading to contradictions in the prediction of experimental measurements--though such contradictions have never materialized. A recent example of this type of inquiry into the logical well-posedness of quantum mechanics is the Frauchiger-Renner Gedankenexperiment, which purports to demonstrate that quantum mechanics is logically inconsistent. In this article, we show that by considering the property of contextuality in quantum systems--as predicted by the Kochen-Specker theorem--the supposed contradiction proposed by Frauchiger and Renner becomes logically inaccessible.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29091v1
- Title: Ether of Orbifolds
- Authors: Henry Lamm
- Categories: hep-lat (primary); hep-lat; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29091v1  pdf=https://arxiv.org/pdf/2603.29091v1.pdf

Abstract:
Whose world is this? The orbifold lattice has been proposed as a bridge to practical quantum simulation of Yang--Mills theory, claiming exponential speedup over all known approaches. Through analytical derivations, Monte Carlo simulation, and explicit circuit construction, we identify compounding hidden costs entirely absent in Kogut--Susskind formulations: a mass-dependent Trotter overhead that scales as $m^4$, gauge-violating dynamics that grow as $m^2$ and worsen with penalty terms, and a mandatory mass extrapolation. Monte Carlo simulations of SU(3) establish a universal scaling: the continuum limit forces $m^2 \propto 1/a$, binding the Trotter step to the lattice spacing through a cost unique to orbifolds. For a fiducial $10^3$ calculation, the orbifold is $10^4$--$10^{10}$ times more expensive than every published alternative. The bridge is not built. The gap is the foundation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29132v1
- Title: Time-resolved role of coherence and delocalization in photosynthetic energy transfer from an extended exciton model
- Authors: Jingyu Liu, Tao-Yuan Du
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29132v1  pdf=https://arxiv.org/pdf/2603.29132v1.pdf

Abstract:
Photosynthetic antenna complexes achieve high quantum efficiency through exciton transport in coupled pigment networks. Conventional Frenkel-exciton models treat each chromophore as a structureless site and neglect internal electronic degrees of freedom that can influence coherence and delocalization. Here we develop an extended excitonic network model that preserves the pigment-pigment coupling topology while introducing tunable intrachromophoric electronic mixing within the single-excitation manifold. Using a Lindblad open-quantum-system framework, we quantify coherence, delocalization, and trapping efficiency across parameter space. We show that intrachromophoric mixing plays a time-dependent role: enhanced mixing on the antenna side promotes short-time coherent delocalization and improves excitation injection, whereas excessive mixing near the trapping site induces persistent delocalization and suppresses transfer efficiency. Simulated two-dimensional electronic spectra reveal enhanced cross peaks and systematic blue shifts, providing spectroscopic signatures of coherence-modulated transport. These results establish a microscopic connection between internal electronic structure and quantum transport performance in excitonic networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29188v1
- Title: Quantum Fisher information in many-photon states from shift current shot noise
- Authors: Evgenii Barts, Takahiro Morimoto, Naoto Nagaosa
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29188v1  pdf=https://arxiv.org/pdf/2603.29188v1.pdf

Abstract:
Quantum Fisher information (QFI) sets the ultimate precision of optical phase measurements and reveals multiphoton entanglement, but it is not accessible with conventional photodetection. We theoretically predict that a photodetector utilizing the shot noise of the quantum-geometric shift current of exciton polaritons can directly measure the QFI of nonclassical light. By solving the Lindblad equation, we obtain the time-dependent nonlinear photocurrent for an arbitrary initial photon state. It turns out that, regardless of the quantum state of the incident light, the integrated current depends only on the mean photon number. In stark contrast, the shot noise retains the quantum information: its Fano factor is proportional to the photon number variance and therefore encodes the QFI. Numerical calculations confirm these relations for illumination with optical Schrödinger cat and squeezed vacuum states. Quantum correlations in nonclassical light, usually hidden from direct detection, become observable in the form of shift current shot noise

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29201v1
- Title: A Floer Theoretic Approach to Energy Eigenstates on one Dimensional Configuration Spaces
- Authors: Kevin Ruck
- Categories: math.SG (primary); math.SG; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29201v1  pdf=https://arxiv.org/pdf/2603.29201v1.pdf

Abstract:
In this article we consider two classical problems in Quantum Mechanics, namely the 'particle on a ring' and the 'particle in a box' from the viewpoint of symplectic topology. Interpreting the solutions of the corresponding time independent Schrödinger equation as orbits in a suitably chosen time dependent Hamiltonian system allows us to investigate them using Floer theory. More precisely we extend the definition of Rabinowitz Floer homology to non-autonomous Hamiltonians on $\mathbb{R}^{2n}$ with its standard symplectic structure and show that compactness of the moduli space of J-holomorphic curves still holds. With this homology we are then able to prove existence results for energy $E$ eigenstates on the 'ring' or in the 'box' for a big range of exterior potentials.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29203v1
- Title: Generation of dipolar supersolids through a barrier sweep in droplet lattices
- Authors: E. L. Brakensiek, G. A. Bougas, S. I. Mistakidis
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29203v1  pdf=https://arxiv.org/pdf/2603.29203v1.pdf

Abstract:
We propose a dynamical protocol to generate supersolids in dipolar quantum gases by sweeping a repulsive Gaussian barrier through an incoherent quasi-one-dimensional droplet array. Supersolidity is inferred by monitoring the ensuing dynamics of the density, momentum distribution, center-of-mass motion, and superfluid fraction within the framework of the extended Gross-Pitaevskii equation with quantum corrections. A persistent superfluid background arises, atop which the crystals oscillate in unison, indicating the establishment of phase coherence. This process is accompanied by energy redistribution and the gradual transfer of higher-lying momenta toward the zero momentum mode. The dependence of the superfluid fraction on the barrier velocity and height is also elucidated evincing the parametric regions which facilitate the rise of a superfluid background. Our results pave the way for engineering supersolid generation using experimentally accessible protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29225v1
- Title: Pointwise and dynamic programming control synthesis for finite-level open quantum memory systems
- Authors: Igor G. Vladimirov, Ian R. Petersen, Guodong Shi
- Categories: math.OC (primary); math.OC; eess.SY; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29225v1  pdf=https://arxiv.org/pdf/2603.29225v1.pdf

Abstract:
This paper is concerned with finite-level quantum memory systems for retaining initial dynamic variables in the presence of external quantum noise. The system variables have an algebraic structure, similar to that of the Pauli matrices, and their Heisenberg picture evolution is governed by a quasilinear quantum stochastic differential equation. The latter involves a Hamiltonian whose parameters depend affinely on a classical control signal in the form of a deterministic function of time. The memory performance is quantified by a mean-square deviation of quantum system variables of interest from their initial conditions. We relate this functional to a matrix-valued state of an auxiliary classical control-affine dynamical system. This leads to a pointwise control design where the control signal minimises the time-derivative of the mean-square deviation with an additional quadratic penalty on the control. In an alternative finite-horizon setting with a terminal-integral cost functional, we apply dynamic programming and obtain a quadratically nonlinear Hamilton-Jacobi-Bellman equation, for which a solution is outlined in the form of a recursively computed asymptotic expansion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29230v1
- Title: Testing classical-quantum gravity with geodesic deviation
- Authors: Tomoya Hirotani, Akira Matsumura
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29230v1  pdf=https://arxiv.org/pdf/2603.29230v1.pdf

Abstract:
A novel semiclassical gravity model proposed by Oppenheim et al., that consistently describes interactions between quantum systems and a classical gravitational field, has recently attracted considerable attention. However, the limitations and phenomenological viability of this model have not yet been thoroughly investigated. In this work, based on the model, we study quantum fluctuations of geodesic deviation coupled with a classical gravitational field. We analytically derive the strain spectrum expected from the fluctuations and show that the original Oppenheim et al. model can be tested with the current observational sensitivity of gravitational-wave experiments. Furthermore, motivated by the novel semiclassical model, we construct two additional models: a modified Oppenheim et al. model that is manifestly consistent with Einstein equation, and a classical-quantum model with environment-induced noise. We analyze the strain spectra predicted by these two models through comparison with those of the original Oppenheim et al. model and perturbative quantum gravity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29266v1
- Title: Analyzing Uniform WKB for Deformed QM Or How Not to Quantize the SW Curve
- Authors: Dharmesh Jain
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29266v1  pdf=https://arxiv.org/pdf/2603.29266v1.pdf

Abstract:
We uncover an inconsistency in the uniform WKB quantization of deformed quantum mechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29287v1
- Title: Entanglement in the $θ$-vacuum
- Authors: Sebastian Grieninger, Dmitri E. Kharzeev, Eliana Marroquin
- Categories: hep-ph (primary); hep-ph; cond-mat.str-el; hep-lat; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29287v1  pdf=https://arxiv.org/pdf/2603.29287v1.pdf

Abstract:
We compute the entanglement entropy and the entanglement spectrum of the vacuum state in the massive Schwinger model at a finite $θ$ angle. The $θ$ term is implemented through a chirally rotated lattice Hamiltonian that preserves the periodicity in $θ$ already at the operator level and maintains the correct massless limit without $θ$-dependent lattice artifacts. We clarify the physical origin of entanglement entropy enhancement at $θ=π$ by relating it to the competition between distinct electric-flux vacuum branches. We show that the peak near $θ=π$ persists across the range of masses studied and corresponds to the point of maximal competition between distinct vacuum branches with opposite electric-field orientation, where quantum fluctuations due to fermion pair creation are maximized. While this entropy enhancement is generic, a pronounced narrowing of the entanglement gap occurs only near the critical mass ratio $m/g\simeq0.33$. Using the Bisognano--Wichmann (BW) theorem, we construct a lattice BW entanglement Hamiltonian and compare it with the exact modular Hamiltonian obtained from the reduced density matrix. We observe agreement between these Hamiltonians in the infrared sector, indicating that the entanglement Hamiltonian is well approximated by a spatially weighted microscopic Hamiltonian. These results establish entanglement observables as sensitive probes of the $θ$-dependent vacuum structure and highlight the chirally rotated formulation as a natural framework for open boundary conditions. Additionally, we discuss possible applications to entanglement in topological insulators and quantum wires.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29390v1
- Title: Nonlinear hydrodynamic response of a quantum Hall system
- Authors: Hiroki Isobe
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.str-el; physics.flu-dyn; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29390v1  pdf=https://arxiv.org/pdf/2603.29390v1.pdf

Abstract:
The quantum Hall effect realizes a quantized Hall resistance $R_{xy} = h/(νe^2)$ whereas the longitudinal resistance vanishes. The quantized value consists of the fundamental physical quantities, the elementary charge $e$ and the Planck constant $h$, along with an integer or fractional constant $ν$. High precision measurements of $R_{xy}$ allude to a linear relation between the applied current $I$ and the Hall voltage $V_\mathrm{H}$. Here, we argue that a nonlinear relation between $I$ and $V_\mathrm{H}$ could arise when the electric field is spatially inhomogeneous. We first discuss that the linear $I$-$V_\mathrm{H}$ relation holds with Galilean invariance. Then we consider a hydrodynamic description of a quantum Hall liquid to deal with an axially symmetric electric field. It reveals a nonlinear electronic response arising from the centrifugal force exerted on a curved flow and the density gradient invoked by vorticity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29509v1
- Title: Quantum Sensing with Triplet Pair States: A Theoretical Study
- Authors: Maria Grazia Concilio, Yiwen Wang, Siyuan Wang, Xueqian Kong
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29509v1  pdf=https://arxiv.org/pdf/2603.29509v1.pdf

Abstract:
Molecular quantum sensors represent a promising frontier for the detection of nuclear magnetic resonance signals and alternating current magnetic fields at the nanoscale, potentially reaching single-proton sensitivity. Although the triplet states of molecular pentacene provide a viable sensing architecture, the triplet pair states produced by singlet fission of pentacene dimers could enable more flexible quantum manipulations through entanglement. In this work, we model the quantum sensing efficacy of a spin-polarized quintet manifold in a photoexcited pentacene dimer generated via intramolecular singlet fission. Using a Lindblad master equation approach, we simulate the evolution of the triplet pair state under standard dynamical decoupling sequences, including spin echo, XY4, and XY8 and provide a direct performance comparison to the traditional pentacene monomer benchmark. While both architectures exhibit comparable sensitivity for isolated single-spin detection, our findings indicate that the dimer architecture provides a superior interaction cross-section for detecting small ensembles of nuclear spins. Analytical expressions derived for fluorescence modulation demonstrate that sensitivity is optimized in the low-magnetic field regime and scales with the number of pulses in the sensing protocol. This study establishes a theoretical baseline for utilizing high-spin multi-excitonic states as chemically tunable, high-sensitivity quantum probes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29568v1
- Title: Phase-space microscopes for quantum gases: Measuring conjugate variables and momentum-weighted densities
- Authors: N. R. Cooper, Y. Yang, C. Weitenberg
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29568v1  pdf=https://arxiv.org/pdf/2603.29568v1.pdf

Abstract:
Quantum gas microscopes offer unprecedented insights into quantum many-body states of cold atomic gases. Here we introduce concrete protocols for extending quantum gas microscopes to measure in phase space, by mapping momentum onto auxiliary degrees of freedom and using positive operator-valued measures. We distinguish between two distinct operational modes. In the Husimi-Q phase space microscope, position and momentum are jointly measured; in this mode the fundamental quantum noise appears in the position measurement. Conversely, the averaged-mode phase space microscope extracts the spatial dependence of averages of the momentum density (and its moments); these averages can be retrieved with arbitrary spatial resolution. We illustrate the utility of these techniques in diverse physical settings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29583v1
- Title: Double-weak-link interferometer of hard-core bosons in one dimension
- Authors: A. Takacs, J. Dubail, P. Calabrese
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29583v1  pdf=https://arxiv.org/pdf/2603.29583v1.pdf

Abstract:
We study the dynamics of a lattice hard-core boson gas released from a domain wall initial state in the presence of two weak links (defects). When the two defects are separated by a finite distance, the resulting density profile exhibits clear deviations from the standard Euler-scale hydrodynamic description of the gas, due to genuine quantum interference effects between the two defects. By analyzing the exact fermionic propagators, we show that repeated reflections at the defects give rise to interference fringes and coherent patterns that are beyond the reach of the (generalized) hydrodynamic description. We derive a closed analytic expression for the density profile during the expansion, explicitly highlighting the role played by these interference processes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29738v1
- Title: Phase diagram of rotating Bose-Einstein condensates trapped in power-law and hard-wall potentials
- Authors: G. M. Kavoulakis
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29738v1  pdf=https://arxiv.org/pdf/2603.29738v1.pdf

Abstract:
We investigate the rotational phase diagram of a quasi-two-dimensional, weakly-interacting Bose-Einstein condensate confined in power-law and in hard-wall trapping potentials. For weak interactions, the system undergoes discontinuous transitions between multiply-quantized vortex states as the rotation frequency of the trap increases. In contrast, stronger interactions induce continuous phase transitions toward mixed states involving both singly and multiply-quantized vortex states. A central result is the qualitative (and experimentally observable) difference between power-law and hard-wall confinement: In hard-wall traps, the leading instability always involves states with nonzero density at the trap center, whereas in power-law traps the density vanishes as the rotation frequency increases. The two different types of confinement give rise to scaling properties in the derived phase diagrams.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29750v1
- Title: A criterion for an effective discretization of a continuous Schrödinger spectrum using a pseudostate basis
- Authors: Tom Kirchner, Marko Horbatsch
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29750v1  pdf=https://arxiv.org/pdf/2603.29750v1.pdf

Abstract:
We consider a Hamiltonian $\hat H$ with a (partially) continuous spectrum and examine the zero-overlap condition which involves the projection onto exact continuum eigenstates of a set of pseudostates obtained from the diagonalization of $\hat H$ in a finite basis of square-integrable functions. For each projected pseudostate the condition implies the occurrence of zeros at all energies that correspond to the pseudo-continuum matrix eigenvalues, except for the eigenenergy associated with that pseudostate. This feature was observed for the Coulomb continuum represented in a Laguerre basis [M. McGovern et al., Phys. Rev. A 79, 042707 (2009)] and later explained using special properties of the Laguerre functions [I. B. Abdurakhmanov et al., J. Phys. B 44, 075204 (2011)]. We establish that a sufficient condition for the zero-overlap condition to occur is that the image space of the operator $\hat Q \hat H \hat P$, where $\hat P$ is the projection operator onto the subspace spanned by the basis and $\hat Q = \hat 1 - \hat P$ its complement, has dimension one. We show that the condition is met for the one-dimensional free-particle problem by a basis of harmonic oscillator eigenstates and for the Coulomb problem by a Laguerre basis, thus offering an alternative proof for the latter case. The zero-overlap condition ensures that in, e.g., an ionizing collision or laser-atom interaction process, transition probabilities obtained from the projection of a time-propagated pseudostate-expanded system wave function onto eigenstates of $ \hat H $ are asymptotically stable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29770v1
- Title: High-Order Perfect Absorption in the Absence of Exceptional Point
- Authors: Huisheng Xu, Luojia Wang, Luqi Yuan, Liang Jin
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29770v1  pdf=https://arxiv.org/pdf/2603.29770v1.pdf

Abstract:
High-order perfect absorption of coherent input has recently attracted significant attention due to its broadband absorption capacity. However, the realization of a high-order perfect absorber relies on the exceptional point (EP) to coalesce the scattering zeros. Here, we present a general scattering framework and achieve the high-order perfect absorber in the absence of EP. We consider the asynchronous coherent input, where a spatial delay introduces a momentum-dependent phase factor beyond the amplitude and phase control in synchronous coherent input. This new degree of freedom enables active control of the momentum dependent output, effectively reshaping the absorption line shape necessary for the high-order perfect absorber. Remarkably, despite the absence of EP, the proposed high-order perfect absorber exhibits significant response to the perturbations in the delay length. Our findings provide insights for the delay induced momentum-sensitive interference phenomenon and offer a new route for wave control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29776v1
- Title: Strongly Nonlinear Slow Light Polaritons in Subwavelength Modulated Waveguides
- Authors: Amir Rahmani, Maciej Dems, Michał Matuszewski
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29776v1  pdf=https://arxiv.org/pdf/2603.29776v1.pdf

Abstract:
Slow light is a regime of reduced group velocity, resulting in increased photon density in optical pulses and enhanced nonlinear effects. Here, we propose the realization of slow light in the regime of strong light-matter interaction between waveguide photons and semiconductor excitons. We design a dielectric superlattice structure with a nearly-flat band characterized by low group velocity and group velocity dispersion, both required for enhancing nonlinear effects with ultrashort pulses. Furthermore, by applying this general framework to a perovskite-based structure, we demonstrate an enhancement of the single-particle phase shift by a factor of more than 20, representing a significant step toward the few-photon quantum regime. Our results provide a blueprint for accessible strong interactions in solid-state integrated optics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.29821v1
- Title: Inverse Design of Strongly Localized Topological $π$ Modes in One-Dimensional Nonperiodic Systems
- Authors: Fumitatsu Iwase
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; quant-ph
- Links: abs=https://arxiv.org/abs/2603.29821v1  pdf=https://arxiv.org/pdf/2603.29821v1.pdf

Abstract:
This study investigates the spatial confinement of topological $π$-modes in one-dimensional chiral-symmetric systems. In conventional periodic and quasiperiodic structures, edge-mode wave functions inevitably penetrate the bulk. To suppress this, inverse design of a potential sequence is performed using a generative model under a global topological constraint. The generated sequence reveals a characteristic structure consisting of a topological boundary layer and a macroscopic S-dense domain, leading to enhanced confinement ($ξ=0.85$) while preserving topology. Based on the physical principle extracted from this result, a minimal heterostructure composed of only two S-blocks is manually constructed, which further reduces the localization length to $ξ=0.75$. These results provide a compact design principle for strongly localized topological states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.30039v1
- Title: The Grothendieck Constant is Strictly Larger than Davie-Reeds' Bound
- Authors: Chris Jones, Giulio Malavolta
- Categories: math.FA (primary); math.FA; quant-ph
- Links: abs=https://arxiv.org/abs/2603.30039v1  pdf=https://arxiv.org/pdf/2603.30039v1.pdf

Abstract:
The Grothendieck constant $K_{G}$ is a fundamental quantity in functional analysis, with important connections to quantum information, combinatorial optimization, and the geometry of Banach spaces. Despite decades of study, the value of $K_{G}$ is unknown. The best known lower bound on $K_{G}$ was obtained independently by Davie and Reeds in the 1980s. In this paper we show that their bound is not optimal. We prove that $K_{G} \ge K_{DR} + 10^{-12}$, where $K_{DR}$ denotes the Davie-Reeds lower bound.   Our argument is based on a perturbative analysis of the Davie-Reeds operator. We show that every near-extremizer for the Davie-Reeds problem has $Ω(1)$ weight on its degree-3 Hermite coefficients, and therefore introducing a small cubic perturbation increases the integrality gap of the operator.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2101.10821v2
- Title: Spin-Polarized Initialization and Readout for Single-Qubit State Tomography
- Authors: M. B. Sambú, L. Sanz, F. M. Souza
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2101.10821v2  pdf=https://arxiv.org/pdf/2101.10821v2.pdf

Abstract:
We propose a theoretical protocol for reconstructing the density matrix of a single-electron spin qubit using spin-polarized transport. The system consists of a quantum dot coupled to ferromagnetic reservoirs and subject to a magnetic field lying in the $xy$ plane of the Bloch sphere. Spin-dependent tunneling events measured along the $x\pm$, $y\pm$, and $z\pm$ quantization axes give rise to probability distributions that encode the quantum state of the qubit. The open-system dynamics are described using a Lindblad master equation, which captures the time evolution of the spin under continuous coupling to the reservoirs. By counting tunneling events for four different magnetic alignments, we formulate a scheme for reconstructing the full density matrix of the qubit. The resulting simulation data are analyzed using machine-learning techniques to process the measured probability distributions and infer the corresponding density matrix elements. The proposed model enables complete access to the open-system density matrix, including both population probabilities and relative phase information. Successful state reconstruction demonstrates the validity and robustness of the approach, highlighting its applicability to experimentally accessible spin-transport platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2403.09095v2
- Title: Exploring Hilbert-Space Fragmentation on a Superconducting Processor
- Authors: Yong-Yi Wang, Yun-Hao Shi, Zheng-Hang Sun, Chi-Tong Chen, Zheng-An Wang, Kui Zhao, Hao-Tian Liu, Wei-Guo Ma, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn; cond-mat.other; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2403.09095v2  pdf=https://arxiv.org/pdf/2403.09095v2.pdf

Abstract:
Isolated interacting quantum systems generally thermalize, yet there are several examples for the breakdown of ergodicity, such as many-body localization and quantum scars. Recently, ergodicity breaking has been observed in systems subjected to linear potentials, termed Stark many-body localization. This phenomenon is closely associated with Hilbert-space fragmentation, characterized by a strong dependence of dynamics on initial conditions. Here, we explore initial-state dependent dynamics using a ladder-type superconducting processor with up to 24 qubits, which enables precise control of the qubit frequency and initial state preparation. In systems with linear potentials, we experimentally observe distinct non-equilibrium dynamics for initial states with the same quantum numbers and energy, but with varying domain wall numbers. Accompanied by the numerical simulation for systems with larger sizes, we reveal that this distinction becomes increasingly pronounced as the system size grows, in contrast with weakly disordered interacting systems. Our results provide convincing experimental evidence of the fragmentation in Stark systems, enriching our understanding of the weak breakdown of ergodicity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2406.00717v2
- Title: Resource-theoretic hierarchy of contextuality for general probabilistic theories
- Authors: Lorenzo Catani, Thomas D. Galley, Tomáš Gonda
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2406.00717v2  pdf=https://arxiv.org/pdf/2406.00717v2.pdf

Abstract:
In this work we present a hierarchy of generalized contextuality. It refines the traditional binary distinction between contextual and noncontextual theories, and facilitates their comparison based on how contextual they are. Our approach focuses on the contextuality of prepare-and-measure scenarios, described by general probabilistic theories (GPTs). To motivate the hierarchy, we define it as the resource ordering of a novel resource theory of GPT-contextuality. The building blocks of its free operations are classical systems and univalent simulations between GPTs. These simulations preserve operational equivalences and thus cannot generate contextuality. Noncontextual theories can be recovered as least elements in the hierarchy. We then define a new contextuality monotone, called classical excess, given by the minimal error of embedding a GPT within an infinite classical system. In addition, we show that the optimal success probability in the parity oblivious multiplexing game also defines a monotone in our resource theory. Finally, we discuss whether the non-free operations can be understood as implementing information erasure and thus explaining the fine-tuning aspect of contextuality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2409.11020v2
- Title: Quantum simulation of wave optics in weakly inhomogeneous media using block-encoding
- Authors: Siavash Davani, Martin Gärttner, Falk Eilenberger
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2409.11020v2  pdf=https://arxiv.org/pdf/2409.11020v2.pdf

Abstract:
We propose a quantum algorithm that simulates the propagation of a light field through a weakly inhomogeneous medium. The wave equation in the paraxial approximation in inhomogeneous material takes the form of the Schrödinger equation with a time-dependent Hamiltonian. This reduction is used to simulate wave optical dynamics on a quantum computer. Beam propagator operators for a short propagation distance are constructed using an efficient and flexible block-encoding that enables the simulation of various optical setups. The algorithm is showcased by simulating the propagation of a 1D Gaussian beam through a lens with a finite thickness, and the resulting spherical aberrations are demonstrated.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2410.07275v2
- Title: Power-law distributions in nonequilibrium open quantum systems
- Authors: Wai-Keong Mok
- Categories: quant-ph (primary); quant-ph; nlin.AO; physics.optics
- Links: abs=https://arxiv.org/abs/2410.07275v2  pdf=https://arxiv.org/pdf/2410.07275v2.pdf

Abstract:
Power-law probability distributions are widely used to model extreme statistical events in complex systems, with applications to a vast array of natural phenomena ranging from earthquakes to stock market crashes to pandemics. We show that analogous heavy tails arise naturally in open quantum systems with nonlinear dissipation. Introducing a prototypical family of quantum dynamical models, we analytically prove the emergence of power-law tails in the steady state energy distribution, originating from an amplification of quantum noise whose microscopic fluctuations grow with energy. Moreover, our analysis suggests a general mechanism for heavy-tail statistics in the nonequilibrium steady states of open quantum systems: Nonlinear dissipation generically induces multiplicative quantum noise, enforced by the constraints of quantum mechanics, which is responsible for the heavy-tail behavior. This is supported by numerical simulations of a general class of nonlinear dynamics known as quantum Liénard systems. Remarkably, even when the corresponding classical system is stable, we find power-law tails in both steady-state populations and coherences, which occur for typical parameters without fine-tuning. This phenomenon can potentially be harnessed to develop extreme photon sources for novel applications in light-matter interaction and sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2411.03680v2
- Title: A Hierarchy of Spectral Gap Certificates for Frustration-Free Spin Systems
- Authors: Kshiti Sneh Rai, Ilya Kull, Patrick Emonts, Jordi Tura, Norbert Schuch, Flavio Baccari
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2411.03680v2  pdf=https://arxiv.org/pdf/2411.03680v2.pdf

Abstract:
Estimating spectral gaps of quantum many-body Hamiltonians is a highly challenging computational task, even under assumptions of locality and translation-invariance. Yet, the quest for rigorous gap certificates is motivated by their broad applicability, ranging from many-body physics to quantum computing and classical sampling techniques. Here we present a general method for obtaining lower bounds on the spectral gap of frustration-free quantum Hamiltonians in the thermodynamic limit. We formulate the gap certification problem as a hierarchy of optimization problems (semidefinite programs) in which the certificate -- a proof of a lower bound on the gap -- is improved with increasing levels. Our approach encompasses existing finite-size methods, such as Knabe's bound and its subsequent improvements, as those appear as particular possible solutions in our optimization, which is thus guaranteed to either match or surpass them. We demonstrate the power of the method on one-dimensional spin-chain models where we observe an improvement by several orders of magnitude over existing finite size criteria in both the accuracy of the lower bound on the gap, as well as the range of parameters in which a gap is detected.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2501.09374v2
- Title: Efficient measure of information backflow with a quasistochastic process
- Authors: Kelvin Onggadinata, Teck Seng Koh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2501.09374v2  pdf=https://arxiv.org/pdf/2501.09374v2.pdf

Abstract:
Characterization and quantification of non-Markovian dynamics in open quantum systems are topical issues in the rapidly developing field of quantum computation and quantum communication. A standard approach based on the notion of information backflow detects the flow of information from the environment back to the system. Numerous measures of information backflow have been proposed using different definitions of distinguishability between pairs of quantum states. These measures, however, necessitate optimization over the state space, which can be analytically challenging or numerically demanding. Here we propose an alternative witness and measure of information backflow that is explicitly state independent by utilizing the concept of quasiprobability representation and recent advances in the theory of majorization for quasiprobabilities. We illustrate its use over several paradigmatic examples, demonstrating consistent Markovian conditions with known results and also reported necessary and sufficient conditions for the qutrit system in a random unitary channel. The paper concludes with a discussion of the foundational implications of quantum dynamical evolution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2502.01005v4
- Title: Solid neon as a noise-resilient host for electron qubits above 100 mK
- Authors: Xinhao Li, Christopher S. Wang, Brennan Dizdar, Yizhong Huang, Yutian Wen, Wei Guo, Xufeng Zhang, Xu Han, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2502.01005v4  pdf=https://arxiv.org/pdf/2502.01005v4.pdf

Abstract:
Solid neon can be used as a solid host for single-electron qubits, and at temperatures of around 10 mK, electron-on-solid-neon charge qubits exhibit long coherence times and high operation fidelities. However, systematic characterization of the noise features of such systems is needed for the development of scalable quantum information architectures. Here, we show that solid neon can be used as a noise-resilient host for electron qubits above 100 mK. We examine the resilience of solid neon against charge and thermal noise when electron-on-solid-neon charge qubits are operated away from the charge-insensitive sweet spot and at elevated temperatures. We show that the extracted high-frequency charge noise density of electron-on-solid-neon qubits, projected as voltage fluctuations on nearby electrodes, is between $10^{-4}$ and $10^{-6}~\mathrm{μV^2/Hz}$ at 0.01 to 1 MHz, which is comparable with common semiconductor hosts. We also show that the electron-on-solid-neon charge qubits operating around 5 GHz frequencies can maintain echo coherence times of over 1 $μ$s at temperatures up to 400 mK.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2503.14894v3
- Title: Logical entanglement distribution between distant 2D array qubits
- Authors: Yuya Maeda, Yasunari Suzuki, Toshiki Kobayashi, Takashi Yamamoto, Yuuki Tokunaga, Keisuke Fujii
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.14894v3  pdf=https://arxiv.org/pdf/2503.14894v3.pdf

Abstract:
Sharing logical entangled pairs between distant quantum nodes is a key process to achieve fault tolerant quantum computation and communication. However, there is a gap between current experimental specifications and theoretical requirements for sharing logical entangled states while improving experimental techniques. Here, we propose an efficient logical entanglement distribution protocol based on surface codes for two distant 2D qubit array with nearest-neighbor interaction. A notable feature of our protocol is that it allows post-selection according to error estimations, which provides the tunability between the infidelity of logical entanglements and the success probability of the protocol. With this feature, the fidelity of encoded logical entangled states can be improved by sacrificing success rates. We numerically evaluated the performance of our protocol and the trade-off relationship, and found that our protocol enables us to prepare logical entangled states while improving fidelity in feasible experimental parameters. We also discuss a possible physical implementation using neutral atom arrays to show the feasibility of our protocol.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2503.23738v5
- Title: Coherent manipulation of interacting electron qubitson solid neon
- Authors: Xinhao Li, Yizhong Huang, Xu Han, Xianjing Zhou, Amir Yacoby, Dafei Jin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.23738v5  pdf=https://arxiv.org/pdf/2503.23738v5.pdf

Abstract:
Electrons trapped on solid neon surfaces serve as low-noise charge qubits with long coherence times and high operational fidelities. Such charge qubits offer full electrical control and compact device footprints, convenient for scaling up with quantum circuits. Realizing two-qubit gates on this platform is a critical step towards practical quantum information processing. In this work, we report the first experimental demonstration of coherent manipulation of multiple interacting electron-on-solid-neon (eNe) charge qubits. By exploiting the electrons naturally confined in close proximity by the surface structures of solid neon, we have achieved a direct qubit-qubit coupling strength of up to 62.5 MHz, as well as implemented cross-resonance (CR) and bSWAP two-qubit gates using global microwave drives. The natural electron confinement by solid neon mitigates the high-density-wiring challenge, simplifies the multi-qubit control, and establishes a unique path to scale up the eNe qubit platform.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2506.18802v2
- Title: Trans-dimensional Hamiltonian model selection and parameter estimation from sparse, noisy data
- Authors: Abigail N. Poteshman, Jiwon Yun, Tim H. Taminiau, Giulia Galli
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.18802v2  pdf=https://arxiv.org/pdf/2506.18802v2.pdf

Abstract:
High-throughput characterization often requires estimating parameters and model dimension from experimental data of limited quantity and quality. Such data may result in an ill-posed inverse problem, where multiple sets of parameters and model dimensions are consistent with available data. This ill-posed regime may render traditional machine learning and deterministic methods unreliable or intractable, particularly in high-dimensional, nonlinear, and mixed continuous and discrete parameter spaces. To address these challenges, we present a Bayesian framework that hybridizes several Markov chain Monte Carlo (MCMC) sampling techniques to estimate both parameters and model dimension from sparse, noisy data. By integrating sampling for mixed continuous and discrete parameter spaces, reversible-jump MCMC to estimate model dimension, and parallel tempering to accelerate exploration of complex posteriors, our approach enables principled parameter estimation and model selection in data-limited regimes. We apply our framework to a specific ill-posed problem in quantum information science: recovering the locations and hyperfine couplings of nuclear spins surrounding a spin-defect in a semiconductor from sparse, noisy coherence data. We show that a hybridized MCMC method can recover meaningful posterior distributions over physical parameters using an order of magnitude less data than existing approaches, and we validate our results on experimental measurements. More generally, our work provides a flexible, extensible strategy for solving a broad class of ill-posed inverse problems under realistic experimental constraints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2507.13862v2
- Title: Role of quantum state texture in probing resource theories and quantum phase transition
- Authors: Ayan Patra, Tanoy Kanti Konar, Pritam Halder, Aditi Sen De
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2507.13862v2  pdf=https://arxiv.org/pdf/2507.13862v2.pdf

Abstract:
Building on the recently developed quantum state texture resource theory, we exhibit that the difference between maximum and minimum textures is a valid purity monotone in any dimension and provide a lower bound for existing purity measures. We introduce a texture-based resource monotone applicable across general convex resource theories, encompassing quantum coherence, non-stabilizerness, and entanglement. In particular, we propose the notion of non-local texture, which corresponds to the geometric measure of bipartite and multipartite entanglement in pure states. Furthermore, we demonstrate that the texture of the entire ground state or its subsystems can effectively signal quantum phase transitions in the Ising chain under both transverse and longitudinal magnetic fields, offering a powerful tool for characterizing quantum criticality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2508.17053v2
- Title: Quantum Speed Limits For Open System Dynamics Based On A Representation-Basis-Dependent $\boldsymbol{\ell^{p}_{w}}$-Seminorm
- Authors: H. F. Chau, Jinjie Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.17053v2  pdf=https://arxiv.org/pdf/2508.17053v2.pdf

Abstract:
We report a family of quantum speed limits (QSLs) that give evolution time lower bounds between an initial and a final state whose separation is described by a certain representation basis dependent norm derived from the weighted $\ell^{p}_{w}$-seminorm. These QSLs are applicable to open, closed, time-dependent, or time-independent systems in finite-dimensional Hilbert spaces whose density matrices are piecewise time differentiable. They can be extended to systems over separable Hilbert spaces as well. Crucially, these QSLs are valid for arbitrary operators, not just density matrices, provided that a modest technical condition is fulfilled. When compared to the existing QSLs applied to pure state time-independent Hamiltonian evolution, qubit spontaneous emission, high-fidelity gate implementation, coherent state photon loss and operator coherence or dephasing, ours consistently show improved sharpness in most cases, along with greater universality and still retaining computational efficiency.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2509.18925v2
- Title: Diffusive Stochastic Master Equation (SME) with dispersive qubit/cavity coupling
- Authors: Pierre Rouchon
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2509.18925v2  pdf=https://arxiv.org/pdf/2509.18925v2.pdf

Abstract:
A detailed analysis of the quantum diffusive Stochastic Master Equation (SME) for qubit/cavity systems with dispersive coupling is provided. This analysis incorporates classical input signals and output signals (measurement outcomes through homodyne/heterodyne detection). The dynamics of the qubit/cavity density operator is shown to converge exponentially towards a slow invariant manifold. This invariant manifold is parameterized by the density operator of a fictitious qubit governed by a quantum SME incorporating the classical input/output signals preserving complete-positivity and trace. The reduced cavity (resp. qubit) operator obtained by partial trace of the qubit (resp. cavity) is then given by a time-varying deterministic quantum channel from the density operator of this fictitious qubit. This formulation avoids non-Markovian descriptions where negative dephasing rates and detection efficiency exceeding temporary one are present in several publications. Extensions are considered where the qubit is replaced by any qudit dispersively coupled to an arbitrary set of cavity modes with collective input/output classical signals.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2509.25861v2
- Title: Coherence restoring in communication line via controlled interaction with environment
- Authors: E. B. Fel'dman, I. D. Lazarev, A. N. Pechen, A. I. Zenchuk
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.25861v2  pdf=https://arxiv.org/pdf/2509.25861v2.pdf

Abstract:
We consider the state-restoring protocol based on the controlled interaction of a linear chain with environment through { incoherent control by} the specially adjusted step-wise time dependent Lindblad operators. We show that the best restoring result (maximal scale factors in the restored state) corresponds to the symmetrical Lindblad equation. (0,1)-excitation dynamics is considered numerically, and restoring protocol for the 1-order coherence matrix is proposed for the case of the two-qubit sender (receiver). The state-restoring with equal scale factors is also considered reflecting the uniform scaling of the restored information

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2510.13360v2
- Title: Efficient lambda-enhanced gray molasses using an EIT-based laser locking scheme
- Authors: Timothy Leese, Siobhan Patrick, Silvia Bergamini, Calum MacCormick
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2510.13360v2  pdf=https://arxiv.org/pdf/2510.13360v2.pdf

Abstract:
We present a novel implementation of lambda-enhanced gray molasses cooling in a non-standard beam geometry and with an inexpensive laser locking set-up. In contrast to the established use of resource-intensive phase locking methods, our laser system uses two independent lasers, frequency -locked to a spectral feature produced by an electromagnetically induced transparency (EIT) resonance. We show that this approach achieves sufficient coherence to enable effective gray molasses cooling without the need for costly GHz electronics, significantly reducing the complexity and cost of experimental setups and represents a step toward more accessible cold atom technologies. A wave-function Monte Carlo analysis supports the experimental findings, offering insight into the cooling dynamics of this unconventional scheme

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2510.13577v2
- Title: Noise-stabilized discrete time crystals on digital quantum processors
- Authors: Kazuya Shinjo, Kazuhiro Seki, Seiji Yunoki
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2510.13577v2  pdf=https://arxiv.org/pdf/2510.13577v2.pdf

Abstract:
Floquet many-body phases such as discrete time crystals (DTCs) are typically fragile to imperfections, and stabilizing them on noisy quantum hardware remains a central challenge in nonequilibrium quantum physics. Here, we use IBM Eagle and Heron superconducting processors to implement Floquet dynamics of a kicked Ising model on two-dimensional Kagome lattices, engineered via ancilla-assisted embeddings into the heavy-hex connectivity of the devices. By combining error-mitigated measurements on quantum hardware with matrix-product-state simulations incorporating an ancilla-noise model constructed from experimental device data, we observe long-lived subharmonic magnetization oscillations that are stabilized -- rather than destroyed -- by structured quantum noise. Across different two-dimensional lattice geometries, increasing cases beyond Kagome lattices, and with or without boundary symmetry-charge pumping, ancilla errors effectively act as spatiotemporal disorder that induces stochastic sign flips of the Ising couplings, providing a unified mechanism for robust period-doubling responses. When symmetry-charge pumping is present, intrinsic boundary-localized $π$ modes cooperate with this disorder to yield a boundary-assisted DTC characterized by suppressed scrambling and sharply localized dynamics. In contrast, in implementations without pumping, the noiseless dynamics rapidly thermalize and exhibit no subharmonic order, whereas the same noise process alone generates a DTC-like long-lived subharmonic response over experimentally accessible time windows. These results identify engineered ancilla noise as a practical control knob for inducing, stabilizing, and geometrically tailoring nonequilibrium dynamical order on scalable superconducting quantum processors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2510.24713v3
- Title: Distinct Types of Parent Hamiltonians for Quantum States: Insights from the $W$ State as a Quantum Many-Body Scar
- Authors: Lei Gioia, Sanjay Moudgalya, Olexei I. Motrunich
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; math-ph
- Links: abs=https://arxiv.org/abs/2510.24713v3  pdf=https://arxiv.org/pdf/2510.24713v3.pdf

Abstract:
The construction of parent Hamiltonians that possess a given state as their ground state is a well-studied problem. In this work, we generalize this notion by considering simple quantum states and examining the local Hamiltonians that have these states as exact eigenstates. These states often correspond to Quantum Many-Body Scars (QMBS) of their respective parent Hamiltonians. Motivated by earlier works on Hamiltonians with QMBS, in this work we formalize the differences between three distinct types of parent Hamiltonians, which differ in their decompositions into strictly local terms with the same eigenstates. We illustrate this classification using the $W$ state as the primary example, for which we rigorously derive the complete set of local parent Hamiltonians, which also allows us to establish general results such as the existence of asymptotic QMBS, and distinct dynamical signatures associated with the different parent Hamiltonian types. Finally, we derive more general results on the parent Hamiltonian types that allow us to obtain some immediate results for simple quantum states such as product states, where only a single type exists, and for short-range-entangled states, for which we identify constraints on the admissible types. Altogether, our work opens the door to classifying the rich structures and dynamical properties of parent Hamiltonians that arise from the interplay between locality and QMBS.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2511.14621v2
- Title: Measuring Reactive-Load Impedance with Transmission-Line Resonators Beyond the Perturbative Limit
- Authors: Xuanjing Chu, Jinho Park, Jesse Balgley, Sean Clemons, Ted S. Chung, Kenji Watanabe, Takashi Taniguchi, Leonardo Ranzani, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con; physics.app-ph
- Links: abs=https://arxiv.org/abs/2511.14621v2  pdf=https://arxiv.org/pdf/2511.14621v2.pdf

Abstract:
We develop an analytic framework to extract circuit parameters and loss tangent from superconducting transmission-line resonators terminated by reactive loads, extending analysis beyond the perturbative regime. The formulation yields closed-form relations between resonant frequency, participation ratio, and internal quality factor, removing the need for full-wave simulations. We validate the framework through circuit simulations, finite-element modeling, and experimental measurements of van der Waals parallel-plate capacitors, using it to extract the dielectric constant and loss tangent of hexagonal boron nitride. Statistical analysis across multiple reference resonators, together with multimode self-calibration, demonstrates consistent and reproducible extraction of both capacitance and loss tangent in close agreement with literature values. In addition to parameter extraction, the analytic relations provide practical design guidelines for maximizing energy participation ratio in the load and improving the precision of resonator-based material metrology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2512.08433v2
- Title: Benchmarking Gaussian and non-Gaussian input states with a hybrid sampling platform
- Authors: Michael Stefszky, Kai-Hong Luo, Jan-Lucas Eickmann, Simone Atzeni, Florian Lütkewitte, Cheeranjiv Pandey, Fabian Schlue, Jonas Lammers, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.08433v2  pdf=https://arxiv.org/pdf/2512.08433v2.pdf

Abstract:
The original boson sampling paradigm-consisting of multiple single-photon input states, a large interferometer, and multi-channel click detection-was originally proposed as a photonic route to quantum computational advantage. Its non-Gaussian resources, essential for outperforming any classical system, are provided by single-photon inputs and click detection. Yet the drive toward larger experiments has led to the replacement of experimentally demanding single-photon sources with Gaussian states, thereby diminishing the available non-Gaussianity-a critical quantum resource. As the community broadens its focus from the initial sampling task to possible real-world applications, it becomes crucial to quantify the performance cost associated with reducing non-Gaussian resources and to benchmark sampling platforms that employ different input states.   To address this need, we introduce the Paderborn Quantum Sampler (PaQS), a hybrid platform capable of performing sampling experiments with eight Gaussian or non-Gaussian input states in a 12-mode interferometer within a single experimental run. This architecture enables direct, side-by-side benchmarking of distinct sampling regimes under otherwise identical conditions. By employing a semi-device-independent framework, offering certification that does not rely on prior knowledge of the interferometer or the input states, we verify that the observed data cannot be reproduced by any classical model-a prerequisite for demonstrating quantum advantage. Applying this framework, we observe clear performance gains arising from non-Gaussian input states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2512.22380v2
- Title: Creating multicomponent Schrödinger cat states in a coupled qubit-oscillator system
- Authors: Pavel Stránský, Pavel Cejnar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.22380v2  pdf=https://arxiv.org/pdf/2512.22380v2.pdf

Abstract:
We present a method for preparing various exotic modifications of Schr{ö}dinger cat states by coupling a semiclassical oscillator to a system of qubits. Varying the number of qubits and parameters of the protocol (involving quantum quench of the coupled system and a subsequent spin measurement), we bring the oscillator into a coherent superposition composed of an arbitrary number of wavepackets in tunable proportions and motion relations. The method can be implemented with the aid of current experimental techniques and may find applications in quantum information and sensing protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2601.03119v3
- Title: Collective dynamics versus entanglement in quantum battery performance
- Authors: Rohit Kumar Shukla, Sunil K. Mishra, Ujjwal Sen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.03119v3  pdf=https://arxiv.org/pdf/2601.03119v3.pdf

Abstract:
Identifying the origin of enhanced charging performance in many-body quantum batteries remains a central challenge in quantum thermodynamics. It is unclear whether improvements in stored energy and instantaneous charging power stem from genuinely quantum correlations, such as entanglement, or from coherent collective dynamics, in which energy is transferred through the battery by many particles acting together in a coordinated, phase-preserving manner. Here, we address this question by comparing the time evolution of energy and a hierarchy of entanglement measures probing bipartite, tripartite, and multipartite correlations. Across diverse battery charger configurations, the instantaneous power peaks early, before significant entanglement develops, indicating that peak charging is dominated by coherent collective transport. Further analysis of k-local interactions under fair constraints shows that only fully collective schemes (k = N ) engage all particles, aligning entanglement growth with energy storage and yielding a genuine enhancement. Partially extended interactions leave many particles inactive and fail to improve performance. Our analysis indicates that the charging advantage arises not from entanglement alone, but from correlations that coherently involve the entire system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.23892v2
- Title: Efficient Preparation of Graph States using the Quotient-Augmented Strong Split Tree
- Authors: Nicholas Connolly, Shin Nishio, Dan E. Browne, William John Munro, Kae Nemoto
- Categories: quant-ph (primary); quant-ph; cs.DM; math.CO
- Links: abs=https://arxiv.org/abs/2603.23892v2  pdf=https://arxiv.org/pdf/2603.23892v2.pdf

Abstract:
Graph states are a key resource for measurement-based quantum computation and quantum networking, but state-preparation costs limit their practical use. Graph states related by local complement (LC) operations are equivalent up to single-qubit Clifford gates; one may reduce entangling resources by preparing a favorable LC-equivalent representative. However, exhaustive optimization over the LC orbit is not scalable. We address this problem using the split decomposition and its quotient-augmented strong split tree (QASST). For several families of distance-hereditary (DH) graphs, we use the QASST to characterize LC orbits and identify representatives with reduced controlled-Z count or preparation circuit depth. We also introduce a split-fuse construction for arbitrary DH graph states, achieving linear scaling with respect to entangling gates, time steps, and auxiliary qubits. Beyond the DH setting, we discuss a generalized divide-and-conquer split-fuse strategy and a simple greedy heuristic for generic graphs based on triangle enumeration. Together, these methods outperform direct implementations on sufficiently large graphs, providing a scalable alternative to brute-force optimization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.27776v2
- Title: Benchmarking simulation of hybrid decoding scheme for parity-encoded spin systems
- Authors: Yoshihiro Nambu
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2603.27776v2  pdf=https://arxiv.org/pdf/2603.27776v2.pdf

Abstract:
This paper presents classical benchmark simulations of a practical hybrid decoding scheme for parity-encoded spin systems, which is well-suited to the development of quantum annealing devices based on on-chip superconducting technology. We compared the performance of finding the optimal solution using two embedding schemes for emulating all-to-all connectivity from local interactions: the SLHZ scheme, proposed by Sourlas, Lechner, Hauke, and Zoller, and the commonly used minor embedding (ME) scheme. We found that the SLHZ scheme is more efficient than the ME scheme when combined with postreadout classical decoding based on the classical bit-flipping algorithm, although the SLHZ scheme itself is substantially less efficient than the ME scheme.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28277v2
- Title: Genuine and Non-Genuine Quantum Non-Markovianity: A Unified Information-Theoretic Review
- Authors: Rajeev Gangwar, Ujjwal Sen
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2603.28277v2  pdf=https://arxiv.org/pdf/2603.28277v2.pdf

Abstract:
Understanding whether the features of open quantum dynamics are genuinely quantum remains a central challenge in quantum dynamics. Even though the non-Markovian behavior of quantum dynamics has been widely investigated across different settings, there is still no consensus on which properties of a dynamics reflect genuine quantum features and which arise from classical or non-genuine quantum sources. In this review, we provide detailed information on recent developments in characterizing quantum non-Markovianity based on information backflow and the nature of its origin. We also present a survey on how various approaches separate classical and quantum contributions, as well as how they define operational tasks that reveal genuine quantum non-Markovianity. We analyze several frameworks, including state-distinguishability -based, channel-based (``CP-divisibility''), and process-tensor methods. For each framework, we outline the underlying physical motivation, the criteria proposed to distinguish genuine quantum non-Markovianity from practical or apparent memory effects. We further compare different approaches and their strengths and limitations. The review aims to clarify the conceptual and operational aspects of quantum non-Markovian processes based on their nature and to provide a foundation for future research on quantum non-Markovianity and its role in advancing quantum information science and technology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28413v2
- Title: Resource-efficient quantum approximate optimization algorithm via Bayesian optimization and maximum-probability evaluation
- Authors: Siran Zhang, Shuming Cheng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2603.28413v2  pdf=https://arxiv.org/pdf/2603.28413v2.pdf

Abstract:
The quantum approximate optimization algorithm (QAOA) is a leading variational approach to combinatorial optimization, but its practical performance depends strongly on objective design, parameter search, and shot allocation. We present a resource-efficient QAOA framework that uses the cut value of the most probable measured bitstring as the optimization objective, combines it with Bayesian optimization, and adaptively allocates shots using dual criteria based on mode confidence and normalized cut-value variance. Numerical experiments on 3-regular MaxCut show that, for both unweighted and weighted instances, the proposed scheme achieves discrete-solution quality comparable to that of the conventional expectation-based objective while typically requiring fewer total shots to reach the same final mode accuracy. These results indicate that reorganizing QAOA around the maximum-probability bitstring provides an effective route to improving practical performance under limited measurement budgets.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2408.01241v5
- Title: Radiofrequency cascade readout of coupled spin qubits
- Authors: Jacob F. Chittock-Wood, Ross C. C. Leon, Michael A. Fogarty, Tara Murphy, Felix-Ekkehard von Horstig, Sofia M. Patomäki, Giovanni A. Oakes, James Williams, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2408.01241v5  pdf=https://arxiv.org/pdf/2408.01241v5.pdf

Abstract:
Silicon spin qubits based on metal-oxide-semiconductor (MOS) technology are compatible with semiconductor manufacturing and offer a route to scalable quantum processing. However, spin readout typically relies on proximal charge sensors, which add architectural complexity and limit qubit connectivity. In situ dispersive readout techniques are more compact, which can alleviate these constraints, but exhibit limited sensitivity. Here we report a radiofrequency electron-cascade readout method that enhances the dispersive signal through alternating-current electron co-tunnelling. With this approach, we achieve an enhancement in signal-to-noise ratio of more than $35~$dB, leading to a minimum integration time of $7.6 \pm 0.2~μ$s. We demonstrate singlet-triplet readout of two-electron spins in a natural silicon planar MOS quantum dot array, and coherent spin control using the exchange interaction, which forms the basis for entangling gates. We find dephasing times of up to $500~$ns and a gate quality factor that exceeds 10.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2509.06937v2
- Title: Quantum Mpemba Effect in a Four-Site Bose-Hubbard Model
- Authors: Asad Ali, Hamid Arian Zad, Muhammad Irtiza Hussain, Saif Al-Kuwari, Hashir Kuniyil, Muhammad Talha Rahim, Michal Jaščur, Saeed Haddadi
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2509.06937v2  pdf=https://arxiv.org/pdf/2509.06937v2.pdf

Abstract:
We investigate relaxation-order inversion, known as the quantum Mpemba effect (QME), in a minimal open many-body system called a one-dimensional four-site Bose--Hubbard chain governed by Lindblad dynamics with local number dephasing. Families of thermal initial states are prepared at a fixed temperature and evolved under a common reference Liouvillian toward the same stationary state. Relaxation is characterized using four complementary diagnostics: trace distance, quantum relative entropy, symmetry-projected entropy imbalance (entanglement asymmetry), and the $\ell_{1}$-norm of coherence in the Fock basis. We find that QME emerges robustly in -the clean interacting regime, where on-site interactions redistribute the overlaps of initial states with slow Liouvillian decay modes, enabling states initially farther from equilibrium to converge faster at late times. In contrast, the noninteracting limit exhibits a monotonic relaxation hierarchy across all metrics. Introducing a linear Stark potential or random on-site disorder suppresses relaxation and eliminates QME signatures by inhibiting transport-assisted mixing and enhancing the dominance of slow modes. Within the explored parameter regime, the Stark field induces significantly stronger retardation than disorder. We further show that symmetry-projected entropy imbalance is particularly sensitive to charge-sector decoherence in reduced subsystems and provides a stringent probe of QME in bosonic platforms. Our results elucidate the essential role of interactions in enabling anomalous relaxation in open lattice systems and connect the suppression of QME under spatial inhomogeneity to localization phenomena in tilted and disordered Bose--Hubbard chains.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2510.06176v2
- Title: An integrated photonic millimeter-wave receiver with sub-ambient noise
- Authors: Junyin Zhang, Shuhang Zheng, Jiachen Cai, Connor Denney, Zihan Li, Yichi Zhang, Xin Ou, Gabriel Santamaria-Botello, et al.
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2510.06176v2  pdf=https://arxiv.org/pdf/2510.06176v2.pdf

Abstract:
Decades of progress in radiofrequency (RF) transistors and receiver frontends have profoundly impacted wireless communications, remote sensing, navigation, and instrumentation. Growing demands for data throughput in 6G networks, timing precision in positioning systems, and resolution in atmospheric sensing and automotive radar have pushed receiver frontends into the millimeter-wave (mmW) and sub-mmW/THz regimes. At these frequencies, however, the noise performance of field-effect transistors (FETs) degrades rapidly due to parasitic effects, limited carrier mobility, hot electrons, and shot noise. Parametric transducers that couple electromagnetic signals to optical fields offer quantum-limited sensitivity at room temperature. Electro-optic materials enable receivers that convert RF signals into optical phase shifts. While early demonstrations used resonant devices and recent efforts have focused on cryogenic microwave-to-optical quantum transduction, room-temperature electro-optic receivers have yet to achieve noise figures comparable to their electronic counterparts. Here we demonstrate a room-temperature integrated cavity electro-optic mmW receiver on a lithium tantalate (LiTaO3) photonic integrated circuit with 2.5% on-chip photon-number transduction efficiency, achieving 250 K noise temperature at 59.33 GHz--matching state-of-the-art LNAs. We report the first direct resolution of thermal noise in cavity electro-optic transduction, showing the system is fundamentally limited by thermal photon occupation (~100) in the mmW cavity. Our work establishes integrated photonics as a path to surpass electronic LNAs while offering exceptional resilience to strong electromagnetic inputs and immunity to EMI, establishing cavity electro-optics as a low-noise, chip-scale, EMI-resilient receiver frontend for mmW applications and scalable analog processing in the optical domain.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2511.04537v3
- Title: Probing quantum entanglement with Generalized Parton Distributions at the Electron-Ion Collider
- Authors: Yoshitaka Hatta, Jakob Schoenleber
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2511.04537v3  pdf=https://arxiv.org/pdf/2511.04537v3.pdf

Abstract:
Within the collinear factorization framework based on Generalized Parton Distributions (GPDs), we calculate the spin density matrix of exclusively produced quark and antiquark pairs $u\bar{u}$, $d\bar{d}$, $s\bar{s}$, $c\bar{c}$, $b\bar{b}$ in electron-proton scattering. The presence of both real and imaginary parts in the scattering amplitudes leads to a rich pattern of entanglement between the quark and the antiquark. We map out kinematical regions where the pairs exhibit entanglement, Bell nonlocality and non-stabilizerness (`magic'). We also predict that massive quarks and antiquarks are transversely polarized, similar to the well-known transverse hyperon polarization in unpolarized collisions. In strangeness, charm and bottom productions, the polarization can reach 50-80\% in certain kinematic regions in the low-energy runs of the Electron-Ion Collider.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2512.07632v2
- Title: Mesoscopic superfluid to superconductor transition
- Authors: Yehoshua Winsten, Doron Cohen
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2512.07632v2  pdf=https://arxiv.org/pdf/2512.07632v2.pdf

Abstract:
Spectrum tomography for the energy ($E$) of a ring-shaped Bose-Hubbard circuit is illustrated. There is an inter-particle interaction $U$ that controls superfluidity (SF) and the transition to the Mott Insulator (MI) regime. The circuit is coupled to an electromagnetic cavity mode of frequency $ω_0$, and the coupling is characterized by a generalized fine-structure-constant $α$ that controls the emergence of superconductivity (SC). The ${(U,α,ω_0,E)}$ diagram features SF and SC regions, a vast region of fragmented possibly chaotic states, and an MI regime for large $U$. The mesoscopic version of the Meissner effect and the Anderson-Higgs mechanism are discussed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2512.12100v2
- Title: On the Bogoliubov-Valatin transformation for fermionic Hamiltonians without a linear part
- Authors: Davide Bonaretti
- Categories: cond-mat.other (primary); cond-mat.other; quant-ph
- Links: abs=https://arxiv.org/abs/2512.12100v2  pdf=https://arxiv.org/pdf/2512.12100v2.pdf

Abstract:
A self-contained treatment of the Bogoliubov-Valatin transformation for homogeneous fermionic Hamiltonians is presented. The aim is to provide a quick reference that may also serve as supplementary material for a graduate-level course, and that can be understood with quantum mechanics knowledge up to the level of the second quantization's rules. The objective of the transformation is to cast a quadratic Hamiltonian into a diagonal form that resembles the Hamiltonian of a system of non-interacting particles. To obtain this, the first step consists in putting its coefficient matrix into its canonical form; the transformation can always be performed on fermionic Hamiltonians, only some care must be taken when this form is singular. Having explained how to cast a general matrix into its standard form, a complete description of the transformation is provided; a novel procedure is proposed here for the singular matrix case.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2601.02259v3
- Title: Exact Mobility Edges in a Disorder-Free Dimerized Stark Lattice with Effective Unbounded Hopping
- Authors: Yunyao Qi, Heng Lin, Quanfeng Lu, Dong Ruan, Gui-Lu Long
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; quant-ph
- Links: abs=https://arxiv.org/abs/2601.02259v3  pdf=https://arxiv.org/pdf/2601.02259v3.pdf

Abstract:
We propose a disorder-free one-dimensional single-particle Hamiltonian hosting an exact mobility edge (ME), placing the system outside the assumptions of no-go theorems regarding unbounded potentials. By applying a linear Stark potential selectively to one sublattice of a dimerized chain, we generate an effective Hamiltonian with unbounded, staggered hopping amplitudes. The unbounded nature of the hopping places the model outside the scope of the Simon-Spencer theorem, while the staggered scaling allows it to evade broader constraints on Jacobi matrices. We analytically derive the bulk spectrum in reciprocal space, identifying a sharp ME where the energy magnitude equals the inter-cell hopping strength. This edge separates a continuum of extended states from two distinct localized branches: a standard unbounded Wannier-Stark ladder and an anomalous bounded branch accumulating at the ME. The existence of extended states is supported by finite-size scaling of the inverse participation ratio up to system sizes $L \sim 10^9$. Furthermore, we propose an experimental realization using photonic frequency synthetic dimensions. Our numerical results indicate that the ME is robust against potential experimental imperfections, including frequency detuning errors and photon loss, establishing a practical path for observing MEs in disorder-free systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.27872v2
- Title: Enhancing Spin Coherence of Optically-Addressed Molecular Qubit by Nuclear Spin Hyperpolarization
- Authors: Boning Li, Patrick Hautle, Duhan Zhang, Liangping Zhu, Ashley Beers, Zeyu Wang, Paola Cappellaro, Tom Wenckebach, et al.
- Categories: physics.chem-ph (primary); physics.chem-ph; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2603.27872v2  pdf=https://arxiv.org/pdf/2603.27872v2.pdf

Abstract:
Optically addressable molecular triplet spins provide a chemically tunable platform for quantum application, but their coherence is often limited by interactions with surrounding spin baths. Here we demonstrate controlled suppression of nuclear-bath-induced decoherence in photoexcited triplet spins of pentacene co-crystallized in high-purity naphthalene single crystals. By hyperpolarizing the proton spin bath through triplet dynamic nuclear polarization (triplet-DNP), magnetic noise generated by the nuclear spins is suppressed, leading to an extension of the electron spin transverse coherence time. Experimentally, we observe a 25\% enhancement of the spin-echo decay time with $60\%$ polarization of the proton spin bath. The measured scaling of the spin-echo decay time ($T_2$) with nuclear polarization quantitatively follows the predicted dependence derived from the polarization-controlled nuclear second moment. Both the enhancement and the absolute value of the coherence time are quantitatively reproduced by cluster correlation expansion (CCE) simulations. These results establish nuclear spin hyperpolarization as a general and actively tunable approach to engineering coherence in molecular qubits. This work provides a broadly applicable design framework for high-coherence molecular and solid-state spin systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28230v2
- Title: Exact $\mathbb{Z}_2$ electromagnetic duality of $\mathbb{Z}_2$ toric code is non-Clifford
- Authors: Ryohei Kobayashi
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28230v2  pdf=https://arxiv.org/pdf/2603.28230v2.pdf

Abstract:
The 2D $\mathbb{Z}_2$ toric code admits a global symmetry exchanging electric and magnetic quasiparticles, known as electromagnetic duality. Known realizations include lattice translation symmetry, an exact $\mathbb{Z}_4$ symmetry generated by a Clifford circuit, and an exact $\mathbb{Z}_2$ symmetry generated by a non-Clifford circuit. We show that a Clifford electromagnetic duality cannot realize an exact internal $\mathbb{Z}_2$ symmetry. This is proved rigorously for symmetries with coarse translation invariance by $l$ lattice units for generic odd $l$. Therefore an exact internal $\mathbb{Z}_2$ electromagnetic duality must be non-Clifford, whereas generic internal Clifford realization necessarily has $\mathbb{Z}_{2^m}$ algebra with $m\ge 2$. Our result suggests an unexpected connection between the algebra of exact electromagnetic duality and Clifford hierarchy of circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-02 09:56
- arXiv: 2603.28373v2
- Title: Perspective of Fermi's golden rule and its generalizations in chemical physics
- Authors: Seogjoo J. Jang, Goun Kim, Young Min Rhee
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.28373v2  pdf=https://arxiv.org/pdf/2603.28373v2.pdf

Abstract:
This perspective provides a succinct history of Fermi's golden rule (FGR), overview of its derivation, assumptions, and representative forms. Major applications of FGR, mostly in the field of chemical physics, are reviewed. These illustrate the broad applicability and success of FGR. Ambiguities and open issues encountered in practical applications of FGR are clarified. Recent advances in generalizations of FGR and computational methods for practical applications are addressed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01250v1
- Title: Hybrid Classical--Quantum Optimization of Wireless Routing Using QAOA and Quantum Walks
- Authors: Eric Howard, Hardique Dasore, Hom Nath Dhungana, Radhika Kuttala, Samuel Murphy, Emma Soo, Shah Haque
- Categories: quant-ph (primary); quant-ph; cs.NI
- Links: abs=https://arxiv.org/abs/2604.01250v1  pdf=https://arxiv.org/pdf/2604.01250v1.pdf

Abstract:
Routing in wireless communication networks is shaped by mobility, interference, congestion, and competing service requirements, making route selection a high-dimensional constrained optimization problem rather than a simple shortest-path task. This paper investigates the use of hybrid classical--quantum methods for wireless routing, focusing on the Quantum Approximate Optimization Algorithm (QAOA) and quantum walks as candidate mechanisms for exploring complex routing spaces. The paper examines how wireless routing can be expressed as a constrained graph optimization problem in which routing objectives, flow constraints, connectivity requirements, and interference effects are mapped into quantum-compatible Hamiltonian representations. It then discusses how these approaches can be integrated into a hybrid architecture in which classical systems perform network monitoring, graph construction, pre-processing, and deployment, while quantum subroutines are used for selected optimization components. The analysis shows that the potential value of quantum routing lies primarily in the treatment of difficult combinatorial subproblems rather than end-to-end replacement of classical routing frameworks. The paper also highlights practical limitations arising from state preparation, constraint encoding, oracle construction, hardware noise, limited qubit resources, and hybrid execution overhead. It is argued that any meaningful near-term advantage will depend on careful problem decomposition, compact encoding, and tight classical--quantum integration.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01282v1
- Title: Exhaustive Optimisation of Automorphism Groups for Stabiliser Codes
- Authors: Aisling Mac Aree, Mark Howard
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01282v1  pdf=https://arxiv.org/pdf/2604.01282v1.pdf

Abstract:
An important measure of utility for a quantum code is the identification of which logical operations can be implemented fault-tolerantly on its codespace. We introduce a framework which leverages the automorphism groups of associated classical codes, the choice of logical basis and exploitation of code equivalence to construct all distinct implementable realisations of each valid logical operation for a given $[[n,k,d]]$ code. We establish conjugacy classes and group transversals (unrelated to transversality) as key explanatory concepts. We subsequently motivate and calculate two figures-of-merit that can be optimised with this framework. Our results yield a table of optimal logical operations and their corresponding physical circuits for all small stabiliser codes with $n \leq 7$ and $k \leq 2$, drawn from quantum databases. This exhaustive table of results provides the optimal physical implementations of logical operations which may be advantageous for both magic state cultivation and experimental purposes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01296v1
- Title: Bootstrapping Symmetries in Quantum Many-Body Systems from the Cross Spectral Form Factor
- Authors: Chen Bai, Zihan Zhou, Bastien Lapierre, Shinsei Ryu
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; hep-th
- Links: abs=https://arxiv.org/abs/2604.01296v1  pdf=https://arxiv.org/pdf/2604.01296v1.pdf

Abstract:
Symmetries play a central role in quantum many-body physics, yet uncovering them systematically remains challenging. We introduce a bootstrap framework designed to reconstruct the representation theory of hidden finite group symmetries of quantum many-body lattice Hamiltonians, using only a known symmetry subgroup $N$ and spectral correlations between its symmetry sectors. We introduce a novel variant of the spectral form factor, the cross spectral form factor (xSFF), which we compute via exact diagonalization to seed the bootstrap algorithm. By applying the constraints derived from these data alongside the algebraic conditions of the fusion rules, our bootstrap procedure sharply restricts the set of candidate groups $G$. Remarkably, without any prior assumptions regarding the full symmetry group $G$, our method can systematically recover its representation-theoretic data, including the number and dimensions of the irreducible representations, their branching rules with respect to $N$, the fusion algebra, and the full character table. This framework applies equally well to chaotic and integrable many-body systems and accommodates both unitary and anti-unitary symmetries. Through various examples, we demonstrate that the underlying group $G$ can be uniquely identified. In particular, our bootstrap independently recovers the $\mathbb{Z}_4$ symmetry at the self-dual point of the three-state quantum torus chain, detects signatures of projective representations in the effective Hamiltonian of the driven Bose-Hubbard model, and rediscovers the $η$-pairing $\mathrm{SO}(4)$ symmetry of the one-dimensional Fermi-Hubbard model. Our framework thus establishes a practical route to identify symmetries directly from dynamical spectral observables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01301v1
- Title: Numerically Optimizing Shortcuts to Adiabaticity: A Hybrid Control Strategy
- Authors: Bo Xing, Jesús G. Parejo, Sofía Martínez-Garaot, Paola Cappellaro, Mikel Palmero
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2604.01301v1  pdf=https://arxiv.org/pdf/2604.01301v1.pdf

Abstract:
Achieving fast, excitation-free quantum control is a vital challenge in modern quantum technologies. In many cases, shortcuts to adiabaticity enable fast adiabatic-like protocols, yet determining control parameters that satisfy practical constraints is often challenging in complex systems. Here, we combine an analytical shortcut to adiabaticity approach with several numerical optimization methods to boost the performance of the protocol. As a proof-of-principle for this hybrid approach, we study a particularly intricate control problem, the separation of two trapped ions. We show that this analytical-numerical approach, along with the physical insight gained through the variety of suboptimal solutions, leads to the exploration of new solutions in a complex landscape that yield improvements of up to 3 orders of magnitude. Moreover, this improvement comes with no additional cost from an experimental point of view.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01353v1
- Title: Constructing Fermionic Dynamics with Closed Moment Hierarchies
- Authors: A. E. Teretenkov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01353v1  pdf=https://arxiv.org/pdf/2604.01353v1.pdf

Abstract:
We construct a broad class of completely positive maps and Go\-rini--Kossakowski--Sudarshan-Lindblad generators for fermionic systems induced by linear transformations of system and environment modes. For these maps, we derive explicit Heisenberg-picture formulas for arbitrary normally ordered monomials in terms of minors of the underlying mode-transformation matrices and environment correlation tensors. We show that for even environment states the linear span of monomials up to any fixed order is invariant, which yields closed equations for low-order moments and makes their computation efficient. We also discuss the relation of this construction to second quantization of non-Hermitian one-particle contractions and extend the formalism to completely positive maps arising from post-selection.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01369v1
- Title: Programmable recirculating bricks mesh architecture for quantum photonics
- Authors: Jacek Gosciniak
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.01369v1  pdf=https://arxiv.org/pdf/2604.01369v1.pdf

Abstract:
General-purpose programmable photonic processors offer a flexible foundation for integrating various functionalities within a single chip. A two-dimensional hexagonal waveguide mesh of Mach Zehnder interferometers has been shown to have great potential in the field of microwave photonics. Additionally, they are a promising platform for the creation of unitary linear transformations, which are key elements in photonic neural networks, In this article, we expand the portfolio of available applications for recirculating bricks mesh architecture to quantum technologies. We will show that a single programmable optical system is capable of performing various functions depending on the requirements. In particular, we will focus in this work on boson sampling, a task that best demonstrates quantum advantage, as well as on tasks that enable the determination of photon indistinguishability, which plays a key role in photonic quantum technologies. We will also show that, in addition to spatial modes, the same optical system can be equally well-suited for work on temporal modes through the implementation of an appropriate number of loops.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01376v1
- Title: Resource Estimation via Efficient Compilation of Key Quantum Primitives
- Authors: Colin Campbell, Rich Rines, Victory Omole, Tina Oberoi, Palash Goiporia, Rayat Roy, R. Peyton Cline, Eric B. Jones, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01376v1  pdf=https://arxiv.org/pdf/2604.01376v1.pdf

Abstract:
Resource estimation is a significant challenge in evaluating fault tolerant quantum computers. Existing approaches often rely on either fixed architectural assumptions or coarse analytical models that fail to capture the interaction between hardware constraints and circuit compilation. This challenge is particularly acute for neutral atom quantum computers, where architectural features such as atom movement, measurement zones, and multi-species arrays introduce a broad design space for implementing fault tolerant computation. Addressing the need for a tighter feedback loop between hardware design and practical application development, we present a compilation-driven framework for quantum resource estimation that translates arbitrary quantum circuits into logical primitive operations with known physical resource costs. This framework allows for easily configurable hardware assumptions that enable rapid comparison of different architectural design choices. We apply our approach to two early fault tolerant quantum simulation and optimization workloads, assuming the use of the surface code, revealing several architectural trends. While the production of magic states continues to be the dominant source of overhead for these benchmarks, access to movement can save time on cultivation and important transversal gates. As problem size grows, routing and qubit movement become dominant bottlenecks, highlighting the need for movement-aware compiler optimizations and frugal routing strategies. Finally, our results suggest that neutral atom architectures combining dual-species arrays with controlled qubit movement offer a promising path toward near-term advantage on fault tolerant devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01408v1
- Title: Quantum polymorphism characterisation of commutativity gadgets in all quantum models
- Authors: Eric Culf, Josse van Dobben de Bruyn, Peter Zeman
- Categories: quant-ph (primary); quant-ph; cs.CC; math.OA
- Links: abs=https://arxiv.org/abs/2604.01408v1  pdf=https://arxiv.org/pdf/2604.01408v1.pdf

Abstract:
Commutativity gadgets provide a technique for lifting classical reductions between constraint satisfaction problems to quantum-sound reductions between the corresponding nonlocal games. We develop a general framework for commutativity gadgets in the setting of quantum homomorphisms between finite relational structures. Building on the notion of quantum homomorphism spaces, we introduce a uniform notion of commutativity gadget capturing the finite-dimensional quantum, quantum approximate, and commuting-operator models. In the robust setting, we use the weighted-algebra formalism for approximate quantum homomorphisms to capture corresponding notions of robust commutativity gadgets.   Our main results characterize both non-robust and robust commutativity gadgets purely in terms of quantum polymorphism spaces: in any model, existence of a commutativity gadget is equivalent to the collapse of the corresponding quantum polymorphisms to classical ones at arity $|A|^2$, and robust gadgets are characterized by stable commutativity of the appropriate weighted polymorphism algebra. We use this characterisation to show relations between the classes of commutativity gadget, notably that existence of a robust commutativity gadget is equivalent to the existence of a corresponding non-robust one.   Finally, we prove that quantum polymorphisms of complete graphs $K_n$ have a very special structure, wherein the noncommutative behaviour only comes from the quantum permutation group $S_n^+$. Combining this with techniques from combinatorial group theory, we construct separations between commutativity-gadget classes: we exhibit a relational structure admitting a finite-dimensional commutativity gadget but no quantum approximate gadget, and, conditional on the existence of a non-hyperlinear group, a structure admitting a quantum approximate commutativity gadget but no commuting-operator gadget.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01426v1
- Title: Distributed Variational Quantum Linear Solver
- Authors: Tong Shen, Zeru Zhu, Ji Liu
- Categories: quant-ph (primary); quant-ph; cs.DC; math.OC
- Links: abs=https://arxiv.org/abs/2604.01426v1  pdf=https://arxiv.org/pdf/2604.01426v1.pdf

Abstract:
This paper develops a distributed variational quantum algorithm for solving large-scale linear equations. For a linear system of the form $Ax=b$, the large square matrix $A$ is partitioned into smaller square block submatrices, each of which is known only to a single noisy intermediate-scale quantum (NISQ) computer. Each NISQ computer communicates with certain other quantum computers in the same row and column of the block partition, where the communication patterns are described by the row- and column-neighbor graphs, both of which are connected. The proposed algorithm integrates a variant of the variational quantum linear solver at each computer with distributed classical optimization techniques. The derivation of the quantum cost function provides insight into the design of the distributed algorithm. Numerical quantum simulations demonstrate that the proposed distributed quantum algorithm can solve linear systems whose size scales with the number of computers and is therefore not limited by the capacity of a single quantum computer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01429v1
- Title: Classical shadows with arbitrary group representations
- Authors: Maxwell West, Frederic Sauvage, Aniruddha Sen, Roy Forestano, David Wierichs, Nathan Killoran, Dmitry Grinko, M. Cerezo, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01429v1  pdf=https://arxiv.org/pdf/2604.01429v1.pdf

Abstract:
Classical shadows (CS) has recently emerged as an important framework to efficiently predict properties of an unknown quantum state. A common strategy in CS protocols is to parametrize the basis in which one measures the state by a random group action; many examples of this have been proposed and studied on a case-by-case basis. In this work, we present a unified theory that allows us to simultaneously understand CS protocols based on sampling from general group representations, extending previous approaches that worked in simplified (multiplicity-free) settings. We identify a class of measurement bases which we call "centralizing bases" that allows us to analytically characterize and invert the measurement channel, minimizing classical post-processing costs. We complement this analysis by deriving general bounds on the sample-complexity necessary to obtain estimates of a given precision. Beyond its unification of previous CS protocols, our method allows us to readily generate new protocols based on other groups, or different representations of previously considered ones. For example, we characterize novel shadow protocols based on sampling from the spin and tensor representations of $\textsf{SU}(2)$, symmetric and orthogonal groups, and the exceptional Lie group $G_2$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01478v1
- Title: Twisted Fiber Bundle Codes over Group Algebras
- Authors: Chaobin Liu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01478v1  pdf=https://arxiv.org/pdf/2604.01478v1.pdf

Abstract:
We introduce a twisted fiber-bundle construction of quantum CSS codes over group algebras \(R=\mathbb F_2[G]\), where each base generator carries a generator-dependent \(R\)-linear fiber twist satisfying a flatness condition. This construction extends the untwisted lifted product code, recovered when all twists are identities. We show that invertible twists (satisfying a flatness condition) give a complex chain-isomorphic to the untwisted one, so the resulting binary CSS codes have the same blocklength \(n\) and encoded dimension \(k\). In contrast, singular chain-compatible twists can lower boundary ranks and increase the number of logical qubits. Examples over \(R=\mathbb F_2[D_3]\) show that the twisted fiber bundle code can outperform the corresponding untwisted lifted-product code in \(k\) while keeping the same \(n\) and, in our examples, the same minimum distance \(d\).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01482v1
- Title: Practical Tomography of Multi-Time Processes
- Authors: Abhinash Kumar Roy, Varun Srivastava, Christina Giarmatzi, Alexei Gilchrist
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01482v1  pdf=https://arxiv.org/pdf/2604.01482v1.pdf

Abstract:
Characterising multi-time quantum processes is essential for analysing temporally correlated noise and for designing effective control and mitigation strategies. A complete operational description through multi-time process tomography requires an informationally complete set of probes, which necessarily includes non-deterministic intermediate operations. On present-day quantum devices, such operations are commonly implemented using mid-circuit measurements and reset, which are technologically limited and can introduce noise and overhead in terms of ancilla requirement. In this work, we study the minimal ancillary dimension required for complete characterisation of multi-time processes. We show that sequential interactions with a single qubit ancilla can generate an informationally complete family of correlated probes for processes of arbitrary length, without requiring mid-circuit measurements or reset. Our result provides a resource-efficient route for complete multi-time process tomography and establishes that one qubit of coherent ancillary memory suffices for full reconstruction of arbitrary multi-time dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01507v1
- Title: The Quantum Walk Characteristic Polynomial Distinguishes All Strongly Regular Graphs of Prime Orde
- Authors: Diego Roldan
- Categories: quant-ph (primary); quant-ph; math.CO
- Links: abs=https://arxiv.org/abs/2604.01507v1  pdf=https://arxiv.org/pdf/2604.01507v1.pdf

Abstract:
Let $G$ be a strongly regular graph of prime order $p$ with connection degree $k \geq 6$. We prove that the \emph{quantum walk characteristic polynomial} $χ_q(G,λ) \coloneqq \det(λI - U_G)$, where $U_G$ is the coined quantum walk operator on $G$, completely determines $G$ up to isomorphism within the class of strongly regular graphs of the same order.   The proof proceeds in three steps. First, we show that $U_G$ block-diagonalizes under the discrete Fourier transform over $\Z_p$, yielding $p$ blocks $U_G^{(j)}$ of size $k \times k$. Second, we prove an explicit formula \[   χ_q\!\bigl(U_G^{(j)}, λ\bigr) =   (λ-1)^{(k-2)/2}(λ+1)^{(k-2)/2}   \!\left(λ^2 - \tfrac{2\widehat{A}_G(j)}{k}\,λ+ 1\right), \] from which the Fourier coefficient $\widehat{A}_G(j)$ is recovered as the unique real part of an eigenvalue of $U_G^{(j)}$ distinct from $\pm 1$. Third, the inverse discrete Fourier transform recovers the connection set $S$ of $G$, and Turner's theorem (1967) identifies $G$ up to isomorphism. As a consequence, graph isomorphism is decidable in polynomial time within this class using the quantum walk spectrum, without resorting to the general quasi-polynomial algorithm of Babai (2016).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01515v1
- Title: Codimension-controlled universality of quantum Fisher information singularities at topological band-touching defects
- Authors: C. A. S. Almeida
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2604.01515v1  pdf=https://arxiv.org/pdf/2604.01515v1.pdf

Abstract:
Topological phase transitions in generic multiband systems are mediated by band-touching defects whose codimension -- the number of momentum directions along which the gap closes linearly -- varies across universality classes. Although singular behavior of fidelity susceptibilities and quantum Fisher information (QFI) has been computed for specific models, no unifying principle connecting these results has been identified: it has remained unclear whether the controlling variable is spatial dimensionality, band structure, or an intrinsic geometric property of the defect. We resolve this question by showing that the singular contribution to the QFI with respect to the tuning parameter $m$ obeys a universal power-law scaling $\sim |m|^{p-2}$ for $p \neq 2$, with a logarithmic divergence $\sim \ln(1/|m|)$ at the marginal codimension $p = 2$, where $p$ denotes the codimension of the band-touching defect. This exponent is independent of spatial dimensionality, anisotropies, ultraviolet regularization, and additional gapped bands, and is protected by renormalization-group arguments at the linearized fixed point. The result unifies previously isolated observations for SSH chains ($p=1$), Chern insulators ($p=2$), and Weyl semimetals ($p=3$) as instances of a single codimension-dependent universality class, and reveals that only defects with $p \leq 2$ generate divergent information-geometric responses. This establishes a direct and previously missing link between topological classification in momentum space and quantum distinguishability in parameter space, with implications for metrological sensitivity near topological transitions and for the experimental detection of topological criticality via quantum geometric observables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01519v1
- Title: DQC1-completeness of normalized trace estimation for functions of log-local Hamiltonians
- Authors: Zhengfeng Ji, Tongyang Li, Changpeng Shao, Xinzhao Wang, Yuxin Zhang
- Categories: quant-ph (primary); quant-ph; cs.CC
- Links: abs=https://arxiv.org/abs/2604.01519v1  pdf=https://arxiv.org/pdf/2604.01519v1.pdf

Abstract:
We study the computational complexity of estimating the normalized trace $2^{-n}Tr[f(A)]$ for a log-local Hamiltonian $A$ acting on $n$ qubits. This problem arises naturally in the DQC1 model, yet its complexity is only understood for a limited class of functions $f(x)$.   We show that if $f(x)$ is a continuous function with approximate degree $Ω({\rm poly}(n))$, then estimating $2^{-n}Tr[f(A)]$ up to constant additive error is DQC1-complete, under a technical condition on the polynomial approximation error of $f(x)$. This condition holds for a broad class of functions, including exponentials, trigonometric functions, logarithms, and inverse-type functions. We further prove that when $A$ is sparse, the classical query complexity of this problem is exponential in the approximate degree, assuming a conjectured lower bound for a trace variant of the $k$-Forrelation problem in the DQC1 query model. Together, these results identify the approximate degree as the key parameter governing the complexity of normalized trace estimation: it characterizes both the quantum complexity (via efficient DQC1 algorithms) and, conditionally, the classical hardness, yielding an exponential quantum-classical separation. Our proof develops a unified framework that cleanly combines circuit-to-Hamiltonian constructions, periodic Jacobi operators, and tools from polynomial approximation theory, including the Chebyshev equioscillation theorem.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01534v1
- Title: Single-shot measurement learning as a self-certifying estimator for quantum-enhanced sensing
- Authors: Jeongho Bang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01534v1  pdf=https://arxiv.org/pdf/2604.01534v1.pdf

Abstract:
Single-shot measurement learning (SSML) learns a compensation unitary from a one-bit success/failure record and halts after a prescribed run of consecutive successes. We recast SSML as an adaptive estimator on a parameterized sensing manifold and ask what role it can play in quantum-enhanced sensing. First, we show that the terminal run itself furnishes an intrinsic certificate of local alignment: longer terminal runs certify smaller infidelity, and near the optimum this becomes a Fisher-calibrated certificate of parameter error. Second, for compensation-type sensing families, the Bernoulli success/failure record is locally matched to the probe quantum Fisher information (QFI), so SSML preserves the probe's metrological content despite using only one classical bit per copy. In this sense, SSML makes the quantum enhancement carried by the probe operationally available in an online self-terminating protocol. Applied to GHZ/NOON probes of depth $m$, SSML retains the familiar square-root entanglement gain over product probes at fixed total resource, while an ideal multiscale architecture remains compatible with Heisenberg scaling. Monte Carlo simulations of photonic NOON-state phase sensing show the expected near-inverse decay of terminal infidelity with entangled shots, SQL-like total-resource scaling at fixed entanglement depth, the corresponding fixed-resource entanglement gain, the global limitation of a single fringe scale, and the recovery of Heisenberg-compatible behavior under ideal multiscale hand-off. These results identify SSML as a Fisher-preserving, self-certifying estimator layer for quantum-enhanced sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01555v1
- Title: Scalable Ground-State Certification of Quantum Spin Systems via Structured Noncommutative Polynomial Optimization
- Authors: Jie Wang, David Jansen, Irénée Frerot, Marc-Olivier Renou, Victor Magron, Antonio Acín
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2604.01555v1  pdf=https://arxiv.org/pdf/2604.01555v1.pdf

Abstract:
A fundamental challenge in quantum physics is determining the ground-state properties of many-body systems. Whereas standard approaches, such as variational calculations, consist of writing down a wave function ansatz and minimizing over the possible states expressible by this ansatz, one can alternatively formulate the problem as a noncommutative polynomial optimization problem. This optimization problem can then be addressed using a hierarchy of semidefinite programming relaxations. In contrast to variational calculations, the semidefinite program can provide lower bounds for ground state energies and upper and lower bounds on observable expectation values. However, this approach typically suffers from severe scalability issues, limiting its applicability to small-to-medium-scale systems. In this article, we demonstrate that leveraging the inherent structures of the system can significantly mitigate these scalability challenges and thus allows us to compute meaningful bounds for quantum spin systems on up to $16\times16$ square lattices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01616v1
- Title: Quantum-Enhanced Processing with Tensor-Network Frontends for Privacy-Aware Federated Medical Diagnosis
- Authors: Hiroshi Yamauchi, Anders Peter Kragh Dalskov, Hideaki Kawaguchi, Rodney Van Meter
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01616v1  pdf=https://arxiv.org/pdf/2604.01616v1.pdf

Abstract:
We propose a privacy-aware hybrid framework for federated medical image classification that combines tensor-network representation learning, MPC-secured aggregation, and post-aggregation quantum refinement. The framework is motivated by two practical constraints in privacy-aware federated learning: MPC can introduce substantial communication overhead, and direct quantum processing of high-dimensional medical images is unrealistic with a small number of qubits. To address both constraints within a single architecture, client-side tensor-network frontends, Matrix Product State (MPS), Tree Tensor Network (TTN), and Multi-scale Entanglement Renormalization Ansatz (MERA), compress local inputs into compact latent representations, after which a Quantum-Enhanced Processor (QEP) refines the aggregated latent feature through quantum-state embedding and observable-based readout. Experiments on PneumoniaMNIST show that the effect of the QEP is frontend-dependent rather than uniform across architectures. In the present setting, the TTN+QEP combination exhibits the most balanced overall profile. The results also suggest that the QEP behaves more stably when the qubit count is sufficiently matched to the latent dimension, while noisy conditions degrade performance relative to the noiseless setting. The MPC benchmark further shows that communication cost is governed primarily by the dimension of the protected latent representation. This indicates that tensor-network compression plays a dual role: it enables small-qubit quantum processing on compressed latent features and reduces the communication overhead associated with secure aggregation. Taken together, these results support a co-design perspective in which representation compression, post-aggregation quantum refinement, and privacy-aware deployment should be optimized jointly.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01638v1
- Title: Mechanism for scale-free skin effect in one-dimensional systems
- Authors: Shu-Xuan Wang
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2604.01638v1  pdf=https://arxiv.org/pdf/2604.01638v1.pdf

Abstract:
Non-Hermitian skin effect (NHSE) is one of the most fascinating phenomena in non-Hermitian systems, which refers to enormous eigenstates localize at the boundary exponentially under open boundary condition (OBC). For typical NHSE, the localization length for a skin mode is independent of the system's size. Recently, some studies have revealed that for specific $1$-dimensional model, the localization length for eigenstates are proportional to the system's length under generalized boundary condition (GBC), and such phenomenon is dubbed as scale-free skin effect (SFSE). Further, SFSE is discovered in $1$-dimensional Hermitian chain with pure imaginary impurity at the end. In this work, we propose a mechanism for SFSE in 1-dimensional systems, which is model-independent. Our work provide a viewpoint for researching SFSE and shed new light on understanding finite size effect in non-Hermitian systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01722v1
- Title: A Differentiable Physical Framework for Goal-Driven Spin-State Engineering in Magnetic Resonance Spectroscopy
- Authors: Gaocheng Fu, Shiji Zhang, Kai Huang, Xue Yang, Huilin Zhang, Daxiu Wei, Ye-Feng Yao
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.med-ph
- Links: abs=https://arxiv.org/abs/2604.01722v1  pdf=https://arxiv.org/pdf/2604.01722v1.pdf

Abstract:
Magnetic Resonance Spectroscopy (MRS) offers a unique non-invasive window into metabolic processes, yet its potential remains strictly constrained by severe spectral congestion and intrinsic insensitivity. Traditional pulse sequence design, tethered to human intuition, predominantly targets simple quantum states, thereby overlooking the vast majority of the exponentially scaling operator space which consists of complex spin superpositions. Here, we introduce a spectrum-driven, end-to-end differentiable physical framework that transcends these heuristic limitations. By integrating physical laws with automatic differentiation algorithm, our approach directly navigates the high-dimensional spin dynamics space, bypassing the intractable inverse problem of state preparation. This enables the discovery of non-intuitive, complex mixed states that simultaneously satisfy the dual objectives of selective excitation and interferometric signal enhancement. We validate this paradigm by achieving the robust separation of Glutamate and Glutamine, which is a longstanding neuroimaging challenge, in the human brain at 3T, demonstrating spectral fidelity superior to conventional methods. By unlocking the "dark" informational content of nuclear spin ensembles, our work establishes a generalizable paradigm for goal-driven quantum state engineering in magnetic resonance and beyond.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01773v1
- Title: Distribution of Bell State Entanglement in Qubit Networks via Collision Models
- Authors: Mert Doğan, Öner Faruk Ödemiş, Elif Yunt, Özgür E. Müstecaplıoğlu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01773v1  pdf=https://arxiv.org/pdf/2604.01773v1.pdf

Abstract:
We propose a general scheme to controllably distribute pairwise entanglement in a quantum network of qubits by exploiting environmental ancilla qubits interacting with the network nodes through tunable Hamiltonians. Our approach leverages collision models, in which a quantum syatem interacts sequentially with ancilla units. We explore two distinct scenarios within this framework: one in which the ancilla is reset to its initial coherent state after each interaction (the traditional collision model), and another where the ancilla is not reset but its state is simply carried over to the next interaction, which we dub the repeated interaction model. In both scenarios, we ensure that the system-ancilla correlations are discarded between steps. We also demonstrate how varying the ancilla-system interaction patterns enables selective generation of entanglement between different qubit pairs, including non-neighbouring nodes that do not directly interact. The scheme is analyzed in networks up to three qubits under both collision and repeated interaction dynamics, revealing the genaration of maximally entangled bell pairs even in configurations where the interacting ancilla couples to only a single node. Our results provide a systematic and physically implementable route to entanglement distribution, offering potential applications in quantum communication, metrology and modular quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01831v1
- Title: Topology-Hiding Path Validation for Large-Scale Quantum Key Distribution Networks
- Authors: Stephan Krenn, Omid Mir, Thomas Lorünser, Sebastian Ramacher, Florian Wohner
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2604.01831v1  pdf=https://arxiv.org/pdf/2604.01831v1.pdf

Abstract:
Secure long-distance communication in quantum key distribution (QKD) networks depends on trusted repeater nodes along the entire transmission path. Consequently, these nodes will be subject to strict auditing and certification in future large-scale QKD deployments. However, trust must also extend to the network operator, who is responsible for fulfilling contractual obligations -- such as ensuring certified devices are used and transmission paths remain disjoint where required. In this work, we present a path validation protocol specifically designed for QKD networks. It enables the receiver to verify compliance with agreed-upon policies. At the same time, the protocol preserves the operator's confidentiality by ensuring that no sensitive information about the network topology is revealed to users. We provide a formal model and a provably secure generic construction of the protocol, along with a concrete instantiation. For long-distance communication involving 100 nodes, the protocol has a computational cost of 1-2.5s depending on the machine, and a communication overhead of less than 70kB - demonstrating the efficiency of our approach.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01856v1
- Title: Curvature-induced bound states in quantum wires
- Authors: Tim Bergmann, Benjamin Schwager, Jamal Berakdar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01856v1  pdf=https://arxiv.org/pdf/2604.01856v1.pdf

Abstract:
A classical particle under spatial constraints is strictly confined to live on a specific space manifold or path, but this assumption is incompatible with the zero-point fluctuations of a quantum particle. One way to describe quantum mechanics under constraints is the confinement potential approach (CPA). For a non-relativistic particle, the CPA maps the problem onto the solution of a Schrödinger-type equation in an isometrically embedded Riemannian submanifold of Euclidean space while the motion along orthogonal directions are decoupled and spatially confined. This approach respects quantum uncertainty, and one of its key results is the appearance of geometry- and metric-induced potentials that affect the stationary states and the dynamics of the particle. For particles constrained to different spaces, such as structures hosting sharp bents, vertices, wedges, conical apices, tips, or self-intersections, a formalism beyond the CPA is needed. Here, a step towards a CPA extension for irregular spaces is presented. After classifying the possible geometric irregularities concerning the CPA formalism, the presentation is focused on a sharply bent quantum wire modeled as an embedded curve with singular (but absolute integrable) curvature. For a subclass fulfilling the additional requirement that the geometric potential is a distribution of first order, a solution scheme for the confined Schrödinger equation is presented based on singular Sturm-Liouville theory and operator theoretic methods. The analytical considerations and numerical simulations evidence the existence of curvature-induced bound states with non-differentiable wave functions localized around the singular point, with an extension well beyond the singularity. Furthermore, a multitude of scattering states appear that may affect the transport and optical properties of the system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01874v1
- Title: Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes
- Authors: Yiming Li, Zimu Li, Zi-Wen Liu
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2604.01874v1  pdf=https://arxiv.org/pdf/2604.01874v1.pdf

Abstract:
We exhibit nontrivial transversal logical multi-controlled-$Z$ gates on $[\![N,Θ(N),\tildeΘ(N)]\!]$ quantum low-density parity-check codes and $[\![N,Θ(N),\tildeΘ(N)]\!]$ quantum locally testable codes with soundness $\tildeΘ(1)$, combining nearly optimal code parameters with fault-tolerant non-Clifford gates for the first time. Remarkably, our proofs are almost entirely algebraic-topological, showing that such presumably intricate logical gates naturally arise as a fundamental topological phenomenon. We develop a general framework for constructing a rich new family of homological invariant forms which we call ''cupcap gates'' that induce transversal logical multi-controlled-$Z$ and, building on insights from [Li et al., arXiv:2603.25831], covering space methods to certify their nontriviality. The claimed almost-good code results follow immediately as examples.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01879v1
- Title: Phase-enhanced nonreciprocal photon-phonon conversion via coupled optomechanical cavities
- Authors: Divya Mishra, Parvendra Kumar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01879v1  pdf=https://arxiv.org/pdf/2604.01879v1.pdf

Abstract:
Nonreciprocity, characterized by direction-dependent signal propagation, is fundamental to technologies such as isolators, signal routing, and precision sensing. This letter theoretically demonstrates nonreciprocal phonon transport and the conversion between photon and acoustic phonon signals in coupled optomechanical cavities via phase-dependent driving. It is demonstrated that, in contrast to nonreciprocal phonon transport, which necessitates both dissipation and phase-induced violation of time reversal symmetry, the nonreciprocity in photon-phonon conversion can occur without violating time reversal symmetry. We demonstrate that such nonreciprocity arises due to the path-dependent asymmetry in photon-phonon conversion. Furthermore, we demonstrate that the nonreciprocity of photon-phonon conversion can be further enhanced, achieving isolation levels of up to 40 dB by suitably modifying the phase difference of the driving lasers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01891v1
- Title: A Loop-Shaping Approach to Coherent Feedback Control in Cavity Optomechanical Cooling
- Authors: Aoi Fujimoto, Hiroyuki Ichihara, Rina Kanamoto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.01891v1  pdf=https://arxiv.org/pdf/2604.01891v1.pdf

Abstract:
We present a loop-shaping approach to coherent feedback (CF) control. By formulating the coupling between a quantum system and its environment in terms of the noise power spectrum, our method enables direct manipulation of the effective dissipation coefficients through spectral shaping. A systematic design framework for CF controllers is also developed, in which transfer functions are shaped to realize desired spectral responses. Applying this framework to optomechanical sideband cooling, we demonstrate that suppression of the Stokes process and enhancement of the anti-Stokes process can be simultaneously achieved, enabling ground-state cooling even in the unresolved-sideband regime. This loop-shaping framework provides an intuitive and general foundation for the design of CF controllers and can be extended to a wide class of quantum systems in which interactions with environments are characterized by noise power spectra.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01918v1
- Title: Universal critical timescales in slow non-Hermitian dynamics
- Authors: Giorgos Pappas, Diego Bautista Avilés, Luis E. F. Foa Torres, Vassos Achilleos
- Categories: quant-ph (primary); quant-ph; cond-mat.other
- Links: abs=https://arxiv.org/abs/2604.01918v1  pdf=https://arxiv.org/pdf/2604.01918v1.pdf

Abstract:
Non-Hermitian systems driven along slow parametric loops undergo non-adiabatic transitions whose outcome depends sensitively on the driving speed, yet no explicit formula has been available for the critical timescale $T_{\mathrm{cr}}$ at which these transitions develop. Using a $2\times 2$ Hamiltonian with circular parameter trajectories, we derive $T_{\mathrm{cr}} = \mathcal{G}\,\ln(1/|Δ|)$ in closed form for non-encircling loops, phase-shifted loops, offset loops, and loops encircling exceptional points, where $\mathcal{G}$ is a geometry-dependent growth factor and $Δ$ is the instability seed. This formula sharply separates the regime where the system remains in the averagely dominant eigenstate ($T< T_{\mathrm{cr}}$) from the superadiabatic regime where the instantaneous dominant eigenstate takes over ($T> T_{\mathrm{cr}}$), resolving the apparent tension between the previous literature. We identify two competing seeds: a geometric Stokes multiplier and the finite-precision floor. When the geometric seed vanishes, precision alone governs the transition, yielding $T_{\mathrm{cr}} \propto m\lnβ$, linear in the number of precision bits $m$. This provides a purely forward-evolution manifestation of precision-induced irreversibility (PIR)~\cite{PIR}, demonstrating that the fundamental limit identified through echo protocols also controls the outcome of slow non-Hermitian dynamics without requiring time reversal. For PT-symmetric energy spectra, $T_{\mathrm{cr}}$ additionally determines the onset of chirality: the dynamics is non-chiral for $T< T_{\mathrm{cr}}$ and chiral for $T> T_{\mathrm{cr}}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01930v1
- Title: Quantum-Inspired Geometric Classification with Correlation Group Structures and VQC Decision Modeling
- Authors: Nishikanta Mohanty, Arya Ansuman Priyadarshi, Bikash K. Behera, Badshah Mukherjee
- Categories: quant-ph (primary); quant-ph; cs.AI
- Links: abs=https://arxiv.org/abs/2604.01930v1  pdf=https://arxiv.org/pdf/2604.01930v1.pdf

Abstract:
We propose a geometry-driven quantum-inspired classification framework that integrates Correlation Group Structures (CGR), compact SWAP-test-based overlap estimation, and selective variational quantum decision modelling. Rather than directly approximating class posteriors, the method adopts a geometry-first paradigm in which samples are evaluated relative to class medoids using overlap-derived Euclidean-like and angular similarity channels. CGR organizes features into anchor-centered correlation neighbourhoods, generating nonlinear, correlation-weighted representations that enhance robustness in heterogeneous tabular spaces. These geometric signals are fused through a non-probabilistic margin-based fusion score, serving as a lightweight and data-efficient primary classifier for small-to-moderate datasets. On Heart Disease, Breast Cancer, and Wine Quality datasets, the fusion-score classifier achieves 0.8478, 0.8881, and 0.9556 test accuracy respectively, with macro-F1 scores of 0.8463, 0.8703, and 0.9522, demonstrating competitive and stable performance relative to classical baselines. For large-scale and highly imbalanced regimes, we construct compact Delta-distance contrastive features and train a variational quantum classifier (VQC) as a nonlinear refinement layer. On the Credit Card Fraud dataset (0.17% prevalence), the Delta + VQC pipeline achieves approximately 0.85 minority recall at an alert rate of approximately 1.31%, with ROC-AUC 0.9249 and PR-AUC 0.3251 under full-dataset evaluation. These results highlight the importance of operating-point-aware assessment in rare-event detection and demonstrate that the proposed hybrid geometric-variational framework provides interpretable, scalable, and regime-adaptive classification across heterogeneous data settings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01983v1
- Title: Towards Chemically Accurate and Scalable Quantum Simulations on IQM Quantum Hardware: A Quantum-HPC Hybrid Approach
- Authors: Anurag K. S. V., Ashish Kumar Patra, Manas Mukherjee, Alok Shukla, Sai Shankar P., Ruchika Bhat, Radhika T. S. L., Jaiganesh G
- Categories: quant-ph (primary); quant-ph; cs.ET; physics.chem-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2604.01983v1  pdf=https://arxiv.org/pdf/2604.01983v1.pdf

Abstract:
We present a large-scale experimental study of quantum-computing-based molecular simulation carried out on IQM's Sirius 24-qubit superconducting processor, utilizing up to 16 operational qubits. The work employs Sample-based Quantum Diagonalization (SQD) together with the Local Unitary Cluster Jastrow (LUCJ) ansatz to estimate ground-state energies for a set of benchmark molecules, including H$_2$, LiH, BeH$_2$, H$_2$O, and NH$_3$. In addition, we introduce a Linear-CNOT variant of the Unitary Coupled-Cluster Singles and Doubles (LCNot-UCCSD) ansatz within the SQD workflow, trading higher circuit depth for reduced classical preprocessing. A comparison between these ansätze is provided, clarifying their respective strengths, limitations, and suitability for near-term quantum hardware. We further explore potential energy landscapes through 1D scans for H$_2$ and HeH$^+$ using both STO-3G and 6-31G basis sets, and for LiH and BeH$_2$ in STO-3G. Extending beyond this, we demonstrate the experimental construction of a full 2D potential energy surface for the water molecule on quantum hardware, mapped over a 32 $\times$ 32 grid in bond length and bond angle. To move beyond small benchmark systems, we combine SQD(LUCJ) with Density Matrix Embedding Theory (DMET) to compute active-space energies for a set of ligand-like molecules, as well as the pharmacologically relevant amantadine system. Across all studies, the majority of quantum-computed energies agree with reference FCI results, as well as with DMET-CASCI energies for embedded systems, to within chemical accuracy for the chosen basis sets. These results demonstrate the reliability of sample-based diagonalization approaches and underscore the potential of hybrid embedding strategies for extending quantum simulations to increasingly complex molecular systems, while also highlighting their practicality on current IQM quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02024v1
- Title: Compact system development of efficient quantum-entangled photon sources towards deployable and industrial devices
- Authors: Yared G. Zena, Moritz Langer, Ahmad Rahimi, Abhishikth Dhurjati, Pavel Ruchka, Sara Jakovljevic, Mandira Pal, Frank H. P. Fitzek, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2604.02024v1  pdf=https://arxiv.org/pdf/2604.02024v1.pdf

Abstract:
Entangled photon pair sources are a key enabling technology for quantum communication and networking, yet their deployment beyond laboratory environments is hindered by system-level complexity, limited operational stability, and insufficient industry compatibility. Here, we demonstrate a rack-based, mobile quantum light source architecture based on a semiconductor quantum dot emitter that directly addresses these challenges through modular system integration and automated operation. The source generates polarization-entangled photon pairs with an entanglement negativity 2n of up to $0.98(1)$, confirming near-maximal entanglement quality. In continuous, hands-off operation over a six-hour time window, the system achieves an average single-photon emission rate of $697(8)$ kHz and a maximum rate of $740(7)$ kHz, while maintaining 2n-value of more than $95$ $\%$. These results are enabled by the integration of optical excitation, collection, cryogenic operation, and control electronics within a standardized rack footprint, together with automated monitoring. By demonstrating simultaneously high entanglement quality, sustained brightness, and long-term operational stability in an industry-aligned system architecture, this work advances semiconductor quantum dot sources toward deployable entangled photon sources for applied quantum photonics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02026v1
- Title: Perspectives in and on Quantum Theory
- Authors: Richard Healey
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2604.02026v1  pdf=https://arxiv.org/pdf/2604.02026v1.pdf

Abstract:
I take a pragmatist perspective on quantum theory. This is not a view of the world described by quantum theory. In this view quantum theory itself does not describe the physical world, nor our observatons, experiences or opinions of it. Instead, the theory offers reliable advice on when to expect an event of one kind or another, and on how strongly to expect each possible outcome of that event. The actual outcome is a perspectival fact: a fact relative to a physical context of assessment. Measurement outcomes and quantum states are both perspectival. By noticing that each must be relativized to an appropriate physical context one can resolve the measurement problem and the problem of nonlocal action. But if the outcome of a quantum measurement is not an absolute fact, then why shoud the statistics of such outcomes give us any objective reason to accept quantum theory? One can describe extensions of the scenario of Wigner's friend in which a statement expressing the outcome of a quantum measurement would be true relative to one such context but not relative to another. However, physical conditions in our world prevent us from realizing such scenarios. Since the outcome of every actual quantum measurement is certified at what is essentially a single context of assessment, the outcome relative to that context is an objective fact in the only sense that matters for science. We should accept quantum theory because the statistics these outcomes display are just those it leads us to expect.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02027v1
- Title: Quantum search algorithm for similar subgraph identification under fixed edge removal
- Authors: Ruben Kara, Sven Danz, Tobias Stollenwerk, Andrea Benigni
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02027v1  pdf=https://arxiv.org/pdf/2604.02027v1.pdf

Abstract:
We introduce a novel quantum algorithm for similar subgraph identification in form of an NP-hard cardinality-constrained binary quadratic optimization problem. Given a weighted reference graph with Laplacian $\boldsymbol{B}$, our algorithm determines the subgraph featuring Laplacian $\boldsymbol{B'}$ on the same vertex set, but $x$ out of $N$ inactive edges, minimizing the Frobenius distance $||\boldsymbol{B} - \boldsymbol{B'}||_\mathrm{F}^2$. We represent the $\binom{N}{x}$ graph topologies by an equal-weight superposition in form of a Dicke state, enabling controlled transformations applied to the quantum state associated with the vectorized Laplacian of the reference graph. Combined with amplitude estimation and a minimum finding approach, our algorithm provides a polynomial speed up $\mathcal{O}(\sqrt{N^{x}/x!}N\log\log N)$ compared to $\mathcal{O}(N^{x+1}/x!)$ of classical brute-force search algorithms. We demonstrate the application of our method on standard test cases, which represent electric power grids, by reconstructing $||\boldsymbol{B} -\boldsymbol{B'}||_\mathrm{F}^2$ from measurements and show how our approach can be additionally used to calculate energy functional like quadratic forms of the Laplacians with respect to a given vector.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02033v1
- Title: High-threshold decoding of non-Pauli codes for 2D universality
- Authors: Julio C. Magdalena de la Fuente, Noa Feldman, Jens Eisert, Andreas Bauer
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2604.02033v1  pdf=https://arxiv.org/pdf/2604.02033v1.pdf

Abstract:
Topological codes have many desirable properties that allow fault-tolerant quantum computation with relatively low overhead. A core challenge for these codes, however, is to achieve a low-overhead universal gate set with limited connectivity. In this work, we explore a non-Pauli stabilizer code that can be used to complete a universal gate set on topological toric and surface codes in strictly two dimensions. Fault-tolerant syndrome extraction for the non-Pauli code requires mid-circuit $X$ corrections, a key difference to conventional Pauli codes. We construct and benchmark a just-in-time (JIT) matching decoder to reliably decide these corrections. Under a phenomenological error model with equally likely physical and measurement errors, we find a high threshold of $\approx 2.5\,\%$, close to the $\approx 2.9\,\%$ of a decoder with access to the full syndrome history. We also perform a finite-size scaling analysis to estimate how the logical error rate scales below threshold and verify an exponential suppression in both physical error rate and in the system size. A second global decoding step for $Z$ errors is required and the non-Clifford gates in the circuit reduce the threshold from $\approx 2.9\,\%$ to $\approx 1.8\,\%$ with a naive decoder. We show how $Z$ decoding can be improved using knowledge of the $X$ corrections, pushing the threshold to $\approx 2.2\,\%$. Our results suggest non-Clifford logic in 2D codes could perform comparably to 2D quantum memory. Our formalism for efficient benchmarking and decoding directly generalizes to a broader family of CSS codes whose $X$ stabilizers are twisted by diagonal Clifford operators, and spacetime versions thereof, defined by CSS-like circuits enriched by $CCZ$, $CS$, and $T$ gates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02064v1
- Title: Quantitative Universal Approximation for Noisy Quantum Neural Networks
- Authors: Lukas Gonon, Antoine Jacquier, Marcel Mordarski
- Categories: quant-ph (primary); quant-ph; math.NA; q-fin.PR
- Links: abs=https://arxiv.org/abs/2604.02064v1  pdf=https://arxiv.org/pdf/2604.02064v1.pdf

Abstract:
We provide here a universal approximation theorem with precise quantitative error bounds for noisy quantum neural networks. We focus on applications to Quantitative Finance, where target functions are often given as expectations. We further provide a detailed numerical analysis, testing our results on actual noisy quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02081v1
- Title: Photonic qubit encoding interconversion for heterogeneous quantum networking
- Authors: Vedansh Nehra, Richard J. Birrittella, Christopher C. Tison, Benjamin K. Malia, Zachary S. Smith, Dylan Heberle, Nicholas J. Barton, Amos Matthew Smith, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02081v1  pdf=https://arxiv.org/pdf/2604.02081v1.pdf

Abstract:
Quantum information processing, communication, and sensing networks are being developed with various qubit platforms that use different encoding schemes. Connecting quantum network nodes to distribute entanglement requires matching photon qubit basis encoding. In this work, we implement an interconversion protocol which converts photon qubit encoding from the polarization basis to the time-bin basis, transmits the photons through a transport fiber with large fluctuations in polarization, and converts back to polarization encoding for ease of measurement. This interconversion scheme faithfully transmits a polarization Bell state across the transport fiber by converting sources of infidelity to changes in transmission rate. These results illustrate a practical approach for interfacing distinct qubit platforms to enable modular and flexible operation in heterogeneous quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02083v1
- Title: Constrained Quantum Optimization via Iterative Warm-Start XY-Mixers
- Authors: David Bucher, Maximilian Janetschek, Michael Poppel, Jonas Stein, Claudia Linnhoff-Popien, Sebastian Feld
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02083v1  pdf=https://arxiv.org/pdf/2604.02083v1.pdf

Abstract:
The Quantum Approximate Optimization Algorithm (QAOA) is a leading hybrid heuristic for combinatorial optimization, but efficiently handling hard constraints remains a significant challenge. XY-mixers successfully confine quantum state evolution to a feasible subspace, such as the Hamming-weight-1 sector for one-hot constraints. On the contrary, warm-starting biases the search toward promising regions based on preliminary solutions. Combining these two techniques requires maintaining the essential alignment between the initial state and the mixer Hamiltonian to preserve convergence guarantees. Previous work demonstrated warm-starting with XY-mixers via a biased initial state, but relying only on standard mixer Hamiltonians. Consequently, the initial state is no longer a ground state of the mixer. In this work, we overcome these limitations by formulating a warm-started XY-mixer Hamiltonian for one-hot constraints and proving its ground-state properties. Furthermore, we provide a shallow circuit implementation suitable for NISQ implementations. We embed the warm-starting into a classical heuristic that iteratively updates the bias based on previous samples, called Iterative Warm-Starting (IWS). Extensive numerical simulations on Max-$k$-Cut and Traveling Salesperson Problem instances demonstrate that IWS-QAOA significantly accelerates the solution-finding process, increasing the probability of sampling optimal solutions by orders of magnitude compared to standard XY-QAOA. Finally, we validate our approach on the ibm_boston QPU using hardware-tailored 144-qubit problem instances. By coupling IWS-QAOA with a greedy steepest-descent post-processing strategy to repair infeasible measurements caused by hardware noise, we successfully identify optimal solutions on actual quantum devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02112v1
- Title: Q2NS Demo: A Quantum Network Simulator Based on ns-3
- Authors: Francesco Mazza, Adam Pearson, Marcello Caleffi, Angela Sara Cacciapuoti
- Categories: quant-ph (primary); quant-ph; cs.NI
- Links: abs=https://arxiv.org/abs/2604.02112v1  pdf=https://arxiv.org/pdf/2604.02112v1.pdf

Abstract:
Q2NS is an open-source quantum network simulator built on ns-3, the de facto standard for classical network simulation. By inheriting ns-3's mature classical stack and event-driven execution model, Q2NS enables faithful co-simulation of quantum-network dynamics and classical signaling, a core requirement for the functioning of any quantum network. Its modular architecture is designed for extensibility, with pluggable quantum-state backends (state-vector, density matrix, stabilizer) and a clean separation between network control and node-level operations. Q2NS comes with a quantum network visualizer Q2NSViz, supporting interactive inspection of both physical- and entanglement-induced connectivity graphs, helping users interpret protocol behavior and entanglement manipulation processes. We present a demonstration of Q2NS, highlighting its ability to capture and simulate the coexistence of quantum and classical communication. The proposed demonstration presents quantum communication scenarios of increasing complexity: from entanglement distribution basics to multipartite graph-state manipulation, complemented by pre-loaded examples in Q2NSViz that require no prior quantum communication or coding experience.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02169v1
- Title: The Phase Quantum Walk: A Unified Framework for Graph State Distribution in Quantum Networks
- Authors: Soumyojyoti Dutta
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02169v1  pdf=https://arxiv.org/pdf/2604.02169v1.pdf

Abstract:
Distributing arbitrary graph states across quantum networks is a central challenge for modular quantum computing and measurement-based quantum communication. I introduce the phase quantum walk (PQW), a discrete-time quantum walk in which the conventional position-permuting shift operator is replaced by a diagonal conditional phase (CZ) gate, enabling distribution of arbitrary graph states, not merely GHZ states, from elementary two-qubit resources. The Byproduct Lemma shows that each walk step teleports edge entanglement with a correctable Pauli byproduct; the Coin Invariance Theorem proves that the optimal fidelity F*(C,E) = F*(H,E) for all unitary coins C and noise channels E, with closed-form expressions F_dep = (1 - 3p/4)^k and F_pd = ((1 + sqrt(1 - p))/2)^k. Analytical correction formulas are derived for tree graphs (general theorem) and ring graphs (C4 case study), with F = 1.0 verified across eight topologies (up to 4096 outcomes). Hardware validation on ibm marrakesh (IBM Heron r2, CZ-native) yields F_cl = 0.924 for |GHZ4> and 0.922 for |L4>, statistically identical, providing the first experimental confirmation that fidelity is independent of graph topology as predicted by the Coin Invariance Theorem.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02175v1
- Title: Shot-to-shot noise cancellation for parametric oscillators
- Authors: Martynas Skrabulis, Martin Colombano Sosa, Nicola Carlon Zambon, Andrei Militaru, Massimiliano Rossi, Lukas Novotny, Martin Frimmer
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02175v1  pdf=https://arxiv.org/pdf/2604.02175v1.pdf

Abstract:
Powerful approaches to squeeze the motional state of a harmonic oscillator rely on the stepwise modulation of its resonance frequency. Such protocols can be limited by forces that vary slowly between experimental runs but are constant during a single experimental shot. Such shot-to-shot noise gives rise to a spread in experimental outcomes that masks the uncertainty intrinsic to quantum theory. Taking inspiration from spin-echo protocols, we propose a decoupling technique that, under ideal conditions, perfectly cancels shot-to-shot force noise in squeezing experiments based on parametric modulation. We implement the protocol using an optically levitated nanoparticle, where shot-to-shot force noise arises from slowly varying stray fields acting on the charge carried by the particle. Using our oscillator-echo protocol, we demonstrate shot-to-shot noise suppression to the measurement-backaction limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02197v1
- Title: A Pragmatist Understanding of Quantum Mechanics
- Authors: Richard Healey
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2604.02197v1  pdf=https://arxiv.org/pdf/2604.02197v1.pdf

Abstract:
Applications of quantum mechanics have led to many successful predictions and explanations of puzzling phenomena, and we now apply quantum mechanics to gain, process, and communicate information in novel ways. We can understand quantum mechanics by understanding how we have applied it. We should not seek agreement on the nature of the world it represents, because this theory does not itself represent the physical world (though its applications do help us to represent it better). When applied to a quantum state, quantum mechanics yields probabiities for physical events: both state and probability are objective--not because they represent elements of phyiscal reality, but because each exerts norrmative authority over the beliefs of anyone who accepts quantum mechanics and applies it relative to a physical situation they may (but need not) occupy. These events may be described by statements that are meaningful in an appropriate environmental context, and quantum mechanics can help one to say when that is. Measurement creates an appropriate context, so here the Born rule indirectly yields probabilities of measurement outcomes. The quantum state of a system does not "collapse" on measurement: a new state must be assigned relative to a physical situation in which information about the outcome is accessible. Understood this way, there is no measurement problem, and violations of Bell inequalities does not demonstrate "spooky" non-local action. Quantum field theories have no physical ontology of their own: a quantum field is a mathematical object in a model whose application helps us to improve and extend our descriptions of the world in other terms. We cannot realise the scenario of Wigner's friend and its recent extensions: but the data that provide overwhelming evidence for quantum mechanics are objective in the same sense as the relative measurement outcomes described in those scenarios.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02218v1
- Title: High-bandwidth Coherence Cloning using Optical-Phase-Locking Feedforward
- Authors: Chen Jia, Zhen-Xing Hua, Yu-Xin Chao, Meng Khoon Tey
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; physics.optics
- Links: abs=https://arxiv.org/abs/2604.02218v1  pdf=https://arxiv.org/pdf/2604.02218v1.pdf

Abstract:
Ultra-narrow-linewidth lasers with suppressed high-frequency phase noise are critical for quantum control and precision metrology. While optical phase locking (OPL) is the standard technique for cloning the coherence of such sources, its effectiveness is often limited at high frequencies by feedback latency. We present a robust feedforward architecture that overcomes this limitation by recycling and demodulating the existing master-slave beat signal to drive a single electro-optic modulator for near-instantaneous noise cancellation. This approach eliminates the extraneous sidebands and transmission losses typical of more complex modulators. Through active stabilization of the beat amplitude and demodulation phase, we demonstrate robust suppression exceeding 30 dB from 10 kHz to 10 MHz. This hardware-efficient framework is readily compatible with standard OPL setups, offering a scalable solution for high-fidelity coherent control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02233v1
- Title: Quantum Time-Space Tradeoffs for Exponential Dynamic Programming
- Authors: Susanna Caroppo, Jevgēnijs Vihrovs, Dārta Zajakina, Aleksejs Zajakins
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02233v1  pdf=https://arxiv.org/pdf/2604.02233v1.pdf

Abstract:
We investigate the quantum algorithms for dynamic programming by Ambainis et al. (SODA'19). While giving provable complexity speedups and applicable to a variety of NP-hard problems, these algorithms have a notable drawback: they require a large amount of Quantum Random Access Memory (QRAM), which potentially could be very challenging to implement in a physical quantum computer. In this work, we study how we can improve the space complexity by trading it for time, while still retaining a speedup over the classical algorithms. We show novel quantum time-space tradeoffs, which we obtain by adjusting the parameters of these algorithms and combining them with "quantized" classical strategies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02234v1
- Title: Explicit constructions of mutually unbiased bases via Hadamard matrices
- Authors: Jean-Christophe Pain
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2604.02234v1  pdf=https://arxiv.org/pdf/2604.02234v1.pdf

Abstract:
We present a detailed computational and algebraic study of Mutually Unbiased Bases (MUBs) in finite-dimensional Hilbert spaces, with a particular focus on dimensions 2, 3, 4, and the challenging case of 6. Starting from the Hadamard-phase parametrization, we derive explicit analytical conditions for mutual unbiasedness in dimension 4, providing a tractable system of trigonometric constraints on the phase parameters. We then explore a tensor-product construction via Pauli operators, highlighting the algebraic and group-theoretical origin of MUBs in two-qubit systems, and demonstrating how these constructions yield a complete set of 5 MUBs in dimension 4. Extending our approach, we investigate the Fourier-family method in dimension 6, where the absence of a prime-power structure imposes strong rigidity constraints and limits the known constructions to sets of 3 MUBs. We provide a systematic computational framework for testing candidate phase vectors, bridging the gap between analytical insight and numerical exploration. Finally, we generalize the discussion to arbitrary prime-power dimensions, emphasizing the role of finite-field structures, Heisenberg-Weyl operators, and discrete symmetries in generating complete sets of MUBs. Our work offers a transparent, line-by-line verification methodology, highlighting both the geometric and algebraic richness of MUBs, and clarifying why certain dimensions resist full analytical constructions. This study serves as a comprehensive resource for researchers seeking both theoretical understanding and practical construction of MUBs in quantum information science.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02301v1
- Title: Lemniscate phase trajectories for high-fidelity GHZ state preparation in trapped-ion chains
- Authors: Evgeny V. Anikin, Andrey Chuchalin, Dimitrii Donchenko, Olga Lakhmanskaya, Kirill Lakhmanskiy
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02301v1  pdf=https://arxiv.org/pdf/2604.02301v1.pdf

Abstract:
In trapped-ion chains, multipartite GHZ states can be prepared natively with the help of a single bichromatic laser pulse. However, higher-order terms in the expansion in the Lamb-Dicke parameter $η$ limit the GHZ state preparation infidelity for rectangular and bell-like pulses to the order of $η^4$. For tens of ions, the infidelity caused by out-of-Lamb-Dicke effects can reach several percents. We propose an amplitude and phase-modulated pulse shape, an "echoed lemniscate pulse", which cancels this contribution into error in the leading order. For the proposed pulse, the infidelity scales as $η^6$. The improved scaling is achieved because of a special phase trajectory of a collective motional mode following the figure-eight curve (lemniscate). We demonstrate that the lemniscate pulse allows achieving lower infidelity than bell-like pulses, which can be as low as $10^{-4}$ for $20$-ion chains.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02311v1
- Title: Space-Efficient Quantum Algorithm for Elliptic Curve Discrete Logarithms with Resource Estimation
- Authors: Han Luo, Ziyi Yang, Ziruo Wang, Yuexin Su, Tongyang Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02311v1  pdf=https://arxiv.org/pdf/2604.02311v1.pdf

Abstract:
Solving the Elliptic Curve Discrete Logarithm Problem (ECDLP) is critical for evaluating the quantum security of widely deployed elliptic-curve cryptosystems. Consequently, minimizing the number of logical qubits required to execute this algorithm is a key object. In implementations of Shor's algorithm, the space complexity is largely dictated by the modular inversion operation during point addition. Starting from the extended Euclidean algorithm (EEA), we refine the register-sharing method of Proos and Zalka and propose a space-efficient reversible modular inversion algorithm. We use length registers together with location-controlled arithmetic to store the intermediate variables in a compact form throughout the computation. We then optimize the stepwise update rules and give concrete circuit constructions for the resulting controlled arithmetic components. This leads to a modular inversion circuit that uses $3n + 4\lfloor \log_2 n \rfloor + O(1)$ logical qubits and $204n^2\log_2 n + O(n^2)$ Toffoli gates. By inserting this modular inversion component into the controlled affine point-addition circuit, we obtain a space-efficient algorithm for the ECDLP with $5n + 4\lfloor \log_2 n \rfloor + O(1)$ qubits and $O(n^3)$ Toffoli gates. In particular, for a 256-bit prime-field curve, our estimate reduces the logical-qubit count to 1333, compared with 2124 in the previous low-width implementation of Häner et al.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02314v1
- Title: Towards High-Brightness Perfect Photon Blockade
- Authors: Zhi-Guang Lu, Xin-You Lü
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02314v1  pdf=https://arxiv.org/pdf/2604.02314v1.pdf

Abstract:
Single-photon sources with high single-photon purity and high brightness are key elements of many future quantum technologies. While photon blockade (PB) is widely exploited in the development of such sources, achieving the coexistence of high purity and high brightness remains a long-standing challenge. Here, we identify a novel mechanism for high-brightness PB and demonstrate that near-ideal purity and near-ideal brightness can be simultaneously achieved in an extended nondegenerate two-photon Jaynes-Cummings model with two-body and three-body interactions. This mechanism is underpinned by a distinctive energy-level structure arising from the combined action of the two interactions. The energy levels in the multi-excitation manifold essentially retain a harmonic ladder of degenerate doublets, whereas in the single-excitation subspace the doublet degeneracy is lifted, with a finite splitting between the two levels. Consequently, when one bosonic mode is driven by a coherent continuous-wave pump, the former degeneracy enables the other bosonic mode to exhibit near-perfect PB even in the strong driving regime, while the latter splitting allows the mean photon number of that mode to approach unity. Our proposed scheme overcomes the outstanding challenge and offers a promising pathway toward realizing ideal single-photon sources.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01285v1
- Title: Temperature and integrability-breaking correspondence via adiabatic transformations
- Authors: Hyeongjin Kim, Souvik Bandyopadhyay, Anatoli Polkovnikov
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; nlin.CD; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01285v1  pdf=https://arxiv.org/pdf/2604.01285v1.pdf

Abstract:
We reveal a correspondence between temperature and integrability-breaking in classical and quantum many-body systems through the lens of geometry and adiabatic transformations. Decreasing the temperature, obtained in a standard way through the derivative of entropy with respect to energy, steers the system towards an integrable point despite strong integrability-breaking interactions. Auto-correlation functions of local observables exhibit slow relaxation dynamics, which violates ergodicity on the approach to this integrable point. Subsequently, the average fidelity susceptibility of stationary states satisfies scaling relations near the integrable point, in close analogy with continuous phase transitions. We further find that the dynamical exponent encompassing relaxation can be different in the quantum and classical models, depending on dimension of the systems. Collectively, our results establish temperature as a tunable control parameter for chaos and puts it on equal footing with integrability-breaking perturbations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01291v1
- Title: Dissipative Floquet engineering of gapped many-body phases using thermal baths
- Authors: Lorenz Wanckel, André Eckardt
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01291v1  pdf=https://arxiv.org/pdf/2604.01291v1.pdf

Abstract:
Floquet engineering, the control of a quantum system by means of time-periodic driving, allows to modify the properties of the system so that it becomes described by an approximate effective time-independent Hamiltonian. However, in the presence of interactions the stabilization of interesting many-body ground states of such effective Hamiltonians is possible only on a certain time scale, beyond which Floquet heating sets in, as it results from unwanted driving induced resonant excitation. Moreover, already the preparation of such states is challenged by excitations due to imperfect adiabatic dynamics, especially when a phase transition has to be passed. Here, we propose a general dissipative strategy for the preparation and stabilization of effective ground states that are protected by an energy gap. Our approach relies on coupling the driven system to a thermal bath, the properties of which are chosen so that it both suppresses Floquet heating and guides the system into a non-equilibrium steady state with a large occupation of the effective ground-state, but generally non-thermal occupations of excited states of the effective Hamiltonian. We use the Floquet-Born-Markov master equation to verify the proposed strategy for the example of a strongly driven Bose-Hubbard chain with an effective gapped Mott-insulator ground state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01320v1
- Title: Solving Lévy Sachdev-Ye-Kitaev Model
- Authors: Budhaditya Bhattacharjee, William. E. Salazar, Alexei Andreanov, Dario Rosa
- Categories: hep-th (primary); hep-th; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01320v1  pdf=https://arxiv.org/pdf/2604.01320v1.pdf

Abstract:
We present an exact solution in the large-$N$ limit of the Lévy Sachdev-Ye-Kitaev (LSYK) model introduced in Ref. [1], wherein the couplings are drawn from a Lévy Stable distribution parameterized by a tail exponent $μ\in [0, 2]$. Starting from the Hamiltonian and its associated partition function, we highlight the key differences from the standard Gaussian SYK model and derive the large-$N$ Schwinger-Dyson equations via a bosonic oscillator representation of the action. These equations are solved both numerically and analytically in the large-$q$ and infrared limits. We subsequently analyze the chaotic properties of the model by computing the Krylov exponent from the large-$q$ Green's function and extracting the Lyapunov exponent from the $4$-point function. The parameter $μ$ continuously interpolates between a free theory at $μ= 0$ and the conventional, maximally chaotic Gaussian SYK model at $μ= 2$, with non-maximal chaos persisting throughout the intermediate regime $0 < μ< 2$. Thermodynamic quantities, including the entropy, free energy, average energy, and specific heat capacity, are computed and compared with their Gaussian SYK counterparts. The interpretations of the thermodynamics are discussed with respect to the holographic dual and non-Fermi liquid theory. Finally, we discuss an alternative representation of the LSYK model based on a distinct decomposition of the Lévy Stable distribution, which establishes a non-trivial connection to Gaussian SYK, and provide supporting analytical and numerical results in the appendices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01367v1
- Title: Approximating the Permanent of a Random Matrix with Polynomially Small Mean: Zeros and Universality
- Authors: Frederic Koehler, Pui Kuen Leung
- Categories: cs.DS (primary); cs.DS; math-ph; math.PR; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01367v1  pdf=https://arxiv.org/pdf/2604.01367v1.pdf

Abstract:
We study algorithms for approximating the permanent of a random matrix when the entries are slightly biased away from zero. This question is motivated by the goal of understanding the classical complexity of linear optics and \emph{boson sampling} (Aaronson and Arkhipov '11; Eldar and Mehraban '17). Barvinok's interpolation method enables efficient approximation of the permanent, provided one can establish a sufficiently large zero-free region for the polynomial $\mathrm{per}(zJ + W)$, where $J$ is the all-ones matrix and $W$ is a random matrix with independent mean-zero entries.   We show that when the entries of $W$ are standard complex Gaussians, all zeros of the random polynomial $\mathrm{per}(zJ + W)$ lie within a disk of radius $\tilde{O}(n^{-1/3})$, which yields an approximation algorithm when the bias of the entries is $\tildeΩ(n^{-1/3})$. Previously, there were no efficient algorithms at biases smaller than $1/\mathrm{polylog}(n)$, and it was unknown whether there typically exist zeros $z$ with $|z| \ge 1$. As a complementary result, we show that the bulk of the zeros, namely $(1 - ε)n$ of them, have magnitude $Θ(n^{-1/2})$. This prevents our interpolation method from contradicting the conjectured average-case hardness of approximating the permanent. We also establish analogous zero-free regions for the hardcore model on general graphs with complex vertex fugacities. In addition, we prove universality results establishing zero-free regions for random matrices $W$ with i.i.d. subexponential entries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01739v1
- Title: Goos-Hänchen Shift in $\mathcal{PT}$-Symmetric and Passive Cavity Optomechanical Systems
- Authors: Shah Fahad, Gao Xianlong
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01739v1  pdf=https://arxiv.org/pdf/2604.01739v1.pdf

Abstract:
We theoretically investigate the control of the Goos-Hänchen shift (GHS) of a reflected weak probe field in both parity-time ($\mathcal{PT}$)-symmetric and conventional optomechanical systems. The proposed scheme consists of a single optomechanical platform where a passive optical cavity is coupled to an active mechanical resonator, in contrast to standard passive-passive configurations. Analysis of the eigenfrequency spectrum reveals the emergence of an exceptional point under balanced gain-loss conditions at a tunable effective optomechanical coupling strength. Using the transfer-matrix method combined with stationary-phase analysis, we examine the GHS across broken and unbroken $\mathcal{PT}$ phases and compare it with that in the conventional system. The lateral shift exhibits strong phase dependence: it is markedly enhanced in the unbroken regime relative to both the broken phase and the passive configuration. We further show that the GHS can be actively tuned through the cavity detuning and the intracavity medium length. These results provide a controlled means for manipulating beam shifts in optomechanical systems and suggest pathways toward tunable photonic components and precision optical sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01876v1
- Title: Topology-Hiding Connectivity-Assurance for QKD Inter-Networking
- Authors: Margherita Cozzolino, Stephan Krenn, Thomas Lorünser
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01876v1  pdf=https://arxiv.org/pdf/2604.01876v1.pdf

Abstract:
While QKD ensures information-theoretic security at the link level, real-world deployments depend on trusted repeaters, creating potential vulnerabilities. In this paper, we thus introduce a topology-hiding connectivity assurance protocol to enhance trust in quantum key distribution (QKD) network infrastructures. Our protocol allows network providers to jointly prove the existence of a secure connection between endpoints without revealing internal topology details. By extending graph-signature techniques to support multi-graphs and hidden endpoints, we enable zero-knowledge proofs of connectivity that ensure both soundness and topology hiding. We further discuss how our approach can certify, e.g., multiple disjoint paths, supporting multi-path QKD scenarios. This work bridges cryptographic assurance methods with the operational requirements of QKD networks, promoting verifiable and privacy-preserving inter-network connectivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01906v1
- Title: Collective quantum tunneling with time-dependent generator coordinate method
- Authors: Wenmin Deng, Guangping Chen, Ganlong Ding, Sibo Wang, Jing Peng, Haozhao Liang
- Categories: nucl-th (primary); nucl-th; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01906v1  pdf=https://arxiv.org/pdf/2604.01906v1.pdf

Abstract:
Inspired by the work of McGlynn and Simenel [Phys. Rev. C {\bf 102}, 064614 (2020)], this study investigates the quantum tunneling of two interacting distinguishable particles in two potential wells. We first benchmark the system by reproducing key established results: the exact quantum solution and the spurious self-trapping effect that arises in the real-time mean-field dynamics for strong interactions. To exactly capture the tunneling dynamics, we apply the time-dependent generator coordinate method (TDGCM) to the model. Numerical simulations demonstrate that the TDGCM, by utilizing the real-time mean-field states as generator states, successfully overcomes the self-trapping effect, yielding tunneling dynamics in excellent agreement with the exact solution. Furthermore, we explore the expectation values of the generator coordinates from the correlated TDGCM many-body wave function. While different methods for calculating expectation values show consistent results in some cases, significant discrepancies are observed in others, providing critical insights into the emergence of collective and single-particle behaviors in interacting systems. This work also verifies the TDGCM as a robust framework for describing collective quantum tunneling and opens avenues for its application to more complex and realistic systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01910v1
- Title: Quantum Networking Fundamentals: From Physical Protocols to Network Engineering
- Authors: Athanasios Gkelias, Felix T. A. Burt, Kin K. Leung
- Categories: cs.NI (primary); cs.NI; eess.SY; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01910v1  pdf=https://arxiv.org/pdf/2604.01910v1.pdf

Abstract:
The realization of the Quantum Internet promises transformative capabilities in secure communication, distributed quantum computing, and high-precision metrology. However, transitioning from laboratory experiments to a scalable, multi-tenant network utility introduces deep orchestration challenges. Current development is often siloed within physics communities, prioritizing hardware, while the classical networking community lacks architectural models to manage fragile quantum resources. This tutorial bridges this divide by providing a network-centric view of quantum networking. We dismantle idealized assumptions in current simulators to address the "simulation-reality gap," recasting them as explicit control-plane constraints. To bridge this gap, we establish Software-Defined Quantum Networking (SDQN) as a prerequisite for scale, prioritizing a symbiotic, dual-plane architecture where classical control dictates quantum data flow. Specifically, we synthesize reference models for SDQN and the Quantum Network Operating System (QNOS) for hardware abstraction, and adapt a Quantum Network Utility Maximization (Q-NUM) framework as a unifying mathematical lens for engineers to reason about trade-offs between entanglement routing, scheduling, and fidelity. Furthermore, we analyze Distributed Quantum AI (DQAI) over imperfect networks as a case study, illustrating how physical constraints such as probabilistic stragglers and decoherence dictate application-layer viability. Ultimately, this tutorial equips network engineers with the tools required to transition quantum networking from a bespoke physics experiment into a programmable, multi-tenant global infrastructure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.01975v1
- Title: Efficient generation and explicit dimensionality of Lie group-equivariant and permutation-invariant bases
- Authors: Eloïse Barthelemy, Geneviève Dusson, Camille Hernandez, Liwei Zhang
- Categories: math.NA (primary); math.NA; quant-ph
- Links: abs=https://arxiv.org/abs/2604.01975v1  pdf=https://arxiv.org/pdf/2604.01975v1.pdf

Abstract:
In this article, we propose a practical construction of Lie group-equivariant and permutation-invariant functions of $N$ variables from the knowledge of a one-particle basis that is stable with respect to the group action. The construction is generic for any linear Lie group and relies on building a matrix constructed from the Lie algebra whose kernel is spanned by a group-equivariant and permutation-invariant basis. In particular, this construction does not require the knowledge of Clebsch--Gordan coefficients and instead directly builds generalized Clebsch--Gordan coefficients. For specific groups such as $SO(3)$ and $SU(2)$, we exploit the Lie algebra structure to simplify the matrix, which then allows us to derive an explicit formula for the exact dimension of the group-equivariant and permutation-invariant space. Numerical simulations are provided to show that the proposed method scales linearly instead of exponentially for existing methods in the literature. We also show that for large values of $N$, the number of rotation-equivariant and permutation-invariant basis functions is of a comparable order as the number of permutation-invariant basis functions, while pre-asymptotically, a large gain can be achieved by explicitly enforcing rotation-equivariance on top of permutation-invariance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02054v1
- Title: Efficient Auxiliary-Field Quantum Monte Carlo using Isometric Tensor Hypercontraction
- Authors: Maxine Luo, Victor Chen, Yu Wang, Christian B. Mendl
- Categories: physics.chem-ph (primary); physics.chem-ph; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2604.02054v1  pdf=https://arxiv.org/pdf/2604.02054v1.pdf

Abstract:
Auxiliary Field Quantum Monte Carlo (AFQMC) has emerged as a powerful framework for treating strongly correlated electronic systems, offering a favorable balance between computational cost and accuracy. In this paper, we present a novel AFQMC method that uses the isometric tensor hypercontraction (ITHC) technique to diagonalize the two-body Coulomb interaction of molecular electronic Hamiltonians by introducing additional fictitious fermionic modes. Our method shows reduced theoretical complexity and better practical performance for both propagation and local energy evaluation compared to the standard AFQMC method. We demonstrate the efficacy of this approach by computing the ground-state energies of a linear $\ce{H10}$-chain and the benzene molecule. Our results show that the extended-basis AFQMC recovers many-body correlations with a precision comparable to that of high-level wavefunction methods such as Coupled Clusters (CC) or Density Matrix Renormalization Group (DMRG), while offering significantly improved scaling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02062v1
- Title: Ultrafast Ionization Dynamics Encoded in a Photoelectron Spin Torus
- Authors: Xiaodan Mao, Feng He, Pei-Lun He
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2604.02062v1  pdf=https://arxiv.org/pdf/2604.02062v1.pdf

Abstract:
We demonstrate that strong-field ionization of atoms in circularly polarized laser fields generates a photoelectron spin texture with toroidal topology in momentum space. Using time-dependent Schrödinger equation simulations, spin-resolved classical-trajectory Monte Carlo calculations, and an extended spin-resolved strong-field approximation including intermediate excitation pathways, we show that the rotation angle of this spin torus provides access to attosecond relative time delays associated with photoelectron wave packets released by tunneling from the counter-rotating and co-rotating \(p\)-orbital channels. When intermediate-state dynamics become significant, the torus develops a clear splitting. These results establish photoelectron spin textures as a complementary source of dynamical information beyond conventional momentum spectroscopy, and identify spin polarization as a robust internal degree of freedom for self-referenced attosecond metrology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02075v1
- Title: Emergence of volume-law scaling for entanglement negativity from the Hawking radiation of analogue black holes
- Authors: S. Mahesh Chandran, Uwe R. Fischer
- Categories: gr-qc (primary); gr-qc; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2604.02075v1  pdf=https://arxiv.org/pdf/2604.02075v1.pdf

Abstract:
The quantum information content of Hawking radiation holds the key to understanding black-hole evaporation and the fate of unitarity. Motivated by recent advances in cold-atom experiments, we develop a lattice-regularization approach aimed at simulating the coarse-grained entanglement scaling of a quantum field in a 1+1D analogue black-hole background. We provide the first concrete demonstration that logarithmic negativity -- an entanglement monotone that typically exhibits a UV-divergent log-scaling for the conformal vacuum -- acquires a UV-finite volume term from the nonlocal correlations seeded by Hawking radiation. We show that this volume term encodes both the number density and spatial distribution of entangled Hawking pairs along the black-hole interior and exterior. We highlight its prospective detection in currently realizable experiments as well as its implications beyond the analogue paradigm, in particular for black-hole thermodynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02269v1
- Title: Tensor invariants for multipartite entanglement classification
- Authors: Sylvain Carrozza, Johann Chevrier, Luca Lionni
- Categories: math-ph (primary); math-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2604.02269v1  pdf=https://arxiv.org/pdf/2604.02269v1.pdf

Abstract:
Organising the space of entanglement structures of a multipartite quantum system is a much more challenging task than its bipartite version: while the local unitary (LU) orbit of a bipartite pure state can be conveniently characterized by its entanglement spectrum, invariants of multipartite entanglement structures are comparatively difficult to define and work with. The root cause of this difference is that the bipartite problem can be reduced to the analysis of matrix invariants, while its multipartite version is governed by a much richer space of tensor invariants. The present work explores the latter through the lens of so-called trace-invariants, which are in one-to-one correspondence with combinatorial objects known as colored graphs. We first explain why trace-invariant evaluations can serve as labels of LU-orbits of multipartite pure states, how this strategy extends to random states, and how the effect of local operations (LO) can be analyzed through such data. We then focus on entanglement classification within an (infinite-dimensional) subspace of reference states, whose basic building blocks are GHZ states of various dimensions. We show that relatively simple subclasses of trace-invariants are sufficient to separate the LU-orbits of reference states, and enable a complete (resp. an incomplete) characterization of their relations in the LO (resp. LOCC) resource theory of entanglement. Finally, we investigate how a (still infinite) subclass of reference states of local dimension N can be efficiently distinguished at leading and subleading orders in an asymptotic large-N expansion (among themselves, or from Haar-random states). This analysis relies crucially on combinatorial quantities associated to colored graphs, some of which have already played instrumental roles in the recent literature on random tensors. Results of broader relevance are reported along the way.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02297v1
- Title: Commutator Estimates for Low-Temperature Fermi Gases
- Authors: Jacky J. Chong, Laurent Lafleche, Jinyeop Lee, Chiara Saffirio
- Categories: math-ph (primary); math-ph; math.AP; math.SP; quant-ph
- Links: abs=https://arxiv.org/abs/2604.02297v1  pdf=https://arxiv.org/pdf/2604.02297v1.pdf

Abstract:
We investigate the semiclassical regularity of thermal equilibria in the presence of a harmonic potential at low temperature; that is, we obtain the asymptotic behavior of the Schatten norms of commutators of the one-body operators associated with these equilibria and the position and momentum operators. We also obtain upper bounds in the magnetic field case for the Fock-Darwin Hamiltonian. Our estimates, in particular, allow us to observe several regimes depending on the joint behavior of the Planck constant, the temperature, and the strength of the magnetic field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.02321v1
- Title: Robust Correlation-Induced Localization Under Time-Reversal Symmetry Breaking
- Authors: Bikram Pain, Sthitadhi Roy, Jens H. Bardarson, Ivan M. Khaymovich
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2604.02321v1  pdf=https://arxiv.org/pdf/2604.02321v1.pdf

Abstract:
We study Anderson localization in a one-dimensional disordered system with long-range correlated hopping decaying as $1/r^{a}$ with complex hopping amplitudes that break time-reversal symmetry in a tunable fashion by varying their argument. We find analytically a corelation-induced algebraic localization that is robust to a finite strength of the time-reversal-symmetry-breaking parameter, beyond which all states delocalize. This establishes a localization--delocalization transition driven by the interplay between long-ranged correlated hopping and time-reversal symmetry breaking. In addition to obtaining the static localization phase diagram, we also investigate the dynamical phase diagram through the lens of wavepacket spreading. We find that the growth in time of the mean-squared displacement of a wavepacket, which is subdiffusive for the time-reversal symmetric case, becomes diffusive for any finite value of the time-reversal-symmetry-breaking parameter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2406.11994v3
- Title: Witnessing network steerability of every bipartite entangled state without inputs
- Authors: Shubhayan Sarkar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2406.11994v3  pdf=https://arxiv.org/pdf/2406.11994v3.pdf

Abstract:
Quantum steering is an asymmetric form of quantum nonlocality where one can detect whether a measurement on one system can steer or change another distant system. It is well-known that there are quantum states that are entangled but unsteerable in the standard quantum steering scenario. Consequently, a long-standing open problem in this regard is whether the steerability of every entangled state can be activated in some way. In this work, we consider quantum networks and focus on the swap-steering scenario without inputs and find linear witnesses of network steerability corresponding to any negative partial transpose (NPT) bipartite state and a large class of bipartite states that violate the computable cross-norm (CCN) criterion. Furthermore, by considering that the trusted party can perform tomography of the incoming subsystems, we construct linear inequalities to witness swap-steerability of every bipartite entangled state. Consequently, for every bipartite entangled state one can now observe a form of quantum steering.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2502.11553v2
- Title: Multiband dispersion and warped vortices of strongly-interacting photons
- Authors: Bankim Chandra Das, Dmytro Kiselov, Lee Drori, Ariel Nakav, Alexander Poddubny, Ofer Firstenberg
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2502.11553v2  pdf=https://arxiv.org/pdf/2502.11553v2.pdf

Abstract:
We present a theoretical study of quantum correlations between interacting photons realized through co-propagating Rydberg polaritons. We show that the spatial evolution of the $n$-photon wavefunction is governed by a multiband dispersion featuring one massive mode and multiple massless modes with degenerate Dirac points and $n$-fold rotational symmetry. The resulting band structure is warped, departing from the single-band, parabolic approximation commonly assumed for interacting polaritons. Our analytical results are supported by rigorous numerical modeling that fully accounts for photon propagation inside the finite atomic medium. These findings advance the understanding of multi-photon interactions and support the development of future multi-photon control tools.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2502.11784v2
- Title: Structure, Positivity and Classical Simulability of Kirkwood-Dirac Distributions
- Authors: Jędrzej Burkat, Sergii Strelchuk
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2502.11784v2  pdf=https://arxiv.org/pdf/2502.11784v2.pdf

Abstract:
The Kirkwood-Dirac (KD) quasiprobability distribution is known for its role in quantum metrology, thermodynamics, as well as quantum foundations. In this work we classify unitary evolutions that preserve KD positivity. We identify conditions under which positivity preservation is equivalent to $l_1$-norm preservation, and exhibit unitaries that preserve positivity on KD-positive distributions while failing to preserve the $l_1$-norm of non-positive ones. We further prove that unitaries inducing stochastic updates of KD quasiprobabilities form a strict subset of the positivity-preserving unitaries. By adapting the classical sampling algorithm of Pashayan et al. [Phys. Rev. Lett. 115, 070501], we obtain efficient simulation methods for all identified classes of positivity-preserving unitaries. Our classification is complete for distributions defined on Fourier-conjugate bases in dimensions $d = p^k$ and $d = pq$, where $p, q$ are distinct primes, as well as for generic randomly chosen bases. As a consequence, no resource theory in the Fourier-conjugate $d=pq$ setting can simultaneously regard KD non-positivity as a monotone and include all efficiently simulable positivity-preserving unitaries among its free operations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2503.13599v3
- Title: Stabilizer Rényi Entropy and Conformal Field Theory
- Authors: Masahiro Hoshino, Masaki Oshikawa, Yuto Ashida
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2503.13599v3  pdf=https://arxiv.org/pdf/2503.13599v3.pdf

Abstract:
Understanding universal aspects of many-body systems is one of the central themes in modern physics. Recently, the stabilizer Rényi entropy (SRE) has emerged as a computationally tractable measure of nonstabilizerness, a crucial resource for fault-tolerant universal quantum computation. While numerical results suggested that the SRE in critical states can exhibit universal behavior, its comprehensive theoretical understanding has remained elusive. In this work, we develop a field-theoretical framework for the SRE in a $(1+1)$-dimensional many-body system and elucidate its universal aspects using boundary conformal field theory. We demonstrate that the SRE is equivalent to a participation entropy in the Bell basis of a doubled Hilbert space, which can be calculated from the partition function of a replicated field theory with the interlayer line defect created by the Bell-state measurements. This identification allows us to characterize the universal contributions to the SRE on the basis of the data of conformal boundary conditions imposed on the replicated theory. We find that the SRE of the entire system contains a universal size-independent term determined by the noninteger ground-state degeneracy known as the g-factor. In contrast, we show that the mutual SRE exhibits the logarithmic scaling with a universal coefficient given by the scaling dimension of a boundary condition changing operator, which elucidates the origin of universality previously observed in numerical results. As a concrete demonstration, we present a detailed analysis of the Ising criticality, where we analytically derive the universal quantities at arbitrary Rényi indices and numerically validate them with high accuracy by employing tensor network methods. These results establish a field-theoretical approach to understanding the universal features of nonstabilizerness in quantum many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2505.09563v2
- Title: Trace Estimation of Quantum State Powers: Sample Complexity and Computational Hardness
- Authors: Kean Chen, Yupan Liu, Qisheng Wang
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2505.09563v2  pdf=https://arxiv.org/pdf/2505.09563v2.pdf

Abstract:
As often emerges in various basic quantum properties such as Rényi and Tsallis entropies, the trace of quantum state powers $\text{tr}(ρ^q)$ has attracted a lot of attention. The recent work of Liu and Wang (SODA 2025) showed that, even for (possibly) non-integer $q>1$, $\text{tr}(ρ^q)$ can be estimated to within additive error $ε$ using a dimension-independent (and also rank-independent) sample complexity of $\widetilde O(1/ε^{3+\frac2{q-1}})$, together with a lower bound of $Ω(1/ε)$. In addition, combining this result with subsequent work of Liu (STACS 2026) shows that the corresponding promise problem is ${\sf BQP}$-complete. In this paper, we significantly improve and extend the sample complexity bounds for this problem. Furthermore, we show that for $0<q<1$, the problem does not admit an efficient estimator unless ${\sf BQP}={\sf NIQSZK}$, which is considered highly unlikely. In particular, we have the following results.   - For $q>2$, we settle the sample complexity with matching upper and lower bounds $\widetildeΘ(1/ε^2)$.   - For $1<q<2$, we obtain an upper bound of $\widetilde O(1/ε^{\frac2{q-1}})$, with a lower bound of $Ω(1/ε^{\max\{\frac1{q-1},2\}})$ for dimension-independent (in fact, rank-independent) estimators.   - For $0<q<1$, we obtain an upper bound of $O((d/ε)^{\frac2{q}})$, with a lower bound of $Ω((d/ε)^{\frac1{q}})$ for $d$-dimensional states (in fact, both bounds can be naturally refined to depend on the rank rather than the dimension). Accordingly, the corresponding promise problem is ${\sf NIQSZK}$-hard, which is in sharp contrast to the case of $q>1$.   Technically, our upper bounds are obtained by (non-plug-in) quantum estimators based on weak Schur sampling, in sharp contrast to the prior approach based on quantum singular value transformation and samplizer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2506.00685v2
- Title: High-order interactions in quantum optomechanics: fluctuations, dynamics and thermodynamics
- Authors: Alessandro Ferreri, Vincenzo Macrì, Yoshihiko Hasegawa, David Edward Bruschi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.00685v2  pdf=https://arxiv.org/pdf/2506.00685v2.pdf

Abstract:
Quantum optomechanics describes the interaction between a confined field and a fluctuating wall due to radiation pressure. The dynamics of this system is typically understood using perturbation theory up to second order in the small coupling. Improving beyond this regime can shed light onto new phenomena. In this work we study high-order resonant wall-field interactions characterized by two- and three-phonon scattering processes. We obtain the Hamiltonian, compute the perturbed energy spectrum and explicitly calculate corrections to the ground state. Finally, we study the dynamics of the system when second- and third-order resonance conditions are activated, showing that the presence of high-order terms in the Hamiltonian drastically affects the populations of all particles, as well as the entropy production rate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2506.11964v4
- Title: Universal cooling of quantum systems via randomized measurements
- Authors: Josias Langbehn, George Mouloudakis, Emma King, Raphaël Menu, Igor Gornyi, Giovanna Morigi, Yuval Gefen, Christiane P. Koch
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2506.11964v4  pdf=https://arxiv.org/pdf/2506.11964v4.pdf

Abstract:
Designing cooling protocols is believed to require knowledge of the system spectrum. In contrast, cooling in nature occurs whenever the system is coupled to a cold bath. How does nature know how to cool? A natural cold bath can be mimicked with a reservoir of "meter" qubits that are initialized in their ground state. We show that a quantum system can be cooled without knowledge of system details when system-meter interactions and meter splittings are chosen randomly. For sufficiently small interaction strengths and long interaction times, the protocol ensures that resonant energy-exchange processes, leading to cooling, dominate over heating. Effectively, the dynamics is then captured by the rotating-wave approximation, which we identify as the basic mechanism for robust and scalable cooling of complex quantum systems through generic, structure-independent protocols. This offers a versatile universal framework for controlling quantum matter far from equilibrium, in particular, for quantum computing and simulation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2507.10656v2
- Title: Stabilizer Rényi Entropy Encodes Fusion Rules of Topological Defects and Boundaries
- Authors: Masahiro Hoshino, Yuto Ashida
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2507.10656v2  pdf=https://arxiv.org/pdf/2507.10656v2.pdf

Abstract:
We demonstrate that the stabilizer Rényi entropy (SRE), a computable measure of quantum magic, can serve as an information-theoretic probe for universal properties associated with conformal defects in one-dimensional quantum critical systems. Using boundary conformal field theory, we show that open boundaries manifest as a universal logarithmic correction to the SRE, whereas topological defects yield a universal size-independent term. When multiple defects are present, we find that the universal terms in the SRE faithfully reflect the defect-fusion rules that define a noninvertible symmetry algebra. These analytical predictions are corroborated by numerical calculations of the Ising model, where boundaries and topological defects are described by Cardy states and Verlinde lines, respectively.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2507.18708v3
- Title: Average-computation benchmarking for local expectation values in digital quantum devices
- Authors: Flavio Baccari, Pavel Kos, Georgios Styliaris
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2507.18708v3  pdf=https://arxiv.org/pdf/2507.18708v3.pdf

Abstract:
As quantum devices progress towards a quantum advantage regime, they become harder to benchmark. A particularly relevant challenge is to assess the quality of the whole computation, beyond testing the performance of each single operation. Here we introduce a scheme for this task that combines the target computation with variants of it, which, when averaged, allow for classically solvable correlation functions. Importantly, the variants exactly preserve the circuit architecture and depth, without simplifying the gates into a classically-simulable set. The method is based on replacing each gate by an ensemble of similar gates, which when averaged together form space-time channels [P. Kos and G. Styliaris, Quantum 7, 1020 (2023)]. We introduce explicit constructions for ensembles producing such channels, all applicable to arbitrary brickwork circuits, and provide a general recipe to find new ones through semidefinite programming. The resulting average computation retains important information about the original circuit and is able to detect noise beyond a Clifford benchmarking regime. Moreover, we provide evidence that estimating average-computation expectation values requires running only a limited number of different circuit realizations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2508.02772v3
- Title: Energy-Invariant Catalysis of Stable Ergotropy in Strongly Coupled Spin-Chain Quantum Batteries
- Authors: Zi-Yi Peng, Shun-Cai Zhao, Liang Luo, Ni-Ya Zhuang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.02772v3  pdf=https://arxiv.org/pdf/2508.02772v3.pdf

Abstract:
Quantum batteries (QBs) provide a platform for exploring quantum-scale energy storage, yet most existing analyses rely on weak-coupling and Markovian approximations. In realistic implementations operating in strongly coupled non-Markovian regimes, environmental memory effects induce pronounced oscillations of the maximum extractable work (ergotropy), hindering stable energy output. Here, we investigate the stabilization of ergotropy in a spin-chain QB assisted by an energy-invariant catalyst, namely an auxiliary subsystem whose average energy remains unchanged during the evolution. The dynamics are described by a Nakajima-Zwanzig master equation with a Gaussian memory kernel, enabling a systematic characterization of non-Markovian effects. Our results show that the memory-kernel parameters, the spin number, and the characteristic frequencies of both the cavity field and the local excitations jointly regulate the ergotropy dynamics. Compared with the uncatalyzed case, the catalyst effectively reshapes the system energy spectrum, markedly suppresses non-Markovian oscillations, and promotes a quasi-stationary regime of extractable work. These findings provide a practical strategy for stabilizing energy flows in strongly coupled open quantum systems, offering theoretical guidance for the development of robust quantum energy devices and contributing to ongoing research in quantum thermodynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2509.21804v3
- Title: Towards reconstructing quantum structured light on a quantum computer
- Authors: Mwezi Koni, Shawal Kassim, Paola C. Obando, Neelan Gounden, Isaac Nape
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.21804v3  pdf=https://arxiv.org/pdf/2509.21804v3.pdf

Abstract:
We introduce a variational quantum computing approach for quantum state reconstruction within a discretized logical framework, using experimental measurement data as input. By mapping the reconstruction cost function onto an Ising model, the problem can be solved using a variational eigensolver on present-day quantum hardware identifying dominant logical elements of the density matrix. As a proof of concept, we demonstrate the method on quantum structured light, in particular, entangled photons carrying orbital angular momentum and show that the reconstruction procedure can yield reliable performance even on noisy devices. Our results highlight the potential of variational algorithms as a complementary approach to quantum state tomography, particularly for high-dimensional structured light, where classical approaches can face bottlenecks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2510.06323v2
- Title: Blind quantum computing with different qudit resource state architectures
- Authors: Alena Romanova, Wolfgang Dür
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.06323v2  pdf=https://arxiv.org/pdf/2510.06323v2.pdf

Abstract:
We discuss how blind quantum computing generalizes to multi-level quantum systems (qudits), which offers advantages compared to the qubit approach. Here, a quantum computing task is delegated to an untrusted server while simultaneously preventing the server from retrieving information about the computation it performs, the input, and the output, enabling secure cloud-based quantum computing. In the standard approach with qubits, measurement-based quantum computing is used: single-qubit measurements on cluster or brickwork states implement the computation, while random rotations of the resource qubits hide the computation from the server. We generalize finite-sized approximately universal gate sets to prime-power-dimensional qudits and show that qudit versions of the cluster and brickwork states enable a similar server-blind execution of quantum algorithms. Furthermore, we compare the overheads of different resource state architectures and discuss which hiding strategies apply to alternative qudit resource states beyond graph states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2510.10629v4
- Title: Liouvillian Exceptional Points in Quantum Brickwork Circuits
- Authors: Vladislav Popkov, Mario Salerno
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.10629v4  pdf=https://arxiv.org/pdf/2510.10629v4.pdf

Abstract:
We demonstrate that Liouvillian exceptional points (LEPs), previously explored only in continuous Lindbladian dynamics, also emerge in discrete brickwork completely positive trace-preserving (CPTP) circuits. By analytically solving a minimal two-qubit brickwork model, we identify the conditions under which discrete-time LEPs arise and show that they retain the hallmark square-root eigenvalue splitting and linear-in-time sensitivity enhancement. These results establish a direct bridge between continuous non-Hermitian physics and discrete quantum-circuit architectures, opening a path toward the realization of exceptional-point-based sensing on near-term quantum processors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2511.09204v2
- Title: Resource-Efficient Variational Quantum Classifier
- Authors: Petr Ptáček, Paulina Lewandowska, Ryszard Kukulski
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2511.09204v2  pdf=https://arxiv.org/pdf/2511.09204v2.pdf

Abstract:
We introduce the unambiguous quantum classifier based on Hamming distance measurements combined with classical post-processing. The proposed approach improves classification performance through a more effective use of ansatz expressivity, while requiring significantly fewer circuit evaluations. Moreover, the method demonstrates enhanced robustness to noise, which is crucial for near-term quantum devices. We evaluate the proposed method on a breast cancer classification dataset. The unambiguous classifier achieves an average accuracy of 90%, corresponding to an improvement of 6.9 percentage points over the baseline, while requiring eight times fewer circuit executions per prediction. In the presence of noise, the improvement is reduced to approximately 3.1 percentage points, with the same reduction in execution cost. We substantiate our experimental results with theoretical evidence supporting the practical performance of the approach.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2512.20881v2
- Title: Heralded Linear Optical Generation of Dicke States
- Authors: Minhyeok Kang, Jaehee Kim, William J. Munro, Seungbeom Chin, Joonsuk Huh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.20881v2  pdf=https://arxiv.org/pdf/2512.20881v2.pdf

Abstract:
Entanglement is a fundamental feature of quantum mechanics and a key resource for quantum information processing. Among multipartite entangled states, Dicke states $|D_n^k\rangle$ are distinguished by their permutation symmetry, which provides robustness against particle loss and enables applications for quantum communication and computation. Although Dicke states have been realized in various platforms, most optical implementations rely on postselection, which destroys the state upon detection and prevents its further use. A heralded optical scheme is therefore highly desirable. Here, we present a linear-optical heralded scheme for generating arbitrary Dicke states $|D_n^k\rangle$ with $3n+k$ photons through the framework of the linear quantum graph (LQG) picture. By mapping the scheme design into the graph-finding problem, and exploiting the permutation symmetry of Dicke states, we overcome the structural complexity that has hindered previous approaches. Our results provide a resource-efficient pathway toward practical heralded preparation of Dicke states for quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2603.24377v2
- Title: Fluctuation-induced symmetry breaking in high harmonic generation for bicircular quantum light
- Authors: Philipp Stammer, Camilo Granados, Javier Rivera-Dean
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2603.24377v2  pdf=https://arxiv.org/pdf/2603.24377v2.pdf

Abstract:
Symmetries are ubiquitous in physics and play a pivotal role in light-matter interactions, where they determine the selection rules governing allowed atomic transitions and define the associated conserved quantities. For the up-conversion process of high harmonic generation, the symmetries of the driving field determine the allowed frequencies and the polarization properties of the resulting harmonics. As a consequence, it is possible to establish classical selection rules when the process is driven by coherent radiation. In this work, we show that fluctuation-induced symmetry breaking in the driving field leads to the appearance of otherwise forbidden harmonics. This is achieved by considering bicircular quantum light, and demonstrate that the enhanced quantum fluctuations due to squeezing in the driving field break the classical selection rules. To this end, we develop a quantum optical description of the dynamical symmetries in the process of high harmonic generation, revealing corrections to the classical selection rules. Moreover, we show that the new harmonics show squeezing-like signatures in their photon statistics, allowing them to be clearly distinguished from classical thermal fluctuations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2603.24588v2
- Title: Finite-Degree Quantum LDPC Codes Reaching the Gilbert-Varshamov Bound
- Authors: Kenta Kasai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2603.24588v2  pdf=https://arxiv.org/pdf/2603.24588v2.pdf

Abstract:
We construct asymptotically good nested Calderbank-Shor-Steane (CSS) code pairs from Hsu-Anastasopoulos codes and MacKay-Neal codes. In the fixed-degree regime, we prove that the coding rate stays bounded away from zero and that the relative distances on both sides stay bounded away from zero with probability tending to one as the blocklength grows. Moreover, within an explicit low-degree search window, we determine exactly which even regular degree choices in our construction attain the classical Gilbert-Varshamov (GV) bound on both constituent sides, and consequently the CSS GV bound at fixed finite degree.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.00118v2
- Title: When level repulsion fails: non-normality and chaos in open quantum systems
- Authors: Caio B. Naves, Thomas Klein Kvorning, Jonas Larson
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.00118v2  pdf=https://arxiv.org/pdf/2604.00118v2.pdf

Abstract:
For Hamiltonian systems, level statistics provide a faithful diagnostic of quantum chaos. By analogy, the statistics of the Lindbladian spectrum are often used in open quantum systems, and the Grobe-Haake-Sommers conjecture proposes that systems with chaotic classical counterparts should exhibit level repulsion in the Lindbladian spectrum. Here we point out an important flaw in this analogy: Hamiltonian and Lindbladian spectra behave differently and have distinct physical interpretations, and one should therefore not expect the latter to provide a reliable diagnostic. For Lindbladians, the late-time dynamics are not determined by the bulk of the eigenvalues but only by those eigenvalues -- and their corresponding eigenvectors -- with small real parts. Combined with the strong non-normality typical of Lindbladians, this allows situations in which the level statistics can be tuned almost arbitrarily without affecting the dynamics on either short or long time scales. We explicitly demonstrate this phenomenon and provide examples in which Ginibre level repulsion arises while the system dynamics at no time show signatures of chaos. We further relate this mechanism to the emergence of a non-Hermitian skin effect in Liouville space, linking boundary-induced eigenvector localization to the observed spectral instability. Our results show that level statistics cannot universally serve as a reliable diagnostic of quantum chaos in open quantum systems and highlight the need for alternative diagnostics that remain robust in strongly non-normal regimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.00272v2
- Title: Quantum Non-Moduler Multiplication with QFT-Based Multi Input Parallelized Adder
- Authors: Murat Kurtand Selçuk Çakmak, Azmi Gençten
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.00272v2  pdf=https://arxiv.org/pdf/2604.00272v2.pdf

Abstract:
In this study, we propose an efficient quantum multiplication approach based on a QFT-assisted parallelized addition scheme. The multiplication stage is implemented using a structure composed entirely of Toffoli gates, which generate partial products. In the second stage, these partial results are accumulated using a QFT-based adder. Unlike conventional QFT-based arithmetic circuits, the proposed design eliminates the repeated application of QFT and inverse QFT (IQFT) operations during intermediate summation processes. This leads to a significant reduction in the total gate count and circuit complexity, enabling a more resource-efficient implementation. To demonstrate the feasibility of the proposed approach, a quantum circuit that performs the multiplication of two 3-bit numbers is designed. The circuit is tested and validated using IBM quantum simulators. The results indicate that the proposed method provides a more efficient alternative to traditional quantum multiplication techniques in terms of gate cost and circuit depth.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2604.00606v2
- Title: Beyond Perturbation Theory: A Resolvent-Based Framework for Strongly Correlated Many-Body Systems
- Authors: Zhi-qiang Huang, Qing-yu Cai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.00606v2  pdf=https://arxiv.org/pdf/2604.00606v2.pdf

Abstract:
Traditional perturbation theory, based on local analyticity (Taylor expansion), often fails in many-body systems with exponentially small energy gaps and strong interactions. This work presents an alternative methodological framework built on two core principles: (1) starting from the pole expansion of the resolvent to directly capture the global analytic structure, and (2) treating local fluctuations statistically (in the spirit of the eigenstate thermalization hypothesis) to close the mean-field equations. Crucially, we go beyond the mean-field level by deriving an exact recursive re-expansion of the cross-correlated terms, which systematically generates higher-order corrections that control the distribution tails, branch splitting, and fluctuations. The framework is realized through a hierarchical ansatz strategy, solving self-consistent equations with Lorentzian, Gaussian, and hybrid forms to describe the bulk, tail, and full distribution, respectively. This methodology does not rely on weak-coupling assumptions and is applicable to the quantitative analysis of global properties such as entropy production and distribution functions in nonintegrable many-body systems. We detail its mathematical structure, the recursive expansion of fluctuations, conditions of validity, comparison with traditional methods, and provide a general implementation workflow.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2503.10761v2
- Title: Quantum teleportation between simulated binary black holes
- Authors: Aiden Daniel, Tanmay Bhore, Jiannis K. Pachos, Chang Liu, Andrew Hallam
- Categories: cond-mat.str-el (primary); cond-mat.str-el; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2503.10761v2  pdf=https://arxiv.org/pdf/2503.10761v2.pdf

Abstract:
The quantum description of a black hole predicts that quantum information hidden behind the event horizon can be teleported outside almost instantaneously. In this work, we demonstrate that a chiral spin-chain model, which naturally simulates a binary black hole system, can realise this teleportation process. Our system captures two essential components of this protocol: Hawking radiation, which generates the necessary entanglement between the black holes, and optimal scrambling, which enables high-fidelity teleportation on short timescales. Through numerical simulations, we quantify the key timescales governing the process, including the Page time, radiation time, scrambling time, and butterfly velocity, showing their universal dependence on the chiral coupling strength. Our results establish the feasibility of simulating quantum properties of black holes within condensed matter systems, offering an experimentally accessible platform for probing otherwise inaccessible high-energy phenomena.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2505.05246v4
- Title: Hamiltonian description of nonreciprocal interactions
- Authors: Yu-Bo Shi, Roderich Moessner, Ricard Alert, Marin Bukov
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.other; cond-mat.quant-gas; cond-mat.soft; quant-ph
- Links: abs=https://arxiv.org/abs/2505.05246v4  pdf=https://arxiv.org/pdf/2505.05246v4.pdf

Abstract:
In a vast class of systems, which includes members as diverse as sedimenting particles and bird flocks, interactions do not stem from a potential, and are in general nonreciprocal. Thus, it is not possible to define a conventional energy function, nor to use analytical or numerical tools that rely on it. Here, we overcome these limitations by constructing a Hamiltonian that includes auxiliary degrees of freedom; when subject to a constraint, this Hamiltonian yields the original nonreciprocal dynamics. We show that Glauber dynamics based on the constrained Hamiltonian reproduce both stationary and nonstationary states of the original Langevin dynamics, as we explicitly illustrate for dissipative XY spins with vision-cone interactions. Further, the symplectic structure inherent to our construction enables us to apply the well-developed notions of Hamiltonian engineering, which we demonstrate by varying the amplitude of a periodic drive to tune the spin interactions between those of a square and a chain lattice geometry. Overall, our framework for generic nonreciprocal pairwise interactions paves the way for bringing to bear the full conceptual and methodological power of conventional statistical mechanics and Hamiltonian dynamics to nonreciprocal systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2509.05597v3
- Title: Entanglement Asymmetry and Quantum Mpemba Effect for Non-Abelian Global Symmetry
- Authors: Harunobu Fujimura, Soichiro Shimamori
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2509.05597v3  pdf=https://arxiv.org/pdf/2509.05597v3.pdf

Abstract:
Entanglement asymmetry is a measure that quantifies the degree of symmetry breaking at the level of a subsystem. In this work, we investigate the entanglement asymmetry in $\widehat{su}(N)_k$ Wess-Zumino-Witten model and discuss the quantum Mpemba effect for SU$(N)$ symmetry, the phenomenon that the more symmetry is initially broken, the faster it is restored. Due to the Coleman-Mermin-Wagner theorem, spontaneous breaking of continuous global symmetries is forbidden in $1+1$ dimensions. To circumvent this no-go theorem, we consider excited initial states which explicitly break non-Abelian global symmetry. We particularly focus on the initial states built from primary operators in the fundamental and adjoint representations. In both cases, we study the real-time dynamics of the Rényi entanglement asymmetry and provide clear evidence of quantum Mpemba effect for SU$(N)$ symmetry. Furthermore, we find a new type of quantum Mpemba effect for the primary operator in the fundamental representation: increasing the rank $N$ leads to stronger initial symmetry breaking but faster symmetry restoration. Also, increasing the level $k$ leads to weaker initial symmetry breaking but slower symmetry restoration. On the other hand, no such behavior is observed for adjoint case, which may suggest that this new type of quantum Mpemba effect is not universal.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2511.21599v3
- Title: Dichroism from Chiral Thermoelectric Probes: Generalized Sum Rules for Orbital and Heat Magnetizations
- Authors: Baptiste Bermond, Lucila Peralta Gavensky, Anaïs Defossez, Nathan Goldman
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.quant-gas; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2511.21599v3  pdf=https://arxiv.org/pdf/2511.21599v3.pdf

Abstract:
We introduce a unified framework that relates orbital and heat magnetizations to experimentally accessible excitation spectra, through thermoelectric probes and generalized sum rules. By analyzing zero-temperature transport coefficients and applying Kramers-Kronig relations, we derive spectral representations of magnetization densities from thermoelectric correlation functions. Excitation rates under chiral thermoelectric drives then naturally emerge as direct probes of these Kubo-type correlators, placing orbital and heat magnetizations on equal footing with the topological Chern number. As a direct consequence of our formalism, we introduce a hierarchical construction that organizes orbital and heat magnetizations into distinct physical contributions accessible through sum rules, and also naturally obtain real-space markers of these magnetizations. Besides, non-chiral thermal probes identify a heat quantum metric, which is defined over the space of gravitomagnetic deformations. From an experimental standpoint, we propose concrete implementations of thermoelectric dichroic measurements in quantum-engineered platforms based on modulated strain fields. These results establish thermoelectric dichroic measurements as a versatile route to access and disentangle fundamental ground-state properties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2512.05069v2
- Title: Hybrid Quantum-Classical Autoencoders for Unsupervised Network Intrusion Detection
- Authors: Mohammad Arif Rasyidi, Omar Alhussein, Sami Muhaidat, Ernesto Damiani
- Categories: cs.LG (primary); cs.LG; cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2512.05069v2  pdf=https://arxiv.org/pdf/2512.05069v2.pdf

Abstract:
Unsupervised anomaly-based intrusion detection requires models that can generalize to attack patterns not observed during training. This work presents the first large-scale evaluation of hybrid quantum-classical (HQC) autoencoders for this task. We construct a unified experimental framework that iterates over key quantum design choices, including quantum-layer placement, measurement approach, variational and non-variational formulations, and latent-space regularization. Experiments across three benchmark NIDS datasets show that HQC autoencoders can match or exceed classical performance in their best configurations, although they exhibit higher sensitivity to architectural decisions. Under zero-day evaluation, well-configured HQC models provide stronger and more stable generalization than classical and supervised baselines. Simulated gate-noise experiments reveal early performance degradation, indicating the need for noise-aware HQC designs. These results provide the first data-driven characterization of HQC autoencoder behavior for network intrusion detection and outline key factors that govern their practical viability. All experiment code and configurations are available at https://github.com/arasyi/hqcae-network-intrusion-detection.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2512.06053v2
- Title: Ferromagnetic Phase Transition of DPPH Induced by a Helical Magnetic Field
- Authors: Emmanouil Markoulakis, John Chatzakis, Antonios Konstantaras, Iraklis Rigakis, Emmanuel Antonidakis
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; physics.app-ph; physics.ins-det; quant-ph
- Links: abs=https://arxiv.org/abs/2512.06053v2  pdf=https://arxiv.org/pdf/2512.06053v2.pdf

Abstract:
We report the results and unique instrument configuration of a novel experiment in which we successfully transitioned a DPPH sample from its natural paramagnetic state and essentially a non-magnetic material to a ferromagnetic state at room temperature. This was achieved using a specifically applied helical flux magnetic field. The DPPH sample (2,2-diphenyl-1-picrylhydrazyl) remained ferromagnetic for at least one hour after the experiment, indicating that a transformation in the material was induced by the external field rather than being merely a temporary magnetic phase transition observed only during the experiment. The external magnetic field used had a helical pitch angle of approximately $54.7°$, known mathematically as the Magic Angle, relative to the +z-axis, which is aligned with the normal S to N external field's magnetic moment vector. Based on the phenomenology of the experiment and results, we suggest that this specific magic angle corresponding to the known quantization precession spin angle of free electrons under a homogeneous straight flux magnetic field potentially enhances the percentage of unpaired valence electrons within the DPPH material, allowing them to align in parallel with the applied external field. Typically, in paramagnetic materials, the distribution of unpaired electrons' quantum spins relative to an external field is nearly random, showing roughly a 50% chance of either parallel or antiparallel alignment. Only a slight majority preference exists in one alignment direction due to the Boltzmann thermal distribution, which contributes to the paramagnetic nature of these materials. In our measurements, we found that the induced ferromagnetism of the DPPH sample resulted in an abnormal thousand-fold decimal value increase in relative magnetic permeability at $μ{\approx}1.4$, compared to its typical paramagnetic value of $1.0001$ for this material.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2512.16836v2
- Title: Revival Dynamics from Equilibrium States: Scars from Chords in SYK
- Authors: Debarghya Chakraborty, Dario Rosa
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2512.16836v2  pdf=https://arxiv.org/pdf/2512.16836v2.pdf

Abstract:
We develop a novel framework to build quantum many-body scar states in bipartite systems characterized by perfect correlation between the Hamiltonians governing the two sides. By means of a Krylov construction, we build an interaction term which supports a tower of equally-spaced energy eigenstates. This gives rise to finite-time revivals whenever the system is initialized in a purification of a generic equilibrium state. The dynamics is universally characterized, and is largely independent of the specific details of the Hamiltonians defining the individual partitions. By considering the two-sided chord states of the double-scaled SYK model, we find an approximate realization of this framework. We analytically study the revival dynamics, finding rigid motion for wavepackets localized on the spectrum of a single SYK copy. These findings are tested numerically for systems of finite size, showing excellent agreement with the analytical predictions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2512.21281v2
- Title: Hamilton-Jacobi as model reduction, extension to Newtonian particle mechanics, and a wave mechanical curiosity
- Authors: Amit Acharya
- Categories: math-ph (primary); math-ph; physics.class-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2512.21281v2  pdf=https://arxiv.org/pdf/2512.21281v2.pdf

Abstract:
The Hamilton-Jacobi equation of classical mechanics is approached as a model reduction of conservative particle mechanics where the velocity degrees-of-freedom are eliminated. This viewpoint allows an extension of the association of the Hamilton-Jacobi equation from conservative systems to general Newtonian particle systems involving non-conservative forces, including dissipative ones. A geometric optics approximation leads to a dissipative Schrödinger equation, with the expected limiting form when the associated classical force system involves conservative forces.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-04-04 09:55
- arXiv: 2601.02459v2
- Title: Asymptotic freedom, lost: Complex conformal field theory in the two-dimensional $O(N>2)$ nonlinear sigma model and its realization in Heisenberg spin chains
- Authors: Christopher Yang, Thomas Scaffidi
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2601.02459v2  pdf=https://arxiv.org/pdf/2601.02459v2.pdf

Abstract:
The two-dimensional $O(N)$ nonlinear sigma model (NLSM) is asymptotically free for $N>2$: it exhibits neither a nontrivial fixed point nor spontaneous symmetry-breaking. Here we show that a nontrivial fixed point generically does exist in the complex coupling plane and is described by a complex conformal field theory (CCFT). This CCFT fixed point is generic in the sense that it has a single relevant singlet operator, and is thus expected to arise in any non-Hermitian model with $O(N)$ symmetry upon tuning a single complex parameter. We confirm this prediction numerically by locating the CCFT at $N = 3$ in two non-Hermitian spin-1 antiferromagnetic Heisenberg chains, and in a non-Hermitian spin-$1/2$ ladder, finding good agreement between the complex central charge and scaling dimensions and those obtained by analytic continuation of real fixed points from $N\leq 2$. We further construct a realistic Lindbladian for a spin-1 chain whose no-click dynamics are governed by the non-Hermitian Hamiltonian realizing the CCFT. Since the CCFT vacuum is the eigenstate with the smallest decay rate, the system naturally relaxes under dissipative dynamics toward a CFT state, thus providing a route to preparing long-range entangled states through engineered dissipation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

