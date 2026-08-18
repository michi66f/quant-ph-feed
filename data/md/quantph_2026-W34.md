- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13614v1
- Title: A Quantum Optimization Framework for Data-Assimilation-Augmented Parameter Estimation
- Authors: Muhammad Jalil Ahmad, Mohammadhossein Mohammadisiahroudi, Animikh Biswas, Kathleen Hoffman
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13614v1  pdf=https://arxiv.org/pdf/2608.13614v1.pdf

Abstract:
Parameter estimation is a fundamental challenge in the calibration of ordinary differential equation (ODE) models, where repeated numerical integration can lead to high computational cost. In this work, we investigate whether quantum algorithms can be leveraged to assist parameter estimation in nonlinear dynamical systems. We develop a hybrid classical-quantum framework that reformulates a data-assimilation-augmented parameter estimation problem as a combinatorial optimization task. Model dynamics and data assimilation are enforced entirely on the classical side, while the resulting parameter estimation cost functional is discretized and approximated by a quadratic unconstrained binary optimization (QUBO) surrogate. This surrogate is mapped to an Ising Hamiltonian, and quantum optimizers are used to search for low-energy configurations corresponding to candidate parameter estimates. We apply the framework to SIS and SIR epidemic models, the chaotic Lorenz-63 system, and a high-dimensional two-layer Lorenz-96 system. In this setting, the method is used to recover classical system parameters from partial state observations across steady-state, chaotic, and high-dimensional multiscale dynamical systems. Numerical experiments with synthetic data show that the proposed approach accurately recovers parameters while requiring data-assimilation solves only on a prescribed coarse grid. The framework avoids quantum state tomography, illustrating a viable pathway for integrating quantum optimization into data-driven parameter estimation for nonlinear dynamical systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13627v1
- Title: A scalable edge-pass Purcell filter for high-fidelity readout of superconducting qubits
- Authors: Xudong Liao, Yuan Li, Sainan Huai, Shuyi Pan, Zhenxing Zhang, Zhiwen Zong, Kunliang Bu, Yulei Ye, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13627v1  pdf=https://arxiv.org/pdf/2608.13627v1.pdf

Abstract:
High-fidelity readout with strong Purcell protection of qubit coherence is essential for scalable superconducting quantum processors, yet the finite passband and sizable footprint of conventional band-pass Purcell filters make them hard to scale. Here we introduce a scalable edge-pass Purcell filter that separates the readout band from the protected qubit band by a single transmission edge, freeing the readout resonators from bandwidth constraint. Depending on whether the transmitting band lies above or below the cutoff, the compact network is realized as a high-pass filter (HPF) or a low-pass filter (LPF). The HPF reaches an average readout fidelity of 99.46(4)% (up to 99.56%) with a 150-ns pulse, and the LPF reaches 99.49(3)% (up to 99.57%) with a 130-ns pulse. The average single-qubit gate fidelities are 99.94% (HPF) and 99.93% (LPF). Relative to the filter-free Purcell limit, the filters substantially extend the qubit lifetime, and the Purcell protection deepens at higher filter order. In addition, an intrinsic dissipation mode of the filter offers a qubit-reset channel. This leads to a compact architecture that unifies fast, high-fidelity readout, Purcell protection, and effective reset within a single filter for large-scale fault-tolerant quantum computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13644v1
- Title: Heuristic Lookahead Distillation Protocol Search
- Authors: Matthew Barber, Stefano Pirandola
- Categories: quant-ph (primary); quant-ph; cond-mat.other; math-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2608.13644v1  pdf=https://arxiv.org/pdf/2608.13644v1.pdf

Abstract:
Bipartite qubit entanglement distillation is the process of converting noisy ebits into pure ebits using only local operations and classical communication. This is a core operation for quantum repeaters, enabling such crucial tasks as long-distance quantum communication and distributed quantum computing. In this work, we introduce a method for searching for entanglement distillation protocols and, using this technique, distil qubit Werner states at a higher rate than could be achieved using previously discovered protocols. In particular, we demonstrate the advantage of our new distillation strategy by improving the best-known lower bound for the two-way-assisted quantum capacity of the qubit depolarising channel across a wide range of channel parameters, making progress in one of the long-standing problems of quantum information theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13649v1
- Title: Tracking real-space quantum state breathing through Floquet-projector geometry
- Authors: Arpit Raj, Johannes Mitscherling, Björn Trauzettel
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2608.13649v1  pdf=https://arxiv.org/pdf/2608.13649v1.pdf

Abstract:
Periodic driving of spatially periodic quantum systems generates band structures that are absent in static crystals. We present a quantum geometric theory to characterize the Floquet-Bloch states at stroboscopic times and during micromotion on equal footing. Our framework builds upon time-evolved Floquet projectors that connect static quantum geometry, micromotion-operator geometry, and Floquet topology. To illustrate the formalism, we introduce the Floquet-projector quantum metric, which we employ to characterize the real-space breathing of localized states in a driven chiral-symmetric integrable spin chain. The Floquet-projector quantum metric, integrated over the Brillouin zone, captures the oscillatory variance during micromotion and, at symmetry-selected times, is bounded below by Floquet topological invariants. We further describe how the Floquet projector geometry enables a systematic investigation of micromotion dynamics in periodically driven lattice systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13654v1
- Title: Entanglement Negativity in Noisy Quantum Volume Sampling
- Authors: Elijah Pelofske, Stephan Eidenbenz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13654v1  pdf=https://arxiv.org/pdf/2608.13654v1.pdf

Abstract:
The Quantum Volume protocol uses scrambling random circuits to benchmark NISQ computers. Quantum Volume is generally well-regarded as a benchmark for small, noisy, quantum computers because it requires the quantum computer to implement many non-local entangling gates within a square-shaped circuit, which incentivizes high qubit count, long qubit coherence times, and low error rates on all hardware gates. Quantum Volume circuits inherently produce high-entanglement states that are fragile to errors and decoherence. The Quantum Volume benchmark measures an observable called heavy-output-probability (HOP), where an HOP of $0.5$ corresponds to complete loss of coherence, and in the limit of system size an HOP $\approx 0.84$ for a fully coherent quantum processor. Here, we numerically study the tradeoff between depolarizing noise, entanglement as quantified by the bipartite negativity measure, and HOP in quantum volume circuits. Our results contextualize prior small scale quantum volume demonstrations on quantum computers and highlight that under depolarizing noise, due to finite system size effects heavy output probabilities can be greater than $0.5$ while the bipartite negativity entanglement has been destroyed. This implies, although improbable, that a NISQ computer could pass the Quantum Volume benchmark test threshold of $2/3$ while the underlying quantum computation has no global entanglement -- albeit only for small $n$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13664v1
- Title: Open system probes of renormalization group flow
- Authors: Andrew Keefe, Brenden Bowen, Saptarshi Biswas, Albion Lawrence, Nishant Agarwal, Archana Kamal
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2608.13664v1  pdf=https://arxiv.org/pdf/2608.13664v1.pdf

Abstract:
Open system probes can provide an efficient means to characterize quantum many-body systems by employing them as engineered environments. The key idea is to map long-range spatial correlations of the environment onto dynamical correlations in the evolution of a simple quantum probe. Using the example of a qubit coupled to a transverse-field Ising model, we show how the non-Markovian rate or spectral flow can be used to identify stable and unstable fixed points, infer scaling dimensions of relevant fields, and deduce the renormalization group flow induced by deformations around any fixed point.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13691v1
- Title: Efficient Hamiltonian Truncation: Fast Matrix Construction and Quantum Krylov Diagonalization
- Authors: Rachel Houtz, Marco Knipfer, Konstantin Matchev, Alexander Roman, Mia West
- Categories: quant-ph (primary); quant-ph; hep-lat; hep-ph; hep-th
- Links: abs=https://arxiv.org/abs/2608.13691v1  pdf=https://arxiv.org/pdf/2608.13691v1.pdf

Abstract:
Hamiltonian truncation offers a nonperturbative route to quantum field theory, yet its accuracy is limited by the rapid expansion of the truncated Hilbert space, which drives up computational cost. We tackle this bottleneck with a hybrid strategy that pairs classical and quantum algorithms: 1) we develop an efficient basis-generation scheme built on integer partitions; 2) we speed up the construction of the sparse Hamiltonian matrix using symmetry-aware algorithms; and 3) we explore quantum Krylov diagonalization as a route to the low-lying spectrum. Benchmarking against the free massive scalar and $φ^4$ theories in two spacetime dimensions, we achieve substantial gains in the computational efficiency of Hamiltonian truncation and chart a path toward future quantum implementations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13725v1
- Title: Scalable Test of Genuine Multipartite Entanglement via Partially Randomized Measurements
- Authors: Jan Wojcik, Pawel Chrabkowski, Wieslaw Laskowski
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13725v1  pdf=https://arxiv.org/pdf/2608.13725v1.pdf

Abstract:
Certifying genuine multipartite entanglement in quantum systems can require a number of measurements that grows exponentially with the system size. Here we introduce a criterion based on correlation-tensor subsector lengths restricted to local measurement planes and show that it can be evaluated using partially randomized measurements without an explicit exponential dependence on the number of qubits. We derive the corresponding bounds for $k$-separable states and illustrate the criterion using representative families of multipartite entangled states. Finally, we demonstrate the practical applicability of the method on an ion-trap quantum computer by certifying genuine five-partite entanglement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13744v1
- Title: Designing robust molecular spins for quantum technologies with theoretical chemistry
- Authors: Timothy J. Krogmeier, Pranay Venkatesh, Mikayla Z. Fahrenbruch, Anthony W. Schlimgen, Andres Montoya-Castillo, Kade Head-Marsden
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13744v1  pdf=https://arxiv.org/pdf/2608.13744v1.pdf

Abstract:
Molecular spins represent a versatile platform for quantum information science, with the potential to offer chemically tunable, addressable qubits. However, achieving this requires understanding and mitigating quantum decoherence. This Chapter provides a theoretical overview of current state-of-the-art chemical theory connecting ab initio electronic structure with open quantum system dynamics to guide the rational design of long-lived molecular qubits. Beginning at the electronic level, multi-reference and relativistic electronic structure methods to parameterize effective spin Hamiltonians are discussed, with a primary focus on accurately capturing $g$-tensors, zero-field splitting, and hyperfine interactions. These parameters feed into models of spin-phonon and spin-spin coupling to quantify $T_1$ and $T_2$ relaxation across various environmental regimes. This Chapter evaluates a hierarchy of dynamical methods, ranging from factorization to matrix product state approaches, balancing computational cost against accuracy and generalizability. Ultimately, mapping these theoretical models to molecular architecture can establish design principles, such as isotopic substitution and spatial spin delocalization, to understand and extend coherence lifetimes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13764v1
- Title: Certified coherent, informative, and non-entanglement-breaking fixed points of future-referential quantum feedback
- Authors: Eran Kopel
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2608.13764v1  pdf=https://arxiv.org/pdf/2608.13764v1.pdf

Abstract:
We study quantum processes in which information extracted from a forward simulation is returned as input to an earlier internal time of the simulated dynamics: externally the protocol is an ordinary causally ordered circuit, but internally it is future-referential. Contracting a process tensor with a leakage instrument and a controller induces a completely positive trace-preserving map on a message register, and we classify its fixed points by five operational properties: stability, informativeness, feedability, coherence, and preservation of quantum correlations. Four results separate notions that informal discussions of "information from the future" often conflate. A two-parameter unitary-dilation family yields a closed-form, globally attractive, coherent fixed point (Proposition 1), yet is entanglement breaking whenever future records are perfectly distinguishable (Lemma 1). Releasing that orthogonality, a four-parameter partial-swap family admits a nonempty open non-entanglement-breaking region (Proposition 2), with an explicit Choi partial-transpose neighborhood of half-width $0.0163π$ (Proposition 3). Combining outward-rounded interval enclosures with perturbation bounds tracking the channel and its stationary-state drift, we certify an explicit parameter square of half-width $0.0013π$ on which the feedback channel is simultaneously strictly contractive (margin $\ge 0.237$), coherent ($\ge 0.416$), informative about the designated future variable ($\ge 0.172$ bits), and non-entanglement-breaking (NPT margin $\ge 0.188$) (Proposition 4). Direct evaluation shows all four properties persisting over a region an order of magnitude larger, so the certified square is a proof of principle rather than a phase boundary. All enclosures and margins are confirmed by a machine-verified ball-arithmetic certificate, and the complete code and certificate accompany the paper.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13781v1
- Title: Entanglement asymmetry characterization of the Chiral Anomaly
- Authors: Alfred Benedito German Sierra
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13781v1  pdf=https://arxiv.org/pdf/2608.13781v1.pdf

