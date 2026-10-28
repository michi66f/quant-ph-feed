- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31694v1
- Title: Verified Pauli-Product Measurement Compilation for Fault-Tolerant Quantum Computation
- Authors: John Zhuoyang Ye, Jens Palsberg
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.31694v1  pdf=https://arxiv.org/pdf/2610.31694v1.pdf

Abstract:
Fault-tolerant quantum compilers implement gates through Pauli-product measurements and classical feedback. Verifying such a compiler requires reasoning about the quantum state and the recorded outcomes together: a correction reads an outcome, a gate's internal outcomes must be hidden from its caller, and an application's outcomes must survive optimization. We introduce QPPM, a language for Pauli-product measurement programs, with a weakest-precondition semantics over store-indexed matrix assertions, following quantum Hoare logic with classical variables. Every program terminates, so the Hoare logic is a syntactic presentation of weakest preconditions whose soundness and relative completeness are immediate. Its value is that component specifications compose. All results are mechanized in Lean.   We verify lowering of Clifford+$T$ circuits to QPPM with private outcomes and supplied magic states, and an optimizer that eliminates measurements, fuses and reorders rotations, and schedules logical rounds while preserving every outcome that subsequent code can read. A compositional approximation relation bounds the effect of synthesis error on specifications and on output trace distance, and a certificate-checked pipeline selects, among synthesized circuits that meet the user's error limit, the one with the lowest certified depth bound. On QASMBench, verified fusion and scheduling reduce logical measurement depth by a median of 17.9\%, and complete source-to-QPPM allowances are certified for all 35 valid selected small-suite inputs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31729v1
- Title: Mutual Information Across Quantum Reference Frame Perspectives
- Authors: Leonardo Valente, Carla Ferradini, Flaminia Giacomini, Viktoria Kabel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.31729v1  pdf=https://arxiv.org/pdf/2610.31729v1.pdf

Abstract:
In quantum information theory, standard notions typically presuppose a fixed partition of the world into subsystems, encoded in a tensor product structure of the Hilbert space. Yet, in some scenarios, the subsystem structure is not uniquely fixed. A case in point is the description of subsystems relative to different quantum reference frames (QRFs), where the tensor product structure, although fixed in a specific QRF, changes across different QRFs. Such a relativity of subsystems underlies many interesting features of QRFs, such as the relativity of entanglement, entropy, and coherence. It also raises a broader question: how do we compare the information across different subsystem perspectives, especially when the corresponding subsystem algebras overlap? Here, we propose a notion of quantum mutual information across different QRF perspectives, which captures the correlations between subsystems relative to different frames of reference. To do so, we focus on an algebraic definition of subsystems. Studying in detail the union and overlap between subsystem algebras relative to different QRFs, we find that the usual definition of mutual information in terms of the chain law overcounts the information associated to the overlap. Based on this insight, we propose a modified chain law and show that the resulting notion of mutual information satisfies subadditivity and connects naturally to other measures found in the literature [1]. Our investigations not only provide a way to quantify the relation between different QRF perspectives from an information-theoretic point of view but also sheds light on some important features of quantum information in absence of a fixed tensor product structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31775v1
- Title: The Entire Quantum Computer on a Classical Leash
- Authors: Yael Tauman Kalai, Dakshita Khurana, Justin Raizes
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2610.31775v1  pdf=https://arxiv.org/pdf/2610.31775v1.pdf

Abstract:
We show that a classical client with no quantum hardware can use a single untrusted and potentially malicious quantum server as if it were its own trusted quantum computer. Through the server, the client can privately choose and run quantum computations, prepare quantum states, and process quantum states supplied by other parties. It can also keep quantum memory on the server, hidden from the server itself, and use that memory in later computations so its quantum state persists across rounds of interaction. Together, these capabilities let a purely classical party act as a quantum party in a variety of interactive protocols.   We expect this virtual quantum computer to be a broadly useful tool. As immediate applications, we resolve two known open problems: (1) classical verification of quantum sampling with negligible computational soundness error, and (2) remote state preparation of arbitrary efficiently preparable quantum states.   Underlying all of these results is a general-purpose, maliciously secure two-party computation protocol between a classical client and a quantum server, which we construct assuming only the post-quantum hardness of learning with errors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31792v1
- Title: Quantum Complexity and Stabilizer-State Expansions: From Pairing to Deformation in Fermionic Systems
- Authors: S. Momme Hengstenberg, Caroline E. P. Robin
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; nucl-th
- Links: abs=https://arxiv.org/abs/2610.31792v1  pdf=https://arxiv.org/pdf/2610.31792v1.pdf

Abstract:
Understanding how collective phenomena such as pairing and deformation emerge in interacting fermionic systems, and how the correlations underlying them shape the resources required for their simulation, is a central challenge in many-body physics. We investigate various aspects of quantum complexity in a fermionic system exhibiting two main forms of collectivity, specifically deformation and pairing, through entanglement, non-stabilizerness, and fermionic non-Gaussianity. In the deformed phase, high entanglement coexists with low non-stabilizerness, while the superfluid pairing phase, by contrast, exhibits substantial multipartite entanglement and non-stabilizerness, together with maximal fermionic anti-flatness. In a second step we examine how to describe the phase diagram of the system in a classically scalable and symmetry-preserving way, by combining stabilizer-state expansion and variational basis optimization. A physics-guided decomposition of the Hamiltonian identifies the relevant stabilizer states, which can be constructed from graph states. A single stabilizer state captures the deformed phase to a large extent, and, although the number of stabilizer states required to describe the pairing phase grows exponentially with system size, a symmetry-preserving basis rotation yields a high-fidelity approximation using far fewer states. This rotated state can then serve as a practical starting point for quantum refinement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31877v1
- Title: Temporal Degeneracy Limits Message Passing Decoding of QLDPC Codes Under Repeated Noisy Syndrome Measurements
- Authors: Dimitris Chytas, Nithin Raveendran, Bane Vasić
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2610.31877v1  pdf=https://arxiv.org/pdf/2610.31877v1.pdf

Abstract:
Practical quantum computations can require logical error rates of $10^{-12}$ or lower. Quantum low-density parity-check (QLDPC) codes are promising candidates for reaching such rates with low qubit overhead, provided that their syndromes can be decoded efficiently. Repeated noisy syndrome measurements introduce temporal degeneracy into the space-time decoding graph. We characterize the temporal kernel, whose vectors have zero total data parity, and show that it is generated by elementary temporal codewords of weight $d_v+2$, where $d_v$ is the variable-node degree. For $(d_v,d_c)$-regular parity-check matrices with fixed degrees $d_v,d_c>2$ and girth greater than four, we derive counting bounds and construct degenerate error patterns of weight $(d_v+2)/2$ for even $d_v$ and $d_v+1$ for odd $d_v$, with multiplicity $Θ(nr)$ in the blocklength $n$ and number of measurement rounds $r$. Under the isolation assumption, these patterns cause local failures of deterministic isotropic message-passing decoders under a flooding schedule. These failures depend on the node degrees rather than the minimum distance; for the bivariate bicycle (BB) codes considered, their weight is equal to four. Monte carlo simulations and fixed-weight importance sampling quantify harmful low-weight degenerate error patterns for the min-sum (MS) decoder beyond the isolation assumption. Motivated by the identified symmetries, we propose space-time anisotropic min-sum decoding with syndrome-guided realizations. Its complexity is linear in the number of Tanner graph edges for fixed maximum number of iterations and number of decoders. Numerical results on BB codes show threshold-like behavior acrossthe tested code sizes and improved failure probabilities relative to MS decoding with ordered statistics decoding post-processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31885v1
- Title: Optimal Control of a Fluxonium Circuit with the Q-PRONTO Numerical Method
- Authors: John Barta, Brian D. Isakov, Pablo Aramburu Sanchez, Jieqiu Shao, Tamás Kalmár, Trevyn F. Q. Larson, Marco M. Nicotra, András Gyenis
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.31885v1  pdf=https://arxiv.org/pdf/2610.31885v1.pdf

Abstract:
Optimizing the control of large quantum systems is a resource-intensive task, where the convergence rate of the underlying iterative schemes is crucial. The recently developed Quantum Projection Operator-Based Newton Method for Trajectory Optimization (Q-PRONTO) offers a unique quadratic convergence for controlling quantum states, while most model-based solvers guarantee only an approximately linear convergence rate. As a proof of concept, here, we design and benchmark single-qubit gates optimized by Q-PRONTO based on the circuit Hamiltonian of a fluxonium superconducting qubit. To ensure that we can apply a long string of arbitrary pulses to the circuit, we modify the firmware associated with the Quantum Instrumentation Control Kit (QICK) by altering its memory allocation. We characterize the performance of the optimal solutions using standard randomized benchmarking and achieve a total error per gate of $6.6\times10^{-4}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31933v1
- Title: Graphical Rigidity of Continuous Variable Graph States under Gaussian Local Transformations
- Authors: Giorgio Ciliberto, Frédéric Grosshans
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.31933v1  pdf=https://arxiv.org/pdf/2610.31933v1.pdf

Abstract:
Multimode entangled pure Gaussian states are an essential resource for continuous variable (CV) quantum information processing. Menicucci et al. [2011] have shown how to describe them as graphs with complex adjacency matrices. Among such complex graph states (CGSs), quantum optics experimental setups straightforwardly display correlations described by purely imaginary graph states (iRGSs) whereas theoretical literature favors off-diagonal real graph state (RGS) descriptions, which actually reflect the entanglement structure in the infinite squeezing limit [Gonzalez-Arciniegas et al. 2021]. We study them beyond this ideal case, thus establishing in the finite squeezing regime an equivalence criterion for the generic case of CGSs through a graph propagating set of conditions which either finds a Gaussian Local Unitary (GLU) converting one state to another or gives a proof of impossibility if such a GLU does not exist. In the experimentally relevant case of the conversion between iRGSs and RGSs, the set of conditions results in simple relations between the topologies of the equivalent real and imaginary graphs. Finally, we show that the canonical forms of iRGSs and RGSs imply that the topology of the CV real and imaginary graph states are too rigid to admit any exact qumode local-addition analogue to the qubit complementation or qudit local-addition, thus demonstrating the non-existence of any exact qumode local-addition for these states. We however define an approximate one when the squeezing is strong enough.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31938v1
- Title: Fidelity Dynamics of a Jaynes--Cummings Qubit under Markovian and Non-Markovian Coupling Noise
- Authors: Fang Wang, Da-Wei Luo, Ting Yu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.31938v1  pdf=https://arxiv.org/pdf/2610.31938v1.pdf

Abstract:
We analytically investigate the fidelity dynamics of a Jaynes--Cummings qubit coupled to a single-mode cavity in the presence of stochastic fluctuations of the qubit--cavity coupling. Such fluctuations naturally arise in cavity- and circuit-QED platforms due to fabrication imperfections, control-field noise, mechanical vibrations, and environmental disturbances. Since the qubit--cavity coupling governs the rate of coherent energy and information exchange, understanding the effects of its fluctuations is essential for assessing the performance of quantum communication, quantum sensing, and quantum information-processing protocols. We consider both Gaussian white noise and Ornstein--Uhlenbeck noise with finite correlation time as models for the coupling fluctuations. Exploiting the closed dynamics within each excitation manifold, we derive exact analytical expressions for the noise-averaged density matrix and the fidelity relative to the ideal noiseless evolution. We show that the fidelity is determined by a single decoherence factor governed by the integrated noise correlation function, establishing a direct connection between microscopic coupling fluctuations and macroscopic coherence loss. In the white-noise limit, the fidelity decays exponentially, whereas finite noise correlation times produce nonexponential decay and slower coherence loss. We further show that the crossover between Markovian-like and non-Markovian regimes is controlled by the ratio of the noise correlation rate to the coherent coupling strength, and that decoherence increases with photon number because of the enhanced effective qubit--cavity coupling. These results provide a unified analytical framework for quantifying decoherence induced by stochastic coupling fluctuations and for evaluating the robustness of cavity-QED protocols under correlated noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31947v1
- Title: Noise-Assisted Quantum Entanglement: Memory-Enhanced Coherence in Stochastic Jaynes-Cummings Dynamics
- Authors: Fang Wang, Quanzhen Ding, Jun Jing, Ting Yu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.31947v1  pdf=https://arxiv.org/pdf/2610.31947v1.pdf

Abstract:
We investigate qubit entanglement dynamics in a two-qubit cavity system with stochastically fluctuating coupling strength, comparing white noise (Markovian) and Ornstein-Uhlenbeck noise (non-Markovian) processes. We analytically solve the system dynamics for both Fock and coherent cavity states and systematically characterize how initial qubit configurations affect entanglement generation and preservation. Our results reveal distinct dynamical regimes: in the Fock-state cavity, initial states in the single-excitation subspace generate robust qubit entanglement in decoherence-free subspaces, while initially entangled states in the double-excitation subspace exhibit inevitable decay without protective symmetries. For coherent cavities, we identify a critical photon-number threshold in the intermediate coherent-state amplitude regime where dynamics transition from low-frequency to high-frequency entanglement oscillations, while universal entanglement loss occurs at large amplitudes. Remarkable resilience against entanglement sudden death emerges under strong non-Markovian noise with long correlation times, where repeated revivals occur. These findings establish cavity photon statistics and environmental memory time as key control parameters for engineering qubit entanglement dynamics in qubit-cavity systems, revealing how system-environment correlations govern quantum information preservation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31998v1
- Title: Demonstrating RFSoC-based Control of a Fully Connected Exchange-Only Qubit
- Authors: Abigail L. Wessels, M. Garrett Bimstefer, Joseph D. Broz, Alen Senanian, Andrew E. Oriani
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.31998v1  pdf=https://arxiv.org/pdf/2610.31998v1.pdf

Abstract:
Semiconductor triple-quantum dots (TQDs) are a promising platform for scalable quantum information processing, but the community has so far lacked access to affordable and flexible high-speed control electronics. SpinQICK, an open-source spin qubit-control package built on the Xilinx Radio Frequency System-on-Chip (RFSoC), directly addresses this gap by leveraging the high sampling-rate signal generation and advanced digital signal processing (DSP) capabilities of the Quantum Instrumentation Control Kit (QICK) to enable precise time-domain voltage control and readout of semiconductor spin qubits. In this paper, we use spinQICK to demonstrate coherent control, state preparation, and readout of a fully connected triangular exchange-only device. We also introduce and experimentally verify a novel dynamical decoupling (DD) sequence enabled by the triangular TQD and leverage its unique decoupling properties to characterize electrical noise. These results establish spinQICK as a low-cost, flexible platform for semiconductor spin qubit control and provide a pathway for hardware optimization through qubit-level noise diagnostics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32001v1
- Title: QuantumMatterExplorer: An Autonomous Agent for the Discovery of Quantum Many-Body Phases of Matter
- Authors: Jannes Nys, Andrew Jreissaty, Juan Carrasquilla
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2610.32001v1  pdf=https://arxiv.org/pdf/2610.32001v1.pdf

Abstract:
Mapping the phase diagram of a new quantum Hamiltonian demands expert judgement at every step: which observables to measure, where in parameter space to compute, or how to separate genuine order from finite-size artefacts. We introduce QuantumMatterExplorer, an autonomous agent that takes only a Hamiltonian and its parameter ranges as input and returns a phase diagram obtained from its own numerical simulations. The agent is built on a large language model and is designed to reason over a long horizon, maintain a persistent written plan, and drive a set of computational tools, with density-matrix renormalization group (DMRG) calculations cross-checked against independent exact diagonalization. The agent combines a large language model with persistent planning, a library of expert computational-physics skills, and density-matrix renormalization group calculations validated against independent exact diagonalization. It adaptively selects quantities to evaluate, refines parameter scans, and performs finite-size analyses as evidence accumulates. After validating the approach on Hamiltonians with known transitions, we challenge it with a frustrated bilinear-biquadratic spin-1 chain with single-ion anisotropy, whose two-dimensional phase diagram was published only recently and is unlikely to appear in any training corpus. Given no hint about the expected physics, the agent proposes which observables to probe, and identifies candidate Néel, Haldane and dimerized phases, in broad agreement with the reference phase diagram. It also detects incommensurate correlations and infers the frustration-dependent geometry of the phase boundaries, all within an eight-hour compute budget. These results open a practical route to the autonomous computational discovery of new phases of quantum matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32014v1
- Title: Additive uncertainty relations via pseudospectral methods
- Authors: Alexander Cerjan, Lara Ismert, Terry A. Loring
- Categories: quant-ph (primary); quant-ph; math.OA
- Links: abs=https://arxiv.org/abs/2610.32014v1  pdf=https://arxiv.org/pdf/2610.32014v1.pdf

Abstract:
Given Hermitian observable $A$, the variance of $A$ is given by the difference of expectations $\langle A^2\rangle - \langle A\rangle^2$, where the expectation of an observable implicitly assumes a choice of state for the underlying system. As a sub-case of a general lower bound for the sum of variances for finitely many arbitrary elements in a $C^*$-algebra, we prove that the sum of the variances for $d$ observables $A_1, \dots , A_d$ is greater than some expression in the expectations $\langle i[A_j,A_k]\rangle$ for $j\neq k$ plus the square of the smallest singular value of the associated localizer. In special cases, this expression is just a root mean square average. Our technique also derives a general containment between the Clifford pseudospectra and quadratic pseudospectra for $d$ observables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32037v1
- Title: Asymptotic scars arising from the remnants of quantum phase transitions
- Authors: Leonard Logarić, Shane Dooley, Tsuyoshi Okubo, Nobuyuki Yoshioka
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32037v1  pdf=https://arxiv.org/pdf/2610.32037v1.pdf

Abstract:
Many-body localisation, Hilbert space fragmentation and quantum many-body scars (QMBS) are well-established mechanisms of ergodicity breaking in quantum systems. Recently, asymptotic quantum many-body scars (AQMBS), non-thermal states whose stability grows with system size, have been proposed theoretically and probed experimentally. Here, we show that AQMBS arise naturally as remnants of certain quantum phase transitions. For a broad class of frustration-free Hamiltonians, we prove that their gapless excitations survive deformation into a scarred Hamiltonian as states whose energy variance is bounded by the excitation gap. Consequently, the gapless excitations at a quantum critical point become AQMBS of the scarred Hamiltonian. Their fidelity relaxation time is then set by the critical scaling of the gap, determined by the dynamic critical exponent. Modelling the critical Fredkin and Motzkin chains and the two-dimensional PVBS model, we obtain AQMBS whose variances directly reflect the dynamic exponents of the underlying transitions. Where the gap of the Motzkin chain closes super-exponentially, we find exponentially stable AQMBS, for which we also observe numerical evidence of volume-law entanglement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32049v1
- Title: Robustness of Quantum Correlations and Controlled Teleportation Fidelity under Noisy Channels
- Authors: S. Archana, Aditi Das, Venkat Abhignan, R. Muthuganesan
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2610.32049v1  pdf=https://arxiv.org/pdf/2610.32049v1.pdf

Abstract:
In distributed quantum computing, quantum networks provide a potential infrastructure for long-range quantum information processing. Controlled quantum teleportation (CQT) is a key practically relevant protocol that can connect two parties on a network and enables a third party, the controller to allow or abort the secure teleportation of an arbitrary single-qubit state between the two parties. We investigate the robustness of a three-qubit GHZ resource under bit-flip, phase-flip, depolarizing, and amplitude-damping noise. Using the Kraus-operator formalism, we characterize the noisy resource through multipartite quantum discord, genuine multipartite concurrence (GMC), localizable entanglement (LE), and CQT fidelity. We also outline a proof-of-concept photonic implementation for preparing the three-qubit GHZ resource and realizing the CQT protocol, which could enable experimental investigation of the effects of noise. Our results show that bit-flip and amplitude-damping noise generally preserve useful mutipartite quantum correlations over broader noise parameter ranges. Interestingly, multipartite discord exhibits freezing under bit-flip noise over a finite parameter regime. Moreover, discord can persist beyond the sudden death of genuine multipartite entanglement, revealing the distinct robustness of nonclassical correlations. We further demonstrate that CQT fidelity which characterizes the performance of CQT can exceed the classical threshold even after GMC vanishes, while LE more closely reflects the operational usefulness of the noisy resource. These findings highlight the complementary roles of quantum correlations and entanglement in assessing the resilience of GHZ-based protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32054v1
- Title: Real-space construction and selection rules of center-of-mass momentum eigenstates in two-dimensional many-body lattices
- Authors: Ling Lin, Yongguan Ke, Chaohong Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32054v1  pdf=https://arxiv.org/pdf/2610.32054v1.pdf

Abstract:
We present a comprehensive framework for the real-space construction of center-of-mass (c.m.) momentum eigenstates in two-dimensional (2D) quantum many-body systems. Unlike standard momentum-space approaches, our real-space formalism explicitly captures the non-uniformity of cyclic subspace dimensions, which are fundamentally governed by the spatial symmetries of the many-body configurations and particle statistics. We demonstrate that performing 2D real-space translations on multi-particle states naturally induces non-trivial translation phase factors associated with the characters of these stabilizer subgroups, leading to a renormalization of permissible momentum values. Notably, we identify an anomalous cross-dimensional momentum coupling in highly symmetric particle distributions, where the permissible momentum values in one direction are strictly constrained by those in the perpendicular direction. We emphasize the algorithmic necessity of this coupling, as neglecting it leads to missing or duplicated basis states in numerical implementations. Concrete examples are provided to demonstrate the practical implementation and physical consequences of this framework.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32145v1
- Title: Quantum Cryptomania with Classical Communication without One-Way Functions
- Authors: Mohammed Barhoush, Amit Behera
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32145v1  pdf=https://arxiv.org/pdf/2610.32145v1.pdf

