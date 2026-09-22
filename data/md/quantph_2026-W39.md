- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20852v1
- Title: UCQM: A Six-Metric Quality Framework for Continuous-Variable Cluster States
- Authors: Saman Sarshar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.20852v1  pdf=https://arxiv.org/pdf/2609.20852v1.pdf

Abstract:
Continuous-variable (CV) cluster states constitute one of the central resources for measurement-based quantum computation (MBQC). Despite substantial progress in their theoretical development and experimental realization, comparing the quality of different cluster-state topologies remains challenging, as existing approaches typically rely either on qualitative inspection of covariance matrices or on individual metrics that characterize only a single aspect of the underlying correlation structure. In this work, we propose a quantitative evaluation framework that integrates six complementary descriptors of CV cluster states: total correlation strength (SSC), correlation uniformity (CAV), error resilience (EVC), communication overhead (COM), path redundancy (RED), and bottleneck vulnerability (BOT). These quantities are combined into a single \textbf{Unified Cluster Quality Metric (UCQM)}, providing a consistent basis for evaluating and comparing different cluster-state architectures.   The proposed framework is applied to four-mode path, square, and star cluster topologies over the squeezing range $r \in [0.2,1.8]$. Across the investigated parameter regime, the square topology consistently achieves the highest UCQM score, indicating the most balanced structural characteristics among the topologies considered and supporting its suitability for measurement-based quantum computation. Because all six metrics are derived directly from covariance-matrix elements together with graph connectivity, the framework naturally extends to arbitrary $N$-mode cluster states, higher-dimensional lattice geometries, and experimentally reconstructed covariance matrices. Beyond providing a single numerical score, UCQM offers a unified perspective for analyzing the structural quality of CV cluster states and establishes a practical framework for their systematic comparison, optimization, and future design.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20853v1
- Title: Set-Packing and Sequence-Pair QUBOs for the 2D Cutting Stock Problem on Quantum Annealing Hardware
- Authors: Miguel Sánchez-Beato, Raul Martinez, Matilde Osa, Jorge Parra, Mario Calonge
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2609.20853v1  pdf=https://arxiv.org/pdf/2609.20853v1.pdf

Abstract:
The two-dimensional Cutting Stock Problem (2D-CSP) is an NP-hard problem with direct economic and environmental impacts on manufacturing and logistics. We encode its fixed-plate variant, with free piece repetition and full non-overlap and containment constraints, as a Quadratic Unconstrained Binary Optimization (QUBO) problem for quantum annealing and compare two formulations from opposite encoding paradigms. The first was a coordinate-based set-packing model with one binary variable per candidate placement. Its variable count grows linearly with plate area and resolution, but its ground state is, by construction, a geometrically feasible maximum-area packing. The second is a coordinate-free sequence-pair model whose variable count is independent of plate resolution and size. We prove that this compactness has a structural limit: no coordinate-free QUBO of bounded interaction degree whose penalties vanish on every geometrically feasible layout can have a geometrically feasible ground state for 2D containment, because containment is a longest-path constraint that bounded-degree penalties cannot enforce on chains longer than their interaction order. We evaluate both formulations under multi-seed simulated annealing, simulated quantum annealing, and an exact integer-programming baseline. Hardware experiments include D-Wave minor embedding, a calibrated direct-QPU sweep, and Leap hybrid solvers in both penalty and constraint-native form, across a six-instance campaign with per-instance calibration. The hybrid solver returns our certificate configuration, tying its energy to thirteen decimal places while overflowing the plate. We claim no quantum speedup. Our contribution is an impossibility result characterizing the limits of compact packing QUBOs, and a practical rule for choosing between the two formulations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20854v1
- Title: Oracle Synthesis Based on X-Map Decision Diagrams
- Authors: Xin Hong, Kezhen Zhang, Aochu Dai, Sanjiang Li, Shenggang Ying, Mingsheng Ying
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.20854v1  pdf=https://arxiv.org/pdf/2609.20854v1.pdf

Abstract:
Quantum oracles act as reversible black-box operators that encode classical Boolean functions into quantum states, enabling efficient function evaluation in quantum superposition. The resource efficiency of oracle implementation is critical to the performance of numerous quantum algorithms. Most state-of-the-art oracle synthesis approaches rely on compact Boolean function representations such as exclusive-sum-of-products (ESOP), yet still suffer from excessive $T$-count and $CX$-count for large-scale functions.   In this paper, we propose a novel compact representation named X-Map decision diagram (XMDD) for Boolean functions, which integrates local invertible maps and complement edges to achieve higher compression efficiency. Based on XMDD, we further develop an optimized quantum oracle synthesis algorithm. Extensive experimental results demonstrate that, for Boolean functions with more than seven input variables, our method outperforms the state-of-the-art ESOP-based approach and Qiskit in nearly all test cases, achieving simultaneous reduction in both $T$-count and $CX$-count without an obvious trade-off. Moreover, we show that the performance can be further boosted by employing more optimal variable orderings. The proposed XMDD-based framework provides a scalable and resource-efficient solution for practical oracle synthesis in near-term and fault-tolerant quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20861v1
- Title: Pauli-string grouping for VQE measurement reduction on a sparse-connectivity quantum annealer
- Authors: Raul Martinez, Miguel Sanchez-Beato, Mario Calonge
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2609.20861v1  pdf=https://arxiv.org/pdf/2609.20861v1.pdf

Abstract:
The Variational Quantum Eigensolver (VQE) requires a large number of measurements to evaluate molecular Hamiltonians. Expressing a molecular Hamiltonian as a linear combination of Pauli strings creates a measurement bottleneck: non-commuting Pauli strings cannot be measured simultaneously. Consequently, mutually commuting Pauli strings must be grouped and measured together to minimise the number of quantum-state preparations. This task maps to the minimum clique cover problem on a commutativity graph, an NP-hard problem typically addressed using classical heuristics. Although an Ising-model formulation has recently been explored on fully connected CMOS Ising machines and demonstrated on physical quantum annealers only at small scale, the embedding cost that governs its behaviour on hardware with sparse connectivity, where each logical variable must be represented by a chain of physical qubits, has not been characterised. In this work, we formulate the Pauli-grouping problem as a standard QUBO colouring model and study its scalability on a D-Wave quantum annealer. Across a series of molecular systems and for both qubit-wise and full commutativity, we quantify the growth in the number of logical variables and the QUBO interaction density, characterise the physical-qubit and chain-length overhead required for embedding on the Zephyr topology, and compare the annealer's time-to-solution and solution quality with those of heuristic classical baselines. This analysis identifies the threshold of molecular complexity beyond which hardware connectivity prevents viable embedding, and shows that a second, practical limit is reached earlier. The threshold therefore measures how far current annealers are from the regime in which pre-optimising a VQE measurement scheme on hardware would be worth considering.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20877v1
- Title: Stabilizer-Public-Key Authentication: Partial Prediction Bounds and Limits of Key Reuse
- Authors: Masahito Hayashi, Jingtian Zhao, Baichu Yu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.20877v1  pdf=https://arxiv.org/pdf/2609.20877v1.pdf

Abstract:
We propose an information-theoretic authentication protocol based on a finite supply of quadratic-stabilizer public-key states over an odd-prime field. A computationally unbounded adversary observes one valid classical signature and may jointly process $N$ public-key copies, while verification uses one additional independent copy. We show that, conditioned on the exposed signature, the security problem reduces to a partial-prediction game for a uniform stabilizer ensemble on $r=n-\ell$ residual qudits, with a partial query along $d=rank(Y-Y')$ directions, where $n$ is the number of qudits, $\ell$ is the message-space dimension, and $Y$ and $Y'$ denote the honestly signed and target-forged messages, respectively. Surprisingly, although the target requires only partial information, there is no first-order reduction in the required copy rate when $d/r\toβ\in(0,1]$. The optimal average fixed-target forgery probability tends to zero for $N/r\toα<1$ and to one for $α>1$, revealing a sharp threshold at $α=1$. Thus, our results guarantee security against fixed-target forgery under a single-signature-exposure model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20951v1
- Title: Nonlocal Magic Spreading in Many-body Quantum Dynamics: From Chaotic Evolution to Quasi-particle Picture in Integrable Models
- Authors: Sreemayee Aditya, Piotr Sierant, Xhek Turkeshi
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2609.20951v1  pdf=https://arxiv.org/pdf/2609.20951v1.pdf

Abstract:
Entanglement and magic are resources that reveal complementary aspects of quantum many-body systems. Their interplay is captured by nonlocal magic, the magic that survives arbitrary local changes of basis. Yet their markedly different dynamical behavior leaves open how this irreducible component of magic spreads. Here we connect nonlocal magic to the capacity of entanglement, a tractable quantity measuring fluctuations of the entanglement Hamiltonian. This connection enables analytically controlled predictions across a wide range of many-body dynamics, from chaotic to integrable systems, which we investigate also using large-scale numerical simulations. In chaotic systems, nonlocal magic exhibits a transient buildup, with logarithmic growth in time followed by decay to a size-independent value. For integrable systems, we develop a quasiparticle picture in quantitative agreement with numerics, showing that the same initial growth instead leads to saturation at a value logarithmic in subsystem size. These contrasting behaviors have an operational consequence for entanglement embezzlement: the strongest scramblers embezzle only transiently, whereas free-fermionic dynamics can sustain universal embezzlement in the steady state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20966v1
- Title: Robust many-body quantum batteries
- Authors: Finn Schmolke, Karen Hovhannisyan, Milton Aguilar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.20966v1  pdf=https://arxiv.org/pdf/2609.20966v1.pdf

Abstract:
Realistic work extraction from many-body quantum batteries must be local. However, only a small fraction of energy eigenstates of a generic many-body system, called scars, can support local extraction. The remaining bulk is useless for the task due to the eigenstate thermalization hypothesis. Here we devise a universal low-complexity protocol that steers any initial state towards exactly one scar---representing a charged state of the battery---from which a macroscopic amount of work can be extracted using local unitary operations. This is achieved by leveraging the nontrivial interplay of engineered dissipation and continuous indirect measurement that, in addition, leads to enhanced stability and charging speed compared to any other strategy using these processes independently. Moreover, the protocol works directly on the hardware level, in that it requires no simulation or suppression of interactions between subsystems. Our construction thereby enables macroscopic charge storage in steady states of generic nonintegrable many-body systems indefinitely, from which a reliable stream of work can be extracted via purely local means.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21086v1
- Title: Autonomous stabilization of many-body entanglement with Floquet Hamiltonians and weak measurement
- Authors: Charlotte Franke, Dorian A. Gangloff
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21086v1  pdf=https://arxiv.org/pdf/2609.21086v1.pdf

Abstract:
Reaching a technological advantage with large quantum systems requires safeguarding their many-body entanglement. Dissipation typically acts to decohere a quantum system via random projective noise but, when judiciously engineered together with coherent interactions, it can funnel the system towards a target entangled state. The native interactions and dissipative channels available to most systems are, however, difficult to combine effectively. Here we propose interleaving Floquet Hamiltonian engineering, which allows the construction of non-native coherent interactions, with weak measurement, which enables a tuneable dissipative channel, to enable programmable and autonomous stabilization of many-body entanglement. We show this analytically and numerically for the central-spin system of a semiconductor quantum dot, for which we construct spin-squeezed and Schrödinger-cat states that are stabilized against realistic levels of dephasing. Our approach is applicable to any system compatible with periodic drives and tuneable measurement strength and could enable novel approaches to practical error correction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21115v1
- Title: Hybrid quantum-classical attention for histopathology-based molecular profiling in data-limited cancers
- Authors: Kahn Rhrissorrakrai, Aritra Bose, Aldo Guzman-Saenz, Filippo Utro, Laxmi Pardia
- Categories: quant-ph (primary); quant-ph; q-bio.GN
- Links: abs=https://arxiv.org/abs/2609.21115v1  pdf=https://arxiv.org/pdf/2609.21115v1.pdf

Abstract:
Molecular profiling from routine histopathology could expand access to precision oncology when sequencing is unavailable, tissue is limited, or training cohorts are small. We developed a hybrid quantum-classical strategy that replaces softmax attention in a transformer for histopathology-based gene expression prediction with a quantum-derived doubly stochastic matrix (QDSM). Across 29 cancer cohorts from The Cancer Genome Atlas and an independent pancreatic cancer cohort from the Clinical Proteomic Tumor Analysis Consortium, QDSM attention produced selective gains, with the largest relative improvements in smaller, data-limited cohorts, including adrenocortical carcinoma and uveal melanoma. Rather than improving transcriptome-wide performance uniformly, QDSM redistributed predictive accuracy across genes and pathways, improving biologically relevant targets in some tumor contexts while worsening others. In adrenocortical carcinoma, preferentially improved genes were enriched for adverse overall-survival associations, linking enhanced molecular inference to prognostically relevant biology. In pancreatic cancer transfer experiments, QDSM improved selected metabolic and lineage-associated genes but did not consistently improve performance under cross-cohort shift. Leave-one-cancer-out mixed-effects analysis showed that baseline molecular features predicted part of the gene-level benefit, while residuals identified cancer-specific programs that improved more or less than expected. Separate experiments on IBM quantum processors recovered the doubly stochastic matrix primitive underlying the attention mechanism. These findings position QDSM attention as a context- and target-dependent strategy for image-based molecular profiling and molecular triage when direct testing is unavailable, incomplete, or impractical.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21152v1
- Title: ReFINE: Scheduling of Distillation and Coding for Rate-Fidelity Tradeoff in Quantum Networks
- Authors: Narges Alavisamani, Matthieu Bloch, Moinuddin Qureshi
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2609.21152v1  pdf=https://arxiv.org/pdf/2609.21152v1.pdf

Abstract:
In quantum networks, nodes are connected via sharing of Einstein-Podolsky-Rosen (EPR) pairs, ideally with high fidelity and high rate. However, the fidelity of EPR pairs degrades due to imperfect generation and decoherence errors. Entanglement Distillation is a method that increases the fidelity but operates probabilistically and may destroy all involved EPR pairs upon failure. This failure reduces available EPR pairs for application use, thereby decreasing the service rate. Quantum Error Correction (QEC) is another mechanism to protect EPR pairs against error by forming what we term as Coding-Enhanced Memory (CEM). While effective, CEM requires extra time and resources to form the code, which also reduces the service rate. Existing methods often use static combinations of distillation and CEM, ignoring demand variations. This results in a low service rate without significant fidelity gain. Limited resources together with this rate-fidelity tradeoff make it essential to schedule when to run distillation, form CEM, or serve requests.   We propose ReFINE, a demand-aware preemptive scheduler that based on application requirements either serves an available EPR pair immediately or preserves it in CEM. This selective use of CEM, only when needed, enables a better balance for rate-fidelity tradeoff than always using CEM. Between request arrivals, ReFINE either schedules distilling EPR pairs or forming CEM to protect distilled pairs, following one of the three priority policies: ReFINE-D (Distillation-First) first generates EPR pairs for distillation and then forms the CEM, prioritizing service rate. ReFINE-M (Memory-First) first forms the CEM, then generates the EPR pairs for distillation, prioritizing fidelity. ReFINE-C (Concurrent) performs both distillation and CEM formation concurrently, balancing between fidelity and service rate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21153v1
- Title: Shock-Capturing Quantum Algorithm for the Linear Advection Operator
- Authors: Samuel Hagele, William Gregory, Yuan Shi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21153v1  pdf=https://arxiv.org/pdf/2609.21153v1.pdf

Abstract:
The linear advection operator is an ubiquitous building block in fluid and plasma problems. We develop a quantum algorithm for enacting the operator. When the advection velocity is constant in space, our algorithm is exponentially more efficient per time step than classical and avoids spurious oscillations near steep gradients. The algorithm is most cleanly illustrated using the one-dimensional advection equation on a uniform spatial grid with periodic boundary conditions, which can be extended to higher dimensions. The algorithm uses a first-order upwind scheme, which captures discontinuities in the wave envelope but is not unitary. We embed the non-unitary upwind scheme using Linear Combinations of Unitaries (LCUs), and develop an efficient quantum gate decomposition of the upwind unitary, which performs one step of advection using $O(n^2)$ two-qubit gates, where $N=2^n$ is the number of spatial grid points, as opposed to a classical computer which costs $O(N)$. Although LCUs introduces a small bounded probability of failure per time step, we show that the accumulation of failures does not lead to exponential-in-time complexity as one would naively expect. Moreover, when LCUs fails, we develop a probabilistic scheme to recover from the failure state, which avoids a full restart of the simulation. The failure recovery scheme uses quantum Fourier transform (QFT) and effectively achieves quantum indefinite integration of an unknown quantum state. The recovery, which can itself fail, is more efficient than a full restart if the wave envelop is well-resolved to include only low Fourier modes. We emulate our scheme classically and demonstrate small problems on Quantinuum's trapped-ion qubits. Our quantum algorithm provides a subroutine for physics simulations that involve linear advection.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21209v1
- Title: Multiscale Schmidt-Spectrum Bounds for High-Dimensional Entanglement: Geometric Measures and Schmidt-Number Witnesses
- Authors: Liang Xiong, Zhixiang Jin, Yanling Wang, Wei Chen, Hong Tao, Nung-sing Sze
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21209v1  pdf=https://arxiv.org/pdf/2609.21209v1.pdf

Abstract:
High-dimensional bipartite entanglement depends on how probability is distributed across the Schmidt spectrum, whereas a single reference-state fidelity resolves only one spectral scale. We develop multiscale Schmidt-spectrum bounds that connect geometric measures with quantitative Schmidt-number witnesses. For any partition of a pure-state Schmidt spectrum, several nested Vidal tails determine block masses. We derive the sharp upper boundary of the associated normalized nuclear-norm coordinate and show that equality holds if and only if the spectrum is uniform within each block. Refining the partition gives a monotone hierarchy of tighter bounds whenever the added tail data distinguish unequal block means. We also solve a relaxed weighted multiscale optimization globally: one scalar parameter specifies its unique full-support optimizer and explicit value on the nontrivial branch. Using the established single-tail fidelity--resource curve as a baseline, we obtain exact-fidelity equality refinements, convex-roof lower bounds for mixed states, and quantitative calibrations of Schmidt-number witnesses. A higher-tail relation further bounds convex-roof extended negativity in terms of Vidal tails and identifies the pure-state equality spectra. Leakage-aware and joint-confidence formulations state how these bounds can be used with incomplete data. Multistep tails require block-resolved or independently certified spectral information; they are not determined by one projector expectation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21237v1
- Title: Unconditional quantum advantage from a two-round CHSH problem in one dimension
- Authors: Yonghae Lee, Jeonghyeon Shin, Soojoon Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21237v1  pdf=https://arxiv.org/pdf/2609.21237v1.pdf

Abstract:
We introduce a relation problem constructed from the Clauser--Horne--Shimony--Holt (CHSH) game, which we call the two-round one-dimensional CHSH problem. Its two-round structure ensures that the CHSH questions are supplied only after the relevant Pauli-frame data have been fixed, thereby ruling out a simple classical strategy that solves the corresponding problem perfectly when all inputs are supplied simultaneously. We construct a quantum circuit on $2N$ qubits that uses only adjacent two-qubit gates, has operational depth at most eight, and achieves the optimal quantum success probability of CHSH, which is strictly smaller than one. We prove that, for every fixed $0\leqδ<(\sqrt{2}-1)/4$, any randomized classical circuit with fixed wiring and bounded gate fan-in that achieves an average success probability of at least $(2+\sqrt{2})/4-δ$ requires depth $Ω(\log N)$ after the questions of the second round are supplied. This yields an unconditional separation even though the quantum circuit is restricted to a one-dimensional geometry, whereas the classical circuit has no geometric locality restriction. The result shows that perfect quantum success is not necessary for unconditional quantum advantage with shallow circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21243v1
- Title: From Trainability Diagnostics to Optimization Claims: Boundaries and Controls in Variational Quantum Optimization
- Authors: Pilsung Kang
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2609.21243v1  pdf=https://arxiv.org/pdf/2609.21243v1.pdf

Abstract:
Barren plateau diagnostics characterize whether gradient signal remains available for training, but surviving signal need not translate into successful optimization. We study this trainability--optimization gap at the level of optimizer steps. Treating coefficient-weighted Hamiltonian-term gradients as task-like components, we introduce step-level diagnostics and derive an exact bridge between signed termwise organization, directional activity, and first-order descent. Resolving this bridge into standard first-order geometry shows that the apparent organization--activity factors are not independent optimization axes and that, at fixed state and update norm, the raw gradient maximizes first-order descent of the summed objective. We compare vanilla gradient descent, a deterministic Hamiltonian-term PCGrad variant, and probe-gated LSO-PCGrad on transverse-field Ising model instances with hardware-efficient and Hamiltonian variational ansatzes, together with matched controls for update norm and probe budget. Blind projection can improve an organization diagnostic while worsening final energy and first-order predictability. After conditioning on standard first-order geometry, residual term-space composition shows no reproducible material incremental association with realized descent, while optimizer-relative update norm shows positive material associations in some settings without cross-regime reproducibility. Matched controls provide no resolved final-energy benefit attributable to the projected direction, and the improvement of LSO-PCGrad is more consistent with probe-based search and step-norm adaptation than with Hamiltonian-term projection itself. These results show that gradient-structure diagnostics can characterize trainability and update geometry without serving as standalone evidence of optimization benefit, which requires controls matched on update norm and search budget.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21249v1
- Title: The Pinnacle Architecture with fixed connectivity of degree eight
- Authors: Paul Webster, Tom Peham, Lawrence Z. Cohen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21249v1  pdf=https://arxiv.org/pdf/2609.21249v1.pdf

Abstract:
We show how the Pinnacle architecture can be adapted to be compatible with superconducting qubits, where the connectivity between qubits must be fixed at fabrication. Specifically, we present a modified instantiation of the architecture that has fixed connectivity degree of eight. With this instantiation, we show that a 2048-bit RSA integer can be factored in one month with approximately 120 000 physical qubits, given a physical error rate of $10^{-3}$, code cycle time of 1 microsecond and reaction time of 10 microseconds.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21260v1
- Title: Pair density Shannon information measures and their $N$-dependent behaviour in diatomic molecular systems
- Authors: Saul J. C. Salazar, J. Antonio Zarate, J. M. Solano-Altamirano, Humberto G. Laguna, Julio M. Hernandez-Perez, Robin P. Sagar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21260v1  pdf=https://arxiv.org/pdf/2609.21260v1.pdf

Abstract:
Pair density Shannon entropies and mutual information in position and in momentum space are calculated for two series of homonuclear and heteronuclear diatomic molecules using Hartree-Fock wave functions. The pair density entropy sum increases with the quality of the basis set. Mutual information, a measure of statistical correlation, is seen to be smaller in momentum space as compared to position space. The interpretation is that the momentum pair density is closer than the position pair density to a Hartree-like reference. The $N$-dependent behaviours of the entropy and mutual information sums are examined by fitting the data to three different model behaviours. Results show that these models are capable of representing the molecular data in differing degrees. The parameters obtained from a particular model are relatively constant across different chemical series. This adds evidence to the argument of a universal $N$-dependent behaviour of the entropy sums.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21310v1
- Title: Commutator Geometry and Information Preservation in the Quantum Switch
- Authors: Xu Chen, Xue Ma
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21310v1  pdf=https://arxiv.org/pdf/2609.21310v1.pdf

Abstract:
Two commuting channels yield the same composite channel in either fixed order, yet their quantum switch can alter information preservation. We study how this effect depends on the input state, retaining the joint output of the control and target. Exact Kraus commutator identities determine overlap and squared fidelity gaps. Fixed order preserves product inputs at least as well as the switch in fidelity. The reverse inequality holds for pure states of two qubits whose control Schmidt basis can be chosen to coincide with the order basis. A commutator matrix determines the target basis that maximizes the squared fidelity gap at fixed entanglement within this aligned family. For Pauli $X$ and $Y$ channels with equal error probabilities, the switch replaces a logical phase flip with an operator that stabilizes a joint code. At fixed noise, the switch preserves at least as much distinguishability and quantum Fisher information as fixed order for every state family in this code. For the pure encoded family studied here, exact formulas connect the phase information gain to the squared fidelity gap and quantify the reduction in information about the noise probability. Optimizing the probes yields equal maximal quantum Fisher information for noise estimation under both joint channels. These results connect commutator geometry and logical error structure to state preservation and the retention of encoded information.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21355v1
- Title: Weighted Berry curvature and global geometry of mixed quantum states
- Authors: Dominik Kuczyński, Erik Sjöqvist
- Categories: quant-ph (primary); quant-ph; cond-mat.other
- Links: abs=https://arxiv.org/abs/2609.21355v1  pdf=https://arxiv.org/pdf/2609.21355v1.pdf

Abstract:
We examine the geometric interpretation of the quantum geometric tensor proposed in [Phys. Rev. B {\bf 110}, 035404 (2024)] for mixed quantum states, focusing on its imaginary part, which is proportional to a weighted sum of the Berry curvatures of the eigenstates of the density operator. While the real part naturally decomposes into Fisher--Rao and weighted Fubini--Study contributions, we show that the imaginary part does not, in general, coincide with the curvature of a connection on a globally defined U(1) line bundle whose holonomy yields a mixed-state geometric phase. Using a two-level system as an explicit example, we demonstrate that its surface integral depends on the choice of surface bounded by the same closed path, with ambiguities that are not integer multiples of $2π$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21373v1
- Title: Passive Pauli Toggling of Polarization Qubits in Optical Fibers: Error Bounds and QKD Performance
- Authors: Bongjune Kim, Jeongho Bang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21373v1  pdf=https://arxiv.org/pdf/2609.21373v1.pdf

Abstract:
Polarization qubits offer a direct route to fiber-based quantum communication, yet the fiber that carries them also scrambles their reference frame through uncontrolled birefringence. Active compensation commonly relies on monitoring and feedback, raising a natural question: can the link itself suppress coherent polarization drift before it reaches the receiver? We show that it can within a regime of sufficiently correlated unitary drift. Our central idea is to embed a fixed cyclic sequence of Pauli rotations along the fiber, turning propagation distance into a spatial toggling frame. Rather than estimating and inverting the unknown transformation, the sequence repeatedly reverses its leading action. We establish exact refocusing for constant generators compatible with a two-segment echo, show that a four-frame Pauli cell cancels the leading contribution of any traceless quasi-static generator, and bound the residual error for smoothly varying birefringence. We then connect these guarantees to operational BB84 quantities, including measured QBERs, the resulting secret fraction, and insertion loss. In simulations of a 50 km fiber with spatially correlated birefringence, a representative design reduces the mean QBER from 6.11% to 0.224% at a device spacing of 1.25 km. With an assumed per-device transmission of t = 0.997, this raises the asymptotic key rate per launched pulse by a factor of approximately 2.5. For this parameter set, the best design in the tested scan is not the densest one: error suppression and optical loss create a finite operating window. These results provide a loss-aware design principle for passive polarization stabilization and suggest a low-overhead complement to active tracking in polarization-encoded QKD networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21376v1
- Title: Denser Planar Color Codes
- Authors: Noah Shutty
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21376v1  pdf=https://arxiv.org/pdf/2609.21376v1.pdf

Abstract:
We consider the 4.8.8 color code in a brickwork layout on the square lattice with nearest-neighbor gates. We identify periodic superdense circuits with twelve CNOT layers that appear to preserve the full distance of these codes. Including ancillas, the family uses $q=(2d^2+5d-5)/2$ physical qubits for distance $d$: asymptotically $2/3$ as many as the triangular 6.6.6 color code and $1/2$ as many as the rotated surface code at the same code distance. Circuit-level simulations targeting superconducting architectures demonstrate favorable scaling of 4.8.8 color codes at plausible physical noise rates, including both for planar codes and their toroidal cousins under periodic boundary conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21380v1
- Title: A memory-information window in finite-duration quantum control
- Authors: Doyeol, Ahn
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21380v1  pdf=https://arxiv.org/pdf/2609.21380v1.pdf

Abstract:
Environmental noise is a major source of decoherence and errors in quantum systems. In a non-Markovian environment, the noise has a finite correlation time, and the system can retain information about its previous interactions with the environment. Here, we investigate how such environmental memory can be observed through a finite-duration coherent quantum operation. Coherent control dynamically reshapes the stochastic coupling operator and thereby changes how two-time noise correlations affect the quantum process. For Ornstein-Uhlenbeck noise, we show analytically that two different limits reduce the information on the correlation time. In the short-memory limit, the leading dynamics depend on the integrated-noise combination σ/τc, where σ is the noise variance and τc is the correlation time, making these parameters locally degenerate. In the long-memory limit, the stochastic field becomes quasi-static during the operation, and sensitivity to the correlation time is suppressed. Exact stochastic simulations for a driven single-qubit Xπ rotation and a two-qubit exchange gate show that independent correlation-time information becomes largest between these limits, when the environmental and control timescales are comparable. Noncommuting controls enhance this information, whereas commuting controls do not. Simulations at different gate durations tg further show that the information window approximately follows the dimensionless correlation ratio τc/tg. These results provide a timescale-matching principle for probing finite-correlation non-Markovian noise with coherent quantum control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21418v1
- Title: Ultimate Information Rate for Quantum Sensing under Multilevel Relaxation
- Authors: Changhun Oh, Seok Hyung Lie, Youngrong Lim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21418v1  pdf=https://arxiv.org/pdf/2609.21418v1.pdf

Abstract:
We determine the ultimate information rate of a relaxing multilevel quantum sensor under unrestricted adaptive control and construct an explicit strategy that attains it. We consider sensing a weak field that couples the ground state to several excited states that decay back to the ground state, a setting that reduces to amplitude-damping sensing for a single excited state. We show that the ultimate information rate is exactly the mean population lifetime of the bright state coupled to the ground state by the signal. Although the sensing dynamics generally involve several decay modes, an explicit rank-one protocol that monitors the ground--bright coherence using fresh meters and classical feedback attains this rate while keeping its finite-time information deficit bounded by a constant. For independently relaxing identical sensors, independent local monitoring attains the sum of their individual optimal rates, so intersensor entanglement and joint quantum error correction cannot increase the asymptotic rate. Consequently, the free population-decay curve provides an operational measure of the optimal sensing performance under arbitrary adaptive control.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21428v1
- Title: Polariton Bell Node for Quantum Repeaters
- Authors: Junhui Cao, Alexey Kavokin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21428v1  pdf=https://arxiv.org/pdf/2609.21428v1.pdf

Abstract:
We propose a Bell-measurement node for quantum repeaters based on a planar semiconductor microcavity operating in the strong-coupling regime. Cavity photons hybridize with quantum-well excitons to form polaritons combining properties of photons and matter quasiparticles. A control photon loaded into one polariton mode changes the polarization response seen by a subsequently incident target photon. This conditional rotation is governed by the interplay of self-induced Larmor precession triggered by spin-dependent exciton-exciton interactions and the polarization beats caused by the splitting of transverse-electric and transverse-magnetic cavity modes. We identify conditions of the experiment that enable implementation of a controlled-Z gate and allow to distinguish all four Bell states in the ideal limit. The one-sided scattering scheme provides a lower interaction threshold than a scalar Kerr reference under the same assumptions. At a selected operating point, the bandwidth-induced identification error scales as the fourth power of the pulse bandwidth in the narrow-band limit. An additional fixed input rotation reduces this error even further. We describe the entanglement swapping between remote memories and determine the minimum quality of the elementary links needed to obtain an entangled output.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21463v1
- Title: Quantum Loads and the Generalized Telegrapher's Problem
- Authors: E. Collin, A. Delattre
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21463v1  pdf=https://arxiv.org/pdf/2609.21463v1.pdf

Abstract:
We report on the mapping of classical microwave transmission line theory onto the quantum scattering matrix description. By means of a generalized flux formalism a la Devoret, we derive a charge-current vector living on the confining electrodes, to which a Hodge-like decomposition is applied. The presented theory holds equally well for all types of waves traveling within Cartesian and cylindrical guide geometries (the usual Transverse Electric Magnetic, but also Transverse Magnetic and Transverse Electric ones). We then demonstrate how a generic load decomposes into a series of complex coefficients $Z_{load}(α)$, for each mode $α$ propagating along the line. This decomposition leads to a particular classification of traveling waves: gradient-type and curl-type charge-currents. This distinction shines a new light on a broken gauge symmetry exhibited by a class of Transverse Electric modes. Our results provide a universal theoretical framework, which finds a direct usage in microwave-based quantum information transfer.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21501v1
- Title: Optimal control for duty-cycle-limited interferometry with single-NV centers
- Authors: Ugur Tamer, Sina Zeytinoglu, Ozgur E. Mustecaplioglu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21501v1  pdf=https://arxiv.org/pdf/2609.21501v1.pdf

Abstract:
Stimulus-responsive hydrogels convert temperature changes into magnetic-field shifts detectable by nitrogen-vacancy (NV) centers, enabling nanoscale thermometry in soft and biological environments. Existing hydrogel-nanodiamond demonstrations rely on NV ensembles, whose high photon throughput is accompanied by gradient-induced inhomogeneous broadening, while idealized single-NV projections assume high-fluence fluorescence/ODMR readout. Here we study a pulsed single-NV route for the same class of sensors and ask whether decoherence-aware coherent control can improve thermometric performance over optimized Ramsey interrogation at equal detected-photon budget. Using a sigmoidal volume-phase-transition model, dipolar magnetic transduction, and Lindblad master-equation simulations, we find a reproducible 25-27% per-shot sensitivity gain over optimized Ramsey, i.e., a 57-60% gain in Fisher information (1.57-1.60). The same gain carries over to the photon-normalized Fisher information. The rate gain is governed by the measurement duty cycle, the fraction of the experimental cycle spent accumulating signal rather than initializing, reading out or waiting, and becomes largest when the overhead or optical-dose constraint dominates the cycle time. The optimized trajectories reveal a response-shaping mechanism in which phase accumulation is concentrated near the end of the sequence, and a closed-form depth-two solution reproduces the numerical optimum and exhibits that mechanism analytically. The advantage is most pronounced when the dephasing time is short compared with the measurement overhead or dose-limited waiting time, which is the operating regime targeted by hydrogel-transduced single-spin biosensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21558v1
- Title: Quantum states with the same entanglement and local unitary equivalence
- Authors: Julio I. de Vicente
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21558v1  pdf=https://arxiv.org/pdf/2609.21558v1.pdf

Abstract:
Local operations assisted by classical communication (LOCC) play a fundamental role in the resource-theoretic formulation of entanglement theory inducing an operationally meaningful ordering in the set of entangled states. The particular class within LOCC of local unitary (LU) transformations is obviously closed under inversion. Thus, LU-equivalent states are interconvertible by LOCC and have therefore the same entanglement. For this reason LU-equivalence has been thoroughly studied in the context of entanglement theory. However, as I note here with a simple example, the converse is not true: there exist entangled states that are interconvertible by LOCC but which are not LU-equivalent. This motivates studying under which conditions LOCC interconvertibility is characterized by LU-equivalence. I provide a sufficient condition for this to hold. When one considers multipartite states with full entanglement dimensionality (as quantified by the Schmidt number vector) LOCC interconvertibility can only hold under LU-equivalence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21560v1
- Title: Giant-Atom-Induced High-Order Output Zeros in a Coupled-Cavity Array
- Authors: Mengxue Li, Bo Liu, H. Z. Shen, H. D. Liu, Gangcheng Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21560v1  pdf=https://arxiv.org/pdf/2609.21560v1.pdf

Abstract:
Coherent perfect absorption, zero transmission and zero reflection are several scattering phenomena governed by interference engineering in Hermitian and non-Hermitian systems. Higher-order coherent perfect absorption can significantly broaden the absorption bandwidth, while existing implementations rely on scattering zero degeneracy induced by exceptional points or additional momentum-dependent phase delays introduced in incident waves. We propose a scheme where a giant atom couples to a one-dimensional coupled-cavity array at two spatially separated sites. The spatially separated coupling configuration of the giant atom generates tunable nonlocal interference phases that dominate the scattering interference process. We further investigate the zero-reflection and zero-transmission behaviors under single-sided incidence. Remarkably, we find that for certain parameter choices, zero transmission can persist over the entire propagating band, rather than being restricted to a single momentum. Our results reveal that the giant-atom interference mechanism enables bandwidth-enhanced coherent perfect absorption and bandwidth-enhanced zero transmission in the absence of exceptional points and incident momentum-dependent phase delays. Our work provides a physical route for coherent wave manipulation in coupled-cavity quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21567v1
- Title: Weighted Quantum Signal Processing: Low-Depth Polynomial Approximation with Applications to Kolmogorov-Arnold Networks
- Authors: Rohit Sarma Sarkar, Rupayan Bhattacharjee, Elias F. Combarro, Michele Grossi, Lirandë Pira, Carmen G. Almudéver, Sergi Abadal, Eduard Alarcon
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.LG
- Links: abs=https://arxiv.org/abs/2609.21567v1  pdf=https://arxiv.org/pdf/2609.21567v1.pdf

Abstract:
Quantum Signal Processing is a powerful quantum framework for generating and approximating univariate polynomials. However, QSP is often limited by circuit-depth bottlenecks and parity constraints on the class of realizable polynomials. In this work, we introduce Weighted Quantum Signal Processing, an extension of QSP in which a weight function is assigned to the central rotation operator. This formulation provides a deeper understanding of QSP, which emerges as the special case of WQSP with unit weights. The choice of weights determines the structure and expressive capabilities of WQSP circuits. When the weights are natural numbers greater than one, WQSP reduces to a pruned version of QSP, revealing parameter redundancies in the standard framework. Through appropriate selection of integer weights, WQSP achieves linear-to-exponential reductions in the number of parameters required to realize arbitrary bounded univariate polynomials while preserving approximation quality. For generic weights, we establish corresponding approximation error bounds and show that, in many cases, the approximation is exact. We analyze WQSP from both a deterministic perspective, where polynomial generation is formulated as the solution of a linear system, and a quantum machine learning perspective, where WQSP serves as a structured and expressive quantum learning model. We further employ this learning framework to parameterize learnable activation functions in Kolmogorov--Arnold Networks for multivariate function approximation. Our results show that WQSP provides a compact, flexible, and theoretically grounded framework for realizing arbitrary univariate polynomials while requiring significantly fewer trainable parameters than conventional QSP. This yields expressive and parameter-efficient neural architectures, highlighting the potential of WQSP as a scalable primitive for quantum-enhanced machine learning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21579v1
- Title: Global Entanglement Quantification via Classical Shadows
- Authors: João P. Engster, Eduardo I. Duzzioni
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21579v1  pdf=https://arxiv.org/pdf/2609.21579v1.pdf

Abstract:
Detecting and characterizing quantum correlations are tasks of great relevance in quantum information. More specifically, quantifying the amount of multipartite entanglement is a known difficult task, even for pure states. To this end, several entanglement measures have been proposed, although there is currently no universal manner to do so. In this work, we propose the classical shadows technique to measure the generalized global entanglement introduced in Phys. Rev. A 74, 022314. This particular multipartite entanglement quantifier $E_G^{(n)}$ relies on the linear entropies of all $n$-qubit partitions of a state. As the linear entropy can be written in terms of a complete set of observables of the subsystem, we employ classical shadows to estimate many observables with fewer measurements. We simulate the quantification of $E_G^{(n)}$ for well-known entangled states and for random states, comparing shadow estimations and grouping techniques. Our results show a clear advantage of classical shadows over direct estimation approaches, indicating that it can be a useful tool to quantify entanglement without the need to reconstruct the density operator of the whole system.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21598v1
- Title: Experimental Measurement and Theoretical Analysis of Energy Relaxation Rates of an Interacting Two-Qubit System on a D-Wave Quantum Annealer
- Authors: Yusei Amano, Sorato Suzuki, Hiroki Kuji, Tetsuro Nikuni, Takashi Imoto, Yuichiro Matsuzaki
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21598v1  pdf=https://arxiv.org/pdf/2609.21598v1.pdf

Abstract:
In D-Wave quantum annealers, various properties of the ground state have been clarified, whereas the correspondence between theory and experiment for energy relaxation rates in multiqubit excited states remains insufficiently understood. Here, we measured the energy relaxation rates of the first excited states in single-qubit systems and interacting two-qubit systems using a D-Wave quantum annealer. We analyzed the measured relaxation rates using a Gorini-Kossakowski-Sudarshan-Lindblad master equation with independent local $σ^{\,\,z}$-type noise channels. The calculated relaxation rates reproduced the overall trends observed experimentally, supporting the model at a qualitative level. We then used the relaxation rates measured for the uncoupled single-qubit systems to calibrate the local relaxation parameters and predict the relaxation rates of the interacting two-qubit systems. The predicted rates remained within a factor of approximately four of the measured rates. These results show that the relaxation measurements on individual qubits can provide a practical estimate of relaxation in small interacting quantum systems and may help clarify relaxation mechanisms in programmable quantum annealers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21625v1
- Title: Semiclassical Arrhenius law for quantum-thermal escape rates
- Authors: Luca Salasnich, Cesare Vianello
- Categories: quant-ph (primary); quant-ph; cond-mat.other; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2609.21625v1  pdf=https://arxiv.org/pdf/2609.21625v1.pdf

Abstract:
The quantum-thermal escape rate from a metastable well in the absence of dissipation is customarily written as a Boltzmann average of the Hill-Wheeler flux over a continuum of energies. However, this continuum treatment diverges exponentially at low temperature. The divergence originates in a mismatch between a quantum partition function and a classical flux integral; retaining the discrete nature of the quasibound spectrum removes it exactly, and the resulting semiclassical Arrhenius law is obtained in closed form on both sides of the crossover temperature. Evaluating a uniform Kemble transmission probability on Bohr-Sommerfeld levels further recovers the standard WKB decay rate of the lowest resonance at zero temperature. Benchmarked against the resonances of cubic and quintic potentials, obtained by complex scaling, this uniform semiclassical result stays within $9\%$ of the exact rate over eleven orders of magnitude.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21640v1
- Title: Time rescaling for second-order feedback-based quantum optimization
- Authors: Leticia Bertuzzi, João P. Engster, Evandro C. R. da Rosa, Eduardo I. Duzzioni
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21640v1  pdf=https://arxiv.org/pdf/2609.21640v1.pdf

Abstract:
Feedback-based quantum algorithms recently gained attention by demonstrating how quantum computers can be used to solve optimization problems without resorting to hybrid quantum-classical architectures. Recent progress made with Feedback-based Algorithm for Quantum Optimization (FALQON) variants significantly reduced the depth of the required circuits. In this work, we merge the time-rescaled and second-order FALQON variants into a unified framework. The results show an important improvement over past modifications, reducing circuit depth and allowing a more flexible choice of time-steps, while maintaining stable solutions. This FALQON variant makes it suitable for the NISQ era.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21741v1
- Title: Floquet physics from quantized light-matter interaction: geometric phases, gauge consistency, and entanglement
- Authors: Beatriz Pérez-González, Sigmund Kohler, Mónica Benito
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2609.21741v1  pdf=https://arxiv.org/pdf/2609.21741v1.pdf

Abstract:
Floquet engineering and cavity quantum electrodynamics represent two complementary descriptions of light-matter interaction, yet their precise connection beyond the small-coupling regime remains subtle. Here, by representing the cavity field in a large-photon-number phase basis, we show that the time-dependent Schrödinger equation of a classically driven system emerges directly from the fully quantized problem, without replacing the field by a classical trajectory or assuming a mean-field decoupling. This establishes a one-to-one correspondence between quasienergies and photon-sector-shifted quantum energies, while providing a direct quantum interpretation of the Floquet mean energy and Anandan phase. Because gauge invariance is exactly preserved at the level of the quantum Hamiltonian, the quantum-to-classical correspondence remains valid beyond perturbative and small-coupling regimes. We further show that light--matter entanglement is encoded in matter--harmonic correlations of the corresponding Floquet mode, thus identifying a semiclassical limit in which Floquet physics emerges without requiring the quantum field itself to approach a coherent classical state.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21776v1
- Title: Intrinsic Vectorial Gradiometry via Quantum Control of a Spin-based Sensor
- Authors: Jaime García Oliván, Pablo Acedo, Oliver T. Whaites, Jorge Casanova
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21776v1  pdf=https://arxiv.org/pdf/2609.21776v1.pdf

Abstract:
Gradiometry provides a versatile alternative to passive environmental shielding in quasi-static magnetometry, effectively suppressing background noise through differential signal extraction. Nevertheless, traditional implementations rely on multi-sensor architectures restricted to spatial gradients, where subtracting signals from independent detectors involves imperfect suppression of common-mode noise and artifacts, limiting their sensitivity. To overcome these limitations, we introduce a quantum control sequence that enables intrinsic temporal and spatial vectorial gradiometry of magnetic fields using a single quantum sensor. Our method provides direct access to first and higher-order derivatives of the magnetic field and extended applicability via auxiliary nuclear spin memory. We showcase this protocol on an ensemble of nitrogen-vacancy (NV) centers in diamond and combine it with mechanical control to realize high-precision differential sensing. Through detailed numerical simulations, we demonstrate the performance of our scheme in two critical DC magnetometry applications: (i) vector magnetic anomaly detection and (ii) non-invasive gradiometry of neuronal action potentials.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21796v1
- Title: Parameter-Decoupled Quantum Superresolution without Multiparameter Estimation
- Authors: X. -F. Qian
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2609.21796v1  pdf=https://arxiv.org/pdf/2609.21796v1.pdf

Abstract:
Quantum superresolution promises to resolve closely spaced sources beyond the diffraction limit, but existing approaches generally rely on idealized source properties or require simultaneous estimation of multiple coupled parameters of realistic sources. Here we introduce a parameter-decoupled measurement that determines the separation of realistic passive sources without estimating their unknown brightness imbalance, mutual coherence, or relative phase. A complete four-parameter quantum Fisher information analysis identifies the separation information that remains accessible in the presence of these nuisance parameters. We then construct a directly measurable log-probability invariant from projection channels whose conditional statistics depend only on the separation. Broad classes of channel pairs satisfy the resulting decoupling condition. For a Gaussian point-spread function, the lowest-order implementation asymptotically attains the four-parameter quantum limit per incident signal in the sub-Rayleigh regime. This approach converts a realistic multiparameter imaging problem into an operationally single-parameter measurement, providing a practical route toward quantum-enhanced resolution of passive spatial, temporal, and spectral signals.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21846v1
- Title: Sine-Gordon Model with Bosonic Tensor Networks: Continuum Matching and Soliton Scattering
- Authors: Florian Hechenberger, Tommaso Rainaldi, Felix Ringer
- Categories: quant-ph (primary); quant-ph; hep-ph; hep-th; nucl-th
- Links: abs=https://arxiv.org/abs/2609.21846v1  pdf=https://arxiv.org/pdf/2609.21846v1.pdf

Abstract:
We use bosonic tensor networks to connect the lattice sine-Gordon model in the Hamiltonian formulation quantitatively to its continuum theory. Matching the lattice vertex operator to its conformal normalization at the free-boson ultraviolet fixed point yields the exact relation between the bare lattice coupling and the renormalized continuum mass parameter. The soliton mass then approaches Zamolodchikov's exact continuum prediction throughout the studied parameter range, without adjustable parameters. Using uniform matrix product states and a quasiparticle ansatz, we also recover the relativistic soliton dispersion and the two lightest breather masses at the percent level. We simulate real-time collisions of Gaussian soliton-antisoliton wave packets near a reflectionless point and extract the Wigner spatial displacement. We compare this displacement with the exact continuum prediction obtained from the momentum derivative of the transmission phase, recovering its characteristic rapidity dependence. Our bosonic simulations provide a foundation for nonintegrable extensions, offer lessons for renormalization in other Hamiltonian lattice field theories, including gauge theories, and provide benchmarks for continuous-variable quantum simulations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21875v1
- Title: Uhlmann Geometry of Fixed-Rank Density Matrices: A Fiber-Bundle Approach
- Authors: Xu-Yang Hou, Hao Guo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21875v1  pdf=https://arxiv.org/pdf/2609.21875v1.pdf

Abstract:
For full-rank density matrices the state space is contractible, the Uhlmann bundle is topologically trivial, and the holonomy admits no quantized invariants; although the Uhlmann phase is genuinely geometric, this topological poverty has kept it from serving as a robust physical diagnostic of mixed-state matter. Mixed states of fixed rank below the Hilbert-space dimension, however, are ubiquitous: reduced states of subsystems, states in an invariant sector, and states in a decoherence-free subspace all have a support smaller than the Hilbert space that can vary with parameters. Their geometry is far richer: the support carries genuine curvature, non-Abelian holonomy, and Chern topology. We formulate Uhlmann's theory directly on the manifold of rank-$k$ density matrices: minimal purifications make the fixed-rank stratum the base of a principal $U(k)$-bundle whose Uhlmann connection is uniquely determined by a Sylvester equation, and in an eigenframe this connection takes a closed form reducing to the Berry, Wilczek--Zee, and faithful Uhlmann connections at $k=1$, at equal weights, and at $k=N$. The fixed-rank bundle inherits the topology of the Grassmannian, and non-factorizable higher Chern topology requires failure of the global eigenline splitting, which in the present spectral setting requires degeneracy, minimally realized by a rank-2 Yang monopole whose quantized second Chern number links the geometry to the four-dimensional quantum Hall response. Solvable models, from a genuinely non-Abelian holonomy to a decoherence-free Lindblad orbit, illustrate the content: the supporting subspace carries the topology, the spectral weights shape the transport, and the Uhlmann phase provides a direct geometric signature of these mixed-state phase transitions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21886v1
- Title: Ensemble Dependence of the Critical Exponent at a Quantum Error Correction Threshold
- Authors: Idan Dror, Moshe Goldstein
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21886v1  pdf=https://arxiv.org/pdf/2609.21886v1.pdf

Abstract:
In thermodynamics it is common to assume that the choice of ensemble (e.g., micro-canonical, canonical, or grand-canonical) should not affect the underlying physics in the thermodynamics limit. We show that this does not necessarily hold for critical exponents. Examining a simplified model of quantum error correction (single step encoding and decoding by a random unitary) and the behavior of both the fidelity and magic at the corresponding threshold, we find different exponents when using generic channels or supposedly equivalent quantum trajectories. Interestingly, the obtained exponents saturate a recently derived information theoretic bound by Feldman et al. (2026), which we extend from the grand-canonical to the canonical case, including intermediate ensembles which we define. Moreover, even the existence of the transition is shown to be ensemble-dependent.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21900v1
- Title: The Quantum KKL Inequality
- Authors: Yong Jiao, Wenlong Lin, Sijie Luo, Dejian Zhou
- Categories: quant-ph (primary); quant-ph; math.FA
- Links: abs=https://arxiv.org/abs/2609.21900v1  pdf=https://arxiv.org/pdf/2609.21900v1.pdf

Abstract:
In this paper, we resolve the quantum KKL conjecture of Montanaro and Osborne \cite{MO2010} for quantum Boolean functions on the $n$-qubit hypercube. More precisely, for every self-adjoint unitary $T$, we bound the largest $L_2$-influence from below by a constant multiple of $\mathrm{Var}(T)\log(n)/n$. The proof heavily depends on upper and lower commutator estimates on the Hilbert space.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21916v1
- Title: Asymptotics for Frequency Redundancies in Quantum Machine Learning Models
- Authors: Felix Paul, Bhilahari Jeevanesan, Peter Jung
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.21916v1  pdf=https://arxiv.org/pdf/2609.21916v1.pdf

Abstract:
The redundancy distribution of the frequency spectrum has been shown in the literature to impact the expressivity and trainability of Quantum Fourier Models (QFMs). In this work, we address the question of how this redundancy spectrum is shaped by the choice of eigenvalues of the data re-uploading Hamiltonians, using a simple mathematical formalism based on generating functions. We derive exact and asymptotic redundancy profiles for several structured eigenvalue choices identical for every layer, including arithmetic progressions and single-qubit Pauli encodings, and show that both approach a Gaussian profile as the number of layers grows. We then show that this Gaussian limit is not specific to these constructions but is a generic feature of QFMs built from integer eigenvalues that are identical in every layer. These results can be tied to the central limit theorem for random walks. These results clarify why generic or unstructured encoding choices give rise to a redundancy bias that favours low frequencies, highlighting the importance of well-thought-out encoding strategies when constructing a QFM.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21944v1
- Title: Guiding Agents of Quantum Games to Equilibrium using Matrix Exponential Fixed-Point Iteration
- Authors: Alireza Habibi, Luis F. Abanto Leon, Setareh Maghsudi
- Categories: quant-ph (primary); quant-ph; cs.GT; cs.LG; cs.MA
- Links: abs=https://arxiv.org/abs/2609.21944v1  pdf=https://arxiv.org/pdf/2609.21944v1.pdf

Abstract:
In recent years, quantum game theory has gained significant attention as a framework for studying decision-making in multi-agent systems using quantum principles. However, computing equilibrium strategies is challenging because the dimension of the joint Hilbert space grows as the product of the players' local dimensions. In this paper, we consider an extended Gutoski-Watrous (EGW) game in which each player's quantum strategy is represented by a local density matrix. We derive tensor-contraction expressions for the payoff functions and their gradients, thereby avoiding the explicit construction of the full joint density matrix and its computationally expensive multiplication by the payoff operators. Building on the resulting effective Hamiltonians, we propose the Matrix Exponential Fixed-Point Iteration with Annealing (MEFPIA) algorithm to search for equilibrium points in EGW games. We compare MEFPIA with the Matrix Multiplicative Weights Update (MMWU) algorithm in terms of convergence. For the tested instances and parameter settings, both algorithms approach the same strategy profiles and payoffs, while MEFPIA achieves lower relative error in fewer iterations. These results indicate that MEFPIA is a promising numerical method for equilibrium search in multi-agent quantum games. Our findings provide important insights into the quantum game theory's potential for addressing complex decision-making processes, as well as opening up new paths for future research and exploration in multi-agent quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21961v1
- Title: Single-atom-based asynchronous photonic interconnect for scalable modular quantum computing
- Authors: Jérémy Raskop, Nadav Kandel, Yaniv Amichy, Yaron Jarach, Tal Kanonich, Andrei Militaru, Johannes Fink, Barak Dayan
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2609.21961v1  pdf=https://arxiv.org/pdf/2609.21961v1.pdf

Abstract:
Scaling quantum computation beyond the capacity of a single quantum processing unit requires quantum interconnects between modular processors. Optical photons are natural carriers for distributing entanglement between these processors. Most loss-resilient protocols use photonic Bell-state measurements based on the linear-optics type-II fusion gate. The resulting entanglement rate scales quadratically with each processor's typically low photon-delivery probability. Here we analyze a memory-assisted quantum interconnect using a near-deterministic, robust photon--atom controlled-$Z$ gate via a single atom trapped in a high-finesse cavity. Detecting and measuring a photon from one processor heralds entanglement between that processor and the atom. This entanglement is preserved while the process repeats with the second processor until the second photon is detected and measured. Reading out the atomic qubit finalizes the entanglement between the processors. As the entanglement is mediated by the atom, the photons from both processors do not need to be indistinguishable, removing a major source of infidelity. Furthermore, by removing the simultaneous photon-arrival requirement, the protocol allows the entanglement rate to scale linearly rather than quadratically with photon-arrival probability over a wide parameter range. We derive entanglement rates under realistic parameters, accounting for decay of the atom's entanglement with the first processor and for decoherence caused by unheralded photon interactions. The nanosecond-scale of the gate and read-out operations leads to orders-of-magnitude entanglement-rate gain over linear optics, removing a key bottleneck in modular quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.22002v1
- Title: Microwave dielectric properties of LiNbO$_{\mathbf{3}}$ and AlN at millikelvin temperatures and single-photon power
- Authors: Alessandro Reineri, Francesco Crisa, Akshay Murthy, Maithlee Shinde, Daniel Bafia, Changqing Wang, Tanay Roy, Alexander Romanenko, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22002v1  pdf=https://arxiv.org/pdf/2609.22002v1.pdf

Abstract:
Efficient bidirectional microwave optical photon conversion is a key capability for scaling superconducting quantum processors into distributed networks. However, achieving the necessary conversion efficiency requires filling a critical knowledge gap in understanding the loss mechanisms of electro optic materials. Here, we characterize the microwave properties of single crystal bulk LiNbO3 and AlN over a broad range of powers, down to single photon levels, and spanning from millikelvin temperatures to above 1K. We demonstrate that both materials exhibit two level systems (TLS) behavior, while piezoelectric related losses are excluded. We show that TLS induced dissipation is predominantly localized on the surface rather than being an intrinsic bulk property, a result further corroborated by room temperature 3D XPS and time of flight SIMS analyses. These findings provide useful insights to engineer hybrid architectures that integrate bulk electro optic crystals within superconducting cavities, proving that microwave quality factors compatible with high efficiency microwave optical transduction are within reach.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.22010v1
- Title: Selection rules for pinned and quasipinned occupation numbers with degeneracy
- Authors: Robin Reuvers
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22010v1  pdf=https://arxiv.org/pdf/2609.22010v1.pdf

Abstract:
When the natural occupation numbers of a fermionic state saturate a generalized Pauli constraint, the state obeys a selection rule: only those configurations of natural orbitals that saturate the constraint themselves contribute. Pinning thus singles out an active space. The selection rule was proved for non-degenerate occupation numbers; for degenerate ones it was conjectured, and proved for one saturated constraint under an unverified assumption. Here, it is proved for every generalized Pauli constraint, with no assumption, and also in the spin-adapted setting. The rule can only fail for the ordering constraints $λ_j\geλ_{j+1}$. Several saturated constraints are served by one basis whenever their common zero face contains a non-degenerate point. In practice, occupation numbers are quasipinned rather than pinned, and I show what the rule then becomes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.22025v1
- Title: Cavity-QED analysis of InAs quantum-dot single photon production
- Authors: W. W. Chow, S. Peana, D. I. Herman, K. Y. Lee, A. Cejan, C. Shang, G. Moody, J. E. Bowers, et al.
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2609.22025v1  pdf=https://arxiv.org/pdf/2609.22025v1.pdf

Abstract:
Cavity quantum electrodynamics is used to study the extent cavity enhancement affects single photon performance of an InAs quantum dot, in terms of emission rate, purity and indistinguishability at different temperatures. Parametric studies show a tradeoff between single photon production rate and purity, as well as between indistinguishability and purity. The results indicate the importance of quantum carrier-photon correlations that yield substantial corrections to mean-field treatments, especially at high light-matter coupling strength, where cavity enhancement is most effective.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.22046v1
- Title: Persistent Quantum-Enhanced Frequency Sensing with T^{-3/2} Scaling
- Authors: Clayton Z. C. Ho, Hao Wu, Grant D. Mitts, Joshua A. Rabinowitz, Eric R. Hudson
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2609.22046v1  pdf=https://arxiv.org/pdf/2609.22046v1.pdf

Abstract:
Quantum sensing uses nonclassical states to improve measurement sensitivity, but the same states that provide metrological gain also decohere more rapidly. This limits the usable interrogation time and, in practice, often precludes improvement in ultimate sensitivity - realized useful quantum advantage has consequently remained rare. Here, we restore persistent quantum advantage by embedding Fock-state enhancement within a quantum heterodyne (Qdyne) protocol, decoupling sensitivity from the decoherence-limited interrogation time τ. Measurements are acquired at short τ where the quantum-enhanced gain is optimal, while precision accumulates with the total measurement time. Demonstrated on the motional mode of a trapped 40Ca+ ion, we observe quantum-enhanced precision that persists to measurement times seven orders of magnitude beyond the dephasing limit, scaling as T^{-3/2} with no indication of saturation. Using the n=3 Fock state, we reach a frequency precision of 0.5uHz relative to an 86MHz carrier, achieving a fractional precision ~6x10^{-15}. This represents a quantum-enhanced gain of 7.1(10) dB over the n=0 state, in agreement with Fisher information predictions. This is the first demonstration of Qdyne beyond solid-state spin-defects. Further, by using the quantum harmonic oscillator to perform frequency mixing, we extend operation beyond 1GHz, two orders of magnitude above the ceiling of pulsed dynamical-decoupling implementations. These results recover quantum advantage at the long timescales required to improve ultimate sensitivity, with direct implications for nanoscale NMR and quantum logic spectroscopy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.22047v1
- Title: Asymmetric quantum cloning on orthogonal orbits and four-mode fermionic states
- Authors: Piotr Ćwikliński, Michał Studziński
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22047v1  pdf=https://arxiv.org/pdf/2609.22047v1.pdf

Abstract:
In this work, we study asymmetric $(1\to2)$ quantum cloning for pure states belonging to orbits generated by the orthogonal group. For every dimension $(d\geq3)$, we determine the full region of achievable pairs of average single-copy fidelities. Using orthogonal covariance and the Brauer algebra, we reduce the optimization over all CPTP maps to a finite-dimensional spectral problem and construct explicit optimal cloning channels. We then apply the general results to four-mode fermionic states in the even-parity sector. Using triality, we identify the fixed-concurrence fermionic families with the orthogonal orbits considered in the first part of the paper. In particular, for pure Gaussian states we show that the symmetric locally optimal cloner is unique. We also compare local and global cloning and find that the channel optimal for the joint two-copy fidelity is different from the one optimal for the single-copy fidelities. Finally, we show that the locally optimal cloner cannot be implemented using only operations which preserve fermionic Gaussian states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2607.01778v3
- Title: Morse Bridge between Planar Kepler and Hyperbolic Landau Dynamics
- Authors: Mikhail S. Plyushchay
- Categories: hep-th (primary); hep-th; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2607.01778v3  pdf=https://arxiv.org/pdf/2607.01778v3.pdf

Abstract:
A common Morse Hamiltonian bridges the planar Kepler--Coulomb and hyperbolic Landau systems, linking flat electric dynamics to curved magnetic dynamics. A radial Liouville transformation with coupling-constant metamorphosis maps the separated Kepler problem to the Morse system, while fixed-horocyclic-momentum reduction maps the hyperbolic Landau problem to the same system. In a common normalization, the Coulomb coupling is the signed product of the magnetic field and conserved horocyclic momentum, while the quantum Landau reduction has the universal half-density shift $1/4$. Beyond this shared reduction, we construct a direct classical orbit map on the regular nonradial sectors for all signs of the Kepler energy. It maps the Landau height to a scaled inverse Kepler radius, Kepler ellipses, parabolas and hyperbolas to magnetic circles, horocycles and hypercycles, and Hamilton's hodograph affinely to the Landau carrier circle. The reduced Kepler symplectic form and the Binet-selected complex structure determine a Poincaré Kähler metric. Its nondegenerate Binet orbits have constant geodesic curvature of magnitude equal to the inverse eccentricity, while zero coupling gives geodesics. The orbit map identifies this metric isometrically with the Poincaré configuration-space metric of the hyperbolic Landau problem. Composing the quantum Liouville maps eliminates the Morse wavefunction and yields an exact weighted intertwining identity between the radial Kepler and horocyclic Landau operator pencils. At distinguished half-integer magnetic fields, the angular-momentum grading of a fixed Kepler shell is reorganized into the finite reduced Landau tower and its threshold endpoint. These exact correspondences hold in the stated reduced sectors despite the unitary inequivalence of the complete parent systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20755v1
- Title: Engineering Weak Universality with Quantum Dots
- Authors: Warre Missiaen, Michael Wimmer, Natalia Chepiga
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2609.20755v1  pdf=https://arxiv.org/pdf/2609.20755v1.pdf

Abstract:
Quantum critical theories with continuously varying critical exponents remain challenging to access experimentally. Here, we propose quantum-dot architectures for realizing the quantum Ashkin-Teller and XYZ/eight-vertex models using resonator-mediated and direct Coulomb interactions, respectively. We focus on the Ashkin-Teller and eight-vertex critical lines, which are connected by a non-local duality relating local order parameters to topological string operators. The resulting platforms provide microscopic control over the parameters explicitly controlling critical exponents, with the Coulomb-based implementation enabling stronger interaction regimes. We demonstrate that continuously varying critical behavior can already be resolved in short chains. For experimentally realistic parameters, the accessible interaction range is expected to produce changes in the critical exponents of order $10\%$ for the Ashkin-Teller model and substantially larger changes for the eight-vertex model. In both cases, the predicted variations lie well above the estimated measurement uncertainties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20912v1
- Title: Do Quantum Models Scale Like LLMs?
- Authors: David S. Berman, Ying-Jer Kao, Roger G. Melko, Alexander G. Stapleton
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2609.20912v1  pdf=https://arxiv.org/pdf/2609.20912v1.pdf

Abstract:
In this work, we study the neural scaling laws of RydbergGPT, an autoregressive transformer model trained on qubit projective measurement data gathered from interacting Rydberg atom arrays. The quantum system is known to exhibit a finite-size remnant of a critical point as the laser detuning parameter is varied. We find that near the critical point the transformer loss as a function of training dataset size is well described by a power-law with a loss floor correction. However, away from criticality the quality of the power-law description is substantially reduced. We then compare the statistical structure of both Rydberg measurements and natural-language corpora using an entropy-normalised, finite sample corrected mutual information "two-point" function. We find that near-critical statistics of the two point functions are closest to those observed in natural-language, whilst other qubit configurations far from the critical point have two-point functions that decay more rapidly. This supports the hypothesis that multi-scale dependence contributes to stable neural scaling, and that scaling behaviour should be viewed as a property of the model-data pair.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.20987v1
- Title: Isometry Groups of Right Invariant Metrics in Geometric Quantum Complexity
- Authors: Xiaobo Liu, Lei Zheng
- Categories: math.DG (primary); math.DG; quant-ph
- Links: abs=https://arxiv.org/abs/2609.20987v1  pdf=https://arxiv.org/pdf/2609.20987v1.pdf

Abstract:
In this paper, we give a complete description for the full isometry groups of a class of right invariant Riemannian metrics on the special unitary group $\mathrm{SU}(2^N)$. These metrics have been used by physicists to study Nielsen's geometric approach for complexities in quantum computations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21273v1
- Title: Transcript-Bound Combiners for Downgrade-Resilient Hybrid Post-Quantum Key Establishment: Definition, Proof, and Embedded-Device Cost
- Authors: Bhanwar Gupta, Sanjeev Rana
- Categories: cs.CR (primary); cs.CR; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21273v1  pdf=https://arxiv.org/pdf/2609.21273v1.pdf

Abstract:
Hybrid key establishment runs a post-quantum key-encapsulation mechanism (KEM) alongside a classical Diffie-Hellman primitive, so that the session key stays secure while either component resists attack. This design is now standardized in the Transport Layer Security protocol, Secure Shell, and the Internet Key Exchange, with the standardized module-lattice KEM (ML-KEM) as the post-quantum component. A hybrid KEM secures the derived key, but not the integrity of the negotiation that selects which primitives are used. Full protocols authenticate that negotiation through a handshake transcript; a hybrid KEM deployed as a standalone drop-in primitive, or inside a minimal handshake without transcript authentication, inherits no such guarantee, and an active attacker can strip the post-quantum option. We ask what the key schedule alone must contain to make downgrade resilience a local property of the combiner. We give a game-based definition at the combiner layer and prove a two-sided separation: a combiner that ignores the transcript is downgraded with certainty, whereas one that binds the session key and the confirmation tag to a hash of the transcript blocks every such attempt, up to a term negligible for a 256-bit transcript hash. We also give an explicit strongest-link security bound. Using a calibrated cost model composed from published Cortex-M4 measurements, transcript binding adds one hash per party - about 11.8% of handshake computation but only 1.5% of radio-inclusive energy - and adds no messages or bytes on the wire. Every reported number is produced by a released harness that passes a 30-check validation gate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21300v1
- Title: The Critical Role of Itinerant Contributions to Orbital Angular Momentum Relaxation and Dynamics
- Authors: Andrew C. Grieder, Luis M. Canonico, Frederico Simões, Aron W. Cummings, Yuan Ping
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; cond-mat.other; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21300v1  pdf=https://arxiv.org/pdf/2609.21300v1.pdf

Abstract:
Orbital angular momentum (OAM) is a promising degree of freedom for low-dissipation transport and magnetization control, yet its relaxation mechanisms remain controversial, with atomcentered approximations (ACA) predicting much shorter OAM diffusion lengths than experiments. We address this discrepancy using first-principles Lindbladian density-matrix dynamics, capturing electron-phonon scattering and itinerant OAM contributions, together with a first-principles parameterized tight-binding approach that separates the ACA and itinerant components. In MoS2,a strong-spin-orbit-coupling (SOC) system, orbital relaxation is multi-timescale, with fast intervalley redistribution followed by slower decay coupled to the spin. In weak-SOC silicene, spin and orbital dynamics decouple; an electric field tunes spin relaxation while leaving orbital lifetimes unchanged. In both materials, ACA orbital lifetimes are at least one order of magnitude shorter than itinerant ones, due to ultrafast precession driven by crystal-field splitting, absent from the itinerant component. These results demonstrate that going beyond atom-centered models is essential for describing orbital relaxation and diffusion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21370v1
- Title: Entanglement entropy in holographic CFTs with generic boundaries
- Authors: Fabio Ori, Peng-Xiang Hao
- Categories: hep-th (primary); hep-th; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21370v1  pdf=https://arxiv.org/pdf/2609.21370v1.pdf

Abstract:
Entanglement entropy in holographic conformal field theories with boundaries of generic spacetime signature cannot be described entirely within the standard holographic duality to a real bulk spacetime. We show, both in static and time-dependent setups, that an exact match with the conformal field theory predictions in two boundary dimensions entails an extension of the dual spacetime to complex coordinates. As a consequence, relevant bulk objects such as Ryu-Takayanagi surfaces and branes are in general complex, yet anchored on a real asymptotic boundary preserving the physical meaning of field-theoretical quantities. We also provide a third numerical check of the holographic prediction with a two-dimensional system of free Gaussian fermions exhibiting the same asymptotic regimes across different entanglement phases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21438v1
- Title: Entanglement-Inducing Quantum Markov Processes
- Authors: J. Fransson, A. P. Sowa
- Categories: math-ph (primary); math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21438v1  pdf=https://arxiv.org/pdf/2609.21438v1.pdf

Abstract:
We introduce a new model for a system of interacting bosons placed in an array of sites. At its core is a nonlinear, nonlocal evolution equation, which we have dubbed the Schrödinger-Dirichlet equation. The construction is closely related to the Bose-Hubbard model and to a specific type of generalized bosons. In contrast to conventional mean-field closures, the resulting nonlinear dynamics need not preserve product structure and can generate entanglement from initially separable states. The relevant methods of analysis are based on harmonic analysis for the multiplicative group of positive rationals.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21506v1
- Title: Mechanical Activation of Terahertz Tunneling in Metallic Nanogaps
- Authors: Dasom Kim, Dukhyung Lee, Young-Mi Bahk, Dai-Sik Kim
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21506v1  pdf=https://arxiv.org/pdf/2609.21506v1.pdf

Abstract:
Metallic nanogaps concentrate terahertz (THz) fields into deep subwavelength volumes and support field-driven electron tunneling when the insulating barrier becomes sufficiently narrow. Here, we demonstrate mechanical control of tunneling-mediated nonlinear THz transmission in a flexible nanogap metasurface. The metasurface consists of Au/PMMA/Au nanogaps fabricated on a polyethylene terephthalate substrate, enabling continuous tuning of the gap geometry through macroscopic bending. In the flat state, the resonant transmission exhibits only a weak dependence on the incident THz field strength. Upon bending, increasing the incident field strength induces pronounced resonance suppression accompanied by saturation of the voltage developed across the nanogaps. This nonlinear response is consistent with the opening of a field-dependent tunneling conduction channel through the mechanically narrowed PMMA barriers. Simmons-model calculations illustrate the strong increase in tunneling current density and the associated dissipative gap response as the local gap width approaches the few-nanometer regime. These results establish mechanical deformation as a macroscopic means of controlling tunneling-mediated THz nonlinearities in flexible metasurfaces.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21536v1
- Title: From sparse quantum-computing data to atomistic simulation with universal machine-learning interatomic potentials
- Authors: Tuan Minh Do, Yuichiro Yoshida, Kenji Ishihara, Wataru Mizukami
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21536v1  pdf=https://arxiv.org/pdf/2609.21536v1.pdf

Abstract:
We propose a framework for incorporating quantum-computing-based electronic-structure calculations into universal machine-learning interatomic potentials (uMLIPs). Rather than constructing an interatomic potential from scratch, we refine a pretrained DFT-based uMLIP using a small set of accurate reference energies obtained from quantum computing. We demonstrate the approach for three chemically distinct applications: the Menshutkin reaction, water adsorption in the metal-organic framework HKUST-1, and CO hopping on a high-entropy-alloy nanoparticle. For the Menshutkin reaction, fine-tuning on gas-phase configurations improves the transition-state energy inside a carbon nanotube but not the product energy. For water adsorption in HKUST-1, fine-tuning with only 14 reference configurations brings adsorption thermodynamics obtained from millions of configurations sampled by Widom insertion into closer agreement with reference values. For CO hopping on an IrPdPtRhRu nanoparticle, the preference for on-top over bridge adsorption is recovered in the finite-temperature free-energy profile obtained from enhanced-sampling molecular dynamics, even though the reference data contain only energies. These results demonstrate that the proposed framework provides a practical route for incorporating quantum-computing calculations into realistic atomistic simulations and that quantum-computing reference data can improve pretrained uMLIPs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21585v1
- Title: Exact DeWitt kernels in Lorentzian quantum cosmology
- Authors: Hiroki Matsui
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21585v1  pdf=https://arxiv.org/pdf/2609.21585v1.pdf

Abstract:
The DeWitt boundary condition can be implemented in the Lorentzian path integral of minisuperspace quantum cosmology by summing only over non-singular paths. We give a general definition of the resulting DeWitt kernels, together with explicit rules for constructing them, and evaluate them exactly. The lapse integral over the positive half-line yields the Dirichlet Green function of the Wheeler--DeWitt operator, whereas the integral over the whole real line yields the Dirichlet group-averaging kernel; both vanish when either endpoint lies at the singularity. Since the minisuperspace actions are at most quadratic, all lapse integrals are performed in closed form without saddle-point approximations. We obtain the kernels for the closed universe without cosmological constant, where the whole-real-line kernel vanishes identically, for the flat de Sitter universe, and, in terms of Airy functions, for the closed and open de Sitter universes. Throughout, the DeWitt condition is imposed as the boundary condition at the singularity, which selects a self-adjoint constraint operator on the half-line and fixes the kernels uniquely, including their normalization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21586v1
- Title: Floquet-spin-orbit compensation and flat- and quadratic-band contact in the $α$-$T_3$ lattice
- Authors: Imtiaz Khan, Muzamil Shah, Reza Asgari, Gao Xianlong
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21586v1  pdf=https://arxiv.org/pdf/2609.21586v1.pdf

Abstract:
We investigate Floquet--spin-orbit compensation in the three-band $α$-$T_3$ system, which interpolates between graphene at $α=0$ and the dice lattice at $α=1$. By tuning the interplay between an off-resonant circularly polarized optical field and intrinsic spin--orbit coupling, we identify three distinct pairwise band-degeneracy conditions in the quasienergy spectrum: (i) valley--spin degeneracy, (ii) spin--band degeneracy, and (iii) flat--dispersive band degeneracy. The flat band is not an artifact of a two-band reduction but rather an exact property of the continuum Hamiltonian at this compensation point, where the complete three-band Hamiltonian supports a momentum-independent dark state. A winding-two low-energy Hamiltonian and a finite-momentum Berry-curvature maximum, whose radius scales as the square root of the detuning, emerge from detuning this contact. We further show that the intrinsic transverse thermoelectric response encodes these spectrum patterns. The flat- and quadratic-band degeneracy can be predicted for $0<α<1/2$ because the two response scales linked to the linear contacts have a monotonic ratio independent of the common spin--orbit energy scale. This allows an inverse determination of $α$ and of the common spectral scale. The analytical results are confirmed by full three-band Kubo calculations, which also define the regime in which this inverse characterization is still observable. These results connect an experimentally accessible, Berry-curvature-sensitive thermoelectric response to tunable Floquet--spin--orbit band geometry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21630v1
- Title: Spatially resolved quantum magnetometry and stray-field reconstruction of permalloy microdisks using boron-vacancy centers in hexagonal boron nitride
- Authors: Peiting Wen, Shuyu Wen, Jiang Qu, Zeling Xiong, Katrin Schultheiss, Slawomir Prucnal, Artur Erbe, Kenji Watanabe, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21630v1  pdf=https://arxiv.org/pdf/2609.21630v1.pdf

Abstract:
Transferable hexagonal boron nitride (hBN) hosting negatively charged boron-vacancy (VB$^{-}$) spin defects offers a versatile platform for integrated quantum magnetometry, yet quantitative imaging of magnetic microstructures remains challenging. Here, we integrate a transferred hBN flake with a 4 $μ$m-diameter permalloy (Py = Ni${81}$Fe${19}$) microdisk and perform spatially resolved optically detected magnetic resonance measurements at room temperature. An applied in-plane magnetic field distorts the vortex-state magnetization, generating edge-localized magnetic surface charges and pronounced stray-field signatures at opposite disk edges. By referencing each pixel to its local zero-field splitting and correcting for a residual out-of-plane bias field, we quantitatively reconstruct the out-of-plane stray-field distribution, revealing peak fields of approximately 11.2 mT. An edge-charge model reproduces the spatial distribution and amplitude of the reconstructed field, linking the ODMR response to the field-driven evolution of the vortex state. These results establish transferred hBN VB$^{-}$ sensors for quantitative magnetometry of magnetic microstructures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.21757v1
- Title: Full macroscopic thermalization and the formation of Schrödinger's cats by unitary time evolution in the weakly perturbed Ising model - Applications of the Roos-Sugimoto-Teufel-Tumulka-Vogel theory
- Authors: Hal Tasaki
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.21757v1  pdf=https://arxiv.org/pdf/2609.21757v1.pdf

Abstract:
We study macroscopic thermalization in the ferromagnetic Ising model with a weak generic (highly nonlocal and many-body) random quantum perturbation. We prove that a single typical perturbation makes every initial state $|Φ(0)\rangle$ in a specified energy shell thermalize: a measurement of a large class of macroscopic observables in the time-evolved state $|Φ(t)\rangle=e^{-i\widetilde H_Lt}|Φ(0)\rangle$ yields their thermal equilibrium values, within a prescribed precision and with overwhelming probability, at sufficiently large, typical times $t$. The result covers the full finite-temperature range, including the ordered phase, where we use plus boundary conditions. With periodic boundary conditions in the ordered phase, every energy eigenstate in the shell is shown to be an almost balanced macroscopic Schrödinger-cat state. Moreover, every pure initial state becomes such a cat at sufficiently large, typical times, with each branch in the corresponding macroscopic thermal equilibrium. The proof combines the theory of Roos, Sugimoto, Teufel, Tumulka, and Vogel with rigorous Ising large-deviation estimates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.22079v1
- Title: Universal Eigenvector Statistics of Non-Hermitian Random Matrices
- Authors: Ze Chen, Zhenyu Xiao, Shinsei Ryu
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2609.22079v1  pdf=https://arxiv.org/pdf/2609.22079v1.pdf

Abstract:
Eigenvector overlaps quantify nonorthogonality and govern the response and dynamics of non-Hermitian systems. We extend the universality of non-Hermitian random matrices to the statistics of these overlaps. We obtain analytical expressions for eigenvector overlaps in the spectral bulk and near the origin, covering ten symmetry classes in the limit of large matrix size. Using fermionic replica nonlinear $σ$ models, we relate these overlaps to Hermitian level statistics, symmetry class by symmetry class and topological sector by topological sector. Numerical calculations in various physical models support the universality of the normalized overlaps in the regimes studied. Our work establishes a duality between Hermitian level statistics and non-Hermitian eigenvector overlaps.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2407.03270v3
- Title: Lattices, Gates, and Curves: GKP codes as a Rosetta stone
- Authors: Jonathan Conrad, Ansgar G. Burchards, Steven T. Flammia
- Categories: quant-ph (primary); quant-ph; math-ph; math.AG; math.DG; math.GT
- Links: abs=https://arxiv.org/abs/2407.03270v3  pdf=https://arxiv.org/pdf/2407.03270v3.pdf

Abstract:
We explain how GKP Clifford gates arise as symplectic automorphisms of the corresponding GKP lattice and show that, for scaled codes of type $D=dI_n$, their integral action agrees with the action of the mapping class group of a genus-$n$ surface on first homology. This correspondence introduces a topological interpretation of fault tolerance for GKP codes and motivates the connection between GKP codes (lattices), their Clifford gates, and algebraic curves, which we explore in depth. For a single-mode GKP code, we identify the space of oriented fixed-covolume lattice realizations with $S^3 - K$, the three sphere $S^3$ with a trefoil knot $K$ removed, and explain how logical degrees of freedom arise from the choice of a level structure on the corresponding curves. Specified Clifford implementations define loops in the space of lattices whose trefoil linking number is a topological invariant. Finally, we relate our observations to the idea of fiber bundle fault tolerance as proposed by Gottesman and Zhang for the GKP code, where logical Clifford and Pauli operations of the single-mode GKP code arise as the monodromy representation of a finite covering of the space of nonzero-distance GKP codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2410.18497v2
- Title: Enumeration of all superconducting circuits up to 5 nodes
- Authors: Eli J. Weissler, Mohit Bhat, Zhenxing Liu, Joshua Combes
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2410.18497v2  pdf=https://arxiv.org/pdf/2410.18497v2.pdf

Abstract:
Nonlinear superconducting circuits can be used as amplifiers, transducers, and qubits. Only a handful have been analyzed or built, so useful configurations likely remain undiscovered. In this paper, we enumerate all unique nonlinear superconducting circuits, up to five nodes in size, built of capacitors, inductors, and Josephson junctions. We catalog the resulting design space by sorting circuits into "Hamiltonian classes" using a set of reference coordinates. Finally, we search for novel superconducting qubits by explicitly considering all three-node circuits, showing how the results of our enumeration can be used as a starting point for circuit design tasks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2503.10601v3
- Title: Performance of the spin qubit shuttling architecture for a surface code implementation
- Authors: Berat Yenilen, Arnau Sala, Hendrik Bluhm, Markus Müller, Manuel Rispler
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2503.10601v3  pdf=https://arxiv.org/pdf/2503.10601v3.pdf

Abstract:
Qubit shuttling promises to advance some quantum computing platforms to the qubit register sizes needed for effective quantum error correction (QEC), but also introduces additional errors whose impact must be evaluated. The established method to investigate the performance of QEC codes in a realistic scenario is to employ a standard noise model known as circuit-level noise, where all quantum operations are modeled as noisy. In the present work, we take this noise model and single out the effect of shuttling errors by introducing them as an additional so-called error location. This hardware abstraction is motivated by the SpinBus architecture and allows a systematic numerical investigation to map out the resulting two-dimensional parameter space. To this end, we take the Surface code and perform large scale simulations, most notably extracting the threshold across said two-dimensional parameter space. We study two scenarios for shuttling errors, depolarization on the one hand and dephasing on the other hand. For a purely dephasing shuttling error, we find a threshold of several percent, provided that all other operations have a high fidelity. The qubit overhead needed to reach a logical error rate of $10^{-12}$ (known as the "teraquop" regime~\cite{Gidney2021Jul}) increases only moderately for shuttling error rates up to about 1 \% per shuttling operation. The error rates at which practically useful, i.e. well below threshold error correction is predicted to be possible are comfortably higher than what is expected to be achievable for spin qubits. Our results thus show that it is reasonable to expect shuttling operations to fall below threshold already at surprisingly large error rates. With realistic efforts in the near term, this offers positive prospects for spin qubit based quantum processors as a viable avenue for scalable fault-tolerant error-corrected quantum computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2508.20166v3
- Title: Symmetry enforces entanglement at high temperatures
- Authors: Amir-Reza Negari, Leonardo A. Lessa, Subhayan Sahu
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2508.20166v3  pdf=https://arxiv.org/pdf/2508.20166v3.pdf

Abstract:
Many-body quantum systems with local interactions undergo ``sudden death of entanglement" at high temperatures, whereby thermal states become classical mixtures of product states. We investigate whether symmetry constraints can prevent this phenomenon. We prove that strongly symmetric thermal states (canonical ensemble) of generic Hamiltonians with on-site Abelian symmetries remain entangled with non-zero entanglement negativity at arbitrarily high temperatures, under mild conditions on the symmetry actions and the charge sector of the strong symmetry. Our results extend to weakly symmetric thermal states (Gibbs ensemble) under superselection rules, which restrict state decompositions to be symmetric. In particular, we show that fermionic Gibbs states evade sudden death of entanglement and have persistent fermionic negativity at high temperatures, proving along the way some existing conjectures about fermionic entanglement. These findings demonstrate that global symmetry correlations can preserve quantum entanglement despite thermal decoherence, providing new insights into the interplay between symmetry and quantum information in thermal equilibrium.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2509.17576v2
- Title: Adaptive Policies for Resource Generation in a Quantum Network
- Authors: Aksel Tacettin, Tianchen Qu, Bethany Davies, Boris Goranov, Ioana-Lisandra Draganescu, Gayane Vardoyan
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.17576v2  pdf=https://arxiv.org/pdf/2509.17576v2.pdf

Abstract:
Protocols for distributed quantum systems commonly require the simultaneous availability of $n$ entangled states, each with a fidelity above some fixed minimum $F_{\mathrm{app}}$ relative to the target maximally-entangled state. However, the fidelity of entangled states degrades over time while in memory. Entangled states are therefore rendered useless when their fidelity falls below $F_{\mathrm{app}}$. This is problematic when entanglement generation is probabilistic and attempted in a sequential manner, because the expected completion time until $n$ entangled states are available can be large. Motivated by existing entanglement generation schemes, we consider a system where the entanglement generation parameters (the success probability $p$ and fidelity $F$ of the generated entangled state) may be adjusted at each time step. We model the system as a Markov decision process, where the policy dictates which generation parameters $(p,F)$ to use for each attempt. We use dynamic programming to derive optimal policies that minimise the expected time until $n$ entangled states are available with fidelity greater than $F_{\mathrm{app}}$. We observe that the advantage of our optimal policies over the selected baselines increases significantly with $n$. In the parameter regimes explored, which are based closely on current experiments, we find that the optimal policy can provide a speed-up of as much as a factor of twenty over a constant-action policy. In addition, we propose a computationally inexpensive heuristic method to compute policies that perform either optimally or near-optimally in the parameter regimes explored. Our heuristic method can be used to find high-performing policies in parameter regimes where finding an optimal policy is intractable.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2510.25854v2
- Title: GHZ-Preserving Gates and Optimized Distillation Circuits
- Authors: Mingyuan Wang, Guus Avis, Stefan Krastanov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.25854v2  pdf=https://arxiv.org/pdf/2510.25854v2.pdf

Abstract:
Greenberger-Horne-Zeilinger (GHZ) states play a central role in quantum computing and communication protocols, as a typical multipartite entanglement resource. This work introduces an efficient enumeration and simulation method for circuits that preserve and distill noisy GHZ states, significantly reducing the simulation complexity of a gate on $n$ qubits, from exponential $O(2^n)$ for standard state-vector methods or $O(n)$ for Clifford circuits, to a constant $O(1)$ for the method presented here. This method has profound implications for the design of quantum networks, where preservation and purification of entanglement with minimal resource overhead is critical. In particular, we demonstrate the use of the new method in an optimization procedure enabled by the fast simulation, that discovers GHZ distillation circuits far outperforming the state of the art. Fine-tuning to arbitrary noise models is possible as well. We also show that the method naturally extends to graph states that are local Clifford equivalent to GHZ states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2511.05328v2
- Title: Quantum non-Markovian Hatano-Nelson model
- Authors: Sumit Kumar Jana, Ryo Hanai, Tan Van Vu, Hisao Hayakawa, Archak Purkayastha
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2511.05328v2  pdf=https://arxiv.org/pdf/2511.05328v2.pdf

Abstract:
While considering non-Hermitian Hamiltonians arising in the presence of dissipation, in most cases, the dissipation is taken to be frequency independent. However, this idealization may not always be applicable in experimental settings, where dissipation can be frequency-dependent. Such frequency-dependent dissipation leads to non-Markovian behavior. In this work, we demonstrate how a quantum non-Markovian Hatano-Nelson model arises microscopically in a quasi-one-dimensional dissipative lattice. This is achieved using non-equilibrium Green's functions without requiring any approximation like weak system-bath coupling or a time-scale separation, which would have been necessary for a Markovian treatment. The resulting effective system exhibits nonreciprocal hopping, the defining characteristic of the Hatano-Nelson model, as well as uniform dissipation, both of which are frequency-dependent. This holds for both bosonic and fermionic settings. We find solely non-Markovian nonreciprocal features like unidirectional frequency blocking in bosonic settings, and a particular type of non-equilibrium dissipative quantum phase transition in fermionic settings, that cannot be captured in a Markovian theory, nor have any analog in reciprocal systems. Our results lay the groundwork for describing and engineering non-Markovian nonreciprocal quantum lattices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2512.13502v2
- Title: Arrival Time\textemdash Classical Parameter or Quantum Operator?
- Authors: MohammadJavad Kazemi, MohammadHossein Barati, Ghadir Jafari, S. Shajidul Haque, Saurya Das
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2512.13502v2  pdf=https://arxiv.org/pdf/2512.13502v2.pdf

Abstract:
The question of how to interpret and compute arrival-time distributions in quantum mechanics remains unsettled, reflecting the longstanding tension between treating time as a quantum observable or as a classical parameter. While recent studies have primarily contrasted arrival-time predictions across different interpretations of quantum mechanics, here we investigate this ambiguity within the standard quantum-mechanical framework itself. Moreover, most previous studies have focused on the single-particle case in the far-field regime, where these distinct approaches yield very similar arrival-time distributions and a semi-classical analysis typically suffices. Recent advances in atom-optics technologies now make it possible to experimentally investigate arrival-time distributions for entangled multi-particle systems in the near-field regime, where a deeper analysis beyond semi-classical approximations is required. Even in the far-field regime, due to quantum non-locality, the semi-classical approximation cannot generally hold in multi-particle systems. Therefore, in this work, two fundamental approaches to the arrival-time problem---namely, the time-parameter and time-operator approaches---are extended to multi-particle systems. Using these extensions, we propose a feasible two-particle arrival-time experiment and numerically evaluate the corresponding joint distributions. Our results reveal regimes in which the two approaches yield inequivalent predictions, highlighting conditions under which experiments could shed new light on distinguishing between competing accounts of time in quantum mechanics. Our findings also provide important insights for the development of quantum technologies that use entanglement in the time domain, including non-local temporal interferometry, temporal ghost imaging, and temporal state tomography in multi-particle systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2604.08655v2
- Title: High-Fidelity Transmon Reset with a Multimode Acoustic Resonator
- Authors: Andraž Omahen, Simon Storz, Igor Kladarić, Yiwen Chu
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2604.08655v2  pdf=https://arxiv.org/pdf/2604.08655v2.pdf

Abstract:
Achieving sufficiently low residual excited-state populations remains a key challenge in superconducting quantum circuits, particularly for protocols operating close to noise limits or requiring repeated qubit initialization. Existing protocols primarily address this challenge through sophisticated control, engineered dissipation, or feedback mechanisms. Here, we demonstrate an alternative approach in which a superconducting qubit is reset using a physically distinct, intrinsically colder phononic bath. Specifically, we interface a transmon with a high-overtone bulk acoustic resonator (HBAR), enabling cooling of the qubit into GHz-frequency modes. Using this approach, we achieve a residual excited-state population of the qubit below $10^{-4}$, representing an improvement of one to two orders of magnitude compared to existing reset schemes. These results highlight the potential of phononic baths as a resource for high-fidelity qubit initialization in superconducting circuits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2606.03848v2
- Title: Generating quantum ensembles via reverse-time quantum diffusions
- Authors: Maël Bompais, Mădălin Guţă, Juan P. Garrahan
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2606.03848v2  pdf=https://arxiv.org/pdf/2606.03848v2.pdf

Abstract:
We establish a reverse-time denoising theory for quantum diffusions of continuously measured quantum systems. Starting from the stochastic Schrödinger equation of a forward noising dynamics, we derive the exact reverse-time dynamics for quantum trajectories, whose law coincides with the time-reversal of the original process. We prove that the denoising dynamics is a physically admissible quantum diffusion, with the same measurement-induced noise but a state-dependent feedback Hamiltonian, a direct analogue of the "score function" of generative classical diffusion models. This provides a principled framework for converting samples of a simple distribution into those of a more complex ensemble of quantum states. We show how the denoising dynamics can be directly learnt from forward trajectory data, and how to exploit purification to initialise the denoising process.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2606.23544v2
- Title: Structure-Aware Variance Reduction for Unbiased Randomized Hamiltonian Simulation
- Authors: Joshua W. Dai, Fredrik Hasselgren, Chusei Kiumi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2606.23544v2  pdf=https://arxiv.org/pdf/2606.23544v2.pdf

Abstract:
Randomized Hamiltonian simulation methods are often governed by a trade-off between systematic bias and sampling overhead. We study how classical variance-reduction techniques can be applied to such methods without changing their mean channel, and therefore without introducing additional bias. As a motivating unbiased estimator, we formulate continuous time-evolution probabilistic angle interpolation (continuous TE-PAI), a quasiprobabilistic random-circuit protocol whose remaining Monte Carlo error is purely statistical. Continuous TE-PAI removes Trotter discretization error with finite-depth random circuits, whereas deterministic Trotterization does so only in the infinite-depth limit. Further, in tensor-network simulations, we demonstrate that discretization error can cause an unphysical exponential growth in the bond dimension required for Trotterized simulations, whereas comparable-depth continuous TE-PAI circuits avoid this growth. We then show that the variance of randomized product-formula-based estimators admits a canonical decomposition into a classical counting component and a quantum ordering component such that the dominant simulation overhead results from the non-commutative parts of the Hamiltonian dynamics. Motivated by this decomposition, we achieve an $\approx70\%$ error-reduction using the counting-component for small systems whereas our tensor-network simulations of $n=30$ spin-chain dynamics use coarser statistics tailored to the observable and estimator attaining a negligible bias and a reduction of $\approx 80\%$ leading to $\approx91\%$ and $\approx96\%$ sampling-cost reductions, respectively.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2608.05314v2
- Title: Machine learning for sample-based quantum diagonalization: a review of generative configuration recovery and the classical-simulability frontier
- Authors: Nicolás Bonilla Vargas
- Categories: quant-ph (primary); quant-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2608.05314v2  pdf=https://arxiv.org/pdf/2608.05314v2.pdf

Abstract:
Sample-based quantum diagonalization (SQD), equivalently quantum-selected configuration interaction (QSCI), has become a centre of gravity of pre-fault-tolerant quantum chemistry: a processor samples electronic configurations and the Hamiltonian is diagonalized classically in the resulting subspace. Accuracy is governed entirely by which configurations enter it -- a machine-learning selection problem, made acute by a coupon-collector bottleneck. We review the generative and learned selectors by what each generates and the signal it exploits, and identify one gap: no reward-proportional generative-flow-network proposer has been built for tail discovery. On the field's central question -- whether the quantum sampler beats classical selected CI -- the negative verdict is not ours to claim: priority belongs to Reinholdt et al. [JCTC 21, 6811 (2025)], and polynomial-time classical estimation of the flagship circuits has reinforced it. We state that verdict at the precision a falsifiable claim requires -- it concerns reproducible, same-active-space comparisons on molecular electronic structure -- and weigh the claims outside those qualifiers. We show that alpha-string weights are not invariant under rotations inside degenerate orbital shells, so determinant counts are undefined until the orbital gauge is declared. We distil a ten-element benchmarking standard and apply it to our own deposit, which returned defects that changed numbers printed here and retracted one from v1. FCI-exact experiments confirm one prediction and refute another: the single generative advantage we find keeps no consistent sign along the dissociation coordinate at device-calibrated noise and reverses under a symmetric readout model. It does beat a noise-matched classical recovery loop on N2 by a margin five seeds cannot resolve, and loses by over a factor of two to a classical selector that needs no sampler.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2608.23285v2
- Title: Efficient Computation of QKD Key Rates without Semidefinite Programming
- Authors: Bence Temesi, Antoine Gansel, Gereon Koßmann, Rene Schwonnek
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.23285v2  pdf=https://arxiv.org/pdf/2608.23285v2.pdf

Abstract:
Translating observed data into a reliable estimate of the secure key rate is a crucial step for operating a quantum key distribution device. We provide a computational method for this task that only requires eigenvalue computations and is therefore both fast and resource efficient. In contrast, existing approaches rely on semidefinite programming or programming on the entropy cone, whose memory requirements can scale as $d^4$ in the underlying Hilbert-space dimension. Our method reduces this requirement to $d^2$. A minimal implementation of our algorithm takes fewer than 100 lines of Common Lisp. We demonstrate real-time key-rate estimation on a Raspberry Pi with a 1 GB memory and a Cortex-A53 processor. Despite these modest resources, our implementation outperforms existing workstation-based benchmarks by several orders of magnitude. Non-numerical verification can be incorporated with little overhead using rational approximations. These results open the way toward embedding complete numerical security analysis directly into qkd hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2608.23681v2
- Title: Bang-bang protocol for nondispersive qubit readout
- Authors: Nina del Ser, Yinan Chen, Jacob Steiner, Gil Refael
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.23681v2  pdf=https://arxiv.org/pdf/2608.23681v2.pdf

Abstract:
Fast, precise, and quantum-non-demolition (QND) readout of superconducting qubits is a fundamental component of high-fidelity quantum sensing and computation. Conventional approaches typically operate in the dispersive regime, where the qubit-resonator coupling $g$ is weak compared to the detuning $Δ$. While exhibiting good QND properties, the readout rate is limited to $\sim g^2\sqrt{N}/Δ\ll g$, where $N$ is the number of photons in the resonator. QND readout in the nondispersive regime, where the readout rate reaches its full potential $\sim g$, relies on parameter sweeps that may encounter resonances, leading to measurement-induced state transitions (MIST). In this work, we study a nondispersive readout protocol that replaces these sweeps by sudden quenches of the coupling constant, using a resonator that is preloaded with photons. We call this protocol bang-bang readout, and show that it realizes single-shot projective measurements. The fidelity and QNDness of the qubit post-measurement are remarkably high, with an error that decreases like $1/N$. We show that the protocol can also be implemented without preloading the resonator by instead strongly driving the qubit, e.g., with a classical flux drive.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.07890v2
- Title: Riemannian optimization for linear optical problems
- Authors: Pablo V. Parellada
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2609.07890v2  pdf=https://arxiv.org/pdf/2609.07890v2.pdf

Abstract:
Many applications of linear optics in quantum science involve searching for some optimal configuration of a multiport interferometer. For example, to find heralded state preparations, one can optimize the interferometer to maximize the fidelity and success probability of the state preparation. In this paper, we derive a closed analytical formula for the Riemannian gradient of any differentiable function defined over the interferometer unitaries. We use this gradient in Riemannian optimization algorithms, such as gradient descent or BFGS, to find the optimal setup of the interferometer. As an interesting use case, we search for linear optical state preparations, improving some of the success probabilities reported in the literature for NOON or photon catalysis preparations. Finally, we show that our optimizer is orders of magnitude faster than other methods in the literature, opening the door for solving linear optical problems involving more modes and photons.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.13022v2
- Title: Grover Search with Semiconductor Spin Qubits at Ambient Conditions
- Authors: Sebastian Gemsheim, Fabian Klüpfel, Max Kneiß, Nicole Raatz, Tobias Herzig, Matthias Mendt, Evgeny Kreissig, Ulrike Rückert, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.13022v2  pdf=https://arxiv.org/pdf/2609.13022v2.pdf

Abstract:
Grover's algorithm is executed on a commercial quantum computer based on nitrogen-vacancy centers in diamond operating under ambient conditions, achieving fidelities up to $99.98\,\%$. Within a $N=8$ search space of three solid-state nuclear spin qubits, the measured success probabilities of finding a single or two marked states are $(77.3 \pm 3.4)\,\%$ and $(87.0 \pm 4.2)\,\%$, respectively. These values surpass published results for superconducting qubits or any quantum computer operating at room temperature. In addition, the paper also details the calibrated fidelities of the implemented universal gate set.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2504.02980v3
- Title: Effective Mode Description for Macroscopic Fabry Pérot Cavities
- Authors: Michael A. D. Taylor, Jonathan Soderquist, Pengfei Huo
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2504.02980v3  pdf=https://arxiv.org/pdf/2504.02980v3.pdf

Abstract:
We introduce an effective modes formalism to describe how the quasi-continuum of photonic modes in an optical cavity effectively behaves in the strong light-matter coupling regime of cavity quantum electrodynamics. By expressing these effective modes, we are able to reproduce the cavity dispersion relation while showing that the mode volumes of these effective modes are independent of the physical area of the Fabry-Pérot cavity mirrors and are instead a measure of light-matter coupling strength, dependent on cavity design parameters such as mirror reflectivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2511.14754v2
- Title: Observation of critical scaling in the Bose gas universality class
- Authors: Leon Kleebank, Frank Vewinger, Arturo Camacho-Guardian, Victor Romero-Rochín, Rosario Paredes, Martin Weitz, Julian Schmitt
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2511.14754v2  pdf=https://arxiv.org/pdf/2511.14754v2.pdf

Abstract:
Critical exponents characterize the divergent scaling of thermodynamic quantities near phase transitions and allow for the classification of physical systems into universality classes. While quantum gases thermalizing by interparticle interactions fall into the XY model universality class, the ideal Bose gas has been predicted to form a distinct universality class whose signatures have not yet been revealed experimentally. Here, we report the observation of critical scaling in a two-dimensional trapped quantum gas of essentially noninteracting photons, which thermalize by radiative contact to a reservoir of molecules inside a microcavity. By measuring the spatial correlations near the condensation transition, we determine the critical exponent for the correlation length to be $ν= 0.52(4)$. Our results constitute a first experimental test of the long-standing scaling predictions for the Bose gas universality class.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2604.18283v2
- Title: On quantum functionals for higher-order tensors
- Authors: Alonso Botero, Matthias Christandl, Thomas C. Fraser, Itai Leigh, Harold Nieuwboer
- Categories: math.AG (primary); math.AG; cs.CC; math.RT; quant-ph
- Links: abs=https://arxiv.org/abs/2604.18283v2  pdf=https://arxiv.org/pdf/2604.18283v2.pdf

Abstract:
Upper and lower quantum functionals, introduced by Christandl, Vrana and Zuiddam (STOC 2018, J. Amer. Math. Soc. 2023), are families of monotone functions of tensors indexed by a weighting on the set of subsets of the tensor legs. Inspired by quantum information theory, they were crafted as obstructions to asymptotic tensor transformations, relevant in algebraic complexity theory. For tensors of order three, and more generally for weightings on singletons for higher-order tensors, the upper and lower quantum functionals coincide and are spectral points in Strassen's asymptotic spectrum. Moreover, the singleton quantum functionals characterize the asymptotic slice rank, whereas general weightings provide upper bounds on asymptotic partition rank. It has been an open question whether the upper and lower quantum functionals also coincide for other cases, or more generally, how to construct further spectral points, especially for higher-order tensors.   In this work, we show that upper and lower quantum functionals generally do not coincide, but that they anchor new spectral points. With this we mean that there exist new spectral points, which equal the quantum functionals on the set of tensors on which upper and lower coincide. The set is shown to include embedded three-tensors and W-like states and concerns all laminar weightings, significantly extending the singleton case. Moreover, it is shown that these spectral points provide obstructions to asymptotic restriction beyond the previously known spectral points.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2605.06985v2
- Title: Real-Time Quantum Dynamics on the Fuzzy Sphere: Chaos and Entanglement
- Authors: S. Kürkcüoğlu, B. Özcan
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2605.06985v2  pdf=https://arxiv.org/pdf/2605.06985v2.pdf

Abstract:
We study the real time quantum dynamics of a matrix model consisting two bosonic fields on the fuzzy sphere using the Gaussian state approximation. Starting from the Hamiltonian formulation and using Wick's theorem, we derive a closed set of coupled nonlinear differential equations governing the time evolution of the one- and two-point correlation functions. Thermal equation of state is found by maximizing the von Neumann entropy over Gaussian states and solving algebraic self-consistency equation(s) leading to a complete determination of the symplectic spectrum of the covariance matrix. We identify near thermal initial conditions and use them to solve the equations of motion and employ our findings to probe chaos by calculating the largest Lyapunov exponent at various temperatures. Our results demonstrate that the latter tends to zero at a finite temperature indicating that the quantum dynamics respect the Maldacena,Shenker,Stanford bound across all temperatures, while approaching toward the classically chaotic regime at high temperatures. Finally, we examine the entanglement dynamics of the model in real-time by considering a sequence of bipartitions of the Hilbert space and computing the entanglement entropy and clearly exhibit the fast scrambling features that emerge in due detail.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2606.00214v2
- Title: Extracting central charge from ground-state overlaps of spatially deformed Hamiltonians
- Authors: Chen Bai, Xinyu Sun, Liang-Hong Mo, Hong-Hao Tu
- Categories: cond-mat.str-el (primary); cond-mat.str-el; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2606.00214v2  pdf=https://arxiv.org/pdf/2606.00214v2.pdf

Abstract:
We show that the conformal anomaly of a $(1+1)$-dimensional conformal field theory can be extracted directly from a ground-state wave-function overlap associated with a spatial conformal deformation. Focusing on the $q$-Möbius deformation, we derive an exact overlap formula between the deformed and undeformed ground states, whose exponent directly encodes the central charge. Motivated by this result, we construct a lattice estimator based solely on ground-state overlaps and apply it to representative critical quantum chains and the gapless edge modes of a two-dimensional Chern insulator. Numerical results demonstrate that the resulting overlaps provide a simple and robust probe of the central charge in microscopic models. We further demonstrate that the deformed ground states retain universal geometric structures in their entanglement spectra and entanglement entropies. These results provide a simple wave-function-based route to probing conformal data in critical systems and topological edge modes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.05556v2
- Title: Kibble-Zurek Dynamics in Two-dimensional Frustrated Systems with a Neural Foundation-state Subspace Method
- Authors: Linda Mauron, Luciano Loris Viteritti, Zakari Denis, Riccardo Rende, Giuseppe Carleo
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2609.05556v2  pdf=https://arxiv.org/pdf/2609.05556v2.pdf

Abstract:
Universal scaling generated when a strongly interacting quantum many-body system is driven across a continuous phase transition provides a dynamical probe of equilibrium criticality. Accessing this regime numerically in two dimensions is challenging because it requires accurate real-time evolution of correlated many-body states over many system sizes and driving rates. We introduce a Neural Foundation-state Subspace (NFS) method for near-adiabatic dynamics. A foundation neural-network quantum state represents the ground-state manifold along the driving path, and a small fidelity-selected subset defines a fixed variational subspace. The many-body Schrödinger equation then reduces to the evolution of a few linear coefficients, with projected operators reusable across ramp times. We validate the method on the two-dimensional transverse-field Ising model, recovering the expected Kibble-Zurek scaling and critical exponents in quantitative agreement with ground-state quantum Monte Carlo estimates. Applied to the frustrated square-lattice $J_1$-$J_2$ Heisenberg model up to $16 \times 16$ clusters, our approach provides strong numerical evidence of Kibble-Zurek mechanism across the Néel-to-spin-liquid transition at $J_2/J_1=0.49$, yielding ${ν=1.23(15)}$ and ${η=0.409(19)}$ at fixed $z=1$, consistent with static estimates and supporting the proposed continuous critical behavior.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-21 14:12
- arXiv: 2609.05634v2
- Title: Fast universal parametric spin control in an acoustically modulated quantum dot
- Authors: Mateusz Kuniej, Michał Gawełczyk
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2609.05634v2  pdf=https://arxiv.org/pdf/2609.05634v2.pdf

Abstract:
Quantum communication, distributed computing, and hybrid architectures rely on nodes enabling coherent control of qubits and coupling to propagating quantum modes. While semiconductor quantum-dot (QD) spins couple to microwave and optical photons, weak interaction with mechanical waves has limited the integration of single-QD spin qubits into on-chip, acoustically coupled hybrid systems. The existing theory of acoustic QD spin control suffers from a limited range of rotation-axis angles, enforcing complex realizations of gate primitives and long gate times, leaving little margin against decoherence from trion decay and quasi-static nuclear-spin noise. We propose parametric control that overcomes these problems. We use far-detuned optical coupling to a trion state to dress and thus mix spin states, combined with acoustic modulation of the optical transition energy. Instead of relying on direct acoustic resonance with the spin splitting that leads to significant bottlenecks, we induce spin rotations parametrically via resonance with the dressed-spin splitting. We thus develop a spin analog of the ``swing-up'' charge-state excitation. Our scheme provides fast universal qubit control with nearly arbitrary rotation axes. Our ${\sim}$155 ps Pauli-$X$ gate duration is ${\sim}290\times$ faster than in the previous acousto-optical formulation and ${\sim}14\times$ faster than optical Faraday-geometry spin rotation. The parametric scheme naturally enables higher-harmonic processes. Numerical simulations for ${\sim}44$ GHz acoustic driving show average gate fidelity $\ge99.9\%$ even for uncooled nuclear-spin environments of GaAs and InAs QDs for trion lifetime $\gtrsim1.25$ ns. These metrics suggest practically usable control and may introduce a spin-phonon interface with high interaction rates, versatility, and multi-phonon processes, essential for future acoustically coupled hybrid architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22159v1
- Title: The Limit and Its Ground. QBism, Scientific Realism, and the Born Rule
- Authors: Harald A Wiltsche
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2609.22159v1  pdf=https://arxiv.org/pdf/2609.22159v1.pdf

Abstract:
QBists insist that theirs is a realist position while denying that the quantum formalism represents a mind-independent world. The insistence is hard to place. The realism debate is throughout a dispute about represented content, so a theory that denies standing in the representation relation appears not to take up a position within that debate at all. This paper examines the most developed attempt to make good on the QBist claim--David Glick's perspectival normative realism--and argues that it fails instructively. Glick seeks the ground of the Born rule's objectivity among states of affairs and construes an agent's perspective as a location within an already-constituted world; finding no state of affairs fit to bind every agent at once, he must book the ground as brute. Phenomenology supplies the third thing his picture lacks. A horizon is not a position within the world but the condition under which a world is given. Read as an agent's weighting--her curvature--of such a horizon, the quantum state is neither a defective description nor a brute posit, and the Born rule articulates the invariant lawfulness by which any sense confers a curvature at all.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22176v1
- Title: Every architecture of six two-qubit gates is locally universal on three qubits
- Authors: Hyunho Cha, Jungwoo Lee
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22176v1  pdf=https://arxiv.org/pdf/2609.22176v1.pdf

Abstract:
We present the \emph{first} analytical determination of the exact accessible dimension for every fixed architecture of arbitrary two-qubit gates on three qubits. A support word represents which pair of qubits each two-qubit gate acts on, and its reduced length is obtained by merging consecutive gates on the same pair. If the reduced length is $r$, then the set of implementable three-qubit unitaries has accessible dimension $d(w)=\min\{63,9r+9\}$. Consequently, six arbitrary two-qubit gates are \emph{necessary and sufficient for local universality}: every fixed architecture reaches a nonempty open subset of $\mathrm{SU}(8)$ when its reduced length is at least six. The result is stronger than existence of one favorable architecture. Every reduced six-slot support word is locally universal, including the alternating nearest-neighbor line $AB,BC,AB,BC,AB,BC$. The upper bound follows from a standard parameter-counting argument. The matching lower bounds are proved by Jacobian certificates in the Pauli basis. Up to qubit relabeling and reversal, there are $22$ reduced architectures of lengths two through six. For each one, a product of rational Pauli rotations yields a nonzero maximal minor modulo the prime $1{,}000{,}003$. Thus, any obstruction to global universality with six two-qubit gates must go beyond parameter counting, connectivity, and differential rank.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22181v1
- Title: Localizable Bipartite Rank-One Ideal Measurements Have a Block-Replicated Nice-Bell Structure
- Authors: Ahmed Younis
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22181v1  pdf=https://arxiv.org/pdf/2609.22181v1.pdf

Abstract:
We prove a complete structural characterization of finite-dimensional bipartite rank-one ideal projective measurements that are localizable without communication in the sense of Akibue and Miyazaki. Up to local-unitary equivalence, every such measurement basis is obtained by replicating a single nice Bell basis across equal-dimensional local subspace blocks. The necessity proof combines the causal block structure of complete measurements established by Beckman, Gottesman, Nielsen, and Preskill with their eigenstate-composition theorem for localizable superoperators. A reference block is first forced to be a nice Bell basis; the same theorem then propagates that basis consistently along every row, column, and interior block. The converse follows from the explicit localization protocol of Akibue and Miyazaki. This establishes their Conjecture 1 and gives a protocol-independent classification of bipartite rank-one ideal measurements in this setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22189v1
- Title: Physics-Informed Classical and Quantum Neural Networks for One-Dimensional Schrodinger Eigenvalue Problems
- Authors: Tariq Mahmood, Waqas Arshad, Bilal Naseer, Alfredo Raya
- Categories: quant-ph (primary); quant-ph; cs.LG; hep-ph; hep-th
- Links: abs=https://arxiv.org/abs/2609.22189v1  pdf=https://arxiv.org/pdf/2609.22189v1.pdf

Abstract:
The Schrodinger equation in one spatial dimension admits a small set of exactly solvable potentials that serve as natural proving grounds for any new eigenvalue solver. We formulate Physics-Informed Neural Networks (PINNs) and Physics-Informed Quantum Neural Networks (PIQNNs) for the time-independent Schrodinger equation and apply them to three of these benchmarks: the harmonic oscillator, the infinite square well, and the finite square well. In each case a composite loss encodes the differential-equation residual, the normalization condition, the boundary behavior, and the orthogonality between eigenstates, so that the trial wave function is driven toward a genuine eigenfunction without supervised data. The eigenvalues and wave functions returned by both methods are compared against the exact spectra and against three classical references: the matrix Numerov method, the finite difference method, and the shooting method. For the smooth oscillator the two neural solvers reproduce the lowest four eigenvalues to parts per million, while for the square wells they recover the analytic levels with comparable fidelity even where the potential is discontinuous. The quantum circuit, built as a layered angle-embedding ansatz with strongly entangling blocks, converges more reliably than its classical counterpart on the higher excited states, where the loss landscape of the classical network becomes harder to navigate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22190v1
- Title: Non-Markovian Quantum Decay in Complex Environments: A Hyperstatistical Approach
- Authors: Nicola Fabiano
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2609.22190v1  pdf=https://arxiv.org/pdf/2609.22190v1.pdf

Abstract:
The exponential decay of an unstable quantum state, as described by standard Markovian theories such as Fermi's Golden Rule, assumes a simple, structureless environment. However, in complex environments characterized by disorder, long-range interactions, or strong fluctuations, local decay rates fluctuate, leading to non-Markovian dynamics and power-law ``long-time tails.'' In this paper, we apply the recently proposed \textit{hyperstatistics} framework to solve the problem of quantum decay in such complex environments. By considering a $γ$-distribution of local decay rates across mesoscopic domains, we derive a macroscopic survival probability governed by a $q$-exponential function. We then use the $q$-generalized Gamma function, defined via the Mellin transform of the $q$-exponential, to calculate the moments of the decay-time distribution. We show that the mean quantum lifetime is finite for $q<2$. The convergence of the second moment instead requires the stricter condition $q<3/2$. For $1<q<3/2$ both the mean lifetime and its variance are finite, for $3/2\le q<2$ the mean lifetime remains finite but lifetime fluctuations become infinitely broad, and for $q\ge2$ the mean lifetime itself diverges. This result provides a physical interpretation linking extreme environmental complexity to Anderson localization and Griffiths-like phases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22425v1
- Title: Gibbs resampling transitions and structured fast-measurement protocols
- Authors: Daan Timmers, Benedikt Placke, Siddharth A. Parameswaran
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22425v1  pdf=https://arxiv.org/pdf/2609.22425v1.pdf

Abstract:
Quantum Gibbs sampling algorithms generalize classical Markov chain Monte Carlo (cMCMC) methods, and prepare thermal states on quantum computers by implementing local dissipative evolution for a mixing time $t_{\rm mix}$. Since quantum measurements disrupt the prepared state, the rate of extracting unbiased information from the system depends on the recovery of the underlying thermal correlations. The corresponding ''Gibbs resampling'' time $t_{\rm res}$ is distinct both from $t_{\rm mix}$ and from the autocorrelation time relevant to cMCMC sampling. We study this problem in effective classical models that emulate disruptive quantum measurements of local observables on extensive subsystems. When such subsystems are chosen randomly, in models with non-local order parameters we uncover a ''resampling transition'' as a function of the fraction of sites $p$ that are measured, from $t_{\rm res}\propto \log L$ for small $p$ to $t_{\rm res}\propto {\rm poly} L$ for large $p$, in systems of linear size $L$. We argue that this transition is generically absent in systems with local order parameters, and relate this dichotomy to one between the coarsening of initial states that break 1- and 0-form symmetries under Glauber dynamics. Finally, we devise a structured fast-measurement protocol that evades slow resampling even with non-local order parameters, while leaving only a vanishing fraction of all sites unmeasured.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22442v1
- Title: Extracting Electromagnetic Bare Mode Couplings in Large Superconducting Quantum Processors
- Authors: Reza Molavi, Ebrahim Forati, Yaxing Zhang, Andrey R. Klots, Juan Atalaya, Brandon W. Langley, Dogan A. Timucin, Moein Nazari, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22442v1  pdf=https://arxiv.org/pdf/2609.22442v1.pdf

Abstract:
High-fidelity control of superconducting quantum processors requires accurate characterization of electromagnetic coupling strengths among the device's constituent elements. Accurately extracting these couplings across large-scale architectures, presently featuring hundreds of qubits, poses a challenging multi-scale modeling problem. This requires resolving scales from the nanometer-scale geometry of Josephson junctions and their leads to the centimeter-scale size of the enclosing metallic packages. We present four numerical coupling extraction methods based on the avoided level crossing, the energy participation ratio, the induced electromotive force, and the impedance matrix. These methods are tailored to work with commercially available 3D electromagnetic solvers. We benchmark these techniques on a $10\times10$ array of transmon qubits, extracting their couplings to standing package modes. Our results show that these methods yield consistent coupling strengths with a maximum relative difference of less than 5%.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22445v1
- Title: A Near-Optimal Joint Lower Bound for Sparse Quantum Linear System Solvers
- Authors: Dhrumil Patel
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22445v1  pdf=https://arxiv.org/pdf/2609.22445v1.pdf

Abstract:
Quantum linear system solvers form one of the central algorithmic primitives in quantum computing, with applications ranging from differential equations and optimization to machine learning. Their cost is commonly measured through query complexity, which counts the number of oracle calls needed to access the input matrix. In the sparse-access model, this complexity is governed by three parameters: the condition number $κ$, the sparsity $s$ of the input matrix, and the target precision $\varepsilon$. The dependence on $κ$ and $\varepsilon$ is already well understood through the lower bound $Ω(κ\log(1/\varepsilon))$, which matches the best known scaling in these parameters. Once the sparsity $s$ is included, however, the expected lower bound has long been conjectured to be $Ω(κ\sqrt{s}\log(1/\varepsilon))$. Recent work by Mori et al. [Quantum Sci. Tech. 11 035063 (2026)] made an important step towards this goal by establishing the lower bound $Ω(κ\sqrt{s})$ for constant error $\varepsilon$. In this work, we complete the picture and prove the full joint lower bound $Ω(κ\sqrt{s}\log(1/\varepsilon))$ in the sparse-access model, thereby establishing the anticipated dependence on all three parameters simultaneously.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22501v1
- Title: Gravitationally Induced Entanglement of Matter in Quadratic Curvature Gravity and Constraints on Ghost Mass
- Authors: Linda M. van Manen, Tim Blankenstein, Anupam Mazumdar
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2609.22501v1  pdf=https://arxiv.org/pdf/2609.22501v1.pdf

Abstract:
We investigate gravitationally generated entanglement in two quantum harmonic oscillators induced by quadratic (Stelle) gravity, including corrections up to $1.5$ post-Newtonian order. Starting from the quadratic action, we derive the effective two-body Hamiltonian for two harmonically trapped masses, incorporating the contributions of the massive spin-$2$ ghost ($m_2$) and massive spin-$0$ ($m_0$) degrees of freedom of the gravitational field. For two quantised oscillators prepared in their ground state, we compute the von Neumann and Rényi entropies of the reduced state and identify a frequency at which the gravitationally-induced entanglement vanishes due to cancellation between relativistic momentum squeezing and quantum-delocalisation-induced position squeezing. We further analyze the cancellation frequency and derive the approximate constraint $m_0 < \sqrt[3]{4}\, m_2$ for the spin-$2$ and spin-$0$ modes. This relation follows from demanding a stable harmonic oscillator description. Finally, we study gravitationally-induced concurrence in a non-Gaussian setup and show how quadratic gravity modifies the entanglement generated between two spatial superpositions. The concurrence can approach $\mathcal{O}(1)$ for certain choices of mass, spatial superposition, particle distance, and spin-$2$ and spin-$0$ modes. The concurrence will deviate from Newtonian gravity at certain particle separations, depending on the energy of the spin-$2$ and spin-$0$ modes. For example, spin modes as low as $0.0197$ eV become distinguishable from Newtonian gravity at a distance $d \sim 40 μ$m. This allows us to constrain the spin-$2$ and spin-$0$ masses in experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22502v1
- Title: Spin-Boson Mappings in the Formalism of $f$-Deformations
- Authors: Vladimir A. Orlov, Liubov A. Markovich, Alexey V. Mikheenkov, Vladimir I. Man'ko
- Categories: quant-ph (primary); quant-ph; cond-mat.other; math-ph
- Links: abs=https://arxiv.org/abs/2609.22502v1  pdf=https://arxiv.org/pdf/2609.22502v1.pdf

Abstract:
We develop a unified algebraic approach to spin-boson transformations based on the formalism of $f$-deformed oscillators. In the single-mode case, we show that the Holstein-Primakoff and Dyson-Maleev transformations, together with the interpolating $α$-family, arise as different factorizations of the same algebraically determined object. The standard spin-boson mappings can thus be interpreted as realizations of a common structure, which makes it possible to clearly separate the exact algebraic content on the physical subspace from effects associated with non-Hermiticity, the choice of metric, and extensions beyond the physical subspace. In the two-mode case, the same approach yields both deformed versions of the Jordan-Schwinger transformation and new exact two-mode realizations. Our results provide a unified description of known spin-boson transformations and naturally lead to new bosonic representations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22564v1
- Title: Generating Dicke State Graphs
- Authors: Rebekah Herrman
- Categories: quant-ph (primary); quant-ph; math.CO
- Links: abs=https://arxiv.org/abs/2609.22564v1  pdf=https://arxiv.org/pdf/2609.22564v1.pdf

Abstract:
Graph theory is a powerful tool in quantum computing, with applications ranging from quantum circuit synthesis and optimization to entanglement mapping. Recent work has shown how one can use edge-colored graphs to model photonic experiments that generate GHZ and W states. However, the latter work also proved that verifying that a graph models a Dicke state experiment is coNP-complete. In this work, we provide families of graphs that generate $|D_{k}^a\rangle \otimes |0\rangle^{\otimes b }$, where $b = |a-2k|$ is the number of spectator modes. The graph setup consists of a doubled complete subgraph on $a$ vertices and a collection of auxiliary vertices. We prove that every coincidence carries exactly $k$ excitations, every weight-$k$ computational basis state on bitstrings of length $a$ is realized, and each of those bitstrings is realized exactly $(n/2)!$ times, where $n = a+b$. Since verifying the Dicke FORALL condition is coNP-complete in general, constructing explicit families that provably generate Dicke states is of interest.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22572v1
- Title: Modular fault-tolerant quantum computing on a non-CSS code
- Authors: Robert Freund, Friederike Butt, César Benito, Ivan Pogorelov, Marcel Meyer, Alex Steiner, Alejandro Bermudez, Markus Müller, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22572v1  pdf=https://arxiv.org/pdf/2609.22572v1.pdf

Abstract:
Modularization promises to break down the design and implementation complexity of large scale quantum processors into smaller manageable subtasks. In this approach, quantum channels, realized for instance through physical rerouting of qubits or quantum teleportation, connect multiple modules. Each of those modules hosts a subset of qubits, e.g. multiple logical qubits, and provides quantum operations on them. In this work, we implement for the first time all logical operations required for modular fault-tolerant universal quantum computing with a non-Calderbank-Shor-Steane (CSS) code, the perfect $[[5, 1, 3]]$ code, on a trapped-ion quantum computer. This code is the smallest quantum error-correcting (QEC) code capable of correcting any single-qubit error, making it a compact alternative to larger CSS codes. We demonstrate logical state teleportation and a full suite of fault-tolerant operations required for universal logical control, including logical state preparation, QEC with real-time feedback, logical measurements, magic-state preparation, logical entangling operations, and magic-state injection. Moreover, we characterize the logical spectator error picked up by idling logical qubits during quantum operations on distinct qubit registers and demonstrate a logical Pauli quantum process tomography that minimizes required sampling resources for logical tomography.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22661v1
- Title: Thermometry in Near-Degenerate Nitrogen-Vacancy Ensembles Enabled by Bright-Dark-State Mixing
- Authors: Matt K. Fu, John O. Dabiri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22661v1  pdf=https://arxiv.org/pdf/2609.22661v1.pdf

Abstract:
Nitrogen-vacancy (NV) centers have emerged as a highly sensitive platform for spatially resolved temperature measurements. When the $\lvert0\rangle\to\lvert+1\rangle$ and $\lvert0\rangle\to\lvert-1\rangle$ transitions are nearly degenerate and the Rabi frequency is comparable to the transition splitting, the spin dynamics encountered during pulsed protocols for temperature measurement can significantly alter the intended accumulation of temperature-dependent phase. We investigate these triplet ($\lvert0\rangle$, $\lvert\pm1\rangle$) spin dynamics and their effect on pulsed thermometry protocols under these conditions. We find that the conventional thermal-echo timing produces negligible temperature-sensitive signal amplitudes at the common-mode detuning. However, we find that the nominal spin-echo timing produces resolvable oscillations at the common-mode detuning, leading to a strong temperature-sensitive carrier signal. This departure from the expected protocol behavior is qualitatively captured by an ensemble model of the triplet dynamics, which supports significant dark-state leakage as a plausible mechanism for the temperature-sensitive response. This mixing-enabled thermal echo uses a four-phase quadrature readout that resolves the signed oscillation frequency and is validated using independent sweeps of the microwave carrier frequency and fluid temperature. We further assess the ability of a four-refocusing-pulse (LDD4B) low-field dynamical-decoupling sequence to extend the NV coherence and find that while the echo retains a sensitivity to common-mode detuning, the effective phase-accumulation interval corresponds to approximately half the total evolution time. These findings could support the use of pulsed NV thermometry in biological or mobile applications where applying magnetic bias fields is impractical and microwave power may be limited.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22669v1
- Title: Metric Self-Dual Completion and Optimal Additive Hardness for Quantum and Graph-State Distance
- Authors: Rafail Ostrovsky
- Categories: quant-ph (primary); quant-ph; cs.CC; cs.IT
- Links: abs=https://arxiv.org/abs/2609.22669v1  pdf=https://arxiv.org/pdf/2609.22669v1.pdf

Abstract:
We prove that the quantum code distance is NP-hard to approximate within an additive error of $c N$, for some constant $c >0$, where $N$ is the number of qubits. Our reductions are deterministic. This improves the previous square-root additive gap to $Ω(N)$ and resolves the explicitly stated linear-gap question of Kapshikar and Kundu. Our result holds for CSS codes with identical $X$- and $Z$-check spaces, and with a constant rate and constant relative distance. For every fixed $λ>1$, there is a constant $c>0$ such that hardness still holds even when every nonidentity stabilizer has weight greater than $λ$ times the quantum distance. We also improve the hardness gap of graph state distance on $N$ vertices of Grigorescu, Jha, and Samperton from cube-root to $Ω(N)$, resolving their explicitly stated open question. Both hardness results are asymptotically optimal since both distances are at most $N$. Our graph state distance hardness result holds for balanced bipartite graphs with a binary adjacency matrix that is its own inverse (mod 2).   Our main technique for both hardness bounds above is classical: we show how to convert any code $C$ of length $m$ into a self-dual code $A(C)$ of length $N=Θ(m)$ while exactly doubling the original coset metric. The conversion is deterministic and efficient. We call it the metric self-dual completion of $C$. It comes with a linear embedding $τ: \mathbb F_2^m \hookrightarrow \mathbb F_2^N$. The embedding doubles all Hamming distances between vectors in $\mathbb F_2^m$ and all pairwise distances between corresponding cosets. The embedding also guarantees that all codewords of $A(C)$ of weight at most $2m$ are exactly $τ(C)$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22673v1
- Title: Collective Chirped STIRAP in a Pair of Three-Level Atoms: Dressed-Manifold Dynamics and Compensation of the Rydberg-Rydberg Interaction-Induced Detuning
- Authors: Vladimir V. Malinovsky, Svetlana A. Malinovskaya
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22673v1  pdf=https://arxiv.org/pdf/2609.22673v1.pdf

Abstract:
We investigate collective chirped stimulated Raman adiabatic passage (STIRAP) in a pair of identical three-level atoms using a symmetric six-state model. Numerical simulations reveal a pronounced oscillatory dependence of the population transfer to the doubly excited Rydberg state on the peak Rabi frequency, indicating dynamics beyond the conventional single-dark-state description of STIRAP. To identify the underlying mechanism, we develop a dressed-manifold description based on gauge-invariant projections onto nearly degenerate instantaneous dressed manifolds. The analysis demonstrates that the wavefunction remains predominantly confined to a two-dimensional dark manifold while becoming transiently coupled to a neighboring bright manifold during the pulse-overlap interval. We further show that in the dressed-manifold representation, the Rydberg-Rydberg interaction modifies the collective resonance structure while preserving the dark-bright manifold dynamics responsible for the oscillatory transfer; an appropriately chosen frequency chirp compensates the interaction-induced detuning and restores efficient population transfer. This dressed-manifold picture provides a consistent interpretation of oscillatory collective transfer and establishes a framework for controlling adiabatic dynamics in interacting multilevel systems by linearly chirped STIRAP, opening a route toward manifold-based control of Rydberg-mediated quantum gates, correlated-state preparation, and other coherent operations in interacting atomic systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22728v1
- Title: Concatenated Composite Pulses Beyond Local Residual-Error Preservation
- Authors: Masamitsu Bando
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22728v1  pdf=https://arxiv.org/pdf/2609.22728v1.pdf

Abstract:
Residual-error preservation (REP) provides a sufficient rule for constructing concatenated composite pulses that compensate multiple systematic errors. We show that local REP is not necessary: deviations from REP can cancel across the full sequence. Using first-order error generators, we derive a necessary and sufficient condition for concatenation to retain the robustness of an outer sequence. A simple sufficient condition is that all inner pulses rescale the corresponding elementary error generators by a common real factor, not necessarily unity. We illustrate this principle using pulse-length and off-resonance errors, two systematic error models commonly considered in magnetic resonance. Short CORPSE and SCROFULOUS each compensate one error without preserving the other locally. Combining these inner pulses with suitable equal-rotation-angle outer sequences yields simultaneous first-order compensation of both errors, extending concatenated composite-pulse design beyond local REP.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22748v1
- Title: Feasibility and optimum recovery in warm-start quantum optimization for a drug-response model on a trapped-ion processor
- Authors: Tanzir Hossain, Rajib Rana, Prabal Datta Barua, Abu Ali Ibn Sina, Niall Higgins, Pascal Elahi, Robert Sang, Bjorn W. Schuller
- Categories: quant-ph (primary); quant-ph; cs.ET
- Links: abs=https://arxiv.org/abs/2609.22748v1  pdf=https://arxiv.org/pdf/2609.22748v1.pdf

Abstract:
On a seven-compound drug-response model, warm-start quantum approximate optimization (QAOA) on IonQ Forte-1 returned valid assignments more often than random bitstrings, but this alone did not show effective optimization. Ideal QAOA raised optimum probability above uniform feasible sampling in only four of twelve reference circuits. Hardware often fell below its own noiseless circuits, while greedy search solved all hardware models within 200 objective evaluations. Expanded simulations showed a gain over feasible sampling in 28 of 35 CAMA-1 panels and none of four 647-V panels. Annealing solved all these panels in every seed. A Grover mixer preserved feasibility and improved optimum probability over feasible sampling in all ten tested models. We analyzed 25 completed tasks containing 5,300 shots from 18 circuits and 14 instances. The encodings use 6-35 qubits and at most 4,900 feasible assignments, which we enumerated to establish exact optima. Noiseless references now cover both the original six circuits and six wider circuits. At 35 qubits, with 4,900 feasible assignments, ideal feasibility was 35.85%, compared with 7 of 200 valid hardware outputs. Its ideal optimum probability was below both sampling controls. The circuits sample assignments in a model built from measured single-agent and pairwise responses.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22768v1
- Title: Neural network-based multipartite entanglement classification with prior guidance from quantum uncertainty relations
- Authors: Qiyi Li, Xiao Zheng, Guofeng Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22768v1  pdf=https://arxiv.org/pdf/2609.22768v1.pdf

Abstract:
Quantum entanglement is a crucial resource in quantum information processing, yet its efficient, scalable and robust classification in multipartite systems remains theoretically challenging. Although supervised machinelearning has been applied to this task, most existing methods still suffer from high measurement costs, computational consumption, and weak noise robustness. In this work, by incorporating multipartite uncertainty relations as prior guidance, we propose a neural network approach to classify distinct Stochastic Local Operations and Classical Communication (SLOCC) multipartite entanglement classes based on states sampled from their local unitary (LU) orbits. Compared with traditional techniques, our method reduces experimental measurement-resource requirements and computational overhead, showing high adaptability to large-scale systems. The classification accuracy of our method reaches 99.5% in 20-qubit systems. The numerical validation is performed on states generated by random LU transformations, which preserve the SLOCC class. Within this setting, the proposed method offers strong effectiveness, scalability, and robustness for multipartite entanglement classification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22791v1
- Title: Gaussian quantum reservoir computing with a hybrid cavity magnomechanical system
- Authors: Hajar Assil, Khadija El Anouz, Abderrahim El Allati, Gian Luca Giorgi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22791v1  pdf=https://arxiv.org/pdf/2609.22791v1.pdf

Abstract:
We propose a quantum reservoir computing framework based on a hybrid cavity magnomechanical system in the linearized Gaussian regime. The reservoir combines microwave-cavity, magnon, and mechanical degrees of freedom, and is extended by an auxiliary cavity acting as an input port, with time-dependent signals encoded in its detuning. The covariance matrix of the quadrature fluctuations provides the features for a trained linear readout. Using linear-memory, nonlinearmemory, and parity-check benchmarks, we find strong temporal memory together with more limited nonlinear processing, whose balance is controlled by the reservoir evolution time, and we show that intermode correlations substantially enhance the information accessible to the readout. The same architecture reconstructs a time-dependent signal encoded in the auxiliary-cavity detuning, with an accuracy governed by the interplay between the internal couplings and the encoding strength, and robust against Gaussian detuning noise. Accounting for finite measurement statistics reveals a trade-off between encoding strength and the precision of the covariance estimation, so that the optimal encoding depends on the available measurement budget. These results establish hybrid cavity magnomechanical systems as a promising platform for continuous-variable quantum reservoir computing with potential applications in signal probing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22815v1
- Title: Asymmetric Two-Way Gaussian Quantum Steering in Coupled Lossy Waveguides
- Authors: Hafsa Zia, Haleema Sadia Qureshi, Shakir Ullah, Mohamed Amazioug, Fazal Ghafoor
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22815v1  pdf=https://arxiv.org/pdf/2609.22815v1.pdf

Abstract:
Quantum steering is an important type of quantum correlation with potential applications in one-sided device-independent (1SDI) quantum information protocols. In this contribution, we explore the time-dependent dynamics of Gaussian quantum steering in coupled lossy optical waveguides using the covariance matrix formalism. Optical dissipation is explicitly incorporated to account for realistic propagation losses in coupled waveguides. We systematically investigate the influence of the optical loss rate, purity, nonclassicality, and squeezing of the input Gaussian states on the generation and evolution of steering. The results demonstrate that increasing nonclassicality and squeezing enhances Gaussian steering, while optical loss and reduced purity progressively suppress it. However, a considerable amount of steering can persist over finite propagation intervals in the presence of optical loss. We further examine that steering is symmetric for input states with identical nonclassicality, while unequal nonclassicalities lead to directional steering asymmetry, offering a way to control the steering direction through input-state engineering. These results demonstrate that coupled optical waveguides can support controllable Gaussian quantum steering under practical loss conditions and offer a promising integrated-photonic platform for asymmetric quantum-information protocols, including 1SDI quantum key distribution (QKD) and quantum communication.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22821v1
- Title: Overcoming the Quasi-Static Bottleneck: A Finite-Time Quantum Otto Information Engine Achieving Near-Unity Efficiency
- Authors: Yang Xiao, Jin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22821v1  pdf=https://arxiv.org/pdf/2609.22821v1.pdf

Abstract:
Generally, quantum heat engines driven by Gibbs reservoirs achieve their maximum work and efficiency only in quasi-static processes, a constraint that hampers practical applications due to the resulting vanishing power output. To address this fundamental limitation, we propose a finite-time quantum Otto information engine (OIE) driven by a Maxwell's demon paired with a single Gibbs reservoir. We demonstrate that the demon's measurement and feedback control can preserve quantum coherence to extract coherent work, while harnessing quantum internal friction as a work source. Consequently, the OIE can produce work by only modulating the eigenstates of the Hamiltonian, and surpass the quasi-static limits of its conventional counterpart in the work output and the efficiency, which accounts for the energetic cost of the demon. Notably, the OIE can achieve near-perfect efficiency alongside positive work extraction in the rapid-driving regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22822v1
- Title: From IceCube to IT-Sphere: A Hybrid Quantum-Classical GNN for Banking IT Root Cause Analysis
- Authors: Antonio Greco, Riccardo Paoletti, Roberto Cappuccio, Mario Onorato
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22822v1  pdf=https://arxiv.org/pdf/2609.22822v1.pdf

Abstract:
We present Hybrid Quantum Root Cause Analysis (HQ-RCA), an industrially grounded workflow for root cause analysis in banking IT operations, built on a hybrid Quantum Graph Neural Network (QGNN): the classical backbone of DynEdge (the IceCube neutrino-reconstruction GNN, which we call standalone DynEdge), with its classification head replaced by a Variational Quantum Circuit (VQC). On 13 months of anonymised IT data (13k alarm clusters) from a major European bank, the hybrid QGNN matches standalone DynEdge -- the strongest classical baseline -- on $F_1$, while standalone DynEdge leads the ranking metrics. A readout-sensitivity and layout-robustness study, analysed via Dimensional Expressivity Analysis (DEA), shows that the effective parameter dimensionality (rank) of the quantum observable has no measurable correlation with $F_1$; we therefore keep the simplest readout $\langle Z_0\rangle$ (the Pauli-$Z$ expectation on the first qubit), which in the deployed layout is rank-1, collapsing optimisation to a 1-D problem solvable by a gradient-free grid scan. Execution on IBM Heron r2 (no error mitigation) shows this gradient-free readout is executable on NISQ hardware after threshold recalibration.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22826v1
- Title: The Filtering Demon: Beyond Standard Thermodynamic Bounds and Harnessing Measurement Error and Quantum Friction
- Authors: Yang Xiao, Jin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22826v1  pdf=https://arxiv.org/pdf/2609.22826v1.pdf

Abstract:
Standard stochastic heat engines operate blindly, enforcing work extraction protocols indiscriminately on microstates, and consequently suppressing work output, stability, efficiency. To overcome this, we propose an Otto information engine (OIE) that employs a Maxwell's demon to filter out detrimental stochastic trajectories, and demonstrate that the OIE can provide enhanced work output and stability compared to the corresponding standard Otto engine. Remarkably, even after accounting for the energetic costs of the demon, the OIE efficiency surpasses both the standard Otto limit and Carnot bound. Furthermore, by applying the fluctuation theorem of information dissipation, we derive upper and lower bounds on efficiency, confirming that our results adhere to the second law of thermodynamics. Finally, and counterintuitively, measurement errors and quantum inner friction, traditionally considered deleterious, can be harnessed as resources, which improves robustness and enables us to ignore the adiabatic strokes time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22831v1
- Title: Unbounded Work Extraction and Zero Work Fluctuations in a Super-Carnot Otto Information Engine
- Authors: Yang Xiao, Jin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22831v1  pdf=https://arxiv.org/pdf/2609.22831v1.pdf

Abstract:
Generally, the work output of stochastic heat engines is governed by the stochastic trajectory distribution and the energy spectrum. Because the trajectory distribution depends on the thermal reservoir temperatures, the work output is not only constrained by temperature but is also susceptible to thermal fluctuations. To address these limitations, we introduce two continuous Maxwell's demons into a quantum Otto cycle, forming an Otto information engine (OIE). We demonstrate that the work output of the OIE depends solely on the energy level gap, enabling arbitrary work extraction while eliminating work fluctuations, thereby ensuring cycle-to-cycle identical work output. Furthermore, we show that the engine's efficiency can surpass the standard Carnot efficiency even after accounting for the energy cost of demon's memory erasure. Finally, we show that the OIE can deliver superior output power even when the demon's measurement time is taken into account, and the corresponding Monte Carlo simulation has been executed.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22902v1
- Title: Characterizing local unitary equivalence of multipartite states by local unitary Bargmann invariants
- Authors: Yi Shen, Lin Chen, Shao-Ming Fei
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22902v1  pdf=https://arxiv.org/pdf/2609.22902v1.pdf

Abstract:
Local unitary (LU) equivalent states are crucial for understanding the structure of quantum entanglement. We investigate the LU equivalence based on the LU Bargmann invariants (LUBIs). We consider for which states the LUBIs are sufficient to ensure the LU equivalence. We focus on a class of multipartite states with complete local commutativity, called CLC states. We first show that for multipartite CLC states, all the LUBIs are sufficient to ensure the local permutation equivalence, if their single-party marginals are diagonal and non-degenerate. By virtue of the fact that the CLC property remains unchanged under local operations, we verify that the LUBIs are also sufficient to ensure the LU equivalence of multipartite CLC states whose single-party marginals are non-degenerate. Furthermore, when the single-party marginals are degenerate, we propose concrete examples of two-qudit and three-qubit systems, showing that there are states which share all the LUBIs but are not LU equivalent.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22937v1
- Title: Efficient creation of shallow NV$^-$ ensembles by high-angle ion implantation
- Authors: Kento Sasaki, Hideyuki Watanabe, Tokuyuki Teraji, Takashi Taniguchi, Kenji Watanabe, Kensuke Kobayashi
- Categories: quant-ph (primary); quant-ph; cond-mat.mtrl-sci
- Links: abs=https://arxiv.org/abs/2609.22937v1  pdf=https://arxiv.org/pdf/2609.22937v1.pdf

Abstract:
Negatively charged nitrogen-vacancy (NV$^-$) centers located a few nanometers below the diamond surface are key quantum defects for nanoscale sensing of external spins. However, the creation of shallow NV$^-$ centers with high yield remains a materials challenge. Here, we demonstrate that high-angle ion implantation enhances the creation efficiency of shallow NV$^-$ centers. By implanting $^{15}$N ions at angles exceeding 60$^\circ$, we achieve high NV$^-$ yields approaching 10% with effective NV$^-$ depths below 10 nm. These yields are significantly higher than those typically reported for shallow NV$^-$ creation. The enhanced NV$^-$ yield is consistent with an increased vacancy-to-nitrogen ratio in the near-surface region, which is expected to promote NV formation during annealing. The created NV$^-$ ensembles show coherence properties comparable to those of single shallow NV$^-$ centers at similar depths, and allow detection of nuclear spins in van der Waals materials attached to the diamond surface. Our results establish geometric control of ion implantation as a simple and broadly applicable approach to engineer shallow vacancy-related quantum defects.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22946v1
- Title: Secure Quantum Metasurfaces for Direct Quantum Key Distribution Measurements
- Authors: Yan He, Adetunmise C. Dada
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2609.22946v1  pdf=https://arxiv.org/pdf/2609.22946v1.pdf

Abstract:
Quantum key distribution (QKD) can deliver information-theoretic security, but its receivers are still typically assembled from cascaded bulk optics. Metasurfaces offer a radical reduction in this complexity. Here, we make the metasurface function as the QKD measurement device itself. We design wavelength-specific dielectric apertures at 780, 1550, 2000, and 10 600 nm that interweave the linear H/V and circular R/L phase libraries at a 0.44--0.49λ cell pitch, i.e., below half the operating wavelength, and map the complete passive-BB84 measurement directly onto four detector channels. This subwavelength basis co-location prevents an ordinary propagating-wave aperture mask from isolating one basis without simultaneously attenuating or perturbing the other. Simulated full-wave focal-plane intensities are converted directly into conditional Born probabilities using fitted, calibration-fixed detector regions. The selected designs achieve probability fidelities of 97.96--99.08%, four-port collected efficiencies of 17.43--40.94%, and mean intrinsic quantum bit error rates of 1.42--3.96%. At 1550 nm, the selected design gives an asymptotic device-level yield of 0.151 secret bits per incident photon under an ideal single-photon model. Six-state detector tomography gives positive both-basis security bounds for all six reconstructed receiver models, including their polarization-dependent loss, basis imbalance and crosstalk. These results establish protocol-matched meta-optics as a route to compact, passive QKD receivers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22965v1
- Title: Exact Realization of Deep ReLU Computation in a Microscopic Statistical-Mechanical System
- Authors: Junxu Li
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2609.22965v1  pdf=https://arxiv.org/pdf/2609.22965v1.pdf

Abstract:
Understanding the physical origin of the piecewise-linear computation in deep rectified linear unit (ReLU) networks remains a fundamental challenge. Here we establish an exact statistical-mechanical realization of arbitrary ReLU networks. Starting from a microscopic configuration space and its state multiplicities, we construct a partition function without prescribing a neural-network activation function. The resulting system admits equivalent descriptions in terms of cascaded quantum operations with post selection, or fermionic transport model. We rigorously prove that in $β\to+\infty$ limit, the thermodynamic observables of this system exactly reproduce the hidden states, outputs, and loss function of an arbitrary deep ReLU network. Crucially, we demonstrate that the piecewise-linear behavior of the ReLU network emerges from a first-order phase transition in the microscopic system, where the discontinuities precisely coincide with the boundaries of linear regions of ReLU network. This work establishes an exact physical foundation for deep neural computation and provides a novel statistical-mechanical perspective on neural architecture design.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22976v1
- Title: Weak Values Beyond the Weak Limit: Measurement-Strength Invariance Under Post-Selection
- Authors: Cosmin Andrei, Vlatko Vedral
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22976v1  pdf=https://arxiv.org/pdf/2609.22976v1.pdf

Abstract:
Weak values are conventionally extracted in the limit of vanishing measurement strength. At finite strength, the corresponding post-selected conditional averages generally acquire nonlinear corrections and need not retain their weak value interpretation. Here we identify a class of measurement protocols for which this expectation fails: the conditional value reconstructed from the measuring probe is exactly independent of the probe strength and therefore coincides with the real part of the weak value. We first analyze this phenomenon in the measurement--disturbance protocol introduced by Lund and Wiseman. We then establish conditions under which this invariance persists, showing that it is determined by the interplay between the probe interaction, a subsequent measurement interaction with an ancillary apparatus, and the final post-selection. These results demonstrate that weak coupling, although generally sufficient for accessing weak values, is not always necessary.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22998v1
- Title: The Generalised Causality Principle
- Authors: Sahil Gopalkrishna Naik
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.22998v1  pdf=https://arxiv.org/pdf/2609.22998v1.pdf

Abstract:
The no-signalling principle lies at the heart of Bell-type experiments involving spacelike-separated parties. Although not all no-signalling correlations can be realized within quantum theory, the no-sinalling principle itself remains fundamental even for post-quantum theories, since its violation would imply superluminal signalling. In the spirit of device independent nature of the Bell inequalities, there has recently been growing interest in causal inequalities, which identify correlations admitting no causal explanation. Such correlations have been rigorously studied within the process-matrix formalism, which is built upon a constraint analogous to spacelike separation in Bell scenarios. We refer to this constraint as the single-interaction constraint, whereby each party interacts with the environment only once. Despite considerable effort, no fundamental guiding principle is currently known that characterizes the restrictions this constraint imposes on the correlations generated by Process Matrices. In this work, we address this gap by proposing a generalized causality principle for the bipartite case. We show that for certain cases, the generalised causality principle defines a strict subset of the set of all signalling correlations. This principle thus provides a fundamental limit on quantum and even post-quantum theories subject to the single-interaction constraint. By analogy with no-signalling, whose violation excludes certain causal structures among the parties, a violation of the generalised causality principle rules out a corresponding class of causal structures(causal structures with the single interaction constraint). More broadly, our techniques provide a general framework for deriving generalised causal constraints, applicable to a wide class of indefinite-causal-order scenarios.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23016v1
- Title: Watching Quantum Models Think: Hilbert-Space Interpretability in Quantum Transformer Blocks
- Authors: Diego Iacopetta, Andrea Gasparini
- Categories: quant-ph (primary); quant-ph; cs.AI; cs.LG
- Links: abs=https://arxiv.org/abs/2609.23016v1  pdf=https://arxiv.org/pdf/2609.23016v1.pdf

Abstract:
Deep learning models are powerful but opaque. As quantum machine learning matures, the field faces a defining choice: build quantum models that are equally opaque, or exploit the mathematical structure of quantum mechanics to make them inherently interpretable. We show that the latter is possible. By tracking quantum mutual information~(MI), entanglement entropy, and state fidelity through the layers of a Quantum Transformer Block (\qtb{}), a fully-coherent variational circuit with quantum analogues of both attention and feedforward, we gain direct insight into how the model processes information: which tokens it attends to, when correlations form, and why predictions fail. On four tasks with known dependency structure we show that (i)~learned MI matrices align with ground-truth task structure (AUC$\,{=}\,0.69$ on lookup), (ii)~disabling entangling gates collapses accuracy from 100\% to 15\% while MI$\to 0$, proving entanglement is the mechanism, (iii)~accuracy and MI co-evolve during training ($ρ\,{=}\,0.92$ on lookup), and (iv)~per-sample MI predicts prediction correctness on the conditional task with ROC AUC$\,{=}\,0.84$. All results are validated on IBM Quantum hardware (ibm\_kingston, Heron~r2): the circuit's reasoning process, from product state through structured entanglement, is directly observable on a superconducting processor. These proof-of-concept results, obtained on small synthetic tasks, suggest that the physics of quantum computation can provide intrinsic interpretability signals with no direct classical counterpart, motivating study of whether this advantage persists at scale.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23020v1
- Title: An attainable Gill-Massar-type bound for spin-factor models
- Authors: Koichi Yamagata
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23020v1  pdf=https://arxiv.org/pdf/2609.23020v1.pdf

Abstract:
We determine the exact local precision limits for single-copy estimation of smooth multiparameter quantum statistical models contained in spin factors, a class of matrix Jordan algebras whose state spaces generalize the qubit Bloch ball. At any parameter point where the symmetric logarithmic derivative (SLD) Fisher information is positive definite, we characterize the entire attainable classical Fisher-information region over all finite-outcome positive-operator-valued measurements. After SLD normalization, this region consists exactly of the real symmetric positive semidefinite matrices with trace at most one, independently of the ambient Hilbert-space dimension. This yields a sharp weighted covariance bound for every positive definite weight, attained by an explicit locally unbiased estimator based on randomized spectral measurements of SLD directions. The proof combines a statistics-preserving positive projection onto the spin factor with the two-eigenvalue structure of its effects, revealing the Jordan-algebraic origin of the tradeoff. The result extends the qubit information tradeoff to models with more than three parameters. Since the optimal measurement depends on the unknown parameter, we simulate an adaptive scheme for a five-parameter model on a four-dimensional Hilbert space and observe performance close to the optimal local benchmark.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23041v1
- Title: The Requirement of (at least) Complex Structure for Quantum Mechanics
- Authors: M. P. Vaughan
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2609.23041v1  pdf=https://arxiv.org/pdf/2609.23041v1.pdf

Abstract:
It is argued that many real-valued constructions of quantum mechanics are only \emph{nominally} real in that the operators and states are restricted to impose a \emph{complex structure} on the Hilbert space. That is, complex algebra between pairs of elements representing complex numbers is preserved in these formulations. It is therefore mistaken to think of these constructions as being `real' as they are actually a representation of complex linear algebra. It is then shown that under the assumptions of state normalisation and strict energy conservation, this complex structure (at the very least) is required to allow for time evolution in quantum mechanics. This is only a \emph{minimum} requirement, as our arguments do not preclude the formulation of quantum mechanics in terms of hyper-complex entities, such as quaternions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23046v1
- Title: Universality in Terms of The BECs Bloch-Sphere Manipulations
- Authors: Genji Fujii
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23046v1  pdf=https://arxiv.org/pdf/2609.23046v1.pdf

Abstract:
Quantum computing promises to outperform classical computing for certain computational tasks. One of the key concepts underlying this potential is universality. Universality has been extensively studied not only for qubits but also for higher-dimensional quantum systems, such as qutrits and qudits, which span Hilbert spaces of dimension greater than two. However, the concept of universality in Bose-Einstein condensates (BECs) qubit systems, which have been proposed relatively recently, remains insufficiently understood. In this work, we analyzed universality in BECs qubit systems. Our results clarify the theoretical aspects of universality in quantum computation within the class of ((N+1))-dimensional representations of SU(2), taking into account two distinct representations of the quantum states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23047v1
- Title: Where to Decide: Control-Plane Geometry in Coherence-Limited Quantum Networks
- Authors: I. Dey, N. Marchetti
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23047v1  pdf=https://arxiv.org/pdf/2609.23047v1.pdf

Abstract:
Quantum networks are usually framed by two hardware limits: how fast entanglement can be heralded, and how long a memory can hold it. We establish a third, geometric limit: entanglement decoheres while control information travels, so the distance to whoever allocates resources enters the fidelity budget directly. We develop a functional-graph abstraction weighting each link by its predicted multiplicative contribution to end-to-end fidelity, separating global but delayed state from local and immediate state, and compare centralized against local allocation in a replicated discrete-event model. Centralized delivery latency grows with network diameter while local latency is nearly scale invariant, differing up to twenty-fold for short-range traffic; the coherence threshold at which a global view outweighs a fresh one does not shift across the tested sizes; and as heralding accelerates, the dominant cost moves into the control plane. Slot synchronization instead obeys the product of slot rate and one-way link delay, so it is bounded by repeater spacing rather than diameter. Controller placement, decision locality, repeater spacing and slot rate are physical design parameters, not implementation details.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23050v1
- Title: A Coherent Memory Register for Sequential Quantum Generative Modeling, with Application to Calorimeter Showers
- Authors: Jamal Slim. Saverio Monaco, Ran Xue, Dirk Kruecker, Kerstin Borras
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23050v1  pdf=https://arxiv.org/pdf/2609.23050v1.pdf

Abstract:
Simulating the showers that particles deposit in a calorimeter, the detector that records their energy across many cells, is one of the largest computing costs in high-energy physics, and fast generative surrogates are needed. Quantum circuits have been proposed as such surrogates, but demonstrations on calorimeter data have either required a register that grows with the image, roughly one qubit per cell, or have passed the information between parts of the image through a classical channel. We remove both constraints for this problem, using a construction drawn from the sequential-generation and hidden-quantum-Markov-model literature. A shower image is generated block by block on a fixed register of six qubits. Three of them, the memory, are never measured. They hold what the circuit knows about the blocks already generated as a quantum state, so the correlations between distant parts of the image cross each block boundary as unmeasured amplitudes. The other three are measured and reset once per block, and each outcome selects the energy pattern of one block. The register size is set by the block, so adding cells to the image adds steps to the sequence, not qubits. We call the model a coherent-memory Born machine (CoMB), a Born machine being a circuit whose measurement statistics are the generated distribution. Its training loss grows only linearly with the number of blocks and never requires enumerating the image distribution, and a depth-two instance runs on an IBM superconducting processor. On a twelve-cell benchmark the model reproduces the energy distribution of every cell, the correlation matrix between cells, and the total-energy spectrum. Removing the three memory qubits, with everything else unchanged, produces independent blocks. Every correlation between blocks is carried by the unmeasured qubits and by nothing else.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23057v1
- Title: A Quantum-Inspired Two-Dimensional Lattice Polarized Radiative Transfer Simulator
- Authors: Shan Zeng, Bing Lin, Ali Omar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23057v1  pdf=https://arxiv.org/pdf/2609.23057v1.pdf

Abstract:
A quantum inspired framework was developed for polarized radiative transfer in the atmosphere to jointly model multiple scattering, absorption, and emission processes. The radiative field is represented by the Stokes vector and discretized using an n-directional two-dimensional spatial lattice on 3-dimensional uniformly distributed zenith and azimuth angular vectors. The formulation of this quantum computation system is based on the Lattice Boltzmann Method, which incorporates a physics-based polarized phase matrix. A classical lattice solver employing identical spatial and angular discretization and physical modeling as in quantum algorithm is implemented. The corresponding quantum algorithm is evaluated using the IBM Qiskit quantum simulator, enabling direct comparison of numerical accuracy to a classical simulation reference. The results demonstrate that fully physics-based polarized radiative transfer can be embedded within a quantum lattice framework, which provides an initial benchmark toward scalable quantum atmospheric radiative transfer and future quantum climate modeling

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23059v1
- Title: clifford qc: A Python Toolkit for Quantum Simulation
- Authors: Ginanjar Utama, Hermawan Kresno Dipojono
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23059v1  pdf=https://arxiv.org/pdf/2609.23059v1.pdf

Abstract:
clifford_qc is a Python research toolkit for constructing quantum models, comparing variational and subspace eigensolvers, and estimating measurement resources. A common sparse Pauli algebra connects Hamiltonians, density operators, gates, and candidate-selection observables, while dedicated interfaces handle circuit programs, execution, and statistical estimates. We introduce the representation with a worked gradient example and trace a molecular calculation through reusable model preparation, an independent solve, and optional reference validation. Shared measurement caches reuse outcomes across observables on the same reference state; packed coefficient storage and streaming expose a memory-recomputation tradeoff. Committed small-system benchmarks show how these interfaces support comparisons with explicit accuracy and cost assumptions. Fully commuting measurement reduces the shots needed to certify a fixed first-order energy functional, but entangling-gate time and connectivity can offset the saving or make the protocol inadmissible under illustrative device models. Other studies identify a subspace bias floor that more shots cannot remove, an indeterminate comparison of fermionic encodings across instances, and an approximate-restriction screen whose required comparison fails before sampling. Generated tables, provenance records, and manuscript checks connect the reported claims to their inputs, although evidence labels are not yet validated uniformly. The package supports reproducible method development; these results establish neither hardware performance nor a general simulation speedup.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23126v1
- Title: Performance optimization of cascaded traveling wave Josephson parametric amplifiers
- Authors: Ilari Lilja, Ekaterina Mukhanova, Stanislav Khaldeev, Ilya Golokolenov, Visa Vesterinen, Pertti Hakonen
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2609.23126v1  pdf=https://arxiv.org/pdf/2609.23126v1.pdf

Abstract:
Traveling-wave parametric amplifiers (TWPAs) based on Josephson metamaterials provide broadband gain with near-quantum-limited added noise. Whereas long nonlinear metamaterial devices can deliver high gain, short arrays suffer less from dissipation, pump depletion, and internal standing waves which can degrade noise performance. Here, we demonstrate a cascaded TWPA architecture that combines the advantages of both approaches by employing a short (736-element), low-dissipation Superconducting Nonlinear Asymmetric Inductive eLement (SNAIL)-based TWPA as the first amplification stage, followed by a conventional long (1632-element) TWPA that provides additional gain. The resulting amplifier cascade achieves nearly 30 dB of total gain over a tunable bandwidth of approximately 1 GHz while maintaining added noise close to the quantum limit. Our results establish a cascade of TWPAs as a practical approach for high-gain, broadband, quantum amplification with applications in quantum information processing, multi-mode entanglement, and quantum sensing applications at microwave frequencies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23154v1
- Title: Quantum Hashing with QKD States
- Authors: A. V. Vasiliev, I. G. Zinnatullin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23154v1  pdf=https://arxiv.org/pdf/2609.23154v1.pdf

Abstract:
Quantum hashing is a well-known technique. In this paper, we present a new construction of a quantum hash function based on binary error-correcting codes. The construction of the quantum hash strongly resembles the quantum state preparation in QKD protocols (e.g., BB84 protocol) and can be implemented on current QKD-devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23171v1
- Title: Deterministic synthesis and processing of frequency-bin qubits in a macroscopically coherent quantum memory
- Authors: S. A. Moiseev
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2609.23171v1  pdf=https://arxiv.org/pdf/2609.23171v1.pdf

Abstract:
Quantum information processing requires efficient storage and manipulation of photonic states.Here, we advance a cavity-assisted quantum memory protocol based on Pre-created Long-lived Macroscopic (PLM) coherence, thereby transforming quantum memory from a passive storage device into a platform for deterministic in-memory photonic processing. It is demonstrated that spin PLM coherence enables all-optical control of quantum memory using robust radio-frequency rotations alone. Here, the spin coherence serves as a distributed coherent quantum bus, which mediates the deterministic synthesis and storage of frequency-bin states through spectrally nonlocal impedance matching. We identify an inherent time-reversal symmetry in the underlying dynamical equations, ensuring unitary evolution of the quantum memory operations. The presented results demonstrate a unified platform for quantum storage and optical signal processing, enabling controlled manipulation of frequency-bin photonic qubits and paving the way for scalable multimode quantum networks based on spectral-encoding architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23180v1
- Title: Adaptive Differential Evolution and Multistart Search for Noisy QAOA Optimization
- Authors: Vojtěch Novák, Ivan Zelinka, Swagatam Das, Martin Beseda
- Categories: quant-ph (primary); quant-ph; cs.NE
- Links: abs=https://arxiv.org/abs/2609.23180v1  pdf=https://arxiv.org/pdf/2609.23180v1.pdf

Abstract:
We benchmark classical optimization of a fixed low-depth Quantum Approximate Optimization Algorithm (QAOA) ansatz across four cost-Hamiltonian families at $N=12$, $p=3$, and $D=6$. Ten optimizers are compared over 25 independent runs under common ceilings of 10\,000 and 30\,000 function evaluations (FEs), first with exact statevector objectives and then with two additive observation-noise levels. Exact objectives favor multistart BFGS and multistart CMA-ES. Under noisy feedback, adaptive population methods become more competitive, but the ranking depends on whether performance is measured by the best exact point visited or by the point selected from noisy observations. A targeted extension over all three pre-screened instances per family confirms this regime change while showing that named adaptive-DE winners are instance dependent: jSO-lite leads low-noise oracle search, iL-SHADE high-noise oracle search, and L-SRTDE high-noise selected solutions in the equal-instance summaries. Bootstrap analysis quantifies a non-negligible high-noise search--selection gap, and a retrospective fixed-budget verification proxy shows that reserving a small measurement budget for final re-evaluation improves selected quality across all ten methods at 30\,000 FEs. A supplementary structure-aware study further shows that QAOA cross-depth restriction and continuous basin refinement are more useful in these conditions than standalone Monte Carlo tree-search selection. Overall, optimizer choice depends jointly on landscape structure, observation noise, and final-point identification.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23189v1
- Title: Entangled measurements are necessary for optimal tomography of mixed fermionic Gaussian states and of bosonic Gaussian states near the vacuum
- Authors: Ron Rubin
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2609.23189v1  pdf=https://arxiv.org/pdf/2609.23189v1.pdf

Abstract:
We prove that learning an unknown mixed fermionic Gaussian state on $m$ modes to trace distance $ε$ requires $Ω(m^3/ε^2)$ copies when measurements act on one copy at a time, even with arbitrary POVMs, fresh ancillas and classical adaptivity, but without quantum memory between copies. The bound holds for $0<ε\le1/3600$ and separates this model from the known collective rate $Θ(m^2/ε^2)$. It follows from a uniform single-copy Fisher-information budget and a dimension-independent comparison between trace distance and Gaussian parameters. On covariance matrices of operator norm at most $1-c$, we prove a Frobenius-to-trace-norm continuity bound with constant $[2c(2-c)]^{-1/2}$; matchgate shadows then attain $O(m^3/(cε^2))$ copies. This also gives explicit error certificates for thermal free-fermion states. For a class of mixed passive bosonic Gaussian states with total mean photon number at most one, a reduction to bounded-block qudit tomography gives a single-copy lower bound $Ω(m^3/(ε^2\sqrt{\log(m/ε)}))$, versus collective complexity $Θ(m^2/ε^2)$. These separations answer the mixed-state measurement-resource question posed by Chen et al. A two-mode example has optimal two-copy Fisher trace $5$, versus the separable ceiling $4$. An IBM replication gave a pre-registered witness lower bound $4.12$ at one-sided $95\%$ shot-noise confidence; its interpretation assumes the prescribed preparations and a common measurement channel and does not bound preparation systematics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23190v1
- Title: QCMI-Based Quantum Markov Blanket Discovery for Semantic Quantum Networks
- Authors: Evangelos K. Markakis, Ilias Politis
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2609.23190v1  pdf=https://arxiv.org/pdf/2609.23190v1.pdf

Abstract:
Quantum-enabled semantic communication networks (QESCs) leverage quantum technologies to transmit data meaning efficiently, yet face challenges from costly resources and noise. This letter introduces Quantum Markov Blankets (QMBs) to QESCs, a novel framework to isolate essential quantum information for semantic transmission. We prove QMBs' validity using quantum conditional mutual information, showing that they shield semantic content from irrelevant subsystems. An implementation strategy optimises QMB detection, reducing resource use. Simulations suggest that QMB-based QESCs cut qubit consumption by 50\%-75\% while enhancing fidelity compared with non-optimised quantum semantic schemes. Unlike classical approaches, QMBs offer inherent security by limiting an eavesdropper's access to classical data outside the blanket. We outline future directions, including real-time QMB adaptation. This work bridges quantum information theory and semantic communication, advancing resource-efficient and secure quantum networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23195v1
- Title: Localized charges, reset noise, and boundary memory in matrix-product-conserving quantum chains
- Authors: Ron Rubin
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; math-ph
- Links: abs=https://arxiv.org/abs/2609.23195v1  pdf=https://arxiv.org/pdf/2609.23195v1.pdf

Abstract:
We construct boundary observables that retain memory for a quantified time window in quantum chains whose basis configurations carry a conserved ordered product of matrix labels. Under strong-irreducibility and proximality hypotheses on the label matrices, projective contraction of random matrix products localizes a conserved charge in the root-mean-square over uniform basis configurations. A finite-time inequality then converts readout overlap and reset leakage into a correlation bound: for a conserved reference observable $H$, a readout $F$, accumulated squared leakage $\mathcal B$, and the normalized Hilbert-Schmidt inner product, $\langle F,Φ(F)\rangle\ge 2\langle H,F\rangle^2/(\|H\|_2^2+\mathcal B)-\|F\|_2^2$. Here $Φ$ is a sequence of conserving channels and partial resets. The bound holds for each such circuit, without averaging its gates. It yields an exponential memory window in the distance from the noisy region, with quantitative corrections for spatially distributed noise and imperfect conservation. For a thirteen-state elementary-matrix model, exact polynomial certificates give root-mean-square localization error $e^{-r/1400}$ between the charge and its restriction to the last $r$ sites, and limiting variance at least $1/19$ for a rational charge. A related normalized-Gram charge gives an eight-site certificate retaining more than half the specified readout correlation through two boundary-reset rounds. Uniform depolarization imposes an inverse-noise-rate lifetime ceiling. A two-qubit IBM experiment illustrates the general reset inequality; it does not realize the matrix-product chain. We provide proofs, exact certificate programs, and an independent recount of the archived experimental outcomes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23221v1
- Title: A remark on the Brown-Susskind conjecture
- Authors: Jean-Luc Brylinski, Ranee Brylinski
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23221v1  pdf=https://arxiv.org/pdf/2609.23221v1.pdf

Abstract:
In the spirit of the Brown-Susskind conjecture, proven in \cite{haf} and \cite{li}, we study the growth of the dimension of the set of $n$-qubit unitaries which can be obtained as a product of a fixed number of $2$-qubit gates from a fixed set of pairs of qubits. We show that this dimension increases strictly when one more pair is added, for at least some choice of the $2$-qubit pairs at each step.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23234v1
- Title: Loss-Tolerant Quantum Position Verification for Metropolitan Area Networks
- Authors: Wen Yu Kon, Niccolò Bigagli, Andrew Conrad, Taylor Shields, Fatih Kaleoglu, Ignatius William Primaatmaja, Alexander Craddock, RJ Pisani, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23234v1  pdf=https://arxiv.org/pdf/2609.23234v1.pdf

Abstract:
A spacetime seal, a cryptographic guarantee that a digital event has occurred at an approved location and time, can augment a digital signature with location attestation for legal, financial, and regulatory use cases. In adversarial settings any purely classical realization of such a seal can be spoofed. Quantum position verification (QPV) offers a physics-based solution, exploiting the no-cloning theorem and the no-signaling principle to certify a party's spacetime coordinates. While the feasibility of QPV has been recently shown via entanglement- and coherent light-based protocols, achieving loss tolerance for these schemes substantially increases implementation complexity at metropolitan scales. Here, we introduce and experimentally demonstrate a loss-tolerant QPV (LT-QPV) protocol whose security is independent of channel loss. We prove finite-size security against quantum polynomial-time entangled adversaries in the quantum random oracle model instantiated with cryptographically secure hash functions. Implemented entirely with commercial off-the-shelf components, our system certifies position within 22 minutes of net data collection time against a restricted adversary, with a clear path to real-time certification (<1s) with upgraded hardware. Our architecture, requiring only a single quantum verifier node alongside classical infrastructure, is naturally compatible with metropolitan-area quantum networks, establishing the foundations for scalable, physics-backed spacetime certification as a deployable service.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23243v1
- Title: Resource and entanglement study of a hybrid qudit-qubit quantum algorithm for solving the integer programming problem
- Authors: Kapil Goswami, Rick Mukherjee, Peter Schmelcher
- Categories: quant-ph (primary); quant-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2609.23243v1  pdf=https://arxiv.org/pdf/2609.23243v1.pdf

Abstract:
Recently, a hybrid qudit-qubit algorithm [1] was presented for solving the integer programming problem with a polynomial quantum advantage. In this work, we investigate the algorithm [1] to understand the role of qudits ($d$-dimensional quantum system) by conducting a comparative resource analysis with its qubit-only implementation and the classical simulability of the algorithm by exploring the entanglement structure. The resource analysis part is performed in terms of logical gate counts, and fault-tolerant physical resources, including non-Clifford gates. The hybrid qudit-qubit implementation has a more compact structure of the unitary operators as opposed to its qubit-only simulation which reduces the logical and fault-tolerant resource requirements. Two example problems, one with qutrits ($d=3$) and the other with ququint ($d=5$), when contrasted with their qubit-only implementation, within a simplified fault-tolerant resource model, showed $\sim 180 \times $ and $\sim 2220\times$ fewer total resource count, respectively. For the entanglement study, volume-law-like entropy growth and signatures of multi-partite entanglement is observed leading to increasing difficulty in the classical simulation of the algorithm. The algorithm generates synergistic tri-partite entanglement even for a quadratic problem, revealing that the algorithmic structure itself can generate higher-order entanglement in the system independent of the problem.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23255v1
- Title: Complete Detector Records and Contextual Source Laws in a Retrocausal Spin Model
- Authors: D. M. Theshan N. Weerasinghe
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23255v1  pdf=https://arxiv.org/pdf/2609.23255v1.pdf

Abstract:
Detector outcome probabilities can be independent of a later measurement setting even when earlier timestamps, detector seeds, or environmental records depend on that setting. We characterize complete-record preservation for a positive wrapped-Cauchy retrocausal spin source. An antipodal identity yields necessary and sufficient conditions for passive and environmental readouts, and source compensation permits a common normalized analyzer for source spins and prepared continuations. Gaussian controller and reset calculations distinguish inverse raw history weights from normalized thermal operations. A quantum instrument provides an operational benchmark, whereas a setting-dependent separable source produces setting-dependent statistics at an earlier joint probe. For two equal-width contexts, a calibrated weak probe requires a minimum source change of $\operatorname{sech}(2g)/8$ in trace distance for exact protection at every nonzero strength. The signal--source-change tradeoff is sharp for this pair of contexts. A contextual positive-history construction recovers the isolated hidden law and preserves records for a specified class of finite adaptive quantum apparatuses, subject to quantum calibration and restricted field access. Direct readout of an added likelihood field distinguishes two future axes with unit probability. The analytical results are supported by continuous-angle and quantum-trajectory simulations, deterministic quadrature, and exhaustive enumeration of a finite policy class. The analysis concerns the specified statistical models; their microscopic physical realization remains an open question.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23277v1
- Title: Radial Coarse Graining Restores Vacuum Majorization in Wigner Phase Space
- Authors: Ao-Xiang Liu, Cong-Feng Qiao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23277v1  pdf=https://arxiv.org/pdf/2609.23277v1.pdf

Abstract:
Quantum uncertainty limits how strongly Wigner functions can concentrate in phase space. It is commonly conjectured that the vacuum Wigner function continuously majorizes that of any Wigner-positive state. However, by constructing Wigner-positive states whose localized quantum coherence lowers their Wigner entropy below the vacuum value, we show that this conjecture is incorrect. We restore vacuum majorization at finite resolution by integrating single-mode Wigner functions over concentric radial energy shells, obtaining probability vectors majorized by that of the vacuum for all Wigner-positive states and for Wigner-negative states with non-negative shell weights. Anchoring these shells to a fixed oscillator frame breaks affine symplectic invariance, rendering this relation strict for every non-vacuum Gaussian pure state. For Wigner-negative states, the persistence of negative shell weights defines a radial negativity scale with Airy-edge semiclassical asymptotics for highly excited Fock states. Operationally, we combine the majorization relation with partial transposition to obtain a two-mode entanglement criterion directly evaluable from radially binned joint homodyne outcomes without state reconstruction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23298v1
- Title: Static classical-quantum-entanglement trade-offs: an entropic converse and single-letter characterizations
- Authors: Mark M. Wilde
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2609.23298v1  pdf=https://arxiv.org/pdf/2609.23298v1.pdf

Abstract:
The direct static capacity region of a bipartite quantum state describes its asymptotic conversion into classical communication, quantum communication, and entanglement, with all communication directed from Alice to Bob. This paper gives a unified entropic converse for this region. The proof treats generated and consumed resources simultaneously and derives all three information inequalities for one local instrument. Its main ingredients are no-signalling, the chain rule, strong subadditivity, and continuity of conditional entropy. A supporting-hyperplane characterization leads to the static capacity formula, which is helpful in determining single-letterization of the capacity region. For a pure state of entanglement entropy $h$ subjected to erasure with probability $p$, the complete region is the convex hull of $0$ and $(0,-ph,(1-p)h)$, plus the unit-resource cone. This statement holds for arbitrary collective instruments by using subset-entropy inequalities related to earlier methods used for the dynamic capacity region of the erasure channel. Complete characterizations also hold for symmetrically extendible states and locally flagged pure-state mixtures. For maximally correlated states, the optimization over local instruments admits an exact matrix formulation and an additive outer bound. An explicit qubit example shows that a nonorthogonal discarded quantum memory can outperform every efficient instrument and every instrument with conditionally commuting discarded states. For states obtained by qubit dephasing of Schmidt-aligned pure states, an exact threshold characterizes when the static capacity formula vanishes, at every blocklength and after regularization. Full single-letter characterizations for general Hadamard states and for the remaining trade-offs for dephased states remain open, with sufficient additivity conditions identified.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23316v1
- Title: Simultaneous Reduction of Observables and Measured Qudits in Entanglement-Assisted Quantum Local Recovery
- Authors: Ryutaroh Matsumoto
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2609.23316v1  pdf=https://arxiv.org/pdf/2609.23316v1.pdf

Abstract:
For a general entanglement-assisted or unassisted quantum error-correcting code, a set of erasures, and an associated repair group, we propose a linear algebraic procedure to compute a reduced set of observables and a reduced repair group of codeword qudits for correcting the given erasures. The procedure has cubic complexity in the repair group size and the computed set of observables has the smallest possible size for correcting the given erasures. We specialize the general procedure to quantum codes constructed from Euclidean and Hermitian orthogonality, and provide closed-form upper bounds on the size of reduced repair groups for those special cases. Based on these closed-form bounds, we propose quantum counterparts of the information locality of classical local recovery.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23334v1
- Title: Stochastic Reconfiguration as Statistical Filtering for Overparameterized Neural Quantum States
- Authors: Tak Hur
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2609.23334v1  pdf=https://arxiv.org/pdf/2609.23334v1.pdf

Abstract:
Stochastic reconfiguration (SR) is the standard optimizer for neural quantum states (NQS), but modern NQS often have far more parameters than Monte Carlo samples. We show that in this regime the diagonal shift is more than a numerical stabilizer. It acts as a statistical filter for finite-sample generalization. At a fixed wave function, SR is ridge regression from tangent features to the centered local energy. Its residual is the expressivity gap, the part of imaginary-time evolution outside the current tangent space. This gap is orthogonal to the tangent space in population, but finite batches make it act as noise that SR can overfit. The shift therefore balances shrinkage of useful update directions against variance from fitting sampled residuals. Exact diagnostics on a $4\times4$ Heisenberg graph separate two effects of overparameterization. Larger tangent spaces help when they reduce the expressivity gap, but they can hurt when they overfit a fixed gap. In a $100$-site transverse-field Ising family trained with a foundation NQS, validation risk is U-shaped in the shift while variance decreases, matching the noisy-ridge model. This view leads to multi-shift SR (MS-SR), which averages independent ridge solves at data-adaptive shifts to form a richer, lower-variance spectral filter. Checkpoint-local experiments show that MS-SR lowers validation risk and update variance relative to the fixed-shift SR baseline. We further compare MS-SR and SR in paired online training continuations, with independent endpoint energy evaluations and a separate update-cost benchmark.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23348v1
- Title: Field-Modified Quantum Potentials from Tridiagonal Representations: Analytical Spectra and Galerkin Simulations
- Authors: Tunde Joseph Osunmusanmi, Berihu Teklu
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2609.23348v1  pdf=https://arxiv.org/pdf/2609.23348v1.pdf

Abstract:
We develop an effective radial framework for analyzing new field-modified potential function of a charged spinless particle in collinear electric and magnetic fields. Using the weak- magnetic field approximation, we neglect the diamagnetic term and other angular projections under an explicit smallness condition $\ll ΔE$, where $E$ is the electric field, and the replacement of the angular factor by $C=\cosθ$ in the spherical coordinates. The resulting equation is therefore a field-aligned radial model whose validity is limited to angularly localized states. Within this setting, we apply the indirect mode (or search mode) of Tridiagonal representation approach in the Laguerre and Jacobi bases. In the Laguerre basis, the tridiagonal constraint generates linear-plus-inverse and linear-plus-quadratic radial potentials, and the coefficient recurrences are connected with Meixner--Pollaczek and Meixner polynomial type structures, therefore yielding the analytic spectra and expansion wavefunctions. In the Jacobi basis, the mapping of the radial half-line to a finite interval produces a singular confining effective potential and a three-term recurrence that is treated through a truncated generalized eigenvalue problem. The formulation provides analytically and numerically tractable benchmark models for field-modified potential functions, while keeping the assumptions, parameter restrictions, endpoint behavior, and convergence tests explicit. All energy spectra formulae obtained under the present models are new and are coupled with magnetic fields analytically and numerically when using the Laguerre bases and the Jacobi bases respectively.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23353v1
- Title: Eigenvalue-by-Eigenvalue Comparison of a Sierra--Rodríguez-Laguna-Type Spectrum with the Riemann Zeros
- Authors: Mi-Ra Hwang, Eylee Jung, MuSeong Kim, DaeKil Park
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23353v1  pdf=https://arxiv.org/pdf/2609.23353v1.pdf

Abstract:
We study the self-adjoint extension of the Sierra--Rodríguez-Laguna (SR) $H=xp$-type Hamiltonian $\widehat H_{SR}$. Its discrete spectrum is fixed by the equation $\mathrm{Re}\!\left[e^{-iθ/2}K_{1/2+iE/2}(2π)\right]=0$. We solve this equation numerically for $θ=1.417π$ and obtain the first 606 eigenvalues $E_n$. We compare them, one by one, with the ordinates $γ_n$ of the first 606 nontrivial zeros of the Riemann zeta function. Using the steepest-descent (saddle-point) method for the modified Bessel function, together with the Riemann--von Mangoldt formula, we derive a closed-form prediction for $E_n-γ_n$ in terms of the Lambert-$W$ function. We show that our leading-order phase for $K_{1/2+iE/2}(2π)$ matches exactly a known, rigorous asymptotic formula for modified Bessel functions of large imaginary order. This rules out the Bessel function as the source of a numerical mismatch we found earlier. We then trace that mismatch to how the counting function $N(T)$ must be treated exactly at $T=γ_n$: the usual midpoint convention for the fluctuating term $S(T)$ shifts the effective quantum number by $1/2$. With this fix, $γ_n\sim g(n-11/8)$ instead of $g(n-7/8)$, and the new prediction for $E_n-γ_n$ matches, to within $0.03\%$, the value we measure directly from the first $10^5$ tabulated zeta zeros (A.~Odlyzko).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23382v1
- Title: Unified Spectral, Dynamical, and Correlation Signatures of an Exceptional Point in Cavity Optomechanics
- Authors: Khazali Fahmi, Ahmad R. T. Nugraha, Ferry A. A. Nugraha, Adam B. Cahaya
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23382v1  pdf=https://arxiv.org/pdf/2609.23382v1.pdf

Abstract:
We investigate how the exceptional-point structure of a dissipative cavity optomechanical system is inherited by experimentally accessible dynamical, spectral, and quantum-statistical observables. At optical-mechanical resonance, the effective non-Hermitian first-moment dynamics exhibits a second-order exceptional point, where two eigenvalues and their eigenvectors coalesce and the eigenvalue splitting follows the characteristic square-root dependence on perturbations. We show that the same square-root feature also governs transient photon and phonon populations, first-order coherence, spectral poles, and second-order intensity correlations. Below the exceptional point, the dynamics is non-oscillatory, whereas above it damped oscillations emerge together with frequency splitting of the spectral poles. At the exceptional point, the Jordan-block structure produces polynomial-exponential relaxation and a second-order spectral pole. Using the quantum regression theorem and Gaussian moment factorization, we further show that the stationary fluctuations satisfy the Siegert relation linking first- and second-order correlations. Although the zero-delay autocorrelations retain their thermal value, the finite-delay intensity correlations exhibit clear exceptional point signatures. This finding connects non-Hermitian mode coalescence with measurable dynamical and correlation observables in cavity optomechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23406v1
- Title: Quantum scattering by intersecting δ-potential barriers: from Gaudin's kaleidoscope to quantum Galperin billiards
- Authors: Yi-Cong Yu, Wen-Jie Qiu, Xiaoming Cai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23406v1  pdf=https://arxiv.org/pdf/2609.23406v1.pdf

Abstract:
We develop a general framework for the scattering of a plane wave by a class of Gaudin kaleidoscope models: straight $δ$-potential barriers intersecting at a common point. The projected Lippmann-Schwinger equations split into a singular part, a finite pole closure generated by a geometric moving rule, and a regular remainder, the outgoing state being an atomic measure on the circle. At the special angles $π/N$, where the intersecting barriers generate the dihedral group $D_N$, the number of channels stays fixed, whereas at generic angles channels are created and destroyed, opening smoothly from zero weight as a critical direction is crossed. This leaves no singular trace in the probabilities, being carried instead by the phase shifts, a quantum-classical correspondence beyond the reach of the coordinate Bethe ansatz. The same equations solve the quantum Galperin billiards exactly, the method of images reducing them to a single linear system whose phase shifts follow in closed form.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23420v1
- Title: Feedback-Induced Dynamical Phases in a Self-Adaptive Quantum Kicked Rotor
- Authors: Pan Gao, Zheng-Wei Zhou, Guang-Can Guo, Xi-Wang Luo
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.stat-mech; physics.optics
- Links: abs=https://arxiv.org/abs/2609.23420v1  pdf=https://arxiv.org/pdf/2609.23420v1.pdf

Abstract:
We introduce a self-adaptive Floquet system based on a quantum kicked rotor, in which the kicking strength itself becomes a dynamical variable generated self-consistently through cavity-mediated feedback. A superradiant transition gives rise to cavity-mediated kicking and two competing instability channels, symmetric and antisymmetric, which provide a unified organizing principle for the nonequilibrium Floquet phases. For resonant kicking, their competition produces double-kick dynamics that support resonant ballistic transport and an emergent antiresonance with period-quadrupled rotor evolution, arising from a balance between the two instability channels. Remarkably, for incommensurate kicking, the antisymmetric instability stabilizes a robust period-doubled localized phase with persistent subharmonic dynamics despite the underlying incommensurate driving, revealing localized temporal order absent in conventional kicked rotors. As the feedback strength increases, correlated temporal fluctuations progressively suppress quantum interference, driving crossovers from period-doubled localization to irregular localization and eventually to subdiffusive transport. Our results establish a general framework for self-adaptive quantum-chaotic dynamics and demonstrate how dynamical feedback can fundamentally reshape transport, localization, and temporal order in driven quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23429v1
- Title: Liouvillian Response for Temporal Information in Quantum Reservoir Computing
- Authors: Jiande Cao, Rui-Yang Gong, Zhongjin Lin, Yexiong Zeng, Ze-Liang Xiang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23429v1  pdf=https://arxiv.org/pdf/2609.23429v1.pdf

Abstract:
Open quantum systems offer a physical substrate for temporal information processing in quantum reservoir computing, yet the microscopic mechanisms linking their dynamics to computational performance remain unclear. Here we establish a microscopic response-to-performance framework that connects Liouvillian dynamics directly to task performance. We decompose observable Volterra weights as $W^{(q)}=BH^{(q)}$, separating internal input-history pathways from their readout visibility, and show that a dynamical response contributes to a task only if it is input-generated, readout-visible, target-correlated, and resolvable above the regularization scale. This framework reveals how Liouvillian modes govern the retention and propagation of task-relevant information, while symmetries determine which components remain visible to the readout. It further establishes how distinct covariance modes encode different temporal information structures and how system parameters and processing protocols can reshape their contributions to improve QRC performance. Thermalization drives the reservoir from processing that retains input history to a response dominated by the most recent input before regularization suppresses the residual information. We finally show that weak measurement can activate task-relevant covariance modes by lifting symmetry-imposed channel equivalence, whereas delayed feedback creates controlled return pathways for historical information. These results establish a microscopic connection between open-system dynamics and computational performance, providing principles for engineering task-relevant information flow in quantum reservoirs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23441v1
- Title: Entanglement Cost of Optimal Distributed Quantum State Purification
- Authors: Jiayi Zhao, Chengkai Zhu, Xin Wang, Ge Bai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23441v1  pdf=https://arxiv.org/pdf/2609.23441v1.pdf

Abstract:
We determine the preshared entanglement required for spatially separated parties, restricted to local operations and classical communication, to attain globally optimal probabilistic two-copy purification of arbitrary bipartite pure states under depolarizing noise. In every local dimension $d\ge 2$, one shared maximally entangled qubit pair suffices: local controlled-SWAP operations exactly reproduce the globally optimal successful transformation. Conversely, any finite-dimensional preshared resource state that attains the same benchmark, even under a positive-partial-transpose relaxation, must have entanglement of formation at least one ebit. For pure resources with one ebit, or for two-qubit resources including mixed states, attaining the benchmark is possible only for states with exactly two nonzero Schmidt weights, both equal to $1/2$, namely those locally unitarily equivalent to a maximally entangled qubit pair. These findings provide a benchmark for evaluating the entanglement demands of noise management in quantum networks and modular quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23455v1
- Title: Zero-Knowledge Proofs of Quantumness
- Authors: Duong Hieu Phan, Weiqiang Wen, Xingyu Yan, Jinwei Zheng
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23455v1  pdf=https://arxiv.org/pdf/2609.23455v1.pdf

Abstract:
With the rapid development of quantum computers, proofs of quantumness have recently become an interesting research direction. However, in current schemes for proofs of quantumness, quantum provers face the risk of being maliciously exploited by classical verifiers. Through malicious strategies in interaction with quantum provers, classical verifiers could solve some instances of hard problems that arise from the specific scheme in use. This is due to the lack of formalization that prevents malicious verifiers from extracting useful information in proofs of quantumness. To address this issue, we formalize zero-knowledge proofs of quantumness. Intuitively, the zero-knowledge property necessitates that the information gained by the classical verifier from interactions with the quantum prover should not surpass what can be simulated using a simulated classical prover interacting with the same verifier. As a result, the new zero-knowledge notion can prevent a malicious verifier from exploiting quantum advantage. We find that the classical zero-knowledge proof is sufficient to compile some existing proofs of quantumness schemes into zero-knowledge proofs of quantumness schemes. It appears to be more general to require zero-knowledge proof on the verifier side instead of the prover side. This helps to regulate the verifier's behavior from malicious to be honest-but-curious. As a result, both parties will play not only one role in the proofs of quantumness but also the dual role in the classical zero-knowledge proof. Specifically, Shor's factoring-based scheme and the learning with errors-based scheme in [Brakerski et al., FOCS, 2018] can be transformed into zero-knowledge proofs of quantumness by requiring an extractable non-interactive zero-knowledge argument on the verifier side. Zero-knowledge proofs of quantumness can thus be viewed as an enhanced security notion for proofs of quantumness.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23459v1
- Title: Quantum Teleportation Over a Noisy Relay Channel
- Authors: Yigal Ilin, Uzi Pereg
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2609.23459v1  pdf=https://arxiv.org/pdf/2609.23459v1.pdf

Abstract:
Quantum teleportation and Bell measurements are considered in a noisy relay setting. We introduce two quantum relay-channel models with closed-form capacity formulas, motivated by the canonical quantum communication protocols of teleportation and superdense coding. In both models, the sender transmits a qubit, while the relay observes side information about the Pauli errors that occur in the channel and communicates with the receiver through an orthogonal rate-limited link. We develop a compress-forward coding scheme in which the relay compresses the Pauli-error sequence into bins and sends the bin index to the receiver. The receiver uses this partial error information to reduce the effective channel noise before quantum decoding. We show that this strategy is optimal by establishing matching converse bounds for both models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23476v1
- Title: Comparative Study of Quantum and Classical Machine Learning Models in Binary Classification
- Authors: Anand Kumar Mishra, Ramanuj Awasthi
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2609.23476v1  pdf=https://arxiv.org/pdf/2609.23476v1.pdf

Abstract:
A potential path forward is Quantum Machine Learning (QML), which aims to leverage quantum computing in conjunction with classical machine learning to enhance computing efficiency and the expressiveness of models. In this paper, two different quantum classifiers - Variational Quantum Classifier (VQC) and Quantum Kernel Support Vector Machine (QSVM) - are compared with three classical classifiers as baseline classifiers - Logistic Regression, Support Vector Machine (SVM), and a Multi-Layer Perceptron (MLP) - on the Breast Cancer Wisconsin dataset. The quantum circuits were created in the PennyLane framework and simulated on a classical backend. However, in terms of accuracy, classical Logistic Regression performed better with an accuracy of 97.8%, classical SVM and QSVM with an accuracy of 95.6% each, although the Quantum VQC achieved a lower accuracy of 88.9% and had a recall of 100% for the benign class, though it correctly identified only 12 of the 17 malignant cases (a malignant-class recall of approximately 70.6%). The drawback of quantum models is the higher training time; however, since the quantum circuit needs to be classically simulated, the quantum SVM took 23.29 seconds compared to less than 0.01 seconds for the classical linear models. These results indicate that for small structured datasets, classifiers based on quantum computing have not yet surpassed well-tuned classical counterparts. In some respects (e.g., benign-class recall), they perform competitively, though not on malignant-class recall, where the VQC in particular performed worse than the classical baselines, which is worth further investigation on real quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23591v1
- Title: Strong Symmetry from Two-Point Correlations
- Authors: Han Yan
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el; hep-th
- Links: abs=https://arxiv.org/abs/2609.23591v1  pdf=https://arxiv.org/pdf/2609.23591v1.pdf

Abstract:
Strong and weak symmetries and their spontaneous breaking distinguish different forms of symmetry and order in mixed states. We show that complete one- and two-point correlation functions, equivalently all two-site reduced density matrices, determine exact strong symmetry for continuous onsite unitary actions of connected groups: states with identical correlations have the same strong symmetry and character. We also present an algorithm to determine the maximal connected strong-symmetry sub-Lie group and its character from two-point correlations. Because such correlations are more accessible than full-state tomography, the algorithm is readily applicable to experiments ranging from condensed-matter systems to quantum simulators and circuits. We also identify group and representation-specific cases in which fewer correlations suffice.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23609v1
- Title: Casimir force in a water nanolayer confined by graphene sheets
- Authors: Wijnand Broer, Jure Dobnikar
- Categories: quant-ph (primary); quant-ph; cond-mat.soft
- Links: abs=https://arxiv.org/abs/2609.23609v1  pdf=https://arxiv.org/pdf/2609.23609v1.pdf

Abstract:
Casimir forces, arising from quantum and thermal fluctuations, depend strongly on the electromagnetic susceptibilities of the interacting materials. Here, we theoretically investigate the Casimir force between two graphene sheets separated by a nanometer-thin layer of liquid water. We find that, at thicknesses up to 3.4 nm, the confinement reduces the Casimir force by up to 26 % compared to the bulk case. At larger thicknesses, the bulk model underestimates the Casimir force by up to 42 % due to the interface effect. This effect does not decrease monotonically as a function of the layer thickness: it increases up to a maximum at 70 nm and it slowly declines to the bulk limit only at 2 microns. We separately assess the effect of nanoscale confinement on the electronic response of graphene, which has no effect on the Casimir force.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23633v1
- Title: Spectral width and polynomial degree in perfect state transfer
- Authors: Xingkun Song
- Categories: quant-ph (primary); quant-ph; math.CO
- Links: abs=https://arxiv.org/abs/2609.23633v1  pdf=https://arxiv.org/pdf/2609.23633v1.pdf

Abstract:
We study the minimum time for perfect state transfer under polynomial Hamiltonians with bounded degree and spectral width. For a strongly cospectral pair and width bound $W$, the optimum, when finite, is an integer multiple of $π/W$, determined by integer interpolation with prescribed parities. For equally spaced supported eigenvalues with alternating signs, we give degree bounds under which every minimizer is affine, and sharp asymptotics for each fixed exact degree. Near-minimizing phase polynomials satisfy a quantitative Chebyshev stability estimate. We determine the optimal transfer time for every degree bound on hypercubes of odd prime dimension. For complementary vertices of $J(2m,m)$, the optimal time at fixed spectral width grows exponentially in $m$ throughout an interval of feasible degrees. We also construct polynomial Hamiltonians showing that every feasible degree $m-t$ with $t=o(m)$ admits subexponential transfer time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23648v1
- Title: Dynamics of nonclassicality in a generalized Tavis Cummings model with XY spin $(1/2,1)$ atomic interactions
- Authors: Bouchra El Alaoui, Abdallah Slaoui, Rachid Ahl Laamara
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23648v1  pdf=https://arxiv.org/pdf/2609.23648v1.pdf

Abstract:
We investigate the dynamics of nonclassicality, quantified by the Wigner Yanase skew information, in generalized Jaynes Cummings (JC) and Tavis Cummings (TC) models describing light matter interactions in cavity quantum electrodynamics. We first analyze a generalized JC model consisting of a single bosonic cavity mode coupled to a spin 1 atom, focusing on the temporal evolution of nonclassicality in both the cavity field and the atomic subsystem. We then extend this framework to a generalized TC model by introducing an additional spin $1/2$ atom, enabling us to examine the influence of collective atomic degrees of freedom. The global dynamics are investigated both with and without an $XY$ spin interaction. Our results show that, under resonance conditions, the system exhibits efficient excitation exchange between the cavity field and the atomic subsystem, resulting in regular, coherent nonclassicality dynamics and enhanced field nonclassicality generation. Conversely, an increasing longitudinal magnetic field acts primarily as an effective detuning parameter rather than a direct exchange interaction. In this off resonant regime, the atom field coupling is substantially weakened, localizing excitations within the atomic subsystem. This localization suppresses coherent energy transfer to the cavity field, leading to a pronounced reduction in field nonclassicality, while the atomic subsystem retains the majority of the quantum correlations. Notably, atomic superposition states exhibit highly irregular spin dynamics, reflecting a detuning-induced redistribution of quantum correlations. These findings demonstrate that the dynamics of spin and field nonclassicality are governed primarily by interaction mediated excitation flow and resonance conditions rather than the initial energy distribution alone, ..

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23651v1
- Title: Nonequilibrium energy transport and fluctuations in two-photon-driven nonlinear quantum optical systems
- Authors: Y. T. Chen, Y. W. Lu, J. C. Lu, C. Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23651v1  pdf=https://arxiv.org/pdf/2609.23651v1.pdf

Abstract:
Understanding nonequilibrium transport and fluctuations driven by nonclassical light in nonlinear quantum optical systems is challenging. Here, we formulate a driven quantum master equation in the rotating frame combined with full counting statistics, retaining the drive-induced frequency shifts in the system-reservoir interactions and providing a unified description of drive-assisted incoherent transitions based on the rotated system dressed-basis. Applied to a Kerr resonator and a nonlinear Jaynes-Cummings model, the approach reveals pronounced multiphoton-resonant enhancement of the drive input energy current, with significant high peaks under two-photon driving compared to the single-photon case. The two-photon resonance relations are analytically obtained. Resonance structure in the nonlinear Jaynes-Cummings model nonlinearly relies on qubit-photon couplings, with additional dressed-state branches. A low-energy-state approximation attributes the resonant current enhancement to dressed-state hybridization and efficient activation of incoherent energy exchange processes. Beyond the average current, two-photon-driving induced energy exchange picture near resonance also substantially modifies the second-order current fluctuation and higher-order current cumulant, while increasing the time-normalized signal-to-noise ratio. Adding two-photon loss introduces extra incoherent photon-pair exchange pathways and further reshapes the current and its fluctuations. We hope these results may deepen interpretation of photon driving and quantum dissipation cooperatively governing nonequilibrium energy transport and fluctuations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23657v1
- Title: QAOA-Based Pilot Assignment for Cell-Free Massive MIMO Systems
- Authors: Xiaoyu Ma, Fang Fang, Xianbin Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23657v1  pdf=https://arxiv.org/pdf/2609.23657v1.pdf

Abstract:
Pilot contamination is a major challenge in cell-free massive multiple-input multiple-output (MIMO) systems, where the limited number of orthogonal pilots makes pilot reuse unavoidable. Since the pilot assignment solution space grows exponentially with the number of users, finding the global optimum becomes computationally challenging on classical computers. Recent advances in quantum computing provide a promising approach for solving such large-scale combinatorial optimization problems. In this paper, we reformulate the assignment problem as a quantum-compatible optimization problem, enabling it to be directly solved by the Quantum Approximate Optimization Algorithm (QAOA). Specifically, the pilot contamination objective and assignment constraints are incorporated into the QAOA formulation. This allows the quantum search to focus on valid pilot assignments with low contamination cost. Simulation results show that the proposed method achieves performance close to exhaustive search, demonstrating the potential of quantum-assisted optimization for pilot assignment in future wireless systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23664v1
- Title: QuWARP: A Workload-Aware Reuse Planner for simulating Quantum Circuits
- Authors: Tim Littau, Rihan Hai
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23664v1  pdf=https://arxiv.org/pdf/2609.23664v1.pdf

Abstract:
Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that could be reused safely. We propose QuWARP, a planner-based workload optimiser for a bounded state of the art simulator execution surface: it performs workload-level planning over related tasks, identifies shared prefixes, and chooses when to materialize exact typed boundary artifacts for later reuse across the evaluated statevector mode, and stabilizer-hybrid mode. Its planner treats continuation legality as a narrow correctness guardrail, abstains when reuse is unprofitable, and keeps each reuse, abstention, or refusal decision auditable through EXPLAIN-style traces, meaning inspectable planner reports with provenance and realized-cost summaries. Across real world quantum application workloads QuWARP delivers 2.95x-32.84x speedups over this work's main direct per-task Qrack denominator on reuse-positive workloads. These results show workload-level reuse planning improves repeated-run simulation while keeping unsupported handoffs auditable and out of the execution path.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23721v1
- Title: Non-Hermitian quantum phase transitions in the XY model induced by staggered imaginary Dzyaloshinskii--Moriya interaction
- Authors: Hong Jiang, Xiang-Ping Jiang, Yan-Chao Li
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2609.23721v1  pdf=https://arxiv.org/pdf/2609.23721v1.pdf

Abstract:
We investigate non-Hermitian quantum phase transitions driven by staggered imaginary Dzyaloshinskii--Moriya (DM) interactions in a transverse-field $XY$ chain. By virtue of a staggered nonunitary transformation, we exactly diagonalize the Hamiltonian. For $D<1$, this procedure maps the non-Hermitian model onto a standard Hermitian $XY$ chain, allowing analytical derivation of the full phase boundaries. The parameter line $D=1$ forms an exceptional boundary with coalesced quasiparticle eigenvalues and eigenvectors, while the entire $D>1$ regime falls into the $\mathcal{RT}$-symmetry-broken phase containing two distinct $z$-ferromagnetic phases. We examine common quantum-information probes and show that conventional measures, such as entanglement entropy, quantum discord, and quantum coherence, fail to capture the $\mathcal{RT}$ symmetry-breaking transition. To address this deficiency, we propose a novel coherence measure $\widetilde{\mathrm{QC}}_{\max}^{\rm LR}$ based on $\mathcal{RT}$ symmetry and complex-conjugate eigenpair correlations. Embedding intrinsic non-Hermitian information of left and right eigenstates, $\widetilde{\mathrm{QC}}_{\max}^{\rm LR}$ reliably identifies the $\mathcal{RT}$ symmetry-breaking transition and accurately resolves all magnetic phase boundaries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23752v1
- Title: Near-optimal incoherent tomography of low-rank quantum channels
- Authors: Kean Chen, Aadil Oufkir
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23752v1  pdf=https://arxiv.org/pdf/2609.23752v1.pdf

Abstract:
We study tomography for quantum channels with input dimension $d_1$, output dimension $d_2$, and Kraus rank at most $r$, to within diamond norm error $\varepsilon$, using adaptive experiments that retain no quantum memory between channel queries.   - For quantum channels whose non-zero Choi eigenvalues are bounded below by $Ω(d_1/r)$, we establish optimal query upper and lower bounds $Θ(d_1d_2r^2/ε^2)$. The upper bound is achieved by a nonadaptive algorithm that uses the estimator from [Surawy-Stepney et al., Quantum (2022)], together with a new diamond-norm analysis. The lower bound applies to arbitrary adaptive incoherent protocols and follows from a new local family of channels and a uniform one-query Fisher-information bound.   - For general channels, we establish an upper bound $O(d_1d_2r^2\log(2d_1)/ε^2)$, nearly matching the above lower bound $Ω(d_1d_2r^2/\varepsilon^2)$. To achieve this, we generalize the above nonadaptive algorithm by adapting the input state over $O(\log(2d_1))$ rounds with the Matrix Multiplicative Weight Update algorithm.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23756v1
- Title: Flow-Based Lattice Surgery Optimization with Runtime T Gate Scheduling
- Authors: Raymond Iacobacci, Tianyi Hao, Neer Patel, Siyuan Niu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23756v1  pdf=https://arxiv.org/pdf/2609.23756v1.pdf

Abstract:
Lattice surgery on the surface code is a leading route to fault-tolerant quantum computation. Compiling logical circuits into lattice surgery operations is a pivotal step that determines the resource cost of a computation. Prior compilers build on idealized assumptions, and one that works in practical settings remains to be developed. Existing works are either unscalable or route one gate at a time within a layer, so the embedding depends on the order of gates and opportunities to route many gates at once are lost. In addition, they assume magic states are always available and cost-free, even though preparing one costs more than a Clifford operation.   We present FlowRouter, the first topological lattice surgery compiler that places Clifford routing and stochastic magic state cultivation inside a single 3D embedding. At compile time, FlowRouter formulates the routing of an entire circuit layer as a maximum-flow problem, embedding many gates simultaneously. At runtime, it allows magic states to be cultivated at every idling patch, works with the realistic cultivation process with multiplexing and multi-stage post-selections, and absorbs the stochasticity by introducing delay mechanisms that add as little spacetime volume as possible. With magic states assumed free, FlowRouter reduces spacetime volume by 2.3x and compiles 10.8x faster than the state-of-the-art static topological lattice surgery compiler. With the cultivation-aware setting that includes both Clifford and magic state cost, FlowRouter reduces spacetime volume by 2.3x on a distance-13 surface code when compared with the state-of-the-art runtime compiler.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23818v1
- Title: A four-state quantum communication protocol with mesoscopic twin beams
- Authors: Stefano Carsi
- Categories: quant-ph (primary); quant-ph; physics.ins-det
- Links: abs=https://arxiv.org/abs/2609.23818v1  pdf=https://arxiv.org/pdf/2609.23818v1.pdf

Abstract:
Twin-beam (TWB) states generated by parametric down-conversion exhibit strong photon-number correlations that can be exploited for quantum communication. In the mesoscopic regime, these correlations can be directly investigated using photon-number-resolving detectors, such as silicon photomultipliers (SiPMs). Their nonclassical nature is quantified by the noise reduction factor (NRF), which provides a witness of quantum correlations and a means of monitoring channel security. In this work, a quantum communication protocol based on TWB states, originally proposed for binary encoding, is extended to a four-state scheme capable of transmitting two bits per use. Information is encoded by combining two mean photon-number values and two mode numbers of thermal noise superimposed on one arm of the twin beam, defining four distinguishable states in the (m,R) plane. While the mean detected photon number enables the retrieval of one bit, the NRF provides discrimination of the second bit and a security check against intercept-and-resend attacks, which introduce additional noise and degrade the quantum correlations. The protocol is investigated through two experimental measurement campaigns. First, the twin-beam source is characterized in terms of photon-number statistics, NRF, and detection efficiency to establish the operating conditions of the communication channel. Subsequently, the four-state protocol is implemented and evaluated through the analysis of state distributions and their 95% confidence regions, error probability as a function of sample size, and a comparative assessment of machine learning classifiers for state discrimination. Finally, the response of the NRF to an intercept-and-resend attack is investigated to assess the protocol's ability to detect eavesdropping.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23870v1
- Title: Hidden collision statistics in bosonic heat transport: Superthermal correlations at fixed mean current
- Authors: Iu. A. Nosal, A. E. Teretenkov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23870v1  pdf=https://arxiv.org/pdf/2609.23870v1.pdf

Abstract:
Reservoirs with the same mean relaxation rate can be indistinguishable at the level of average energy transport while producing different fluctuations. We study a bosonic mode coupled to hot and cold Poisson streams of thermal ancillas through finite beam-splitter collisions. The averaged evolution is a compound-Poisson semigroup generated by finite Gaussian event channels. Its nonequilibrium steady state is an exact mixture of thermal states governed by a random affine fixed point. Consequently, the mean-occupation dynamics and bath-resolved mean heat currents coincide with those of the matched continuous Lindblad reservoir, whereas higher correlations retain the collision strength. For equal collision transmissivities, we derive an exact superthermal bunching law controlled by the temperature contrast and collision strength. We also obtain the asymptotic rates of the first two heat cumulants for an ideal stationary event-resolved two-point-measurement record and separate local one-collision contributions from temporal correlations. Fock-space diagonalization and Monte Carlo trajectories validate the formulas and connect full resets to the weak-collision Gaussian limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23914v1
- Title: Bell-certified retardance polarimetry from CHSH correlators
- Authors: J. Sumaya-Martinez
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.23914v1  pdf=https://arxiv.org/pdf/2609.23914v1.pdf

Abstract:
Bell-CHSH measurements with polarization-entangled photons are commonly used as nonlocality witnesses. Here we show that the same coincidence data can also provide a quantitative metrological certificate for optical retardance sensing. For a local birefringent phase encoded on one photon, we derive the classical Fisher information directly from experimentally accessible CHSH correlators and obtain a lower bound expressed in terms of the measured correlations and the phase derivative of the CHSH parameter. In the unbiased-marginal two-qubit regime, the canonical CHSH analyzer settings are shown to be simultaneously Bell-optimal and Fisher-optimal, saturating the quantum Fisher information for retardance estimation in the ideal case. We further analyze reduced visibility, phase noise, analyzer misalignment, and finite coincidence counts, and construct conservative lower confidence bounds that can be evaluated without quantum-state tomography. The results also clarify that Bell violation and metrological usefulness are distinct resources: nonzero Fisher information can persist below the CHSH-violation threshold. The protocol therefore enables a standard Bell-test data set to provide both a nonlocality benchmark and a statistically controlled sensitivity certificate for quantum polarimetry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23942v1
- Title: Lee-Yang theorem for fermions
- Authors: Chaithanya Rayudu, Takahiro Misawa, Andrew Zhao, Jun Takahashi
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; cond-mat.str-el; cs.CC; math-ph
- Links: abs=https://arxiv.org/abs/2609.23942v1  pdf=https://arxiv.org/pdf/2609.23942v1.pdf

Abstract:
Lee-Yang theorems are a powerful tool for studying many-body systems, with applications ranging from analyzing phase transitions to proving the efficiency of certain classical and quantum algorithms. In this work, we prove a Lee-Yang zero-freeness theorem for the partition function of a broad class of interacting fermion models, implying the existence of a provably efficient quantum algorithm for estimating their ground-state energies. This class includes several well-known models such as the attractive Hubbard model, repulsive Hubbard model on bipartite graphs, and the interacting Hofstadter model. Our results also rigorously establish the nonexistence of phase transitions in these models in the presence of a nonzero local external field.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23946v1
- Title: A constructive violation of additivity of minimum output von Neumann entropy
- Authors: Laura Shou, Alexey V. Gorshkov
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2609.23946v1  pdf=https://arxiv.org/pdf/2609.23946v1.pdf

Abstract:
We give an explicit non-random example of nonadditivity of minimum output von Neumann entropy. The proof uses a finite-dimensional construction which imitates free Haar unitary behavior. The same channel also gives a violation of additivity for the minimum output Rényi-$p$ entropy for any $1\le p\le\infty$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23960v1
- Title: Global zero-excitation state preparation through subsystem cooling
- Authors: Kerstin Beer, Daniel Burgarth
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2609.23960v1  pdf=https://arxiv.org/pdf/2609.23960v1.pdf

Abstract:
Preparing interacting quantum systems in low-energy or ground states is a fundamental task in quantum simulation and quantum information processing. In realistic settings, dissipation and active cooling can typically be engineered only on a limited subset of the system. We study the dissipative dynamics of excitation-number conserving quantum systems governed by a GKLS master equation with local jump operators acting on a subset of qubits. We establish sufficient conditions under which such localized dissipation drives the full system to a unique globally attractive zero-excitation state. In particular, we prove that if the Hamiltonian generates excitation transfer described by a graph for which the dissipative subsystem forms a zero forcing set, then the zero-excitation state is the unique globally attractive stationary state. When this state coincides with a ground state of the Hamiltonian, the same mechanism realizes ground-state cooling. Our results provide a graph-theoretic criterion for global state preparation from localized dissipation, which we illustrate using a nearest-neighbor Heisenberg spin chain. For this model, a reduction to the single-excitation sector further yields a scaling estimate with the length of the chain which indicates efficient cooling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24074v1
- Title: Trace-distance-based complementarity relations in a multipath interferometer
- Authors: Yue Sun, Jingyan Liu, Peng-Tong Li, Chenxu Li, Ming-Jing Zhao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24074v1  pdf=https://arxiv.org/pdf/2609.24074v1.pdf

Abstract:
The complementarity relations in an interferometer reflect an important phenomenon in quantum mechanics: wave-particle duality. Here, we develop a method to quantify both wave and particle behaviors in a multi-path interferometer. In particular, we find that the trace distance is a good candidate for wave and particle measures. As a result, some duality relations and triality ralations are established respectively. This work not only extends the application of the trace distance to the interferometer, but also opens up new perspectives on the quantification of waveness and particleness.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24132v1
- Title: Pauli-resolved virtual distillation
- Authors: Si-Yuan Chen, Congcong Zheng, Kun Wang, Ming-Cheng Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24132v1  pdf=https://arxiv.org/pdf/2609.24132v1.pdf

Abstract:
Learning the full Pauli profile of the virtually distilled quantum state $ρ^m/\text{tr}(ρ^m)$ has so far required exponentially many copies of $ρ$. We show that all $4^n$ squared Pauli moments $[\text{tr}(Pρ^m)]^2$ can be learned to additive error $\varepsilon$ with confidence $1-δ$ from one $2m$-replica measurement setting using $O(m[n+\log(1/δ)]/\varepsilon^2)$ copies. This is an exponential speedup in the system size $n$ over previous protocols. For $m = 2$, we propose the coherent Bell difference sampling circuit that realizes this measurement on current devices. The speedup originates from paired replicas that cancel the anticommutation signs of Pauli operators, collapsing the incompatibility of the Pauli family. We certify this collapse by introducing the quantum Bernstein norm, a computable incompatibility measure for nonlinear functionals. A further information-theoretic $m$-replica protocol recovers the signed moments $\text{tr}(Pρ^m)$ using $O(m[n+\log(1/δ)]/\varepsilon^4)$ copies. For fixed $m$ in the stated lower-bound regime, it attains the optimal replica number, since any protocol with fewer replicas requires exponentially many copies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24139v1
- Title: Sparse and weak-measurement certification of graph-edge entanglement in PXP scar wavepackets
- Authors: Ximo Wang, Yichi Zhang, Qiwei Han, Xi Zhao, Yuhang Wang, Chunxiao Du, Rui Li, Wenxiu Li, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24139v1  pdf=https://arxiv.org/pdf/2609.24139v1.pdf

Abstract:
An imperfect many-body revival does not by itself certify the entanglement of the returning state. We give a finite-record protocol for graph-edge localizable entanglement along scar wavepackets of a graph-dressed PXP chain. The target cluster state has nonzero energy variance, so neither an exact target eigenstate nor a dark-state embedding is assumed. Fresh binary probes of the undeformed Hamiltonians Pauli terms have a fully separable explanation, even within the dressed blockade sector. Adding local graph-stabilizer probes makes established entanglement witnesses accessible with simultaneous confidence bounds. For a specified square-root instrument, an imposed worst-case disturbance budget fixes the strength that minimizes the equal-allocation Hoeffding sufficient sampling cost. A local commutator bound accounts for finite-duration ancilla pulses while the Hamiltonian remains active. We test the protocol on chains through twenty spins, under perturbed dynamics, and with independent implementations. At the first twenty-spin return, synthetic weak records certify all nineteen graph edges. Generator, two-color, bounded-weight, and full-group benchmarks separate this localizable resource from genuine multipartite certification. The protocol measures recoverable entanglement in a known scar wavepacket, with explicit calibration and limits on its physical and statistical interpretation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24147v1
- Title: Reconstructing the phonon distribution of trapped ions out of the Lamb-Dicke regime
- Authors: Christophe H. Valahu, Prachi Nagpal, Teerawat Chalermpusitarak, Maverick J. Millican, Cameron McGarry, Frank Scuccimarra, Vassili G. Matsos, Hon-Kwan Chan, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24147v1  pdf=https://arxiv.org/pdf/2609.24147v1.pdf

Abstract:
Characterizing the phonon distribution of trapped-ion motional states is essential for many applications in quantum information processing, but existing methods become ill-conditioned beyond the Lamb-Dicke regime. We overcome this limitation by recasting phonon-state reconstruction as a filter-function inversion problem. Using composite pulses on the carrier and multiple sidebands, we engineer well-conditioned filters in phonon space to characterize pure and mixed states, study heating dynamics, and reconstruct Fock states up to $n=250$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24166v1
- Title: Nondemolition filtering of an embedded cluster-state scar under continuous local monitoring
- Authors: Ximo Wang, Xi Zhao, Xiayu Sun, Qiwei Han, Yuhang Wang, Chunxiao Du, Wenxiu Li, Hao Zhang, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24166v1  pdf=https://arxiv.org/pdf/2609.24166v1.pdf

Abstract:
Identifying a low-entanglement eigenstate inside a many-body spectrum and preserving it during measurement are distinct tasks. We construct an explicit local ring Hamiltonian with an exact cluster-state eigenvector and study continuous monitoring of its stabilizer defects. For arbitrary mixed inputs, the conditional cluster fidelity is the initial target weight divided by the no-observed-click probability. A positive defect-operator gap gives finite-time bounds that hold for noncommuting Hamiltonian dynamics, nonnormal effective generators and imperfect detection. At fixed total monitoring rate, the guaranteed exponent falls inversely with system size; high conditional fidelity does not remove the preparation cost set by the initial overlap. Exact diagonalization up to eleven qubits gives finite-size evidence for a cluster-state outlier in a chaotic spectral background. Independent matrix and trajectory calculations verify the dynamics and a conservative coherent-error bound. This construction specializes established scar embedding and nondemolition verification frameworks, with explicit measurement assumptions, finite-time guarantees and resource limitations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24169v1
- Title: No violation on a generalisation of Leggett-Garg inequality and Bell-CHSH inequality with extended probability
- Authors: Sirawit Kajonsombat, Pongwit Srisangyingcharoen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24169v1  pdf=https://arxiv.org/pdf/2609.24169v1.pdf

Abstract:
A generalisation of the Leggett-Garg inequality (LGI) and the Bell-CHSH inequality is proposed in this work, by replacing a classical probability notion with an extended probability notion. The extended probability serves as an underlying layer of reality to the classical probability. Within the consistent history framework, the underlying layer is so-called a non-settleable history. Hence, the bounds of the LGIs and Bell-CHSH inequalities are extended. The resulting generalised inequalities are satisfied without violation for arbitrary measurement settings. Furthermore, generalised Macro- realism and generalised Local realism are introduced and analysed within the extended probability framework without relying on an explicit measurement. This opens up further possibilities on one of the great pursuits in physics, understanding on how a quantum system can possess classical properties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24266v1
- Title: A QSVT-Based Quantum Jacobi Algorithm for Linear Systems with Application to the Poisson Equation
- Authors: Louisa M. Piskol, Thorsten Grahs, Stefan Langer, Oleksandr Kyriienko
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24266v1  pdf=https://arxiv.org/pdf/2609.24266v1.pdf

Abstract:
Many computational fluid dynamics (CFD) algorithms solve partial differential equations by discretization, resulting in large and sparse systems of linear equations. While iterative methods are widely used to solve these systems classically, most existing quantum linear system solvers target the solution through matrix inversion rather than approximating it using an iterative procedure. In this work, we develop a quantum implementation of the Jacobi method based on quantum singular value transformation (QSVT). By reformulating the Jacobi iteration as a polynomial transformation of a block-encoded operator, the algorithm requires only a constant ancilla overhead with respect to the number of iterations while maintaining a circuit depth that scales linearly with the iteration number. We demonstrate the algorithm for one- and two-dimensional Poisson problems, including the pressure Poisson equation arising in Chorin's projection method for the lid-driven cavity flow. The proposed algorithm provides a promising building block for future quantum implementations of multigrid methods and preconditioning techniques, bringing quantum algorithms closer to established CFD solution strategies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24269v1
- Title: On the Born rule in a new quantum approach
- Authors: Inge S. Helland
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24269v1  pdf=https://arxiv.org/pdf/2609.24269v1.pdf

Abstract:
In the context of a new approach towards quantum foundation, the Born rule is proved under a weak condition through several steps. The sole weak condition behind the Born rule is called the transition probability principle, which is closely related to the likelihood principle of statistics. This condition is discussed from several points of view. The whole approach leads to a simpler state concept than the traditional one in finite-dimensional quantum mechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24282v1
- Title: Quantum Computing Solution of the Bethe-Salpeter Equation for Relativistic Scalar Bound States via Tensor-Network VQE
- Authors: Gerhard Hellstern
- Categories: quant-ph (primary); quant-ph; hep-ph; hep-th
- Links: abs=https://arxiv.org/abs/2609.24282v1  pdf=https://arxiv.org/pdf/2609.24282v1.pdf

Abstract:
We present a gate-based quantum computing solution of the homogeneous Bethe-Salpeter equation (hBSE) for the bound state of two massive relativistic scalar particles interacting via ladder-approximation scalar exchange. After Wick rotation to Euclidean space and O(4) S-wave partial-wave projection, the hBSE is reduced to a symmetric matrix eigenvalue problem of dimension N = 2^n. We decompose the resulting Hamiltonian into a sum of n-qubit Pauli operators and solve it with the Variational Quantum Eigensolver (VQE) using a Matrix Product State (MPS) tensor-network ansatz. For N=16 (n=4 qubits), the VQE recovers the maximum eigenvalue - which encodes the minimum coupling constant for binding - to better than 1 % mean relative error compared to classical diagonalization. Entanglement analysis of the BSE amplitude shows low, area-law-like entanglement over the tested sizes, which motivates the MPS ansatz. A critical analysis of three independent barriers - exponential Pauli overhead, approximately size-independent low entanglement, and decreasing VQE gradient scales for the tested ansatz, consistent with generic barren-plateau concerns at larger n - reveals that the specific problem studied here lies in a classically tractable regime: over the tested range it is well described by low-bond-dimension tensor networks and efficiently handled by MPS/Lanczos methods. This negative result provides, to our knowledge, the first entanglement quantification of the BSE amplitude in qubit encoding, establishes the Pauli Hamiltonian framework for future BSE variants, and identifies 2D Minkowski-space BSE, N-body bound states, and non-ladder kernels as physically motivated extensions where genuine quantum advantage may become plausible.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24291v1
- Title: New lower bounds for CDS and $f$-routing
- Authors: Atsuya Hasegawa, Ranitha Mataraarachchi
- Categories: quant-ph (primary); quant-ph; cs.CR
- Links: abs=https://arxiv.org/abs/2609.24291v1  pdf=https://arxiv.org/pdf/2609.24291v1.pdf

Abstract:
Understanding the entanglement cost of non-local quantum computation (NLQC) is relevant to complexity theory, cryptography, quantum gravity, and related areas. A central special case is $f$-routing, motivated in part by quantum position verification. Proving lower bounds on its entanglement cost in the fully robust setting has been a major open problem in NLQC.   Motivated by this problem, we establish two related lower bounds. First, we study the shared-randomness cost of robust conditional disclosure of secrets (CDS). The connection between CDS and $f$-routing established by Allerstorfer et al. (Quantum 2024) makes understanding the randomness complexity of robust CDS a natural step toward lower bounds for the fully robust routing problem. We show that the shared-randomness cost of robust CDS is lower bounded by the logarithm of deterministic SMP communication complexity, even when communication and private randomness are unrestricted. Our lower bound is tight for the equality function.   Second, we consider one-sided-perfect $f$-routing, in which the protocol is exact on one input class and has constant error on the other. By exploiting the positivity of the low-rank matrix arising in the method of Asadi, Culf, and May (ITCS 2025), we derive a general lower bound on the entanglement cost in terms of sign rank. In particular, this yields a linear lower bound on the entanglement cost of routing for the inner-product function in both one-sided-perfect settings, matching the known upper bound.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24316v1
- Title: A Sharp Noise Threshold for Shor's Quantum Factoring and Discrete Log Algorithms
- Authors: Jin-Yi Cai, Ben Young
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24316v1  pdf=https://arxiv.org/pdf/2609.24316v1.pdf

Abstract:
We study the asymptotic behavior of Shor's quantum factoring and discrete log algorithms when noise affects the precise controlled rotation gates in their quantum Fourier transforms. Improving the results of Cai (2024) and Cai and Young (2025), we identify a sharp and vanishingly small noise threshold. If the noise level lies below this threshold, then the two algorithms succeed in expected polynomial time. If the noise level exceeds this threshold, then the algorithms provably fail to solve their respective problems in expected polynomial time when the underlying primes belong to a set of positive density.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24349v1
- Title: Robust self-testing of nonmaximal entanglement from a reduced inner product game
- Authors: Ranyiliu Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24349v1  pdf=https://arxiv.org/pdf/2609.24349v1.pdf

Abstract:
We reduce Lalonde's pseudo-telepathy inner product game from six to five dimensions, keeping its four Alice questions and three Bob questions and reducing each answer alphabet to five. We prove that the reduced game self-tests its nonmaximally entangled state and all 35 measurement effects. The self-test is also robust: for a strategy winning with probability at least $1-\varepsilon$ we obtain $d_{\mathrm{ext}}\le\min\{1,2^{21}\sqrt{\varepsilon}\}$, where $d_{\mathrm{ext}}=\sqrt{1-Ξ}$ and $Ξ$ is the optimal squared fidelity with the reference state under local extraction channels. A compactness argument then gives simultaneous qualitative robustness for all measurement actions on the state under common local isometries. As a consequence of the self-test, no maximally entangled state of any finite dimension can win the game perfectly.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24381v1
- Title: Versatile Quantum Machine Learning with an Ultra-low Power Photonic Quantum Reservoir Computer
- Authors: Wei Wang, Zan Tang, Menglong Fang, Daiqin Su, Mile Gu, Jayne Thompson, Lip Ket Chin, Hong Cai, et al.
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2609.24381v1  pdf=https://arxiv.org/pdf/2609.24381v1.pdf

Abstract:
Integrated photonic microprocessors provide high-bandwidth, massively parallel linear computation, but realizing nonlinear feature maps and temporal memory remain key challenges for machine learning. Conventional approaches rely on active tuning and additional nonlinear elements, increasing architectural complexity and power overhead. Here we demonstrate an integrated photonic quantum reservoir computer that achieves nonlinear mapping, fading memory, and task versatility without active tuning of the reservoir core. The same chip supports accurate static classification, dynamic prediction, and stable autonomous forecasting, establishing broad utility across both classification and temporal inference tasks. Competitive performance is retained in the zero-bias state, where all on-chip phase shifters are unpowered, eliminating active control and reducing computational power consumption to zero. This passive operation highlights a scalable route to multifunctional machine-learning hardware, where large-scale photonic quantum processors can be repurposed as reservoirs without reconfiguring their internal optical networks. By combining quantum-state encoding, multimode interferometric mixing, and photon-statistical readout, this architecture provides a physically grounded paradigm for low-power, large-scale quantum reservoir computing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24425v1
- Title: Quantum Work Extraction via Conditional Spatial Displacements
- Authors: Necati Çelik
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24425v1  pdf=https://arxiv.org/pdf/2609.24425v1.pdf

Abstract:
We propose a protocol for extracting work from a coherent quantum battery state by exploiting measurement-assisted feedback mediated by a continuous-variable pointer. The scheme relies on the unitary operator $U = \exp(-i k t \, \hat{H} \otimes \hat{P}/\hbar)$, which generates entanglement between the battery's energy eigenstates and the position of an auxiliary pointer. A subsequent projective measurement of the pointer's position conditionally prepares the battery in a pure state from which work can be extracted via a feedback unitary. We analyze the protocol for a two-level quantum battery and a Gaussian pointer, computing the conditional states and the corresponding daemonic ergotropy. For the pure initial state considered, we find that the daemonic ergotropy equals the standard ergotropy for all interaction strengths, demonstrating that the measurement-assisted feedback recovers the full extractable work that would otherwise become inaccessible due to entanglement with the pointer when its degrees of freedom are traced out. The protocol thus provides a physically transparent realization of a quantum Maxwell demon, where the pointer acts as a quantum measurement ancilla whose position becomes correlated with the battery's energy. The scheme is amenable to experimental implementation in trapped-ion systems, and it contributes to the ongoing efforts to understand the role of quantum coherence and measurement in thermodynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24475v1
- Title: Subspace Controllability in Variational Quantum Circuits: Maximising Expressivity and Increasing Search Efficiency with Dynamical Lie Algebras
- Authors: Andrew Rowan Barlow, Hans-Martin Rieser, Markus Lange
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24475v1  pdf=https://arxiv.org/pdf/2609.24475v1.pdf

Abstract:
Variational hybrid quantum models are a common paradigm for realising machine learning on quantum hardware. Nonetheless, they are challenging to train due to several problems intrinsic to the loss landscapes formed by variational quantum circuits. To mitigate these issues, researchers have extended the idea of subspace controllability leading to an increase in the success rate of variational models in finding the global minimum for quantum-based tasks. However, it remains unknown whether these results extend to classical-based tasks, and if any advantages are realised over a hyperparameter search. We begin to address this question by employing controllable circuits in a multi- classification task using MNIST-1D. Our results show that over a hyperparameter search, the majority of quantum models that achieve the lowest training and validation losses are subspace controllable. These results indicate that the hyperparameter search can be restricted to such models, in turn reducing computational cost and time.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24508v1
- Title: Statistical mechanics of multipartite entanglement in hypergraph states
- Authors: Paolo Scarafile, Giorgia Trotta, Paolo Facchi, Giuseppe Magnifico, Giorgio Parisi, Saverio Pascazio, Karol Życzkowski
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24508v1  pdf=https://arxiv.org/pdf/2609.24508v1.pdf

Abstract:
We investigate multipartite entanglement in a particular family of pure $n$-qubit hypergraph states through a statistical-mechanics framework, where the average bipartite purity maps onto an effective Hamiltonian of $2^n$ classical binary spins. In this correspondence, each hypergraph state uniquely corresponds to a classical spin configuration, while temperature serves as a control parameter that continuously interpolates between a uniform ensemble of random hypergraph states at high temperature and maximally multipartite entangled states (MMES) at zero temperature. Remarkably, the exponential of the zero-temperature entropy directly gives the number of MMES within the set of hypergraph states. For small system sizes ($n \leq 5$), we perform an exact enumeration, fully characterizing the energy landscape and associated thermodynamic observables, and validating known MMES counts. For larger systems ($n = 6$ and $7$), where exact methods become computationally infeasible, we employ simulated annealing and parallel tempering algorithms to efficiently sample the exponentially large state space. Our analysis yields quantitative predictions of the number of MMES and reveals how entanglement is statistically distributed across the sets of hypergraph states. These results establish hypergraph states as an ideal platform for investigating multipartite entanglement through thermodynamic methods, offering both computational advances and physical insights into the structure of quantum entanglement in restricted families of quantum states.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24558v1
- Title: Collective advantage from a minimal record in a quantum information engine
- Authors: Kangqiao Liu, Jie Gu, Deyou Chen
- Categories: quant-ph (primary); quant-ph; cond-mat.quant-gas; cond-mat.stat-mech; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2609.24558v1  pdf=https://arxiv.org/pdf/2609.24558v1.pdf

Abstract:
For a single particle, a quantum information engine can turn measurement fluctuations into transport by raising a barrier behind the particle each time its position is measured. When many particles are present, the barrier still depends on just one number, the position of the leftmost particle, so we let the demon measure that order statistic and nothing else. A demon that resolves every position instead pays a record entropy that grows with particle number, even though the extra distinctions never change where the barrier is placed. We show that the coarser measurement supplies an energy that is bounded independently of particle number, and that this bound yields a ceiling on the record entropy that falls as the filling increases. At the same tilt, the collective engine then delivers $44\%$ more work per recorded nat than independent single-particle engines, each with its own optimized cycle time and each running at equal or greater power per particle. Pauli blocking ends this advantage once the accessible region just above the wall fills. We also evaluate the coherence that the coarse measurement leaves behind, and the cost of placing the barrier imprecisely.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24561v1
- Title: A Reconfigurable Multilayer Quantum Key Distribution Network over Existing Metropolitan Fibre
- Authors: Mariella Minder, Andreas Siakolas, Elizabeth Pasatembou, Stylianos Mavrikos, Stephanos Yerolatsitis, Konstantinos Katzis, Kyriacos Kalli
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24561v1  pdf=https://arxiv.org/pdf/2609.24561v1.pdf

Abstract:
Scaling quantum networks requires architectures extending end-to-end service reachability despite constrained fibre and equipment. Critically, in brownfield deployments, the quantum network must be engineered around classical telecommunications infrastructure and the operating capabilities of quantum key distribution (QKD) technology. To address this, we demonstrate a seven-node, multilayer QKD network deployed over existing metropolitan fibre. The implementation compares spectral management techniques to accommodate inherited constraints across its layers. It combines a trusted-node ring with a three-node subnetwork interconnected through reconfigurable optical switching, extending physical connectivity and service reachability without an additional transmitter. A meshed key management layer maps endpoint requests onto trusted-relay paths and supplies Layer 1, Layer 3, and one-time-pad applications. Over 73 days, eight link configurations generated 119.4 Gbit of secret key material with 99.1% link availability. Randomised end-to-end requests revealed indirect cross-layer coupling between key consumption, stored-key state and quantum-layer reconfiguration, demonstrating resource sharing through reconfigurability, spectral multiplexing and logical key-management abstraction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24603v1
- Title: An Exact Operator Formulation of Statistical Quasiparticle Theory for Nonlinear System-Bath Coupling
- Authors: Yu Su, Yao Wang
- Categories: quant-ph (primary); quant-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2609.24603v1  pdf=https://arxiv.org/pdf/2609.24603v1.pdf

Abstract:
We develop an operator formulation of statistical quasiparticle theory for open quantum systems with nonlinear system-bath coupling, extending beyond the linear coupling setting of the standard Gaussian influence functional formulation. For Gaussian baths, the statistical quasiparticles, termed dissipatons, are explicitly constructed as collective operators in the thermofield bath space. Our construction provides a microscopic operator basis for the dissipaton algebra and generates hierarchical equations of motion directly from the Liouville equation. Nonlinear interactions are incorporated through a recursive generalized Wick's theorem, enabling automatic generation of hierarchical equations for polynomial couplings. The resulting framework connects explicit bath operator representations to nonperturbative, non-Markovian dynamics and unifies the treatment of linear and nonlinear system-bath interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24617v1
- Title: Explicit closed-form propagators for time-dependent gain-loss master equations
- Authors: Léonce Dupays
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24617v1  pdf=https://arxiv.org/pdf/2609.24617v1.pdf

Abstract:
Time ordering is a central obstacle in driven open-system dynamics governed by master equations with time-dependent rates. We derive explicit closed-form factorizations of the chronological and antichronological propagators for a time-dependent generator of the form $\mathcal{L}(t)=α(t)A+β(t)B$, when the commutator $[A,B]$ is a simultaneous eigenoperator of the adjoint actions of $A$ and $B$, namely $[A,[A,B]]=λ_{A}[A,B]$ and $[B,[A,B]]=λ_{B}[A,B]$. In contrast to the disentangling procedure known as the Wei-Norman decomposition, our construction determines the factorization coefficients directly, without solving a coupled system of nonlinear differential equations. Applying this result to the bosonic gain-loss Lindblad equation, we obtain the exact dynamical map for arbitrary time-dependent gain and loss rates. The gain-loss master equation provides a canonical description of a driven harmonic oscillator coupled to a thermal bath. We benchmark the construction by deriving the time evolution of the Wigner function of an initial Fock state and comparing it with independent phase-space results. We further apply the resulting dynamical map to evaluate the code-space survival probability of a binomial bosonic code under driven gain-loss dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24636v1
- Title: Phase space anatomy of dynamical quantum phase transitions
- Authors: Zakaria Mzaouali
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24636v1  pdf=https://arxiv.org/pdf/2609.24636v1.pdf

Abstract:
Dynamical quantum phase transitions (DQPT) are commonly defined either by the behavior of a late-time order parameter or by nonanalyticities in a quantum state's return rate. We show that discrete phase space fundamentally separates these two notions by the scale of information they require. An order parameter transition is determined by a local reduced state, requiring no quasiprobability negativity. In contrast, general global returns can contain information absent from every proper reduced state. For stabilizer returns, we derive an exact decomposition of the rate into distinct costs from loss of support and destructive quantum interference. Dynamics of a qutrit Potts chain show that selective cancellation can reverse the ranking of competing block returns and delay their exchange. An exact control also exhibits a thermodynamic return cusp with zero negativity at the crossing. The existence of a return singularity and the role of interference in selecting its branches are therefore distinct physical questions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24657v1
- Title: Circuit Hypernetworks for Quantum-Augmented Diffusion Language Models
- Authors: Xiaoqiang Wang, Mengyang Xiong, Jun Dai, Bang Liu
- Categories: quant-ph (primary); quant-ph; cs.CL
- Links: abs=https://arxiv.org/abs/2609.24657v1  pdf=https://arxiv.org/pdf/2609.24657v1.pdf

Abstract:
Language models can be adapted by changing the computations applied to individual tokens. Quantum circuits offer one such approach, but evaluating wider circuits inside a large model can be computationally demanding. Here we introduce HyperQ, which adds token-conditioned quantum residual branches to a frozen masked-diffusion language model. A quantum residual branch is a module in each transformer block that reads a token's hidden state, emits the coordinates of that token's circuit, executes it, and adds the measured values back through a residual connection. The backbone remains frozen, and only the added branches are trained. Within each branch, a lightweight circuit hypernetwork emits token-specific rotation angles, coupling strengths, and measurement axes in a shared sparse circuit structure. The required expectation values have an exact classical expression whose evaluation cost grows linearly with the qubit count, enabling circuits from 16 to 64 qubits to be trained within a 1.1-billion-parameter backbone. Across downstream benchmarks, increasing circuit width raises the average score from 47.65 to 54.30. At 64 qubits, HyperQ exceeds the backbone and its low-rank-adapted counterpart by 4.71 and 3.67 points, respectively. HyperQ is fine-tuned on 20,000 prompt-response pairs, compared with 200,000 for the classical baselines. These findings support token-conditioned circuit emission as a tractable architectural approach to quantum-augmented language modelling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24666v1
- Title: Experimental evidence of generalization in quantum machine learning in small-data regime
- Authors: Leena Anthony, Artemiy Burov, Nicolas Piro, Matteo Dal Peraro, Clément Javerzac
- Categories: quant-ph (primary); quant-ph; q-bio.QM
- Links: abs=https://arxiv.org/abs/2609.24666v1  pdf=https://arxiv.org/pdf/2609.24666v1.pdf

Abstract:
Quantum machine learning is a promising paradigm for learning from limited data, a central bottleneck in domains such as medical imaging, clinical trials, and rare diseases. Quantum convolutional neural networks (QCNNs) are particularly attractive in this setting, combining a hierarchical architecture with strong inductive bias and a parameter count that grows only logarithmically with system size. Their appeal rests on the generalization bounds of Caro et al. (2022), which show that the generalization error of a quantum model scales with the number of trainable parameters rather than with the Hilbert-space dimension, placing QCNNs in a potentially sample-efficient regime. We develop a hardware-compatible QCNN with mid-circuit measurement and classical feed-forward, and show on a binary handwritten-digit task that strong test performance is achievable from as few as 10 training samples, with the generalization error decreasing as the training set grows. At a matched 45-parameter budget the QCNN learns where an equally small classical convolutional network stays at chance, although an unconstrained classical baseline with roughly 25,000 parameters remains strongest when data are plentiful. Transpiling amplitude and angle encoded circuits across image resolutions from 2x2 to 512x512 pixels then exposes the dominant scaling bottleneck: amplitude encoding stays qubit-efficient but grows extremely deep, whereas angle encoding stays shallow but becomes qubit-prohibitive. On the medically motivated BreastMNIST benchmark the QCNN does not surpass the unconstrained classical network, yet it learns consistently above chance using orders of magnitude fewer parameters. Our results indicate that for QCNNs, learning from few samples is attainable in practice, whereas scaling to realistic image data is constrained less by optimization than by data encoding and hardware execution.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24670v1
- Title: Wigner-positive quantum states can have lower entropy than the vacuum
- Authors: Zacharie Van Herstraeten, Nicolas J. Cerf, Ulysse Chabaud
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24670v1  pdf=https://arxiv.org/pdf/2609.24670v1.pdf

Abstract:
The Wigner entropy conjecture posits that pure Gaussian states minimize the Shannon entropy of non-negative Wigner functions, known as the Wigner entropy. We show that mixing a specific pure Wigner-negative state with another suitably chosen quantum state can restore Wigner positivity while retaining a Wigner entropy that is slightly - but strictly - below the vacuum entropy. As a consequence, we disprove the Wigner entropy conjecture, as well as the stronger Wigner majorization conjecture, by deriving simple analytical counterexamples with violations of the entropy bound no larger than $10^{-3}$. Such states with sub-vacuum Wigner entropy can be found arbitrarily close to the vacuum and can also exhibit sub-vacuum Wigner-Rényi $α$-entropy for $0<α<2$. We identify the physical mechanism behind the existence of such states, which arises from a subtle interplay between the uncertainty principle and non-Gaussianity. The key idea of this paper was developed with the help of AI tools, building on the characterization of extreme non-negative Wigner functions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24680v1
- Title: Unified spatiotemporal quantum states and spatiotemporal entanglement from Kirkwood-Dirac phase space
- Authors: Zhian Jia, Mei-Hui Xiao
- Categories: quant-ph (primary); quant-ph; gr-qc; hep-th
- Links: abs=https://arxiv.org/abs/2609.24680v1  pdf=https://arxiv.org/pdf/2609.24680v1.pdf

Abstract:
The notion of a spatiotemporal quantum state extends the conventional concept of a spatial quantum state to the spatiotemporal domain. Such states are represented by unit-trace operators that encode correlations among quantum events distributed across space and time. In this work, we use the spatiotemporal Kirkwood-Dirac phase space to provide a unified characterization of spatiotemporal quantum states. Spatiotemporal states obtained from Kirkwood-Dirac distributions are generally non-Hermitian and nonnormal; whereas those constructed from Margenau-Hill distributions are Hermitian. We provide a unification via (quasi)probabilistic mixture of Kirkwwod-Dirac spatiotemporal states which encompasses almost all existing formulations of spatiotemporal quantum states. We derive recursive expressions for spatiotemporal states and elucidate the relation between Kirkwood-Dirac nonclassicality and the temporality of spatiotemporal states. We further extend the construction to many-fold correlation functions and establish its connection with out-of-time-ordered correlators (OTOCs). We also develop a more general unifying framework based on (quasi)probabilistic mixture of $s$-parametrized spatiotemporal states and establish their Petz time reversal and application in studying Kubo-Martin-Schwinger (KMS) condition in two-time setting. Finally, we apply this framework to characterize quantum entanglement in spacetime and analyze spatiotemporal entanglement using several complementary entropy measures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24759v1
- Title: Superconducting qubit based on altermagnets
- Authors: Xue-Feng Pan, Xin-Lei Hei, Franco Nori, Peng-Bo Li
- Categories: quant-ph (primary); quant-ph; cond-mat.supr-con
- Links: abs=https://arxiv.org/abs/2609.24759v1  pdf=https://arxiv.org/pdf/2609.24759v1.pdf

Abstract:
Altermagnets, characterized by vanishing net magnetization and momentum-dependent spin splitting, provide a promising platform for next-generation Josephson devices. Here, we exploit the Josephson effect in superconductor-altermagnet-superconductor junctions and show how to engineer prescribed current-phase relations by device design. Based on these programmable Josephson potentials utilizing altermagnetism, we propose a new class of transmon-like superconducting qubits that combine large anharmonicity with enhanced robustness against decoherence via coherent two-Cooper-pair tunneling. We show that in the $2φ$-junction regime, this kind of qubit provides intrinsic protection against charge noise due to parity protection. Magnetic flux can be used to precisely control the qubit and, under appropriate bias, this architecture further suppresses charge and flux noise. Our results establish altermagnets as a versatile platform for Josephson-potential engineering and open a new route toward high-performance superconducting qubits combining high coherence, large anharmonicity, and broad tunability.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24794v1
- Title: Observable-targeted variational quantum simulation of Hamiltonian dynamics
- Authors: Leonardo Zambrano, Luciano Pereira, Antonio Acín
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24794v1  pdf=https://arxiv.org/pdf/2609.24794v1.pdf

Abstract:
Standard variational quantum simulation seeks to reproduce the evolution of the full quantum state, although many applications require only the expectation values of a few observables. We study a variational method for pure-state Hamiltonian dynamics that updates circuit parameters to reproduce the evolution of selected expectation values. An exact error identity guides the choice of observables, motivating a construction based on repeated commutators of the target with the Hamiltonian. For Pauli observables and Pauli-rotation circuits, the update can be estimated without ancillary qubits or controlled operations for overlap estimation. Across six-qubit spin, fermionic, and molecular benchmarks, the targeted update extends the median time within the target-error tolerance by up to a factor of $4.2$ relative to standard variational quantum simulation at equal shot budgets. These results show that directing the variational update toward the target observable can extend accurate simulation without increasing the measurement cost per time step.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24805v1
- Title: Stabilizing temporal quantum-enhanced sensitivity via sub-optimal measurements
- Authors: Wangsheng Zheng, Yaoling Yang, Abolfazl Bayat
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24805v1  pdf=https://arxiv.org/pdf/2609.24805v1.pdf

Abstract:
In non-equilibrium probes, quantum-enhanced sensitivity is quantified through super-linear scaling of precision with respect to time, as a central metrology resource. However, this requires optimal measurements, which are often complex and time-dependent, making it challenging in practice. Sub-optimal measurements typically fail to retain robust super-linear scaling and show oscillations. Here, we begin by establishing a universal temporal scaling law in a general multi-parameter non-equilibrium quantum sensing framework. Within this setting, we identify the universal behavior of the sensing precision with sub-optimal measurements which shows quadratic scaling modulated by an additional bounded oscillatory function. To remove the oscillatory part, we propose a protocol in which measurements are partitioned into different groups, each performed at different times. The collective precision obtained from this protocol stabilizes a robust quadratic scaling even for sub-optimal measurements in the multi-parameter regime. We validate our protocol through three distinct examples as well as Bayesian estimation. Our protocol is applicable to every informative measurement and takes a key step towards practical realization of quantum-enhanced sensitivity.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24835v1
- Title: Trade-offs and experimental feasibility of nonlocal polygamy with two-outcome Bell inequalities
- Authors: Josep Batle, Tomasz Rybotycki, Tomasz Białecki, Piotr Gawron, Adam Bednorz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24835v1  pdf=https://arxiv.org/pdf/2609.24835v1.pdf

Abstract:
Entanglement and Bell nonlocality have different sharing constraints across subsystems of a multipartite quantum system. We examine simultaneous violations of Bell inequalities with two-outcome observables and two or three measurement settings per party. We identify configurations whose simultaneous violations can be demonstrated on IBM Quantum hardware, and derive bounds and trade-off relations for several polygamous configurations. The results connect experimental capabilities of quantum computers with mathematical methods for studying the limits of quantum correlations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24858v1
- Title: Overcoming the Hong-Ou-Mandel interference limitation for the second photon from a two-photon cascade
- Authors: Raphael Joos, Michal Vyvlecka, Tim Strobel, Benjamin Breiholz, Furkan Aglarci, Ponraj Vijayan, Hans-Georg Babin, Arne Ludwig, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; physics.optics
- Links: abs=https://arxiv.org/abs/2609.24858v1  pdf=https://arxiv.org/pdf/2609.24858v1.pdf

Abstract:
Quantum emitters such as semiconductor quantum dots can provide entangled photon pairs emitting from a system of cascaded states. However, the resulting temporal correlation between the two photons from the three-level ladder system has been shown to set a limit on the achievable two-photon interference. In this work, we show that such limitation, for photons emitted by the second transition, is only due to reduced temporal overlap at the interference beam splitter. We investigate this theoretically and experimentally by determining time-resolved four-photon coincidences between two successively emitted photon pairs. Post-emission synchronization shows the recovery of maximum interference visibility; in prospective quantum networks this could be achieved via deterministic quantum memories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24900v1
- Title: Explanation of the Observed Energy Exchange through the vacuum in Optomechanics
- Authors: Vincenzo Macrì, Franco Nori, Alessandro Ferreri
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24900v1  pdf=https://arxiv.org/pdf/2609.24900v1.pdf

Abstract:
In cavity optomechanics, the standard large-detuning regime is commonly described by retaining only the radiation-pressure interaction, while higher-order mirror--field interactions are assumed to be negligible. This approximation, however, fails to provide a microscopic explanation for the vacuum-mediated heat transfer observed between the mechanical membranes in the experiment of Fong, et.al.,[Nature \textbf{576}, 243 (2019)], whose physical origin has remained under active debate. Here, using a fully quantum model, we show that the neglected higher-order optomechanical interactions naturally generate phonon-phonon coupling and quantitatively account for the observed energy exchange within the standard optomechanical framework. Building on this microscopic description, we further propose a protocol in which phonon-phonon interaction drives a cyclic process enabling net work extraction. Our results establish the fundamental role of higher-order optomechanical interactions and provide a microscopic framework for describing next-generation optomechanical experiments beyond the linear approximation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24933v1
- Title: A thermal microwave bus for neutral atom quantum computing
- Authors: Matthew J. H. Kendall, Christopher J. Watson, Michael Ben Shem, Jonathan D. Breeze
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24933v1  pdf=https://arxiv.org/pdf/2609.24933v1.pdf

Abstract:
High-fidelity two-qubit gates in neutral-atom arrays rely on the Rydberg blockade, which is intrinsically short ranged and requires long range connectivity to be achieved through atom shuttling. We propose a four level architecture, where the typical ground state qubit can be leveraged for its long lifetime and the Rydberg states couple to a microwave cavity, allowing for long range cavity mediated gates. We first find the thermal dependence of two established protocols, the dispersive iSWAP native to the Tavis-Cummings model and the Controlled phase gate generated from driving the cavity. We simulate them under the presence of Rydberg decay, thermal photons, finite cavity linewidth and find fidelities which accompany closed form bounds. We then introduce the bichromatic Raman gate, which only virtually populates the Rydberg states and cancels dispersive shifts to mitigate both atomic and cavity decay, achieving a fidelity of $F = 0.997$. Finally, we consider a full optical tweezer array in a microwave cavity, and show that using a cavity mediated gate to close the periodic boundaries of the toric code shortens an error correction round by a factor of 2.3 for realistic array sizes. This was then applied to the wider family of Bivariate bicycle codes, and we find that it shortens a round of the gross code by a factor of 4.8.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24941v1
- Title: Efficient Heralding of Loss-Tolerant Photonic GHZ States for Device-Independent Conference Key Agreement over Long Distances
- Authors: Yazeed K. Alwehaibi, Makoto Ishihara, Shakib Daryanoosh, Ewan Mer, Shang Yu, Wojciech Roga, Ian A. Walmsley, Masahiro Takeoka, et al.
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24941v1  pdf=https://arxiv.org/pdf/2609.24941v1.pdf

Abstract:
Heralded multipartite entanglement distribution is a key requirement for device-independent conference key agreement (DI-CKA) over lossy quantum networks. Although locally equivalent in the absence of loss, different single-rail photon-number encodings of Greenberger-Horne-Zeilinger (GHZ) states can exhibit substantially different loss tolerance. We show that computational-basis GHZ states, comprising a coherent superposition of vacuum and an $n$-photon component, enable detection-loophole-free parity-CHSH violations at markedly lower detection efficiencies than previously considered fixed-photon-number GHZ states, and derive exact analytical conditions for the critical detection efficiencies of both state classes. Motivated by this advantage, we introduce a star-network protocol using heterogeneous sources to directly herald vacuum-$n$-photon GHZ states with long-distance scaling $O(η_{\mathrm{c}}^{n/2})$, where $η_{\mathrm{c}}$ is the channel transmittance. For four users, we characterize the heralded state under photon loss and show that tunable source parameters preserve genuine multipartite entanglement at any finite channel distance. For both ideal Pauli measurements and experimentally accessible displacement-based measurements, our protocol enables DI-CKA at detection efficiencies achievable with current photodetectors, while retaining key rates and communication distances comparable to those of previous heralded schemes. We discuss physical implementations and analyze an SPDC-based realization, showing that source-induced asymmetry can make measurement-role assignment in the parity-CHSH test crucial. These results identify photon-number encoding, source architecture, and measurement-role assignment as design parameters for loss-tolerant multipartite quantum networks and enhanced DI-CKA performance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24953v1
- Title: Tight entropy contraction beyond detailed balance
- Authors: Li Gao, Jingyu Guo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.24953v1  pdf=https://arxiv.org/pdf/2609.24953v1.pdf

Abstract:
We establish quantitative entropy contraction bounds for finite-dimensional quantum channels beyond detailed balance. For channels compatible with a faithful conditional expectation, we show that GNS (Gelfand--Naimark--Segal) norm contraction yields relative entropy contraction with only a logarithmic loss in the dimensional constant. For quantum Markov semigroups with a faithful asymptotic conditional expectation, this gives a lower bound on the complete modified logarithmic Sobolev constant in terms of the GNS spectral gap. The bounds allow initial entanglement with an external environment and are independent of its system size. Applications to alternating reservoir pulses and continuously coupled energy ladders give bounds with optimal size dependence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2503.06124v3
- Title: Two and three-state quantum heat engines with stochastic resetting
- Authors: Ashutosh Kumar, Sourabh Lahiri, Trilochan Bagarti, Subhashish Banerjee
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2503.06124v3  pdf=https://arxiv.org/pdf/2503.06124v3.pdf

Abstract:
Quantum heat engines have undergone extensive studies over the last two decades. Simultaneously, the studies of the applications of stochastic resetting in various fields are on the rise. We explore the effect of stochastic resetting on the dynamics of a two-level and a three-level quantum heat engine. The extracted work is shown to increase with the resetting rate. The effective efficiency that takes into account the work done due to resetting remains constant. However, if the work done due to resetting is ignored, then the system can incorrectly imply a different behaviour, including the false inference that it is not working as an engine at all. The efficient power is observed to increase beyond that obtained in the absence of resetting, and is shown to be higher for a three-level engine.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2608.19696v1
- Title: Coherence protection of a silicon hole spin qubit with phase-modulated microwave driving
- Authors: Sayyid I. Ibad, Yusuke Sato, Takuma Kuno, Itaru Yanagi, Toshiyuki Mine, Ryuta Tsuchiya, Digh Hisamoto, Hiroyuki Mizuno, et al.
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2608.19696v1  pdf=https://arxiv.org/pdf/2608.19696v1.pdf

Abstract:
Hole spins in silicon quantum dots are a promising platform for quantum computing due to their strong intrinsic spin-orbit coupling (SOC), which enables fast, all-electrical control. However, this coupling also increases their susceptibility to charge noise, thereby limiting coherence times. Moreover, holes in silicon are also affected by hyperfine interactions with residual nuclear spins in the silicon substrate, introducing a non-negligible source of low-frequency noise. Here, we implement a phase-modulated concatenated continuous driving (CCD) technique for hole spin qubits to suppress low-frequency noise through microwave phase modulation. This approach stabilizes Rabi oscillations and extends the oscillation decay time compared to the conventional method. Furthermore, by defining a qubit in the CCD frame, we achieve coherent control while simultaneously protecting the qubit from noise, confirming coherence protection during gate operations. These results demonstrate a viable route toward noise-robust hole spin qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22186v1
- Title: Design of a Lamb-Shift Polarimeter for $^3$He Ions and Atoms
- Authors: N. Faatz, R. Engels, C. Kannis, S. J. Pütz, J. Steinhage
- Categories: physics.ins-det (primary); physics.ins-det; physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.22186v1  pdf=https://arxiv.org/pdf/2609.22186v1.pdf

Abstract:
In high energy physics experiments $^3$He$^{2+}$ nucleons are suitable to test the internal structure of neutrons, which makes them the perfect substitute. Moreover, it is one of the atomic species for which high polarization values are achievable through the use of optical pumping methods. Therefore, nuclear polarized sources for $^3$He$^{2+}$ ions are currently in development. Consequently, detector systems validating their nuclear polarization value need to be established. Such a detector system, based on the Lamb-shift polarimeter, is introduced in this work. Its advantage is that it can operate at low energies in the range of 10 to 100 keV, which makes preacceleration unnecessary. In addition, a fast evaluation of the nuclear polarization within seconds leads to shorter disruptions for beam times.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22420v1
- Title: Bootstrap certification of string order in quantum spin chains
- Authors: Sagnik Banerjee, Haoyu Guo, Debanjan Chowdhury
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2609.22420v1  pdf=https://arxiv.org/pdf/2609.22420v1.pdf

Abstract:
The many-body bootstrap certifies ground-state properties by minimizing energy over correlators constrained only by positivity, without any variational wavefunction. Its cost, however, grows exponentially with the size of the operators involved, placing the long-range string correlators that diagnose topological phases out of reach. We overcome this by treating string operators as primary objects: bare and endpoint-dressed strings satisfy a closed operator algebra with one another and with local words, yielding a semidefinite program whose cost grows only polynomially with string length. A single computation then yields estimates of string correlators of all lengths. Rigorous two-sided bounds are obtained for each target string once the ground-state energy is pinned within a window. When benchmarked against density-matrix renormalization group computations on the cluster Ising and spin$-1$ Heisenberg chains, the method certifies the nonlocal string order of the cluster and Haldane phases directly from the Hamiltonian. Our rigorous certification of string order parameters reveal that the sharpness of the bounds is set by which operators enter the calculation, not by their length alone. By exploiting algebraic closure of strings and local words, our framework lifts spatially extended observables into polynomially tractable bootstrap variables, opening up a route to wavefunction-free certification of nonlocal order in quantum many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22504v1
- Title: Tripartite Form Universality in Holographic Entropy Inequalities
- Authors: Veronika E. Hubeny, Yu Liu
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2609.22504v1  pdf=https://arxiv.org/pdf/2609.22504v1.pdf

Abstract:
To elucidate the meaning of holographic entropy inequalities (beyond subadditivity) which characterize the entanglement structure of geometric states in holography, arXiv:2309.06296 proposed the "tripartite form" for these inequalities, consisting of tripartite information and conditional tripartite information terms with unit coefficients. While this provides a compact and useful packaging of the inequalities, it is not a priori guaranteed that all inequalities can be recast in this form. Here we conjecture that they can, and present substantial evidence, by proving that the two known infinite families of holographic entropy inequalities found in arXiv:2309.15145 can indeed be written in the tripartite form. This is significant because such recasting is particularly nontrivial for these families. Apart from providing the explicit tripartite form expressions for every member of these two infinite families, we detail how we arrived at them, in the process deriving several useful identities which may serve as stepping stones to formulate further repackaging of the corresponding information quantities. We also illustrate the power of the tripartite form by proving a number of structural properties satisfied by any holographic entropy inequality.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22729v1
- Title: Can Chemically Inspired Parameter Initialization Mitigate Barren Plateaus in Variational Quantum Eigensolvers?
- Authors: Zhangyu Yang, Jinzhao Sun, Jianpeng Chen, Weitang Li, Zhigang Shuai
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.22729v1  pdf=https://arxiv.org/pdf/2609.22729v1.pdf

Abstract:
Recent advances in the variational quantum eigensolver (VQE) have strengthened its promise for molecular electronic-structure calculations on near-term noisy intermediate-scale quantum (NISQ) devices. However, barren plateaus (BPs) remain a major obstacle to scaling VQE, as vanishing gradients can severely obstruct optimization at large scale. While most BP studies focus on randomly initialized circuits and global gradient behavior, practical quantum chemistry VQE typically uses chemically motivated initializations and local optimization around HF- or MP2-derived states. Although chemically informed initializations are widely expected to improve VQE trainability, how they mitigate local barren plateaus remains unclear. We therefore study the occurrence of local barren plateaus in molecular UCCSD-VQE, considering both chemically motivated initialization points and iterates along the corresponding optimization trajectories. In the benchmarks considered here, chemically initialized starting points and variational trajectories show polynomial decay of local gradient variance with system size instead of the exponential BP-like decay observed for random controls, indicating that chemical initialization mitigates barren plateaus in the local optimization regions and highlights the trainability advantage of chemically motivated VQE strategies.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22817v1
- Title: Exact ballistic energy transport and emergent XXZ dynamics in an integrable three-state chain
- Authors: Hanbing Liang, Fujun Liu
- Categories: physics.comp-ph (primary); physics.comp-ph; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2609.22817v1  pdf=https://arxiv.org/pdf/2609.22817v1.pdf

Abstract:
We investigate the coupling dependence of ballistic energy transport and the emergent spin dynamics in an integrable Hermitian three-state chain that connects a clock interaction to a highly degenerate flag limit. By constructing a regular $R$-matrix to establish a globally conserved energy current, we analytically evaluate its full variance to obtain the exact, strictly positive leading high-temperature coefficient of the thermal Drude weight and the ballistic growth rate of the energy-correlation second moment. In the strong-coupling limit, the degeneracy is lifted by virtual transitions of a delocalized third-color spectator state, which generates an effective spin-$1/2$ XXZ Hamiltonian with anisotropy $Δ= -1/2$ and fundamentally selects the all-active two-color sector as the true ground state. For periodic boundaries, this virtual spectator motion introduces a positive length-changing XXZ supercharge squared that, for $L\ge4$, strictly annihilates all states within a finite, length-independent energy interval above the ground state. Consequently, we rigorously prove that the full periodic effective theory perfectly replicates the exact low-energy XXZ spectrum, including all state multiplicities, as well as its macroscopic bulk free-energy density.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.22890v1
- Title: Time and causality in quantum gravity
- Authors: Charis Anastopoulos
- Categories: gr-qc (primary); gr-qc; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2609.22890v1  pdf=https://arxiv.org/pdf/2609.22890v1.pdf

Abstract:
The problem of time in quantum gravity is often presented as a consequence of applying quantum theory to general relativity. These notes adopt a broader perspective. We first examine how time enters classical mechanics, relativity, quantum theory, and quantum field theory, distinguishing three principal aspects: causal order, temporal duration, and the present. This analysis shows that the conceptual difficulties associated with time do not arise only when gravity is quantised. Tensions between causal structure, clocks, observables, and measurement are already present in the theories from which quantum gravity is constructed. We then survey responses to the problem of time across the principal approaches to quantum gravity. These include canonical and Wheeler-DeWitt quantisation, path-integral and histories formulations, perturbative and background-dependent approaches, causal sets, and twistor theory. The programmes are compared according to whether they retain an external time, render time problematic through quantisation, or incorporate causal or temporal structure into their foundations. Particular emphasis is placed on questions arising from quantum foundations and relativistic quantum information. We conclude by examining linearised gravity and weak-gravity quantum systems. This regime shows that the problem of time is not confined to Planck-scale physics, but arises already in attempts to provide a predictive and operationally meaningful quantum description of spacetime near flat geometry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23295v1
- Title: Non-Markovian Quantum Dynamics of Exciton-Polaritons
- Authors: Rajanya Sarkar, Pritha Ghosh, Arshath Manjalingal, David R. Reichman, Arkajit Mandal
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2609.23295v1  pdf=https://arxiv.org/pdf/2609.23295v1.pdf

Abstract:
Exciton-polaritons, hybrid light-matter quasiparticles formed when a material interacts with a confined electric field, have experimentally been shown to exhibit mesoscale coherent quantum propagation that remains robust at room temperature. However, an accurate and direct quantum dynamical simulation of this phenomenon that does not resort to semi-classical approximations is prohibitively expensive computationally, limiting the microscopic understanding of the rich dynamical interplay among phonons, photons, and electrons under collective light-matter coupling. To address this fundamental challenge, we develop a non-Markovian master equation approach which enables the fully quantum mechanical simulation of non-equilibrium exciton-polariton dynamics and captures phonon-induced decoherence and dissipation beyond the conventional Markovian limit. To carry out this task, a procedure is developed in which the wave vector space is coarse-grained and each diagonal element of the density matrix is evolved in parallel. To demonstrate the utility of this approach, we simulate exciton-polariton transport in TIPS-pentacene. We find that our approach reasonably captures the experimentally observed renormalization of the polariton group velocity, which originates from the phonon-induced non-Markovian Lamb shift. We further show that this renormalization cannot be reproduced within conventional Markovian theories.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23513v1
- Title: Critical Touching of Temporal Entanglement Transitions
- Authors: Ting-Long Wang, Shi-Xin Zhang, Shuai Yin, Yi-Fan Jiang
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2609.23513v1  pdf=https://arxiv.org/pdf/2609.23513v1.pdf

Abstract:
Equilibrium phase transitions are conventionally categorized into first-order and continuous phase transitions. Far from equilibrium, many new transitions emerge during the real-time evolution of quantum systems. One such transition is the temporal entanglement transition (TET) characterized by the nonanalyticity of the entanglement spectrum. So far, all TETs occur through a linear crossing of the leading Schmidt levels in different symmetry sectors, resembling a first-order transition in equilibrium. A natural question is whether a continuous TET, featured by entanglement spectrum touching, is possible. In a periodically driven transverse $J_1$-$J_2$ Ising chain, we show that two such TETs can merge into a critical touching, where the leading levels meet tangentially without exchanging, realizing the temporal analog of a continuous phase transition. Near the critical frequency, the temporal separation of the two TETs vanishes continuously and its derivative with respect to frequency diverges, a nonanalytic signature that is absent in a single first-order TET. This finite-frequency touching arises from the interplay between a weak symmetry-preserving perturbation of the product initial state and Floquet corrections. Further extending the frequency scan reveals a second critical touching at a higher frequency, and the two critical frequencies enclose a finite window with no TET. These features can be understood from a second-order Floquet Hamiltonian and persist across a broad range of coupling ratios, establishing the critical touching as a distinct form of TET.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.23794v1
- Title: Sum of Three Squares and Particle in a Cubic Box - Degeneracies
- Authors: S. Pratik Khastgir
- Categories: math-ph (primary); math-ph; math.NT; quant-ph
- Links: abs=https://arxiv.org/abs/2609.23794v1  pdf=https://arxiv.org/pdf/2609.23794v1.pdf

Abstract:
We address the problem of determining the degeneracy of a particular energy eigenvalue corresponding to a quantum particle trapped in a cubic box. In other words, we aim to find the number of ways a specific positive integer can be written as the sum of three natural number squares. This is a classic problem in number theory. We provide a closed-form, exact solution to the problem. We do not claim to provide proofs, as we have none; instead, we build up the formulae starting from simple cases where the answer could be deduced by studying the list of degeneracies. We present ample examples that could be verified against the degeneracy calculated numerically via the brute-force method. We arrived at the solution by meticulously studying the list of degeneracies for the first five million numbers, generated by Mathematica$^{\circledR}$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24168v1
- Title: A complete characterization of eventually entanglement breaking unital quantum channels
- Authors: B. V. Rajarama Bhat, Pankaj Dey, Biswarup Saha
- Categories: math.OA (primary); math.OA; math-ph; math.FA; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24168v1  pdf=https://arxiv.org/pdf/2609.24168v1.pdf

Abstract:
We obtain a complete characterization of eventually entanglement breaking (EEB) unital channels in terms of some simple commutation properties of their eigenvectors. Specifically, the following properties are equivalent for a unital channel: (i) it is EEB; (ii) it is eventually positive partial transpose (PPT); (iii) it is eventually mixed twisted dephasing; and (iv) its eigenvectors corresponding to non-zero eigenvalues commute with all its peripheral eigenvectors. Similar results hold for one-parameter semigroups of unital quantum channels, where continuity forces such semigroups to become primitive. We employ a matrix integral technique inspired by a result of Watrous. We also characterize the extreme points of the convex set of unital EB channels and, using this characterization and the theory of equiangular tight frames (ETFs), identify several extreme points beyond the twisted dephasing channels.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24211v1
- Title: Universal Dynamics of a Spin-$3/2$ Fermi Gas in Traps with Distinct Spectra
- Authors: Shuyi Li, Qiang Gu
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24211v1  pdf=https://arxiv.org/pdf/2609.24211v1.pdf

Abstract:
Universal power-law decay of spin-mixing oscillations has been observed in a harmonically trapped spin-$3/2$ Fermi gas, whose exactly equally spaced spectrum represents a highly special case. To gain insight into the origin of this behavior, we investigate the dynamics in traps with increasing and decreasing level spacings, represented by the infinite square well and the Pöschl--Teller potential, respectively. Despite pronounced differences in their single-particle spectra, all systems exhibit power-law decay of coherent oscillations, described by $A(t) = A_{0} - γt^α$. The exponent $α$ remains insensitive to particle number, interaction strength, and the overall energy scale, but exhibits systematic differences among traps with distinct spectral structures. In contrast, the decay parameter $γ$ is strongly influenced by both the spectral structure and the overall energy scale. These findings demonstrate that power-law decay is not restricted to the harmonic trap but persists across qualitatively distinct spectral structures. The observed variation of $α$ among different traps further suggests that the underlying single-particle spectrum plays an important role in shaping the decay dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24230v1
- Title: Fault-Class-Matched Test Oracles for Output-Invisible Quantum Transpiler Regressions
- Authors: Furqan Nasir, Arif Shah, Iftikhar Alam
- Categories: cs.SE (primary); cs.SE; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24230v1  pdf=https://arxiv.org/pdf/2609.24230v1.pdf

Abstract:
Test oracles for quantum transpilers typically judge correctness by comparing compiled output against a reference: a statevector, a sampled distribution, or a unitary compared modulo global phase. A companion empirical study measures how often that choice fails. Roughly 28% of merged Qiskit transpiler bug-fixes (95% Wilson CI 19-40%) repair a fault that corrupts layout metadata, global phase, or run-to-run reproducibility while output stays correct: invisible to a black-box output-equivalence oracle by construction. This paper closes that gap with a fault-class-matched, layout-aware, width-tiered oracle family: a layout/permutation contract checker and a contract-level metamorphic relation (MR-1) for the metadata channel, a global-phase tracker for the phase channel, and a determinism runner for reproducibility. Verified from source on nine real, merged Qiskit transpiler regressions (three per channel), the output-equivalence oracle is blind throughout and the matched mechanism fires on every case. A 675-configuration sweep of the contract/metadata invariant finds no false positive. Synthetic mutant families confirm reliability at scale: 1.00 sensitivity and specificity across 36 mutants apiece for the contract/metadata and global-phase channels, and 1.00 sensitivity (95% CI 0.44-1.00) for reproducibility on the three circuits where the mutation is constructible. The contract checker costs two to six orders of magnitude less than a plain output check, the global-phase tracker is comparably cheap within its exact tier, and only the metamorphic relation carries a bounded cost. Ported natively to pytket/tket, the global-phase mechanism transfers cleanly, an identical 1.00/1.00 result with phases recovered to double-precision accuracy, evidence against a Qiskit-specific artifact.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24247v1
- Title: Thermal Evolution and Disorder Dependence of the Bose-glass: Spatial, Spectral, and Localization Signatures
- Authors: Madhumita Kabiraj, Raka Dasgupta
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24247v1  pdf=https://arxiv.org/pdf/2609.24247v1.pdf

Abstract:
In this work, we characterize the glassy character of the Bose-glass phase in a disordered Bose-Hubbard model using three complementary diagnostics: the finite-temperature spectral function, spatial inhomogeneity, and the inverse participation ratio. Spectral analysis, obtained from finite-temperature Green's function and random phase approximation, shows that disorder introduces localized low-energy states within the Mott gap, eventually closing the gap at sufficiently strong disorder. Spatial inhomogeneity, calculated using the Gutzwiller ansatz, increases sharply with disorder and then saturates at moderate disorder strengths. The inverse participation ratio has been calculated from the exact diagonalization of a small system, and it reveals enhanced localization with stronger disorder. Increasing temperature suppresses these disorder-induced features: the low-energy spectral weight diminishes, the spatial inhomogeneity varies more smoothly, and the IPR decreases. Taken together, these diagnostics show that disorder drives the development of glassy character, while thermal fluctuations gradually wash out its signatures. The early saturation of spatial inhomogeneity compared with the continued evolution of low-energy excitations and the inverse participation ratio demonstrates that no single diagnostic fully captures the evolution of the Bose-glass state, highlighting the need for a combined characterization.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24281v1
- Title: Electronic-Entropy-Driven Phase Transitions in Compressed Iron Oxides
- Authors: S. Azadi, S. M. Vinko, C. Crepisson, A. Principi, T. D. Kuehne, M. S. Bahramy
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; physics.plasm-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24281v1  pdf=https://arxiv.org/pdf/2609.24281v1.pdf

Abstract:
Electronic entropy is usually treated as a secondary correction to structural stability, but under strong electronic excitation it can become a primary thermodynamic driving force. Here we show that electronic entropy can drive both polymorphic and stoichiometric phase transformations in compressed iron oxides. Using finite-temperature density functional theory, we calculate the electronic-temperature-dependent Gibbs free energies of Fe$_2$O, FeO, Fe$_4$O$_5$, Fe$_3$O$_4$, and multiple Fe$_2$O$_3$ polymorphs, including $α$-, $ι$-, $ζ$-, $η$-, and $θ$-Fe$_2$O$_3$, over the pressure range 60--260 GPa. At 60-140 GPa, electronic excitation mainly reorganizes the relative stability of Fe$_2$O$_3$ polymorphs, driving transitions from $ι$-Fe$_2$O$_3$ to $η$-Fe$_2$O$_3$. At 180 GPa, the free-energy landscape becomes strongly competitive as FeO is stabilized over an intermediate range of electronic temperature, while $η$-Fe$_2$O$_3$ becomes favourable at higher T. At 220-260 GPa, the lowest-free-energy phase at low T is the Fe-rich compound Fe$_2$O, but increasing electronic temperature stabilizes FeO. These results demonstrate that electronic entropy can control not only the relative stability of crystal structures at fixed composition, but also the competition between different iron-oxide stoichiometries. The predicted electronic-entropy-driven phase boundaries provide a route to nonthermal structural transformations in ultrafast and high-energy-density experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24284v1
- Title: Quantum many-body framework for passive-scalar turbulence
- Authors: Zhaoyuan Meng, Long Wang, Guowei He
- Categories: physics.flu-dyn (primary); physics.flu-dyn; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24284v1  pdf=https://arxiv.org/pdf/2609.24284v1.pdf

Abstract:
How spatial structures manifest in multi-time correlations is a fundamental question in turbulence. We develop a non-Hermitian bosonic framework that unifies equal-time anomalous statistics and their temporal propagation within a common operator representation. A continuous Wegner flow reorganizes stochastic mode couplings in an extended wave-frequency space. Applied to the Taylor-Kraichnan model, the framework recovers the established equal-time hierarchy and constructs multi-time contributions through propagators acting on successively smaller sets of active fields. This construction separates uniform transport from intrinsic relative dynamics and shows how a higher-order equal-time state evolves under a generator acting only on the fields that remain dynamically active. Within an isotropic radial closure, we derive an explicit fourth-order two-time zero mode scaling function that describe how relative dispersion progressively weakens sensitivity to the initial separation. The framework thus connects spatial intermittency to temporal evolution by identifying how the sequence of observation times determines the propagation of equal-time anomalous structures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24295v1
- Title: Vacancy aggregation enhances NV- spin coherence in diamond: a cluster-correlation-expansion study of multi-vacancy spin baths in semiconductors
- Authors: Chikara Shinei
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24295v1  pdf=https://arxiv.org/pdf/2609.24295v1.pdf

Abstract:
Annealing a semiconductor makes its vacancies mobile; they aggregate into multi-vacancy complexes that often carry spin. Such centres are a magnetic-noise source for any spin qubit among them, in silicon and silicon carbide as well as in diamond, and they are accordingly blamed for NV- decoherence in irradiated and implanted diamond, with two coherence records credited to removing them. Cluster-correlation-expansion simulations driven by published electron-paramagnetic-resonance parameters invert that attribution. At a fixed paramagnetic spin density a multi-vacancy bath gives a Hahn-echo coherence time 2.7-4.4 times longer than a bath of isolated negative vacancies, constant over three decades of concentration. A bath dephases the qubit because its spins exchange spin projections with one another, and two can exchange only if their transition frequencies match. A fine-structure splitting shifts those frequencies. Were every defect on the same crystallographic site, all would shift alike and still match: worth only a factor 1.3. Real defects occupy symmetry-equivalent sites pointing in different directions, so neighbours land at different frequencies and stop exchanging: a further 1.9. What governs the coherence time is therefore the fraction of bath pairs sharing a transition frequency, not the zero-field splitting. Vacancy aggregation extends NV- spin coherence rather than shortening it.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24428v1
- Title: Do gravitational waves assist the genuine tripartite entanglement harvesting?
- Authors: Xiang-Yue Yu, Xiao-Li Huang, Shu-Min Wu
- Categories: gr-qc (primary); gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24428v1  pdf=https://arxiv.org/pdf/2609.24428v1.pdf

Abstract:
We investigate the harvesting of genuine tripartite entanglement by three linearly arranged Unruh-DeWitt detectors locally coupled to a massless scalar field in a gravitational wave background. We show that gravitational waves play a dual role in entanglement harvesting, either enhancing or suppressing the harvested entanglement depending on the system parameters. In particular, genuine tripartite entanglement exhibits a pronounced nonmonotonic response to the gravitational wave frequency, characterized by successive suppression, enhancement resembling resonance, and renewed suppression, while approaching its corresponding value in Minkowski spacetime in the regime of high frequencies. Its dependence on the detector separation is also nonmonotonic, displaying local enhancement peaks that are absent in the corresponding bipartite entanglement behavior. Compared with bipartite entanglement, genuine tripartite entanglement therefore exhibits a higher sensitivity to gravitational wave perturbations in both the frequency and spatial domains. These results suggest that genuine tripartite entanglement may provide a sensitive quantum probe of spacetime perturbations induced by gravitational waves.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24459v1
- Title: On the dual character of Zn impurity in SnTe: Tuning thermoelectric and topological properties
- Authors: Kacper Pryga, Bartlomiej Wiendlocha
- Categories: cond-mat.mtrl-sci (primary); cond-mat.mtrl-sci; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24459v1  pdf=https://arxiv.org/pdf/2609.24459v1.pdf

Abstract:
We present a first-principles study of the electronic structure and thermoelectric properties of Zn-doped SnTe using the Korringa-Kohn-Rostoker method within the coherent potential approximation, complemented by pseudopotential calculations. SnTe is a lead-free analogue of PbTe and a candidate thermoelectric material in which Zn doping has been experimentally reported to enhance the performance of $p$-type samples. We show that Zn introduces a resonant-like impurity state, located within the conduction band, which evolves strongly depending on the Zn concentration. This feature leads to a significant enhancement of the thermopower in $n$-type SnTe. In the valence band, Zn doping induces L-$Σ$ band convergence, also resulting in an increased $p$-type Seebeck coefficient over a broad concentration range and delaying the onset of the bipolar effect. We further demonstrate that the Zn-induced band-structure modifications drive a transition from an inverted to a trivial band ordering, indicating a controllable topological phase transition. Our results clarify the microscopic role of Zn in SnTe and identify doping as a mechanism for simultaneously tuning thermoelectric and topological properties.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24572v1
- Title: The Superconducting Talbot Effect in Phased-Array Josephson Junctions
- Authors: Hechen Ren, Ziying Li
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.supr-con; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24572v1  pdf=https://arxiv.org/pdf/2609.24572v1.pdf

Abstract:
We introduce the superconducting Talbot effect---a macroscopic quantum self-imaging phenomenon occurring when proximitized Cooper pairs propagate through a ballistic two-dimensional electron gas. By configuring periodic superconducting leads into a phased-array Josephson junction with programmable phase differences, we demonstrate active steering of the resulting superconducting Talbot carpet. To overcome transport resolution limits, we design a Vernier-scale collector array that performs sub-wavelength sampling of the fractional Talbot pattern. This approach maps real-space quantum interference with high robustness to disorder, enabling direct extraction of Fermi wavelengths across helical, spin-degenerate, and spin-orbit-split Fermi surfaces. Tight-binding numerical calculations on a square lattice validate the real-space interference patterns. Our results establish a versatile framework for coherent wavefront engineering and quantum materials diagnostics in superconducting optics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24602v1
- Title: Random-matrix and transport frequencies in eigenstate spectral functions
- Authors: Kadir Çeven, Rohit Patil, Marcos Rigol, Fabian Heidrich-Meisner
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.dis-nn; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24602v1  pdf=https://arxiv.org/pdf/2609.24602v1.pdf

Abstract:
The fact that generic isolated many-body quantum systems thermalize is understood using the eigenstate thermalization hypothesis (ETH). In recent years, there has been much interest in the behavior of the ETH spectral functions, which characterize the smooth dependence of the variance of the off-diagonal matrix elements of observables on the associated energy and frequency, and whose low-frequency part contains information about the long-time dynamics. In finite systems described by the ETH, the spectral functions are expected to exhibit plateaus below a characteristic frequency $ω^{}_{\mathrm{ETH}}$. In this regime, the statistics of the matrix elements of observables are expected to be described by random matrix theory. Related frequencies that have been studied in the literature are $ω^{}_{\mathrm{SFF}}$, which controls the onset of random-matrix behavior in the spectral form factor, and the transport frequencies $ω^{}_{\mathrm{tr}}$, which are derived from transport coefficients. However, a direct quantitative comparison of these frequencies is lacking. Using exact diagonalization, we conduct such a comparison for the spectral functions of current operators in clean and disordered quantum spin ladders with diffusive energy and spin transport. We find clear evidence for the expected low-frequency plateaus in the ETH spectral functions. For the accessible system sizes, $ω^{}_{\mathrm{SFF}}$ is consistent with the extent of the plateaus, while the transport frequencies are systematically larger and lie in the nonuniversal regime of the spectral functions. Our findings highlight the need to better understand the origin of these quantitative differences.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24606v1
- Title: Benchmarking higher-ranking multipoles and polarizability tensors for small molecular systems
- Authors: Bruno V. von Bruening, Alston J. Misquitta
- Categories: physics.chem-ph (primary); physics.chem-ph; physics.comp-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24606v1  pdf=https://arxiv.org/pdf/2609.24606v1.pdf

Abstract:
Molecular properties govern how molecules interact with one another or external fields. Accurate molecular properties are essential for constructing intermolecular interaction models, and to achieve high accuracy we need to go beyond leading-order (dipolar) terms.   This work presents CCSD(T) references for 73 small non-spin-polarized molecules for molecular dipole and quadrupole moments, and dipole-dipole and quadrupole-quadrupole polarizabilities. Using these results, we provide a holistic performance analysis of molecular properties computed with HF, MP2, CCSD, and a wide range of density-functional methods. Additionally, we investigate in detail what levels of basis sets are required to simultaneously describe all properties in the data set.   The best-performing density functionals for all four properties are the asymptotically cor- rected hybrid GGAs B97-3-AC, closely followed by PBE0-AC. Surprisingly, modern meta- GGAs and range-separated functionals perform inconsistently, with large errors in the quadrupo- lar properties. These results have direct implications for methods for intermolecular interac- tions, such as symmetry-adapted perturbation theory based on density functional theory, or for the quality of properties and interactions in machine-learning datasets.   Finally, for DFT methods, the Jensen aug-pcseg-2 basis set is a computationally efficient alternative to more established basis sets, but for generating correlated references, third-row elements benefit from core polarization, and double augmentation is strictly necessary for quadrupole-quadrupole polarizabilities.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24709v1
- Title: Pendellösung length-scale neutron and X-ray interferometry
- Authors: Owen Lailey, Alexandre Boutot, David G. Cory, Joseph P. Cotter, Vishal Dhamgaye, Tao Hong, Michael G. Huber, Young-June Kim, et al.
- Categories: physics.app-ph (primary); physics.app-ph; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24709v1  pdf=https://arxiv.org/pdf/2609.24709v1.pdf

Abstract:
Neutron and X-ray perfect-crystal interferometers (PCIs) are powerful platforms for studies of fundamental physics and phase-contrast imaging. Further enhancing several PCI capabilities requires reducing crystal blade thickness to the micron scale, which minimizes dynamical-diffraction image blur, permits operation in the pendellösung regime where blade thickness controls beam splitting, and reduces absorption for simultaneous neutron and X-ray operation. However, fabricating multiple crystal blades with identical micrometer-scale thicknesses over centimeter-scale areas remains a major challenge. Here, using a non-etching sub-micron fabrication technique, we demonstrate silicon triple-Laue interferometers with equal-blade-thicknesses of 110 $μ$m and 350 $μ$m, operated with both neutrons and X-rays. These devices are the thinnest PCIs realized to date, enabling a factor-of-six reduction in dynamical-diffraction beam spreading for improved phase-contrast imaging, while reaching the single pendellösung length regime in which crystal thickness provides an experimentally accessible control parameter for engineered quantum-optical beam splitting of plane-wave inputs. These results motivate multi-blade PCI designs utilizing identical half-pendellösung crystal lamellae that are proposed for neutron spin--orbit and electric dipole moment measurements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24800v1
- Title: Collective cavity quantum electrodynamics in solid-state optical clocks
- Authors: Karen Mamian, Georgy A. Kazakov, Thorsten Schumm, Charles Roques-Carmes
- Categories: physics.optics (primary); physics.optics; nucl-th; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24800v1  pdf=https://arxiv.org/pdf/2609.24800v1.pdf

Abstract:
Solid-state frequency standards are generally limited by strong decoherence, rendering conventional interrogation schemes inefficient. The $^{229}$Th nuclear clock provides a unique and timely platform for solid-state optical metrology and nuclear cavity quantum electrodynamics (QED), featuring a coherence time many orders of magnitude shorter than the radiative lifetime in current experiments. Here, we propose and analyze three cavity QED-enhanced clock interrogation schemes that turn this timescale mismatch into an advantage, leveraging collective coupling of thorium nuclei to nanophotonic modes to enable fast interrogation and detection despite the long population lifetime. We reveal the central role of collective cooperativity in determining the clock frequency instability, and derive the optimal conditions (power, working-point detuning, thorium density) for clock operation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24873v1
- Title: Measuring correlations using local and nonlocal quenches
- Authors: Alexey G. Mikhaylenko, Andrew G. Semenov
- Categories: hep-th (primary); hep-th; cond-mat.stat-mech; hep-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24873v1  pdf=https://arxiv.org/pdf/2609.24873v1.pdf

Abstract:
We present a theoretical proposal for measuring correlation functions in a quantum field system based on the use of quantum quenches. Using the examples of massive and massless scalar field theories, we show that a short-term perturbation of the system leads to a dependence of the further evolution of the average field on the initial state's correlation functions. Considering two types of perturbations, namely local and nonlocal quenches, we show which correlation functions can be measured in each of these cases. The proposed procedure can be applied to study non-Gaussian correlations.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24874v1
- Title: Anomalously enhanced lifetimes of low angular momentum Rydberg states in singly charged alkaline-earth metal ions
- Authors: Simon Euchner, Weibin Li, Igor Lesanovsky
- Categories: physics.atom-ph (primary); physics.atom-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24874v1  pdf=https://arxiv.org/pdf/2609.24874v1.pdf

Abstract:
Trapped ions excited to high-lying electronic states, so-called Rydberg states, open new opportunities for quantum simulation and quantum computing. Generally, the fidelity of quantum coherent operations critically depends on the longevity of Rydberg states. However, scaling laws predict that the lifetimes of Rydberg states in singly charged alkaline-earth metal ions are 16 times shorter, compared to their neutral atom counterparts. Here, we show that this is not generally the case. We report an anomalous lifetime enhancement of certain low angular momentum ionic Rydberg series by factors larger than eight. The anomaly is present at both zero and finite temperature, although it is caused by different mechanisms. At zero temperature, the anomalously enhanced lifetimes are caused by accidental cancellations of the relevant dipole transition matrix elements, while at room temperature the anomaly originates from the enlarged energetic separation of ionic Rydberg levels with respect to neutral-atom levels.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24915v1
- Title: Fisher-information training of optical sensing front ends from natural fluctuations
- Authors: Abhinav Sinha, Kai Wang
- Categories: physics.optics (primary); physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24915v1  pdf=https://arxiv.org/pdf/2609.24915v1.pdf

Abstract:
Fisher-information-based optimization of programmable optical front ends in situ generally requires a response model or parameter-labeled measurements. We show that natural parameter fluctuations can instead provide the training signal. We construct proxies for the Fisher information (FI) of one parameter and the prior-weighted FI spectrum of multiple parameters from measured covariances after subtracting conditional detection noise, assuming locally affine responses. We use simulated photon counts from two incoherent point sources to train a mode sorter that approaches the quantum limit for separation and the Nagaoka--Hayashi single-copy bound for joint centroid--separation estimation. We demonstrate count-only updates that require no instrument response model and achieve performance comparable to model-based gradients. Our results provide a route to adaptive optical measurements without controlled parameter scans.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.24993v1
- Title: Quantum Mpemba effect from Stark localization
- Authors: Nico Albert, Masudul Haque, Shovan Dutta
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2609.24993v1  pdf=https://arxiv.org/pdf/2609.24993v1.pdf

Abstract:
In classical systems, rugged potential energy landscapes provide a transparent mechanism for the celebrated Mpemba effect, in which hotter initial states cool down faster. This picture generally does not survive in quantum systems. Here we show how to design a quantum energy landscape with local dissipation leading to an Mpemba effect with parametrically separated timescales. Our approach uses Stark localization to design an energy landscape and localized incoherent hopping as cooling mechanism. The hops are triggered by rare "detection" events whose rate grows with energy, allowing hotter states to cool faster and producing super-exponentially separated cooling rates for localized initial states. We further show that the effect is dramatically enhanced by collective hopping of bound pairs in the presence of attractive on-site interactions. These findings have clear experimental signatures accessible in present-day setups.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2203.06695v3
- Title: Relative State Quantum Logic
- Authors: Martin Paul Vaughan
- Categories: quant-ph (primary); quant-ph; physics.hist-ph
- Links: abs=https://arxiv.org/abs/2203.06695v3  pdf=https://arxiv.org/pdf/2203.06695v3.pdf

Abstract:
A projective quantum logic in terms of relative states is developed, emphasizing the importance of information transfer between a system under study and its environment. The need for accounting for the historical evolution of system is highlighted and it is found that the conjunction of observations involving conjugate variables can be consistently defined but is found to be non-commutative. It is shown that the Birkhoff and von Neumann approach to quantum logic is unable to deal with such conjunctions. It is found that whilst the proposed scheme is still not distributive in general, the discrepancy is directly related to interference effects that may disappear when information is transferred from the system to its environment. It is argued that the probabilities associated with projections be mapped to an orthocomplemented ternary logic, in which it is shown that the law of the excluded middle still holds.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2209.07867v3
- Title: Time symmetry in quantum theories and beyond
- Authors: John H. Selby, Maria E. Stasinou, Stefano Gogioso, Bob Coecke
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2209.07867v3  pdf=https://arxiv.org/pdf/2209.07867v3.pdf

Abstract:
There exists a stark tension among different formulations of quantum theory as some are inherently time-symmetric while others are time-asymmetric. This tension is crisply captured when considering physical theories as theories of processes. We present the process theory of quantum physics, QPhys, which treats classical systems as internal to quantum theory. We provide three ways to incorporate time symmetry in QPhys. The first restricts the process theory of QPhys to one that satisfies an additional retrocausality constraint. The second is a novel approach, which extends the notions of causality and retrocausality to apply to systems along with processes. Utilizing this approach, we create a toy model for particle physics , where the causal and retrocausal systems correspond to particles and anti-particles respectively. The third approach extends QPhys to a supertheory that satisfies neither a causality nor a retrocausality constraint. To avoid unphysical predictions we modify either its composition rule or its processes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2403.01854v2
- Title: Quantum counterdiabatic driving enhanced by two-stage local control
- Authors: Changhao Li, Jiayu Shen, Ruslan Shaydulin, Marco Pistoia
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; physics.app-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2403.01854v2  pdf=https://arxiv.org/pdf/2403.01854v2.pdf

Abstract:
Counterdiabatic driving can suppress diabatic losses during adiabatic ground state preparation. As its implementation necessitates the generation of an adiabatic gauge potential, which requires knowledge of the spectral gap of instantaneous Hamiltonians and involves highly non-local controls in many-body systems, local counterdiabatic driving with approximate adiabatic gauge potential has been widely adopted. In this work, using transverse-field Ising model as an example, we present an in-depth study of the performance of local counterdiabatic protocols and provide a closed-form analysis of ground-state-fidelity optimization. We then propose a two-stage protocol based on local counterdiabatic and simple local single-body control to further improve the performance. The practical implementation of these protocols does not require diagonalization of instantaneous Hamiltonians or spectral gaps, and only additional local single-body driving is involved. To benchmark their performance, we experimentally implement digitized adiabatic quantum evolution in a trapped-ion system. We characterize the quality of the prepared states and explore the scaling behavior with system size up to 14 qubits. Our demonstration of quantum shortcut to adiabaticity opens a path towards preparing ground states of complex systems with accessible local controls.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2409.16540v2
- Title: Quantum Authenticated Key Expansion with Key Recycling
- Authors: Wen Yu Kon, Jefferson Chu, Kevin Han Yong Loh, Obada Alia, Omar Amer, Marco Pistoia, Kaushik Chakraborty, Charles Lim
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2409.16540v2  pdf=https://arxiv.org/pdf/2409.16540v2.pdf

Abstract:
Data privacy and authentication are two main security requirements for remote access and cloud services. While QKD has been explored to address data privacy concerns, oftentimes its use is separate from the client authentication protocol despite implicitly providing authentication. Here, we present a quantum authentication key expansion (QAKE) protocol that (1) integrates both authentication and key expansion within a single protocol, and (2) provides key recycling property - allowing all authentication keys to be reused. We analyse the security of the protocol in a QAKE framework adapted from a classical authentication key exchange (AKE) framework, providing separate security conditions for authentication and data privacy. We experimentally implemented the protocol with appropriate post-selection. Additional results on the security of pseudorandom basis generation in QAKE and decoy state BB84 are provided.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2410.16231v3
- Title: A Quantum Optimization Algorithm for Optimal Electric Vehicle Charging Station Placement for Intercity Trips
- Authors: Tina Radvand, Alireza Talebpour, Homa Khosravian
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2410.16231v3  pdf=https://arxiv.org/pdf/2410.16231v3.pdf

Abstract:
Electric vehicles (EVs) play a significant role in enhancing the sustainability of transportation systems. However, their widespread adoption is hindered by inadequate public charging infrastructure for long-distance travel. Identifying optimal charging station locations in large transportation networks is an NP-hard combinatorial optimization problem. This paper applies Grover Adaptive Search (GAS) to improve the efficiency of solving the Charging Station Location Problem (CSLP). The proposed method achieves a quadratic improvement in computational complexity over classical exact methods, such as branch and bound. This paper develops a quantum subroutine that encodes the CSLP constraints by marking feasible solutions with objective value below a given threshold, and integrates this subroutine within the GAS procedure. The approach is demonstrated on a 7-node transportation network in central Illinois, with an analysis of success probability and sensitivity to algorithm parameters.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2411.04858v3
- Title: Reliable Entropy Estimation from Observed Statistics for Device-Independent Quantum Cryptography
- Authors: Gereon Koßmann, René Schwonnek
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2411.04858v3  pdf=https://arxiv.org/pdf/2411.04858v3.pdf

Abstract:
This paper introduces a numerical framework for establishing lower bounds on the conditional von-Neumann entropy in device-independent quantum cryptography and randomness extraction scenarios. Leveraging a hierarchy of semidefinite programs derived from the Navascués-Pironio-Acin (NPA) hierarchy, our tool enables efficient computation of entropy bounds based solely on observed statistics, assuming the validity of quantum mechanics. The method's computational efficiency is ensured by its reliance on projective operators within the non-commutative polynomial optimization problem. The method facilitates provable bounds for extractable randomness in noisy scenarios and aligns with modern entropy accumulation theorems. Consequently, the framework offers an adaptable tool for practical quantum cryptographic protocols, expanding secure communication possibilities in untrusted environments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2412.06548v3
- Title: Evidence for Exceptional Points as Topological Defects
- Authors: Chia-Yi Ju, Szu-Ming Chen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2412.06548v3  pdf=https://arxiv.org/pdf/2412.06548v3.pdf

Abstract:
Studies have shown that quantum states reside in a Hilbert space bundle. When a quantum system depends on continuous external parameters, these parameters define additional dimensions in the base space of the bundle. While much of the existing literature focuses on eigenstate subbundles, where geometric properties like Berry curvature arise, this work considers the entire Hilbert space bundle. Although the Hilbert space bundle has been found to be locally flat, suggesting that the system's topology may appear trivial, we revisit this assumption. Specifically, we examine how an arbitrary quantum state evolves when transported along closed parameter loops, a phenomenon characterized by holonomy. Our results demonstrate that nontrivial holonomy can emerge in the presence of exceptional points. Consequently, exceptional points naturally manifest as topological defects. Finally, we show that this nontrivial topology manifests in physical, time-dependent evolutions, providing a simple experimental signature to detect exceptional points by comparing state transport along distinct paths.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2412.17027v5
- Title: Entanglement as Difference: Reduction-induced Minimal Partial Entropy Difference
- Authors: Jing-Min Zhu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2412.17027v5  pdf=https://arxiv.org/pdf/2412.17027v5.pdf

Abstract:
Bipartite mixed-state quantum entanglement (QE) and its measures play a crucial role in both theoretical research and practical quantum applications. Its internal structure is far more complex and less well understood compared with bipartite pure-state QE. Some existing measures involve inherently intractable global optimizations, while others are only applicable to highly limited-dimensional quantum systems. Here based on the inherent feature that bipartite QE systems nonseparable necessarily implies that local reduced density matrix differs from its \textquotedblleft native\textquotedblright density matrix, we propose a more physical and intuitive measure termed Reduction-induced Minimal Partial Entropy Difference to quantify arbitrary bipartite mixed-state QE. Partial Von Neumann Entropy is only a pure-state special case of this method. This measure offers intrinsic structural %perspective insights into bipartite QE characterization, thereby establishing itself as a valuable complementary measure. Its intuitive and clear physical picture, combined with relatively low computational complexity and wide applicability, facilitates exploring its potential quantum information applications, hence its conceptual framework and line of thought deserve to be further developed to describe and quantify multipartite QE in the future.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2503.16977v3
- Title: Parallel splitting method for large-scale quadratic programs
- Authors: Matteo Vandelli, Francesco Ferrari, Daniele Dragoni
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2503.16977v3  pdf=https://arxiv.org/pdf/2503.16977v3.pdf

Abstract:
Current algorithms for large-scale industrial optimization problems typically face a trade-off: they either require exponential time to reach optimal solutions, or employ problem-specific heuristics. To address these limitations, we introduce SPLIT, a general-purpose quantum-inspired framework for decomposing large-scale quadratic programs into smaller subproblems, which are solved in parallel. SPLIT heuristically accounts for objective-function cross-interactions between subproblems, usually neglected in other decomposition techniques. The SPLIT framework can integrate generic subproblem solvers, from branch-and-bound to quantum optimization methods. We demonstrate its effectiveness through comparisons with commercial solvers and published results on MaxCut and Antenna Placement Problems, with up to 20,000 variables. Our results show that SPLIT is capable of providing drastic reductions in computational time, while delivering high-quality solutions. In these regards, the proposed method is well-suited for near real-time applications that require a solution within a strict time frame, or when the problem size exceeds hardware limitations of dedicated devices, such as current quantum computers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2506.08092v2
- Title: Kirkwood-Dirac Nonpositivity is a Necessary Resource for Quantum Computing
- Authors: Jonathan J. Thio, Songqinghao Yang, Nicole Yunger Halpern, Stephan De Bièvre, Crispin H. W. Barnes, David R. M. Arvidsson-Shukur
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.08092v2  pdf=https://arxiv.org/pdf/2506.08092v2.pdf

Abstract:
We elucidate the boundary between classical and quantum computation by constructing qubit Clifford circuits with nonstabilizer inputs that can be efficiently simulated classically. We do so by casting the quantum circuits realizable by defect braiding in the surface code in terms of a Kirkwood-Dirac (KD) quasiprobability distribution, a generalization of a joint probability distribution. If this distribution remains a proper (positive) probability distribution throughout a circuit, then a classical algorithm can simulate the circuit efficiently. By leveraging recent results on the geometry of KD-positive states, we construct bound-magic states. Classical computers can efficiently simulate these bound-magic states' evolutions under the circuits, although other magic states enable universal quantum computation when inputted. Furthermore, we show that KD nonpositivity is a resource monotone in this model. Thus, we establish KD nonpositivity as a necessary resource for quantum-computational advantages.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2507.07900v3
- Title: Methods for Reducing Ancilla-Overhead in Block Encodings
- Authors: Francisca Vasconcelos, András Gilyén
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.07900v3  pdf=https://arxiv.org/pdf/2507.07900v3.pdf

Abstract:
Block encodings are a fundamental primitive in quantum algorithms, but can often have large ancilla overhead. In this work, we introduce novel techniques for reducing this overhead in two distinct ways. In Part I, we prove the existence of a "space-time tradeoff" by deriving an algorithm that, for any block encoding, approximately uncomputes all but one of its ancilla (freeing up those ancillae for reuse in later parts of a quantum algorithm). In Part II, we evaluate the minimum number of ancillae required to perform coherent multiplication of block encodings and introduce a "space-accuracy tradeoff". Specfically, we prove that logarithmic ancillae is optimal for exact multiplication of block encodings, but show that (in certain block encoding regimes) approximate multiplication of block encodings can be achieved to high-precision with just one ancilla.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2508.04769v2
- Title: Power and Limitations of Linear Programming Decoder for Quantum LDPC Codes
- Authors: Shouzhen Gu, Mehdi Soleimanifar
- Categories: quant-ph (primary); quant-ph; cs.IT
- Links: abs=https://arxiv.org/abs/2508.04769v2  pdf=https://arxiv.org/pdf/2508.04769v2.pdf

Abstract:
Decoding quantum error-correcting codes is a key challenge in enabling fault-tolerant quantum computation. In the classical setting, linear programming (LP) decoders offer provable performance guarantees and can leverage fast practical optimization algorithms. Although LP decoders have been proposed for quantum codes, their performance and limitations remain relatively underexplored. In this work, we uncover a key limitation of LP decoding for quantum low-density parity-check (LDPC) codes: certain constant-weight error patterns lead to ambiguous fractional solutions that cannot be resolved through independent rounding. To address this issue, we incorporate a post-processing technique known as ordered statistics decoding (OSD), which significantly enhances LP decoding performance in practice. Our results show that LP decoding, when augmented with OSD, can outperform belief propagation with the same post-processing for intermediate code sizes of up to hundreds of qubits. These findings suggest that LP-based decoders, equipped with effective post-processing, offer a promising approach for decoding near-term quantum LDPC codes.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2509.01482v2
- Title: Enhanced measurements on quantum computers via the simultaneous probing of non-commuting Pauli operators
- Authors: Rick P. A. Simon, Zheng Shi, Charlie Nation, Andrew Jena, Luca Dellantonio
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.01482v2  pdf=https://arxiv.org/pdf/2509.01482v2.pdf

Abstract:
Measuring the state of quantum computers is a highly non-trivial task, with implications for virtually all quantum algorithms. A promising avenue is multi-copy schemes, where identical copies of a quantum state are measured jointly so that all Pauli operators within the considered observable can be simultaneously assessed. Here, we present a first implementation of such a two-copy scheme in a measurement protocol. Based on Bayesian statistics, it accurately estimates not only the average of the desired observable but also the error en route. This enables an adaptive shot-allocation algorithm that preferentially samples the most uncertain Pauli terms. In regimes with many non-commuting Pauli operators, this ``double'' scheme can outperform the state-of-the-art measurement protocol in minimizing total shots for a given precision. We also numerically confirm the finding in previous theoretical works that the two-copy scheme incurs an overhead due to the square-root relationship between the variance of measured quantities and the number of measurement shots.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2509.19501v2
- Title: Non-local mass superpositions and optical clock interferometry in atomic ensemble quantum networks
- Authors: Charles Fromonteil, Denis V. Vasilyev, Torsten V. Zache, Klemens Hammerer, Ana Maria Rey, Jun Ye, Hannes Pichler, Peter Zoller
- Categories: quant-ph (primary); quant-ph; gr-qc; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2509.19501v2  pdf=https://arxiv.org/pdf/2509.19501v2.pdf

Abstract:
Quantum networks are emerging as powerful platforms for sensing, communication, and fundamental tests of physics. We propose a programmable quantum sensing network based on entangled atomic ensembles, where optical clock qubits realize mass superpositions arising via mass-energy equivalence, as in atom and atom-clock interferometry. Our approach uniquely combines scalability to large atom numbers with minimal control requirements, relying only on collective addressing of internal atomic states. This enables the creation of both non-local and local superpositions with spatial separations beyond those achievable in conventional matter-wave interferometry with single atoms. Starting from Bell-type seed states distributed via photonic channels, collective operations within atomic ensembles coherently build many-body mass superpositions sensitive to gravitational redshift. The resulting architecture implements a non-local Ramsey interferometer, where gravitationally induced phase shifts are imprinted on non-local entangled states and are read out through local measurements at the network nodes. Beyond extending the spatial reach of mass superpositions, our scheme establishes a scalable, programmable platform to probe the interface of quantum mechanics and gravity, and offers a new experimental pathway to test atom and atom-clock interferometer proposals, e.g. for probing gravitational dephasing, in a network-based quantum laboratory.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2509.21131v3
- Title: Limits to black-box amplification in QMA
- Authors: Scott Aaronson, Phillip Harris, Freek Witteveen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.21131v3  pdf=https://arxiv.org/pdf/2509.21131v3.pdf

Abstract:
We study the limitations of black-box amplification in the quantum complexity class QMA. Amplification is known to boost any inverse-polynomial gap between completeness and soundness to exponentially small error, and a recent result (Jeffery and Witteveen, 2025) shows that completeness can in fact be amplified to be doubly exponentially close to 1. We prove that this is optimal for black-box procedures: we provide a quantum oracle relative to which no QMA verification procedure using polynomial resources can achieve completeness closer to 1 than doubly exponential, or a soundness which is super-exponentially small. This is proven by using techniques from complex approximation theory, to make the oracle separation from (Aaronson, 2008), between QMA and QMA with perfect completeness, quantitative.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2510.06346v2
- Title: Limitations of Noisy Geometrically Local Quantum Circuits
- Authors: Jon Nelson, Joel Rajakumar, Michael J. Gullans
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.06346v2  pdf=https://arxiv.org/pdf/2510.06346v2.pdf

Abstract:
Quantum circuits with a constant rate of depolarizing noise per qubit per time step are known to converge to the uniform distribution at depth $ω(p^{-1}\log n)$, and hence become trivially classically simulable by uniform sampling. We show that under the physically natural constraint of geometric locality, noisy circuits become classically simulable at shallower depths by substantially more structured classical algorithms. We consider arbitrary geometrically local quantum circuits on $n$ qubits, initialized in an arbitrary product state, with nearest-neighbor gates in $O(1)$ spatial dimensions and interspersed depolarizing noise of any constant strength $p$.   Our first result is that when the depth exceeds a threshold $d^*=Θ(p^{-1}\log n)$, the output distribution can be approximately sampled in quasipolynomial time. This gives a worst-case simulability result for noisy geometrically local circuits, and matches in its $n$-dependence the best previously known results for noisy random circuits. The proof is based on new information-theoretic bounds showing that in geometrically local noisy circuits, local regions lose correlations and independently converge to maximally mixed strictly before the entire system converges to the uniform distribution.   We further prove structural results suggesting a sharper transition at depth $\tildeΘ(p^{-1})$: after coarse-graining the lattice, Pauli weight supported on long connected paths can be truncated with exponentially small error. These results provide evidence for a percolation-like mechanism behind classical simulability at constant depth, and motivate our conjecture that all noisy geometrically local circuits admit quasipolynomial-time approximate sampling once circuit depth exceeds $\tildeΘ(p^{-1})$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2510.15030v2
- Title: Adiabatic transport of neural network quantum states
- Authors: Matija Medvidović, Alev Orfi, Juan Carrasquilla, Dries Sels
- Categories: quant-ph (primary); quant-ph; cond-mat.dis-nn
- Links: abs=https://arxiv.org/abs/2510.15030v2  pdf=https://arxiv.org/pdf/2510.15030v2.pdf

Abstract:
Variational methods have offered controllable and powerful tools for capturing many-body quantum physics for decades. The recent introduction of expressive neural network quantum states has enabled the accurate representation of a broad class of complex wavefunctions for many Hamiltonians of interest. We introduce a first-principles method for building neural network representations of many-body excited states by adiabatically continuing eigenstates of simple Hamiltonians into the strongly correlated regime. With controlled access to the full many-body gap, we obtain accurate estimates of critical exponents. Successive eigenstate estimates can be run entirely in parallel, enabling precise targeting of excited-state properties without reference to the rest of the spectrum, opening the door to large-scale numerical investigations of universal properties of entire phases of matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2511.05031v2
- Title: Frequency collisions in parametrically modulated superconducting circuits
- Authors: Zhuang Ma, Peng Zhao, Xinsheng Tan, Yang Yu
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.05031v2  pdf=https://arxiv.org/pdf/2511.05031v2.pdf

Abstract:
Superconducting circuits are a leading platform for scalable quantum computing, where parametric modulation is a widely used technique for implementing high-fidelity multi-qubit operations. A critical challenge, however, is that this modulation can induce a dense landscape of parasitic couplings, leading to detrimental frequency collisions that constrain processor performance. In this work, we develop a comprehensive numerical framework, grounded in Floquet theory, to systematically analyze and mitigate these collisions. Our approach integrates this numerical analysis with newly derived analytical models for both qubit-modulated and coupler-modulated schemes, allowing us to characterize the complete map of parasitic sideband interactions and their distinct error budgets. This analysis forms the basis of a constraint-based optimization methodology designed to identify parameter configurations that satisfy the derived physical constraints, thereby avoiding detrimental parasitic interactions. We illustrate the utility of this framework with applications to analog quantum simulation and gate design. Our work provides a predictive tool for co-engineering device parameters and control protocols, enabling the systematic suppression of crosstalk and paving the way for large-scale, high-performance quantum processors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2511.22771v2
- Title: Extensive search of Shannon entropy-based randomness certification protocols
- Authors: Robert Okuła, Piotr Mironowicz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.22771v2  pdf=https://arxiv.org/pdf/2511.22771v2.pdf

Abstract:
Quantum technologies offer significant advancements in information processing and communication, notably in the domain of random number generation (RNG). The use of Bell inequalities enables users to certify the randomness of outputs produced by untrusted quantum RNG devices. We present a method for quantitatively analyzing Bell expressions used to certify randomness in quantum systems. Using this method, we conducted a comprehensive analysis on more than half a million Bell expressions involving configurations with four measurement settings for one party and three for the other. We identified five notable examples based on entropy scores under varying levels of white noise. As an extension of these results, we further incorporate the concept of self-testing for boxes (Banacki et al 2022, New J. Phys. 24 083003), enabling a more comprehensive characterization of quantum correlations through the evaluation of $Boxes(α, B)$ and the corresponding measure $Flex(α, B)$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2511.23081v3
- Title: Algebraic power scaling in a slowly-quenched bosonic quantum battery
- Authors: Donny Dwiputra, Ahmad R. T. Nugraha, Sasfan A. Wella, Freddy Permana Zen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.23081v3  pdf=https://arxiv.org/pdf/2511.23081v3.pdf

Abstract:
Bosonic modes provide a promising platform for quantum batteries as a result of their unbounded energy spectrum. However, the energy that can be stored during a coherent charging process is limited due to coherent oscillations between the charger and battery. In this work, we show that by introducing a slow quench in the interaction between a coherently driven charger mode and a quadratic oscillator battery, the maximum stored energy and maximum battery power scale algebraically with the quench duration, with exponents controlled by the ramp profile. This finding implies that, quite counterintuitively, slower quenches lead to faster charging. Such a quench suppresses coherent energy oscillations between the battery and the charger, allowing an unbounded increase in power. We further show that, in the ideal closed protocol, the stored energy is fully extractable as ergotropy, while charger dissipation converts the algebraic enhancement into a finite-time scaling window with an optimal quench duration. We also show that the temporal-extensive scaling occurs in a broader context by mapping the system to a coherently driven Tavis-Cummings battery. Finally, we discuss experimentally accessible signatures in superconducting circuit quantum electrodynamics and organic microcavity platforms.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2512.05761v2
- Title: Exclusive Control of Quantum Memory Erasure
- Authors: Mir Alimuddin, Nathan Shettell, Raja Yehia, Antonio Acín, Federico Centrone
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.05761v2  pdf=https://arxiv.org/pdf/2512.05761v2.pdf

Abstract:
Erasing memory is a fundamental operational task in quantum information processing, governed by Landauer's principle, which links information loss to thermodynamic work. We introduce and analyze assisted quantum erasure, where correlations with a remote system reduce the energetic cost of resetting a memory. We identify exclusive control of erasure as the central operational requirement: only a designated party should be able to achieve the minimal cost, whereas any adversary must fail. In the device-dependent regime, we show that entanglement of formation exactly characterizes exclusivity, establishing entanglement as the decisive thermodynamic resource. Moving to a one-sided device-independent scenario, in which only the memory holder's device is trusted, we develop an operational erasure protocol based on random dephasing and conditional operations. Finally, in a fully device-independent setting, we show how Bell nonlocality and self-testing translate observed violations into lower bounds on any adversary's erasure capability, yielding a device-independent notion of exclusive thermodynamic control. Taken together, these results elevate quantum erasure from a thermodynamic constraint to an operational primitive: the erasure work cost quantifies secure, exclusive control over quantum memory, ensuring that an unauthorized agent cannot fully erase information under a bounded work budget.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2512.16752v2
- Title: QuantumSavory: symbolic modeling and multi-backend simulation of quantum computing and networking systems
- Authors: Hana Kimlee, Leonardo Bacciottini, Abhishek Bhatt, Andrew Kille, Stefan Krastanov
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.16752v2  pdf=https://arxiv.org/pdf/2512.16752v2.pdf

Abstract:
Progress in quantum computing and networking depends on codesign across abstraction layers: device-level noise and heterogeneous hardware, algorithmic structure, and distributed classical control. We present QuantumSavory, an open-source toolkit built to make such end-to-end studies practical by cleanly separating a symbolic computer-algebra frontend from interchangeable numerical simulation backends. States, operations, measurements, and protocol logic are expressed in a backend-agnostic symbolic language; the same model can be executed across multiple backends (e.g., stabilizer, wavefunction, phase-space), enabling rapid exploration of accuracy-performance tradeoffs without rewriting the model. Furthermore, new custom backends can be added via a small, well-defined interface that immediately reuses existing models and protocols. QuantumSavory also addresses the classical-quantum interaction inherent to LOCC protocols via discrete-event execution and a tag/query system for coordination. Tags attach structured classical metadata to quantum registers and message buffers, and queries retrieve, filter, or wait on matching metadata by wildcards or arbitrary predicates. This yields a data-driven control plane where protocol components coordinate by publishing and consuming semantic facts (e.g., resource availability, pairing relationships, protocol outcomes) rather than by maintaining rigid object graphs or bespoke message plumbing, improving composability and reuse as models grow. Our toolkit is also not limited to qubits and Bell pairs; rather, any networking dynamics of any quantum system under any type of multipartite entanglement can be tackled. Lastly, QuantumSavory ships reusable libraries of standard states, circuits, and protocol building blocks with consistent interfaces, enabling full-stack examples to be assembled, modified, and compared with minimal glue code.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2512.19665v2
- Title: QuSquare: Scalable Quality-Oriented Benchmark Suite for Pre-Fault-Tolerant Quantum Devices
- Authors: David Aguirre, Rubén Peña, Mikel Sanz
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.19665v2  pdf=https://arxiv.org/pdf/2512.19665v2.pdf

Abstract:
As quantum technologies continue to advance, the proliferation of hardware architectures with diverse capabilities and limitations has underscored the importance of benchmarking as a tool to compare performance across platforms. Achieving fair, scalable and consistent evaluations is a key open problem in quantum computing, particularly in the pre-fault-tolerant era. To address this challenge, we introduce QuSquare, a quality-oriented benchmark suite designed to provide a scalable, fair, reproducible, and well-defined framework for assessing the performance of quantum devices across hardware architectures. QuSquare consists of four benchmark tests that evaluate quantum hardware performance at both the system and application levels: Partial Clifford Randomized, Multipartite Entanglement, Transverse Field Ising Model (TFIM) Hamiltonian Simulation, and Data Re-Uploading Quantum Neural Network (QNN). Together, these benchmarks offer an integral, hardware-agnostic, and impartial methodology to quantify the quality and capabilities of current quantum computers, supporting fair cross-platform comparisons and fostering the development of future performance standards.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2512.20492v2
- Title: End-to-end Optimization of Single-Shot Quantum Machine Learning for Bayesian Inference
- Authors: Theodoros Ilias, Fangjun Hu, Marti Vives, Hakan E. Türeci
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.20492v2  pdf=https://arxiv.org/pdf/2512.20492v2.pdf

Abstract:
We introduce an end-to-end optimization strategy for quantum machine learning that directly targets performance under finite measurement resources, where learning objectives are defined directly at the level of task performance. The method is applied on a Bayesian quantum metrology task since it provides a natural testbed with known fundamental limits and scaling with system size. The sampling-aware hybrid algorithm achieves a single-shot risk within 1 dB of the -20 dB Bayesian limit using 32 qubits. We extend the Bayesian framework from parameter estimation to global function inference, where the task is to infer a target function of the sensor input drawn from an arbitrary prior, and we demonstrate a clear computational-sensing advantage for direct functional inference over indirect reconstruction. We relate the corresponding Bayesian risk to the Capacity metric and argue that the Resolvable Expressive Capacity provides a natural measure of the space of functions accessible in a single shot. The resulting eigentask analysis identifies noise-robust feature combinations that yield compact estimators with improved accuracy and reduced optimization cost in resource-limited or real-time on-device settings. Going beyond the irreducible statistical uncertainty associated with finite measurement records, we study implementation-induced distortions of the sensor response focusing on representative imperfections arising from readout errors and static coherent gate disorder. We show that when these imperfections are stationary across training and inference, end-to-end optimization can adapt the quantum circuit and classical estimator to the implemented hardware response, preserving high inference performance over a broad range of imperfection strengths.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2601.03616v3
- Title: Transmutation based Quantum Simulation for Non-unitary Dynamics
- Authors: Shi Jin, Chuwen Ma, Enrique Zuazua
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2601.03616v3  pdf=https://arxiv.org/pdf/2601.03616v3.pdf

Abstract:
We present a quantum algorithm for simulating dissipative diffusion dynamics generated by positive semidefinite operators of the form $A=L^\dagger L$, a structure that arises naturally in standard discretizations of elliptic operators. Our main tool is the Kannai transform, which represents the diffusion semigroup $e^{-AT}$, where $T$ is the final simulation time, as a Gaussian-weighted superposition of unitary wave propagators. For target accuracy $\varepsilon$, this representation leads to a linear-combination-of-unitaries implementation with a Gaussian tail and yields query complexity $\widetilde{O}(\sqrt{\|A\|\,T\,\log(1/\varepsilon)})$, up to the standard dependence on state-preparation and output-norm factors, improving the scaling in $\|A\|$, $T$, and $\varepsilon$ compared with generic Hamiltonian-simulation-based methods. We instantiate the method for the heat equation and biharmonic diffusion under non-periodic physical boundary conditions, and further use it as a subroutine for constant-coefficient linear parabolic surrogates arising in entropy-penalization schemes for the viscous Hamilton--Jacobi equations. In the long-time regime, under a spectral-gap assumption, the same framework gives a structured quantum linear solver by exploiting convergence to the steady state. For normalized positive definite systems $σ(A)\subset[1,κ]$, the solver outputs an $\varepsilon$-approximation to the state proportional to $\mathbf{x}=A^{-1}\mathbf{b}$ with query complexity $\widetilde{O}\left(\frac{\|\mathbf{b}\|}{\|\mathbf{x}\|}\sqrtκ\log^2\frac{\|\mathbf{b}\|}{\varepsilon\|\mathbf{x}\|}\right)$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2603.24444v2
- Title: Introducing a Kondo-type interaction to the model of quantum walkers
- Authors: Manami Yamagishi, Naomichi Hatano, Kohei Kawabata, Chusei Kiumi, Akinori Nishino, Franco Nori, Hideaki Obuse
- Categories: quant-ph (primary); quant-ph; cond-mat.other
- Links: abs=https://arxiv.org/abs/2603.24444v2  pdf=https://arxiv.org/pdf/2603.24444v2.pdf

Abstract:
We introduce a model of discrete-time quantum walkers interacting with a lozalized magnetic impurity. Each quantum walker interacts with an impurity, through which multiple quantum walkers indirectly interact with each other, as in the Kondo model. We first identify a quantum walker as a massless Dirac particle propagating in continuous space via a series of Dirac's delta potentials. Based on the identification, we add a spin-$1/2$ degree of freedom to Dirac's potential at the origin. We derive all scattering matrices for massless Dirac particles arising from the impurity. First, for a simple set of parameter values, we analytically obtain the eigenvalues and eigenvectors of the bound states, in which a quantum walker is bound to the magnetic impurity. Second, we study two quantum walkers indirectly interacting with each other via the magnetic impurity. We numerically simulate the collision dynamics in one dimension when the spin-spin interaction at the origin is of the XX type and the SU(2) Heisenberg type. In the case of the XX interaction, we calculate the entanglement negativity to quantify how much the two quantum walkers are entangled with each other, and find that the negativity increases drastically upon the collision of the two walkers. In the case of the SU(2) Heisenberg interaction, we simulate the dynamics starting from the initial state in which one fermionic walker is in a bound eigenstate around the origin and the other fermionic walker is a delta function colliding with the first walker. We find that a bound eigenstate closest to the singlet state of the first walker and the magnetic impurity is least perturbed by the collision of the second walker. We speculate that this finding may be related to Kondo screening-like behavior at the lowest level of the real-space renormalization-group procedure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2604.09892v2
- Title: Enhanced dissipative criticality at an exceptional point
- Authors: Jongjun M. Lee
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2604.09892v2  pdf=https://arxiv.org/pdf/2604.09892v2.pdf

Abstract:
Exceptional points (EPs) represent non-Hermitian degeneracies where eigenvalues and eigenvectors coalesce, giving rise to enhanced sensitivity and critically damped dynamics. We demonstrate that when an EP coincides with a dissipative phase transition in an extended open Dicke model of two cavities coupled to a collective spin, the critical fluctuations are strongly amplified and governed by modified critical exponents. Numerical results reveal enhanced critical scaling in both the normal and superradiant phases, in agreement with an analytical theory based on the Jordan-block structure of the linearized dynamical matrix at the EP. Our results establish EPs as a mechanism to engineer critical scaling in open quantum systems, with potential applications to critical quantum sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2604.22232v2
- Title: A Simulation Framework for Noise and Error-Correction Analysis in Device-Independent Quantum Key Distribution
- Authors: Nguyen Duong Hoang Duy, Nguyen Trinh Dong, Vu Tuan Hai, Le Vu Trung Duong, Nguyen Van Tinh
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2604.22232v2  pdf=https://arxiv.org/pdf/2604.22232v2.pdf

Abstract:
Device-Independent Quantum Key Distribution (DIQKD) certifies security from the violation of a Bell inequality alone, but its practical margin against noise is narrow and is usually quoted only through the Bell violation itself. We build a simulator of the event-ready DIQKD experiment and use it to trace readout noise through the Bell test into classical post-processing. For a symmetric outcome-flip channel of strength $e$, we reproduce the simulated violation window e<5.86%, to within $0.11$ percentage points. Combining these with a multi-pass Cascade reconciliation and the Devetak-Winter bound gives r<=0.162 bits per round, and shows that a positive key rate requires e<0.89 - roughly one-sixth of the window in which a Bell violation is still observed. The gap quantifies how far certified nonlocality overstates the usable noise budget of a DIQKD link.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2604.25333v2
- Title: Sign Embedding Quantum Algorithms for Matrix Equations and Matrix Functions
- Authors: Yanqiao Wang, Jin-Peng Liu
- Categories: quant-ph (primary); quant-ph; math.NA
- Links: abs=https://arxiv.org/abs/2604.25333v2  pdf=https://arxiv.org/pdf/2604.25333v2.pdf

Abstract:
We develop operator-output quantum algorithms for matrix equations and matrix functions using matrix-sign embeddings. For each problem, an augmented matrix $M$ is chosen so that the target operator is a block of $\text{sign}(M)$ or is recovered from blocks of $(I-\text{sign}(M))/2$. We approximate the half-plane sign by a logarithmic-sinc formula and implement the shifted inverse families by scaled multiplexing with node-dependent rebalancing. For ordinary Sylvester equations, this yields a block-encoding of the solution with query complexity linear in the relevant conditioning parameters and logarithmic in the inverse error tolerance, under either a field-of-values (FoV) gap or a strip-resolvent bound. The same method extends to generalized Sylvester and Lyapunov equations, principal square and inverse square roots, matrix geometric means, and continuous-time algebraic Riccati equations (CARE), with explicit query-complexity and block-encoding-normalization bounds that cover non-normal and non-diagonalizable cases.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2605.00954v4
- Title: Symmetry-Engineered Multiple Bulk-Boundary Correspondences and Anomalous Modes in a Non-Hermitian Creutz Ladder
- Authors: Xin Li, TongYi Li, JingYu Peng, Yu Wang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.00954v4  pdf=https://arxiv.org/pdf/2605.00954v4.pdf

Abstract:
The synergy between non-Hermiticity and topology makes the bulk-boundary correspondence (BBC) highly elusive. Here we study a non-Hermitian Creutz ladder incorporating both gain-loss and nonreciprocity, and construct multiple BBCs involving scale-free, normal, and anomalous skin modes, as well as topological zero- energy modes. We characterize the skin effect induced by the parity-time (PT) phase transition through an average winding number, thereby formulating a PT-related BBC. Furthermore, a hidden chiral symmetry ensures that topological phase transitions can be reliably detected via a Z 2 invariant. Although the gain-loss breaks the standalone P symmetry, it preserves the combined PT symmetry, allowing a modified Z 2 invariant to sustain the topological BBC. Notably, sublattice symmetry facilitates the precise analytical determination of non-Bloch spectra. Leveraging this, we introduce a hybrid spectral winding that encodes the localization (or delocalization) characteristics of two counterintuitive bulk modes coexisting with normal skin modes, thus defining a non-Hermitian BBC. One of these modes exhibits exponential boundary accumulation in a direction opposite to the nonreciprocity, while the other manifests as an anomalous surge of Bloch-wave states within the nonreciprocal lattice. These results reveal a series of unexpected phenomena governed by underlying symmetry, significantly broadening our fundamental understanding of the BBC mechanism in non-Hermitian topological systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2605.26377v2
- Title: Single-Ensemble Multiparameter Squeezing with Qudits
- Authors: Xiaoshui Lin, Chunlei Qu, Chong Zu, Chuanwei Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2605.26377v2  pdf=https://arxiv.org/pdf/2605.26377v2.pdf

Abstract:
Conventional spin squeezing enhances a single sensing channel. Here, we show how internal qudit levels enable simultaneous multiparameter squeezing within one ensemble. In two-component magnetometry, a qutrit sensor provides two orthogonal and weakly compatible channels. A collective twisting interaction squeezes both responses while preserving joint attainability of the ultimate sensitivity. The sensing gain is quantified by using a matrix generalization of the Wineland sensitivity that retains both noise correlations and cross-channel response. An interaction-based echo amplifies the signal to overcome noise from a fixed local joint readout, yielding a simulated $13~\mathrm{dB}$ gain over the product-state standard quantum limit for $N=128$ qutrits. More generally, we use the single-site quantum Fisher information matrix to select reference states and channel quadratures for prescribed sensing tasks. The tangent geometry permits at most $d-1$ independent, weakly compatible channels around a common pure reference state for a $d$-level sensor. Our work provides a constructive task-to-protocol map for multiparameter squeezing in a single qudit ensemble.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2606.22212v2
- Title: Probing the Weak-Driving Quantum Speed Limit via Drift-Aware Shooting Methods
- Authors: Denis Janković, Saba Taherpour, Paul-Louis Etienney, Paul-Antoine Hervieux, Christoph Wolf
- Categories: quant-ph (primary); quant-ph; math-ph; physics.comp-ph
- Links: abs=https://arxiv.org/abs/2606.22212v2  pdf=https://arxiv.org/pdf/2606.22212v2.pdf

Abstract:
A central goal of quantum optimal control is to achieve high-fidelity and low-energy control pulses. When quantum optimal control methods optimize every point of a pulse discretized over small time steps independently this can yield high fidelity control but also results in broadband and energy-hungry waveforms. We extend MAGICARP, a shooting method inspired by Pontryagin's maximum principle on energy that generates an entire pulse from a small set of parameters, making it smooth and energy-efficient by construction, from driftless systems to closed systems with the constant drift Hamiltonian of two exchange-coupled spins in an external magnetic field. The optimization proceeds in stages: the dressed states of the drift Hamiltonian structure the target, an initial shooting optimization is performed in the rotating-wave frame, and an exact laboratory-frame refinement follows. Benchmarked against Krotov and GRAPE at matched gate infidelity, MAGICARP consistently achieves the lowest energy and a conserved pulse area, concentrates its spectral weight on the gate-relevant transitions, and is the most robust to fluctuations in the exchange coupling; GRAPE independently converges to essentially the same pulse while black-box Krotov meets the same error at an order-of-magnitude energy premium. This method-independence is what qualifies the bounded solver as a measurement instrument, and the central result follows: a large statistical survey of unselected optimization runs resolves a weak-driving quantum speed limit for two exchange-coupled electron spins: low-amplitude realizations of the two-qubit quantum Fourier transform cease to exist below a critical gate time, and the minimum control energy diverges on approach to this limit. The divergence obeys a simple two-parameter area--pole law, $E_2^{\mathrm{law}}(T)=A/T+B/(T-T^*)$.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2608.19459v2
- Title: Is the Quantum-Entangled Universe a Small World?
- Authors: Gregory S. Duane
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2608.19459v2  pdf=https://arxiv.org/pdf/2608.19459v2.pdf

Abstract:
Partial entanglement may provide enough connections in the universe to satisfy the definition of a small world. To investigate this possibility, we define a network of particles on a given space-like hyper-surface with a long-range link between any two particles that are connected by a chain of exchanged particles involving a limited number of interactions. Considering the mean free paths of particles in different regions of space and the resulting probability distributions of entanglement connections vs. distance, we find evidence of small-world or random network structure on all but the smallest scales - corresponding to stars and planets - on which other types of connections would need to be added to complete the small world picture.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2608.23113v2
- Title: Dark-Mode Control of Contrasting Entanglement and Bell Nonlocality between Mechanical Oscillators
- Authors: Souvik Agasti, Philippe Djorwe, Xin Zhou
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.23113v2  pdf=https://arxiv.org/pdf/2608.23113v2.pdf

Abstract:
This study presents a detailed proposal for an optomechanical system consisting of two mechanical oscillators coupled to a common cavity, aimed at generating pure and entangled two-mode squeezed mechanical steady states. We found that the violation of Bell's measurement may not occur where the entanglement is maximum; rather, nonlocality can be observed for lower entangled states. A central result is that optomechanical coupling imperfections can enhance mechanical entanglement while simultaneously suppressing Bell nonlocality by reducing the purity of the mechanical state. To mitigate this trade-off, we introduce phase-dependent phonon hopping between the mechanical oscillators and show that Bell nonlocality can be selectively enhanced in specific dark-mode configurations, even when the overall entanglement is reduced. We trace this contrasting behaviorto changes in state purity associated with the imbalance of the Bogoliubov-mode occupations. Compatible with existing microwave cavity optomechanical platforms, the proposed architecture provides an experimentally accessible route for controlling nonlocal quantum correlations in multimode mechanical systems. Our proposed scheme serves as an attractive platform for the deployment of continuous-variable teleportation and high-fidelity quantum communication.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2608.23819v2
- Title: CircLS: Compiling Lattice Surgery to Physical Circuits with Dynamic Allocation
- Authors: John Yuehan Zhang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2608.23819v2  pdf=https://arxiv.org/pdf/2608.23819v2.pdf

Abstract:
In fault-tolerant quantum computing, lattice surgery (LS) is one of the leading ways to realize logical operations, and the Pauli product measurement (PPM) is the basic instruction of LS-based computing. Compilers that work on the PPM sequence, however, stay at the logical level rather than the physical circuit level. This is because lowering PPMs from the logical level to physical circuits is complicated. CircLS is a full-stack lattice surgery compiler: it compiles a quantum program through its PPM sequence to a Stim circuit, lowering every PPM through linear-time stabilizer construction rules. On this basis, we develop a compiler that allocates data patches dynamically: each patch is allocated at its first use and freed at its last use, and the freed tiles can be reused as ancilla paths. Against the two baselines, CircLS reduces the allocated spacetime volume by 34% and 27% and the logical error rate (LER) by 40% and 48%, and it compiles programs that they cannot. CircLS is open source at https://github.com/John-YuehanZhang/CircLS

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.06688v2
- Title: Error Exponents of Probabilistic Quantum Resource Distillation
- Authors: Xian Shi
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.06688v2  pdf=https://arxiv.org/pdf/2609.06688v2.pdf

Abstract:
In this manuscript, we establish a unified framework for analyzing the conditional error exponents of probabilistic resource distillation under approximately resource-nongenerating instruments. For generic quantum resource theories satisfying suitable structural conditions, we derive general oneshot bounds on the conditional distillation error exponents. By relating probabilistic distillation to postselected composite quantum hypothesis testing, we obtain bounds of the conditional error exponents for coherence distillation under finite blocklength and asymptotic zero-rate scenarios, we furthermore obtain analytical characterizations of the conditional error exponents for entanglement and magic distillation under finite blocklength and asymptotic zero-rate scenarios. For several representative families of states in entanglement and magic resource theories, these characterizations reduce to explicit closed-form formulas. Comparing them with the corresponding deterministic distillation exponents, we identify regimes in which postselection yields a strict improvement in the exponential decay rate of the conditional error. Our results reveal an operational advantage of postselection in quantum resource distillation and establish postselected composite hypothesis testing as a general tool for characterizing probabilistic resource-processing tasks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.06802v2
- Title: Spectral Twisting in a Common Bosonic Reservoir: Fragility of Two-Qubit Dark-State Protection
- Authors: Fabio Borrelli, Giovanni Miano, Carlo Forestiere
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.06802v2  pdf=https://arxiv.org/pdf/2609.06802v2.pdf

Abstract:
The interaction of two qubits with a common bosonic reservoir is encoded by a matrix-valued spectral density $\mathbf{J}(ω)$, whose diagonal entries describe the local spectra, while the off-diagonal entries encode cross-correlations. Even when \(\mathbf{J}(ω)\) has rank one, a frequency-independent dark channel need not exist because the family \(\{\mathbf{J}(ω)\}_ω\) may have a trivial common kernel. We term the frequency-dependent rotation of the bright and dark directions \textit{spectral twisting} and quantify it through the Fubini--Study speed $τ(ω)$ of the bright spectral projector. We analyze how twisting modifies two-qubit dynamics and quantify the loss of dark-state protection through the leakage \(P_{\mathrm{leak}}(t)\). Comparisons with untwisted asymmetric reservoirs and rotating-wave dynamics, together with detuned and finite-temperature calculations, distinguish spectral twisting from coupling asymmetry, counter-rotating processes, and thermal absorption. For resonant qubits tuned to the crossing of the two local spectra $ω_\times$, the singlet is locally dark at the transition frequency but couples to off-resonant components whose bright directions are rotated. In the weak-twisting regime, the fixed-time leakage scales as $P_{\mathrm{leak}}(t)\propto[ω_\timesτ(ω_\times)]^2$. We test this prediction for mismatched Drude-Lorentz spectra using nonperturbative hierarchical equations of motion generalized to cross-correlated bath forces. These results provide a geometric framework for dark-state engineering in structured reservoirs.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.13839v2
- Title: What Output-Equivalence Oracles Miss: An Empirical Study of Equivalence-Invisible Bug Fixes in Quantum Transpilers
- Authors: Furqan Nasir, Arif Shah, Iftikhar Alam
- Categories: quant-ph (primary); quant-ph; cs.SE
- Links: abs=https://arxiv.org/abs/2609.13839v2  pdf=https://arxiv.org/pdf/2609.13839v2.pdf

Abstract:
Quantum compilers are judged correct by an output-equivalence oracle: the compiled circuit must compute the same unitary as the original, modulo global phase and a qubit-layout permutation. This oracle, by construction, checks only that semantic map, not the circuit's own layout, permutation, or phase records: a defect there, or in a fixed-seed run's determinism, can pass unseen though the record is public. We measure how often this happens in real merged compiler fixes: a systematically identified corpus of Qiskit transpiler bug-fixes, classified by an independently dual-coded, source-validated manifestation taxonomy. Nineteen of 68 fixes (28%, 95% Wilson CI 19-40%) repair faults that this equivalence screen does not catch, even one augmented with compilation-validity, circuit-quality, and performance checks, and an extended 104-fix corpus over a wider window holds at the same rate with a tighter interval (29/104, 27.9%, CI 20-37%). A conservative floor remains even restricted to the one unconditionally equivalence-invisible channel (a corrupted layout or permutation record): 10 of 68 fixes (15%, CI 8-25%) beneath the 28% headline. The gap is not Qiskit-specific: it replicates in tket (7 of 21, 33%), with Cirq smaller but consistent. We detected no systematic differences on five inexpensive PR-level characteristics (19 vs 49, underpowered on its own; the same comparison on the extended 29-vs-75 corpus tightens every interval toward zero). This class dominates the invisible set, concentrating at representation-boundary crossings. We release the corpus, codebook, and coding artifacts. Here we only measure it.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.14937v2
- Title: Entanglement free Metrology Exploiting Multimode Hong Ou Mandel Sensor Advantage
- Authors: Qian Li, Jianning Han
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2609.14937v2  pdf=https://arxiv.org/pdf/2609.14937v2.pdf

Abstract:
The Hong-Ou-Mandel (HOM) interference in the multimode frequency domain has been explored for precision metrology, with several experimental demonstrations exploiting its robustness against dispersion and phase noise, as well as its large dynamic range and compatibility with fragile samples. Conventional multimode HOM metrology exploits frequency-entangled states, which naturally satisfy bosonic exchange symmetry under any centered symmetric joint spectral distribution, to provide these advantages. However, these entangled states are typically generated via spontaneous parametric down-conversion (SPDC), requiring strong pump lasers that hinder practical implementation. In this paper, we employ frequency product states, which do not possess entanglement or path-mode exchange symmetry, as the probe state and post-select measurement outcomes exhibiting frequency anti-correlation. Our results demonstrate that these advantages,peak narrowing, dispersion cancellation, phase-noise immunity, a large dynamic range, and compatibility with fragile samples, arise neither from entanglement nor from bosonic exchange symmetry, but rather from spectral anti-correlation. We further show that entanglement is not the source of the measurement precision: the entanglement-free approach attains the same quantum Fisher information as the entangled-state scheme, indicating that the fundamental precision limit does not originate from entanglement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2502.14026v2
- Title: Orbital Wigner functions and quantum transport in multiband systems
- Authors: Johannes Mitscherling, Dan S. Borgnia, SuryaNeil Ahuja, Joel E. Moore, Vir B. Bulchandani
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.mes-hall; cond-mat.mtrl-sci; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2502.14026v2  pdf=https://arxiv.org/pdf/2502.14026v2.pdf

Abstract:
Traditional theories of electron transport in crystals are based on the Boltzmann equation and do not capture physics arising from quantum coherence. We introduce a transport formalism based on orbital Wigner functions, which accurately captures quantum coherent physics in multiband fermionic systems. We illustrate the power of this approach compared with traditional semiclassical transport theory by testing it numerically against microscopic simulations of one-dimensional, noninteracting, two-band systems---the simplest systems capable of exhibiting interorbital coherence. We show that orbital Wigner functions accurately capture strongly nonequilibrium features of electron dynamics that lie beyond conventional Boltzmann theory, such as the ballistic transport of a relative phase between microscopic orbitals and topological Thouless pumping of charge, both at nonzero temperature and away from the adiabatic limit. Our approach is motivated in part by modern ultracold atom experiments that can prepare and measure far-from-equilibrium charge transport and phase coherence in multiband fermionic systems, calling for correspondingly precise theories of transport. The quantitative accuracy exhibited by our approach, together with its capacity to capture nontrivial physics even at the ballistic scale, establishes orbital Wigner functions as an ideal starting point for developing a fully systematic theory of transport in crystals.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2506.19969v3
- Title: Holography for bulk-boundary local topological order
- Authors: Corey Jones, Pieter Naaijkens, David Penneys
- Categories: math-ph (primary); math-ph; cond-mat.str-el; math.OA; math.QA; quant-ph
- Links: abs=https://arxiv.org/abs/2506.19969v3  pdf=https://arxiv.org/pdf/2506.19969v3.pdf

Abstract:
In our previous article [arXiv:2307.12552], we introduced local topological order (LTO) axioms for quantum spin systems which allowed us to define a physical boundary (associated to a cut of the lattice) manifested by a net of boundary algebras in one dimension lower. This gives a formal setting for topological holography, where the braided tensor category of DHR bimodules of the physical boundary algebra captures the bulk topological order.   In this article, we extend the LTO axioms to quantum spin systems equipped with a topological boundary (domain wall with the trivial phase), again producing a physical boundary algebra for the bulk-boundary system, whose category of (topological) boundary DHR bimodules recovers the topological boundary order. We perform this analysis in explicit detail for Levin-Wen and Walker-Wang bulk-boundary systems.   Along the way, we introduce a 2D braided categorical net of algebras built from a unitary braided fusion category (UBFC). Such nets arise as boundary algebras of Walker-Wang models. We consider the canonical state on this braided categorical net corresponding to the standard topological boundary for the Walker-Wang model. Interestingly, in this state, the cone von Neumann algebras are type I with finite dimensional centers, in contrast with the type II and III cone von Neumann algebras from the Levin-Wen models studied in [arXiv:2307.12552]. The superselection sectors recover the underlying unitary category of our UBFC, and it was recently proven in [arXiv:2609.20725] that the superselection category also captures the fusion and braiding.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2508.13780v2
- Title: Many-body theory of false vacuum decay in quantum spin chains
- Authors: Christian Johansen, Alessio Recati, Iacopo Carusotto, Alberto Biella
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; cond-mat.str-el; hep-lat; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2508.13780v2  pdf=https://arxiv.org/pdf/2508.13780v2.pdf

Abstract:
In this work we theoretically investigate the false vacuum decay process in a ferromagnetic quantum spin-1/2 chain. We develop a many-body theory describing the nucleation and the coherent dynamics of true-vacuum bubbles that is analytically tractable and agrees with numerical matrix product state calculations in all parameter regimes up to intermediate times. This theory allows us to identify different regimes in the parameter space and unravel the underlying physical mechanisms, thus offering new conceptual insight on the microscopic quantum dynamics of metastable states. In particular, analogies and differences with the cosmological false vacuum decay picture are highlighted and characterized in terms of experimentally observable quantities.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2509.00695v2
- Title: Parametrically Driven Superradiance of an Interacting Tavis-Cummings Model
- Authors: Wen-Jie Geng, Yiwen Han, Wei Yi
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2509.00695v2  pdf=https://arxiv.org/pdf/2509.00695v2.pdf

Abstract:
We consider the superradiant transition of a generalized Tavis-Cummings model, where a number of two-level qubits are coupled to a dissipative cavity. The cavity is coherently driven through a parametric medium, and all-to-all interactions between the qubits are introduced. While the nonlinear gain from the parametric drive breaks the U(1) symmetry of the standard Tavis-Cummings model, thus giving rise to superradiance with squeezed cavity fields, we show that the interactions impact the collective excitations and significantly modify the superradiant transition. Insights to the superradiant phase transitions, as well as the interaction effects, are obtained through effective models involving only a handful of low-lying collective states, under which the steady-state phase diagram of the hybrid system is faithfully reproduced. Our study is relevant to Rydberg-atom arrays coupled to a parametrically driven cavity, where the long-range interactions derive from the dipole-dipole interatomic interactions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2511.16363v3
- Title: On the resolution of categorical symmetries in (Non-) Unitary Rational CFTs
- Authors: Arpan Bhattacharyya, Saptaswa Ghosh, Sounak Pal, Jagannath Santara
- Categories: hep-th (primary); hep-th; cond-mat.str-el; math-ph; math.QA; quant-ph
- Links: abs=https://arxiv.org/abs/2511.16363v3  pdf=https://arxiv.org/pdf/2511.16363v3.pdf

Abstract:
We explore several aspects of categorical symmetry-resolved entanglement entropy (SREE) directly within two-dimensional rational conformal field theory (RCFT) (without invoking any SymTFT construction arXiv:2409.02806). We derive a general formula applicable whenever the action of the relevant topological defect lines on the annulus Hilbert space is known. This framework accommodates weakly and strongly symmetric boundaries, cloaking states, and fusion rings with multiplicities. We verify the formula in a range of diagonal unitary and non-unitary examples, including theories with generalized Haagerup-Izumi modular data. Furthermore, we extend the analysis to non-diagonal RCFTs. The $\frac{1}{2}E_6$ example demonstrates that closed-channel modular data and NIM-rep multiplicities alone do not suffice to determine the defect action on the complete open-channel Hilbert space.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2512.01120v3
- Title: Variational quantum algorithm for anion exchange across electrolyzer membrane
- Authors: Timur Gubaev, Philipp Pfeffer, Christian Dreßler, Jörg Schumacher
- Categories: physics.flu-dyn (primary); physics.flu-dyn; quant-ph
- Links: abs=https://arxiv.org/abs/2512.01120v3  pdf=https://arxiv.org/pdf/2512.01120v3.pdf

Abstract:
We present a variational quantum algorithm that solves the one-dimensional diffusion problem with a space-dependent diffusion constant $D(x)$. This problem is relevant for the exchange of hydroxide ions across a two-layer membrane in an alkaline electrolyzer, where the concentration of OH$^-$ ion determines the chemical stability for longer time periods. We use $16$ to $64$ grid points across the membrane, resulting from $n=4$ to $6$ data qubits for the ideal statevector and shot-based quantum simulations implemented using Qiskit. For these qubit numbers, the depth of the parametric quantum circuit has been chosen to ensure sufficient expressibility. The state preparation requires particular attention since the diffusivity $D$ is piecewise constant in the different layers with discontinuities at the interface. Furthermore, we compare different classical optimization schemes with respect to their convergence in the VQA method. We demonstrate the applicability of the quantum algorithm to a problem with non-trivial boundary conditions and jump conditions of the diffusion constant and outline possible extensions of the proof-of-concept application case of quantum computing. Our simulations show that pronounced hydroxide ion concentration gradients, and thus chemical instabilities, can occur only when the ratio of diffusivity in both layers of the membrane exceeds approximately 50.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2512.03368v2
- Title: Short-Range Modulated Electron Lattice and d-Wave Superconductivity in Cuprates: A Phenomenological Ginzburg-Landau Framework
- Authors: Jaehwahn Kim, Davis A. Rens, Waqas Khalid, Hyunchul Kim
- Categories: cond-mat.supr-con (primary); cond-mat.supr-con; cond-mat.mtrl-sci; cond-mat.str-el; physics.app-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2512.03368v2  pdf=https://arxiv.org/pdf/2512.03368v2.pdf

Abstract:
A short-range charge modulation near 0.3 reciprocal lattice units along the Cu-O bond is present in every hole-doped cuprate family. Resonant x-ray scattering now shows that superconductivity does two opposite things to it at once: below Tc the modulation weakens yet becomes more phase coherent. We trace this split to symmetry: the modulation's envelope carries lattice momentum, which leaves a d-wave condensate exactly two ways to couple to it at quartic order, through the modulation's amplitude or through its phase. The first moves amplitude, coherence, and superfluid stiffness together; the second buys coherence at the expense of stiffness, so the two are separately measurable. We call this Ginzburg-Landau framework the modulated electron lattice (MEL).   Classical Monte Carlo on 120x120 lattices with quenched disorder places the x-ray observation, read as a single component, at competing amplitude coupling and cooperative phase coupling, where the model gives no stiffness gain. But the measured intensity sums bond-centred and site-centred components. A two-component simulation gives the same pair of bulk signatures, intensity down and coherence up, both with a stiffness loss and with a stiffness gain, depending on the strength of the bond channel. Bulk data therefore cannot say whether this charge order stiffens the superconductor or softens it. What settles the question is the bond-channel amplitude, which form-factor-resolved scattering and phase-resolved tunnelling measure.   The response follows the local pairing amplitude, so its onset need not be sharp at Tc. We also compute vortex pinning in the modulated landscape and obtain an in-plane penetration depth of about 124 nm once the transition temperature fixes the energy scale.   This version corrects the first: its linear envelope coupling was symmetry-forbidden, and all numerical results are new.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2512.13901v2
- Title: Quantum fields in a cold atomic simulator: relaxation and phase locking in tunnel-coupled 1D bosonic quasi-condensates
- Authors: B. Fitos, G. Takács
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2512.13901v2  pdf=https://arxiv.org/pdf/2512.13901v2.pdf

Abstract:
We consider a prime example of simulating interacting relativistic QFT with cold atoms: the realisation of the sine-Gordon model by tunnel-coupled quasi-1D Bose gases. While experiments have shown that it can realise the sine-Gordon model in equilibrium, studies of non-equilibrium dynamics have revealed phase-locking behaviour that contrasts with predictions from sine-Gordon field theory. Here, we examine a one-dimensional field-theoretic model of the system and find that the phase-locking behaviour can be understood in terms of the longitudinal harmonic trap, and that the additional degrees of freedom observed in the experiment do not appear to play a significant role. Therefore, the experimental setup provides a good simulator of the sine-Gordon quantum field theory, even out of equilibrium, if the inhomogeneous background induced by the trap is taken into account. Furthermore, our results support the idea that modifying the longitudinal trap to a box shape should result in agreement with standard sine-Gordon dynamics. The main remaining open issues are accounting for 3D corrections and modelling the effect of the boundaries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2602.05901v2
- Title: Spontaneous Parity Breaking in Quantum Antiferromagnets on the Triangular Lattice
- Authors: Songtai Lv, Yuchen Meng, Haiyuan Zou
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.stat-mech; hep-lat; quant-ph
- Links: abs=https://arxiv.org/abs/2602.05901v2  pdf=https://arxiv.org/pdf/2602.05901v2.pdf

Abstract:
Frustration on the triangular lattice has long been a source of intriguing and often debated phases in many-body systems. Although symmetry analysis has been employed, the role of the seemingly trivial parity symmetry has received little attention. In this work, we show that phases induced by frustration are systematically shaped by an implicit rule-of-thumb associated with spontaneous parity breaking in weak longitudinal field. This principle enables us to anticipate and rationalize the regimes and conditions under which nontrivial phases emerge. For the spin-$S$ antiferromagnetic XXZ model, we demonstrate that a controversial parity-broken phase appears at intermediate values of $S$. In bilayer systems, enhanced frustration leads to additional phases, such as supersolids, whose properties can be classified by their characteristic parity features. Benefiting from our improved tensor network contraction techniques, we confirm these results through large-scale tensor-network calculations. This study offers an alternative viewpoint and a systematic approach for examining the interplay between spin, symmetry, and frustration in many-body systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2605.03434v3
- Title: Quantum Hierarchical Reinforcement Learning via Variational Quantum Circuits
- Authors: Yu-Ting Lee, Samuel Yen-Chi Chen
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2605.03434v3  pdf=https://arxiv.org/pdf/2605.03434v3.pdf

Abstract:
While parameterized quantum computations have shown success in standard reinforcement learning (RL), whether these advantages adapt to hierarchical RL (HRL) remains a critical open question. This work demonstrates that variational quantum circuits (VQCs) can effectively enhance HRL agents based on the option-critic architecture. Evaluated in standard environments, a hybrid HRL agent with a quantum feature extractor outperforms classical baselines while using fewer parameters. We also identify an architectural bottleneck: using VQCs for option-value estimation severely degrades learning. Further ablations reveal how quantum circuit design affects performance. Our work establishes design principles for parameter-efficient hybrid HRL agents.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2605.29871v2
- Title: Enhanced Density Fluctuations Near a Disordered Chiral Topological Transition
- Authors: Hai-Tao Ding, Sen Mu, Leong-Chuan Kwek, Gabriel Lemarié, Jiangbin Gong
- Categories: cond-mat.dis-nn (primary); cond-mat.dis-nn; quant-ph
- Links: abs=https://arxiv.org/abs/2605.29871v2  pdf=https://arxiv.org/pdf/2605.29871v2.pdf

Abstract:
The universal statistics of density fluctuations of localized quantum states may offer unprecedented opportunities to probe and understand quantum transport in connection with dimensionality, coherence, symmetry and disorder. To date, the possible role of topological phase transitions in the fluctuation statistics is not studied yet. Using a Su-Schrieffer-Heeger chain subject to off-diagonal disorder (so that chiral symmetry is preserved), this work investigates how a disorder driven topological phase transition impacts on the spatial fluctuations of the logarithmic wave-packet density $\ln P(r)$ at distance $r$ from the initial excitation. Away from the transition, in both topological and trivial localized phases, the standard deviation follows the conventional one-dimensional scaling $σ[\ln P(r)]\sim r^θ$ with $θ\simeq 1/2$. Near the transition, however, the fluctuation growth is enhanced: the fitted exponent $θ$ increases above $1/2$ in a nonmonotonic manner before returning close to $1/2$ at criticality. We interpret this behavior from the energy-resolved density of states and localization length. Near the transition, several energy sectors carry appreciable spectral weight and exhibit competitive decay rates, preventing a single localization scale from dominating the accessible wave-packet tail and thereby enhancing the fluctuations of $\ln P(r)$. Our results establish wave-packet fluctuation statistics as a dynamical diagnostic of disordered chiral topological transitions and motivate broader studies of fluctuation phenomena in disordered topological quantum systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2606.21901v2
- Title: Entanglement, Discord, and Residual Coherence in Scalar-Induced Gravitational Waves
- Authors: Waqas Ahmed
- Categories: gr-qc (primary); gr-qc; hep-ph; hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/2606.21901v2  pdf=https://arxiv.org/pdf/2606.21901v2.pdf

Abstract:
Scalar-induced gravitational waves (SIGWs) are usually characterized by their power spectrum, although their quadratic scalar source also carries higher-order correlation information. We investigate whether phase-sensitive correlations of a primordial Gaussian scalar state can survive decoherence and be transferred to the induced tensor sector. The scalar state is described in a fixed oscillator basis by the occupation $N_k^ζ$ and anomalous moment $M_k^ζ$, while the transfer is formulated through the unequal-time scalar Wightman function. The late-time tensor moments $d_k$ and $γ_k$ define an effective Gaussian reference state and its discord, whereas the exact SIGW state is generally non-Gaussian and contains an additional connected fourth-order cumulant. We therefore introduce the baseline-subtracted observable $Δκ_{\rm coh}=κ_N[G^>_{\rm coh}]-κ_N[G^>_{\rm ref}]$. For phase damping with $M_k^ζ\propto e^{-D_k}$, the Gaussian-reference contribution conditionally scales as $|γ_k|\propto e^{-2D_k}$ and $κ_N^{\rm G}\propto e^{-4D_k}$. This provides a framework in which the SIGW spectrum fixes the signal band, while higher-order statistics probe residual coherence beyond the power spectrum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2606.29316v2
- Title: Emergent energy scales in magnonic systems with relative motion
- Authors: Daigo Oue
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2606.29316v2  pdf=https://arxiv.org/pdf/2606.29316v2.pdf

Abstract:
Relative motion between interacting systems can generate emergent energy scales that are absent in isolated systems. While uniform motion can be eliminated by a Galilean transformation, relative motion between interacting systems generally cannot. By coupling to an excitation's spatial structure, relative motion generates a Doppler frequency determined by its wavevector and the relative velocity, providing a mechanism for driving nonequilibrium phenomena. In this tutorial, we illustrate these ideas using magnonic systems as a concrete platform. We first discuss motion-induced magnon transport between relatively moving ferromagnets, in which the Doppler frequency serves as an effective nonequilibrium bias in the perturbative regime. This mechanism produces magnon currents even without conventional driving forces such as temperature gradients or chemical potential differences. We then introduce motion-induced parametric instabilities. When the emergent scale becomes sufficiently large to resonantly create magnon pairs, the perturbative description breaks down, and the magnonic vacuum becomes unstable. This instability occurs above a critical velocity threshold and leads to spontaneous magnon-pair creation. Connections to related phenomena, including quantum friction, Cherenkov emission, and Zel'dovich superradiance, are also highlighted. The concept of an emergent energy scale provides a unifying framework for understanding transport phenomena and instabilities in quantum systems with relative motion.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2608.05427v2
- Title: School network reorganization under educational and spatial constraints using classical and quantum optimization
- Authors: Alessia Ciacco, Luigi Di Puglia Pugliese, Francesca Guerriero
- Categories: cs.CY (primary); cs.CY; quant-ph
- Links: abs=https://arxiv.org/abs/2608.05427v2  pdf=https://arxiv.org/pdf/2608.05427v2.pdf

Abstract:
School network reorganization is a strategic planning problem that requires balancing demographic trends, territorial accessibility, educational requirements, and institutional constraints while ensuring an efficient allocation of public resources. This paper proposes an optimization framework for school dimensioning decisions based on a novel Integer Linear Programming formulation integrating geographical, administrative, and educational criteria. A synthetic benchmark generator is introduced to evaluate the scalability and computational performance of the model on artificial instances, while a real-world case study involving the complete public school network of the Calabria region (Italy) is conducted using actual institutional, territorial, and demographic data. Furthermore, the model is implemented within a hybrid quantum optimization environment. The results show that the proposed formulation can be effectively solved by exact classical optimization and can also be represented and evaluated within a hybrid quantum-classical optimization framework. The computational experiments provide a proof-of-concept assessment of the applicability of hybrid quantum optimization to the considered school aggregation problem, while also highlighting the current computational advantage of classical optimization and the limitations of the tested benchmark instances.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2608.15116v2
- Title: Quantum channels on duals of von Neumann algebras in the Schrödinger picture
- Authors: Sviatoslav V. Dzhenzher
- Categories: math.OA (primary); math.OA; math.FA; quant-ph
- Links: abs=https://arxiv.org/abs/2608.15116v2  pdf=https://arxiv.org/pdf/2608.15116v2.pdf

Abstract:
The theory of quantum channels is traditionally studied either on finite-dimensional state spaces or within the Heisenberg picture as completely positive maps on C^*-algebras. In this paper, we consider quantum channels as completely positive maps on the duals of general von Neumann algebras in the Schrodinger picture. We investigate the construction of such channels through Pettis integrals using representations of topological groups.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-09-22 14:13
- arXiv: 2609.13387v2
- Title: Quantum Stochastic Walks on the Permutation Group
- Authors: Feng He, Arthur Hutsalyuk, Giuseppe Mussardo, Andrea Stampiggi
- Categories: cond-mat.stat-mech (primary); cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2609.13387v2  pdf=https://arxiv.org/pdf/2609.13387v2.pdf

Abstract:
How rapidly does order give way to randomness, and can quantum coherence accelerate this process? We address these questions through the paradigmatic problem of card shuffling, formulated as a random walk on the symmetric group $S_n$. We first recast the random-transposition walk studied by Diaconis and Shahshahani, as well as more general walks generated by conjugacy classes of $S_n$, in continuous time. We then identify the transition matrix of each classical walk with a permutation Hamiltonian generating a corresponding unitary quantum walk. Purely unitary evolution, however, does not generically converge to the uniform distribution in the classical sense of mixing: coherence preserves information rather than erasing it. We therefore embed the problem into a quantum stochastic walk, where coherent dynamics competes with the dissipative process responsible for classical mixing. In this setting, quantum coherence assists randomization. We prove that it can only decrease the distance from the uniform distribution in the computational basis and can therefore accelerate mixing. An analysis of the slowest mode yields a criterion for the coupling strength required to produce an appreciable speedup. Finally, numerical results reveal a scaling collapse of the ratio between quantum and classical mixing times onto a simple one-parameter form. Our results illustrate how coherence and dissipation can cooperate in the emergence of randomness in walks on permutation groups.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