Abstract:
Shao et al. recently showed that the 1+1D staggered fermion Hamiltonian admits a whole algebra of lattice operators that flow to the same axial charge in the thermodynamic limit (TL). On the lattice the principal axial charge does not commute with the vector charge, although their commutator is expected to vanish in the TL, providing a lattice realization of the chiral anomaly. We investigate the effect of this anomaly on the ground state(s) using the entanglement asymmetry. Unexpectedly, the asymmetry remains nonzero in the TL, despite the vanishing of the commutator, and exhibits a novel scaling behavior.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13805v1
- Title: Fast classical simulation of `Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor'
- Authors: Xiao-Yu Ouyang, Runze Chi, Garnet Kin-Lic Chan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13805v1  pdf=https://arxiv.org/pdf/2608.13805v1.pdf

Abstract:
We study the Néel quench dynamics of a 1D Fermi-Hubbard model which has recently been simulated on quantum hardware. We demonstrate that the set of 7260 observable trajectories measured in the quantum experiment can be obtained more quickly and accurately through classical tensor network simulation using modest computation. Our result relies on transverse tensor network contraction, where a bond dimension of 32 is already sufficient to reproduce the quantum experiment. We further extend the converged observable trajectories to longer times than in the hardware simulation and in other recent classical simulations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13862v1
- Title: Resource-efficient quantum eigenvalue transform with commutator scaling
- Authors: Arul Rhik Mazumder, James D. Watson, Samson Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13862v1  pdf=https://arxiv.org/pdf/2608.13862v1.pdf

Abstract:
We develop quantum algorithms for estimating properties of general matrix functions of Hermitian matrices, with applications to phase estimation, Green's function evaluation, and estimating measurement distributions of time-evolved states. The resulting methods exhibit commutator scaling in matrix parameters similar to that usually found for product formulae, lower circuit depth in other parameters, and require only a single ancillary qubit. Our central primitive consists of classically postprocessing randomly chosen product formulae circuits, which mathematically corresponds to an approximation of a Richardson extrapolation. Within our framework, we introduce a protocol for approximating the measurement distributions of quantum states, extending beyond standard observable estimation. We also provide tightened gate complexity bounds for practically relevant systems, including those with k-local interactions, long-tailed matrix ensembles, and conserved quantities. Finally, numerical experiments confirm that our method can achieve significantly shallower circuit depths than standard product formulae in certain parameter regimes, and highlight the potential of their heuristic application.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13881v1
- Title: Nonorthogonal-state erasure as the resource behind apparent second-law violations
- Authors: Xinshu Xia, Hui Hui Qin, Yu-Han Ma, Chang-Pu Sun, Hui Dong
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2608.13881v1  pdf=https://arxiv.org/pdf/2608.13881v1.pdf

Abstract:
Perfect deterministic distinguishing of nonorthogonal quantum states is forbidden by the linear and unitary structure of quantum mechanics. It has often been assumed that, if such distinguishing were available, it would be the resource enabling work extraction from a single heat bath. We show that this expectation identifies the wrong thermodynamic operation and prove such hypothetical operation increases, rather than decreases, the joint entropy of system and detector. The entropy-decreasing resource is instead the inverse operation, which we call nonorthogonal-state erasure. Reanalyzing a Peres-type Szilard engine, we show that the apparent extracted work $W_{\mathrm{ext}}=0.2766k_{\mathrm{B}}T$ for an equal mixture of an atomic ensemble with spin state $\left|\uparrow\right\rangle $ and $\left|\rightarrow\right\rangle $. Thus the apparent second-law violation is supplied not by nonorthogonal-state distinguishing, but by a nonorthogonal quantum state erasure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13894v1
- Title: de Broglie-Bohm Dynamics with Schrödinger Source Fields: A Framework for Subquantum Theory
- Authors: Said Mikki
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2608.13894v1  pdf=https://arxiv.org/pdf/2608.13894v1.pdf

Abstract:
We extend de Broglie--Bohm (dBB) pilot-wave theory by introducing a complex source field into the Schrödinger equation and examining its effects on quantum equilibrium and nonequilibrium dynamics. In dBB theory, the physical particle distribution P, rather than the Born density $|ψ|^2$, carries the ensemble probability, so a source term may modify the pilot wave without violating conservation of total particle probability. We derive the source-modified Hamilton--Jacobi and continuity equations, the transport equation for the nonequilibrium ratio $f=P/|ψ|^2$, and an exact entropy-production formula. Three applications follow. First, suitably designed sources can drive exponential relaxation toward quantum equilibrium. Second, the entropy-production rate admits a Prigogine-type bilinear form, providing a basis for a subquantum thermodynamics with entropy-producing and entropy-extracting regimes. Third, a tuned source can exactly cancel the Bohmian quantum potential, yielding classical particle trajectories while the guiding wave retains nontrivial structure and the nonequilibrium ratio remains conserved. The resulting framework provides a unified setting for studying source-driven quantum nonequilibrium, entropy exchange, and classicalization, and motivates further investigation of the physical and ontological status of the source field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13907v1
- Title: Robust Quantum Extremal Numbers
- Authors: Wanchen Zhang, Zicheng Han, Xiande Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13907v1  pdf=https://arxiv.org/pdf/2608.13907v1.pdf

Abstract:
Absolutely maximally entangled states require every reduction of at most half of the parties to be maximally mixed, a condition that is both rigid and often impossible for qubit systems. Previous work introduced the quantum extremal number, which maximizes the number of exactly maximally mixed half-body marginals, and determined the exact value Qex(8,4)=56. The present work develops a robust extension of this extremal problem. For a subsystem $A$, the marginal maximal-mixing defect is defined by \[ D_A=2^{|A|}\operatorname{Tr}(ρ_A^2)-1 =2^{|A|}\left\|ρ_A-\frac{I_A}{2^{|A|}}\right\|_2^2, \] and $Q_{\mathrm{ex},\varepsilon}^{D}(n,k)$ is defined as the maximum number of $k$-body marginals satisfying $D_A\leq\varepsilon$ in an $n$-qubit pure state. This counting problem differs from approximate $k$-uniformity, which requires all $k$-body marginals to obey a common error bound.   For pure states on $4m$ qubits, the following local stability inequality is established: \[ \sum_{i\in T}D_{T\setminus\{i\}}\geq1 \qquad (|T|=2m+1). \] It follows that, whenever $\varepsilon<1/(2m+1)$, the hypergraph of $\varepsilon$-good $2m$-subsets is $K_{2m+1}^{(2m)}$-free. Combined with the known exact eight-qubit construction, this yields the stability plateau \[ Q_{\mathrm{ex},\varepsilon}^{D}(8,4)=56, \qquad 0\leq\varepsilon<\frac15. \] For odd systems of $2k+1$ qubits, the exact forbidden hypergraph $H_k$ is used to derive explicit finite-error stability radii. In particular, $Q_{\mathrm{ex},\varepsilon}^{D}(9,4)\leq120$ for $0\leq\varepsilon<1/17$. These results turn exact quantum Turán obstructions into quantitative robustness statements and identify intervals on which quantum extremal numbers are stable under imperfect marginal mixedness.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13942v1
- Title: Maximizing Nonclassicality of Massive Objects via Quantum Zeno Effect
- Authors: Debarshi Das, Pritam Roy, Marko Toroš, Hendrik Ulbricht, Dipankar Home, Sougato Bose
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13942v1  pdf=https://arxiv.org/pdf/2608.13942v1.pdf

Abstract:
For testing quantum mechanics in the macroscopic domain, a major challenge is to devise effective means for enhancing the observable nonclassical signatures despite the ubiquitous presence of environmental decoherence. Toward this goal, we invoke the Quantum Zeno Effect (QZE) for achieving a tunable amplification of an inherently nonclassical quantum disturbance induced by any measurement. Such an enhancement of otherwise small and decoherence-suppressed nonclassicality can arise from the cumulative quantum disturbances generated by repetitive measurements, with the tunability of amplification controlled by the number of measurements. To evidence this, we formulate a testable loophole-free scheme using a massive oscillator, where the system preparation requires trapping and ground-state cooling of a massive object. The required measurements can be realized through a beam-splitter-type interaction between the mechanical oscillator and an optical field, followed by photon detection. Our analysis shows that such amplification, suitably quantified in terms of a testable witness, remains appreciably observable even in the realistic regimes of optomechanical damping, and for sufficiently large masses, thus enabling the demonstration of QZE in the macroscopic domain.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13975v1
- Title: Neural decoders for subsystem many-hypercube codes
- Authors: Ryota Nakai, Hayato Goto
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13975v1  pdf=https://arxiv.org/pdf/2608.13975v1.pdf

Abstract:
To maximize the potential of quantum error-correcting codes, it is essential to develop high-performance decoders. The subsystem many-hypercube (MHC) codes have been developed to achieve both high encoding rates and low-weight syndrome-measurements, but the introduction of gauge degrees of freedom makes decoding more challenging. In this work, we develop neural-network-based decoders for the subsystem MHC codes in a circuit-level noise model. We demonstrate that even the gauge-measurement information can be utilized for decoding by carefully arranging the syndrome-measurement sequence, improving the decoding performance. We further show that recurrent neural decoders outperform simple fully connected neural decoders, and can decode syndrome-measurement sequences longer than those used during training.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13997v1
- Title: Limits of independent and identical measurements for quantum illumination with an unknown return phase
- Authors: Ko Shiraiwa, Shingo Kukita
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.13997v1  pdf=https://arxiv.org/pdf/2608.13997v1.pdf

Abstract:
Quantum illumination exploits entanglement between a transmitted signal and a retained idler to improve the error-probability exponent of target detection by roughly a factor of four (6 dB) over that with a coherent state of the same transmitted energy. This advantage presumes a known return phase. In practice, the phase is set by the range to the target and the condition of its surface, and is difficult to know in advance. Whether the advantage survives when this phase is unknown is not obvious. Here, we cast target detection as a composite hypothesis test in which the return phase is an unknown constant common to all trials, and we restrict the receiver to independent and identical measurements on each copy. We bound the worst-case error exponent at low reflectivity for every such measurement and every input state of a single signal mode and an idler of any dimension. We then show that unentangled coherent light with heterodyne detection already saturates this bound, for every value of the phase. Entanglement therefore confers no advantage in this setting. The class of independent and identical measurements contains many implementable quantum-illumination receivers, including the optical parametric amplifier and phase-conjugate receivers. Our result shows that none of them can offer a quantum advantage in the worst case over the phase, to leading order in the reflectivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14002v1
- Title: Circuit Depth Compression via Spectral Gap Amplification in Quantum Phase Estimation
- Authors: Sk Mujaffar Hossain, Satadeep Bhattacharjee
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2608.14002v1  pdf=https://arxiv.org/pdf/2608.14002v1.pdf

Abstract:
We show that quantum phase estimation (QPE) circuits can be significantly compressed in depth by preprocessing the input operator with a sigmoid spectral filter before estimation. For systems with small spectral gaps Delta_lambda, standard QPE requires m = ceil(log2(1/Delta_lambda)) precision qubits and depth Theta(2^m). Applying a soft-step transformation f(lambda; tau,w) amplifies the effective gap to Delta_f > Delta_lambda (for w < 1/4), reducing the required precision to m_f = ceil(log2(1/Delta_f)) and compressing circuit depth by 2^(alpha Delta_m), where alpha = 1 for the LMR density-matrix exponentiation framework and alpha is in [0.11,0.42] for controlled-phase-gate circuits. We prove that this compression is exact, bounded above by log2(1/(4w Delta_lambda)) + 1, and impossible for exactly degenerate spectra. We further show that the threshold parameter tau requires only O(w) accuracy, so classical preprocessing such as covariance diagonalisation or CASSCF avoids circularity. A net resource advantage occurs when 4w^2(2^Delta_m - 1) > Delta_lambda log(1/epsilon). Validation on LiH and BeH2 bond-stretch calculations, classical covariance datasets, and synthetic near-degenerate cases demonstrates depth reductions of up to 27x and CX-gate reductions of up to 21x. For LiH, QPE output fidelity improves from 0.66 to 0.98 at a 1% hardware error rate. The method preserves the principal subspace to machine precision, requires no modification of QPE, and can be combined with readout-stage and state-preparation filtering. Negative-control tests establish the benefit condition: m_raw >= 2 and Delta_lambda > 0.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14041v1
- Title: Non-Abelian geometry and globally inequivalent symmetry reductions of the cylindrical Dirac doublet
- Authors: Zhongze Guo, Bei Xu, Qiang Gu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14041v1  pdf=https://arxiv.org/pdf/2608.14041v1.pdf

Abstract:
Different exact cylindrical Dirac constructions are locally related within the same two-dimensional positive-energy sector, suggesting that they might be merely alternative choices of basis. We show that this equivalence can fail globally. Treating the cylindrical Dirac doublet as a rank-two bundle over momentum space, we identify transverse helicity, a mass-dressed transverse integral, and helicity as distinct symmetry-selected rank-one reductions, whose normalized restrictions organize the internal doublet through a Pauli algebra. The positive-energy Dirac $SU(2)$ connection Abelianizes exactly on fixed-azimuth meridians in the transverse-helicity basis, while its full three-dimensional curvature remains genuinely non-Abelian for nonzero mass. We derive the corresponding azimuthal Wilson-loop spectrum in closed form. The three reductions then display sharply different global structures: the transverse-helicity splitting terminates on the momentum axis, the mass-dressed splitting extends smoothly and is Chern trivial for $m>0$, whereas helicity defines line bundles with opposite unit Chern numbers. Thus a single Dirac doublet admits symmetry resolutions that are locally equivalent but globally inequivalent.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14083v1
- Title: Information-Calibrated Quantum Diffusion: Aligning Forward Noise with Reverse Recoverability
- Authors: Qipeng Qian, Yuntao Qian
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14083v1  pdf=https://arxiv.org/pdf/2608.14083v1.pdf

Abstract:
Quantum diffusion models typically parameterize forward corruption by raw channel strength, even though equal parameter increments need not erase equal information or induce comparable inverse problems. We introduce the classical--quantum information decrement $Δ_t=I(X{:}Q_{t-1})-I(X{:}Q_t)$ as an intrinsic diffusion coordinate for labeled quantum ensembles. Along depolarization, equalizing $Δ_t$ yields the unique minimax discretization of the forward path, while universal recoverability gives the same quantity an operational reverse interpretation as an attainable expected log-fidelity budget for a label-independent CPTP recovery channel. Complementary continuity and pairwise-geometric converses lower-bound the optimal common-channel recovery error. We further show that local calibration is fundamentally insufficient for stochastic generation: even in a fixed noncommuting two-qubit system, identical local-fidelity laws and budget-feasible risks can coexist with macroscopically different output distributions. This motivates a stochastic learner combining theorem-scaled recovery constraints with distribution matching, for which we establish finite-sample calibration and compositional trace-Wasserstein control. On four-qubit TFIM, a controlled capacity extension reduces endpoint $\Wtr$ from $.622$ to $.424$ on all ten matched seeds and achieves lower $\Wtr$ than official QuDDPM ($.498$) with fewer trainable parameters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14110v1
- Title: Entanglement certification via causal-order interferometry in a quantum switch
- Authors: Haojie Wang, Shuheng Liu, Qiongyi He
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14110v1  pdf=https://arxiv.org/pdf/2608.14110v1.pdf

Abstract:
Entanglement certification is often performed on states that have already undergone noisy transmission or processing. Noise can reduce the surviving entanglement and can also cause a given criterion to fail even when entanglement remains. In this context, the quantum switch, a paradigmatic realization of indefinite causal order (ICO), coherently controls the orders in which two channels act and has been shown to offer advantages across a range of quantum information-processing tasks. Here we ask whether this coherent control enlarges the noise-parameter region in which entanglement remains certifiable. We regard the two order branches as the arms of a causal-order interferometer and insert a local unitary between the channel uses to tune their interference. For stochastic Pauli noise, a postselected ICO output can exhibit greater entanglement negativity than any classical mixture of the two definite orders; in particular, we identify regimes where its negativity remains nonzero while that of every classical mixture vanishes. A suitable local Pauli unitary substantially enlarges this ICO-only region, while an input-dependent path-difference indicator qualitatively links operator noncommutativity to the postselected negativity gain. Numerical examples extend the advantage to local amplitude-damping noise and two-qutrit Weyl noise. At a representative Weyl-noise point for the $3\times 3$ positive-partial-transpose (PPT) Tiles bound-entangled state, a nondecomposable witness detects the postselected ICO output, whereas an analytic bound excludes detection of the definite-order outputs and their mixtures by the entire locally rotated witness family. These results identify causal-order interferometry as a strategy for enhancing entanglement certification across distinct noise models and dimensions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14133v1
- Title: A groupoidal approach to quantum reference frames
- Authors: Samuel Fedida, Alberto Ibort, Arnau Mas-Dorca
- Categories: quant-ph (primary); quant-ph; hep-th; math-ph
- Links: abs=https://arxiv.org/abs/2608.14133v1  pdf=https://arxiv.org/pdf/2608.14133v1.pdf

Abstract:
We develop the kinematical and operator-algebraic foundations of a groupoid-based relational quantum field theory (RQFT) on curved spacetimes. Indeed, the usual group-based quantum reference frame (QRF) formalism is not directly suited to generic curved Lorentzian backgrounds as global symmetry groups are typically absent or too small. We formulate a notion of QRF for a continuous groupoid. This yields a groupoid relativization map and relational observables. We show that a localization limit recovers the ordinary non-relational description. We construct canonical sharp groupoid QRFs, which form the groupoidal counterpart of the ideal group QRFs based on $L^2(G)$. We further prove that the groupoid QRF construction reduces to the standard operational QRF formalism for locally compact groups. The action groupoid QRFs are torsor QRFs only for specific classes of fields of positive operator-valued measures (POVMs), and the torsor relativization map only applies to constant operator fields of system observables.   We review the foundations of RQFT in Minkowski spacetime. We prove new results that further link RQFT to Wightman QFT. We show that covariant POVMs are $μ$-continuous with respect to quasi-invariant $σ$-finite positive Borel measures $μ$. Thus, relational quantum fields can be understood as the smearing of pointwise-defined kernels with respect to the QRF's statistics. We develop RQFT in curved spacetime, where we argue that the correct replacement for the Poincaré group is the Poincaré groupoid of the spacetime. We also indicate how the framework extends further to internal gauge symmetry and relational gauge-covariant quantum field theory via Atiyah groupoids, providing a first step towards formulating a relational quantum Yang-Mills field theory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14134v1
- Title: Photonic Quantum Computing vs. Classical Solvers in Constrained Factor Portfolio Optimization
- Authors: Nirvik Sahoo, Chyng Wen Tee, Paul Robert Griffin
- Categories: quant-ph (primary); quant-ph; q-fin.PM
- Links: abs=https://arxiv.org/abs/2608.14134v1  pdf=https://arxiv.org/pdf/2608.14134v1.pdf

Abstract:
The authors present a rigorous empirical evaluation of three distinct optimization paradigms for institutional factor portfolio construction: an entropy-based photonic quantum annealer (Dirac-3, Quantum Computing Inc.), a commercial mixed-integer programming solver (Gurobi), and a model-free deep reinforcement learning agent (SAC). Evaluating these pipelines on the Jensen-Kelly-Pedersen 13-factor equity library across 164 months test window, we implement a full factorial penalty sweep comprising 48 hyperparameter configurations that govern return, volatility, and skewness trade-offs. Our findings demonstrate that while photonic hardware can locate superior risk-return topologies within a narrow operating range, classical mixed-integer programming remains superior for risk-constrained mandates requiring tight tail-risk control and cross-seed stability. Furthermore, we document structural failure modes in reinforcement learning factor allocators under unanchored higher-moment shaping. We translate these empirical results into actionable, mandate-specific guidelines for quantitative portfolio managers deploying advanced optimization engines.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14169v1
- Title: Classical Limits of Spectral Filtering in Quantum Generative Models
- Authors: Marco Roth
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2608.14169v1  pdf=https://arxiv.org/pdf/2608.14169v1.pdf

Abstract:
Spectral filtering has been proposed as a route to regularization in quantum generative models: the quantum Fourier transform exposes the amplitude spectrum of a quantum circuit Born machine, and a diagonal filter suppresses the high frequencies associated with finite-sample noise, an operation whose classical counterpart seemingly requires manipulating an exponentially long amplitude vector. We examine whether this coherent operation produces anything that classical post-processing of samples from the unfiltered model cannot match. Measuring the filter against convolution with a symmetric probability kernel at matched sampling cost, which accounts for the post-selection overhead of attenuation, we derive necessary and sufficient conditions for the gap between the two to vanish. Magnitude (attenuating) filters obey a dichotomy: at a fixed affordability threshold, the filtered output is either a constant-size Fourier object with an efficient classical sampler, or the passband must widen until no fixed frequency is attenuated and the filter no longer smooths. In neither case does the filter create a quantum-classical separation. Whatever separation survives is inherited from the spectral phase of the input state. Numerical experiments on trained circuit Born machines confirm the classification and show that the deciding phases are invisible to the Born-rule training loss and set by the initialization. Within the diagonal family, pure phase filters remain the only spectral operations exempt from these constraints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14181v1
- Title: The Organization of Environmental Coupling Shapes What Quantum Reservoirs Remember
- Authors: Markus Baumann, Itamar Fink, Johannes Wittmann, Claudia Linnhoff-Popien, Jonas Stein
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14181v1  pdf=https://arxiv.org/pdf/2608.14181v1.pdf

Abstract:
For an open quantum reservoir, how the system forgets is part of how it computes. Quantum reservoir computing processes input streams with fixed quantum dynamics and trains only a linear readout. Dissipation can make old inputs fade, but prior studies commonly fix the environmental process and tune only its strength. Here we show numerically that the coupling pattern, meaning whether transitions connect to separate or shared environmental channels, changes which parts of the input history remain accessible. Paired simulations of finite spin reservoirs keep the Hamiltonian, inputs, measurements, and readout fixed. The tested patterns produce distinct task profiles, with no universal winner. Shared relaxation preserves more recent input history than independent local loss, and the retained memory changes when the qubits contribute with different relative phases to the shared decay channel. This ordering recurs across system sizes, Hamiltonians, input protocols, and targeted controls. Environmental coupling is therefore more than a damping parameter: it is a design layer that shapes not only how quickly information fades, but which input history remains available for computation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14199v1
- Title: Local geometry for Schmidt number witnesses
- Authors: Young-Hoon Kiem, Seung-Hyeok Kye
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14199v1  pdf=https://arxiv.org/pdf/2608.14199v1.pdf

Abstract:
Suppose that $F_E$ is the face of the convex set of all $m\otimes n$ bi-partite states which consists of states with ranges contained in a subspace $E$. For generic subspaces $E$ with a specific dimension, we use the result in [Phys. Rev. A 112 (2025), 032426] to see that there exists a number $κ$, depending only on the dimension of $E$, such that there exist Schmidt number $\ell$ witnesses outside of $F_{E^\perp}$ if and only if $\ell\leκ$. In this generic case, we show in this paper that there exist Schmidt number $\ell$ witnesses for $\ell>κ$ around the projection states located at the center of $F_{E^\perp}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14206v1
- Title: Synthesizing In-Bulk Topological Corner States via Giant Atoms
- Authors: Zhao-Min Gao, Xin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14206v1  pdf=https://arxiv.org/pdf/2608.14206v1.pdf

Abstract:
Corner states in higher-order topological insulators are typically confined to geometric corners, limiting their flexibility for scalable quantum information processing. We propose a scheme to synthesize topological corner states at arbitrary positions within the bulk of a two-dimensional Su-Schrieffer-Heeger (SSH) lattice by coupling it to giant atoms. By engineering an L-shaped multi-point coupling that satisfies the vacancy-like dressed state (VDS) condition, where the photonic wavefunction vanishes at the coupling sites to form an artificial bulk boundary, we derive the conditions for synthesizing a zero-energy corner state at any target position. We demonstrate that the engineered corner state exhibits high fidelity and spatial localization, remaining robust against realistic disorder. Extending to multi-atom networks, we realize a versatile quantum switch via a giant superatom, enabling multi-channel control over 0D corner states and 1D edge states through the dual-resonance condition. Furthermore, we demonstrate the coherent interactions between two giant atoms mediated by VDS-engineered corner states. Governed by a sublattice selection rule, the coupling activates exclusively in intersecting configurations and decays exponentially with distance. Our work establishes a highly reconfigurable platform for embedding topological boundary modes within the bulk, offering a robust pathway for scalable topological quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14208v1
- Title: Foundation Neural Effective Hamiltonian for Strongly Correlated Quantum Materials
- Authors: Lixing Zhang, Hongjie Jiang, Di Luo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14208v1  pdf=https://arxiv.org/pdf/2608.14208v1.pdf

Abstract:
Simulating strongly correlated quantum materials often involves not a single Hamiltonian, but a family of Hamiltonians whose ground states evolve across experimentally tunable couplings. Foundation neural quantum states (FNQS) offer a promising route to amortizing many-body calculations across such families, but can lose accuracy near phase transitions and still incur non-negligible sampling costs that grow with the number of target couplings. We introduce the Foundation Neural Effective Hamiltonian (FNEH), which projects a Hamiltonian family onto a compact subspace spanned by FNQS sampled at selected couplings. By variationally combining FNQS across parameter space, FNEH systematically improves their ground-state approximation and can recover phase boundaries that the foundation model misidentifies. Once the required operator matrix elements are sampled, FNEH enables sweeps over couplings, observables, and phase boundaries at a cost governed by the small effective-Hamiltonian dimension, without repeated neural-network sampling at every target coupling. We demonstrate FNEH in strongly correlated moiré materials, where it accurately resolves competing phases, enables high-resolution multidimensional phase scans, and substantially reduces the computational cost of exploring many target Hamiltonians. The results open a new avenue for studying strongly correlated quantum materials with foundation models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14214v1
- Title: Exchange-only qubit stabilized by a single-spin qubit
- Authors: Irina Heinz, Mira Sharma, Joris Kattemölle
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2608.14214v1  pdf=https://arxiv.org/pdf/2608.14214v1.pdf

Abstract:
Hybrid approaches that combine different spin qubit encodings offer promising advantages. In particular, the additional degrees of freedom available in exchange-only qubits and their extensions enable enhanced spin lifetimes and facilitate error detection through the use of auxiliary spins. We show that integrating Loss-DiVincenzo with exchange-only qubits provides a practical route to realizing these benefits while remaining compatible with spin-shuttling architectures. We further demonstrate how the singlet-only exchange-only qubit can be employed for error detection, and we present a fault-tolerant $π$-rotation about each of the three control axes of the (singlet-only) exchange-only qubit. By enabling error detection at the lowest encoding level, our approach effectively converts charge and nuclear noise into erasures, thereby suppressing error propagation and potentially enhancing the performance of quantum error-correction schemes. More broadly, our work establishes a new perspective on the singlet-only exchange-only qubit as a logical encoding, opening the door to fault-tolerant gate constructions and spin-tailored quantum error-correction protocols for semiconductor-based quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14263v1
- Title: SymQuPS: Symbolic Quantum Phase Space Algebra in Python
- Authors: Hendry M. Lim, Donny Dwiputra, Ahmad R. T. Nugraha
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2608.14263v1  pdf=https://arxiv.org/pdf/2608.14263v1.pdf

Abstract:
We present \texttt{SymQuPS}, a SymPy-based algebra system in Python mainly aimed toward the phase space representation of quantum mechanics within the Cahill-Glauber formalism (including the Glauber-Sudarshan $P$, Wigner, and Husimi $Q$ representations). By extension, the package serves as an algebraic venue for canonical quantization. A key feature is the phase space representation of an arbitrary Lindblad master equation, which gives the phase space equation of motion of the quantum system. We describe the core functionalities of the package, consisting of $s$-ordered operators, the star products, and the phase space representation. Some examples of use are given to illustrate the application of the package, and the package's performance in typical use cases is discussed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14285v1
- Title: Qu-Trefoil: Large-Scale Quantum Circuit Simulator Working on FPGA With SATA Storages
- Authors: Kaijie Wei, Hideharu Amano, Ryohei Niwase, Yoshiki Yamaguchi, Takefumi Miyoshi
- Categories: quant-ph (primary); quant-ph; cs.AR
- Links: abs=https://arxiv.org/abs/2608.14285v1  pdf=https://arxiv.org/pdf/2608.14285v1.pdf

Abstract:
Quantum circuits are fundamental components of quantum computing, and state-vector-based quantum circuit simulation is a widely used technique for tracking qubit behavior throughout circuit evolution. However, simulating a circuit with $n$ qubits requires $2^{n+4}$ bytes of memory, making simulations of more than 40 qubits feasible only on supercomputers. To address this limitation, we propose the Qu-Trefoil, a system designed for large-scale quantum circuit simulations on an FPGA-based platform called Trefoil. Trefoil is a multi-FPGA system connected to eight storage subsystems, each equipped with 32 SATA disks. Qu-Trefoil integrates a suite of HLS-based universal quantum gates, including Clifford gates (Hadamard (H), Pauli-Z (Z), Phase (S), Controlled-NOT (CNOT)), the T gate, and unitary matrix computation, along with HDL-designed modules for system-wide integration. Our extensive evaluation demonstrates the system's robustness and flexibility, covering quantum gate performance, chunk size, disk extensibility, and efficiency across different SATA generations. We successfully simulated quantum circuits with over 43 qubits, which required more than 128 TB of memory, in approximately 3.72 to 13.06 hours on a single storage subsystem equipped with one FPGA. This achievement represents a significant milestone in the advancement of quantum computing simulations. Furthermore, thanks to its unique architecture, Qu-Trefoil is more accessible, flexible, and cost-efficient than other existing simulators for large-scale quantum circuit simulations, making it a viable option for researchers with limited access to supercomputers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14325v1
- Title: Krylov complexity and Berry phase in quantum adiabatic dynamics
- Authors: Han-Qi Zheng, Peng-Zhang He, Lei-Hua Liu, Hai-Qing Zhang
- Categories: quant-ph (primary); quant-ph; cond-mat.other; hep-th
- Links: abs=https://arxiv.org/abs/2608.14325v1  pdf=https://arxiv.org/pdf/2608.14325v1.pdf

Abstract:
The connection between Krylov complexity and Berry phase in adiabatic dynamics is investigated under the instantaneous eigenstate basis of a slowly evolving spin system. Adiabatic dynamics force the Krylov complexity to vanish if the initial Krylov basis is an instantaneous eigenstate of the Hamiltonian. Nevertheless, we demonstrate that the Krylov complexity will be nonvanishing if the initial Krylov basis is a superposition state rather than an eigenstate. Time evolution of Krylov complexity will behave periodically or quasi-periodically depending on the controlling parameters. In particular, for a single qubit system with constant parameters, the Krylov complexity will oscillate harmonically in time with the frequency relevant to the combination of the strength of the external field and the geometric Berry phase.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14327v1
- Title: Quantum Snapshots Reveal a Compact Conformal Boundary Mode
- Authors: M. A. Rajabpour
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2608.14327v1  pdf=https://arxiv.org/pdf/2608.14327v1.pdf

Abstract:
A projective measurement of a many-body state produces a microscopic snapshot, usually viewed as random classical data. We show that partial occupation snapshots of the critical XX chain contain a universal angle with a precise conformal meaning. Dividing the ring into two measured and two unmeasured arcs, we assign geometry-dependent conformal side weights to the observed occupations and obtain a compact variable $δ_L$. At every finite size, $δ_L$ is fixed by the measured sites alone; the particular complete-configuration lift $X_L$ used in the proof additionally depends on unobserved particles. This angle is an exact microscopic compact coordinate whose scaling-limit law is that of the relative Dirichlet phase of the associated conformal quadrilateral---the boundary coordinate conjugate to charge in continuum post-measurement descriptions. Exact free-fermion determinants yield all of its Fourier moments. We prove that the lift becomes Gaussian with variance $2h(ζ)$, where $h(ζ)$ is the rectangle modulus, and hence $\langle e^{\ii qδ_L}\rangle\to e^{-h(ζ)q^2}$. Thus raw quantum snapshots realize the heat kernel on a circle and provide an outcome-level microscopic foundation for the compact zero-mode sector of Born averages over fluctuating conformal boundary conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14331v1
- Title: Equivalence Between Average-Case Hardness of Learning and Cryptography for Mixed Quantum States
- Authors: Alexandru Cojocaru, Laura Lewis
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2608.14331v1  pdf=https://arxiv.org/pdf/2608.14331v1.pdf

Abstract:
The relationship between cryptography and learning theory has long been a central theme in the foundations of theoretical computer science: cryptographic primitives can imply hardness of learning, while hardness of learning can in turn be used to construct cryptographic schemes. Recent works have begun exploring analogous connections in the quantum setting, relating the average-case hardness of learning quantum states (AHL) to cryptographic primitives such as one-way state generators (OWSG). Despite recent progress exploring this for pure states, the relationship for mixed states has remained an open question.   In this work, we prove that the existence of AHL for mixed quantum states is equivalent to the existence of inefficiently verifiable one-way state generators (IV-OWSGs). As a consequence, this relates mixed-state AHL to EFI pairs. Moreover, as a corollary of existing results, we obtain a separation between IV-OWSGs and OWSGs relative to the SWAP oracle.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14343v1
- Title: Analytical Theory of Higher-Order Collective Spin Interactions in Cavity Quantum Electrodynamics
- Authors: Leilani Ainsworth, Chase Gomes, Joseph Prescott, Kaley Wilcox, Jack Sullivan, Esteban Teran, Manav Bilakhia, Simone Colombo
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2608.14343v1  pdf=https://arxiv.org/pdf/2608.14343v1.pdf

Abstract:
Cavity-mediated collective-spin interactions are commonly described by a quadratic one-axis twisting Hamiltonian. However, the underlying atom-light interaction naturally generates nonlinearities to arbitrary order. Here, we derive a closed-form analytical expression for the complete hierarchy of cavity-mediated collective-spin interactions. We show that the nonlinear coefficients $χ_k$ are governed by Chebyshev polynomials, with $k$ the order of nonlinearity. This yields a universal scaling $χ_k\proptoη^k$ with the single-atom cooperativity $η$ and a description of their dependence on cavity detuning. The result provides a systematic framework for determining when higher-order nonlinearities become relevant and when the quadratic approximation breaks down. We identify experimentally relevant regimes in which higher-order terms substantially modify collective-spin dynamics, accelerating the generation of quantum correlations and quantum Fisher information, and demonstrate that finite-order expansions can accurately reproduce the full cavity-mediated evolution. Our results establish a general framework for understanding higher-order nonlinearities in cavity quantum electrodynamics and their role in collective entanglement and quantum-enhanced sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14357v1
- Title: Native multi-qubit gates on a single-junction unimon circuit
- Authors: Sasu Tuohino, Mikko Möttönen, Matti Silveri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14357v1  pdf=https://arxiv.org/pdf/2608.14357v1.pdf

Abstract:
Quantum processors with native multi-qubit gates may offer very efficient implementations of near-term quantum algorithms on noisy hardware. Here, we introduce the multiunimon, a superconducting multimode circuit that encodes multiple qubits and enables native multi-qubit gates in a device consisting of a single Josephson junction embedded in a coplanar waveguide structure. Closely related to the unimon qubit, it inherits properties such as high anharmonicity, full protection against low-frequency charge noise, and partial protection against flux noise. By designing such a three-qubit device with Josephson-to-inductive energy ratio above unity and using a leakage-aware encoding scheme for the computational states, we simulate all twelve different controlled-controlled-NOT gates with a mean fidelity of 99.5% with simple sine-squared pulses of comparable length to single-qubit gates. The performance is limited by incoherent errors dominated by dielectric loss. With improvements in noise protection, design, and pulse shaping, the simulations suggest that fidelities approaching 99.99% are within reach. Our results demonstrate the potential of the multiunimon as a highly connected multi-qubit unit for larger superconducting quantum processors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14387v1
- Title: Linearised quantum signal processing
- Authors: Marek Arsenault, Hlér Kristjánsson
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14387v1  pdf=https://arxiv.org/pdf/2608.14387v1.pdf

Abstract:
Quantum functional programming has been developed through two distinct paradigms in the last few years: Quantum Signal Processing (QSP)-based methods, including the Quantum Singular Value Transformation (QSVT), and methods based on higher-order quantum transformations, such as the Universal Hamiltonian Eigenvalue Transformation (UHET). While UHET performs functional transformations of Hamiltonian dynamics, its relationship to QSP-based techniques has remained unclear despite evident structural similarities. In this work, we resolve this gap by establishing a connection between UHET and QSP-based frameworks; specifically, we show that UHET can be interpreted as a (randomised) linearisation of Generalised QSP (GQSP). Building on this result, we introduce a linearised variant of (Hamiltonian-based) QSVT, which we call Universal Hamiltonian Singular Value Transformation (UHSVT), that enables the efficient transformation of the singular values of any arbitrary matrix $A$ encoded in a block of a Hamiltonian, whose dynamics is accessible as a black box, by any sufficiently differentiable complex-valued function $f$. Our algorithm requires the sole condition that $f$ vanishes at the origin, in contrast to previous QSVT-based approaches that assumed either a lower bound on the singular values of $A$ or the ability to perform $X$-rotation gates on the induced two-dimensional 'qubitised' subspace.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14468v1
- Title: To $\mathcal{PT}$ or not to $\mathcal{PT}$: Noise-induced escape and nonlinear-damping stabilization in a parity-time dimer
- Authors: Richelle Jade L. Tuquero, Kilian Seibold, Oded Zilberberg
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14468v1  pdf=https://arxiv.org/pdf/2608.14468v1.pdf

Abstract:
Parity-time ($\mathcal{PT}$) symmetric systems exhibit long-lived excitations by balancing gain and loss in coupled resonators, driving extensive theoretical interest and diverse experimental realizations. Realistic physical implementations, however, inevitably introduce nonlinearities and noise. This mandates a rigorous reevaluation of their global long-time dynamics. In this work, we show that Hamiltonian Duffing nonlinearity restricts the $\mathcal{PT}$-unbroken phase to a finite, nonattracting region of phase space. Consequently, unavoidable fluctuations drive first-passage escape into runaway trajectories. This renders the linearly $\mathcal{PT}$-unbroken phase a purely transient phenomenon. We then recover global stochastic stability by introducing two-photon loss on the gain oscillator. This nonlinear damping explicitly breaks exact $\mathcal{PT}$ symmetry while supplying genuine phase-space attraction, generating a bistable regime where a low-amplitude orbit mimicking the original linear state coexists with a high-amplitude limit cycle. Thus, we establish a revised origin for stability in non-Hermitian experiments: the observed long-time stochastic stability is governed by inherent restoring dissipation rather than the spectral $\mathcal{PT}$ symmetry itself.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14469v1
- Title: Current fluctuations in a non-additive open quantum system: breakdown of the quantum-jump approach
- Authors: Ilia Khomchenko, Saulo V. Moreira, Emanuel Schwarzhans, Mark T. Mitchison, Tony J. G. Apollaro
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14469v1  pdf=https://arxiv.org/pdf/2608.14469v1.pdf

Abstract:
Open quantum system dynamics is efficiently described by the quantum master equation formalism. Therein, quantum master equations in Lindblad form constitute an important subclass describing Markovian dynamics. When an open quantum system is in an out-of-equilibrium state, an exchange of particles between the open system and reservoirs takes place yielding to a non-zero average net current and associated current fluctuations, which can be characterised with the quantum jump formalism for quantum master equations expressed in Lindblad form. However, a large class of quantum master equations cannot be described by Lindblad dynamics. Here we assess the validity and the effectiveness of the quantum jump formalism when the dissipators in the quantum master equation describe a non-additive, open quantum system dynamics. We find that an additive unravelling of the non-additive quantum master equation does not generate a completely-positive dynamics in the scenario of perfect jump detection. Nevertheless, allowing for an imperfect jump detection scenario, we find that an additive unravelling is possible that reproduces the current and the fluctuations obtained via the Landauer-Büttiker formalism.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14493v1
- Title: Measurement-Feedback Quantum Information Engine: Coherence-Transition Interference and Correlated Work Statistics
- Authors: Yingying Hong, Dehua Liu, Jinfeng Wei, Leilei Yan, Jianhui Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.14493v1  pdf=https://arxiv.org/pdf/2608.14493v1.pdf

Abstract:
Measurement and feedback jointly prepare coherence and select finite-time dynamics in quantum information engines. Complementing a companion experimental realization, we develop a mechanism-resolved theory of the resulting work statistics and temporal correlations. The con?ditional work separates into population transfer and a phase-sensitive coherence-transition inter?ference term. Symmetric full counting statistics maps this interference to an equal-and-opposite half-quantum pair in the work quasiprobability, entering odd moments while leaving even moments fixed by endpoint mixing. An outcome-resolved tilted kernel then propagates these statistics through the correlated measurement record, yielding finite-cycle and fixed-time fluctuation corrections. The same memory reduces the reversible record-reset cost from the one-symbol entropy to the entropy rate. Our results link coherent work statistics, feedback memory, and information thermodynamics

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13646v1
- Title: Dual-species alkali and alkaline-earth-like optical tweezer arrays via interferometrically aligned high-NA objectives
- Authors: K. Weber, M. McMaster, M. Anderson, J. Tu, S. E. Eustice, N. A. Schine, I. B. Spielman, J. V. Porto, et al.
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13646v1  pdf=https://arxiv.org/pdf/2608.13646v1.pdf

Abstract:
We have developed a dual-species optical tweezer array apparatus combining $^{87}\text{Rb}$ and $^{174}\text{Yb}$ atoms with a permanent hybrid Twyman-Green--Fizeau interferometer, which provides precision co-alignment of two opposing 0.6-numerical aperture (NA) objectives and the high NA beams that pass through the system. This technique is extensible to other tweezer platforms operating at high numerical aperture across widely-separated wavelengths. Here we present simultaneous trapping and single-site resolved imaging of both species in co-aligned tweezer arrays with $^{87}\text{Rb}$ confined at $840\ \rm{nm}$ and $^{174}\text{Yb}$ at $532\ \rm{nm}$. The platform provides a foundation for hybrid quantum register operation, including mid-circuit measurements and asymmetric intra- and inter-species interactions, greatly expanding the capabilities of neutral atom arrays.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13686v1
- Title: Strong-field Herman-Kluk propagator method for high-harmonic generation in molecules
- Authors: Phi-Hung Tran, Hao Quan Truong, R. Esteban Goetz, Anh-Thu Le
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13686v1  pdf=https://arxiv.org/pdf/2608.13686v1.pdf

Abstract:
We extend our recently developed semiclassical strong-field Herman-Kluk (SFHK) propagator method to calculate high-order harmonic generation (HHG) in diatomic molecules driven by few-cycle intense laser fields. On the example of applications to H2 and N2, we show that our method, based on a combination of the Herman-Kluk propagator and the strong-field approximation, can provide very accurate results for both HHG yield and phase, nearly identical to those from the exact numerical solutions of the time-dependent Schrodinger equation. To compare with experimental measurements, averaging over molecular orientations must be performed. Here we demonstrate a distinct and powerful advantage of the SFHK, as its Monte Carlo sampling for the integration over the alignment distribution can be efficiently combined with the integration over the initial momentum distributions of electron wave-packet right after the tunnel exit. Therefore, the total number of trajectories used for the alignment-averaged HHG spectrum does not increase much compared to that for a single fixed alignment. Similar to atomic targets, the main computational task in the SFHK is to solve the classical Hamiltonian equations for the active electron in the combined electron-target ion potential and electron-laser interaction. The motion of the center of each electron wave packet in the continuum, represented by a coherent state, is governed by an independent classical trajectory so that the computation can be parallelized very efficiently.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13750v1
- Title: Choi--Jamiołkowski-type isomorphisms for von Neumann algebras
- Authors: Marcin Marciniak, Michał Cholewiak
- Categories: math.OA (primary); math.OA; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13750v1  pdf=https://arxiv.org/pdf/2608.13750v1.pdf

Abstract:
The Choi--Jamiołkowski isomorphism identifies completely positive maps with bipartite states and underlies much of finite-dimensional quantum information theory. For systems with infinitely many degrees of freedom, modelled by von Neumann algebras of type III, neither traces nor density matrices are available, and the isomorphism has to be reformulated. We show that for arbitrary von Neumann algebras $\mathcal{M}$ and $\mathcal{N}$ there is a canonical order isomorphism between the space of normal completely bounded maps from $\mathcal{M}$ into the predual of $\mathcal{N}$ and the predual of the spatial tensor product of $\mathcal{M}$ with the \emph{opposite} algebra of $\mathcal{N}$; under this identification complete positivity corresponds to positivity. Replacing the opposite algebra by $\mathcal{N}$ itself requires an anti-isomorphism of $\mathcal{N}$ with itself, and we prove that this condition is not only sufficient but also necessary, provided the identification is required to be natural in $\mathcal{M}$. Some such requirement is unavoidable, since for every $\mathcal{M}$ anti-isomorphic to itself an isomorphism exists for trivial reasons. Consequently no Choi--Jamiołkowski correspondence exists for the type III factors constructed by Connes. Along the way we show that the space of all normal maps, taken with the operator norm, is strictly too large for this purpose, and that complete positivity does not force complete boundedness in this setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13811v1
- Title: Strong photoresponse of edge two-dimensional electrons in a magnetic field
- Authors: Sergey A. Mikhailov, Wladislaw Michailow
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; physics.app-ph; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13811v1  pdf=https://arxiv.org/pdf/2608.13811v1.pdf

Abstract:
Electrons in two-dimensional electron gases in the presence of an out-of-plane magnetic field propagate along the edge with a high velocity of the order of the Fermi velocity. Under microwave and terahertz radiation, photon absorption by these electrons provides a pathway to realising sensitive radiation detection. Here, we develop a detailed quantum theory of the photocurrent generated in such a system by an incident electromagnetic wave and propose an experimental geometry for observing the predicted phenomenon. By using suitably arranged radiation confinement structures, a strong photocurrent generation efficiency can be obtained. We also demonstrate that the resulting photoresponse in III-V semiconductor structures can be orders of magnitude higher than that measured in graphene.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13855v1
- Title: Small-world structure of quantum computer hardware
- Authors: S. J. da Silva Junior, D. L. Shepelyansky, J. Lages
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13855v1  pdf=https://arxiv.org/pdf/2608.13855v1.pdf

Abstract:
We show that the network of quantum register states of a quantum computer (QC), coupled through residual two-body interactions between qubits, exhibits small-world properties analogous to those of complex networks found in human society. The most probable Erdős number between any two states is about 9, comparable to the six degrees of separation reported by Milgram for social networks. Using the $\mathring{A}$berg criterion, which retains only interactions exceeding the local energy spacing, we construct an effective ($\mathring{A}$berg) network and show that, above a critical coupling strength, this network percolates into a giant component spanning nearly the whole quantum register space. This percolation transition closely matches the onset of quantum chaos and dynamical thermalization established previously via costly exact diagonalization, while our approach extends the accessible system size up to $n_q=30$ qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13860v1
- Title: The Capacity Region of the Multiple Access Channel with Non-Signaling Assistance
- Authors: Yuhang Yao, Syed A. Jafar
- Categories: cs.IT (primary); cs.IT; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13860v1  pdf=https://arxiv.org/pdf/2608.13860v1.pdf

Abstract:
The capacity region of the $K$-sender discrete memoryless multiple access channel (MAC) is fully characterized when non-signaling (NS) assistance is available to all $K$ transmitters and the receiver. It is shown to have the same form as the classical capacity region of the MAC, except that the input distribution is allowed to be arbitrarily dependent across the senders. In particular, the NS-assisted capacity region matches the natural generalization to $K$ senders of an outer bound that was previously established by Fawzi and Fermé for $K=2$ senders. Additionally, we provide examples of $K$-sender MACs where the multiplicative gain in capacity from NS-assistance is arbitrarily close to $K$. Combined with an upper bound from prior work, this establishes $K$ as the extremal value of the multiplicative gain from NS-assistance across all $K$-sender MAC settings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13914v1
- Title: Hybrid Quantum-inspired Kolmogorov-Arnold Networks for Privacy-Aware Federated Biosignal Learning
- Authors: Chun-Hua Lin, Samuel Yen-Chi Chen, Yu-Chao Hsu, Kuo-Chung Peng, Jiun-Cheng Jiang, Chi-Sheng Chen, Tai-Yue Li, Nan-Yow Chen, et al.
- Categories: cs.LG (primary); cs.LG; cs.AI; cs.DC; cs.ET; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13914v1  pdf=https://arxiv.org/pdf/2608.13914v1.pdf

Abstract:
Electrocardiogram (ECG) recordings are sensitive biomedical data, limiting the ability of hospitals and wearable devices to share raw signals for centralized model training. Federated learning addresses this practical privacy constraint by enabling collaborative model training while keeping raw biosignal data at their respective sources. However, federated ECG classification remains challenging due to limited client-side samples, imbalanced arrhythmia labels, and non-independent and identically distributed (non-IID) data across clients. These constraints require classifiers that are both communication-efficient and robust to cross-client distribution shifts. In this work, we evaluate a hybrid quantum-inspired Kolmogorov-Arnold network (HQKAN) against a multilayer perceptron (MLP) for five-class arrhythmia classification on the MIT-BIH dataset and three-class classification on the INCART dataset under federated averaging (FedAvg). Across multiple client configurations, HQKAN improves most aggregate and minority-class metrics while using 37.35% fewer trainable parameters and reducing communication cost by 24.89% on MIT-BIH; on INCART, it achieves corresponding reductions of 44.81% and 36.41%. These results indicate that HQKAN offers a compact, communication-efficient and robust alternative to the MLP baseline for privacy-aware federated learning on biosignal data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.13936v1
- Title: Cold-atom comagnetometry via optical control of spin states
- Authors: J. -L. Zhang, W. -T. Luo, Y. A. Yang, Y. -Q. Wang, T. Xia, Z. -T. Lu
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2608.13936v1  pdf=https://arxiv.org/pdf/2608.13936v1.pdf

Abstract:
Atomic spin-based comagnetometers are powerful tools for precision sensing and tests of fundamental physics. Compared with the widely used gas-cell comagnetometer systems, cold-atom systems offer access to much shorter distance scales and allow implementation of {optical} quantum control techniques. However, in order to realize long spin coherence times with cold atoms, it is necessary to employ diamagnetic atoms and overcome decoherence induced by light shifts. Here we demonstrate a cold-atom comagnetometer based on the nuclear spins of $^{171}$Yb (spin-1/2) and $^{173}$Yb (spin-5/2), jointly trapped in an optical lattice. Vector light shifts are suppressed by enforcing linear polarization of the lattice, while tensor shifts in $^{173}$Yb are suppressed via the use of a Schrödinger cat state. This enables simultaneous Ramsey interferometry on both isotopes with a spin coherence time of 60 s. We achieve a magnetic noise suppression factor exceeding $3\times10^4$, and determine the ratio of nuclear magnetic moments to 4 ppm precision. Our results establish a new cold-atom platform for spin-based sensing and open pathways toward quantum-enhanced searches for physics beyond the Standard Model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14296v1
- Title: Entanglement spectrum ordering and flavor polarization in the two-flavor Schwinger model at vacuum angle $θ= π$
- Authors: Boliang Yu, Ruixin Zhou, Meisen Gao
- Categories: hep-lat (primary); hep-lat; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2608.14296v1  pdf=https://arxiv.org/pdf/2608.14296v1.pdf

Abstract:
Entanglement spectra in gauge theories can encode both symmetry breaking and the organization of gauge sectors. In the two-flavor Schwinger model at vacuum angle $θ=π$, we find that the joint Schmidt distribution $p_{Q_A,F_A}$, labeled by the subsystem gauge charge $Q_A$ and flavor imbalance $F_A$, reveals a cut-dependent gauge-sector hierarchy and a mass-induced flavor asymmetry: changing the staggered cut reorganizes the gauge-charge distribution $p_{Q_A}$, while mass imbalance breaks the $F_A\leftrightarrow-F_A$ symmetry of the conditional flavor distribution $p_{F_A|Q_A}$. Defining the combined weight $W_F^{(q)}=p_{q,+1}+p_{q,-1}$ and conditional polarization $\mathcal P_F^{(q)}=(p_{q,+1}-p_{q,-1})/W_F^{(q)}$, we find that changing the cut reverses the weight hierarchy, $W_F^{(-1)}>W_F^{(+1)}$ at unit-cell boundaries but $W_F^{(+1)}>W_F^{(-1)}$ at intra-cell cuts, while mass imbalance drives $\mathcal P_F^{(q)}$ away from zero with a $q$-dependent cut response. Symmetry resolution therefore separates gauge-sector ordering, sector weight, and flavor polarization that are mixed in the globally ordered entanglement spectrum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14319v1
- Title: Quantum Multi-Armed Bandits and Linear Bandits: Lower Bounds and Algorithms
- Authors: Maoli Liu, Zhuohua Li, John C. S. Lui
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2608.14319v1  pdf=https://arxiv.org/pdf/2608.14319v1.pdf

Abstract:
We study quantum multi-armed bandits (QMAB) and quantum linear bandits (QLB) in the model of Wan et al. [2023], where the learner queries each arm or action through a quantum reward oracle or its inverse. Prior work gives algorithms over horizon $T$ with regret $O(K\log T)$ for QMAB with $K$ arms and $O(d^2\operatorname{polylog} T)$ for $d$-dimensional QLB. This leaves open whether the $K\log T$ scale is unavoidable and whether the $d^2$ dependence can be improved. We prove the first minimax lower bounds of $Ω(K\log(T/K))$ for QMAB and $Ω(d\log(T/d))$ for finite-action QLB, resolving the question raised by Wan et al. [2023] of whether regret independent of $T$ is achievable. At the heart of our argument is a high-confidence single-arm quantum testing lower bound for distinguishing a fixed reward mean from an interval of alternatives, proved by the polynomial method and a Remez-type inequality for trigonometric polynomials. A bandit-to-testing reduction then lifts it to the QMAB lower bound, while a linear embedding gives the finite-action QLB lower bound. Complementing the lower bounds, we give a design-based elimination algorithm for finite-action QLB. When the action set has size $\operatorname{poly}(d)$, its regret is linear in $d$, improving the prior $d^2$ dependence and matching our lower bound up to polylogarithmic factors. The algorithm couples a low-bias low-variance quantum mean estimator with a small-support $G$-optimal design through a query allocation matched to the design weights. The design-based elimination reduces the dimension dependence from $d^2$ to $d^{3/2}$ when using Quantum Monte Carlo estimates. The low-variance estimator then makes reconstruction error aggregate through variance rather than worst-case absolute error, removing the remaining $\sqrt d$ factor.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14353v1
- Title: Orbital Hall Effect in Weyl Semimetals from quantum geometric band interference
- Authors: Chiara Pacella, Maximilian Ünzelmann, Ahmed Osman, Tim Figgemeier, Friedrich Reinert, Angel Rubio, Domenico Di Sante
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2608.14353v1  pdf=https://arxiv.org/pdf/2608.14353v1.pdf

Abstract:
Orbital angular momentum (OAM) transport in solids, prominently manifested in the orbital Hall effect, has emerged as a fundamental phenomenon that can decisively exceed its spin-based counterparts. However, the microscopic mechanisms governing OAM dynamics remain only partially understood. In particular, the role of band geometry in orbital transport is still largely unresolved. Here we address this question in the TaAs family of Weyl semimetals, TaAs, TaP, NbAs, and NbP, whose well-established topology and associated OAM textures make them an ideal platform in this context. Using ab initio density functional theory, complemented by a minimal Weyl model based on adiabatic perturbation theory, we establish --- both numerically and analytically --- a direct link between OAM transport, band geometry, and topological electronic structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14447v1
- Title: Angular displacement readout of a mechanical oscillator with a guided mode resonance
- Authors: Diego Torres-Barajas, Oscar Angulo, Aman R. Agrawal, Mohamed ElKabbash, Dalziel J. Wilson
- Categories: physics.optics (primary); physics.optics; cond-mat.mes-hall; physics.ins-det; quant-ph
- Links: abs=https://arxiv.org/abs/2608.14447v1  pdf=https://arxiv.org/pdf/2608.14447v1.pdf

Abstract:
Measuring the angular displacement of a mechanical oscillator is a ubiquitous task; however, the multimode nature of angular optomechanical coupling makes coherent signal enhancement challenging. Here we demonstrate coherently enhanced angular displacement readout with an integrated guided mode resonance (GMR) structure, applying it to precision readout of a nanomechanical oscillator. Specifically, we fabricate subwavelength gratings into 100-nm-thick Si$_3$N$_4$ membranes and record their vibration by direct transmission measurements. The narrow linewidth $\approx 2.5\;\text{mrad}$ of the GMR enables a shot-noise-limited displacement imprecision of $ 10^{-9}\;\text{rad}/\sqrt{\text{Hz}}$ with nanowatts of optical power, sufficient to resolve the thermal motion of a $Q\approx 10^6$ torsion mode with a signal-to-noise ratio of 47 dB. Control experiments based on polarization and wavelength detuning confirm that the measured signal arises from GMR-mediated transduction. These results establish guided-mode resonance as an on-chip approach to angular displacement readout in quantum optomechanical sensors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14476v1
- Title: A Fixed Universal Determinant is Variationally Complete for Continuum Fermions
- Authors: Giuseppe Carleo, Riccardo Rossi
- Categories: cond-mat.str-el (primary); cond-mat.str-el; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2608.14476v1  pdf=https://arxiv.org/pdf/2608.14476v1.pdf

Abstract:
How many Slater determinants does an accurate variational description of interacting fermions require? Exact expansions in a finite basis need combinatorially many, and state-of-the-art fermionic neural quantum states stack growing numbers of them. We prove that, in the norms that govern variational calculations, at most two are needed, independently of the number of particles and of the target accuracy. A single universal Slater determinant-specified in advance, independent of both the system and the state-multiplied by a smooth bosonic wave function approximates any fermionic wave function in up to three spatial dimensions in the first-order Sobolev norm, which controls the variational energy. Reaching the second-order Sobolev norm-for Coulomb interactions, the domain of the Hamiltonian, which bounds the variance of the local energy at the core of variational Monte Carlo-requires at most one additional fixed determinant, and only in three dimensions. Antisymmetry therefore costs at most two universal determinants and no expressiveness: generalized Slater-Jastrow neural quantum states are variationally complete.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14508v1
- Title: Universal aspects of bulk density of states in non-Hermitian lattices
- Authors: Mykhailo Pavliuk, Askar Iliasov, Emil J. Bergholtz, Tomáš Bzdušek
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2608.14508v1  pdf=https://arxiv.org/pdf/2608.14508v1.pdf

Abstract:
Non-Hermitian lattice Hamiltonians generally exhibit strong boundary sensitivity, with periodic and open boundary conditions producing distinct density of states (DOS) in the complex-energy plane. This has led to the view that extended non-Hermitian systems lack a unique bulk DOS, with different prescriptions representing inequivalent bulk physics. Here, we show that this apparent ambiguity is largely illusory. For any finite-range tight-binding Hamiltonian, we establish a universal bulk structure: all DOS definitions arising as thermodynamic limits of finite systems share identical multipole moments and generate identical bulk dynamics at finite times and for observables measured far from boundaries. This universality is intimately tied to the thermodynamic Green's functions, which we show to be independent of the boundary condition for large enough complex frequencies. Among all equivalent descriptions, we identify the Brown measure - obtained via Hermitization and resolvent analysis - as a canonical and convenient representative of the bulk DOS, defined directly from the infinite-volume Hamiltonian. We further show that point-gap topology imposes additional universal constraints: boundary-dependent Green's functions are forced to coincide throughout topologically trivial point gaps. This, in particular, provides a systematic criterion, valid in arbitrary dimension, for determining where and how eigenvalues of different boundary truncations can accumulate in the complex plane, and precisely delineates the regime in which the DOS ambiguity retains physical significance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.14544v1
- Title: GPU implementation of mixed quantum-classical Liouville molecular dynamics without momentum jump
- Authors: Koji Ando
- Categories: physics.chem-ph (primary); physics.chem-ph; cond-mat.mtrl-sci; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2608.14544v1  pdf=https://arxiv.org/pdf/2608.14544v1.pdf

Abstract:
We implemented on GPU a mixed quantum-classical Liouville molecular dynamics simulation based on a momentum-jump-free theory. The trajectory spawning that was previously implemented on CPU for sampling enhancement was eliminated to avoid the overhead of thread divergence and dynamic memory allocation on the GPU. This achieved a speedup of an order of magnitude compared to the CPU computation with spawning, as well as a linear scaling with respect to the number of sampling trajectories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2403.07596v3
- Title: A Provably Secure Framework for Noise-Aware Delegated Quantum Computation and Storage
- Authors: Sanidhya Gupta, Ankur Raina
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2403.07596v3  pdf=https://arxiv.org/pdf/2403.07596v3.pdf

Abstract:
As large-scale quantum computers become a reality, they will likely exist as centralized cloud resources accessible to a broad user base. Securely delegating private quantum computations to untrusted servers is therefore a foundational challenge. This requires rigorous guarantees of privacy (blindness), correctness (completeness), and integrity against malicious actions (verifiability). This paper presents an integrated architectural framework for noise-aware distributed quantum computation. The framework combines three technical components into a unified system: (1) a distributed stabilizer-code backbone to encode and store quantum states across multiple server nodes, with security analyzed under non-communication and bounded-collusion assumptions; (2) a two-level error-management structure, where each server node can locally handle errors based on its specific noise model; and (3) a trap-based verification protocol to detect malicious deviations with probability controlled by a security parameter. We provide a security analysis showing that, under the stated assumptions, the framework achieves completeness, blindness, and verifiability with respect to the permitted leakage. Our work provides an architectural blueprint for trustworthy distributed quantum computation under explicitly stated assumptions, paving the way for further development of secure quantum cloud services.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2408.07118v3
- Title: Efficient Multiparty Entanglement Distribution in Dynamic Quantum Networks
- Authors: Roberto Negrin, Nicolas Dirnegger, William Munizzi, Jugal Talukdar, Prineha Narang
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2408.07118v3  pdf=https://arxiv.org/pdf/2408.07118v3.pdf

Abstract:
Distributing multipartite entanglement over a quantum network means routing it through a shared resource state. Existing measurement-based schemes search for a fresh path and re-verify the topology before every request, placing a network-wide classical exchange on the critical path of each one. We introduce DODAG-X, which removes it. A single destination-oriented directed acyclic graph spanning tree is computed once and reused across all requests, so each party's route is recovered by following parent pointers instead of by a new search. The per-request routing cost drops from $\mathcal{O}(N)$ to $\mathcal{O}(\sqrt{N})$ on symmetric grids and to $\mathcal{O}(\log N)$ on small-world networks for $N$ nodes, and only the $N-1$ tree links need be maintained under link loss. Routing on the sparse tree also shrinks the neighborhoods cleared to isolate the parties, lowering measurements per request by roughly 19\% on small-world graphs and up to 34\% on moderately dense, strongly rewired ones; on a fixed tree the two protocols use identical counts. We prove correctness for up to three parties with no restriction on topology, and prove a sufficient condition under which one application yields an $n$-party GHZ state for any $n$. We then delimit it, exhibiting requests outside the hypothesis whose output is multipartite entangled yet in a different local-Clifford class. Under a discrete-time Markov failure model the classical repair layer matches the reachability of full-graph re-search up to a failed-edge fraction of one half, and a coherence criterion relating tree depth to memory lifetime identifies the viable hardware platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2502.07706v3
- Title: Materials and spin characteristics of amino-terminated nanodiamonds embedded with nitrogen-vacancy color centers
- Authors: Nikoletta Jegenyes, Vladimir Verkhovlyuk, Szabolcs Czene, Attila Csáki, Olga Krafcsik, Zsolt Czigány, David Beke, Adam Gali
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2502.07706v3  pdf=https://arxiv.org/pdf/2502.07706v3.pdf

Abstract:
Fluorescent nanodiamonds (FNDs) with optically read qubits hold great potential for detecting electric and magnetic fields, temperature, and other nanoscale physico-chemical quantities relevant to chemistry and biology. Proper surface functionalization is essential for their application as probes, but surface modifications can impact qubit sensor properties. We systematically study nitrogen-vacancy (NV) color centers in FNDs as a function of size and surface termination. FNDs were produced from high-pressure, high-temperature diamonds, with NV centers introduced via electron irradiation and annealing. The initial oxygen-covered FNDs were homogenized with hydroxyl (-OH) groups as reference samples, while the non-invasive Hofmann degradation introduced amino (-NH2) groups for potential direct biomolecule attachment. Amino groups may not cover the nanodiamonds homogeneously, but we label them as -NH2 terminated throughout. We monitored charge state stability and the zero-field splitting parameters of the embedded NV centers. First, we resolve the size dependence of the NV(-) zero-field splitting parameters across the 10-140 nm range and show that the symmetry-breaking E parameter decreases monotonically from about 8 to about 5 MHz with increasing size, while the axial D parameter is shifted only in the smallest (<= 30 nm) particles, thereby disentangling the static-strain and fluctuating-electric-field contributions to the spin levels. Second, while NV charge state stabilization was observed in both -OH- and -NH2-terminated FNDs above a certain size, we demonstrate that a remarkably high and laser-power-independent NV(-) content (f_NV(-) = 0.8) is achieved by wet-chemical Hofmann amino termination only at 140-nm particles, an effect we link through electron spin resonance to the degradation of surface paramagnetic defects rather than to the introduction of new ones.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2503.14660v2
- Title: Heuristic and Optimal Synthesis of CNOT and Clifford Circuits
- Authors: Mark Webster, Stergios Koutsioumpas, Dan E Browne
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.14660v2  pdf=https://arxiv.org/pdf/2503.14660v2.pdf

Abstract:
Efficiently implementing Clifford circuits is crucial for quantum error correction and quantum algorithms. Linear reversible circuits, equivalent to circuits composed of CNOT gates, have important applications in classical computing. In this work we present methods for CNOT and general Clifford circuit synthesis which can be used to minimise either the entangling two-qubit gate count or the circuit depth. We present three families of algorithms - optimal synthesis which works on small circuits, A* synthesis for intermediate-size circuits and greedy synthesis for large circuits. We benchmark against existing methods in the literature and show that our approach results in circuits with lower two-qubit gate count than previous methods. The algorithms have been implemented in a GitHub repository for use by the classical and quantum computing community.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2504.17790v3
- Title: Quantum Error Correction with Girth-16 Non-Binary LDPC Codes via Affine Permutation Construction
- Authors: Kenta Kasai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2504.17790v3  pdf=https://arxiv.org/pdf/2504.17790v3.pdf

Abstract:
We propose a method for constructing quantum error-correcting codes based on non-binary low-density parity-check codes with Tanner graph girth 16. While conventional constructions using circulant permutation matrices are limited to girth 12, our method employs affine permutation matrices and a randomized sequential selection procedure to eliminate short cycles and achieve girth 16.   Numerical experiments show that the proposed codes significantly reduce the number of low-weight codewords. Joint belief propagation decoding over depolarizing channels reveals that although a slight degradation appears in the waterfall region, a substantial improvement is achieved in the error floor performance.   We also evaluated the minimum distance and found that the proposed codes achieve a larger upper bound compared to conventional constructions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2507.11534v3
- Title: Sharp Error-Rate Transitions in Quantum QC-LDPC Codes under Joint BP Decoding
- Authors: Daiki Komoto, Kenta Kasai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2507.11534v3  pdf=https://arxiv.org/pdf/2507.11534v3.pdf

Abstract:
In this study, we report that quantum quasi-cyclic low-density parity-check codes decoded via joint belief propagation (BP) exhibit steep error-rate curves, despite the presence of error floors. To the best of our knowledge, this is the first observation of such threshold-like behavior for quantum LDPC codes with non-vanishing coding rate, excluding those decoded with non-binary BP decoders. Moreover, we find that dominant error events contributing to the error floor typically involve only a small number of bits. These findings suggest that the error floor is caused by trapping sets--specific subgraph structures in the Tanner graph--and indicate that identifying and avoiding such structures may lead to further reduction of the error floor.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2508.07344v2
- Title: QuMIMO Diversity over Discrete-Variable Free-Space Optical Channels
- Authors: Shehbaz Tariq, Junaid ur Rehman, Symeon Chatzinotas
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.07344v2  pdf=https://arxiv.org/pdf/2508.07344v2.pdf

Abstract:
Free-space optical (FSO) links carry quantum states without fiber, but diffraction, pointing error, and atmospheric turbulence couple spatial modes and reduce end-to-end fidelity. Classical multiple-input multiple-output (MIMO) uses spatial channels for multiplexing or diversity. For unknown quantum states, however, the no-cloning theorem prevents classical replication. We therefore formulate an FSO quantum multiple-input multiple-output (QuMIMO) link for an unknown polarization qubit as a single completely positive and trace-preserving (CPTP) map. It combines passive field transfer, bosonic pure loss lifted to Fock space, a receiver map to erasure-augmented polarization qubits, and effective per-port polarization noise. The plane-wave Rytov variance parameterizes turbulence, while an internal-state Gram matrix captures partial photon distinguishability and its effects on path coherence and multiphoton interference. Using Haar-averaged state fidelity, we compare direct transmission, fixed quantum error correction (QEC), approximate quantum cloning, coherent path superposition, and channel-adapted encoder and recovery maps, while distinguishing channel state information (CSI) from endpoint availability. With Full CSI on the two-rail channel, asymmetric cloning and coherent path superposition exceed the fixed single-input single-output (SISO) baseline in average fidelity. Adding rails and their admitted photon-number sectors enlarges the attained general-CPTP gain over the fixed SISO baseline, with the widest margin at moderate turbulence. Fixed stabilizer encoders perform poorly as turbulence makes rail survival unequal and produces errors unlike erasures at known code positions. Thus, QuMIMO realizes channel-adapted spatial diversity without requiring multiple copies of the logical qubit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2508.16683v2
- Title: Intersubjective Agreement about Measurement Outcomes Is Unnecessary in QBism
- Authors: Gino Elia, Jennifer Carter, Robert Crease
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.16683v2  pdf=https://arxiv.org/pdf/2508.16683v2.pdf

Abstract:
The thought experiment called ``Wigner's Friend" has experienced a renewal of interest for interrogating the meaning of intersubjectivity and objectivity in quantum mechanics. These new inquiries extend to investigations at the intersection of phenomenology and QBism. Philosopher of physics Steven French argues that QBism does not give assurances that Wigner and friend must agree on the same quantum state or measurement outcomes. In this article, we draw on Wigner's Friend to argue that an external guarantee for agreement on either quantum states or measurement outcomes is unnecessary. We defend the view that the quantum formalism is already inherently intersubjective in the way required to sustain objectivity. Here we explore the QBist notion of reciprocity, which treats Wigner and friend as physical systems taking mutual actions on each other. The QBist notion of reciprocity leads to a sharper characterization of what it means to objectify quantum systems with the formalism. Drawing on phenomenological resources, we argue that state assignments for quantum systems, including those for Wigner and friend, are a form of objectification. To assign a quantum state is to objectify a phenomenon as a quantum system, to treat something as the sort of object to which the formalism applies. Our argument accounts for why the quantum formalism does not radically change in application for different systems because the systems themselves exceed their formalization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2510.25583v2
- Title: Systematic Non-Binary Extension of LDPC-CSS Codes Preserving Orthogonality
- Authors: Kenta Kasai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2510.25583v2  pdf=https://arxiv.org/pdf/2510.25583v2.pdf

Abstract:
We study finite-field extensions that preserve the same support as the parity-check matrices defining a given binary CSS code. Here, an LDPC-CSS code refers to a CSS code whose parity-check matrices are orthogonal in the sense that each pair of corresponding rows overlaps in an even (possibly zero) number of positions, typically at most twice in sparse constructions. Beyond the low-density setting, we further propose a systematic construction method that extends to arbitrary CSS codes, providing feasible finite-field generalizations that maintain both the binary support and the orthogonality condition.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2511.03796v2
- Title: Boltzmann Sampling of Frustrated J1 - J2 Ising Models with Programmable Quantum Annealers
- Authors: Elijah Pelofske
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2511.03796v2  pdf=https://arxiv.org/pdf/2511.03796v2.pdf

Abstract:
One of the surprising, and potentially very useful, capabilities of analog quantum computers, such as D-Wave quantum annealers, is sampling from the Boltzmann, or Gibbs, distribution defined by a classical Hamiltonian. In this study, we thoroughly examine the ability of D-Wave quantum annealers to sample from the Boltzmann distribution defined by a canonical type of competing magnetic frustration $J_1$-$J_2$ model; the 1-dimensional ANNNI (axial next-nearest-neighbor Ising) model. Boltzmann sampling error rate is quantified for standard linear-ramp anneals ranging from $5$ nanosecond annealing times up to $2000$ microseconds on two different D-Wave quantum annealing processors. Interestingly, we find some analog hardware parameters which result in a very high accuracy (down to a TVD of $0.0003$) and low temperature sampling (down to $β=32.2$) in a frustrated region of the ANNNI model magnetic phase diagram. This bolsters the viability of current analog quantum computers for thermodynamic sampling applications of highly frustrated magnetic spin systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2511.04634v2
- Title: Random Construction of Quantum LDPC Codes
- Authors: Koki Okada, Kenta Kasai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2511.04634v2  pdf=https://arxiv.org/pdf/2511.04634v2.pdf

Abstract:
We propose a method for modifying orthogonal sparse matrix pairs used in CSS codes while preserving their matrix row and column weight distributions, which play a crucial role in determining the performance of belief-propagation decoding. Unlike simple row or column permutations that merely reorder existing elements, the proposed local modification introduces genuine structural randomness through small $2\times2$ cross-swap operations followed by integer-linear-program-based local repairs that restore orthogonality. By applying this procedure repeatedly in a random manner, ensembles of randomized quantum LDPC codes can be constructed. The computational complexity of each repair depends only on the maximum row and column weights and is independent of the overall matrix size, ensuring scalability to large code blocks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2512.10000v2
- Title: A Unified Linear Algebraic Framework for Physical Models and Generalized Contextuality
- Authors: Farid Shahandeh, Theodoros Yianni, Mina Doosti
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2512.10000v2  pdf=https://arxiv.org/pdf/2512.10000v2.pdf

Abstract:
We develop a bottom-up, statistics-first framework in which the full probabilistic content of an operational theory is encoded in its matrix of conditional outcome probabilities of events (COPE). Within this setting, five model classes (preGPTs, GPTs, quasiprobabilistic, ontological, and noncontextual ontological) are unified as constrained factorizations of the COPE matrix. We identify equirank factorizations as the structural core of GPTs and noncontextual ontological models and establish their relation to tomographic completeness. This yields a simple, model-agnostic criterion for noncontextuality: an operational theory admits a noncontextual ontological model if and only if its COPE matrix admits an equirank nonnegative matrix factorization (ENMF). Failure of the equirank condition in all ontological models therefore establishes contextuality. We operationalize rank separation via two complementary methods provided by the linear-algebraic framework. First, we use ENMF to interpret noncontextual ontological models as nested polytopes. This allows us to establish that the boxworld operational theory is ontologically contextual. Second, we apply techniques from discrete mathematics to derive a lower bound on the ontological dimensionality of COPE matrices exhibiting sparsity patterns, and use this bound to establish a new proof that a discrete version of qubit theory exhibits ontological contextuality. By reframing contextuality as a problem in matrix analysis, our work provides a unified structure for its systematic study and opens new avenues for exploring nonclassical resources.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2512.17530v2
- Title: Refrigeration of a 1D gas of microwave photons
- Authors: Lukas Schamriß, Louis Garbe, Peter Rabl
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2512.17530v2  pdf=https://arxiv.org/pdf/2512.17530v2.pdf

Abstract:
We discuss a conceptually simple scheme for cooling a one dimensional gas of microwave photons in a superconducting transmission line. By shunting one end of the transmission line by a nonlinear Josephson element, we show how a cooling mechanism can be engineered that transfers photons from high- into low-frequency modes, while preserving their total number. We evaluate the resulting nonequilibrium steady state of the photon gas, which arises from a competition between this engineered cooling process and the natural, number non-conserving thermalization with the surrounding bath. Our analysis predicts that for realistic experimental parameters, this mechanism can be used to prepare photonic gases at sub-millikelvin temperatures, considerably below the typical base temperature of a dilution refrigerator. In addition, the system exhibits a new type of condensation transition that does not occur in the corresponding equilibrium scenario. As an outlook, we discuss potential applications of this cooling approach for quantum simulation schemes with interacting microwave photons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2604.00711v2
- Title: Learning Hidden Structures in Open Quantum Dynamics
- Authors: Alexander Teretenkov, Sergey Kuznetsov, Alexander Pechen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.00711v2  pdf=https://arxiv.org/pdf/2604.00711v2.pdf

Abstract:
We introduce a machine-learning approach for identifying hidden structural features of open quantum dynamics under restricted experimental access. Unlike most existing data-driven methods which focus on detection or prediction of dynamical behavior, our framework targets the inference of invariant algebraic structures underlying the effective Markovian evolution. Measurement limitations, symmetries, and superselection rules are incorporated through a *-algebraic description of accessible observables. The learning problem is formulated as maximum-likelihood estimation from multi-time measurement sequences, where the algebraic type of an invariant subalgebra, particularly a decoherence-free subalgebra, is treated as a discrete structural hypothesis. The feasibility of the approach is illustrated on multiple synthetic models and a waveguide quantum electrodynamics system, where nontrivial intermediate algebraic structures are identified directly from measurement data.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2604.27817v2
- Title: High-Girth Regular Quantum LDPC Codes from Square-Base Hypergraph Products via CPM Lifts
- Authors: Koki Okada, Kenta Kasai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2604.27817v2  pdf=https://arxiv.org/pdf/2604.27817v2.pdf

Abstract:
We study square-base Calderbank--Shor--Steane (CSS) hypergraph-product codes as a finite-length class for regular high-girth quantum low-density parity-check (LDPC) design. For base matrices of small column weight, we give checkable conditions for regularity, rank deficiency, and short-cycle exclusion, and we present explicit column-weight-three and column-weight-four examples with Tanner girth 6 and 8. We also analyze circulant permutation matrix (CPM) lifts of this class. Using the standard voltage-sum criterion, we identify orthogonality-forced Tanner 8-cycles and show that CPM lifting cannot raise the Tanner girth beyond 8 when these cycles are present. As a representative finite-length instance, a randomized CPM lift of the girth-8 base construction gives a $[[28800,62,\le192]]$ girth-8 $(3,6)$-regular CSS-LDPC code. Explicit weight-$192$ non-stabilizer logical representatives give $d_X,d_Z\le192$. Under degeneracy-aware belief-propagation decoding with optional ordered-statistics-decoding-lite post-processing, this code produced zero decoding failures in $2.993\times 10^8$ independent trials at depolarizing probability $p=0.1402$; the Wilson 95\% upper confidence bound is $1.28\times 10^{-8}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2605.11076v2
- Title: Graph-State Circuit Blocks control Entanglement and Scrambling Velocities
- Authors: Chandana Rao, Himanshu Sahu, Aranya Bhattacharya, Suhail Ahmad Rather, Mario Flory, Zahra Raissi
- Categories: quant-ph (primary); quant-ph; hep-th
- Links: abs=https://arxiv.org/abs/2605.11076v2  pdf=https://arxiv.org/pdf/2605.11076v2.pdf

Abstract:
Random circuit models often describe local dynamics using generic two-qubit gates, which have proven successful in capturing entanglement growth and operator spreading in many contexts. This approach naturally leads to the expectation that detailed gate structure plays only a limited role in coarse-grained entanglement and scrambling diagnostics. We show that the internal structure of multipartite circuit primitives can significantly influence these dynamical rates, even within a fixed random-circuit architecture. To investigate this, we study an exactly simulable family of Clifford quantum circuits built from fixed $n$-qubit graph-state preparation unitaries, which we treat as elementary building blocks. Specifically, we consider a one-dimensional chain of $N$ qubits initialized in a product state and evolved by layers in which nonoverlapping length-$n$ blocks are placed at uniformly random positions with sparsity $α$. We find that different choices of graph-state building blocks lead to strongly varying dynamical rates. Graph states that are inequivalent under local Clifford (LC) transformations generate sharply different entanglement velocities $v_E$ and butterfly velocities $v_B$, even though the circuits are drawn from the same ensemble with identical architecture and randomness parameters. We further show that this hierarchy is captured by two complementary block-level characteristics: the distribution of entanglement across internal bipartitions of the graph state, which correlates with $v_E$, and a graph-theoretic connectivity profile across bipartitions, which correlates with $v_B$. Neither descriptor alone fully determines the dynamics; rather, entanglement growth and operator spreading are controlled by distinct structural features of the local circuit blocks. Notably, AME states appear among the fastest scrambling building blocks within the ensembles studied here.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2605.14432v3
- Title: Singular Asymptotics of SPADE in Quantum Source Discrimination
- Authors: Natsuki Kariya
- Categories: quant-ph (primary); quant-ph; math.ST; stat.ME
- Links: abs=https://arxiv.org/abs/2605.14432v3  pdf=https://arxiv.org/pdf/2605.14432v3.pdf

Abstract:
We study far-field discrimination between one and two incoherent point sources in the singular regime of weak and closely spaced emitters. Under ideal alignment, spatial-mode demultiplexing (SPADE) attains the quantum-optimal large-sample Stein exponent, but the finite-photon behavior near the one-source boundary and the effect of realistic imperfections remain less understood. Using singular learning theory, we analyze both the aligned and misaligned problems. In the aligned Gaussian case, for prior densities that are smooth and strictly positive in the physical $(ε,s)$ coordinates near the singularity of the aligned model, direct imaging and SPADE share the same real log canonical threshold $λ=1/2$ but have different multiplicities, yielding distinct Bayes free-energy asymptotics. A fixed nonzero misalignment removes the exact support mismatch of ideal SPADE: locally, the fixed-offset binary-SPADE Kullback--Leibler function has the normal-crossing form $K\asympε^2s^2$, giving $(λ,m)=(1/2,2)$ under the same prior class, as for direct imaging. The local separation scale nevertheless depends on the source-position convention. Moreover, full Hermite--Gaussian mode counting about an offset sorter axis has a reflection-induced KL-zero branch at $s^\ast=2θ$, where the two-source alternative becomes indistinguishable from the null. Pointwise finite-$n$ binary-SPADE calculations exhibit the corresponding power collapse. These results identify measurement support, nuisance geometry, prior weighting, and identifiability as structural ingredients that must be tracked in finite-photon quantum discrimination.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2605.23894v2
- Title: A Two-Branch Finite-Field Construction for Regular CSS LDPC Bases
- Authors: Koki Okada, Kenta Kasai
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2605.23894v2  pdf=https://arxiv.org/pdf/2605.23894v2.pdf

Abstract:
This paper develops a two-branch multiplicative-coset construction for regular Calderbank-Shor-Steane (CSS) quantum low-density parity-check base matrices. For a target column weight \(J\) and an even row weight \(L\), the method reduces regularity, CSS orthogonality, and same-type 4-cycle exclusion to explicit quotient-coset conditions over a finite field. A normalized exhaustive search for these conditions produces base matrices for several \((J,L)\) pairs, so the construction is not tied to a single degree distribution. The construction separates the finite-length design into two stages: the base matrix fixes the degree distribution and the first girth constraints, and a cyclic lift randomizes edge connections subject to exact algebraic checks. As a detailed example, we carry one \((3,10)\)-regular base through the lift and decoding stages. For this example, the selected 64-fold lift gives a code whose same-type Tanner graphs have girth at least eight, and it also excludes a specified weight-16 nondegenerate logical-support orbit. The resulting instance is a \([[10240,4108,\,10\le d\le32]]\) CSS code. For decoding, we use joint log-domain belief propagation together with low-complexity deterministic post-processing rules for small residual syndromes, including repairs for residual patterns with two unsatisfied checks. The frame error rate (FER) measurements provide finite-length decoding data for this detailed example; at depolarizing probability \(p=0.058\), the post-processing FER is \(1.0\times10^{-7}\).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.04850v3
- Title: Two-dimensional Toda--Arnoldi correspondence: Holomorphic Krylov geometry and counterdiabatic transport
- Authors: Urei Miura
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; math-ph; nlin.SI
- Links: abs=https://arxiv.org/abs/2608.04850v3  pdf=https://arxiv.org/pdf/2608.04850v3.pdf

Abstract:
Although Arnoldi reduction of a generally non-Hermitian Hamiltonian yields an upper Hessenberg matrix rather than the tridiagonal form of Hermitian Lanczos theory, we show that a closed Toda sector survives in its diagonal and subdiagonal coefficients. For a fixed finite-dimensional Hamiltonian and a cyclic state vector deformed holomorphically, the Krylov Gram determinants are $τ$ functions of the finite two-dimensional Toda lattice, whose Flaschka variables coincide exactly with these Arnoldi coefficients. The Toda dynamics therefore closes on this sector without determining the remaining upper Hessenberg entries. The subdiagonal part of the same sector also has a direct geometric meaning: the squared subdiagonal coefficients determine both the Fubini--Study metric and the Berry curvature of holomorphic Krylov subspaces, whereas the geometric quantities associated with subspaces lost at Arnoldi breakdown cease to be defined. Along a smooth real path in the cyclic region, the Arnoldi-frame connection further provides a Hermitian tridiagonal generator of exact isospectral transport. When added to the Arnoldi matrix, this generator cancels transitions between instantaneous eigenspaces and realizes counterdiabatic driving whenever the matrix is diagonalizable with a nondegenerate spectrum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2608.12712v2
- Title: Parity Floors in Quantum Denoisers: A Closed-Form Benchmark for Fixed-Map Denoising Networks
- Authors: Jaeuk Kim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.12712v2  pdf=https://arxiv.org/pdf/2608.12712v2.pdf

Abstract:
Fixed quantum feature maps are increasingly inserted into diffusion denoisers, but standard image benchmarks do not reveal which structural constraint limits them. We introduce CoupledPhaseTexture, a torus-diffusion benchmark with analytic heat-kernel noising that separates parity, within-sector approximation, and sample-complexity limitations. For the depth-1 RY+CNOT+Pauli-Z family we prove a containment-free parity floor: all reachable features are even functions of the encoded angles while the sine components of the Bayes denoiser are odd, so the excess risk splits exactly into an inaccessible odd part and a within-sector residual. The first term is an irreducible, noise-scale-resolved lower bound holding for every even feature class, with no containment, linearity, or closedness assumption on the feature class. The obstruction is a property of the noise-conditioned denoising target rather than static representability: the floor is re-derived at each noise scale because the target's parity content changes with noise. The measured excess is dominated by the parity proxy on two distinct priors. Higher-order Z readouts improve the even sector, but entanglement does not lower the floor and re-uploading does not reliably close it. Classical controls confirm the deficit is parity rather than quantumness: a cosine-only bank is floored similarly, while adding the sine sector matches the reference. Among tested constructions, odd readouts and a noise-coupled encoder do not match the sine-carrying classical bank. These results motivate nonclassical data access or feature classes without efficient classical surrogates; they do not establish either as sufficient for quantum advantage.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2202.06937v2
- Title: What is the group of a quantum group? From $SL_q(2)$ to MPO representations of $SL(2)$
- Authors: Weronika Wiesiolek, Romain Couvreur, Dmitry Chernyak, Laurens Lootens, Frank Verstraete
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2202.06937v2  pdf=https://arxiv.org/pdf/2202.06937v2.pdf

Abstract:
Generalized symmetries realized by matrix product operators (MPOs) have so far been tied to discrete data leaving continuous symmetries outside the framework. Quantum groups fill this gap: starting from the RTT relations of $SL_q(2)$ at an odd root of unity $q^d=1$, we construct a three-parameter family of periodic-boundary MPOs of bond dimension $d^2$ that multiply according to the group law of $SL(2)$. This gives Lusztig's quantum Frobenius map a concrete operator form, and endows the XXZ chain on the ring at $Δ=(q+q^{-1})/2$ with an intrinsically non-local $SU(2)$ symmetry. Fusion of the local tensors is generically semisimple. On special loci it is non-semisimple, and yields reducible but indecomposable tensors with Jordan blocks. Differentiating $\mathcal{D}(g)$ at the identity produces the $\mathfrak{sl}(2)$ generators as $d$-body operators: the MPO algebra supplies the exponential map for quantum group algebras.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2409.11035v4
- Title: Quantum enhanced metrology based on flipping trajectory of cold Rydberg gases
- Authors: Ya-Jun Wang, Jun Zhang, Zheng-Yuan Zhang, Shi-Yao Shao, Qing Li, Han-Chao Chen, Yu Ma, Tian-Yu Han, et al.
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2409.11035v4  pdf=https://arxiv.org/pdf/2409.11035v4.pdf

Abstract:
The dynamical trajectory of a dissipative Rydberg many-body system could be flipped under a microwave field driving, displaying an enhanced sensitivity. This is because the intersection of the folded hysteresis trajectories exhibits a sharp peak near the phase transition, amplifying the response to small changes in the microwave field. Here, we demonstrate an experiment of enhanced metrology through flipping the hysteresis trajectory in a cold atomic system, displaying an approach to improve sensitivity near the gap-closing points. By measuring the intersection points of hysteresis trajectories versus Rabi frequency of the microwave field, we quantify the equivalent sensitivity to be 1.6(5) nV cm-1 Hz-1/2. The measurement is also dependent on the interaction time, optical depth and principal quantum number since the long-range interaction between Rydberg atoms could dramatically change the shape of hysteresis trajectories. The reported results suggest that flipping trajectory features in cold Rydberg many-body systems could advance sensing and metrology applications.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2512.10627v2
- Title: Edge states of a Bi$_2$Se$_3$ nanosheet in a perpendicular magnetic field
- Authors: Stan P. J. Koenis, Lucas Maisel Licerán, Henk T. C. Stoof
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2512.10627v2  pdf=https://arxiv.org/pdf/2512.10627v2.pdf

Abstract:
Conventional wisdom dictates that the conducting edge states of two-dimensional topological insulators of the Bi$_2$Se$_3$ family are protected by time-reversal symmetry. However, theoretical bulk calculations and a recent experiment show that the edge states persist in the presence of large external magnetic fields. To address this apparent contradiction, we have developed an analytical description for the edge-state wave function of a semi-infinite sample in a perpendicular magnetic field. Our description relies on the usual bulk Landau levels, together with additional states arising due to the presence of the hard wall, which are unnormalizable in the infinite system. The analytical wave functions agree extremely well with numerical calculations and can be used to directly analyze the behavior of the edge states in a magnetic field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2604.08587v3
- Title: Markovian dephasing has no entanglement-breaking threshold, and a fixed tolerance will report one anyway
- Authors: Hikaru Wakaura, Taiki Tanimae
- Categories: q-bio.NC (primary); q-bio.NC; physics.bio-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2604.08587v3  pdf=https://arxiv.org/pdf/2604.08587v3.pdf

Abstract:
When modelling decoherence in a biological spin system it is tempting to seek a critical rate beyond which the channel is entanglement-breaking (EB) and quantum resources are gone. We show that for the two channel families in which such a model would be posed, no critical rate exists. For uniform dephasing at rate $γ$ the partial transpose of the Choi state has eigenvalue $-e^{-γ}/d$, so the channel is non-PPT -- hence not EB -- at every finite $γ$. Adding amplitude damping changes nothing: the qubit map's partial transpose stays negative at all finite rates. What does vanish at a finite rate is the coherent information, exactly where the qubit map turns antidegradable: the root of $c^{2}=p$, $γ_{\Ic}=0.668$ at $κ=0.1$. Antidegradability survives tensor products, so the single-letter and regularised thresholds coincide: of the three properties usually conflated here, two share one finite boundary and the third has none. Our main object is the numerical mechanism that manufactures a threshold where there is none. A quantity that decays exponentially to zero without reaching it, tested against a fixed absolute cutoff, yields a "threshold" set by the cutoff: the PPT test gives $γ=5.49$ at $ε=10^{-10}$ and $6.58$ at $10^{-12}$, sliding by $0.55$ per decade. We reported the first number in three now-retracted preprints. Preparing this paper we made the same error three more times -- most seriously in $γ_{\Ic}$ itself, which a bisection against a $10^{-7}$ cutoff placed at $0.62$ -- and we document all four instances, with the closed forms and code that avoid them.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2605.00026v4
- Title: The $γ_c$-Peak: Covariant Recovery on Four Organic Qubit Platforms
- Authors: Hikaru Wakaura, Taiki Tanimae
- Categories: q-bio.NC (primary); q-bio.NC; quant-ph
- Links: abs=https://arxiv.org/abs/2605.00026v4  pdf=https://arxiv.org/pdf/2605.00026v4.pdf

Abstract:
We characterize where, in the noise parameter space of the uniform dephasing--depolarizing channel $\mathcal N_γ^δ=\mathcal E_δ\!\circ\!\mathcal D_γ$, a deterministic, \emph{nonlinear, target-informed} denoising heuristic yields its largest fidelity gain. The procedure pulls the off-diagonal magnitudes of the noisy state toward those of a known target, with efficiency set by a SWAP-test-purified catalyst; it is not a quantum channel, and target access is an explicit classical resource, so the results describe a benchmark procedure, not blind error correction. Our main tool is the covariant purification map $\mathcal P_\mathrm{cov}(ρ)=(ρ+ρ^2)/(1+\mathrm{Tr}\,ρ^2)$, an exact closed form for one SWAP-test purification round (a rederivation of symmetrization purification: Barenco \emph{et al.}, Cirac--Ekert--Macchiavello) that reduces the catalyst to a scalar eigenvalue iteration. With it we derive the $d\to\infty$ fidelity-gain peak location on Haar-random pure states (Theorem~3): $γ_{\rm peak}(d)\toγ^\star(r,δ)$, with $γ^\star(2,0.1)=0.4725$ and limiting magnitude $0.2262$. Bootstrap-quantified sweeps to $d=256$ are consistent with both limits. The peak is resource- and protocol-dependent: a catalyst-only reference moves it from $\approx0.50$ to $\approx0.34$, and one purification round instead of two to $\approx0.39$. Bell and uniform $d=4$ states admit unique-peak theorems for the $r=0$, $δ=0$ protocol member. All results are reproducible from the open-source \texttt{organic-qc-bench} package with seed~42.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-08-18 10:59
- arXiv: 2605.19725v2
- Title: Microcanonical Energy Sharing and a Page-like Curve for the Capacity of Entanglement
- Authors: Raul Arias
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2605.19725v2  pdf=https://arxiv.org/pdf/2605.19725v2.pdf

Abstract:
We study the capacity of entanglement in the microcanonical ensemble for an effectively additive bipartite system. Using typicality and the block structure of the microcanonical reduced state, we show that in the thermodynamic regime the capacity is controlled by energy-sharing fluctuations and can be expressed purely in terms of standard thermal response data of the subsystems. As an illustration, we apply the result to a toy model consisting of a Schwarzian ``black-hole'' sector coupled to a two-dimensional CFT radiation sector. At fixed total energy, the growth of the radiation sector forces the common temperature to decrease, producing a smooth Page-like single-hump curve for the capacity. We also distinguish the capacity of the reduced microcanonical state from that of a Haar-typical pure state in the same energy shell. A block-Wishart analysis shows that the effective-heat-capacity result holds on both sides of the Page crossover, while a universal folded-normal scaling function resolves a narrow window in which the two effective Hilbert-space dimensions become comparable. The construction is an equilibrium microcanonical mechanism for Page-like capacity curves, rather than a complete dynamical evaporation calculation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