Abstract:
In classical cryptography, one-way functions are necessary for most of cryptography. In the quantum world, however, Kretschmer at {TQC'21} and subsequent works have demonstrated that quantum versions of various primitives in minicrypt, such as signatures and private-key encryption, do not require quantum-computable one-way functions (\textsf{qOWF}s). However, the question of the necessity of \textsf{qOWF}s for primitives in Cryptomania like public-key encryption with classical public keys and ciphertexts (\textsf{qPKE}) has remained open.   We provide a comprehensive picture of the relationship between \textsf{qPKE} and \textsf{qOWF}. First, our main result is a black-box separation between \textsf{qOWF}s and \textsf{qPKE}. In particular, we show that relative to a unitary, real, and self-inverse oracle, there exists a \textsf{qPKE} scheme (with classical keys and ciphertexts), but \textsf{qOWF}s do not exist. Further, our oracles admit a point-function obfuscation construction, thus ruling out black-box construction of \textsf{qOWF} from point function obfuscations.   On the positive side, we construct \textsf{qPKE} from quantum indistinguishability obfuscation for quantum circuits with classical obfuscated descriptions and efficiently verifiable one-way puzzles, which is known to be a potentially weaker assumption than \textsf{qOWF}s, due to an existing black-box separation. Our construction is the quantum analog of the classical construction of \textsf{PKE} from one-way functions and indistinguishability obfuscation in the quantum computation with classical communication (QCCC) setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32152v1
- Title: Trident: Efficient Load Verification for Yoked Surface Codes using a Three-Level Memory Hierarchy
- Authors: Gunagya Singh Mamak, Suhas Vittal, Kabir Dubey, Kaitlin N. Smith, Moinuddin K. Qureshi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32152v1  pdf=https://arxiv.org/pdf/2610.32152v1.pdf

Abstract:
Fault-Tolerant Quantum Computers (FTQCs) commonly use the surface code to encode program qubits as error-corrected logical qubits. Unfortunately, the surface code has a poor encoding rate, so recent work has proposed Yoked Surface Codes (YSCs), which concatenate the surface code with a high-rate quantum code. The surface code qubits in YSCs are protected by the checks, or yokes, of the high-rate code. YSCs have 1D and 2D variants, which are $1.8\times$ and $4.5\times$ more efficient than the surface code, respectively.   Modern FTQC architectures use a two-level hierarchy: surface codes perform logical operations (compute) while 2D YSCs store idle program qubits (memory). To load a qubit from memory, the FTQC first performs retrieval, which logically moves a program qubit from a 2D YSC into a surface code (8 cycles). However, retrieval is not fault-tolerant, so the FTQC must verify the load by measuring all the yokes of the 2D YSC (178 cycles). As verification dominates memory access latency, eliminating it can provide a speedup of $5.7\times$.   Our goal is to reduce the verification overhead of 2D YSCs while retaining their storage efficiency. We exploit the fact that 1D YSCs, though less storage-efficient, incur negligible verification latency. We propose Trident, which expands the two-level hierarchy into a three-level hierarchy by adding a small intermediate level containing a 1D YSC (L1). If most loads hit L1 rather than L2 (2D YSC tier), it can significantly reduce verification overhead. We present two variants: Trident-D (demand-driven) and Trident-P (prefetch-driven), which achieve speedups of $2.8\times$ and $4.2\times$, respectively, while increasing the physical qubit cost of memory by only 4.9%.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32154v1
- Title: Photon-Number Discrimination from Increasing Time-of-Arrival Separation in Wide Superconducting Microstrip Single-Photon Detectors
- Authors: Hsin-Yeh Wu, Shu-Xiao Liu, Boris Tuchming, Xavier-François Navick, Pu-Kai Wang, Yi-Ren Wu, Jia-Wern Chen, Marc Besançon, et al.
- Categories: quant-ph (primary); quant-ph; hep-ex; physics.app-ph
- Links: abs=https://arxiv.org/abs/2610.32154v1  pdf=https://arxiv.org/pdf/2610.32154v1.pdf

Abstract:
Measurements of photon-number-dependent time-of-arrival (TOA) distributions in wide NbN superconducting microstrip single-photon detectors (SMSPDs) are presented. Two \SI{10}{\um}-long devices with widths of \SI{3.2}{\um} and \SI{6.4}{\um} are characterized under pulsed \SI{515}{nm} excitation. The TOA histograms are described by sums of exponentially modified Gaussian (EMG) components, with the wider device exhibiting components assigned to photon numbers up to \(n=8\). Adjacent TOA peaks become more distinguishable relative to their widths at higher photon number, in contrast to the compression of neighboring photon-number timing shifts observed in conventional narrow-wire SNSPDs. For the components assigned to \(n=7\) and \(n=8\), the FWHM-normalized peak separation is \(2.15\), and the fitted EMG distributions yield an equal-prior pairwise TOA-assignment fidelity of \(99.6\%\). The EMG exponential-tail parameter \(τ_n\) decreases strongly with photon number, while the Gaussian-location parameter \(μ_n\) continues to shift between neighboring components. A phenomenological model motivated by absorption-site-dependent vortex processes and collective current redistribution captures these timing trends. These results support wide SMSPDs as a platform for TOA-based photon-number discrimination at high photon number, relevant to multiphoton-state characterization and photonic quantum information processing. The same geometry also provides a setting to examine how the spatial distribution of photon absorption affects vortex-assisted detection.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32156v1
- Title: Quantum Evolution Networks Learn Long-Time Coherent Dynamics in Driven Spin Registers
- Authors: Puran Li, Condon Lau, Xiu-Hao Deng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32156v1  pdf=https://arxiv.org/pdf/2610.32156v1.pdf

Abstract:
Predicting and controlling driven quantum systems requires access to dynamics across physical parameters, initial states, and evolution times. A reusable neural model must capture this dependence while preserving unitary structure and maintaining accuracy over long-time coherent evolution. Here we introduce Quantum Evolution Networks (QENs), which map physical parameters and time to complete propagators for periodically driven three-spin registers. Shared networks learn unitary one-period propagators and compatible within-period paths, enabling predictions through known periodic composition without query-specific numerical integration. For transverse driving, the fifth-percentile fidelity, minimized over input states and sampled times, is 0.9947 over 24 periods on 256 held-out configurations. A leading-order analysis of spectrally resolved endpoint residuals predicts multicycle process error more accurately than quadratic or spectrum-averaged estimates. Interventions at matched single-period infidelity produce orders-of-magnitude differences in multicycle infidelity, demonstrating the importance of residual orientation. Compatible component replacements identify how endpoint and within-period approximations limit reconstruction accuracy. These results establish a reusable neural representation of the studied propagator families and connect its learned residual structure to its observed long-time reliability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32209v1
- Title: Bogoliubov Dynamics and Zitterbewegung in Optical Dirac Systems
- Authors: Lili Yang
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2610.32209v1  pdf=https://arxiv.org/pdf/2610.32209v1.pdf

Abstract:
We develop a bosonic Bogoliubov description of Zitterbewegung in time-dependent optical-Dirac systems. Within the optical-Dirac framework, the anomalous pair-creation and pair-annihilation terms of a bosonic Bogoliubov Hamiltonian correspond to couplings between the positive- and negative-frequency sectors, whose coherence underlies the Zitterbewegung response. When the constitutive parameters vary in time, the resulting moving-frame connection generates dynamical interbranch coupling and positive--negative-frequency coherence. Under periodic modulation, this coupling becomes resonant near $Ω\simeq2ω_0$, leading to parametric amplification of the coherence and consequently to an enhanced Zitterbewegung motion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32218v1
- Title: Traceable Quantum Secret Sharing
- Authors: Mengyan Qiao, Jian Long, Yu Li, Zhu Cao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32218v1  pdf=https://arxiv.org/pdf/2610.32218v1.pdf

Abstract:
Quantum secret sharing protects distributed quantum information against unauthorized reconstruction, yet existing schemes provide no intrinsic accountability when shares are leaked or forged. This missing capability is particularly relevant in realistic distributed settings, where compromised participants may either expose valid shares or maliciously interfere with reconstruction. Here we establish a framework for traceable quantum secret sharing under these two threat models. We introduce leakage-verifiable and traceable quantum secret sharing (LVT-QSS), which attributes leaked shares through an explicit leakage verification mechanism, and malicious-traceable and accountable quantum secret sharing (MTA-QSS), which identifies participants who submit forged shares during reconstruction. We formulate security definitions for both settings and prove that the proposed protocols satisfy the corresponding guarantees against the relevant adversaries. Numerical simulations under per-share depolarizing noise further quantify the robustness of the proposed schemes and identify verification as the dominant noise sensitive stage. These results incorporate accountability into quantum secret sharing and provide a foundation for traceable distributed quantum cryptography.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32227v1
- Title: Performing a Quantum Subroutine Using Cluster States
- Authors: Sakibul Islam Rayhan, Karima Hassan, Md Rasedujjaman, Md Mohsinur Rahman Adnan
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2610.32227v1  pdf=https://arxiv.org/pdf/2610.32227v1.pdf

Abstract:
Quantum subroutines, like their classical counterparts, serve as essential components of larger algorithms. They can be realized using gate based architectures or measurement based quantum computation (MBQC), where computation proceeds through adaptive measurements on highly entangled cluster states. In this work, we implement a phase oracle as a reusable subroutine within the MBQC framework using experimentally feasible cluster states. Unlike prior demonstrations of Grover's algorithm in MBQC that omit explicit oracle construction, our approach provides a transparent formulation of the oracle subroutine, including its measurement patterns, byproduct correlations, density-matrix simulations, and corresponding MBQC measurement circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32267v1
- Title: Two-Layer Verification for Fault-Tolerant Magic-State Preparation in High-Rate Quantum Codes
- Authors: Naoyuki Kanomata, Hayato Goto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32267v1  pdf=https://arxiv.org/pdf/2610.32267v1.pdf

Abstract:
Encoded magic states are essential for universal fault-tolerant quantum computation, but their resource-efficient preparation in high-rate quantum codes remains challenging. To address this limitation, we propose two-layer verification, which combines local verification of independently prepared subblocks with logical verification after their embedding into a target code. This hierarchy detects harmful error patterns, including even-parity logical-eigenvalue flips that are invisible to a collective product check alone. We demonstrate this scheme for a $[[21,3,5]]$ code by constructing a circuit that embeds three verified seven-qubit Steane-code magic states into the target code. Circuit-level simulations of $T$- and $S$-state preparation show logical-error suppression consistent with the code distance. These results demonstrate the potential of two-layer verification as a design principle for reliable magic-state preparation in quantum codes encoding multiple logical qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32287v1
- Title: Near-field maps of topological edge states of molecular aggregates
- Authors: Aritra Mishra, Sidhartha Nayak, Alexander Eisfeld
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2610.32287v1  pdf=https://arxiv.org/pdf/2610.32287v1.pdf

Abstract:
Self-assembled two-dimensional molecular aggregates provide a versatile platform for engineering excitonic states, including topologically nontrivial edge states. However, these edge-states are difficult to probe optically: they have weak far-field transition strengths, and far-field spectra do not reveal whether an excitation is localized at the edge. For an aggregate consisting of two sublattices of molecules with genuinely complex transition dipoles, we show that spatially resolved near-field spectroscopy encodes the full spatial structure of these states. The resulting near-field maps do not mirror the site populations, but instead exhibit strongly nonuniform, interference-like features. We demonstrate that a convolutional neural network can reconstruct the complex expansion coefficients of the eigenstates from these maps, and that this reconstruction is robust against substantial random noise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32292v1
- Title: High Resolution Hyperspectral Quantum Infrared Imaging with Undetected Photons
- Authors: Aadi Suketu Bharatia, Vidya Prakash Muppalla, Ananya Asthana, Priyanka Kandankel, Tanmoy Chakraborty, Sreelaja Nair, Anshuman Kumar
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2610.32292v1  pdf=https://arxiv.org/pdf/2610.32292v1.pdf

Abstract:
Quantum sensing in the infrared regime often demands the use of expensive and cryogenically operated detectors. Nonlinear interferometry has paved the way for information transfer from the infrared to the near--infrared or visible regime in various quantum technologies. A particularly interesting application of these interferometers involves spectrally--resolved quantum imaging using undetected photons, enabled by the use of temperature--tunable parametric amplifiers. In this work, we demonstrate spectrally resolved transmission imaging with undetected photons around 1550 nm using a spontaneous parametric down conversion based folded nonlinear interferometric scheme, registering the attenuation of a zebrafish larva as a biological feasibility test. We characterize and calibrate the interferometer, having achieved spectrally resolved interference fringes with a maximum baseline visibility of $\sim 74\%$ in the near--infrared regime. Phase--stepped readout of a grating spectrometer gives a resolving power of $\sim1460$ (from the spectrometer's point spread function) at 1550 nm, and $\sim 730$ from the coherence length, the finest reported for imaging with undetected photons, over an instantaneous spectral window of $\approx 51$ cm$^{-1}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32315v1
- Title: Fundamental bound on Wigner negativity generation from environmental collisions
- Authors: Isaac Layton, Takahiro Sagawa, Ken Funo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32315v1  pdf=https://arxiv.org/pdf/2610.32315v1.pdf

Abstract:
Beyond quadratic potentials, classical evolution laws are typically thought to arise from quantum theory as an approximate description. Here we show that classical evolution laws can emerge exactly, provided the environment interacts with the system via collisions. We use this to derive an inequality that lower bounds the distribution of environmental momentum kicks by the absolute value of the Fourier transform of the potential. We show that violating this inequality is necessary and sufficient for a non-quadratic potential to generate negativity from the set of positive Wigner functions. A simple consequence of this is a lower bound on the heating rate for a quantum system to evolve effectively classically. We illustrate our results using the theory of a levitated nanoparticle subject to photon recoil and background gas collisions. We derive the strength of external potential needed to generate Wigner negative states in an optical tweezer and propose an experimental test of whether a nanoparticle in an optical lattice is operating in a non-classical regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32319v1
- Title: Finite Nonsignalling Resources Suffice to Simulate Entangled Qubits
- Authors: Ziao Tang, Xin Wang, Ge Bai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32319v1  pdf=https://arxiv.org/pdf/2610.32319v1.pdf

Abstract:
A longstanding question in Bell nonlocality is whether finite-alphabet nonsignalling resources can reproduce the continuum of measurement correlations of partially entangled qubits. Here we resolve this problem by showing that every fixed pure two-qubit state admits an exact simulation of all local projective-measurement statistics using shared randomness and finitely many Popescu-Rohrlich (PR) boxes, without communication or postselection. The boxes operate in parallel, with a worst-case bound independent of the measurement settings: at most $128\cot^4θ$ calls for the Schmidt state $\cosθ|00\rangle+\sinθ|11\rangle$, $0<θ<π/4$. The key is an exact finite-selection method that reduces input-dependent continuous sampling to a choice from a fixed-length shared random list, implemented through a finite PR-box network. The construction extends to arbitrary mixed two-qubit states and local binary-outcome POVMs. This reveals a fundamental separation between the continuity of quantum measurement correlations and the alphabet size of the resources needed to simulate them, shedding light on the resource-theoretic structure of Bell nonlocality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32347v1
- Title: Entangled logical qubits on a superconducting quantum processor
- Authors: Robin Harper, Xanda C. Kolesnikow, Campbell K. McLauchlan, Georgia M. Nixon, Stephen D. Bartlett, Benjamin J. Brown
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32347v1  pdf=https://arxiv.org/pdf/2610.32347v1.pdf

Abstract:
We demonstrate high-fidelity logical qubit operations using \texttt{ibm\_phoenix}, a square-lattice array of 120 coupled superconducting qubits that are capable of fast reset. Using strategies to exclude underperforming components together with noise informed decoding, we routinely produce surface codes at distance-3 and distance-5 with logical error per round below 1\%. We demonstrate entanglement between two logical qubits, where logical Bell-state fidelities above 93\% are observed for entanglement created via lattice surgery. With three logical qubits and lattice surgery, we perform logical teleportation of a range of states and gates, observing fidelities in the range 78\% - 93\%. Using reset to reduce qubit leakage, we show that repeated rounds of stabilizer measurements continue to exhibit improvements in a stability experiment up to $\sim 2\cdot 10^{-7}$ over 170 measurement rounds.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32368v1
- Title: Quantum theory of laser noise in coherent-scattering levitated optomechanics
- Authors: Davide Candoli, Andreu Riera-Campeny, Lorenzo Dania, Oscar Schmitt Kremer, Johannes Piotrowski, Jayadev Vijayan, Lukas Novotny, Martin Frimmer, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32368v1  pdf=https://arxiv.org/pdf/2610.32368v1.pdf

Abstract:
State purity is a key resource for experimental tests of quantum mechanics with massive objects. Cavity cooling of a levitated nanoparticle via coherent scattering stands out as a strategy to prepare highly pure states of its roto-translational motion. In several cases, though, the performance of cooling by coherent scattering is limited by the classical fluctuations of the laser field. Here we present a quantum theory of coherent-scattering experiments which includes the effect of the laser amplitude and phase noise. We derive a master equation for the noise-averaged particle's dynamics, valid for both center-of-mass and rotational degrees of freedom, and quantify the cooling performance for different levels of noise in state-of-the-art experiments. We compute approximate analytical expressions for the laser-noise-induced heating rates and excess phonon number in both regimes of weak and strong optomechanical coupling. Moreover, our model can be applied to laser noise processes with generic power spectral densities and finite correlation times. This work offers a toolbox to quantify and optimize the state purity in coherent-scattering experiments, and opens new avenues towards the preparation of quantum states with levitated systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32428v1
- Title: Quantum Secret Sharing from CSS qLDPC Codes: Computable Access Structures, Accessible Logical Dimension, and Topology-Aware Network Cost
- Authors: Malik Mouaji, Saif Al-Kuwari
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32428v1  pdf=https://arxiv.org/pdf/2610.32428v1.pdf

Abstract:
Quantum secret sharing (QSS) schemes can be constructed from quantum error-correcting codes, but characterizing their access structures and implementation costs becomes challenging for finite-length, high-rate quantum low-density parity-check (qLDPC) codes. We develop an exact computational framework for QSS induced by CSS qLDPC codes. The framework characterizes authorized, forbidden, and intermediate coalitions using restricted parity-check matrices and binary linear algebra, and introduces the accessible logical dimension \(κ(A)\), defined through the symplectic rank of locally supported logical classes, to refine the characterization of intermediate coalitions. We further incorporate physical network constraints through separate Tanner-incidence, Steiner-routing, and scheduling-depth costs, and treat the partitioning of physical qubits into participants as an explicit design variable. Numerical experiments on four CSS qLDPC codes verify the predicted complement duality and monotonicity properties and show substantial variation in access transitions and network costs. For the codes studied, the bivariate bicycle instance exhibits the sharpest transition, while network embedding costs vary by more than an order of magnitude across physical topologies. We also show that participant partitioning can substantially improve block-level security and reconstruction thresholds. These results provide a practical bridge between the algebraic structure of CSS qLDPC codes, the graded accessibility of quantum secrets, and the physical constraints of networked QSS implementations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32518v1
- Title: LYNX - A trapped-ion quantum information processor
- Authors: Alexander Erhard, Georg Jacob, Max Hettrich, Philip C. Holz, Juris Ulmanis, Thomas Feldker
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32518v1  pdf=https://arxiv.org/pdf/2610.32518v1.pdf

Abstract:
We introduce LYNX, a quantum information processor based on trapped $^{40}$Ca$^+$ ions. It utilizes up to 31 qubits with all-to-all connectivity. We characterize the system performance using rigorous benchmarks, such as randomized benchmarking (RB), GHZ state fidelity estimates, and quantum volume (QV) tests. The LYNX processor shows average 1-qubit gate errors of $8(5)\times 10^{-5}$ tested via standard RB in a 24-qubit register. An average 2-qubit gate error in a 24-qubit register of $2.84(8)\times 10^{-3}$ is demonstrated using interleaved RB. Furthermore, the device passes QV tests using up to 15 qubits which corresponds to a quantum volume of QV$=2^{15}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32541v1
- Title: Photon-Pair Advantage for Dissipative Parameter Estimation in Whispering-Gallery-Mode Interferometers
- Authors: Elnaz Darsheshdar, Callum Jones, Seyed Mostafa Moniri, Antonio Vidiella-Barranco, Jolly Xavier, Frank Vollmer
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32541v1  pdf=https://arxiv.org/pdf/2610.32541v1.pdf

Abstract:
We study the estimation of detuning and intrinsic loss in a lossy whispering-gallery-mode (WGM) resonator located in a balanced Mach--Zehnder interferometer. We use indistinguishable photon pairs and coherent-state probes. We show that using indistinguishable photon pairs can provide higher Quantum Fisher Information (QFI) of dissipative parameters, such as intrinsic loss, at resonance away from critical coupling. Taking into account all photon-loss outcomes, we obtain analytical QFI expressions and compare photon-pair and coherent-state probe results when they have the same mean photon number. For estimating the round-trip amplitude transmission at resonance and away from critical coupling, the photon-pair probe gives a higher QFI than the coherent-state probe, and photon-number-resolved detection saturates this QFI. This advantage is due to the photon-loss statistics and it is still accessible for a typical overcoupled condition after averaging over fluctuations of the unresolved detuning. We identify the limits of this advantage: phase doubling does not improve resonant detuning estimation, and coincidence-only detection is inefficient close to a zero transmission. These results identify the cases in which photon pairs can be useful for absorption and pump--probe WGM sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32571v1
- Title: Classical Pre-Training of Large Shallow Parametrized Quantum Circuits through Pauli Propagation and deployment on Quantum Hardware
- Authors: Saverio Monaco, Jamal Slim, Ran Xue, Dirk Krücker, Kerstin Borras
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32571v1  pdf=https://arxiv.org/pdf/2610.32571v1.pdf

Abstract:
Scaling parametrized quantum circuits to a larger number of qubits is a central challenge in Quantum Machine Learning: gradient estimation via the parameter-shift rule quickly becomes prohibitively expensive, while gradient-free optimizers offer limited convergence guarantees. We apply the Pauli propagation framework to a broad class of Quantum Machine Learning problems in which the loss is expressed as a function of expectation values of the circuit's observables, while keeping the relevant quantity of interest, such as the quantum state or its samples, classically intractable to compute. By propagating the observables backward through the circuit, we obtain an explicit parametric expression for the loss that can be minimized entirely on classical hardware. We also present complementary strategies to make propagation tractable at large scale, including weight-based and degree-based truncations and pruning heuristics. We demonstrate the approach on two benchmarks run on 64-qubit circuits: Variational Quantum Eigensolver on a two-dimensional Ising model, and training of a discrete-type generative model for binary images. In both cases, the classically pre-trained parameters are deployed on the IBM quantum processor ibm_berlin. For generative learning, we additionally show that the circuits considered here require substantially fewer parametrized gates than IQP-style ansätze, reducing transpilation overhead and making deployment on current quantum hardware feasible.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32585v1
- Title: A note on the monotonicity of observational ergotropic advantage
- Authors: Debanjan Dey Sarkar, Mallika Mondal, Preeti Parashar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32585v1  pdf=https://arxiv.org/pdf/2610.32585v1.pdf

Abstract:
Very recently, Mahanti et al. (arXiv:2609.18735) introduced the observational ergotropic advantage, which gives the maximum value of extra work that a measurement can obtain with respect to all incoherent measurements. However, the above quantity does not show monotonic behaviour under the resource theory of measurement coherence. So, the search for a resource theory in which it is a monotone was open. We derive the monotonicity of this quantity using energy-preserving channels and passive resets as free operations and energy-incoherent measurements as free objects. We show the monotonicity property of the measure as a necessary criterion of measurement transformation, but it turns out not to be a sufficient condition. It is further established that the measure is not convex. A short analysis of bounds and tightness of the measure using a degenerate Hamiltonian is also given.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32595v1
- Title: The Compendium of Super-Quadratic Computational Quantum Advantages
- Authors: Philipp Kammerlander, Thomas E. O'Brien, Robbie King, Rolando D. Somma, Mária Kieferová, Brad Lackey, Alexander Schmidhuber, Siddhartha Jain, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32595v1  pdf=https://arxiv.org/pdf/2610.32595v1.pdf

Abstract:
This compendium presents a structured collection of computational problems with credible prospects for realizing meaningful quantum advantage, focused on describing problem characteristics rather than specific algorithms. It is intended for non-quantum researchers and practitioners with strong computational backgrounds, particularly domain experts, seeking to assess the relevance of quantum methods to real-world problems. The compendium focuses on enumerating core problems for which there is good evidence that a quantum computer can realize more than a quadratic speedup in offline non-relativized time-complexity (e.g., as opposed to in oracular settings, streaming models, or communication advantages). Entries characterize the structural constraints that real-world instances must satisfy to realize those advantages in practice. The intention is to provide a reference that can be leveraged to connect quantum algorithms to practical use cases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32605v1
- Title: QuantumBilliards.jl: An extensible, user friendly, high-performance Julia library for the large scale computation of spectra and eigenstates of quantum billiards and related problems
- Authors: Matic Orel, Črt Lozej
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2610.32605v1  pdf=https://arxiv.org/pdf/2610.32605v1.pdf

Abstract:
We present QuantumBilliards.jl, an open-source Julia library providing a suite of numerical solvers for the two-dimensional interior Helmholtz eigenproblem with Dirichlet boundary conditions, a paradigmatic model in quantum chaos. The library implements conventional wavenumber-sweep techniques together with several accelerated eigensolvers: the Vergini--Saraceno scaling method, the expanded boundary integral method (EBIM), Beyn's contour-integral method, and the Compact Rational Krylov (CORK) method. It provides a common framework for constructing billiard geometries, exploiting discrete symmetries, computing eigenvalues and eigenstates, and treating smooth, cornered, and multiply connected domains. The library further includes reconstruction of eigenfunctions from boundary normal derivatives and the computation of Poincaré--Husimi (PH) phase-space representations.   Available at: https://github.com/Quantum-Chaos-Julia/QuantumBilliards.jl.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32610v1
- Title: Optimizing Quantum Battery via Counterdiabatic driving
- Authors: F. Ahmadi, S. Salimi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32610v1  pdf=https://arxiv.org/pdf/2610.32610v1.pdf

Abstract:
We analyze the energy charging of a quantum battery within an open quantum framework, where the interaction between the battery element and an external power source is mediated by an ancilla system acting as a controllable switch. Specifically, we investigate the charging and discharging dynamics of a cavity-based quantum battery coupled to a driven qubit functioning as the charger. To ensure lossless power transfer, we utilize an adiabatic evolution protocol. Furthermore, we implement counterdiabatic driving, achieved by applying an auxiliary control field to the original Hamiltonian, to suppress undesired transitions and realize fast adiabatic dynamics. This scheme significantly accelerates the charging process. We demonstrate that the charging efficiency under adiabatic evolution is enhanced and exhibits stable, non-oscillatory behavior, and we determine the optimal duration for the operation. Finally, we show that counterdiabatic driving minimizes the path length between the initial and final states, inducing the shortest possible evolution distance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32622v1
- Title: Trace-distance characterization of recurrent pairwise synchronization in cavity-coupled superconducting qubits
- Authors: Tiantian Huan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32622v1  pdf=https://arxiv.org/pdf/2610.32622v1.pdf

Abstract:
We theoretically investigate recurrent pairwise synchronization in three super?conducting qubits coupled to a common single-mode microwave cavity. The qubits interact indirectly through the cavity field and are driven by a coher?ent microwave field. We obtain the coherent dynamics in the dressed-state basis and quantify pairwise synchronization by the trace distance between reduced single-qubit density matrices. The trace-distance dynamics exhibit oscillatory wave-packet structures, with low-trace-distance regions identifying finite syn?chronization windows. An envelope-threshold procedure is introduced to extract the representative duration of these windows. By varying the middle-qubit coupling strength and the relative coupling ratio of the outer qubits, we con?struct a parameter-dependent map of the synchronization-window duration. The duration decreases rapidly with increasing relative outer-qubit coupling and becomes weakly dependent on the middle-qubit coupling in the stronger-coupling regime. These results provide a reduced-state-based characterization of coherent collective dynamics in multiqubit circuit-QED systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32634v1
- Title: From Link Availability to Deadline-Constrained Key Service: A Feasibility Framework for Mobile Free-Space Quantum Key Distribution
- Authors: Hasan Abbas Al-Mohammed
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32634v1  pdf=https://arxiv.org/pdf/2610.32634v1.pdf

Abstract:
Mobile free-space quantum key distribution (QKD) links can provide secret bits intermittently, whereas applications may need cryptographic key material at specified times. Optical feasibility, positive finite-key output, and deadline-compliant key service are consequently different claims. This technical note formalizes their separation through a time-indexed, security-qualified arrival process and a key-inventory model. Under explicitly stated assumptions, an elementary prefix-feasibility condition characterizes whether all demands can be served without borrowing keys from future contact windows. A stylized finite block model then illustrates why positive long-run optical availability does not ensure positive finite-key output when observations are fragmented into short contacts. Two transparent numerical examples distinguish total key yield from key delivery time and show the conditional benefit of pooling data across acquisition windows. The analysis is intended as a systems-level accounting and benchmarking framework, not a new QKD security proof or a demonstration of hardware performance. It identifies measurements and security assumptions needed to evaluate train, UAV, high-altitude-platform, and satellite-assisted optical QKD against application-level service requirements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32659v1
- Title: An Invitation to Algebraic Methods in Quantum Theory
- Authors: Peter T. J. Bradshaw, Jonte R. Hance
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2610.32659v1  pdf=https://arxiv.org/pdf/2610.32659v1.pdf

Abstract:
In this paper, we present various well-studied examples of quantum systems, and discuss how they might be analysed algebraically. We analyse the harmonic oscillator, hydrogenic atom, optical components, and particle spin using multiple algebraic methods, and highlight the central importance of algebraic relationships between operators in determining the physical character of the system. In particular, we show: the ubiquity of the Lie algebra $\mathfrak{so}(2,1)\cong\mathfrak{su}(1,1)$ as the ``spectrum generating algebra''; the role of $\mathfrak{su}(2)$ and $\mathfrak{su}(1,1)$ in determining the action of optical components; that an elementary algebraic approach to particle spin offers novel insights into its nature versus the usual approaches; and how understanding the full (often hidden) symmetry of a problem enables it to be solved immediately without the need to solve differential equations. We hope this work will serve as a gentle introduction to algebraic methods in quantum mechanics for the interested reader --- we therefore signpost active areas of research within the community.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32693v1
- Title: Elementary proofs of quantum lower bounds for element distinctness and k-sum
- Authors: Andris Ambainis, Martins Kokainis
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32693v1  pdf=https://arxiv.org/pdf/2610.32693v1.pdf

Abstract:
We give elementary proofs of the $Ω(n^{2/3})$ quantum query lower bound for element distinctness and the $Ω(n^{k/(k+1)})$ lower bound for the $k$-sum problem, for fixed $k$ and sufficiently large groups. The proofs use only basic properties of quantum states and linear algebra, analyzing the differences of algorithm states on different inputs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32724v1
- Title: Optimal probes for estimating the dephasing of a quantum spin system
- Authors: Leonardo Ratini, Stefano Carretta, Francesco Albarelli
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32724v1  pdf=https://arxiv.org/pdf/2610.32724v1.pdf

Abstract:
We investigate the optimal estimation of dephasing in finite-dimensional quantum spin systems. We first discuss some properties of the optimal probe states and present an efficient numerical algorithm to compute the optimal precision in dephasing estimation and identify the optimal probe states. For the dephasing channel arising from Gaussian phase diffusion, a spin cat state is known to be optimal for small dephasing. We analytically determine the range of dephasing strengths over which the cat state remains globally optimal for spins $J=1$ and $J=3/2$, and derive upper bounds on its optimality region for larger spins. We then compare numerically several probe states proposed in the literature, showing in particular that the simple class of probes obtained from uniform superpositions of all levels performs near-optimally for stronger dephasing. Finally, we apply our framework to a central-spin model coupled to a nuclear-spin bath, whose dynamics we simulate using the cluster-correlation expansion. Our results show that, while the cat state is optimal for weak Gaussian dephasing, pulse-controlled non-Markovian dynamics can favor states with amplitudes distributed over multiple spin levels, and in some cases the uniform state outperforms the other fixed probes considered. This shows how the choice of probe state depends both on the dephasing strength and on the dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32733v1
- Title: Entanglement Asymmetry and Asymmetry Contour under Boundary Symmetry Breaking
- Authors: Takahiro Orito, Daisuke Yamamoto
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2610.32733v1  pdf=https://arxiv.org/pdf/2610.32733v1.pdf

Abstract:
We investigate how symmetry-breaking boundary magnetic fields affect magnetization and Rényi-2 entanglement asymmetry (EA) in the transverse-field Ising model. For the ground state, magnetization exhibits qualitatively distinct behaviors in the ordered and disordered phases. EA also exhibits phase-dependent behavior, which is well captured by the lower and upper bounds derived in this work. In the critical regime, both magnetization and EA exhibit behavior qualitatively consistent with the field-theoretical predictions for a related setup. We also study boundary-quench dynamics and find that magnetization propagates from the boundary into the bulk with a velocity consistent with the maximum quasiparticle velocity. In contrast, because EA is a subsystem-integrated quantity, its spatial structure is not directly resolved. We therefore introduce the asymmetry contour, a contour-like finite-difference quantity that provides a spatially resolved characterization of the symmetry-breaking information encoded in the reduced density matrix. The resulting contour is complementary to the local magnetization, retaining sensitivity to nonlocal many-body correlations while its dynamics also reflects the underlying quasiparticle propagation. These results show how EA and its contour can provide complementary information-theoretic characterizations of symmetry breaking and its spatial structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32762v1
- Title: Quantum Machine Learning in Medical Imaging: A Primer for Radiologists
- Authors: Ruben Ortiz Cordero, Gaven K. Smart, Harshada Gothankar, Emilio Supsupin, Priya Bhosale, Mayur Virarkar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32762v1  pdf=https://arxiv.org/pdf/2610.32762v1.pdf

Abstract:
Deep learning has transformed radiology, but the computational cost of training and deploying modern models is outpacing what classical hardware can support. Quantum computing has been proposed as one response to this bottleneck: an n-qubit system can represent $2^n$ states simultaneously, although practical speedups require efficient algorithms, data encoding, and measurement strategies rather than superposition alone. This review introduces radiologists to five core quantum concepts, qubits, superposition, entanglement, quantum gates, and quantum circuits, and to the superconducting, trapped-ion, and photonic hardware platforms that define the current noisy intermediate-scale quantum (NISQ) era. We then summarize the quantum machine learning architectures most often applied to medical imaging (quantum support vector machines, quantum neural networks, variational quantum circuits, and quantum convolutional neural networks) and quantum image representations such as the flexible representation of quantum images (FRQI) and the novel enhanced quantum representation (NEQR). Reported applications include brain tumor classification and segmentation on MRI, pneumonia detection on chest radiographs, skin and breast lesion classification, CT and PET reconstruction, and ultrasound denoising. Nearly all published systems are hybrid quantum-classical pipelines evaluated on small, downsampled benchmark datasets or simulators, and clinical deployment is not yet feasible. We conclude with current limitations and translational priorities for radiology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32783v1
- Title: Bounding single-copy information causality violations
- Authors: Marco Pompili, Costantino Budroni
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32783v1  pdf=https://arxiv.org/pdf/2610.32783v1.pdf

Abstract:
Information causality is a physical principle that constrains bipartite post-quantum nonlocal correlations from information-theoretic assumptions. A direct characterization of the correlations satisfying it, however, remains difficult because the defining entropic condition must hold for all admissible protocols in the corresponding task. Here, we formulate the single-copy information causality problem as an optimization over all protocol parameters and simplify it by proving a deterministic reduction. We then show that generic adaptive multi-copy protocols can be represented as single-copy protocols applied to an effective behavior obtained by local wirings. As a consequence, for families of correlations closed under wirings, excluding single-copy violations suffices to exclude all finite-copy adaptive-protocol violations. We formulate the resulting membership and set-inclusion problems as optimization problems and discuss possible semidefinite programming relaxations. As an application, we study expansions of the information causality functional around zero-capacity channels, generalizing a method recently employed by Gachechiladze and Miklin to derive the Tsirelson--Landau--Masanes boundary from information causality. For expansions centered on channels whose output distribution has full support, imposing the second-order constraints for all single-copy protocols characterizes exactly the set of macroscopic locality in the CHSH scenario. Expanding instead around appropriate constant-output channels with perturbations that change the channel support, we show that every single-copy IC violation can be witnessed already at first order with a channel of arbitrarily small capacity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32812v1
- Title: Exploiting the Weyl-Chamber Structure for Hardware-Aware Quantum Circuit Compression
- Authors: Neel Misciasci, Isabel Nha Minh Le, Christian B. Mendl
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32812v1  pdf=https://arxiv.org/pdf/2610.32812v1.pdf

Abstract:
Quantum circuit compression based on tensor networks enables long-time simulation of quantum many-body dynamics on near-term hardware. While Riemannian optimization has been successfully employed for this purpose, it typically optimizes over the manifold of generic two-qubit unitaries. Consequently, the resulting gates must still be synthesized into the hardware's native gate set via KAK decomposition, an overhead that partially negates the original compression gain. We show that Riemannian-optimized gates already exhibit a predictable Weyl structure: near-$R_{ZZ}$ for the Ising model and near-fSim for the Heisenberg XXZ model. Building on this insight, we investigate whether parameterized optimization directly over the native gate set can offer a beneficial trade-off between expressivity and circuit efficiency by reducing the circuit's dimensionality. When comparing the two approaches, we find that the small residual Weyl parameters neglected by the latter are essential for high compression of the Ising propagator, whereas for the Heisenberg propagator, the native XXZ structure can be exploited directly to build a more efficient compressed circuit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32823v1
- Title: Minimal unitary representations of time-invariant causal quantum channels
- Authors: Antonius Jacobus Hasenack, Boris Škorić
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32823v1  pdf=https://arxiv.org/pdf/2610.32823v1.pdf

Abstract:
In this work, we study quantum channels that respect causality in single-input-single-output linear time-invariant systems. We show that positive semidefinite kernels satisfying certain analyticity constraints, which we call Schur-class kernels, provide a suitable description of such channels through multiplicative maps (Schur multipliers). Using the Moore-Aronszajn Theorem, we establish that these multipliers admit a minimal analytic Stinespring representation, which, in the unital case, is given by multiplication by a left inner function. We then relate the output rank of pure-state inputs to the dimension of the associated reproducing kernel Hilbert space. Using de Branges-Rovnyak realizations, we derive a stability criterion for the existence of two-sided inner completions of these vector-valued functions. We further show that the adjoint of the Julia embedding associated with the realization is minimal, and that its characteristic function essentially coincides with the canonical two-sided inner completion suggested by the Beurling-Lax-Halmos Theorem. Finally, we provide algorithms for explicitly computing minimal two-sided inner completions in the case of finite McMillan degree.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32838v1
- Title: Modular optical fault-tolerant quantum computation via an interface between verified resources and online logical operations
- Authors: Kosuke Fukui, Takaya Matsuura, Yohji Chin, Shohei Kiryu, Takaya Hoshi, Kan Takase, Warit Asavanant
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32838v1  pdf=https://arxiv.org/pdf/2610.32838v1.pdf

Abstract:
We introduce a factory--processor interface architecture for modular optical fault-tolerant quantum computation that separates code-dependent encoded-resource preparation from reusable online logical processing on a common Gaussian optical processor. Beyond encoded resources, the interface specifies logical outputs, code-to-mode mapping, measurement roles, frame updates, verification records, and resource-injection boundaries. As a concrete realization, we combine an offline verified Bell-resource factory based on a recursively concatenated $C_4$ code with physical Gottesman--Kitaev--Preskill (GKP) qubits with an online time-domain measurement-based quantum computation (MBQC) processor. Under the specified additive-displacement-noise model and fixed postselection policy, simulations support the finite-level logical Bell-error ordering $P_5<P_4<P_3<P_2$ at 12.25 dB of effective GKP displacement-noise quality, both with and without the prescribed additional post-injection displacement noise. At 15.6 dB and $L=2$, a separate fixed-sample evaluation gives one-sided 95$\%$ Clopper--Pearson upper bounds below $10^{-5}$ for both conditions under the binomial model. The interface supports address-tracked injection, transversal CNOT and logical Bell-measurement constructions, and logical SWAP and Hadamard constructions with tracked code permutations. Given advance resource preparation and sufficient routing parallelism, increasing the concatenation level expands parallel encoded-resource width without increasing the protected online sequence length of these constructions. These results identify a modular route to lower logical error rates while retaining a common Gaussian MBQC operation set with shallow online processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32841v1
- Title: Hardware-Friendly Estimation of LCU-Based Expectation Values via Quantum-to-Classical Workload Shifting
- Authors: Hari Hara Suthan Chittoor, Thirumalai Manimaran
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2610.32841v1  pdf=https://arxiv.org/pdf/2610.32841v1.pdf

Abstract:
Estimating the expectation value of an observable $O$ for a quantum state evolved under a general, possibly non-unitary, operator $A$ is a fundamental task in quantum simulation, chemistry, and variational algorithms. Existing linear-combination-of-unitaries (LCU) approaches implement $A$ on hardware, requiring ancilla qubits, controlled unitaries and, in randomized variants, fresh circuit executions for every Monte Carlo sample. These costs are prohibitive on NISQ and early fault-tolerant devices. We propose HERMES (Hardware-Efficient Reusable Measurements for Estimating LCU-based expectation valueS), which moves the processing of $A$ entirely to the classical domain. Expanding $A$ and $O$ in the Pauli basis and sampling pairs of Pauli terms classically, HERMES rewrites $μ= \mathrm{Tr}(OAρA^{\dagger})/\mathrm{Tr}(AρA^{\dagger})$ as a ratio of weighted sums of Pauli expectation values on the unmodified state $ρ$, with no ancillas, controlled unitaries, or quantum implementation of $A$. A two-level measurement reduction scheme (Pauli deduplication and commuting-group partitioning) bounds the number of distinct measurement settings independently of the sample count, unlike randomized LCU methods whose circuit executions grow linearly with it. On ground-state energy estimation of $\mathrm{H}_2$ and $\mathrm{LiH}$ via imaginary-time evolution, HERMES matches or beats Pauli single-ancilla LCU baseline using shallow circuits with no two-qubit gates beyond state preparation under qubit-wise commuting grouping. It is also more robust to noise and completes a noisy $\mathrm{LiH}$ simulation infeasible for the baseline, at the cost of classical overhead growing with the number of Pauli terms in $A$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32882v1
- Title: Fermion Scattering on Quantum Computers
- Authors: Steven Abel, Michael Spannowsky, Simon Williams
- Categories: quant-ph (primary); quant-ph; hep-ph; hep-th
- Links: abs=https://arxiv.org/abs/2610.32882v1  pdf=https://arxiv.org/pdf/2610.32882v1.pdf

Abstract:
Resonant scattering links particle interactions to the formation and decay of unstable excitations. We develop a hybrid quantum-computing framework to study these dynamics through fermion--antifermion collisions. Our formulation of $(1+1)$-dimensional Yukawa theory encodes fermions in qubits and the scalar field in qumodes. We identify the operations needed for a photonic implementation and benchmark the dynamics with tensor-network simulations. Near resonance, we resolve the build-up of a localised scalar excitation and the subsequent partial return of energy to the fermions. Enhanced entanglement accompanies this exchange. Time-dependent correlator measurements reproduce the analytically predicted decay rate to a few percent precision, with energy scans exhibiting a resonance peak consistent with packet-averaged Breit--Wigner behaviour. These results establish a concrete scattering benchmark for hybrid quantum computers and demonstrate how local real-time observables can probe particle-resonance dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32908v1
- Title: Nonclassicality from Incomplete Fock-State Statistics
- Authors: Martin Žonda, Pavel Baláž, Lukáš Lachman, Darren W. Moore, Tomáš Novotný, Radim Filip
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2610.32908v1  pdf=https://arxiv.org/pdf/2610.32908v1.pdf

Abstract:
Nonclassicality in bosonic systems can be certified directly from occupation probabilities without full state reconstruction. To complete a library of such criteria we introduce a numerical framework that constructs optimal linear nonclassicality witnesses from arbitrary subsets of measured occupation probabilities by solving a semi-infinite linear program. The method contains known analytical criteria as special cases while generally detecting substantially larger nonclassical regions. We provide an open-source implementation of the numerical optimization together with the analytical criteria discussed here, enabling direct application of the framework to measured occupation statistics across bosonic platforms. As a case study, we apply it to the resonant Jaynes--Cummings model with thermal states and reveal nonclassicality at short interaction times and close to thermal balance, where detection of nonclassicality is otherwise challenging.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32923v1
- Title: One-sided-DIQKD using any pure bipartite entangled state secure against all attacks
- Authors: Bohnishikha Ghosh, Chithra Raj, Shubhayan Sarkar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32923v1  pdf=https://arxiv.org/pdf/2610.32923v1.pdf

Abstract:
Quantum Key Distribution (QKD) allows spatially separated parties to establish a secret key among themselves based on quantum principles. While QKD systems are being deployed worldwide, their reliance on trusted measurements makes them vulnerable. Moreover, existing protocols have largely focussed on the qubit cases, and rely on the maximally entangled state, a costly resource to generate. Here, we consider the one-sided-device-independent (1SDI) QKD protocols, where one of the measurement devices is trusted while the other is untrusted. The resource in this scenario is quantum steering, an asymmetric form of quantum nonlocality. This is inspired by a real-world scenario, where the trusted party can be considered to be a bank, or any large organisation that has sufficient resources to protect its systems and validate them, while the users are vulnerable to attacks. We then demonstrate that a secure key can be obtained using any pure bipartite entangled state in this setup. Considering realistic detectors and sources based on current technology, we demonstrate that even states that are almost separable can be used to extract a secure key. Moreover, for every pure entangled bipartite state, we find the critical detection efficiencies and visibility to obtain a secure key.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32936v1
- Title: Generating entanglement in quantum matter with pathway-entangled photons via resonant inelastic X-ray scattering
- Authors: Chunjing Jia, Valentin Walther, Laimei Nie
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; physics.optics
- Links: abs=https://arxiv.org/abs/2610.32936v1  pdf=https://arxiv.org/pdf/2610.32936v1.pdf

Abstract:
Resonant inelastic X-ray scattering (RIXS) is conventionally used to probe elementary excitations and correlations in quantum materials. Here, we propose an interferometric RIXS protocol that instead creates entanglement between spatially separated regions of a solid-state material. An incident X-ray photon is coherently split by a beam splitter into two arms illuminating opposite ends of a sample. Recombining the scattered photons at a second beam splitter and detecting an energy-selected photon then projects the material into a coherent superposition of excitations at the two ends. This protocol is the X-ray, solid-state analogue of the Duan-Lukin-Cirac-Zoller (DLCZ) heralding scheme. Using a Kramers-Heisenberg formalism with quantized photon modes, we show that orthogonal and degenerate end excitations yield maximally entangled states. We illustrate this mechanism in three models: (1) two decoupled sites yield a heralded Bell state. (2) An open tight-binding chain exhibits reflection-parity-dependent interference, providing a benchmark for the interferometer's coherence. (3) A spin-1 Haldane (AKLT) chain yields an entangled pair of fractionalized edge spins. We also discuss practical considerations and challenges for realizing the protocol in X-ray experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32937v1
- Title: Certain Quantum States Already Require Quantum Time Evolution
- Authors: Joel D. Huber, Matthias Kleinmann
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32937v1  pdf=https://arxiv.org/pdf/2610.32937v1.pdf

Abstract:
Model-independent tests of quantum theory, such as Bell inequality violations, focus on static properties of the theory and do not rely on its dynamical aspects. Hence, this core part of quantum theory remains largely untested in a model-independent way. We show that the structure of quantum time evolution can be examined by testing the consistency between the state space and the dynamical laws. Considering a class of generalized phase-space theories, we find that certain quantum states can only be part of a theory if the time evolution is quantum: their evolution in anharmonic potentials would otherwise result in unphysical, negative marginal distributions. Furthermore, we demonstrate that the existence of the first excited state of a quantum harmonic oscillator is already sufficient to single out the Moyal bracket (quantum dynamics) to leading order in $\hbar^2$. We outline how theory-independent Wigner tomography of this state can be used to empirically exclude nonquantum dynamical theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32946v1
- Title: Low-frustration block encodings by patch routing
- Authors: Minzhao Liu, Abeynaya Gnanasekaran, Ananth Kaushik, Siddharth Hariprakash, Alireza Marefat Khah, Martin Roetteler, Grant Salton
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32946v1  pdf=https://arxiv.org/pdf/2610.32946v1.pdf

Abstract:
Block-encoding has emerged as a core primitive in many quantum algorithms, including quantum simulation. In this work, we design efficient and extensible methods for generating low-frustration block encodings of frustrated lattice Hamiltonians built from repeated local interaction patches through a technique we call "patch routing". We construct block encodings for a full Hamiltonian by first block-encoding a small local patch and then using a SWAP-style routing network to coherently apply the local patch encoding across the lattice. The expensive, local block-encoding cost is paid only once per query and is independent of lattice size, whereas the comparatively inexpensive routing network grows linearly with the lattice size, dominating at large sizes. Our method allows for a hierarchical structure in which larger patches can be block-encoded with small normalization factors, albeit at a higher (local, non-extensive) block-encoding cost, thereby reducing overall query complexity in an algorithm. We exploit symmetries and algebraic structures in local interactions to construct efficient block encodings, and we apply these techniques to the Heisenberg, Fermi-Hubbard, and honeycomb spin-liquid models. For a $120\times 120$ square-lattice $J_1$-$J_2$ Heisenberg model near maximal frustration ($J_2/J_1=0.4-0.6$), our methods result in a $15-17\times$ reduction in the leading $T$ cost per qubitized-QPE run (ignoring initial state preparation and overlap) relative to prior state-of-the-art Pauli LCU constructions. Corresponding reductions are approximately $3\times$ for the $120\times120$ Fermi-Hubbard model at half-filling. For time evolution of the honeycomb spin-liquid model on $120\times120$ unit cells, the leading cost is reduced by $5\times$. Our framework provides a systematic way forward for larger and more accurate fault-tolerant simulations of real-world quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32968v1
- Title: Distributed Quantum-Centric Supercomputing with Multi-Layered Generative Learning for Intermolecular Interactions
- Authors: Chayan Patra, Prayas Ghosh, Adwait Patkhedkar, Rahul Maitra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32968v1  pdf=https://arxiv.org/pdf/2610.32968v1.pdf

Abstract:
Quantum-centric supercomputing (QCSC) approaches, such as sample-based quantum diagonalization (SQD), combine quantum processors with high-performance computers (HPC), offering a promising route toward solving challenging electronic structure problems. However, implementation of QCSC approaches to large active space calculations is constrained by the associated number of qubits, deep quantum circuits, sampling cost, and large-scale Hamiltonian diagonalization. To overcome these limitations, we introduce a distributed QCSC framework that decomposes complex molecular problems into parallel sub-problems requiring fewer qubits, shallower circuits, and reduced shot budgets. A physically motivated, two-step aggregation scheme then reconstructs the global solution: first, a computational bit assignment strategy optimizes a cost function to appropriately map local bit indices to global ones, yielding a mapped tensor product state (MTPS); second, an inter-fragment correlation recovery module restores missing cross-fragment interactions. Herein, we employ a multi-layered generative machine learning architecture, starting with utilizing the recently proposed physics-informed generative SQD (PIGen-SQD) as a distributed QCSC solver, followed by a secondary generative module to model configuration distributions and identify dominant sectors of the global Hilbert space. For water and formamide dimers, our method achieves up to $95\%$ reduction in the diagonalization dimension while enhancing energy accuracy by an order of magnitude over conventional SQD. Furthermore, application to the water hexamer ($\mathrm{(H_2O)_6}$) cage successfully decomposes a 120-qubit problem into six 20-qubit monomeric subsystems, and stitches the monomers under a dimeric approximation, demonstrating excellent agreement with the reference classical methods.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32974v1
- Title: Maximal Orbital Entanglement from Non-Interacting Fermions
- Authors: Damiano Aliverti-Piuri, Julia Liebert, Christian Schilling
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.32974v1  pdf=https://arxiv.org/pdf/2610.32974v1.pdf

Abstract:
Orbital rotations are used in quantum many-body physics and chemistry to reduce the complexity of quantum states by compressing their correlation into a small set of relevant orbitals. In striking contrast, quantum information processing strives for the opposite: orbitals that maximize entanglement as a resource. Motivated by this, we prove that Slater determinants of $N$ fermions on a lattice of $d_A + d_B = d$ sites, although free of particle correlation, can carry up to $\min\{d_A, d_B, N, d-N\}$ ebits of orbital entanglement. Given enough particles and holes, this equals the maximum over all fermionic states. For arbitrary free states, we derive the maximal orbital total correlation in closed form for all bipartitions, the finest partition, and all partitions of up to five sites, using new majorization relations for Hermitian matrices. Taken together, these results turn mean-field states, the starting point of most many-body methods in physics and chemistry, into a viable resource for quantum information processing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31680v1
- Title: Local Thermodynamics and Rényi Bounds on Black Hole Mergers
- Authors: Sudhanva Joshi, Sunil Kumar Mishra
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2610.31680v1  pdf=https://arxiv.org/pdf/2610.31680v1.pdf

Abstract:
Rényi entropy inequalities have been proposed to strengthen the area-theorem bound on mergers of thermodynamically stable black holes in Anti de Sitter (AdS) space. The stronger bounds depend on the joint initial state, whereas masses and temperatures fix only its local thermal marginals. We quantify this distinction inside the canonical two-hole description. Correlations confined to rare energy fluctuations can leave both thermal states exactly intact and drive the trace distance and mutual information to zero, yet still change the joint Rényi entropy at leading semiclassical order. We determine the smallest entropy compatible with a controlled approach to statistical independence, uniformly over all positive Rényi orders up to one. For equal Schwarzschild--AdS$_4$ holes, the resulting optimized canonical mass constraint reduces to the area bound at leading semiclassical order. The reduction concerns only the information needed to infer a bound; it does not produce a lighter attainable remnant or a dynamical instability. Stronger merger constraints therefore require control of the initial correlations beyond single black hole thermodynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31717v1
- Title: In situ enhanced detectability of axions' responses in a microwave cavity
- Authors: Li Gao, Suirong He, Hao Zheng, Ni Chen, Xianing Feng, Qingquan Jiang, Jin Li, L. F. Wei
- Categories: hep-ph (primary); hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2610.31717v1  pdf=https://arxiv.org/pdf/2610.31717v1.pdf

Abstract:
Microwave cavities in strong magnetic fields are among the most sensitive detectors for axion dark matter detection. Its sensitivity, however, is fundamentally limited by the second order nature of axion photon energy conversion, which yields an extremely weak signal. Here we propose a feasible approach to break this limitation, by pre-exciting the target cavity mode to generate a first order power response signal in situ. The resulting signal amplitude scales linearly with the axion-photon coupling parameter, which is in sharp contrast to the quadratic scaling of conventional schemes, and is detectable via standard quadrature balanced homodyne detection system, even though its phase remains stochastic. Numerical simulations demonstrate that this pre-excited seed field can effectively suppress thermal noise, and thus the detection sensitivity of the system can approach the lower quantum noise limit. Consequently, the sensitivities predicted by the KSVZ and DFSZ models could be surpassed. This proposal might offer a pathway to a major leap in axion dark matter searches, as it is within reach of current technology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31811v1
- Title: Photoelectrons resolve the phase-dependent variance of bright squeezed vacuum
- Authors: Haoran Ma, Yihe Wang, Chuan Cheng, Ian Gabalski, Aaron M. Ghrist, Eleanor Weckwerth, Mohammed Th. Hassan, Philip H. Bucksbaum
- Categories: physics.atom-ph (primary); physics.atom-ph; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2610.31811v1  pdf=https://arxiv.org/pdf/2610.31811v1.pdf

Abstract:
The variance of bright squeezed vacuum (BSV) is not only strong but also phase dependent, yet recent strong-field experiments with BSV have recorded only its magnitude. A coherent field of the same color provides the phase reference that resolves this phase-dependent noise. Strong-field ionization of xenon by this light shows that the photoelectron yield follows the BSV quadrature along the coherent field, and that the nonlinearity of ionization amplifies the quadrature noise many times over in the electron yield. The noise is moreover distributed unevenly over the photoelectron momentum distribution, differing by an order of magnitude between ionization channels. Strong-field ionization thus offers a phase-sensitive, channel-resolved detector of quantum light, while the quadrature noise of quantum light offers a probe of the intensity dependence of individual ionization pathways.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31814v1
- Title: SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains
- Authors: Khadijeh Bagheri, Hassan Khodaiemehr, Chen Feng
- Categories: cs.CR (primary); cs.CR; cs.DC; cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2610.31814v1  pdf=https://arxiv.org/pdf/2610.31814v1.pdf

Abstract:
Permissioned blockchains authenticate transactions, votes and quorum certificates with computationally secure signatures, and post-quantum replacements inflate consensus traffic by orders of magnitude. Information-theoretic alternatives have required a trusted authority, quantum channels, per-signature interaction, or single-use keys with bounded transfer. We present SILMARILS-MV, a multi-verifier unconditionally secure signature in which a signature is the vector $α= A\,e(m)$ and each verifier holds a secret functional $c_i = Γ^T λ(x_i)$ derived from virtual anchors $Γ$ that nobody learns. Against unbounded adversaries corrupting up to $ω$ verifiers and any signers, and observing every decision, an honest verifier accepts a forged or invalid signature with probability at most $Q/q + 1/(q-1)$, a bound that is tight in its leading term. The scheme is strongly unforgeable, non-repudiable, transferable across unboundedly many hops, and linearly aggregatable. Keys are issued by the validators through perfectly secure MPC for $t < n/3$, without broadcast. To scale, we let the committee itself sign: in threshold notarization, finality certificates have constant size $32(ω+1)$ bytes and per-validator issuance cost no longer depends on $n$. Arbiter-verified keys give clients 32-byte signatures, robust redistribution supports membership changes and share refresh, and verifiers can be enrolled retroactively. A certificate verifies in 2.4 microseconds. In an analytic normal-case model at 1000 validators, threshold notarization needs 71 KiB of authentication traffic per validator per block, 22x less than ML-DSA-44 for admitted verifiers. In a Rust HotStuff prototype with 100 validators, SILMARILS-MV commits 2.8x more transactions per second than ML-DSA-44 with 67x less cryptographic CPU, and Monte-Carlo attacks match the bounds.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31824v1
- Title: A Topology-Aware Quantum-Classical Framework for Multi-Target Active Debris Removal using Gaussian Boson Sampling
- Authors: Komal Pandya, Saiyam Sakhuja, Nagaraj Kattian
- Categories: cs.CE (primary); cs.CE; cs.ET; quant-ph
- Links: abs=https://arxiv.org/abs/2610.31824v1  pdf=https://arxiv.org/pdf/2610.31824v1.pdf

Abstract:
The continued growth of orbital debris threatens the safety and sustainability of near-Earth space, making Active Debris Removal (ADR) an important mitigation strategy. Selecting $k$ targets from $N$ candidates yields a combinatorial search space of size $\binom{N}{k}$, making joint target selection and mission sequencing computationally demanding. We present a topology-aware quantum-classical framework integrating orbital mechanics, weighted orbital-transfer graphs, Gaussian Boson Sampling (GBS), and multi-objective evolutionary optimization. Seven target-prioritization strategies represent physical consequence, orbital persistence, conjunction risk, network centrality, community structure, inferred source families, and random selection. GBS generates candidate target subsets from the weighted graph, which are then evaluated using PyGMO-based evolutionary optimization to identify servicing sequences that jointly minimize total velocity increment ($Δv$) and mission duration, accounting for modeled timing, propulsion, and mass feasibility. We evaluate the framework across three benchmark environments, SOCRATES Minefield, Collision Cloud, and Random, with candidate-pool sizes $N\in\{15,18,22,25\}$ and target cardinalities $k\in\{3,5\}$. The experiments characterize how benchmark topology, prioritization strategy, and problem scale relate to sampling behavior and downstream mission performance. By separating candidate-subset generation from detailed trajectory optimization, the framework offers a topology-aware approach to focusing computational effort on a limited set of candidate ADR missions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32030v1
- Title: Can Spontaneous Time-Translation Symmetry Breaking Be Quantized Without Explicit Branches?
- Authors: Partha Nandi
- Categories: hep-th (primary); hep-th; gr-qc; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32030v1  pdf=https://arxiv.org/pdf/2610.32030v1.pdf

Abstract:
Can classically branched dynamics associated with spontaneous time-translation-symmetry breaking be quantized without explicitly retaining the branches of the Hamiltonian? We investigate this question using a reduced phase space. formulation in which the Hamiltonian is single-valued, while the critical structure of the classical Legendre map is encoded in a singular, momentum-dependent symplectic geometry. Quantization of the reduced Poisson algebra yields a deformed position-momentum commutator whose singularities determine distinct regular momentum sectors. Using the positive measure induced by the reduced symplectic structure, we identify a bounded central sector and two unbounded outer sectors. In the central sector, states with vanishing mean momentum obey a nonzero lower bound on position uncertainty, subject to the operator-domain assumptions of the representation. We further identify a possible field-theoretic connection with k-essence, where nonlinear scalar-field kinetics can produce finite-velocity degeneracies of the Legendre map. The relationship between the resulting reduced quantum description and branch-matching quantization remains unresolved and requires a comparison of the corresponding Hilbert spaces and operator domains.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32121v1
- Title: Material criteria for angular-momentum transfer from twisted photons to photoelectrons
- Authors: A. A. Shchepkin, D. V. Karlovets
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32121v1  pdf=https://arxiv.org/pdf/2610.32121v1.pdf

Abstract:
We study the material requirements for transferring the total-angular-momentum (TAM) projection of a twisted photon to the orbital angular momentum (OAM) of a photoelectron emitted from an $n$-type semiconductor surface. Within a single-valley effective-mass model of surface photoemission, we calculate OAM-resolved spectra for GaAs, InSb, $\mathrm{InAs}_{0.34}\mathrm{Sb}_{0.66}$, and $\mathrm{Hg}_{0.76}\mathrm{Cd}_{0.24}\mathrm{Te}$ irradiated by twisted photons with Laguerre--Gaussian--like momentum profile. The OAM transfer is characterized by the mean electron OAM, its root-mean-squared width, and the fraction of electrons with OAM-projection equal to the photon TAM-projection. Efficient transfer requires the transverse momentum of the conduction electron to be much smaller than the transverse momentum width of the photon, which favors low temperatures, small conduction-band effective masses, and shallow donor levels. GaAs is less favorable within the present model because of its larger effective mass and deeper donor levels. We also discuss the demanding photon-wave packet parameters, possible extensions to Dirac and Weyl semimetals, and post-emission OAM selection. Although the generation of vortex electrons with a vanishing OAM uncertainty via photoemission seems challenging, we argue that it is still possible to generate single-electron vortex states with a finite OAM dispersion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32123v1
- Title: Kinetic competition controls loss-induced exceptional points of Hubbard pairs
- Authors: Ho-Kin Tang, Xiaosen Yang
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32123v1  pdf=https://arxiv.org/pdf/2610.32123v1.pdf

Abstract:
Two-body loss can bind two fermions in a Hubbard lattice, yet the binding threshold in the infinite lattice need not be an exceptional point (EP). At fixed total momentum $\mathbf{K}$, the hops of the two particles interfere into a relative-motion hopping along each lattice direction, which sets the kinetic energy of the relative motion. On a hypercubic lattice, the threshold $g_c=1/[πρ_2(0)]$ is an EP precisely when the maximum kinetic energy along one direction exceeds the sum of the transverse maxima. This dominance keeps every transverse-momentum scattering channel propagating near the band center, making the local pair Green function purely imaginary there. Two real-energy scattering zeros associated with coherent perfect absorption then coalesce at the threshold into a second-order EP of the analytically continued pair problem, where loss restores the parity-time symmetry of the pair's scattering solutions. Without a dominant direction, binding occurs without coalescence and without breaking of that symmetry. Total momentum can therefore select EP sectors even on isotropic lattices. More broadly, the kinetic structure of the two-particle continuum determines whether loss-induced binding and exceptional degeneracy coincide.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32160v1
- Title: Single-step SU(3) Hahn Echo in a Qutrit Atom Interferometer
- Authors: Chirantan Mitra, Lucas Gabardos, François Impens, David Guéry-Odelin, David Wilkowski, Chang Chi Kwong
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32160v1  pdf=https://arxiv.org/pdf/2610.32160v1.pdf

Abstract:
The Hahn echo is a well-known dynamical decoupling method that refocuses the dephasing due to energy inhomogeneities of a spin-1/2 ensemble and is widely used to extend phase coherence in quantum computers and sensors. Extensions of such techniques beyond the spin-1/2 have been reported, but have mainly used SU(2) gates, limiting their scalability. Here, we generalize the Hahn echo to qutrits using single-step SU(3) gates and extend the coherence time by more than an order of magnitude. The gates are generated through optimal control theory and implemented in an ultracold atomic ensemble in free fall. A quantum process tomography procedure benchmarks the gates and yields fidelities of ~ 93%, limited mainly by state preparation and measurement errors. Due to the geometry of the laser beams, the generalized Hahn echo also realizes a three-path Mach-Zehnder atomic interferometer with two independent interferometric phase differences. Our results therefore establish SU(3) control for dynamical decoupling of qutrits and multi-path atom interferometers, with the latter opening the possibility for vector force measurements and interferometric tests of the validity of Born's rule.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32249v1
- Title: Bose-Einstein condensate in a shell: nonlinear modes and symmetry breaking
- Authors: Alexander Wolf, Vladimir V. Konotop, Maxim A. Efremov
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; nlin.PS; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32249v1  pdf=https://arxiv.org/pdf/2610.32249v1.pdf

Abstract:
The state of a quantum particle confined to a spherical surface is commonly described using spherical harmonics, which play a crucial role in solving many scientific problems featuring spherical symmetry. A mean-field description of a system of many interacting quantum particles confined to a spherical shell naturally leads to nonlinear generalizations of spherical harmonics. In this study, we analyze the emergence of such nonlinear modes in a shell-shaped Bose-Einstein condensate with both repulsive and attractive two-particle interactions. We find several classes of nonlinear modes. The first kind is an analytical continuation of a single spherical harmonic or their superposition for nonvanishing atom-atom interaction. Some of these solutions have planar counterparts in the form of Townes solitons and Townes vortices, which either appear stable even in the case of attractive interactions or can be stabilized by three-particle interactions. The second kind originate from symmetry-breaking bifurcations in the case of a repulsive interaction, and therefore have no linear counterparts. Moreover, we demonstrate the existence of a breathing dynamics that oscillates primarily between an unstable soliton and a stable vortex necklace state. Our findings show that the physics of nonlinear matter waves on curved geometries differs substantially from that in planar systems, suggesting the feasibility of observing these unconventional wave patterns experimentally.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32405v1
- Title: Quantum Landau Lifshitz Gilbert equation in ferromagnetic conductors and magnetic insulators
- Authors: Ji Yang Zhu, Zheng Chuan Wang
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32405v1  pdf=https://arxiv.org/pdf/2610.32405v1.pdf

Abstract:
Understanding the microscopic origin of magnetic damping is essential for describing magnetization dynamics in nanoscale magnetic systems. In this work, we develop a microscopic framework to derive Gilbert damping terms from specific interactions in ferromagnetic conductors and magnetic insulators. In ferromagnetic conductors, magnetic damping is dominated by the s d exchange interaction between the localized magnetic moments and the itinerant electrons, which is effectively equivalent to an electronmagnon interaction. From the spin diffusion equation and the spin transfer torque therein, we obtain the corresponding quantum LLG equation. In magnetic insulators, where free electrons are absent, spin phonon interactions become the primary source of the damping.Starting from an effective spin phonon interaction and using linear response theory, we derive a quantum LLG equation with a Gilbert damping tensor analytically. Our results demonstrate that different microscopic interactions lead to qualitatively different structures of magnetic damping. Instead of being described by a universal scalar parameter, Gilbert damping can exhibit spatial dependence and tensorial characteristics determined by the underlying microscopic interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32642v1
- Title: High-quality, deep formation and identification of oxygen-vacancy defects in silicon carbide
- Authors: Ryo Shiotani, Fu-Chieh Chuang, Mitsuaki Kaneko, Tetsuri Nishikawa, Hiroshi Abe, Taiga Matsuoka, Shigehito Miki, Kazuki Okajima, et al.
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32642v1  pdf=https://arxiv.org/pdf/2610.32642v1.pdf

Abstract:
Optically addressable paramagnetic defects in silicon carbide (SiC) are attractive for scalable quantum technologies such as quantum sensing. PL5, PL6, and PL7 are promising defects for their high brightness and spin-readout contrast. Although generation by oxygen implantation has been reported very recently, nonuniform spin and optical properties and the limited generation depth of implanted defects hinder both high-sensitivity sensing and conclusive microscopic identification. Here we engineer high-quality defects by decoupling oxygen incorporation and defect formation, realizing highly homogeneous spin-resonance frequencies as well as narrow optical linewidths and long T2* coherence time. Further, we demonstrate defect formation beyond the ion range utilizing oxygen diffusion, exceptional among impurities in SiC. We further provide hyperfine-interaction statistics of 17O and host nuclei across many PL6 defects, making the oxygen-vacancy origin conclusive. Together, the microscopic identification and the demonstrated formation route establish a foundation for developing the oxygen-vacancy spin defect into a versatile quantum platform.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32683v1
- Title: Stochastic and quantum autonomous information machine: efficiency fluctuations, precision and optimization
- Authors: Lucas Trigal, Gonzalo Manzano
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32683v1  pdf=https://arxiv.org/pdf/2610.32683v1.pdf

Abstract:
We investigate the conversion between thermal and informational resources in an autonomous machine coupled to thermal reservoirs and a tape, playing the role of an information reservoir. The machine is able to perform information erasure driven by heat, and information-powered refrigeration, for which we introduce suitable efficiency definitions. We focus on the role of fluctuations in the currents and stochastic efficiencies, as well as in operation at optimal performance. The model is also extended to allow a coherent information reservoir, which is able to modify operation and performance. All in all, our work provides insights for the design and optimization of information-to-work conversion devices at small scales.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32710v1
- Title: Discrete WKB approach to density profiles in inhomogeneous two-band free-fermion chains
- Authors: Federico Finkel, Artemio González-López, Martín Zapata
- Categories: cond-mat.str-el (primary); cond-mat.str-el; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32710v1  pdf=https://arxiv.org/pdf/2610.32710v1.pdf

Abstract:
We extend the discrete WKB method to one-dimensional bipartite tight-binding chains of free fermions with slowly varying hopping amplitudes and on-site potentials. We focus on the inhomogeneous Rice-Mele model, suggesting possible experimental realizations thereof in optical superlattices. We derive explicit semiclassical expressions for the single-particle wave functions and density of states, as well as the sublattice-resolved local particle densities and filling fraction at arbitrary Fermi energy. In particular, we show that the WKB density profiles agree with those obtained from the local-density approximation. We analyze the spatial dependence of the local band edges and its consequences for the global spectral structure, and clarify the role played by the phase-space topology in determining the Bohr-Sommerfeld quantization conditions. Finally, we illustrate our results with two representative examples: a homogeneous Rice-Mele chain subject to a harmonic trap and a fully inhomogeneous chain containing a domain wall.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.32973v1
- Title: Ideal interaction dynamics of defects and background fields in condensed matter
- Authors: François Gay-Balmaz, Tudor S. Ratiu, Cesare Tronci
- Categories: math-ph (primary); math-ph; cond-mat.soft; physics.flu-dyn; quant-ph
- Links: abs=https://arxiv.org/abs/2610.32973v1  pdf=https://arxiv.org/pdf/2610.32973v1.pdf

Abstract:
While defect dynamics in condensed matter systems is widely studied and several methods are available to track the defect position over time, the formulation of dynamical models for the coupled evolution of both defect and background field quantities seems to be more challenging. Yet, the overall behavior of a system containing moving defects is strongly influenced by this defect-field interaction. Here, we propose a modeling framework for the conservative coupled evolution of the defect density and the background fields upon focusing on two relevant cases of study: the Gross-Pitaevskii theory of quantum fluids and the Ericksen-Leslie model of nematic liquid crystals. To achieve the coupled evolution, we combine the Euler-Poincaré variational setting of continuum dynamics with the gauge theory of topological defects. While the latter allows us to overcome certain ambiguities in definition of the defect density, the Euler-Poincaré method provides a unified modeling approach in the absence of defect reconnection.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2309.10333v2
- Title: QubiC 2.0: An Extensible Open-Source Qubit Control System Capable of Mid-Circuit Measurement and Feed-Forward
- Authors: Yilun Xu, Gang Huang, Neelay Fruitwala, Neel R. Vora, Abhi D. Rajagopala, Akel Hashim, Larry Chen, Noah Goss, et al.
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.ins-det
- Links: abs=https://arxiv.org/abs/2309.10333v2  pdf=https://arxiv.org/pdf/2309.10333v2.pdf

Abstract:
Researchers manipulate and measure quantum processing units via the classical electronics control system. We developed an open-source FPGA-based quantum bit control system called QubiC for superconducting qubits. After years of qubit calibration and testing experience on QubiC 1.0, we recognized the need for mid-circuit measurement and feed-forward capabilities to implement advanced quantum algorithms, and upgraded the system to QubiC 2.0 on an AMD ZCU216 RFSoC evaluation board with all these enriched features. The system uses portable FPGA gateware with a simplified processor to handle commands on-the-fly. For design simplicity and straightforward scaling, we adopted a multi-core distributed architecture, assigning one processor core per qubit. The pulses combine the unique pulse envelope and carrier information specified in a command. Each pulse envelope is pre-stored in the FPGA's block RAMs, ensuring speed and reusability throughout the quantum circuit, while pulse parameters including amplitude, phase, and frequency can be updated from pulse to pulse. The software stack is developed in Python, running on both the FPGA's ARM core and a host computer via XML-RPC. Quantum circuits can be described in a high-level language supporting both pulse-level and native-gate-level programming with high-level control flow constructs, and are compiled into binary commands loaded into the FPGA. With QubiC 2.0, we achieved multi-FPGA synchronization and low-latency data communication, and demonstrated feed-forward experiments on conditional circuits. The system also serves as a platform for artificial intelligence and machine learning driven quantum control, such as FPGA-based real-time quantum state discrimination. The enhanced QubiC system provides researchers with powerful tools to explore and implement advanced quantum algorithms and applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2407.06072v2
- Title: Freezing and Shielding under Global Quenches for Long-Range Interacting Many-Body Systems
- Authors: Daniel Arrufat-Vicente, Nicolò Defenu
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2407.06072v2  pdf=https://arxiv.org/pdf/2407.06072v2.pdf

Abstract:
We investigate how local perturbations spread on long-range interacting spin chains and show how their nonequilibrium behavior exactly matches the one of a Fermi-Hubbard model with long-range hoppings. We then focus on the thermalization of the fermionic model following a sudden quench of local interactions between two distinct fermionic species. For both models, the quasiparticle spectrum consists of gapped low-energy levels, while the high-energy ones accumulate at a single point. When the low-energy gaps are large enough, turning on the local interactions does not effectively mix high- and low-energy modes, resulting in a freezing of the dynamical evolution. In general, the states within the excited subspace are shielded from the long-range signatures of the model, which are responsible for the low-energy extended states, and the dynamics effectively look as if long-range couplings were absent. This shielding mechanism becomes evident in the presence of disorder. It is shown that shielding and freezing are a universal feature of long-range interacting systems, and their relation to the existence of quasistationary states is conjectured.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2502.21055v2
- Title: Quantum-aware Transformer model for state classification
- Authors: Przemysław Sekuła, Michał Romaszewski, Przemysław Głomb, Michał Cholewa, Łukasz Pawela
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2502.21055v2  pdf=https://arxiv.org/pdf/2502.21055v2.pdf

Abstract:
Entanglement is a fundamental feature of quantum mechanics, playing a crucial role in quantum information processing. However, classifying entangled states, particularly in the mixed-state regime, remains a challenging problem, especially as system dimensions increase. In this work, we focus on bipartite quantum states and present a data-driven approach to entanglement classification using transformer-based neural networks. Our dataset consists of a diverse set of bipartite states, including pure separable states, Werner entangled states, general entangled states, and maximally entangled states. We pretrain the transformer in an unsupervised fashion by masking elements of vectorized Hermitian matrix representations of quantum states, allowing the model to learn structural properties of quantum density matrices. This approach enables the model to generalize entanglement characteristics across different classes of states. Once trained, our method achieves near-perfect classification accuracy, effectively distinguishing between separable and entangled states. Compared to previous Machine Learning, our method successfully adapts transformers for quantum state analysis, demonstrating their ability to systematically identify entanglement in bipartite systems. These results highlight the potential of modern machine learning techniques in automating entanglement detection and classification, bridging the gap between quantum information theory and artificial intelligence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2507.22117v2
- Title: A comprehensive benchmark of an Ising machine on the Max-Cut problem
- Authors: Salwa Shaglel, Markus Kirsch, Marten Winkler, Christian Münch, Stefan Walter, Fritz Schinkel, Martin Kliesch
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2507.22117v2  pdf=https://arxiv.org/pdf/2507.22117v2.pdf

Abstract:
QUBO formulations of combinatorial optimization problems allow for solving them using various quantum heuristics. While large-scale quantum computations are currently still out of reach, we can already numerically test such QUBO formulations on a perhaps surprisingly large scale. In this work, we benchmark Fujitsu's Digital Annealer (DA) on the Max-Cut problem, which captures the main complexity of the QUBO problem. We make a comprehensive benchmark against leading other heuristic algorithms on graphs with up to 53,000 variables by focusing on the wall-clock time. Moreover, we compare the DA performance against published performance results of the D-Wave hybrid quantum-classical annealer and the recently proposed QIS3 heuristic. Based on performance statistics for over 2,000 graphs from the MQLib, we find that the DA yields competitive results. We hope that this benchmark demonstrates the extent to which large QUBO instances can be heuristically solved today, yielding consistent results across different solvers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2508.17871v2
- Title: Succession of Ising criticality and its threshold in critical quantum Ising model subject to $X+ZZ$ decoherence
- Authors: Yoshihito Kuno, Takahiro Orito, Ikuo Ichinose
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2508.17871v2  pdf=https://arxiv.org/pdf/2508.17871v2.pdf

Abstract:
We investigate a mixed state quantum criticality in the Ising model under $X+ZZ$ decoherence. In the doubled Hilbert space formalism, the decohered state resides on the self-dual critical line of the quantum Ashkin-Teller (qAT) model, as a result of the specific choice of the decoherence channel. On the other hand, since the mixed state under $X+ZZ$ decoherence satisfies the Kramers-Wannier self-duality in a weak sense, the Ising criticality of the pure state can be partially preserved in the mixed system. By making use of the combination of the doubled Hilbert space formalism and matrix product states, a numerical study is carried out. We numerically find that, up to moderate decoherence strength, the behavior of the mixed states on the critical line is consistent with Ising-like scaling within the accessible system sizes, with the effective central charge and critical exponents close to the Ising-CFT values $c=1/2$, $η=1/4$, and $η_X=2$. Our results of the central charge and critical exponents contradict the ones in the $c=1$ orbifold boson CFT describing the critical state of the qAT model. In addition, we also numerically observe the flow of the central charge up to strong decoherence. The strong decoherence washes out the remnant Ising criticality and induces strong-to-weak spontaneous symmetry breaking.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2511.10921v2
- Title: MERA: A Mid-Circuit-Measurement Error-Aware Compilation Framework for Quantum Circuits
- Authors: Ming Zhong, Zhemin Zhang, Xiangyu Ren, Chenghong Zhu, Siyuan Niu, Zhiding Liang
- Categories: quant-ph (primary); quant-ph; cs.AR
- Links: abs=https://arxiv.org/abs/2511.10921v2  pdf=https://arxiv.org/pdf/2511.10921v2.pdf

Abstract:
Mid-circuit measurement (MCM) enables qubit reuse and dynamic control in quantum processors, underpinning resource-efficient algorithms and quantum error correction. However, MCM introduces non-negligible errors, including measurement-induced crosstalk, idling-qubit decoherence, and reset infidelity. Additionally, MCM error rates vary across qubits within the same processor, with some exhibiting substantially higher errors. Existing compilers, including Qiskit-compiler and QR-Map, ignore MCM error variations, leading to fidelity loss in circuits with frequent MCM operations.   In this paper, we present MERA, an MCM-error-aware quantum compilation framework that integrates MCM error modeling into the layout, routing, and scheduling stages. We first use the lightweight profiling method to capture a per-qubit MCM error distribution that remains stable for over 24 hours. The distribution guides MERA in applying MCM-error-aware layout and routing, while MERA further incorporates context-aware dynamic decoupling to improve fidelity. In evaluation, MERA delivers 24.94% -- 80.48% average fidelity gains over the Qiskit-compiler (optimization level 3) across different groups in selected benchmarks without additional SWAP overhead. It also boosts the fidelity of QR-Map-generated circuits by 29.26% on average (up to 122.58%), demonstrating its effectiveness for circuits with frequent MCM operations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2601.04732v2
- Title: The Role of Quantum in Hybrid Quantum-Classical Neural Networks: An Empirical Assessment
- Authors: Dominik Freinberger, Philipp Moser
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.LG
- Links: abs=https://arxiv.org/abs/2601.04732v2  pdf=https://arxiv.org/pdf/2601.04732v2.pdf

Abstract:
Quantum machine learning has emerged as a promising application domain for near-term quantum hardware, particularly through hybrid quantum-classical models that leverage both classical and quantum processing. Although numerous hybrid architectures have been proposed and demonstrated successfully on benchmark tasks, a significant open question remains regarding the specific contribution of quantum components to the overall performance of these models. In this work, we aim to shed light on the impact of quantum processing within hybrid quantum-classical neural network architectures through a rigorous statistical study under ideal, noise-free simulation. We systematically assess a selection of commonly used HQNN architectures on three binary medical classification tasks covering medical signal data as well as planar and volumetric images. In doing so, we examine the influence attributable to classical and quantum aspects such as encoding schemes, entanglement, and circuit size. Within this experimental setting, we find that in best-case scenarios, hybrid models show performance comparable to their classical counterparts. However, in most cases, performance metrics deteriorate when the investigated QNN components replace matched classical processing layers. Our multi-modal analysis provides empirical insights into the contributions of the tested quantum components and advocates for cautious claims and design choices for hybrid models in near-term applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2604.02854v3
- Title: Continuous-time evolution via probabilistic angle interpolation and its applications
- Authors: Tomoya Hayata, Yuta Kikuchi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.02854v3  pdf=https://arxiv.org/pdf/2604.02854v3.pdf

Abstract:
We explore the applicability of a stochastic time-evolution algorithm based on probabilistic angle interpolation. To simplify the pre-processing of the algorithm, we take the continuous-time limit, thereby explicitly eliminating Trotter errors and streamlining the resource analysis. We also introduce a noise-mitigation method tailored to it. As demonstrations, we apply the algorithm to two representative problems: estimating the ground-state energy of the $H_3^+$ molecular Hamiltonian and computing out-of-time-ordered correlators in the sparse Sachdev--Ye--Kitaev model. We evaluate the protocol's performance through numerical simulations and experiments on a trapped-ion quantum computer, Quantinuum Reimei.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2604.18119v2
- Title: Dissipative dynamics and superradiant countinuous time crystal in a Rydberg-interacting Dicke system
- Authors: Haohang Zhou, Xianfeng Chen, Luqi Yuan
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2604.18119v2  pdf=https://arxiv.org/pdf/2604.18119v2.pdf

Abstract:
The interplay between many-body interactions and controlled dissipation provides a rich setting for nonequilibrium quantum phases. We explore the superradiant phase transitions in a Rydberg-interacting open Dicke model with cavity loss and local dissipation. We find that the nonlinear feedback from atomic interactions stabilizes the atomic collective excited state and induces resonant collective motion, which can be further converted into robust superradiant oscillations with the inclusion of local dissipation. Beyond the mean-field approximation, we prove this system can support the finite-size local dissipative temporal order, i.e., continuous time crystal, from evidences of the decreasing damping of a finite-frequency Liouvillian mode and the linear-size scaling of quantum fluctuations. The correlation between the atomic colletive dynamics and the cavity photon number makes our findings easy to detect from output optical signal. By bridging interacting atomic matter and driven-dissipative cavity QED, our Rydberg-interacting Dicke model provides a unique spin-1/2 platform for exploring dynamical phase transitions and macroscopic temporal order in open quantum matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2604.26289v2
- Title: Recent Advances in Quantum Architecture Search
- Authors: Haozhen Situ, Zhimin He, Lvzhou Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.26289v2  pdf=https://arxiv.org/pdf/2604.26289v2.pdf

Abstract:
Variational quantum algorithms (VQAs) constitute a prominent paradigm for exploring the capabilities of near-term quantum computers. As the effectiveness of VQAs depends heavily on the design of variational quantum circuits, Quantum Architecture Search (QAS) has emerged as a critical research area to automate the discovery of high-performing circuit structures. This paper reviews key advancements in current research on QAS, including its core concepts, representative methodologies, applications, and emerging trends. The content is structured to ensure broad accessibility for a diverse audience of researchers while preserving the core principles of complex methodologies. In addition, we discuss remaining challenges and suggest potential research directions to offer perspectives on future exploration in this rapidly evolving field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2605.14523v2
- Title: HQTN-SER: Speech Emotion Recognition with Hybrid Quantum Tensor Networks
- Authors: Mahad Mohtashim, Nouhaila Innan, Muhammad Shafique
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.14523v2  pdf=https://arxiv.org/pdf/2605.14523v2.pdf

Abstract:
Speech emotion recognition (SER) remains fragile in real-world conditions because emotional cues are subtle, speaker-dependent, and easily confounded by recording variability, while high-performing deep models typically rely on large and carefully curated training sets. Quantum machine learning offers an alternative way to introduce nonlinear correlation modeling with compact modules, yet existing quantum SER studies remain limited, and the impact of circuit structure is not well understood. This paper presents HQTN-SER, a hybrid quantum-classical framework that investigates how quantum tensor network connectivity can support SER under small-qubit settings. HQTN-SER introduces (i) an MPS-inspired quantum tensor network module that enforces structured interactions to model correlations in speech representations with a small number of trainable parameters, and (ii) a fusion strategy that combines quantum measurement features with a learned classical latent embedding for end-to-end emotion classification. We evaluate HQTN-SER on three public benchmarks (RAVDESS, SAVEE, and MDER) under a unified preprocessing and training protocol. The proposed model achieves test accuracies of 80.09\% on RAVDESS, 78.12\% on SAVEE, and 73.51\% on MDER, with corresponding macro-F1 scores of 0.8012, 0.7826, and 0.7351, respectively. The model also exhibits stable convergence while using only three or four qubits, suggesting that MPS-inspired circuit structure can be an effective and hardware-aware design choice for quantum-assisted SER. These results provide a compact experimental baseline for studying structured quantum modules in affective computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2605.28055v2
- Title: Correlation Harvesting by Unruh--DeWitt Detectors in a Cylindrical Cavity: Entanglement, Mutual Information, and Quantum Discord
- Authors: Shagun Kaushal, Harkirat Singh Sahota
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.28055v2  pdf=https://arxiv.org/pdf/2605.28055v2.pdf

Abstract:
We study correlations between two Unruh--DeWitt detectors coupled to a massless scalar field confined inside a cylindrical cavity through entanglement negativity, mutual information and quantum discord measures. The entanglement negativity follows the free space behavior for small energy gaps and small separation, while it gets enhanced for large energy gap as the off-axis detector reach cavity boundary. The entanglement island, where negativity is nonzero, gets extended for large energy gaps as compared to free space and the detectors can get entangled for large separations when one of them is placed near cavity boundary. In contrast, quantum mutual information and quantum discord remain nonzero over a substantially broader parameter range, including regions in which the negativity has vanished. However, these correlations are suppressed inside the cavity as compared to the free space correlations. Therefore, boundary conditions can selectively reshape the structure of harvested correlations in quantum field theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2606.02421v2
- Title: Dynamics of the Density Cube
- Authors: Nabin Bhatta, Djordje Minic, Tatsu Takeuchi
- Categories: quant-ph (primary); quant-ph; hep-th; math-ph
- Links: abs=https://arxiv.org/abs/2606.02421v2  pdf=https://arxiv.org/pdf/2606.02421v2.pdf

Abstract:
Density cube theory extends the canonical quantum density matrix $ρ_{ij}$ with the addition of an extra index to $ρ_{ijk}$. The elements of the density cube with two different indices, $ρ_{iij}$ and $ρ_{ijj}$, correspond to the real and imaginary parts of the off-diagonal element $ρ_{ij}$ of the density matrix and describe double-path interference, while those with three different indices describe non-canonical triple-path interference. In this letter, we propose an equation of motion for the density cube, obtained from the quantization of ternary Nambu dynamics, and find that pairs of triple-path interferences oscillate into each other.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2606.28536v2
- Title: Pauli-Sparse regularised Counterdiabatic Shortcuts for Linear-Ramp QAOA
- Authors: Stefano Cipolla, Fabio Durastante
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2606.28536v2  pdf=https://arxiv.org/pdf/2606.28536v2.pdf

Abstract:
Combinatorial optimization is a leading target for quantum algorithms, but finite-depth QAOA can suffer from strong diabatic errors when the interpolation Hamiltonian has small, or exponentially small, spectral gaps. We propose a Pauli-sparse counterdiabatic extension of linear-ramp QAOA based on the regularised adiabatic gauge potential \[   \bigl(\mathcal L_H^2+ηI\bigr)A_λ^{(η)}   =   -\mathrm{i}\mathcal L_H(\partial_λH),   \qquad   \mathcal L_H(X)=[H,X]. \] Instead of computing a dense AGP, we solve this equation approximately by an inexact conjugate-gradient method in Pauli coordinates, truncating the Pauli expansion during the iteration to obtain a gate-budget-aware set of implementable rotations. The selected support is then improved by a Galerkin refit and certified by an a posteriori residual bound. The regularization parameter \(η\) acts as an energy-resolution scale: it suppresses transitions below \(\sqrtη\) while retaining larger-gap transitions. Thus, the method can avoid resolving exponentially small splittings inside a low-energy solution manifold while reducing leakage away from it. Numerical experiments on Ferromagnetic Chain (FC) and perturbed FC--MaxCut/MarketSplit instances show that the resulting LR-CD-QAOA ansatz improves approximation ratios over the uncorrected linear ramp, especially in regimes where LR-QAOA remains far from the optimum. Overall, the proposed regularized LR-CD-QAOA framework substantially broadens the practical applicability of QAOA to QUBO optimization by improving its robustness across heterogeneous problem landscapes, including instances with near-degenerate low-energy structures and small spectral gaps.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2609.06605v2
- Title: Solution-phase fluorination of nanodiamond: near-surface NV$^-$ activation and spin relaxation
- Authors: Szabolcs Czene, Olga Krafcsik, Nikoletta Jegenyés, Dávid Beke, László Péter, Vladimir Verkhovlyuk, Adam Gali
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2609.06605v2  pdf=https://arxiv.org/pdf/2609.06605v2.pdf

Abstract:
Nanodiamonds hosting luminescent point defects, known as fluorescent nanodiamonds (FND), are a leading platform for quantum technology. The nitrogen-vacancy (NV) centre is the most intensively studied of these; its negatively charged state (NV$^-$) can serve as a qubit at room temperature, and its stability is governed by surface functional groups. We present two solution-phase fluorination routes for stabilising NV$^-$: direct C-F bond formation by decarboxylation with xenon difluoride via a radical mechanism, and the Balz-Schiemann reaction, which replaces surface amino groups with fluorine. The two routes were compared by infrared, X-ray photoelectron, energy-dispersive X-ray, Raman and photoluminescence spectroscopy. Both gave a high NV$^-$ fraction, up to $\sim$85% on average, which to our knowledge is among the highest reported for surface-terminated nanodiamonds of this size and, in particular, for fluorine termination. We attribute the stabilisation to the fluorination treatment, which removes acceptor-like carboxyl groups and forms C-F bonds that give the surface a positive electron affinity. Frequency-domain relaxometry shows that the fluorinated particles retain a long spin-lattice relaxation time, $733\pm56$ and $712\pm20$ $μ$s for the XeF$_2$ and Balz-Schiemann routes, several times the values reported for commercial HPHT nanodiamonds, although shorter than the $1173\pm123$ $μ$s of the as-received material. Fluorination thus activates near-surface NV$^-$ centres, which dominate relaxometric sensing, at the cost of a moderate shortening of $T_1$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.06775v2
- Title: Engineering logical gates with irrep surface codes
- Authors: Yabo Li, Zijian Song, Vieri Mattei, Naren Manjunath, Apoorv Tiwari, Tyler D. Ellison
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2610.06775v2  pdf=https://arxiv.org/pdf/2610.06775v2.pdf

Abstract:
Fault-tolerant quantum computation can incur a substantial resource cost when a desired logical operation must be constructed from a restricted set of logical primitives. To make such operations directly available, we introduce irrep surface codes (ISCs), two-dimensional topological quantum error-correcting codes engineered to transversally implement a prescribed set of logical gates. The target logical gates only need to satisfy two conditions: (i) they generate a finite group, which, up to global phases, is forced by the Eastin-Knill theorem, and (ii) they are irreducible, meaning that any operator commuting with the set of gates must be proportional to the identity. This accommodates arbitrary finite groups of diagonal gates and arbitrary reversible classical gates, since each can be embedded into a larger irreducible finite group of gates. It also enables logical gates outside every finite level of the Clifford hierarchy. To incorporate these operations into surface-code computations, we further develop lattice-surgery protocols to transfer the encoded information between surface codes and ISCs obeying one of two sufficient conditions. Together, these results establish a systematic method for tailoring topological codes to desired logical operations and integrating them into conventional computations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.30216v2
- Title: Lean-QuantumAlg: A Framework for AI Agents to Produce Quantum Algorithms that Humans Can Trust
- Authors: Lei Zhang, Mingrui Jing, Yusheng Zhao, Jiahong Liu, Xin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.30216v2  pdf=https://arxiv.org/pdf/2610.30216v2.pdf

Abstract:
AI agents are increasingly capable of constructing quantum algorithms and proofs, yet machine-checked proofs alone cannot guarantee that the intended problem is solved or that resource claims match the verified computation. Here we introduce Lean-QuantumAlg, a Lean 4 framework for trustworthy AI-assisted development of quantum algorithms. Its Algorithm-Solves-Problem contract binds correctness, success probability, borrowed-state restoration and quantum and classical resource bounds to a single execution, while separating the guarantees that Lean checks from the problem specifications and execution models that humans review. We demonstrate the framework on nine AI-formalized quantum algorithms, from Grover search to quantum attacks on RSA-2048 and P-256, with less than 1% of each algorithm's imported source code requiring statement-level human review once the shared framework has been audited. By integrating reusable mathematical foundations, certified algorithmic primitives and execution-grounded verification, Lean-QuantumAlg provides a basis for AI agents to construct and certify quantum algorithms, opening a path toward scalable AI-driven discovery of quantum algorithms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2610.31554v2
- Title: ArcTN: Efficient Tensor-Network Contraction Planning for Quantum Circuit Simulation
- Authors: Zhengyi Liu, Li Liu, Songtao Liu, Xianglong Liu, Xiangzhen Zhou, Mingyu Huang, Dingchao Gao, Shenggang Ying, et al.
- Categories: quant-ph (primary); quant-ph; cs.MS
- Links: abs=https://arxiv.org/abs/2610.31554v2  pdf=https://arxiv.org/pdf/2610.31554v2.pdf

Abstract:
Tensor-network simulation of quantum circuits depends on contraction orders with low computational cost and small intermediate tensors, found without excessive planning time. We present ArcTN, a contraction-order optimization framework with two search presets. Light keeps planning overhead low, and Heavy spends more effort on refinement. Both combine randomized-greedy construction, subtree reconfiguration, and parallel tempering with stage-specific stopping rules. ArcTN also provides Fixed and Dynamic slicing to meet tensor-size limits and executes the returned orders. On the 30 QC32 quantum-circuit networks completed by all eight compared configurations, Light reduces FLOPs by 61.32% and plans 1.62$\times$ faster than Cotengra Auto/CMA-ES, and Heavy reduces FLOPs by 43.83% and plans 7.21$\times$ faster than Cotengra AutoHQ/Optuna. Heavy also needs 11.85% fewer FLOPs than OMECO TreeSA-8 and plans 1.33$\times$ faster. Dynamic slicing meets the size limits in all 90 runs on 18 scalar-output networks and reduces total sliced FLOPs by 31.99% relative to Fixed slicing, at the cost of longer planning. With a common NumPy executor, Heavy has the lowest combined planning and execution time among five configurations on the runs that all of them completed. On 672 networks built from 320 MQT Bench circuits, Heavy obtains the lowest geometric-mean FLOPs on the 142 large networks while planning 3.1$\times$ and 31$\times$ faster than Cotengra AutoHQ and Hyper128.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2504.06898v2
- Title: Identification and mitigation of errors in hole spin qubit readout
- Authors: Eoin Gerard Kelly, Leonardo Massai, Bence Hetényi, Marta Pita-Vidal, Alexei Orekhov, Cornelius Carlsson, Inga Seidler, Konstantinos Tsoukalas, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2504.06898v2  pdf=https://arxiv.org/pdf/2504.06898v2.pdf

Abstract:
High-fidelity readout of spin qubits in semiconductor quantum dots can be achieved by combining a radiofrequency charge sensor with spin-to-charge conversion and Pauli spin blockade. However, reaching high readout fidelities with hole spin qubits remains challenging due to site-dependent spin anisotropies and short relaxation times during readout. Here, we analyze the multiple error processes that arise during readout using a double-latched scheme in a germanium double quantum dot hole spin qubit system. We first investigate the spin-to-charge conversion process as a function of magnetic field orientation, and configure the system to adiabatically map the $\lvert \downarrow\downarrow \rangle$ state to the only non-blockaded state. We reveal a strong magnetic field strength dependence of the spin relaxation rates, and minimize it by operating at low fields. We further characterize and mitigate the error processes that arise during the double-latching process. By combining a radiofrequency charge sensor, a double-latching process, and optimized magnetic field parameters, we achieve a single-shot single-qubit state-preparation-and-measurement fidelity of 97.0% while maintaining control of both spins under the readout conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-26 14:05
- arXiv: 2605.04016v2
- Title: Entangling gates for the SU(N) anyons
- Authors: Sergey Mironov, Andrey Morozov
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2605.04016v2  pdf=https://arxiv.org/pdf/2605.04016v2.pdf

Abstract:
The model of a topological quantum computer is a promising one due to its natural resistance to noise and other errors. Operations in such a computer are implemented by braiding the trajectories of anyons. While it is easy to understand how to build one-qubit operations, two-qubit operations are more difficult. In arXiv:2412.20931 we suggested an approach to build such operations for a topological quantum computer based on SU(2) Chern-Simons theory with arbitrary level using cabling of knots. In this paper we discuss how this approach should be generalized to the SU(N) case, what the differences are, and which new problems arise.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36047v1
- Title: Symmetry-resolved fermionic correlations in iron-oxide ground spaces
- Authors: Federico Petrovich, Daniel Staros, Daniel N. Blaschke, Jian-Xin Zhu, M. Cerezo
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2610.36047v1  pdf=https://arxiv.org/pdf/2610.36047v1.pdf

Abstract:
Symmetries of quantum systems provide a natural way to organize the eigenspaces of many-body Hamiltonians. When degeneracies exist, however, they play a more subtle role as different sets of symmetry operators can resolve the same energy subspace into states with very different correlation properties. We study this interplay using a sequence of FeO and Fe$_2$O$_2$ models. For a Hubbard model of FeO, the ground space is 16-fold degenerate. Resolving it by local magnetizations gives a basis of Slater determinants, while total-spin quantum numbers select entangled and non-Gaussian states from the same ground manifold. Adding density-density Hund interactions breaks the independent spin rotations and reduces the ground space to a spin-reversal pair with maximal magnetization. These states are extremely close to Slater determinants in their natural occupations, yet have finite two-body cumulants and conserved-operator algebras whose orbit dimensions differ substantially from the Slater values. Fe$_2$O$_2$ provides a larger example in which spatial mode entanglement can be substantial while fermionic non-Gaussianity remains weak, with the conserved-operator structure again distinguishing the state from the corresponding Slater transformation class. Together, these examples show that symmetry resolution, mode entanglement, reduced-density-matrix correlations, and conserved-operator structure provide complementary information about interacting and degenerate electronic ground states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36067v1
- Title: Diagonal, Switching, and Locally Optimal Unraveling for efficient quantum trajectories in metastable open quantum systems
- Authors: Pietro Pacchioni, Alberto Mercurio, Patrick Winkel, Fabrizio Minganti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36067v1  pdf=https://arxiv.org/pdf/2610.36067v1.pdf

Abstract:
Open quantum systems can display metastability, with multiple long-lived states coexisting. Examples include the bistability of bright and dim manifolds in nonlinear driven resonators, or the long-lived coherent states of opposite phases in parametrically-driven systems, the building block of cat-state-based quantum computers. Metastability often emerges at system sizes where density-matrix evolution is impractical. Quantum trajectories mitigate this issue by evolving wavefunctions rather than density matrices. Metastable states then emerge as attractors towards which the system rapidly relaxes until a rare switching event brings it to another attractor. Simulating them remains costly, as one must resolve fast intra-attractor dynamics over timescales long enough to gather switching statistics. To tackle this problem, we introduce the Diagonal, Switching, and Locally Optimal Unraveling (DiSLOU) method, which combines three optimization layers: (i) Switching among locally optimal unravelings that minimize the number of quantum jumps in each metastable region. (ii) Diagonal propagation: the no-jump evolution is accelerated by diagonalizing the non-Hermitian effective Hamiltonian once per attractor. (iii) Local reduced eigenspaces: the no-jump state can be faithfully propagated in a truncated subspace of only slowly decaying eigenmodes. We benchmark DiSLOU on the driven-dissipative Kerr resonator, finding no measurable loss of accuracy and the largest speedup in the bistable regime, where standard trajectories are most expensive. We then apply the method to the more challenging problem of accurately simulating rare bit-flip events in the cat manifold emerging in a two-mode dissipatively stabilized parametric oscillator, obtaining a performance improvement of over one order of magnitude. An implementation of DiSLOU in Julia is available as an open-source package.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36070v1
- Title: Equilibrium Learning of Quantum Circuits
- Authors: Frank Barrows, Touheed Atif, Yiğit Subaşı, Tyler Volkoff
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36070v1  pdf=https://arxiv.org/pdf/2610.36070v1.pdf

Abstract:
Equilibrium learning trains a physical system using observables of its relaxed states. We extend this principle to gate-based quantum circuits by embedding a parametrized circuit in a Feynman-Kitaev (FK) Hamiltonian and imposing the compilation target either through an output clamping term or through a target-dependent cyclic condition on the clock register. The ground state energies and the overlaps of the corresponding ground states with the free history state define faithful cost functions for unitary and state compilation. We show that these costs are nonlinear functions of the compilation infidelity and therefore reshape the optimization landscape. We show that starting from the free history state, quantum phase estimation can prepare the relevant ground states and estimate the cost functions with polynomial resources. In two-qubit benchmarks, optimization with the equilibrium cost functions reaches a fixed fidelity threshold in fewer sweeps than standard compilation infidelity cost function for many instances. The results demonstrate the potential for encoding quantum learning problems as computation of equilibrium observables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36076v1
- Title: An algebraic characterisation of $n$-qubit pure-state invariants
- Authors: Markus Frembs
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2610.36076v1  pdf=https://arxiv.org/pdf/2610.36076v1.pdf

Abstract:
We study the set of $n$-qubit pure quantum states. Specifically, we consider their incarnation as density matrices in Bloch representation. Building on prior work, we define a family of quadratic functions in Pauli expectation values, and fully characterise all instances that result in state-independent purity constraints. The resulting family of pure-state invariants is surprisingly rich in structure, with strong ties to the geometry of symplectic polar spaces. After charting the general landscape, we define a sub-family of pure-state invariants that satisfies the dynamical constraint of being stable under state update. We prove that it corresponds with (different embeddings of) symplectic Lie algebras $\mathfrak{sp}(2^{n-1})\subset\mathfrak{su}(2^n)$, which admit a generating set of Pauli operators. We carefully distinguish the symplectic case from its orthogonal counterpart, using the Arf invariant of quadratic refinements of the symplectic form on the projective Pauli group, which we further identify with quaternionic structures on $\mathbb{C}^{2^n}$ that are both generated by and restricted to Pauli operators. As a consequence of this analysis, we reveal previously largely overlooked structure in the $n$-qubit Pauli group. We highlight this in a number of examples. We characterise all state-independent uncertainty relations in variance for Pauli observables, as well as all Pauli channels for which the output fidelity and output purity are state-independent. We further show that the orbits of the projective stabiliser groups of pure-state invariants, which for $n\geq2$ are proper subgroups of the Clifford group, form complex projective state $2$-designs, while their unitary lifts form symplectic $2$-designs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36156v1
- Title: Many-body entanglement quantification in arbitrary states through a few partial-transpose moments
- Authors: Sudip Chakrabarty, A. S. Majumdar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36156v1  pdf=https://arxiv.org/pdf/2610.36156v1.pdf

Abstract:
Can the entanglement of an arbitrary many-body state be quantified without reconstructing the state? We answer the question affirmatively by showing how the measure of logarithmic negativity can be estimated using a finite number of even partial transpose (PT) moments of a many-body state. Considering the squared PT spectrum as a probability measure, we solve exactly the task of a truncated Hausdorff moment problem with Gauss and Gauss-Radau quadrature. We obtain a hierarchy of lower bounds on the logarithmic negativity, which improves with increasing order of moments. Convergence to the exact value of the measure can be achieved for every state of finite dimension. We illustrate the bounds for ground states of three different interacting spin models, as well as for a thermal state. An error analysis demonstrates the efficacy of our scheme towards handling the limitation of finite statistics encountered in actual experiments with randomized measurements. Moreover, an example of density matrix renormalization group based numerical estimation is provided for handling system sizes beyond the scope of exact diagonalization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36167v1
- Title: Analog Quantum Experiments Meet Automatic Differentiation - from Programs to Atoms
- Authors: Yue Shi, Pengyu Liu, Yuxiang Peng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36167v1  pdf=https://arxiv.org/pdf/2610.36167v1.pdf

Abstract:
Gradient-based optimization of analog quantum hardware poses a concrete programming problem: given an executable experiment P(θ) that returns only measurement samples, what executable experiment should the system run to obtain (d/dθ_ell)P(θ)? Conventional automatic differentiation cannot propagate through the inaccessible quantum state, while finite differences require a noise-sensitive step size and analytic gradient identities cover only parts of an experiment. We present DiffSimuQ, which shows that a broad class of open-loop analog quantum experiments is closed under automatic differentiation. A compositional transformation maps P(θ) to a derivative program D_ell[P(θ)] in the same language whose expected outcome is exactly the derivative. Only continuous evolution requires a strategy-specific rule, and we give two realizations. Our Nyquist shift rule (NSR) applies to general time-dependent evolution: we prove that the observable response to shifting the Hamiltonian along its tangent is band-limited even for non-commuting controls, enabling exact reconstruction from shifted executions. For involutory generators, a parameter-shift realization (PSR) inserts a parameter-independent operation at a sampled time. Because derivative programs remain ordinary programs, source and derivative experiments share one compiler, which reuses the source realization, lowers branches to device-ready neutral-atom controls, and selects between NSR and PSR based on estimated cost. Under device noise, the exact derivative programs differentiate the objective realized by the device, with hardware realization errors treated separately. In machine-level noisy emulation, NSR and PSR avoid the finite-difference error floor and improve closed-loop optimization; they win in complementary cost regimes, while each derivative branch at 1000 qubits add at most 0.3% to source compilation time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36172v1
- Title: Quantum circuit simulation with high-order optical tensor processing
- Authors: Yufeng Zhang, Xuhan Guo, Zixuan Ning, Zhiliang Yuan, Yikai Su, Kaizhi Wang, Sergei Turitsyn, Zhipei Sun
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2610.36172v1  pdf=https://arxiv.org/pdf/2610.36172v1.pdf

Abstract:
Classical simulation is essential for developing and testing quantum circuits, but the exponential growth of Hilbert space challenges conventional digital processors. Here, we introduce a classical optical quantum simulation architecture that treats gates and batches of input states as independent tensor dimensions rather than separate simulation instances, while mapping eligible tensor network contractions onto the same processor. Using co-designed multidimensional encoding and readout across spatial and wavelength degrees of freedom, we experimentally realize high-order tensor-matrix multiplication in a single propagation and process all computational-basis inputs for each 4-qubit gate. Using a physics-based optical propagation model, we further numerically evaluate the architecture for the Deutsch algorithm and for the tensor network of all 128 target instances of a 7-qubit Grover algorithm. These results establish a unified framework for gate-state batch and tensor network simulation, providing a route to exploit optical concurrency across quantum simulation tasks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36233v1
- Title: Generation of quantum light with tunable Wigner negativity with a semiconductor quantum dot
- Authors: Hubert Lam, Petr Steindl, Yann Portella, Kiarn T. Laverick, Kian Hwee Lim, Juan R. Alvarez, Aristide Lemaitre, Maria Maffei, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.optics
- Links: abs=https://arxiv.org/abs/2610.36233v1  pdf=https://arxiv.org/pdf/2610.36233v1.pdf

Abstract:
Wigner-negative states of light are key resources for quantum advantage in continuous-variable optical quantum computing. They can be produced probabilistically via frequency conversion and photon detection, or deterministically by exploiting the single-photon nonlinearity of a quantum emitter. Here, we generate such Wigner-negative states of light with a tunable negativity using a single semiconductor quantum dot in a cavity. Optical coherent control of the quantum-dot transition allows to generate a quantum superposition of zero and one photon. The generated quantum states are characterized point-by-point in the phase space through homodyne measurement. The emergence of Wigner-function negativity is observed as the excitation power is increased. After correcting for collection and propagation losses, we obtain fidelities to the ideal state and quantum purities above 95%, together with near-optimal quadrature squeezing. The ability to generate a wide variety of Wigner-negative states with mature semiconductor technology opens promising opportunities for continuous-variable optical quantum technologies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36322v1
- Title: Experimental Geometric State Preparation on the Bloch Sphere Via Linear Mechanical Resonator
- Authors: Abrar N-E Faiaz, Donte McMullen, Kazi T Mahmood, M. Arif Hasan, Pierre Deymier, Keith Runge, Joshua A. Levine
- Categories: quant-ph (primary); quant-ph; physics.class-ph
- Links: abs=https://arxiv.org/abs/2610.36322v1  pdf=https://arxiv.org/pdf/2610.36322v1.pdf

Abstract:
The Bloch sphere representation, familiar from quantum two-level systems, can also describe classical linear systems whose dynamics are effectively confined to two modes. Here, we experimentally realize this framework in a linear two-mass, three-spring mechanical system by controlling superpositions of its symmetric and antisymmetric eigenmodes. The system is driven from both boundaries at a fixed frequency between the two resonances, so that the steady-state response remains within a two-mode manifold. By independently varying the relative amplitude and phase of the boundary excitations, we generate tunable modal superpositions. Scanning laser vibrometer measurements and frequency-domain analysis are used to extract the complex modal coefficients, which are then normalized and mapped onto Bloch sphere coordinates. This reconstruction reveals planar rotations of the state under phase sweeps and continuous steering between eigenstates under amplitude-ratio tuning. These results provide an experimental validation of Bloch sphere state reconstruction and steady-state geometric state preparation in a minimal linear mass-spring platform, establishing a simple classical testbed for exploring two-mode manifold dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36356v1
- Title: Probability bounds on trajectory-level exceedances of quantum speed limits under continuous-measurement feedback
- Authors: Kohei Kobayashi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36356v1  pdf=https://arxiv.org/pdf/2610.36356v1.pdf

Abstract:
We investigate the probability that a conditioned quantum trajectory exceeds an ensemble-derived quantum speed limit (QSL) velocity under continuous measurement-based feedback. Using the finite-time average fidelity velocity, we derive an upper bound on the exceedance probability in terms of its mean and variance. We further obtain state-independent bounds from uniform constraints on the fidelity drift and diffusion, including an exponential concentration bound. For a feedback-controlled qubit, we derive explicit model-specific bounds and show that they are nontrivial in a short-time regime. We also identify a finite-time regime in which the exceedance probability vanishes exactly due to the restricted support of the conditioned dynamics. Monte Carlo simulations confirm the analytical bounds and illustrate their tightness.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36365v1
- Title: Suppressing microwave crosstalk in superconducting quantum processors by designing parasitic drive capacitances
- Authors: Anuj Aggarwal, Jorge Fernández-Pendás, Simon Pettersson Fors, Zakaria Mohamed, Halldór Jakobsson, Amr Osman, Janka Biznárová, Andreas Nylander, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36365v1  pdf=https://arxiv.org/pdf/2610.36365v1.pdf

Abstract:
As superconducting quantum processors scale to large qubit counts, unwanted microwave drive crosstalk becomes an important source of coherent errors. Here, we investigate the role of parasitic coupling paths in the suppression of drive crosstalk in a processor with two fixed-frequency transmon qubits and a tunable coupler. To account for the many different coupling paths, we develop a detailed circuit model to capture the dependence of crosstalk on the coupler frequency. We experimentally demonstrate suppression of crosstalk, finding that the suppression does not originate solely from cancellation of the effective qubit-qubit coupling, but also is a result of interference between other coupling paths. Building on these insights, we show that drive crosstalk can be suppressed with the right choice of parasitic capacitances, which otherwise often are treated as unwanted design imperfections. Our results provide practical guidance for low-crosstalk device design of superconducting quantum processors and point toward a broader strategy in which parasitic coupling paths are engineered rather than simply minimized.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36385v1
- Title: Finite-temperature Quantum Quasinormal Mode Theory for Spatiotemporally-resolved Dissipative Cavity Quantum Magnonics
- Authors: Lars Meschede, Daniel D. A. Clarke, Ortwin Hess
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36385v1  pdf=https://arxiv.org/pdf/2610.36385v1.pdf

Abstract:
Cavity quantum magnonics has ushered in an unprecedented era of hybrid light-matter interfaces in which microwave photons, collective spin excitations, and superconducting or spin qubits can be coupled within a single device architecture, facilitating a versatile platform for quantum information processing. Realizing their full potential, however, requires a theory that can treat non-reciprocal magnetic media, material dissipation and open-cavity radiation losses, as well as finite-temperature fluctuations rigorously and without significant approximation. The dissipative magnonic resonances of such systems are described as quasinormal modes (QNMs), yet a consistent quantization procedure for lossy gyrotropic resonators has remained elusive. In this work, we present a finite-temperature quantum QNM theory, based on macroscopic quantum electrodynamics for non-reciprocal media and complex coordinate transformations, that achieves QNM quantization for a wide class of spatially inhomogeneous, dissipative and dispersive, cavity magnonic systems. We demonstrate the predictive capabilities of our theory via applications to hybrid dielectric-magnonic resonators interacting with both spin and superconducting qubits, evidencing modal interference effects, a continuous transition from coherent to dissipative coupling, spatiotemporal quantum field dynamics, and magnon-mediated qubit synchronization, at both zero and finite temperatures. By addressing the intricacies of modal loss and non-reciprocity in a fully quantum theory of cavity magnonics, our approach enables the quantitative design of hybrid quantum devices that operate under realistic open-system and thermal conditions, without recourse to ad hoc quantization schemes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36391v1
- Title: Consensus And Information Redistribution In Quantum Networks
- Authors: J. Novotný, D. Štěrba, I. Jex, H. -H. Kowalski, A. Abedi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36391v1  pdf=https://arxiv.org/pdf/2610.36391v1.pdf

Abstract:
Consensus algorithms are mechanisms driving nodes of a network to agreement. In quantum networks they also redistribute information encoded in the global quantum state, allowing global properties to be inferred from local measurements without reconstructing the global state. Motivated by this, we investigate decentralized quantum consensus in qudit networks governed by discrete random unitary dynamics. We characterize the analytic asymptotic dynamics, identify global information preserved by the evolution, and derive conditions for which different notions of quantum consensus emerge. A general theorem is derived that establishes a unified framework for extracting globally encoded information from local measurements beyond consensus states. First, we analyze CNOT networks and determine which global information can be recovered by individual nodes and which requires joint measurements on cooperating nodes. The CNOT model is well understood and presents a case with entanglement creation - a characteristic quantum feature of networks worth analyzing in detail. Second, we identify the complete class of two-qubit interactions that asymptotically achieve consensus on the average number of excitations, thereby establishing a quantum analogue of classical average consensus. We further show that joint measurements on k cooperating nodes recover exactly the first k moments of the excitation-number distribution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36421v1
- Title: Radial power-like potentials: from the Bohr-Sommerfeld $\ell \neq 0$ state energies to the exact ones
- Authors: J. C. del Valle, A. V. Turbiner
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2610.36421v1  pdf=https://arxiv.org/pdf/2610.36421v1.pdf

Abstract:
Two new Bohr-Sommerfeld (B-S) type quantization conditions for $d$-dimensional radial potentials are proposed for non-singular and singular potentials, respectively. The power-like potentials \hbox{$V=\operatorname{sign}(m)\,r^m$} for $m=-3/2,-1,-1/2, 1,3,4,6$ and $V=\log r$ (that corresponds to $m=0$) are studied in detail for radial quantum numbers $n_r \in [0,100]$ and for angular momenta $\ell=1,2,3,4,5$ in dimensions $d=2,3$. It is shown that for large $n_r$ the B-S energies $E_{BS}$ always tend to the exact ones. For $m=2$ (the radial harmonic oscillator) and $m=-1$ (the $d$-dimensional analogue of the $3D$ Coulomb potential) the B-S spectrum coincides with the exact one for the first and second quantization conditions, respectively. In general, up to a small parametric shift of the radial quantum number, the analytic formulas for the energy spectrum can be written for arbitrary power-like potential. A comparison of $E_{BS}$ with the energies $E^{(L)}_{BS}$, obtained for the radial potentials modified by the Langer correction for $d=3$, are in good agreement in general: in detail, it was checked for the quartic oscillator $V=r^4$. It is demonstrated that introducing a dimensionless {\it WKB correction} $γ$ into the r.h.s. of the proposed B-S type quantization condition allows us to reproduce the exact energies with $γ$ being very small for positive degrees $m \geq 0$ and sufficiently small for non-positive ones $m < 0$ for all $n_r, \ell$ studied.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36423v1
- Title: Coherent Optical Control of a Single Donor Electron Spin
- Authors: Yuxi Jiang, Amirehsan Alizadehherfati, Christine Falter, Jasvith R. Basani, Nils von den Driesch, Yurii Kutovyi, Jan Seelbinder, Alexander Pawlis, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36423v1  pdf=https://arxiv.org/pdf/2610.36423v1.pdf

Abstract:
Coherent spin-photon interfaces are essential for scalable quantum networks, but their realization requires optically bright transitions, long-lived spin coherence, and complete coherent control. Donor-bound electron spins in II-VI semiconductors offer an attractive platform for optically active spin qubits because they combine strong donor-bound exciton transitions in a direct-bandgap material with a potentially nuclear-spin-free environment. However, coherent control of an individual optically active donor spin has remained elusive. Here we demonstrate optical initialization, coherent control, and readout of a single donor-bound electron spin in ZnSe. Using spin-selective donor-bound exciton optical transitions, we initialize the electron spin and directly resolve its spin-relaxation dynamics. We achieve coherent spin control with off-resonant picosecond optical pulses, as demonstrated by spin Rabi oscillations and Ramsey interference. We further coherently drive two spin-selective optical transitions and observe high-contrast coherent population trapping, demonstrating the formation of an optically controlled dark state. At higher driving strengths, multiple dark resonances reveal the hyperfine interaction between the electron and the I = 3/2 Cl nucleus. These results establish the first coherent optical control of a single donor electron spin in a II-VI semiconductor and identify isolated optical donors as a promising platform for solid-state optically active qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36438v1
- Title: Dynamical behaviour of the mass tensor in the lattice
- Authors: Josué Calle, Diego Sanjinés, Evaristo Mamani
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36438v1  pdf=https://arxiv.org/pdf/2610.36438v1.pdf

Abstract:
We study with the semiclassical model the dynamics of a particle moving in a orthorrombic lattice by the hopping mechanism in the presence of a static Coulomb field and a rapidly oscillating homogeneous field. Based on results for the anisotropic Kepler problem, where a chaotic trajectory arises due to different masses of the particle in the X and Y directions, and since this result is also obtained in the rectangular lattice at the continuum limit, the application of the oscillating field allows reparameterizing the effective masses so that they become equal in both directions. Thus, the result is an elliptic trajectory in the continuum limit of the lattice. This chaos-order transition is confirmed by the calculation of Lyapunov exponents for the different trajectories. It is also found that the application of an external magnetic field in the Z direction of the lattice yields chaos control which can be generalized beyond the simple case of the circular trajectory shown in this work. The previous scheme of chaos control was extended for trajectories in 3D in the continuum limit of the orthorrombic lattice which is also equivalent to the far region approximation where the particle moves with respect to the Coulomb field origin. In this case it found that the chaos control technique permits to observe two different dynamical regimes which, although consistent with Bohr-van Leeuwen theorem, suggests that an observable way to distinguish one from the other is to be sought.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36521v1
- Title: Anomalous Structures of Fisher Zero Lines in Biorthogonal Dynamical Quantum Phase Transitions
- Authors: Wen-Hui Nie, Chong Li, Lin-Cheng Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36521v1  pdf=https://arxiv.org/pdf/2610.36521v1.pdf

Abstract:
Fisher zero lines of the Loschmidt amplitude in non-Hermitian quenches can exhibit anomalous structures in the complex time plane, such as divergence, separation, and the restriction of all branches or a specific branch to the real or imaginary axis. Here, we use the biorthogonal framework to reveal the origin of these structures and determine the corresponding critical momentum conditions by analyzing the values of $m_k=\hat{\mathbf{h}}_0\cdot\hat{\mathbf{h}}_1$, the dot product between the normalized prequench and postquench complex Bloch vectors. When Fisher zeros continuously cover the real-time axis, the density of Fisher zeros is further introduced to identify the critical times within these critical regions, at which the rate function becomes nonanalytic. We verify our results in a generalized non-Hermitian SSH model by quenching the Peierls phase and the non-Hermitian gain-loss strength, and also use the Jordan form to analyze the dynamics at postquench exceptional points, where the conventional Fisher zero formula is not applicable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36525v1
- Title: Minimal Projective Measurement Settings for Estimating Multiple Observables
- Authors: Yibin Huang, Muchun Yang, D. L. Zhou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36525v1  pdf=https://arxiv.org/pdf/2610.36525v1.pdf

Abstract:
We study the minimum number of orthogonal projective measurement settings needed to estimate multiple observables without bias for arbitrary input states. We derive structural bounds that go beyond dimension counting and combine them with explicit constructions to certify minimum setting counts for selected target spaces. A classical variational algorithm searches for shared measurement bases and optimizes their readout coefficients and sample allocation. For the collective first and second moments of two qubits, we certify that four projective settings are necessary and sufficient. For this task, a numerically optimized four-setting design achieves a Haar-averaged variance within approximately $0.0341\%$ of a lower bound valid for any number of projective settings in our fixed-allocation, unbiased linear estimation model. Numerical examples show that shared measurements can improve precision relative to the comparison protocols. For finite-depth circuits, we account for reconstruction bias and identify finite-sample regimes in which this advantage persists.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36597v1
- Title: Effective Noise Thresholds for Reliable Quantum Approximation Optimisation Algorithm under Noisy Environment
- Authors: Yozef Tjandra, Hendrik Santoso Sugiarto, Celine Vania Setiadi, Joanna Gracia Tan, Andriyan Bayu Suksmono
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2610.36597v1  pdf=https://arxiv.org/pdf/2610.36597v1.pdf

Abstract:
Variational quantum algorithms are leading candidates for practical utilisation on noisy intermediate-scale quantum (NISQ) processors, but accumulating noise bounds the usefulness of circuit depths. For the quantum approximate optimisation algorithm (QAOA), this trade-off has mostly been addressed by searching for the best depth for a given device. In this work, we consider the inverse question: how much noise each depth can tolerate. Using GPU-accelerated noisy QAOA simulations for MaxCut on three graph families with 6 to 18 vertices, depths up to 10 and three noise channels, we fit the approximation ratios with a generalised logistic surface. We propose the effective noise threshold as the inflection boundary of the logistic surfaces, a noise boundary separating reliable and unreliable QAOA approximation regimes. In general, the threshold decreases as depth rises, indicating that deeper circuits demand for stricter noise requirement for reliable approximation. Its best and worst values over depth divide the noise axis into three regions: every depth remains effective, depth must be chosen with care, or no depth induces effective optimisation. Assessing on the ibm_marrakesh processor, although modelled gate errors understate factual noise, the threshold modeling remains beneficial in informing qualitative depth-dependence structure and identifying dominating noise channel in noisy QAOA.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36663v1
- Title: Diagnostic-dependent lasting Mpemba effect in a parametrically driven oscillator
- Authors: Shu He
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36663v1  pdf=https://arxiv.org/pdf/2610.36663v1.pdf

Abstract:
For two Gaussian preparations of a detuned degenerate parametric amplifier below threshold, the trace distance shows a lasting Mpemba reversal, whereas the relative entropy eventually restores the initial order and the Hilbert--Schmidt distance alternates indefinitely. All three diagnostics agree on the initial order, and these orders persist on open sets of preparations and quadratic generators. The disagreement is possible because a real relaxation mode and a complex-conjugate pair share the leading decay rate, a coincidence that holds for any single-mode quadratic oscillator with linear damping in the elliptic regime. Number symmetry hides their competition in the undriven trace-distance tail, and parametric driving exposes it. Near a pure stationary state, the relative entropy strongly weights changes of the symplectic eigenvalue, which approximately follow the nonoscillating energy deviation; thermal occupation weakens this preference. A first-order splitting rule shows that weak number dephasing and two-photon loss favor the real branch, whereas a Kerr interaction with the same sign as the detuning favors the pair. We quantify the thermal-occupation and dephasing tolerances and estimate the measurement precision needed to observe the disagreement. Whether a Mpemba reversal is lasting therefore depends on the diagnostic and on the observation window.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36680v1
- Title: Quantum State Preparation for Complex-Valued Amplitudes
- Authors: Fred Sun
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36680v1  pdf=https://arxiv.org/pdf/2610.36680v1.pdf

Abstract:
We present a state preparation procedure that takes binary registers containing the real and imaginary parts of a complex number $z=x+iy$ and prepares an amplitude approximating $z/α$, where $α$ is a normalization constant. The magnitude and argument are computed using the Coordinate Rotation Digital Computer (CORDIC) algorithm. We then encode the magnitude into an amplitude, and apply phase gates to introduce the argument. A reversible in-place multiplier allows the coordinate updates to use fixed precision while clearing their temporary workspace. The procedure uses $O(n^2)$ $T$ gates and $O(n)$ additional qubits. Compared with separately encoding the real and imaginary parts and combining them through LCU, the construction can allow a smaller normalization and reduce amplitude-amplification costs. The computed polar representation also remains available for further arithmetic before amplitude-encoding.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36704v1
- Title: Controlled Dark-State Energy Storage and Work Extraction in V-Type Quantum Batteries
- Authors: Chia-Hung Chu, H. H. Jen
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2610.36704v1  pdf=https://arxiv.org/pdf/2610.36704v1.pdf

Abstract:
The performance of a quantum battery depends not only on its ability to retain stored energy against unwanted discharge but also on the amount of useful work that can be extracted from it. Here, we investigate these complementary aspects in an ensemble of V-type qutrits coupled to a lossy cavity. By applying a finite splitting pulse to the two excited states of each qutrit, cavity-bright excitations are converted into atomic dark states, whose populations remain protected upon restoring degeneracy, even while the light-matter coupling remains active. Simulations with finite-duration pulses reveal a capture window governed by the competition among energy transfer, bright-to-dark conversion, and photon leakage. We further show that if the energy is stored in the fully symmetric atomic subspace, the passive energy is bounded by twice the transition energy for number of atoms $N\geq2$. Consequently, if the stored energy scales extensively with $N$, the ratio of extractable work to stored energy approaches unity in the thermodynamic limit. Comparing different initial preparations at equal mean input energy, we find that coherent-state can yield greater finite-time ergotropy despite capturing less energy, whereas Fock-state favors greater extractable work in the stationary component. Our results demonstrate how controlled dark-state population trapping in an atom-cavity coupled system can protect stored energy while providing a conditional route toward high extractable work.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36754v1
- Title: A Unified Protocol for Arbitrary Z Rotations of a Class of Bosonic cQED Qubits
- Authors: Vahid Shaghaghi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36754v1  pdf=https://arxiv.org/pdf/2610.36754v1.pdf

Abstract:
Bosonic-qubit encodings provide diverse approaches to storing and processing quantum information, with logical operations often implemented through encoding-specific physical strategies. Here, we identify a class of bosonic Fock-based qubits in circuit QED for which distinct implementations of arbitrary Z rotations share a common structure. We formulate this structure as a six-step protocol that provides a unified procedure for implementing arbitrary Z rotations across this class of bosonic cQED qubits. The applicability of the protocol is determined by a specific condition on the encoding, providing a criterion for identifying bosonic Fock-based cQED qubits that admit the common implementation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36936v1
- Title: Qubit-environment entanglement in pure dephasing dynamics for mixed initial states
- Authors: Małgorzata Strzałka, Nico Peters, Laura Ares, Jan Sperling, Katarzyna Roszak
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36936v1  pdf=https://arxiv.org/pdf/2610.36936v1.pdf

Abstract:
Decoherence of qubits is one main limitation in quantum information processing, where the qubits themselves can be mixed because of decoherence and additional decoherence may generated through interactions with a bath. Here, we present a complete study of qubit-environment entanglement in the case of interactions that lead to pure dephasing of the qubit by allowing the initial state of the qubit to be mixed, exceeding previous restrictions. We find that the criteria for separability that hold for pure initial states of the qubit are reduced to witness status. Yet, the evolution of the witnesses reflects the array of features that entanglement can exhibit in the mixed case but are forbidden in the pure-qubit case. Most notably, this includes sudden birth of entanglement as the initial phase of the evolution is typically separable. Moreover, there is a stark numerical advantage to the study of entanglement for large environments when using the witness rather than the traditional measures available. We include the study of entanglement generated between a spin qubit and a sparse spin environment to illustrate the peculiarities of the evolution of entanglement in this case, as well as to emphasize the level of reliability of the entanglement witness.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36963v1
- Title: Correlation-sensitive magic-state distillation from spin-squeezed neutral atoms
- Authors: Ximo Wang, Ruyue Guo, Xinbo Li, Min Feng, Haozhe Wang, Zhenqi Bai, Yichi Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36963v1  pdf=https://arxiv.org/pdf/2610.36963v1.pdf

Abstract:
We show that interblock correlations can reverse magic-state distillation even when every input exceeds the threshold for independent states. For the five-to-one Bravyi-Kitaev protocol with independent local Clifford twirls, we express the output in terms of measurable target-axis moments. Fourth-order correlations determine acceptance, while third- and fifth-order correlations determine the output polarization. This relation yields a direct sign test for distillation gain and opposite gains for inputs with identical single-qubit and two-qubit reduced states. We connect this mechanism to neutral-atom resource preparation through finite-range Ising dynamics. Block separation suppresses detrimental interblock coupling, and locally addressed Clifford phases release interaction-generated magic from a spin-squeezed precursor by changing the symmetry selected by code projection. A protocol that retains accepted source outputs achieves positive gain above a source-contrast threshold set by circuit errors and storage dephasing. The same moments specify a finite-sample experimental diagnostic. These results connect the correlation structure of a resource state to its preparation, acceptance, and distillation gain.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36965v1
- Title: From QCCD Trapped-Ion Hardware to Quantum Compilers: Capabilities, Architectures, and Compilation
- Authors: Ludwig Schmid, Jurek Eisinger, Daniel Schoenberger, Christian D. Marciniak, Janine Hilder, Ulrich Poschinger, Robert Wille, Ferdinand Schmidt-Kaler
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36965v1  pdf=https://arxiv.org/pdf/2610.36965v1.pdf

Abstract:
Shuttling-based trapped-ion quantum computers (QCCD) rank among the most mature hardware platforms. Existing and envisaged devices exhibit architectural differences in terms of register layout and connectivity. Platform-specific compilers are required to translate quantum circuits into resource-optimized hardware-level command chains. Hardware platforms and compiler software stacks are mostly developed independently of one another by different research communities. This work aims to bridge these communities by abstracting QCCD architectures and native operations, enabling computer scientists to address compilation problems using generic methods without requiring a deep background in the physical operating principles of the platform. The resulting design space is organized into a small set of architectural archetypes, each posing its own compilation problem. We then select and apply compilation methods to one- and two-dimensional QCCD architectures, finding that the routing overhead scales approximately cubically with the number of qubits for the one-dimensional architecture and approximately quadratically for the two-dimensional one. Extending this to compilation with a quantum error-correction layer reveals additional differences and similarities between the physical and logical levels. We conclude that co-design is a requirement rather than an option, and this work provides the vocabulary, archetypes, and compilation abstraction it needs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36972v1
- Title: Quantum and Classical Memory for Storage and Retrieval of Quantum Measurements
- Authors: Filip Turoboś, Ludmiła Marcinkowska, Zbigniew Puchała
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.36972v1  pdf=https://arxiv.org/pdf/2610.36972v1.pdf

Abstract:
We study the persistent quantum and classical memory required for exact heralded storage and retrieval of quantum measurements. Given only black-box access to the measurement channel, we construct an exact compression of the port-based program into an outcome-type record and a quantum register, with total dimension polynomial in the query count. For every universal retrieval processor we prove the bounds $Q+C\ge\log_2 n$ and $2Q+C\ge\log_2\bigl((n-1)d^2+1\bigr)$ on the numbers $Q$ of qubits and $C$ of bits of the program, for $n$-outcome POVMs on $\mathbb{C}^d$ with $d\ge2$. For $n\ge2$, no finite classical memory removes the need for quantum memory: any such processor requires a quantum program of dimension at least $d$, at that dimension its classical alphabet must have at least $n$ symbols, and both minima are attained by a single-query protocol with success $1/d^2$. Combining direct-program compression with a converse from approximate measurement programming gives logarithmic total-memory scaling in $1/(1-p)$ as the uniform success probability $p$ approaches one, at fixed $d,n\ge2$. At fixed input dimension and target success below one, the optimal total-memory scaling is logarithmic in $n$. We also construct self-contained programs under branch-decomposition access and compare the quantum and classical costs of all constructions, including where the outcome-type record is kept: for POVMs with $n$ nonzero rank-one effects the direct program admits a purely quantum allocation whose register is never larger than that of the minimal-Naimark unitary program and which succeeds more often whenever $n>d$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36984v1
- Title: Quantum Evolution Kernel for Node-Attributed Graphs
- Authors: Manuel Padovani, Alessandra Di Pierro, Claudia Daffara
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2610.36984v1  pdf=https://arxiv.org/pdf/2610.36984v1.pdf

Abstract:
We present a novel approach to embed node-attributed graphs onto neutral-atom quantum computers, and propose an application to digit recognition. Our approach extends PASQAL's quantum evolution kernel (QEK) by introducing a node-level feature encoding based on three-level quantum states. To this purpose, we present a prototype showing how the resulting embedding can be leveraged to extract correlation-based information for classification tasks. The entire quantum process is simulated using Pasqal's Pulser library, which inevitably imposes constraints on the size of the experimental datasets. We compare our method with classical baselines to evaluate its potential. We show that, for the digit recognition task, our method achieves a higher mean accuracy than the more commonly used Jensen-Shannon distance-based methods by utilizing the Wasserstein distance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37012v1
- Title: The TEMPO network can be made independent of the system size
- Authors: Valentin Link
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37012v1  pdf=https://arxiv.org/pdf/2610.37012v1.pdf

Abstract:
The time-evolving matrix product operator (TEMPO) method efficiently simulates non-Markovian open quantum system dynamics by contracting a two-dimensional tensor network representing the time-discretized Feynman-Vernon influence functional. The standard form of this network has an unfavorable scaling with the size of the system. We show that, within the usual second-order time-step error, the dimensions of all internal network bonds can be reduced to $(2m+1)(m+1)$, where $m$ is the number of independent coupling channels. This dimension does not depend on the number of distinct eigenvalues of the coupling operators. The system size only enters in the final boundary layer of the network, making large system sizes accessible to TEMPO methods. This structure was discovered by Claude Opus 5.5 during guided algorithm development.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37040v1
- Title: Quantum Annealing for Gamma-ray Source Detection and Localization with AGILE Data
- Authors: Alessandro Rizzo, Nicolò Parmiggiani, Andrea Bulgarelli, Gabriele Panebianco, Carlo Burigana, Vincenzo Fabrizio Cardone, Farida Farsian, Massimo Meneghetti, et al.
- Categories: quant-ph (primary); quant-ph; astro-ph.HE; astro-ph.IM
- Links: abs=https://arxiv.org/abs/2610.37040v1  pdf=https://arxiv.org/pdf/2610.37040v1.pdf

Abstract:
The detection and localization of gamma-ray sources via maximum-likelihood analysis is a complex parameter optimization problem. We address this challenge using quantum annealing, a computational approach that solves optimization tasks by encoding them into the ground state of an Ising Hamiltonian. Specifically, we apply this method to observations from AGILE's Gamma-Ray Imaging Detector (GRID) in the 30 MeV-50 GeV band. We reformulated the standard analysis as a Quadratic Unconstrained Binary Optimization (QUBO) problem. We tested this method on a set of AGILE observations generated with AGILEpy, solving the QUBO with simulated quantum annealing. The method reproduces the classical flux and position estimates within their statistical uncertainty and identifies the correct grid node among the candidate positions in 97% of the maps. These promising results demonstrate that quantum annealing could be used in this optimization problem, laying the ground for its deployment on actual quantum annealers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37087v1
- Title: Exact decoherence dynamics of a detector coupled to vacuum fluctuations in bounded geometries
- Authors: Zi'an Zhao, Wenting Zhou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37087v1  pdf=https://arxiv.org/pdf/2610.37087v1.pdf

Abstract:
The properties of quantum vacuum are highly sensitive to the underlying spacetime geometry and boundary conditions. We investigate in this paper the decoherence dynamics of a two-level system (detector) coupled to a vacuum scalar field through the $\hatσ_z$-coupling scheme under various boundary environments. By rigorously evaluating the reduced density matrix of the detector, we derive an exact general expression for the detector's decoherence function, $γ(Δt)$, and use it to characterize the dynamical decoherence of a detector in three scenarios: free space, a perfectly reflecting boundary, and a cavity formed by two parallel reflecting boundaries. We find that in free space the detector's coherence decays monotonically with time, indicating that vacuum fluctuations alone inevitably lead to a complete loss of coherence. In the single-boundary case, by contrast, the detector's coherence displays non-monotonic time evolution: $γ(Δt)$ increases with time up to a maximum and then settles to a steady value, indicating that the initial coherence can be partially preserved due to the presence of the boundary. When the detector is placed inside a cavity, its coherence evolution exhibits oscillatory behavior, and a significant fraction of the initial coherence survives. Moreover, for the same detector-boundary distance, more coherence is preserved in the cavity case than in the single-boundary case. These results provide a viable route for engineering quantum coherence via boundary conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37092v1
- Title: Quantum Fisher Information Deficit as a Geometric Signature of Strong-to-Weak Spontaneous Symmetry Breaking
- Authors: Zhang-Chi Yin, Wei Zheng
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.stat-mech; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2610.37092v1  pdf=https://arxiv.org/pdf/2610.37092v1.pdf

Abstract:
Recently, strong-to-weak spontaneous symmetry breaking (SW-SSB) has been established as a framework for describing quantum phases in open systems. However SW-SSB cannot be characterized by conventional charged two-point correlators. In this work, we show that, for strongly $\mathbb{Z}_2$-symmetric states with local charged involutions, SW-SSB manifests as a persistent deficit from the maximal quantum Fisher information (QFI) under symmetry-neutral pair rotations. A model-independent inequality hierarchy establishes the equivalence of this deficit with fidelity and Rényi-1 correlators as asymptotic long-range-order diagnostics. It thereby connects finite-angle state overlaps to a constraint on the infinitesimal Bures geometry along the same pair-generated orbit. For symmetry-projected Gibbs states, we further derive a lower bound on the deficit governed by the mean energy injected by the pair operation. Crucially, locality keeps this energy cost uniformly bounded in system size and endpoint separation, maintaining a finite gap below the maximal QFI at any fixed finite temperature. When ordinary charged long range order is absent, this persistent geometric constraint provides a quantitative information-geometric characterization of thermal SW-SSB.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37094v1
- Title: Certification Time for Weak-Force-Mediated Entanglement between Levitated Particles
- Authors: Yao-Tong Chen, Salambo Dago, Oriol Romero-Isart, Andreu Riera-Campeny
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37094v1  pdf=https://arxiv.org/pdf/2610.37094v1.pdf

Abstract:
Certifying motional entanglement generated by weak forces between levitated nanoparticles requires distinguishing entangled from separable states using finite, noisy measurement records. We show that the number of measurements required to certify Gaussian entanglement can vary among equally entangled states, and quantify this variation. We derive an attainable lower bound showing that, near the separability threshold, the required number of measurements diverges inversely with the square of the distance from this threshold. We translate the required number of measurements into an experimental certification time, comparing two protocols under comparable experimental conditions: release--recapture, in which particles evolve freely before measurement, and continuous monitoring, in which the steady state is measured continuously. We find that release--recapture enables entanglement certification at interaction strengths several orders of magnitude weaker. Moreover, minimizing certification time can favor states with less entanglement, revealing a trade-off between entanglement generation and its certification. These results highlight the role of certification in the design and optimization of ongoing efforts to probe weak-force-mediated entanglement between levitated nanoparticles.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37116v1
- Title: Generative quantum extreme learning machines
- Authors: Marcin Płodzień
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37116v1  pdf=https://arxiv.org/pdf/2610.37116v1.pdf

Abstract:
Training the circuit of a quantum generative model is hampered by barren plateaus, where gradients vanish exponentially with the number of qubits. In the present work we propose a generative protocol based on the paradigm of quantum extreme learning machines, in which the circuit is never trained. A random latent vector is encoded into a quantum state, evolved with a fixed unitary and measured, and only a linear output layer is trained. The encoding of the latent variable determines the functions available to the model, while the unitary decides which combinations of them are seen by the trained layer. With the help of Pauli propagation we show that for a Clifford unitary each feature is a single product of sines and cosines of the encoded angles, so that a Clifford circuit, even a strongly entangling one, does not create new functions. Doping the circuit with $T$ gates mixes these products and changes the nonstabilizerness of the state, but the space of functions remains the one fixed by the encoding. For brickworks of Haar-random two-qubit gates the features are no longer single products, and their variation with the latent variable decreases with the depth of the circuit. For the proposed encoding and for one- and two-dimensional distributions, generated both from expectation values and from single measurements, neither the entanglement produced by a Clifford reservoir nor the additional nonstabilizerness of Haar-random brickworks systematically improves the generator, and a reservoir with no gates at all is competitive with entangling circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37204v1
- Title: QNETSIM for memory assisted design of satellite and hybrid quantum networks
- Authors: Seid Koudia, Francesco Vista, Heyang Peng, Ilora Maity, Intidhar Bedhief, Juan Carlos Hernandez Hernandez, Symeon Chatzinotas
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37204v1  pdf=https://arxiv.org/pdf/2610.37204v1.pdf

Abstract:
Space-based quantum information networks require simulation tools that capture orbital dynamics, probabilistic quantum operations, and classical coordination. We introduce QNETSIM, a modular discrete-event simulator for the design and performance evaluation of satellite and hybrid space-ground quantum networks. The framework integrates orbital geometry, free-space optical and fiber channels, quantum memories, entanglement generation, and Bell-state measurements within a common event-driven architecture. Physical models account for optical loss, atmospheric turbulence, detector imperfections, finite memory capacity, and storage-induced decoherence. Space-time routing and segmented nesting support entanglement distribution across changing topologies, while a software-defined control plane coordinates generation, storage, and swapping. Configurable scenarios encompass onboard repeaters, satellite constellations, ground-based repeaters, and direct satellite distribution. Through explicit interfaces between physical models, network protocols, and orchestration, QNETSIM links component characteristics and operational policies to entanglement fidelity, throughput, latency, availability, and memory utilization, enabling systematic exploration of architectural and resource-management trade-offs in future space-based quantum information networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37247v1
- Title: Quantum circuits of elastic wave equations via Schrödingerisation
- Authors: Shi Jin, Chundan Zhang
- Categories: quant-ph (primary); quant-ph; math.NA
- Links: abs=https://arxiv.org/abs/2610.37247v1  pdf=https://arxiv.org/pdf/2610.37247v1.pdf

Abstract:
We construct explicit quantum circuits for the velocity-stress formulation of elastic wave equations in homogeneous media using Schrödingerisation. After rewriting the equations in symmetric matrix form(SMF), we use Fourier spectral discretization for source-driven periodic problems and staggered-grid finite differences for Dirichlet, Neumann, and impedance boundary conditions. The Schrödingerisation method transforms any linear PDEs into a system of Schrödinger-type PDEs -with unitary evolution- using the warped phase transformation that maps the equations in one higher dimension. For periodic problems, we develop circuits by combining controlled Fourier-mode rotations. For physical boundaries, interleaved encoding swaps the spatial and field-component registers, enabling a more efficient circuit construction using shift operators. We analyze $p$th-order Trotter-Suzuki formulas and derive splitting-error and CNOT-gate estimates, under the assumptions of smooth auxiliary initialization and solution-state recovery. Comparison with classical partitioned splitting methods identifies a polynomial improvement in spatial-resolution dependence for the quantum state-evolution subroutine. Noiseless circuit simulations of a forced periodic problem and an impedance problem illustrate the constructions and quantify their errors against exact solutions and classical reference computations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37249v1
- Title: HTM: A Hybrid Classical-Quantum Computation Model
- Authors: Guoqiang Shu, Zongjiang Yi, Jinyang Yao, Haomiao Dong, Zhihang Li, Fudong Liu, Zheng Shan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37249v1  pdf=https://arxiv.org/pdf/2610.37249v1.pdf

Abstract:
Classical and quantum computers have achieved collaborative computation and completed applications across numerous fields. Nevertheless, the absence of a unified hybrid computation model has led to issues such as non-standardized engineering architecture design, ambiguous task partitioning criteria and so on. To address these issues, this research proposes a hybrid classical-quantum computation model (HTM). By constructing unified state sets and transition function representations, HTM clarifies hybrid control logic and implements a control-sharing mechanism. Simultaneously, a comprehensive complexity calculation method based on entanglement and superposition was proposed, supporting computation task partitioning and resource scheduling. The HTM fills a theoretical gap in the classical-quantum hybrid computation area and implements the joint promotion and development of computing models and hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37268v1
- Title: Deployed entanglement-based BBM92 quantum key distribution using frequency-converted photons emitted by a quantum dot
- Authors: Michal Vyvlecka, Raphael Joos, Benjamin Breiholz, Emma Marmasse, Ilenia Neureuther, Timo Schnieber, Anna Frederike Köhler, Tim Strobel, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37268v1  pdf=https://arxiv.org/pdf/2610.37268v1.pdf

Abstract:
Establishing secure communication is an important requirement in existing and future networks. Although current solutions rely on classical approaches, quantum mechanics offers the possibility of moving from computational to information-theoretic security. Quantum key distribution (QKD) has been extensively studied as a means of achieving such security. Recently, epitaxial quantum dots started to be studied and employed in quantum cryptography, because of their rapid development that made them one of the brightest sources of quantum light to date. In particular, they are known to be excellent sources of polarization-entangled photon pairs, especially droplet-etched dots operating at $\sim$780 nm. Here, we employ such a quantum dot to generate entangled photon pairs under 1 GHz excitation rate. Using quantum frequency conversion, we interface the emitted photons with the telecommunication wavelength range while preserving their polarization entanglement. This enables quantum key distribution over a 1.59 km field-deployed fibre link across the University of Stuttgart - campus Vaihingen, using the BBM92 protocol: we achieve a secure key rate of 206 Hz over 19 h of stable operation, resulting in a total secure key length of 14.2 Mbit. This key enables the safe encryption and decryption of a colour image with further implementation of error correction and privacy amplification. These results demonstrate important steps towards hybrid quantum networks by combining high-quality entangled-photon sources operated at high excitation rates, efficient frequency conversion module, and picosecond-level time synchronization in a realistic deployed network.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37293v1
- Title: Experimental evidence for quantum Brownian motion in electron-metal decoherence
- Authors: Wayne Cheng-Wei Huang, Zilin Chen, Herman Batelaan
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2610.37293v1  pdf=https://arxiv.org/pdf/2610.37293v1.pdf

Abstract:
Feynman once remarked that the double-slit experiment has in its heart the only mystery of quantum mechanics. Arguably, the scientific significance of double-slit experiments lies in motional decoherence and the mechanism behind it. Decoherence of motional states underpins our understanding of quantum-to-classical transition. It is also central to the operation of miniaturized quantum electron devices and poses a resolution limit for electron microscopes. In this work, we provide experimental evidence for the critical role of quantum Brownian motion in electron motional decoherence. We demonstrate, for the first time, clear signatures of electron-metal decoherence and its continuous tunability. Our experiment concludes a two-decade long search for experimental realization of the Anglin-Paz-Zurek proposal, establishing electron-microchannel systems as viable open quantum platforms for free-electron quantum optics. The quantitative agreement between experiment and theory further paves the way for testing the Caldeira-Leggett quantum dissipation theory with free electrons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37296v1
- Title: Prepare-and-measure quantum key distribution from a bound on information leakage
- Authors: Abhishek Mishra, Michele Masini, Maria Balanzó-Juandó, Armin Tavakoli, Stefano Pironio
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37296v1  pdf=https://arxiv.org/pdf/2610.37296v1.pdf

Abstract:
Every quantum key distribution (QKD) protocol must limit the information available outside the users' laboratories. In device-independent QKD this is essentially the only assumption made on the devices. In a prepare-and-measure setting it cannot be imposed strictly, since the sender's device must emit a signal that depends on her private input. The natural replacement, and a minimal one, is a leakage bound: a bound on how much information about the input leaves the sender's laboratory, through the intended signal or through any side channel. We ask how far this unavoidable requirement can replace a detailed model of the source. We show that this single bound, quantified by the probability of guessing the input from everything the source emits, suffices to prove security against collective attacks. In our analysis, nothing is assumed about the precise form of the emitted states, their dimension, energy or purity, nor about the receiver's measurement device, beyond the standard requirement that it does not leak Bob's data. The standard B92 and BB84 protocols do not certify any key under this minimal leakage bound assumption. But closely related protocols can and, in the ideal limit, achieve one secret bit per key round. For noisy implementations, we compute key rates using semidefinite programming relaxations. Our best protocols tolerate visibilities down to 0.84, corresponding to an 8% quantum bit error rate, compared with the 11% threshold of standard device-dependent BB84.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37337v1
- Title: Security Analysis of Ekert-type QKD Protocol Coming Under Cloning Attacks
- Authors: Kaushiki Mukherjee, Sumana Karmakar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37337v1  pdf=https://arxiv.org/pdf/2610.37337v1.pdf

Abstract:
We analyze the security of an Ekert type bipartite key distribution protocol coming under cloning attacks by an untrusted observer. Precisely, an eavesdropper is assumed to intercept and apply an asymmetric, phase-variant cloner on one or both qubits which are transmitted over public channel from an authenticated source to the trusted parties. We partially characterize two-qubit states from the perspective of designing a QKD protocol that can generate a distillable secret key among the trusted users even under such cloning attacks. We rely upon Devetak Winter framework for computing key rate so as to identify states, which when used in the protocol, secret-key can be distilled. Utility of an entangled state, for designing a successful QKD protocol, changes from single-qubit to double-qubits cloning attacks. Interestingly, we can distinguish some useful families of two-qubit entangled states when only one of the transmitted qubits is cloned by a malicious third party.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37347v1
- Title: Measurement incompatibility and noiseless quantum codes
- Authors: Yu-Xuan Zhang, Jing-Ling Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37347v1  pdf=https://arxiv.org/pdf/2610.37347v1.pdf

Abstract:
We construct a rank-one minimal informationally complete measurement (MIC) with an invertible dual operator and prove that, for arbitrary finite input and output dimensions, a channel universally preserves measurement incompatibility if and only if its input space contains a noiseless code subspace of the full output dimension. Preserving the compatibility threshold of a finite family of binary measurements already guarantees such a code. Furthermore, for every $d\ge2$, there exists a family of binary measurements that is incompatible on the full space but compatible after compression to any proper subspace. These results resolve the conjecture of Chitambar and Zhang and the existence question posed by Uola and coauthors. We also give an explicit construction of exact encodings and show that, for a sufficiently small shift in the compatibility threshold, the transmission error of an approximate encoding is bounded by a constant times the square of the shift. These results establish a connection between measurement compatibility, quantum steering, and quantum error correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37438v1
- Title: Homodyne Unravelling and Parameter Estimation in Squeezed Thermal Baths
- Authors: Eoin O'Connor, Francesco Albarelli, Marco G. Genoni
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37438v1  pdf=https://arxiv.org/pdf/2610.37438v1.pdf

Abstract:
We derive an alternative formulation of the stochastic master equation describing the evolution of quantum systems continuously measured via homodyne detection in a squeezed-thermal environment. This formulation allows us to identify two distinct collapse operators, corresponding respectively to the monitored and unmonitored channels, and to express the quantum state evolution directly in terms of Kraus-like operators. As a consequence, it facilitates the application of advanced numerical methods that account for higher-order corrections and discrete-time monitoring, and it also enables the efficient numerical evaluation of Cramér-Rao bounds in parameter estimation problems. To demonstrate the latter, we evaluate the Fisher information of the continuous homodyne monitoring for qubit frequency estimation in the presence of a squeezed-thermal bath. Our results show that exponential scaling of the steady-state Fisher information rate with squeezing is retained even at non-zero temperature.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37491v1
- Title: Adaptive Information Mining: Approaching the Quantum Limit of Super-Resolution Imaging
- Authors: Seungman Choi, Peter Menart, Andrew Schramka, Zubin Jacob
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2610.37491v1  pdf=https://arxiv.org/pdf/2610.37491v1.pdf

Abstract:
The "Rayleigh limit" is not an intrinsic property of light, but a consequence of sub-optimal measurement of collected photons by the imaging instrument. To overcome this limitation, we present Adaptive Information Mining, a framework that achieves super-resolution by using sequentially refined measurements for incoming photons. Our approach employs a reconfigurable imaging system that dynamically reshapes the instrument measurement responses to maximize the Fisher information and guide scene estimation toward the fundamental quantum limit, even in deep sub-Rayleigh regimes. We demonstrate that this approach achieves an estimation error 2-5 times closer to the fundamental quantum limit than traditional direct imaging when imaging point sources, without requiring any prior knowledge of their positions and brightnesses. Importantly, we demonstrate that AIM can be extended to fully blind multi-parameter estimation in scenarios involving an unknown number of sources or turbulence-induced wavefront distortions. Our approach addresses the limitations of conventional fixed imaging, offering a practical path toward quantum-limited super-resolution imaging.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37493v1
- Title: Recovering classical gauge geometry from quantum master constraints
- Authors: Alejandro Corichi
- Categories: quant-ph (primary); quant-ph; gr-qc; math-ph
- Links: abs=https://arxiv.org/abs/2610.37493v1  pdf=https://arxiv.org/pdf/2610.37493v1.pdf

Abstract:
Exact normalizable solutions of quantum constraints form a symplectic submanifold of the space of rays, whereas classical first-class constraints define a surface on which the symplectic form is degenerate. We ask how the degenerate directions can be recovered when quantum theory is regarded as fundamental and the constraints are imposed through a single positive master operator. For a nonnegative master function whose zero set is a Morse--Bott critical manifold, the image of the linearized Hamiltonian vector field is the symplectic orthogonal of the zero set, and coisotropy is equivalent to this linearization having square zero. The image is fixed by the zero set, but the theorem identifies it with the response of the master dynamics, which makes it accessible to quantum states. Three realizations follow. The exact quantum physical space is the opposite, rotational case of the same dichotomy. For quadratic masters, the bottom of the spectrum is $(\hbar/2)\Tr_+L$, so first-class zero sets carry no offset of order $\hbar$; within the harmonic approximation this explains the $\hbar$ versus $\hbar^2$ offsets observed in tests of the master-constraint programme. Finally, the second time derivative of the limiting covariance of a semiclassical packet, which can be determined by bounded probes, has the gauge distribution as its image. Two oscillators at fixed total energy give exact master evolution, an exact realization of this covariance shear, and the reduced symplectic limit. For the non-Abelian SL(2,$\R$) model we compute the coherent and Weyl master symbols, prove essential self-adjointness and a finite-time propagation estimate, and derive the spectral bottom $\hbar^2/2$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37552v1
- Title: Meet-in-the-Middle Compilation of the $[\mathrm{CNOT}]$ Class with Fibonacci Anyons
- Authors: Matvei Fedin, Andrey Morozov
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2610.37552v1  pdf=https://arxiv.org/pdf/2610.37552v1.pdf

Abstract:
Compilation of two-qubit Fibonacci anyon gates is complicated by leakage ($\ell$) from the four-dimensional computational sector to the fifth state of the fusion space. We construct a GPU pipeline to find low-leakage representatives of the $[\text{CNOT}]$ class on different subsets of the braid group.   We exhaustively explore the full positive five-generator alphabet up to $L=21$ with minimal leakage $\ell\sim10^{-3}$ and error $d_{[\text{CNOT}]}\sim 10^{-8}$ on it. To reach larger lengths, the search space is successively narrowed to three-generator, boundary-$σ_3$, and palindromic braids, and by considering only the Garside left normal form. These optimizations allow us to reach $L=72$. For $L=69$, a braid with $\ell\sim10^{-10}$ and $d_{[\text{CNOT}]}\sim 10^{-10}$ is found.   In addition to directly enumerating optimal braids, we proved that $\ell\in\mathbb Z[\varphi]$, and any nonzero leakage obeys an exponential lower bound in the braid length, and obtained the limit laws $F_{3,\infty}(\ell)=\ell^2$ and $F_{5,\infty}(\ell)=\ell^4$ for our sets. Using asymptotics for the distribution function $F$, we showed that for sufficiently long braids, the asymptotics of exhaustive search are better than the asymptotics of random sampling for finding low-leakage braids.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37589v1
- Title: Dynamical quantum simulations as laboratories for quantum information
- Authors: Su Yeon Chang, Hailey S. Murray, Brian Barch, Greeshma Oruganti, Luis Pedro García-Pintos, Martin Larocca, Mark M. Wilde, M. Cerezo
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2610.37589v1  pdf=https://arxiv.org/pdf/2610.37589v1.pdf

Abstract:
Dynamical quantum simulations are commonly designed to access a particular response function or correlation function. Yet the underlying protocol prepares a family of many-body states that contains information well beyond the observable for which the simulation was originally designed. In this work, we explore the idea of using these states as laboratories for quantum information. As a case study, we consider the local-pulse protocols used to compute Green functions in finite XX and XXX spin chains, and we interpret opposite source rotations as encoding a classical bit into the many-body system. This allows us to follow how the resulting record propagates, how it is encoded across local subsystems, and how readily it can be accessed with different measurements. We also find a clear separation between representation and readout. While fermionic covariance data exactly reconstruct the signed response in the XX chain, simple spin measurements recover a larger fraction of the locally available information in the XXX chain. This reversed ordering persists when we move from finite-pulse discrimination to local source-angle estimation. Going beyond the source record, the same reduced states also allow us to reinterpret results in terms of Bell state recovery and quantum communication rates, as well as providing direct access to the evolving bipartite and genuine multipartite entanglement of the system. Our results show that dynamical quantum simulations developed for response calculations can naturally be used to ask a much broader set of quantum-information questions about the many-body states they already prepare.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37635v1
- Title: Classical Verification of Quantum Computation Beyond the Polynomial Hierarchy
- Authors: Atul Mantri
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.CR
- Links: abs=https://arxiv.org/abs/2610.37635v1  pdf=https://arxiv.org/pdf/2610.37635v1.pdf

Abstract:
It is not known whether a classical polynomial-time verifier can verify arbitrary polynomial-time quantum computations with an efficient quantum honest prover without computational assumptions. We show that, relative to a classical oracle, such verification is possible for a language beyond the polynomial hierarchy that is decided exactly in quantum polynomial time. The protocol is public-coin, with perfect completeness and soundness error at most 1/4. To our knowledge, no language with such a proof system was previously proved to lie outside AM relative to an oracle.   For every unbounded polynomial-time computable function, the oracle can be chosen so that the message count and the oracle query counts of the quantum algorithm, verifier, and honest prover are bounded by this function of the input length. The message count is optimal up to a constant factor, since for a suitable oracle every interactive proof system for the language uses at least a constant fraction of the messages of our protocol on infinitely many lengths, with a constant depending on its verifier.   The language is a variant of recursive Fourier sampling in which code tables encode secrets that address data tables. The tables are evaluated recursively, and the oracle stores only the leaves. The quantum algorithm recovers every secret exactly, and the verifier checks the prover's secrets recursively against random code entries. The recursion restricts the input in a correlated way, as the same secret fixes the code bits and chooses the free coordinate, so Håstad's switching lemma does not apply. We prove a switching theorem for these restrictions, which may be of independent interest. For instances of sufficient height, no constant-depth circuit of size $2^{\mathrm{poly}(n)}$ changes its output with probability above $2^{-Ω(n)}$ when the answer of a random instance is flipped by changing a single leaf.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37660v1
- Title: Optimal quantum discrimination at Liouvillian exceptional points
- Authors: Aritra Ghosh, M. Bhattacharya
- Categories: quant-ph (primary); quant-ph; math-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2610.37660v1  pdf=https://arxiv.org/pdf/2610.37660v1.pdf

Abstract:
Central to non-Hermitian sensing is the question of whether exceptional points (EPs) can make weak perturbations easier to detect. We show that despite enhanced spectral response, in finite-dimensional Lindblad systems with a unique stationary state and a nonzero relaxation gap, EPs offer no fundamental advantage in how the observation time required for reliable detection of a weak perturbation scales with the perturbation strength. We nevertheless demonstrate that by selectively choosing perturbations that enhance the quantum Fisher information rate, EPs can shorten the observation time needed to reach a predefined detection accuracy relative to a comparable non-EP reference at the same decay rate. As an illustration, we show using an optomechanical model at an EP that we can detect a weak force through the cavity output at the same reliability in less time than a non-EP reference. Our results establish fundamental limits on perturbation detection at EPs and can guide the design of faster non-Hermitian sensors based on optomechanical resonators, superconducting qubits, and trapped ions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37665v1
- Title: Exact Analytical Treatment of Collectively Pumped Dicke Superradiance
- Authors: Avishi Poddar, Nico Baßler, Julian Lyne, Susanne F. Yelin, Helmut Ritsch, Claudiu Genes, Raphael Holzinger
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.37665v1  pdf=https://arxiv.org/pdf/2610.37665v1.pdf

Abstract:
We study the dynamics of an ensemble of $N$ two-level emitters undergoing collective decay at rate $Γ$ and collective incoherent pumping at rate $R$, confined to the fully symmetric Dicke ladder. Although the population dynamics are confined to a finite set of rate equations, their quantum-trajectory representation involves infinitely many pump-decay histories. We derive an exact finite continued fraction for the Laplace-transformed Dicke-state populations by resumming the infinitely many quantum trajectories generated by competing pump and decay processes. Our construction provides a physically transparent interpretation of the tridiagonal resolvent and extends to arbitrary permutationally symmetric initial states. In the strong- and weak-pumping regimes, we obtain perturbative transient solutions. We also identify exact relaxation eigenvalues and emission observables at balanced pump and decay strengths. Our solution provides a starting point for extending trajectory-based analytical methods to more general driven-dissipative collective systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.35931v1
- Title: An exactly solvable obstructed seam on a lattice Klein bottle: bulk-locked Majorana rings and register-dependent toric codes
- Authors: Junhao, Wang
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2610.35931v1  pdf=https://arxiv.org/pdf/2610.35931v1.pdf

Abstract:
We study a frustrated seam produced by literal reflection gluing of Wen's plaquette model on a closed lattice Klein bottle. The seam operators anticommute along two cycles for even circumference and one cycle of twice the length for odd circumference. Their algebra reduces to free Majorana rings, while the commuting bulk stabilizers constrain the allowed ring sectors. This bulk locking yields exact ground energies, excitation gaps and degeneracies, checked by phase-aware Pauli traces and finite-size diagonalization, including two 24-qubit energy predictions. The seam degeneracy is not topological: the single-site seam fields tested split it at second order. We contrast this obstructed gluing with consistent toric-code realizations. An edge register preserves the anyon labels; a Hadamard-dressed site register has colour-dependent seam transport, with ground-state degeneracy 2 or 4 for even circumference and a sign-frustrated exception at odd circumference. For the enumerated lattice isometries and sizes, we compute logical gates and distances, distinguishing abstract qubit relabelling from local hardware depth. Finally, on three 16- and 24-qubit lattices, chiral matter selects a holonomy doublet whose electric-field splitting follows two competing tunnelling routes. These matter results remain finite-size statements. The main result is the exact obstructed-seam solution with bulk sector locking; the register, gate and matter calculations delimit its relation to topological codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.35993v1
- Title: Amorphization-Depth-Dependent Bismuth Redistribution and Activation in Silicon for Quantum Devices
- Authors: Youcef A. Bioud, Simon-Jean Michel, Sebastien Francoeur, Sjoerd Roorda, Eva Dupont-Ferrier
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.35993v1  pdf=https://arxiv.org/pdf/2610.35993v1.pdf

Abstract:
Near-surface bismuth donors are promising for silicon quantum devices because of their rich electron-nuclear spin structure and long spin coherence, but their electrical activation is strongly influenced by implantation-induced amorphization. We compare redistribution and electrical activation of 20 keV Bi implanted directly into Si and after Si preamorphization. The two routes produce amorphous-layer depths of approximately 47 nm and 177 +/- 15 nm, respectively. After annealing at 650 C for 300 s, Rutherford backscattering spectrometry and channeling reveal comparable substitutional Bi fractions of 91 +/- 2% and 89 +/- 4%, whereas Hall measurements indicate Hall-derived electrical activation yields of approximately 60% and 90%, respectively. Depth-resolved ion-scattering analysis reveals a buried Bi-related feature at or beyond the initial amorphous/crystalline interface, within the end-of-range region, together with increasing surface segregation at higher annealing temperatures. The buried feature is consistent with trapping near residual end-of-range defects. X-ray photoelectron spectroscopy and low-temperature photoluminescence on the Bi-only sample reveal no resolvable Bi-oxide contribution and a donor-related optical signature, respectively. These results show that amorphization depth and regrowth geometry govern Bi redistribution and influence electrical activation beyond substitutional incorporation alone.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36026v1
- Title: A Correspondence Between Qubit- and Boson-Based Sensing Protocols
- Authors: Zachary Bogorad, Roni Harnik
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36026v1  pdf=https://arxiv.org/pdf/2610.36026v1.pdf

Abstract:
Recent years have seen a surge of interest in adapting non-classical states to search for physics beyond the Standard Model, including both qubit- and boson-based systems. These two classes of systems are closely related through the Holstein--Primakoff transformation (HPT). In this work, we show that the HPT offers novel insights into inherently quantum-mechanical detection of new physics. We begin by discussing how the HPT can be used to unify certain existing qubit- and boson-based proposals in a single framework. We then show how it naturally reveals a novel generalization of GHZ states which offer superior performance for the detection of rare interactions. We demonstrate that these novel states can be readily prepared, and combine the coherent advantage of GHZ states with superior error rejection. Finally, we show that the HPT also reveals a natural extension of the Hamiltonian-Not-in-Lindblad-Span theorem for collections of bosonic modes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36029v1
- Title: AlgebrasTQD: Computing Algebras and Interfaces in Twisted Quantum Doubles
- Authors: Alison Warman
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; math.QA; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36029v1  pdf=https://arxiv.org/pdf/2610.36029v1.pdf

Abstract:
We present AlgebrasTQD, an open-source code written in GAP (Groups, Algorithms, and Programming), for computing condensable algebras and the corresponding topological boundaries and interfaces of twisted quantum doubles $D^ω(G)$. These algebras can be used to classify 1+1d gapped and gapless phases whose symmetry is related by gauging to a finite group $G$ with anomaly $ω\in H^3(G,U(1))$, to study 2+1d anyon proliferation and to construct logical gates in non-Abelian topological quantum codes. The functions in AlgebrasTQD compute all condensable algebras $A(H,F,γ,ε)$ with their algebra structure and anyons, sort them into isomorphism classes and identify the twin algebras that are inequivalent but share the same anyon decomposition. AlgebrasTQD also determines all the subalgebra relations, the corresponding Hasse diagram and the types of 1+1d phases for any chosen, possibly non-invertible, group-theoretical symmetry. For non-maximal algebras, the code computes the reduced topological order with its $3$-cocycle and the map of anyons across the topological interface. Finally, AlgebrasTQD includes functions that construct certain non-Clifford logical gates via non-Abelian surface codes. We summarize the formulas that are implemented in the AlgebrasTQD code, and we illustrate its use with Abelian and non-Abelian groups including $\mathbb{Z}_2^3$ with $ω_\text{III}$, $D_8$, $A_4$ with and without anomaly, twin algebras and twin phases, and the Clifford-hierarchy gates in quantum doubles of dihedral groups. All arithmetic is exact and AlgebrasTQD can be used with any finite group $G$ and 3-cocycle $ω$, limited only by the time and size of the calculation. The code is available at https://github.com/AlisonWarman/AlgebrasTQD

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36031v1
- Title: Analytic Bootstrap Solution for Quantum Mechanics on a Circle
- Authors: David Berenstein, Upamanyu Moitra
- Categories: hep-th (primary); hep-th; hep-lat; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36031v1  pdf=https://arxiv.org/pdf/2610.36031v1.pdf

Abstract:
We solve the Schrödinger equation for a particle in the circle with a quantum mechanical bootstrap method. The main idea is that in physical situations one needs solutions of the recursion relations for the Fourier coefficients of the measure that vanish exponentially fast. We show that this results in a (generalized) continued fraction representation of the solution. The solution is an analytical function of the couplings and the energy. We also show how one this method directly computes the density of states and checking that the answer is physical is reduced to checking an inequality for a single variable. We also show how to reconstruct the wave function and how to extract the quasimomentum of the particle as a function of the energy. We illustrate our solution in the simplest case of the Mathieu equation, where we show that the method can easily resolve exponentially small bands in the band spectrum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36044v1
- Title: An open EFT for dark matter searches with matter-wave interferometers
- Authors: Leonardo Badurina, Kathryn M. Zurek
- Categories: hep-ph (primary); hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36044v1  pdf=https://arxiv.org/pdf/2610.36044v1.pdf

Abstract:
Matter-wave interferometers (MWIs) are a genuine quantum probe of dark matter (DM), being sensitive to DM-induced phase shifts and loss of contrast. Treating the interferometer as an open quantum system and the dark sector as its environment, we derive an open EFT to study these signatures using the Schwinger-Keldysh formalism. Starting from a microscopic theory, we derive the interferometer's effective action, which we then project onto the many-body worldline sectors relevant for atom interferometers and MWIs employing mesoscopic objects, i.e., composite-particle interferometers (CPIs). This construction clarifies the heavy-probe limit and organizes phase shifts and decoherence as distinct real-time components of the influence action: the retarded kernel controls the causal response of the environment, while the Keldysh kernel controls environmental fluctuations and hence loss of contrast. At leading order, these kernels reduce to: (i) DM bubble diagrams in the case of four-point interactions, and (ii) dressed in-medium mediator propagators in the case of long-range interactions, where the dressing is provided by the DM environment. Within this framework, we study the signatures of elastic spin-independent sub-GeV DM scattering off nucleons and find that: (i) owing to Bose enhancements below the DM wave-particle boundary, ambitious CPIs could probe Higgs-portal DM with mass below 1 eV in an unexplored region of model space; (ii) for DM coupled to nucleons via a light hadrophilic scalar, the DM background can drive the mediator's in-medium mass tachyonic over much of parameter space; outside these regions, CPIs could probe provide powerful probes of light DM.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36048v1
- Title: Typicality of entanglement growth and transport fluctuations in quantum symmetric exclusion processes
- Authors: Ewan McCulloch
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.dis-nn; cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36048v1  pdf=https://arxiv.org/pdf/2610.36048v1.pdf

Abstract:
We use macroscopic fluctuation theory (MFT) to establish the typicality of charge-transfer statistics and entanglement dynamics in the quantum symmetric exclusion process, a model of stochastically hopping free fermions with diffusive transport and long-range quantum coherence. We show that the leading long-time charge-transfer full counting statistics of individual noise realizations coincide almost surely with those of the classical symmetric exclusion process (SSEP), in equilibrium and following quenches from arbitrary occupation-diagonal product states. Our results apply to transient fluctuations in the thermodynamic limit, extending previous work that has primarily focused on stationary regimes. Our approach compares the noise averages of the charge-transfer generating function and its inverse. The former reduces to SSEP, while the latter maps to an auxiliary Brownian energy process whose MFT saddle-point problem is related to that of SSEP, yielding matching large-deviation exponents. Through free-fermion identities relating entanglement to subsystem-number fluctuations, this establishes the self-averaging of the covariance-matrix eigenvalue distribution and of Rényi and von Neumann entropies. We obtain asymptotically exact predictions for entanglement growth from domain-wall and Néel initial states, in excellent agreement with numerical simulations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36054v1
- Title: Mesons, Confinement, and Complexity: A Krylov Space Perspective on the Long-Range Ising Chain
- Authors: Xuhao Jiang, Jad C. Halimeh, N. S. Srivatsa
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-lat; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36054v1  pdf=https://arxiv.org/pdf/2610.36054v1.pdf

Abstract:
We investigate the interplay between confinement and Krylov complexity in the long-range transverse-field Ising chain, where power-law interactions $\sim 1/r^α$ generate an effective confining potential between domain walls without an explicit symmetry-breaking field. Using the time-averaged Krylov state complexity after a quench as a diagnostic, we find that the complexity is strongly suppressed and only weakly system size-dependent at small $α$ and small transverse field $h_x$, where confinement is strongest, and crosses over to rapid growth at larger $α$, where it increases with system size. Within the confined regime, the oscillation frequencies of the complexity agree with the meson masses of an effective two-kink model, with the dominant frequency growing linearly with the lightest meson mass and the time-averaged complexity decreasing approximately as its inverse square. We further study operator Krylov complexity at finite temperature using the Wightman inner product. At low temperature, it exhibits bounded oscillations that directly encode the meson spectrum, whereas this structure is progressively washed out as the temperature increases. These results identify Krylov complexity as a spectroscopic probe of interaction-induced confinement and reproduce, in a microscopic lattice model, the hallmarks of Krylov complexity identified in confining field theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36058v1
- Title: Universal Scaling of Conditional Mutual Information in Classical Stochastic Dynamics
- Authors: Songlei Wang, Chenguang Liang, Zhi-Cheng Yang
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36058v1  pdf=https://arxiv.org/pdf/2610.36058v1.pdf

Abstract:
Conditional mutual information (CMI) characterizes dependence between two regions conditioned on an intervening buffer. Its characteristic decay length, the Markov length, has recently been identified as a diverging length scale at mixed-state phase transitions. Here, we investigate CMI dynamics in one-dimensional classical stochastic models and propose a universal scaling form for systems whose Markov length diverges with time. We derive this form in the inactive phase of parity-conserving directed percolation, where domain-wall coarsening generates a growing length scale and a self-similar probability distribution. We introduce a Hankel-based truncation scheme that enables matrix-product-state simulations at long times and over large spatial regions. Using this method, we verify the proposed scaling both in the inactive phase and at the nonequilibrium critical point, where the dynamical critical exponent governs Markov-length growth. More broadly, the same scaling form captures cases in which collective inference sets the diverging Markov length. Despite these distinct mechanisms, the CMI between fixed microscopic regions exhibits a common scaling dimension of two. Finally, we extend this framework to temporal CMI, establishing an analogous relation between the strength of conditional dependence in time domain and its characteristic memory time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36061v1
- Title: Parity-doublet spin interactions in ultracold polyatomic molecules
- Authors: Junheng Tao, Paige Robichaud, Christian Hallas, Giseok Lee, John M. Doyle
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36061v1  pdf=https://arxiv.org/pdf/2610.36061v1.pdf

Abstract:
Precision measurements exploit internal molecular structure to search for physics beyond the Standard Model. Reaching the entanglement-enhanced regime requires preparing and preserving correlated molecular states within the same manifold used for sensing. Parity-doublet states are central to proposals for precision measurements with polyatomic molecules because they enable large molecular polarization for enhanced sensitivity, and provide internal state co-magnetometry to suppress systematic errors. Here we report the observation and control of resonant dipolar exchange interactions in a parity-doublet sensing manifold of ultracold polyatomic molecules. Using laser-cooled CaOH molecules in a crossed optical dipole trap, we encode a pseudospin in the $\ell$-type parity-doublet states and observe two complementary signatures of interactions: a density-dependent Ramsey contrast decay and a spin-projection-dependent mean-field precession whose sign reverses with the initialized population imbalance. Both observables are well described by a common discrete truncated Wigner model using independently calibrated experimental parameters. We further Floquet-engineer the interaction anisotropy and observe suppressed many-body dephasing near the SU(2)-symmetric Heisenberg point, identifying a protected regime relevant for spin squeezing and precision measurement with dense molecular ensembles. Our results establish parity doublets as a coherent, interacting, and programmable molecular degree of freedom, connecting the polyatomic precision-measurement platform to dipolar many-body physics and opening a route to entanglement-enhanced tests of fundamental physics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36080v1
- Title: Non-Hermitian Schwinger effect in an imaginary magnetic field
- Authors: Ahmad Jafar Arifi, Kei Suzuki
- Categories: hep-th (primary); hep-th; hep-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36080v1  pdf=https://arxiv.org/pdf/2610.36080v1.pdf

Abstract:
We investigate a non-Hermitian Schwinger effect by analyzing a one-loop effective Lagrangian of scalar and Dirac quantum electrodynamics (QED) in the presence of a real electric field and a parallel imaginary magnetic field. We show that an imaginary magnetic field produces an additional pole family in the integrand of the proper-time representation. Unlike a real magnetic field, an imaginary magnetic field can generate a nonzero imaginary part of the effective Lagrangian even in the absence of an electric field. The interplay between the two fields leads to nontrivial phenomena, such as a cancellation mechanism between the contributions of two fields. We also point out that when the ratio of two field strengths is rational, some poles among the two families coincide, and a careful treatment of double poles is required. By further examining the complex Landau-level structure of the electric-pole contribution, we find that the field dependence of the vacuum decay rate from each Landau level exhibits a sinusoidal-like behavior, and their sum determines the overall field dependence. Our results clarify the analytic structure of the QED effective Lagrangian in imaginary magnetic backgrounds and provide a basis for investigating its relation to non-Hermitian phenomena in the QED vacuum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36113v1
- Title: Scaling and Renormalization in Neural Networks: An Effective Renormalization-Group Description of Grokking
- Authors: Min Chen, Junqi Wang, Zeguan Wu, Wenhao Huang, Junyu Liu
- Categories: cs.LG (primary); cs.LG; cs.AI; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36113v1  pdf=https://arxiv.org/pdf/2610.36113v1.pdf

Abstract:
Grokking is a delayed transition from memorization to generalization in deep neural networks (NNs). We examine whether scaling and renormalization group (RG) theories can describe this dynamics, establishing a quantitative physical framework for neural generalization transitions. For modular addition on a two-layer NN, an ensemble of trained models defines an order parameter (the squared weight norm) and fluctuation proxies for the heat capacity and the susceptibility, with training epoch and weight decay serving as thermal and field control coordinates. To bridge neural architectures to real-space RG, we construct an exact coupling matrix via a second-order expansion of the loss with respect to per-neuron norms and use its Fiedler vector to define an effective geometry. This spectral ordering yields a monotonic spatial decay of coupling strength that is absent under random permutations. We then execute real-space RG by block-spin aggregating adjacent neurons and parameterizing the coupling matrix into off-diagonal band strengths. Linearizing this local RG map yields relevant scaling exponents and five derived critical exponents, with direct empirical estimates matching RG predictions within 1-10%. Overall, our framework provides a consistent effective description of grokking, suggesting the scaling and renormalization group formalism as a tool to investigate NN dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36182v1
- Title: Ultrafast light-electron modulation for free-electron quantum optics: fundamentals and applications
- Authors: Zirui Zhao, Ruoyu Chen, Changying Li, Yongcheng Ding, Zhaopin Chen, Xinbing Song, Shuaishuai Sun, Ye Tian, et al.
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36182v1  pdf=https://arxiv.org/pdf/2610.36182v1.pdf

Abstract:
Coherent optical modulation of free-electron wavepackets offers a route to ultrafast beam steering, energy exchange, temporal compression, and quantum-state shaping. Recent advances in photon-induced near-field electron microscopy (PINEM), ultrafast Kapitza-Dirac effect (KDE) and dielectric laser acceleration (DLA) have demonstrated strong light-electron coupling, but longitudinal energy modulation, transverse momentum transfer, and wavepacket-dependent diffraction are still commonly described with separate models. Here, we develop a unified Light-Electron Modulation (LEM) framework that treats optical near fields as programmable phase modulators for free-electron wavepackets. Within this framework, we identify longitudinal and transverse modulation channels, analogous to electro-optic phase modulation and acousto-optic diffraction of light, respectively, and show how their operation depends on wavepacket extent, recoil, phase matching, and optical-field geometry. This formulation organizes PINEM, Raman-Nath and Bragg diffraction, DLA-like acceleration, and anomalous PINEM as limiting regimes of a common modulation picture. The resulting framework provides design principles for free-electron modulators that can control energy spectra, temporal density, transverse wavefronts, and electron-photon quantum interfaces, establishing LEM as a device-level platform for programmable femtosecond-to-attosecond matter-wave control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36257v1
- Title: Dynamical Tensor Train Approximation for Wigner--Fokker--Planck Equation with Applications to Open Quantum Systems
- Authors: Geshuo Wang, Jingwei Hu
- Categories: math.NA (primary); math.NA; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36257v1  pdf=https://arxiv.org/pdf/2610.36257v1.pdf

Abstract:
We develop a dynamical tensor-train method for the Wigner--Fokker--Planck equation arising in continuous-variable open quantum systems. The Wigner function is evolved directly in tensor-train form using a projector-splitting integrator, while the nonlocal Wigner pseudo-differential operator is treated through low-rank representations of the potential difference and matrix-free exponential actions. The resulting method avoids full tensor-product computations in high-dimensional phase space. Numerical experiments in one, two, and three spatial dimensions demonstrate the accuracy and scalability of the method, including simulations in a six-dimensional phase space.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36268v1
- Title: Towards Quantum Computation of Bulk FeO
- Authors: Daniel Staros, Federico Petrovich, Ammar Kirmani, Daniel N. Blaschke, M. Cerezo, Jian-Xin Zhu
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36268v1  pdf=https://arxiv.org/pdf/2610.36268v1.pdf

Abstract:
Quantum computation offers a promising path towards efficient calculations of the electronic structure of correlated materials. The properties of iron-based materials, which are key for advancing geological and astrophysical understanding, are notoriously difficult to calculate with classical computers. However, despite the many recent advances in quantum computing on near intermediate scale quantum hardware, a full treatment of the electronic structure of high-$Z$ atoms or molecules remains challenging. Here, we investigate the ground-state properties of molecular FeO and Fe$_2$O$_2$ model Hamiltonians using classical exact diagonalization, Variational Quantum Eigensolver (VQE), and Sample-based Quantum Diagonalization (SQD). The experimental quintet ground state of FeO is recovered classically and with quantum algorithms, while a nonet ground state is recovered for Fe$_2$O$_2$. Although raw VQE does not achieve chemical accuracy for the ground state of FeO or Fe$_2$O$_2$, SQD with two connectivity shells recovers the exact ground energy for both molecules utilizing remarkably few quantum computational resources. Overall, our results indicate that $ab \; initio$-informed low-energy models of correlated materials, combined with SQD, offer a new alternative for scaling up calculations of ground-state properties of strongly correlated solids on existing quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36275v1
- Title: Quantum hydrodynamics from Nambu's unpublished fluid notes
- Authors: Kazuki Ikeda
- Categories: hep-th (primary); hep-th; math-ph; physics.flu-dyn; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36275v1  pdf=https://arxiv.org/pdf/2610.36275v1.pdf

Abstract:
We develop a quantum hydrodynamic theory based on Nambu's unpublished note \emph{A New Look at Fluid Dynamics}. The kinetic action defines a metric on configuration space and a mechanical connection coupling an observable cyclic deformation to unobserved fluid modes. Tracing out these modes yields a quantum channel for the observed deformation. We establish a criterion for the exact preservation of coherence between opposite momenta and show how nonzero connection curvature prevents this coupling from being removed. The leading quadratic decay of quantum coherence is determined by the prepared quantum state. For two shear flows, we identify an exact noiseless sign subsystem. Introducing additional generating flows cancels the initial residual of the Euler equations while producing nonzero connection curvature, governed by the same kinetic integrals that determine the classical correction. At fixed mean energy, choosing amplitudes adapted to the dominant coupling flow substantially reduces the initial decoherence, even along the direction that cancels the Euler residual. This advantage gradually diminishes under conditional evolution, eventually leading to a crossing of the decoherence curves. Our example shows that a preparation with a smaller initial coherence-decay coefficient can have a larger maximum sampled loss over a finite readout interval.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36359v1
- Title: Multi-day single-cell magnetic imaging of living cancer cells using Quantum Cell Monitoring
- Authors: Andre Pointner, Sarah Belasi, Regine Schneider-Stock, Roland Nagy
- Categories: physics.optics (primary); physics.optics; physics.bio-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36359v1  pdf=https://arxiv.org/pdf/2610.36359v1.pdf

Abstract:
Live-cell imaging of cellular and tissue samples relies predominantly on optical modalities, such as fluorescence, confocal, and multiphoton microscopy, in which cellular information is encoded in emitted photons. Photons scatter and attenuate in biological samples, restricting depth resolution, while the excitation light required to produce them induces photodamage that perturbs the very biology under observation. Magnetic fields, by contrast, traverse biological samples without attenuation at cellular length scales, but the imaging modality that extracts the encoded information, magnetic resonance imaging, cannot resolve individual cells. Here we present Quantum Cell Monitoring (QCM), a widefield nitrogen-vacancy magnetometry platform that encodes single-cell information in stray magnetic fields rather than emitted photons and reads it out at subcellular resolution. Integrated with a specialized live-cell incubator, QCM tracks magnetically labeled living cancer for up to 72 h through their individual magnetic field signatures. It captures single-cell mitosis and morphological remodeling, as well as cell cluster formation, splitting, and migration even within dense regions where brightfield contrast collapses. By shifting the carrier of single-cell information from propagating optical photons to static magnetic stray fields, QCM decouples cell from cellular optical accessibility and auto-fluorescence, enabling sustained live-cell observation in regimes inaccessible to optical microscopy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36416v1
- Title: Side jump and anomalous Lorentz transformation of a coherent Dirac wave packet
- Authors: Jin-Rui Wu, Shuai Y. F. Liu
- Categories: nucl-th (primary); nucl-th; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36416v1  pdf=https://arxiv.org/pdf/2610.36416v1.pdf

Abstract:
Spin-orbit coupling makes the mean position of a spinning particle transform anomalously under a Lorentz boost, with an additional shift known as a side jump. In this work, we develop a trace method to derive an exact but compact transformation kernel for the probability center of a general three-dimensional Dirac wave packet under an arbitrary finite Lorentz boost. The expression includes the physics of finite momentum width, spin-momentum correlations, and coherent phase structure without a semi-classical expansion. We identify texture-dependent side jumps even at fixed initial mean momentum, spin, and orbital angular momentum, as well as a non-monotonic mass dependence for Gaussian packets at fixed momentum width. The explicit kernels further resolve the spin and orbital angular-momentum contributions for massive and massless fermions, providing a kinematic basis for covariant particle-based spin transport that retains wave-packet information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36528v1
- Title: Measurement-induced entanglement phases in hyperbolic gauge-Higgs models
- Authors: Cole Kelson-Packer, Hiroki Sukeno, Akimasa Miyake
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.dis-nn; hep-lat; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36528v1  pdf=https://arxiv.org/pdf/2610.36528v1.pdf

Abstract:
Gauge-Higgs theory in flat spacetime provides a prime theoretical model of multiple phases of matter with distinct entanglement structures. More recently, there has been interest in hyperbolic space and the influence its extensive boundaries have on these structures. Entanglement transitions between non-equilibrium phases, such as topological phases, can be realized by the competition of non-commutating measurements. Here we study the entanglement phases of gauge-Higgs models on hyperbolic lattices described by measurement-only dynamics. We chart 2D phase diagrams by employing topological entanglement entropy and introducing a generalized measurement-induced entanglement tailored for hyperbolic Higgs phases. Utilizing duality, we find a phase absent in Euclidean space, wherein the bulk lattice hosts separated clusters of symmetry-protected topological order. Transitions between this "archipelago" phase and neighboring topological and trivial phases feature a critical exponent $δ$ belonging to a mean-field universality class. Our essential tool is a 3D resource state inspired by measurement-based quantum computation that simulates the spacetime evolution of the 2D quantum state with a third direction of entanglement. This allows us to analyze spacetime "sponges" of entanglement, which map to classical percolation theory and allow us to infer values of critical points on our phase diagrams' boundaries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36661v1
- Title: Kinetic Slush in Dissipative Rydberg Arrays
- Authors: Hufeng Wen, Ya-Xin Xiang, Qun-Li Lei, Thomas Pohl, Zhengyang Bai, Yu-Qiang Ma
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36661v1  pdf=https://arxiv.org/pdf/2610.36661v1.pdf

Abstract:
We investigate the nonequilibrium dynamics of a kinetic slush state realized via facilitated excitations in a two-dimensional dissipative Rydberg atom array. Utilizing kinetic Monte Carlo simulations in the strong dephasing regime, we show that tuning the laser detuning to compensate for nearest-neighbor interactions enables facilitated dynamics, while residual next-nearest-neighbor interactions induce kinetic frustration. This competition gives rise to an emergent slush phase characterized by pronounced dynamical heterogeneity and the coexistence of liquid- and solid-like configurations. By probing its nonequilibrium real-time evolution, we uncover a dynamical crossover from isotropic spreading to one-dimensional constrained growth, which can be continuously tuned by the frustration strength. Within this crossover regime, the slush dynamics generate fractal cluster geometries and generalized Ornstein-Zernike spatial correlations. Finite-size scaling analysis supports the system's proximity to criticality. Our findings establish driven-dissipative Rydberg systems as a highly controllable platform for engineering complex nonequilibrium soft-matter phenomena.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36700v1
- Title: Ancestor Lifting of Quasi-Cyclic Additive Codes and Certified Quantum Codes
- Authors: Liangdong Lu, Ran Xu, Ruipan Yang, Qiang Fu
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36700v1  pdf=https://arxiv.org/pdf/2610.36700v1.pdf

Abstract:
Additive codes over $\Ffour$ that are self-orthogonal under the trace inner product correspond to binary quantum stabilizer codes. We study 1-generator $(1,2)$-quasi-cyclic (QC) additive codes and their exact quantum distances. For composite lengths $n=\ell m$, an ancestor-lifting theorem transports dual words of the folded ancestor to the length-$n$ code. A two-layer decomposition for $\ell=2$ and a CRT splitting for odd $\ell$ yield dimension laws and explain equality, escape, and mixed-branch behavior in the certified examples. A palindromic criterion ensures symplectic self-orthogonality, while reversal pairing and a symplectic Gram rank formula describe broader construction families. Exact distances are established by information-set decoding screening, Brouwer--Zimmermann computation on the additive dual, and independent witness verification. We certify twenty-one record-breaking binary quantum codes across twenty entries of Grassl's code table, with twenty-eight certified members in total. Propagation improves thirty-four further entries, and explicit constructions are supplied for three table-tying GV entries marked Code Missing Construction. Six additional candidates are reported only with rigorous upper bounds and heuristic screening evidence. The results connect divisor-lattice structure in additive quasi-cyclic codes with reproducible certification of exact quantum distances.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36898v1
- Title: The Disordered Universe 2025: Open Effective Field Theories
- Authors: Alessandro Fumagalli, Francesco Paronetto, Leonardo Stanzani, Mattia Varrone, Lucas Vicente García-Consuegra, Thomas Colas, Paolo Benincasa, Guilherme Leite Pimentel
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36898v1  pdf=https://arxiv.org/pdf/2610.36898v1.pdf

Abstract:
Effective field theories (EFTs) offer a powerful method to unify diverse models under a small set of control parameters, allowing systematic expansions around well-established theories. While these techniques were traditionally developed for particle physics experiments with clean, isolated initial states, realistic macroscopic environments are often noisy and dissipative. Recognising the limitations of traditional EFTs has recently sparked intense progress at the interface of high-energy physics and condensed matter. These developments motivate a new approach to gravitation and cosmology, one that models the gravitational sector as evolving in the presence of an unobservable medium. Open Effective Field Theories provide a systematic, controllable framework for this endeavour. This chapter presents this versatile framework and illustrates how the Schwinger-Keldysh formalism captures the influence of unknown environments, manifesting as dissipation and noise, on observational probes. These notes are based on a series of lectures held during the La Ricotta Summer School "The Disordered Universe 2025" from 21 July to 1 August 2025.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.36976v1
- Title: Toward Circuit-Aware Mutation Testing for Quantum Programs: Exact Visibility and Execution Planning
- Authors: Andriy Miranskyy, Jose Campos
- Categories: cs.SE (primary); cs.SE; quant-ph
- Links: abs=https://arxiv.org/abs/2610.36976v1  pdf=https://arxiv.org/pdf/2610.36976v1.pdf

Abstract:
Mutation testing assesses test suites by introducing program changes and checking whether tests detect them. In quantum programs, a surviving mutant may leave program behavior unchanged, produce a change hidden by the chosen input or measurement, or remain undetected because statistical evidence is insufficient. We develop a circuit-aware framework to distinguish these causes and guide execution planning and test changes. The framework covers ideal, noiseless programs and mutations that replace one gate or subcircuit. The method traces how a mutation can affect measured outputs and combines established mathematical checks with statistical estimates. For supported cases, we establish conditions under which a test cannot reveal a mutation and exact formulas for its effect when the required state information is available. Under stated assumptions, we bound the mutation score while retaining surviving and unresolved mutants, and identify a restricted circuit family whose mutation effects admit efficient classical classification. The deliverables include a decision procedure, mathematical guarantees, worked examples of test changes and their implementation requirements, and a small-circuit reference implementation for differential expectation tests. These results help testers decide what to execute, what to change, and what remains unknown. The evidence is limited to proofs and executable examples under the ideal model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37009v1
- Title: Momentum-space entanglement and mutual information in Kaluza-Klein reduction
- Authors: Udaykrishna Thattarampilly, Yunlong Zheng
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2610.37009v1  pdf=https://arxiv.org/pdf/2610.37009v1.pdf

Abstract:
In theories with compact extra dimensions, the four-dimensional effective description is obtained by Kaluza-Klein reduction. The state available to a four-dimensional observer is the reduced density matrix obtained by tracing the higher-dimensional vacuum over the tower of massive modes, and it need not be pure. In this paper we study the momentum-space entanglement of this state for a five-dimensional scalar on $M_4\times S^1$ with a cubic or quartic self-interaction. We compute, at leading order in the coupling, the mutual information $I_n$ between the zero modes below a resolution scale $μ$ and a single Kaluza-Klein level $n$. When the zero modes couple linearly and without derivatives to pairs of tower modes, $I_n$ falls as $1/m_n$, where $m_n$ is the mass of level $n$. In the cubic theory, this tail is independent of the ultraviolet cutoff, with coefficient $(μR)^2/1024π^3$ for compactification radius $R$, and the mutual information with the whole tower grows logarithmically with the number of levels. In the quartic theory, the tail is masked by states containing additional hard quanta, which make $I_n$ depend on the cutoff. Compared with the corrections the tower makes to low-energy amplitudes, which are dominated by the lightest levels and captured by local operators, the mutual information with the tower is not dominated by any finite set of levels and arises from the time-nonlocal part of the effective action. The local four-dimensional effective theory therefore describes the low-energy observables of the reduced system but not its state. Unbroken supersymmetry cancels the vacuum energy of the compactification but not the mutual information, which at leading order is a sum of squared amplitudes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37122v1
- Title: Matrix Samplers and Quantum-Proof Extractors: Their Correspondence and Almost-Optimal Constructions
- Authors: Kuan Cheng, Ruiyang Wu
- Categories: cs.CC (primary); cs.CC; quant-ph
- Links: abs=https://arxiv.org/abs/2610.37122v1  pdf=https://arxiv.org/pdf/2610.37122v1.pdf

Abstract:
We establish an equivalence between matrix samplers and quantum-proof randomness extractors. The classical sampler--extractor equivalence is established by a seminal work of Zuckerman (Random Structures & Algorithms, 1997).   Using this equivalence, we construct explicit strong matrix samplers with optimal randomness overhead and near-optimal sample complexity via constructing quantum-proof extractors. Specifically for matrix dimension $D$, accuracy $\varepsilon$ and failure probability $δ\leq\varepsilon$, our matrix sampler uses $m+O_α(\log(D/δ))$ random bits and $O_α(\varepsilon^{-2-α}\log^{1+α}(D/δ))$ samples, for any constant $α>0$. Compared with the matrix sampler of Xun and Zuckerman (CCC 2025), our construction has improvements in two aspects. Under the same optimal random seed length, we can replace the $\operatorname{poly} D$ dependence in the number of samples by $O(\log^{1-γ} D)$. Under the same scale of sample size, we can remove their $\log\log D$ factor in the length of the random seed. Our underlying strong quantum-proof extractor has output length $n-O_α(a+\log(1/η))$ and seed length at most $(1+α)\log a+(2+α)\log(1/η)+O_α(1)$ for $n$-bit sources with conditional min-entropy $n-a$ and error $η$.   We also obtain strong quantum-proof extractors for every constant entropy rate, for any error as small as $2^{-Ω(n)}$, having optimal seed length $O(\log(n/η))$ and output length $Ω(n)$, improving previous constructions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37142v1
- Title: Threshold Criteria for Bosonic and Fermionic Trimers on a Square Lattice: A Birman--Schwinger Comparison
- Authors: Janikul Abdullaev, Abdumalik Eshniyozov, Mikhail Dolgopolov
- Categories: math-ph (primary); math-ph; cond-mat.quant-gas; math.SP; quant-ph
- Links: abs=https://arxiv.org/abs/2610.37142v1  pdf=https://arxiv.org/pdf/2610.37142v1.pdf

Abstract:
We compare two three-particle lattice models on the square lattice at total quasimomentum zero: three identical bosons with attractive contact interactions, and a two-fermion plus one distinguishable particle system with attractive interspecies contact. Using the Birman--Schwinger principle combined with symmetry reduction and strong-coupling asymptotics, we distinguish shared methodology from model-dependent spectral conclusions. For bosons, the ground-state energy behaves as minus three times the coupling plus six minus three over twice the coupling plus higher-order corrections, and exactly two bound states exist below the threshold for large coupling; the second lies at a finite distance 0.03542 below the threshold, a genuine eigenvalue rather than a threshold resonance. For fermions, the critical mass ratio is pi divided by pi minus two, approximately 2.75194; above it, a doubly degenerate level appears at strong coupling. Near onset, the binding energy follows a linear-over-logarithmic law. The results are compared with numerical finite-grid Faddeev computations and with recent three-dimensional classifications of threshold states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.37654v1
- Title: Mediated Interactions between Fermi Polarons in the Strongly Interacting Regime
- Authors: Renato Pessoa, S. A. Vitiello, Luis A. Peña Ardila
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2610.37654v1  pdf=https://arxiv.org/pdf/2610.37654v1.pdf

Abstract:
Mediated interactions between quasiparticles lie at the heart of Landau Fermi-liquid theory, yet their behavior in the strongly correlated regime is not fully understood. Motivated by recent experiments [Nat. Phys. 20, 68--73 (2024)], we investigate mediated interactions between quasiparticles emerging from a Fermi sea---Fermi polarons---using zero-temperature quantum Monte Carlo methods. Our main result is that the Landau interaction between polarons remains repulsive in the strongly interacting regime for any coupling strength in the polaronic branch, in contrast to the downward trend observed experimentally near resonance. Deep in the short-range universal regime, our results are insensitive to the microscopic details of the interaction potential, providing robust evidence for the sign of the ground-state induced interaction. In addition, we determine the real-space interaction between static impurities, recovering a Ruderman-Kittel-Kasuya-Yosida (RKKY)-like behavior at weak coupling and the nonperturbative Born-Oppenheimer result at strong coupling. More broadly, our results establish a microscopic benchmark for how Landau quasiparticle interactions survive beyond the perturbative regime of strongly correlated quantum matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2310.02248v2
- Title: A variational coherent quantum annealing protocol
- Authors: N. Barraza, G. Alvarado Barrios, E. Solano, F. Albarrán-Arriagada
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2310.02248v2  pdf=https://arxiv.org/pdf/2310.02248v2.pdf

Abstract:
We introduce variational coherent quantum annealing (VCQA), a hybrid protocol that optimizes finite-time annealing schedules within a low-dimensional parameter space. We consider three schedule functions that interpolate between the initial, problem (final), and auxiliary Hamiltonians, each represented by a piecewise cubic Hermite interpolant. The auxiliary Hamiltonian is a problem-informed, longitudinal, and local field that vanishes at both ends of the evolution, providing a mechanism to enlarge the minimum energy gap. We benchmark our protocol on QUBO and (HUBO) instances, as well as, a non-stoquastic model, using systems of up to ten qubits. With only six variational parameters for the entire protocol, we find that the characteristic time of the adiabatic-like evolution is reduced by at least a factor of 2.4 in every case. These finite-size, closed-system results establish VCQA as a compact control ansatz and motivate tests under hardware noise and control constraints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2401.09007v3
- Title: Operator quantum singular value transformation: Spectral mapping, design and topological invariants
- Authors: Chusei Kiumi, Yohei Tanaka, Akito Suzuki
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2401.09007v3  pdf=https://arxiv.org/pdf/2401.09007v3.pdf

Abstract:
Quantum singular value transformation (QSVT) provides a unifying framework for quantum algorithms by applying the polynomials of quantum signal processing (QSP) to block-encoded matrices. We connect this framework with spectral analysis, design and topological protection in condensed matter physics. Extending QSVT beyond matrices to possibly infinite-dimensional operators (operator QSVT), we establish the following. First, it transforms every block of the operator by the QSP polynomials; no singular value decomposition is needed. Second, a spectral mapping theorem determines the full spectrum of the QSVT operator, including continuous spectra, from the embedded operator through the QSP polynomial, allowing spectral analysis without translation invariance. Third, the spectral mapping turns QSP into spectral design: the QSP phases can stretch, fold and separate the bands and place the eigenvalues. Finally, the kernel sectors that conventional QSVT usually sets aside carry a topological index, invariant under the choice of QSP phases, local perturbations and gap-preserving deformations, which guarantees topologically protected states. These results unify two quantum walks: Szegedy's walk from quantum algorithms and the split-step walk from condensed matter physics. Their kernel sectors encode the graph's Euler characteristic and the difference of bulk winding numbers, respectively. For the split-step walk, QSP breaks chiral symmetry but not the topological protection, and can move the protected state into a continuous band to form a bound state in the continuum (BIC).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2507.20667v2
- Title: Utilizing Partitioning for Distributed Tensor Network Contraction
- Authors: Manuel Geiger, Qunsheng Huang, Christian B. Mendl
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.20667v2  pdf=https://arxiv.org/pdf/2507.20667v2.pdf

Abstract:
Tensor networks have proven to be a valuable tool, for instance, in the classical simulation of (strongly correlated) quantum systems. As the size of the systems increases, contracting larger tensor networks becomes computationally demanding. In this work, we explore the use of partitioning to distribute the contraction task across a distributed memory architecture, commonly found in high-performance computing environments. This approach offers a promising alternative to the widely used parallelization based on slicing, which often incurs significant computational overhead. We particularly investigate how a given partitioning can be optimized to enable efficient contraction, as both computational and memory costs are highly sensitive to the chosen strategy. To this end, we introduce a simulated annealing-based method that iteratively refines a partitioning to minimize the operation count along the critical path, thereby reducing time-to-solution. The algorithm is evaluated on MQT Bench circuits and achieves a lower computational cost in 47 of 71 circuits, with improvements up to 5 orders of magnitude compared to contraction paths generated by Cotengra, a state-of-the-art contraction path finding library.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2508.17040v3
- Title: Robust Preparation of Bell States by Time Boundary Effect
- Authors: Jia-Nan Wu, Bingsuo Zou, Guojun Jin, Yongyou Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.17040v3  pdf=https://arxiv.org/pdf/2508.17040v3.pdf

Abstract:
Quantum entanglement is essential for modern quantum information processing. Entanglement gates convert initially non-entangled states into entangled ones by applying time-dependent parametric pulses. While Bell state preparation has been experimentally validated in various platforms, its stability and fidelity are constrained by environmental decoherence and parametric fluctuations. Here, we propose a dynamically robust method for preparing Bell states by leveraging the time boundary effect and momentum-space projective measurements within Su-Schrieffer-Heeger systems. Employing the Lindblad master equation, we theoretically demonstrate that the prepared Bell states exhibit remarkable robustness against both environmental decoherence and parametric time fluctuations, achieving nearly perfect quantum fidelity, with the momentum conservation law governing this robust behavior. This framework based on the time boundary effect is applicable to both fermionic and bosonic excitations, offering a unified paradigm for generating Bell states in quantum computation and communication.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2510.08267v2
- Title: Low-depth measurement-based deterministic quantum state preparation
- Authors: Roselyn Nmaju, Fiona Speirits, Sarah Croke
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.08267v2  pdf=https://arxiv.org/pdf/2510.08267v2.pdf

Abstract:
We present a low-depth amplitude encoding method for arbitrary quantum state preparation. Building on the foundation of an existing divide-and-conquer algorithm, we propose a method to disentangle the ancilla qubits from the final state. Our method is measurement-based but deterministic, and offers an alternative approach to existing state preparation algorithms. It has circuit depth $Θ(n^2)$ and requires $Θ(2^n)$ ancilla qubits. The resulting spacetime allocation is $Θ(2^n)$, which is optimal. Furthermore, we go beyond scaling arguments to precisely quantify the resources needed for any $n$. We illustrate our method through detailed worked examples of both a ``dense'' state and a W-state. Finally, we demonstrate how to combine this method with existing methods to construct hybrid algorithms with varying space and circuit depth complexities.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2510.17248v2
- Title: Nonstabilizerness as a diagnostic of criticality and exceptional points in non-Hermitian spin chains
- Authors: Cătălin Paşcu Moca, Doru Sticlet, Balázs Dóra
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2510.17248v2  pdf=https://arxiv.org/pdf/2510.17248v2.pdf

Abstract:
We investigate nonstabilizerness, also known as ``magic,'' to understand criticality and exceptional points in non-Hermitian quantum many-body systems. Our focus is on parity-time ($\mathcal{PT}$)-symmetric spin chains, specifically the non-Hermitian transverse-field Ising and XX models. We calculate stabilizer Rényi entropies in their ground states using non-Hermitian matrix product state methods. Our findings show that magic exhibits unique and model-specific signs of phase transitions. In the Ising chain, it peaks near the regular Hermitian-like critical line but disappears across exceptional points. In contrast, in the XX chain, it reaches its maximum at the exceptional line where $\mathcal{PT}$ symmetry is broken. Finite-size scaling reveals that these effects become more pronounced with larger systems, highlighting nonstabilizerness as a sensitive marker for both quantum criticality and non-Hermitian spectral degeneracies. We also investigate magic in momentum space for the XX model analytically and find that it reaches a minimum around exceptional points. Our results indicate that magic takes extremal values at the exceptional points and serves as a valuable tool for examining complexity, criticality, and symmetry breaking in non-Hermitian quantum matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2512.03029v2
- Title: Combinatorial foundations for solvable chaotic local Euclidean quantum circuits in two dimensions
- Authors: Fredy Yip
- Categories: quant-ph (primary); quant-ph; math.CO; math.MG
- Links: abs=https://arxiv.org/abs/2512.03029v2  pdf=https://arxiv.org/pdf/2512.03029v2.pdf

Abstract:
We investigate a graph-theoretic problem motivated by questions in quantum computing concerning the propagation of information in quantum circuits. A graph $G$ is said to be a bounded extension of its subgraph $L$ if they share the same vertex set, and the graph distance $d_L(u, v)$ is uniformly bounded for edges $uv\in G$. Given vertices $u, v$ in $G$ and an integer $k$, the geodesic slice $S(u, v, k)$ denotes the subset of vertices $w$ lying on a geodesic in $G$ between $u$ and $v$ with $d_G(u, w) = k$. We say that $G$ has bounded geodesic slices if $|S(u, v, k)|$ is uniformly bounded over all $u, v, k$. We call a graph $L$ geodesically directable if it has a bounded extension $G$ with bounded geodesic slices.   Contrary to previous expectations, we prove that $\mathbb{Z}^2$ is geodesically directable. Physically, this provides a setting in which one could devise exactly-solvable chaotic local quantum circuits with non-trivial correlation patterns on 2D Euclidean lattices. In fact, we show that any bounded extension of $\mathbb{Z}^2$ is geodesically directable. This further implies that all two-dimensional regular tilings are geodesically directable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2604.12976v2
- Title: Hamiltonian Chaos
- Authors: Steven Tomsovic
- Categories: quant-ph (primary); quant-ph; nlin.CD; physics.class-ph
- Links: abs=https://arxiv.org/abs/2604.12976v2  pdf=https://arxiv.org/pdf/2604.12976v2.pdf

Abstract:
Through semiclassical methods the subject of quantum chaos motivates and depends on Hamiltonian chaos research. Presented here is a selection of some of the most important Hamiltonian chaos topics that in this way get directly related to any of a variety of quantum chaos research problems. The overall emphasis is on intuitive explanations and illustrations of various ideas with the references containing more mathematically rigorous expositions. The chapter begins with a description of various useful theoretical and computational tools of chaos research, e.g.~surfaces of section, paradigms of chaos, stability analysis, and symbolic dynamics... This is followed by discussions regarding the geometry of chaos, how chaotic systems respond to perturbations, and the complexification of Hamiltonian dynamics. Most of the contents concern topics that are long established and well known by now. The exceptions involve complications that arise from the complexification of phase space variables and time. There are relatively recent results summarized regarding the appropriate branches of determinant phases and how to distinguish complex trajectories that are associated with classically allowed processes versus those associated with non-allowed ones.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2604.13172v2
- Title: Simple slow operators and quantum thermalization
- Authors: Tian-Hua Yang, Ethan Jeon, Sarang Gopalakrishnan, Dmitry A. Abanin
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2604.13172v2  pdf=https://arxiv.org/pdf/2604.13172v2.pdf

Abstract:
We establish a rigorous operator-space condition for the thermalization of typical initial states. We introduce a concept of simple slow operators (SSOs), defined as operators that evolve slowly under Heisenberg-picture dynamics and have significant small-sized components. We show that the non-thermalization of typical initial states drawn from a weakly entangled state ensemble implies the existence of SSOs; equivalently, the absence of SSOs implies that typical initial states thermalize. We establish these results by introducing the concept of an ensemble variance norm of an operator, defined as the typical magnitude of the expectation value of that operator with respect to states in the ensemble. For low-entanglement ensembles, the norm is related to operator sizes, allowing us to establish a direct link between operator dynamics and thermalization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2605.02056v3
- Title: Benchmarking quantum trial wavefunctions for phaseless auxiliary-field quantum Monte Carlo
- Authors: Rod Rofougaran, Neil Mehta, Katherine Klymko, Pooja Rao, J. Wayne Mullinax, Samuel Stein, Norm M. Tubman, Ermal Rrapaj
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.02056v3  pdf=https://arxiv.org/pdf/2605.02056v3.pdf

Abstract:
The phaseless auxiliary-field quantum Monte Carlo (ph-AFQMC) method is a stochastic imaginary-time projection method for computing ground-state properties of strongly correlated quantum systems, whose accuracy depends critically on the trial wavefunction. We present a benchmarking study of trial wavefunctions prepared using parameterized quantum circuits, spanning unitary coupled cluster (UCC), Hamiltonian-informed, Jastrow-inspired, and adaptively constructed ansatzes, and evaluate their accuracy, expressibility, and resource requirements within the quantum-computing-enhanced AFQMC (QC-AFQMC) framework. Trial states are prepared with GPU-accelerated statevector simulations using CUDA-Q and tested on stretched linear hydrogen chains and nine closed-shell molecules at equilibrium with varying static correlation. We find that at similar parameter counts, ph-AFQMC largely removes differences between families for weakly and moderately correlated systems: every trial yields a ph-AFQMC energy within chemical accuracy despite trial energy errors spanning nearly three orders of magnitude, whereas ansatz choice becomes consequential as static correlation grows. Our results indicate that trial variational energy is not always a reliable indicator of ph-AFQMC quality, and that adding variational parameters can lower the trial energy while degrading the ph-AFQMC energy. Across our benchmark systems, trial fidelity ranks trials more reliably than variational energy, and for spin-contaminated trials, the singlet-projected fidelity is more reliable than unprojected fidelity. The UCCSD ansatz initialized from unrestricted CCSD amplitudes provides a robust and inexpensive-to-optimize baseline across benchmark systems, with circuit depth as its principal limitation, while adaptive and compact layered ansatzes remain competitive in accuracy under strong correlation with substantially shallower circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2605.02986v4
- Title: Exploiting all ancilla outcomes in linear combinations of unitaries: low-rank recovery and quantum trapdoor functions
- Authors: Ammar Daskin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.02986v4  pdf=https://arxiv.org/pdf/2605.02986v4.pdf

Abstract:
The linear combination of unitaries (LCU) is a fundamental quantum computing primitive used to embed non-unitary operators into larger systems via ancilla post-selection. In standard LCU implementations, only the zero-state ancilla outcome is retained, while all other measurement branches are discarded as unusable overhead. We study these discarded parts. Every computational-basis outcome of the ancilla projects the system onto a different linear combination of the target unitaries; collecting these outcome states in a matrix gives a factorization $Φ=CX$, where $C$ is determined by the ancilla preparation and the rows of $X$ are the states $U_t|ψ\rangle$, so that $rank(Φ)\le K$. Although this holds for any LCU circuit; to make the analysis easier, we use a simplified model circuit with Hadamard gates on the index register and a single rotation qubit in place of the coefficient preparation unitary, in which $C$ is explicit. The structure suggests two complementary applications: (i) in an explicit amplitude-access model, classical low-rank matrix completion can reconstruct the full output (including the target) from a subset of its amplitude entries, while computational basis counts provide intensities and generally require additional phase information for full complex recovery; (ii) treating $C$ as a secret key suggests a candidate quantum trapdoor function, whose security remains informal and depends on the difficulty of structured phase retrieval. The scheme thus turns the "junk" ancilla outcomes into a structured resource, possibly opening paths for further applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2609.05904v2
- Title: Boundary-Canceled Score-Hamiltonian Sampling
- Authors: Masayuki Ohzeki
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2609.05904v2  pdf=https://arxiv.org/pdf/2609.05904v2.pdf

Abstract:
Diffusion sampling is related to imaginary-time quantum annealing through a forward/backward Schrödinger equation pair and its one-sided counterdiabatic connection. For a smooth, gapped Score-Hamiltonian path, the exact connection transports the target density at any evolution time. We apply quantum-annealing performance analysis to residuals from approximating this connection with a trained score. If the first $r$ terminal schedule derivatives vanish, the squared Hellinger error scales as $T^{-2r-2}$, with a prefactor determined by the terminal learning residual and inverse gaps. Direct two-dimensional imaginary-time evolution with one fixed neural score reproduces these powers and prefactors. Terminal schedule design thus suppresses the distributional effect of imperfect score learning without retraining the network.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.30645v2
- Title: FVQKD: A Formal Verification of Quantum Key Distribution Security in Rocq
- Authors: Ruixuan Deng, Zhengfeng Ji, Jiayu Zhang, Li Zhou
- Categories: quant-ph (primary); quant-ph; cs.CR; cs.LO
- Links: abs=https://arxiv.org/abs/2610.30645v2  pdf=https://arxiv.org/pdf/2610.30645v2.pdf

Abstract:
Quantum key distribution (QKD), whose security is derived from quantum mechanics rather than computational assumptions, is moving into standardization and commercial deployment. Yet its security guarantees rest on technically delicate proofs checked by hand. Formal verification closes this gap, establishing a two-factor assurance: unconditional security from physical principles, and machine-checked proofs against reasoning errors. We present FVQKD, a Rocq library for machine-checking QKD security proofs. Its first result is a complete, end-to-end machine-checked proof of composable, finite-key security for BB84. The mechanization reconstructs the complete proof infrastructure from first principles, including the smooth entropy framework, the entropic uncertainty relation, and the Quantum Leftover Hash Lemma. It uncovers necessary side conditions that the published argument leaves unstated, one of which reveals a missing proof branch, and it grounds the information-theoretic bound in a formal semantics of protocol execution, which the pen-and-paper analysis lacks. The proof is entirely admit-free, relying only on the Rocq kernel and standard foundational axioms. To our knowledge, this is the first end-to-end formal verification of a QKD security proof. Built on MathComp, MathComp-Analysis, and CoqQ, the development provides quantum-information infrastructure designed for reuse across broader QKD variants and quantum cryptography applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.31359v2
- Title: Finite Systems in the Space of Projective Measurements
- Authors: Miguel Flores R., Carlos A. Muñoz
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2610.31359v2  pdf=https://arxiv.org/pdf/2610.31359v2.pdf

Abstract:
We investigate the dynamics of two-level systems using the quasidistribution $Q$ function projected onto the space of collective measurements. Particular attention is given to evolution under Hamiltonians that are invariant under particle permutations, for pure states that are either invariant or noninvariant under such permutations. This requires constructing an approximate analog of the star product between quasidistribution functions: the projected $Q$ function of a product of two operators is expressed approximately in terms of the individual operators' $Q$ and $P$ functions. We rewrite the Liouville equation to determine approximate state dynamics and compare the result with exact evolution using the Hellinger distance. Overall, the method performs well for permutation-invariant pure states and Hamiltonians, whereas deviations arise for arbitrary pure states and noninvariant Hamiltonians.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.35227v2
- Title: A Control Line Multiplexing Framework for Scalable Quantum Computing
- Authors: Dayu Li, Naibin Zhou, Zhiyuan Chen, Zihua Chen, Yu Xu, Yuan Li, Daojin Fan, Wenhao Chu, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.35227v2  pdf=https://arxiv.org/pdf/2610.35227v2.pdf

Abstract:
Universal fault-tolerant superconducting quantum computers are expected to require millions of physical qubits; yet extending the prevailing dedicated-control-line paradigm to this scale would exceed the wiring density and cooling-power budget of dilution refrigerators. Microwave frequency-division multiplexing (FDM) revolutionized classical communications by enabling many independent channels to share common transmission infrastructure. Translating this principle to superconducting quantum control, however, requires an all-microwave architecture and experimental validation of frequency-multiplexed gate control. Recent work in quantum error correction has demonstrated microwave-based readout, single-qubit gates and leakage suppression, whereas two-qubit gates remain predominantly driven by unipolar pulses and thus constitute the missing element of an all-microwave architecture. Here, we propose a periodically extensible hybrid multiplexing framework in which all gate operations are frequency-division multiplexed using polychromatic microwave pulses and band-pass filters, thereby reducing the required control-line count by one to two orders of magnitude. In a 1:4 demonstration, we achieve average errors of $(6.4\pm0.2)\times10^{-3}$ for parallel FDM CZ gates and $(10.6\pm0.2)\times10^{-4}$ for parallel FDM $XY(π/2)$ gates, without statistically significant multiplexing-induced degradation. Together with on-chip DC sources, this FDM-based gate-control scheme completes the last missing module in a scalable multiplexed-control architecture toward universal fault-tolerant quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.35445v2
- Title: Multistability and Critical Frustrated Superradiance in Open Anisotropic Quantum Rabi Trimer
- Authors: Ya-Ping Ni, Yi-Ge Wu, Jie-Qiao Liao, Jin-Feng Huang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.35445v2  pdf=https://arxiv.org/pdf/2610.35445v2.pdf

Abstract:
We study the nonequilibrium steady states of an open anisotropic quantum Rabi trimer. Combining semiclassical and quantum mechanical treatments, we map out the system's phase diagram and elucidate the critical phenomena induced by anisotropic light-matter coupling, cavity dissipation, and complex photon hopping, which give rise to abundant multistable phases. Counterintuitively, the frustrated superradiant phase (FSP) can be stabilized by both positive and negative photon hopping, a feature absent in closed Rabi and Dicke trimers. We further uncover two independent dissipation thresholds for the normal superradiant phase and the FSP. Unlike isotropic open quantum Rabi trimers, both phases are suppressed once the dissipation exceeds their respective critical values. The rotating and counter-rotating interaction terms exhibit mutually reciprocal effects on the quantum phase transitions. By analyzing universal scaling behaviors with quantum fluctuations incorporated, we reveal an unprecedented finite-fluctuation critical exponent for the FSP. Moreover, the critical exponents of individual phases are coupling-strength dependent. The multistability and FSP can be tuned by anisotropy and dissipation. Our results broaden the scope of nonequilibrium quantum phase physics in few-body systems and hold promising applications for quantum state engineering and cavity/circuit quantum electrodynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.35660v2
- Title: Quantum computation of energy level degeneracy and thermodynamical properties of spin systems
- Authors: V. M. Tkachuk, M. I. Samar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2610.35660v2  pdf=https://arxiv.org/pdf/2610.35660v2.pdf

Abstract:
We propose a hybrid quantum-classical method for reconstructing energy-level degeneracies and thermodynamic properties of spin systems. A single ancilla qubit is used to measure the partition function at imaginary inverse temperatures. For spectra lying on a known equally spaced energy grid, the inverse discrete Fourier transform allows exact reconstruction of degeneracies in the absence of noise, without spectral leakage. The quantum circuits are optimized using commuting interactions and Eulerian ordering. We demonstrate the method for frustrated Ising antiferromagnets on periodic Kagome graphs with up to 36 spins, using the ibm_kingston quantum processor. Despite substantial circuit depth and hardware noise, the reconstructed spectra retain their dominant features, and the calculated heat capacities reproduce the main temperature dependence of the exact results.   Keywords: partition function, imaginary temperature, Ising model, heat capacity, ancilla qubit, quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2102.13248v4
- Title: Quantum structured light: Non-classical spin texture of twisted single-photon pulses
- Authors: Li-Ping Yang, Zubin Jacob
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2102.13248v4  pdf=https://arxiv.org/pdf/2102.13248v4.pdf

Abstract:
Classical structured light with controlled polarization and orbital angular momentum (OAM) of electromagnetic waves has varied applications in optical trapping, bio-sensing, optical communications and quantum simulations. The classical electromagnetic theory of such structured light beams and pulses have advanced significantly over the last two decades. However, a framework for the quantum density of spin and OAM for single-photons remains elusive. Here, we develop a theoretical framework and put forth the concept of quantum structured light for space-time wavepackets at the single-photon level. Our work marks a paradigm shift beyond scalar-field theory as well as the paraxial approximation and can be utilized to study the quantum properties of the spin and OAM of all classes of twisted quantum light pulses. We capture the uncertainty in full three-dimensional (3D) projections of vector spin demonstrating their quantum behavior beyond the conventional concept of classical polarization. Even in laser beams with high OAM along the propagation direction, we predict the existence of large OAM quantum fluctuations in the transverse plane which can be verified experimentally. We show that the spin density generates modulated helical texture beyond the paraxial limit and exhibits distinct statistics for Fock-state vs. coherent-state twisted pulses. We introduce the quantum correlator of photon spin density to characterize the nonlocal spin noise providing a rigorous parallel with fermionic spin noise operators. Our work paves the way for quantum spin-OAM physics in twisted single photon pulses and also opens explorations for new phases of light with long-range spin order.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2510.05198v2
- Title: Intrinsically Quantum Effects of Axion Dark Matter are Undetectable
- Authors: Yunjia Bao, Dhong Yeon Cheong, Nicholas L. Rodd, Joey Takach, Lian-Tao Wang, Kevin Zhou
- Categories: hep-ph (primary); hep-ph; astro-ph.CO; hep-ex; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2510.05198v2  pdf=https://arxiv.org/pdf/2510.05198v2.pdf

Abstract:
Is the usual treatment of axion dark matter as a classical field reliable? We show that the answer is subtle: the axion field could well be in a quantum state that has no complete classical description, but realistic detectors cannot tell the difference. To see this, we solve a fully quantum model of axion detection using quantum optics techniques. We show that intrinsically quantum effects are washed out by mode averaging or small amounts of noise, and significantly suppressed by the weakness of the axion coupling. Our work exemplifies that there should always be a classical analog for axion dark matter effects, extends to other wave (ultralight) dark-matter candidates, and gives a general method to compute the effects of exotic dark-matter states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2603.24052v2
- Title: Data-driven synthesis of high-fidelity triaxial magnetic waveforms for quantum control
- Authors: Giuseppe Bevilacqua, Valerio Biancalana, Roberto Cecchi
- Categories: physics.ins-det (primary); physics.ins-det; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2603.24052v2  pdf=https://arxiv.org/pdf/2603.24052v2.pdf

Abstract:
We present a system for generating arbitrary, triaxial magnetic waveforms with a spectral content spanning from DC to tens of kHz, a critical capability for quantum control and spin manipulation. To compensate for amplifier-coil dynamics, we implement a data-driven approach to identify a numerical compensation model. The method parametrizes the system response using a Finite Impulse Response (FIR) filter calibrated on the specific waveform to be generated. The application of a driving signal designed via frequency-domain inversion of the identified model enables the synthesis of complex field sequences with sharp transitions between static and single- or multi-frequency temporal segments. The work is validated with experimental results demonstrating waveform fidelity and transient performance, thereby showcasing the precision and feasibility of the method.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2606.00968v2
- Title: Fundamental Limit for One versus Two Point Sources Detection using Direct Imaging
- Authors: Parth Hemant Darekar, Amit Kumar Jha, Michael R. Grace, Aqil Sajjad, Saikat Guha
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2606.00968v2  pdf=https://arxiv.org/pdf/2606.00968v2.pdf

Abstract:
We consider the task of distinguishing between a single weak incoherent optical point source and two weak incoherent optical point sources located symmetrically about the first source. $θ$ is the separation between the two point sources scaled to the Point Spread Function (PSF) width in the image plane. Using an ideal focal plane array of intensity detectors (ideal direct imaging), we quantify the performance using the Bhattacharyya distance and find the scaling of its leading order term in terms of $θ$ in the sub-Rayleigh regime. A suite of previous analyses of this problem lacked a comprehensive analysis for when the amplitude spread function (ASF) of the imaging system has zeros and reported a scaling that we find to be incorrect. We complete this analysis by explicitly calculating the leading order term of the Bhattacharyya distance for ideal direct imaging with any ASF, for small $θ$ and show the difference in scaling based on the presence or absence of zeros in the ASF. This is similar to the ASF dependent performance in the task of estimating the separation between the two point sources and the task of detecting a change to an object. We then apply our results to the specific example of a Gaussian and a Sinc ASF and show good agreement with numerical calculations. Our results allow the accurate comparison of other measurement schemes with ideal direct imaging, and to the quantum limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2606.18349v2
- Title: Ghosts versus Unstable Particles in Quantum Field Theory
- Authors: Luca Buoninfante
- Categories: hep-th (primary); hep-th; gr-qc; hep-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2606.18349v2  pdf=https://arxiv.org/pdf/2606.18349v2.pdf

Abstract:
We elucidate the physical nature of ghosts above the multi-particle threshold by contrasting them with unstable particles in quantum field theory. We first consider the asymptotic formulation, where ordinary positive-norm one-particle states can be unstable and decay, whereas ghosts survive asymptotically without decaying, yet admit no particle interpretation due to interference with the multi-particle component which masks the negative-norm one-particle state. This distinction originates from two different analytic structures of the dressed propagator, whose complex conjugate poles lie on the first or second Riemann sheet in the ghost or ordinary case, respectively. Ghost resonances are, in principle, phenomenologically distinguishable from ordinary ones, being narrower and exhibiting weaker interference between positive- and negative-energy peaks. We then formulate the quantum field theory in a finite interval of time and, working within a suitable approximation for the dressed propagator, find that finite-time effects amplify differences in the resonant behavior and give rise to new features, such as higher peaks in ghost resonances. Distinct temporal regimes are also identified: for times shorter than the inverse width, an approximate free-particle description is valid; at later times interactions and interference dominate, leading to decay or multi-particle masking. This study supports the absence of freely propagating ghost particles in the asymptotic limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2606.24468v2
- Title: Entanglement of momenta at colliders
- Authors: Marco Fabbrichesi, Roberto Floreanini, Luca Marzola
- Categories: hep-ph (primary); hep-ph; hep-ex; quant-ph
- Links: abs=https://arxiv.org/abs/2606.24468v2  pdf=https://arxiv.org/pdf/2606.24468v2.pdf

Abstract:
We investigate the entanglement in the momenta of particle pairs produced at colliders, discarding the information on their spin state. We show how to quantify this entanglement by reducing the continuous momentum variables to a two-qubit system through hemispherical projections. We discuss in detail the production of $τ$-lepton pairs at an electron collider. In the Standard Model, the discretized momenta are in a genuinely maximally entangled pure state for suitable choices of the hemispheres.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.30321v2
- Title: Extreme competition between stripes and superconductivity in the hole-doped Hubbard model
- Authors: Ao Chen, Johnnie Gray, Si-Jing Du, Garnet Kin-Lic Chan
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.dis-nn; cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2610.30321v2  pdf=https://arxiv.org/pdf/2610.30321v2.pdf

Abstract:
The two-dimensional Hubbard model was originally proposed as the minimal model of uniform $d$-wave superconductivity in the cuprate high-temperature superconductors, but recent calculations with relevant parameters in a realistic doping regime have often found other ground states. Further, uncertainty remains over such results due to the intrinsic bias of different computational methods. Here we address this uncertainty through state-of-the-art neural tensor network and neural backflow state simulations, enabled by large-scale GPU computation, that together reach an unprecedented variational accuracy on lattices with up to 1024 sites. At $1/8$ doping in the pure Hubbard model, as well as with next-nearest-neighbor hopping relevant to the hole-doped cuprates, we reveal a near degeneracy among a low-energy uniform $d$-wave state, superconducting stripes, and non-superconducting stripe states on the milli-$t$ energy scale. Our work rebalances the narrative that the Hubbard model supports a single dominant order in relevant parameter regimes towards a picture of extreme competition between stripes and superconductivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-10-28 14:59
- arXiv: 2610.34330v2
- Title: On the uniqueness of translation-invariant ground states of the $S=1$ Heisenberg and $J$--$D$ antiferromagnetic chains
- Authors: Hal Tasaki
- Categories: math-ph (primary); math-ph; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2610.34330v2  pdf=https://arxiv.org/pdf/2610.34330v2.pdf

Abstract:
Using the analytic machinery and numerical inputs of OpenAI's proofs of the Haldane gap, we prove uniqueness of the translation-invariant ground state of the infinite $S=1$ Heisenberg antiferromagnetic chain and of the $J$-$D$ model for sufficiently small $|D|$. Uniqueness is among all translation-invariant ground states in the operator-algebraic sense, without assuming a gap or spin-rotation symmetry for a competing state. The proof combines concentration of the spatial transfer spectrum, an exponentially small low-temperature free-energy correction, and a Golden--Thompson comparison for separated local observables. The unique translation-invariant state is pure, locally unique and gapped, and continuous in $D$. The ground states of even periodic chains and odd open chains with equal positive endpoint fields converge to this state along their full sequences, uniformly in $D$, with a stretched-exponential local rate. Every choice of ground states of open chains without endpoint magnetic fields has the same local limit. These conclusions do not establish uniqueness among arbitrary nontranslation-invariant ground states of the infinite chain.   The author formulated the problems and proposed the core strategies. ChatGPT Astra made substantial contributions to developing the proofs and preparing the manuscript.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

