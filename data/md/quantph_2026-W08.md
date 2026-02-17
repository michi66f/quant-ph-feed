- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12309v1
- Title: Resource-Adaptive Teleportation Under Imperfect Entanglement: A Code-Puncturing Framework
- Authors: Mahmoud Saad Abouamer, Jaron Skovsted Gundersen, Søren Pilegaard Rasmussen, Petar Popovski
- Categories: quant-ph (primary); quant-ph; cs.IT; cs.NI
- Links: abs=https://arxiv.org/abs/2602.12309v1  pdf=https://arxiv.org/pdf/2602.12309v1.pdf

Abstract:
Quantum teleportation is a foundational protocol for sending quantum information through entanglement distribution and classical communication. Assuming ideal classical communication, the reliability of quantum teleportation is limited by the fidelity of the shared EPR pairs. This reliability can be improved through two mechanisms: entanglement purification and quantum error correction (QEC). Using both techniques in concert requires flexible QEC rates, since purification alters the structure of errors induced by imperfect-EPR teleportation, and fixed-rate codes cannot be uniformly effective across purification regimes or reliability targets. In this work, we supplement purification with punctured QEC codes, providing a family of code variants that can be adapted to error-channel characteristics and reliability targets. Punctured codes improve teleportation reliability across a broader range of purification regimes, enabling target reliability to be met without hardware-level code switching. This is corroborated by numerical results, showing that different punctured codes achieve the lowest logical error probability in different operating regimes, and that selecting among them reduces logical error relative to fixed-rate encoded teleportation. This reduction relaxes the requirement on the initial EPR fidelity or purification needed to achieve a target reliability. Overall, puncturing enables adaptation to varying entanglement conditions and reliability requirements while reusing a single stabilizer structure.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12334v1
- Title: Reconstruction of finite Quasi-Probability and Probability from Principles: The Role of Syntactic Locality
- Authors: Jacopo Surace
- Categories: quant-ph (primary); quant-ph; math.LO; math.PR; math.ST
- Links: abs=https://arxiv.org/abs/2602.12334v1  pdf=https://arxiv.org/pdf/2602.12334v1.pdf

Abstract:
Quasi-probabilities appear across diverse areas of physics, but their conceptual foundations remain unclear: they are often treated merely as computational tools, and operations like conditioning and Bayes' theorem become ambiguous. We address both issues by developing a principled framework that derives quasi-probabilities and their conditional calculus from structural consistency requirements on how statements are valued across different universes of discourse, understood as finite Boolean algebras of statements.We begin with a universal valuation that assigns definite (possibly complex) values to all statements. The central concept is Syntactic Locality: every universe can be embedded within a larger ambient one, and the universal valuation must behave coherently under such embeddings and restrictions. From a set of structural principles, we prove a representation theorem showing that every admissible valuation can be re-expressed as a finitely additive measure on mutually exclusive statements, mirroring the usual probability sum rule. We call such additive representatives pre-probabilities. This representation is unique up to an additive regraduation freedom. When this freedom can be fixed canonically, pre-probabilities reduce to finite quasi-probabilities, thereby elevating quasi-probability theory from a computational device to a uniquely determined additive representation of universal valuations. Classical finite probabilities arise as the subclass of quasi-probabilities stable under relativisation, i.e., closed under restriction to sub-universes. Finally, the same framework enables us to define a coherent theory of conditionals, yielding a well-defined generalized Bayes' theorem applicable to both pre-probabilities and quasi-probabilities. We conclude by discussing additional regularity conditions, including the role of rational versus irrational probabilities in this setting.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12387v1
- Title: Accelerating Feedback-based Algorithms for Quantum Optimization Using Gradient Descent
- Authors: Masih Mozakka, Mohsen Heidari
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2602.12387v1  pdf=https://arxiv.org/pdf/2602.12387v1.pdf

Abstract:
Feedback-based methods have gained significant attention as an alternative training paradigm for the Quantum Approximate Optimization Algorithm (QAOA) in solving combinatorial optimization problems such as MAX-CUT. In particular, Quantum Lyapunov Control (QLC) employs feedback-driven control laws that guarantee monotonic non-decreasing objective values, can substantially reduce the training overhead of QAOA, and mitigate barren plateaus. However, these methods might require long control sequences, leading to sub-optimal convergence rates. In this work, we propose a hybrid method that incorporates per-layer gradient estimation to accelerate the convergence of QLC while preserving its low training overhead and stability guarantees. By leveraging layer-wise gradient information, the proposed approach selects near-optimal control parameters, resulting in significantly faster convergence and improved robustness. We validate the effectiveness of the method through extensive numerical experiments across a range of problem instances and optimization settings.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12459v1
- Title: Temporal Framework for Causality-Preserving Scheduling of Measurements in Quantum Networks
- Authors: Jakob Kaltoft Søndergaard, René Bødker Christensen, Petar Popovski
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12459v1  pdf=https://arxiv.org/pdf/2602.12459v1.pdf

Abstract:
Distributed quantum protocols rely on classical feedforward information to process measurement outcomes, but heterogeneous hardware and uncertain local timing can make the causal order of measurements ambiguous when inferred solely from arrival times. Even in simple line networks with only Pauli measurements, end nodes cannot distinguish whether a missing outcome is caused by slow measurement or by delayed classical propagation. To resolve this ambiguity, we propose a time-division architecture for quantum networks in which nodes perform measurements in pre-assigned slots, ensuring a unique causal interpretation of outcomes. We formalize this temporal framework and derive the feedforward and adjacency constraints required to preserve measurement causality. For simple network topologies, we present an algorithm that yields optimal measurement schedules. Overall, the proposed time-division model provides a practical coordination layer that bridges the classical network timing with quantum measurement processing, enabling reliable and scalable measurement-based quantum networking.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12464v1
- Title: Challenge-Response Quantum Reinforcement Learning with Application to Quantum-Assisted Authentication
- Authors: Jawaher Kaldari, Saif Al-Kuwari
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12464v1  pdf=https://arxiv.org/pdf/2602.12464v1.pdf

Abstract:
Quantum reinforcement learning (QRL) has emerged as a promising research direction that integrates quantum information processing into reinforcement learning frameworks. While many existing QRL studies apply quantum agents to classical environments, it has been realized that the potential advantages of QRL are most naturally explored in environments that exhibit intrinsically quantum characteristics, where the agent's observations and interactions arise from quantum processes. In this work, we propose a quantum reinforcement learning environment formulated as a challenge-response task with hidden information. In the proposed environment, Alice encodes a classical bit into the parameters of a quantum circuit, while Bob, with a trained reinforcement learning agent, interacts with a limited number of quantum state copies to infer the hidden bit. The agent must select measurement strategies and decide when to terminate the interaction under explicit resource constraints. To study the solvability of the proposed environment, we consider three agents: a purely classical agent, a lightweight hybrid agent and a deep hybrid agent. Through experiments, we analyze the trade-off between inference accuracy and quantum resource consumption under varying interaction penalties. Our results show that the lightweight hybrid agent achieves reliable inference using as few as two quantum state copies, outperforming both the classical baseline and the deep hybrid agent in highly resource-constrained regimes. We further evaluate robustness under realistic quantum noise models and discuss the relevance of the proposed environment for security-oriented applications, including quantum-assisted authentication.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12465v1
- Title: Probabilistic Design of Parametrized Quantum Circuits through Local Gate Modifications
- Authors: Grier M. Jones, Aviraj Newatia, Alexander Lao, Aditya K. Rao, Viki Kumar Prasad, Hans-Arno Jacobsen
- Categories: quant-ph (primary); quant-ph; cs.LG
- Links: abs=https://arxiv.org/abs/2602.12465v1  pdf=https://arxiv.org/pdf/2602.12465v1.pdf

Abstract:
Within quantum machine learning, parametrized quantum circuits provide flexible quantum models, but their performance is often highly task-dependent, making manual circuit design challenging. Alternatively, quantum architecture search algorithms have been proposed to automate the discovery of task-specific parametrized quantum circuits using systematic frameworks. In this work, we propose an evolution-inspired heuristic quantum architecture search algorithm, which we refer to as the local quantum architecture search. The goal of the local quantum architecture search algorithm is to optimize parametrized quantum circuit architectures through a local, probabilistic search over a fixed set of gate-level actions applied to existing circuits. We evaluate the local quantum architecture search algorithm on two synthetic function-fitting regression tasks and two quantum chemistry regression datasets, including the BSE49 dataset of bond separation energies for first- and second-row elements and a dataset of water conformers generated using the data-driven coupled-cluster approach. Using state-vector simulation, our results highlight the applicability of local quantum architecture search algorithm for identifying competitive circuit architectures with desirable performance metrics. Lastly, we analyze the properties of the discovered circuits and demonstrate the deployment of the best-performing model on state-of-the-art quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12472v1
- Title: Dynamic Programming Principle and Stabilization for Mean-Field Quantum Filtering Systems
- Authors: Sofiane Chalal, Nina H. Amini, Hamed Amini, Mathieu Laurière
- Categories: quant-ph (primary); quant-ph; math.OC
- Links: abs=https://arxiv.org/abs/2602.12472v1  pdf=https://arxiv.org/pdf/2602.12472v1.pdf

Abstract:
Working within the quantum filtering framework, we establish a dynamic programming principle in an infinite-dimensional setting by embedding the state space into the Hilbert-Schmidt space. We then study a stabilization problem for continuously monitored Ising-coupled qubits and, in the mean-field limit, demonstrate quantum state reduction together with exponential convergence toward prescribed eigenstates under suitable feedback laws.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12518v1
- Title: Compressed Sensing Shadow Tomography
- Authors: Joseph Barreto, Daniel Lidar
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12518v1  pdf=https://arxiv.org/pdf/2602.12518v1.pdf

Abstract:
Estimating many local expectation values over time is a central measurement bottleneck in quantum simulation and device characterization. We study the task of reconstructing the Pauli-signal matrix $S_{ij}=\text{Tr}(O_i ρ(t_j))$ for a collection of $M$ low-weight Pauli observables $\{O_i\}_{i=1}^M$ over $N$ timesteps $\{t_j\}_{j=1}^N$, while minimizing the total number of device shots. We propose a Compressed Sensing Shadow Tomography (CSST) protocol that combines two complementary reductions. First, local classical shadows reduce the observable dimension by enabling many Pauli expectation values to be estimated from the same randomized snapshots at a fixed time. Second, compressed sensing reduces the time dimension by exploiting the fact that many expectation-value traces are spectrally sparse or compressible in a unitary (e.g., Fourier) transform basis. Operationally, CSST samples $m\ll N$ timesteps uniformly at random, collects shadows only at those times, and then reconstructs each length-$N$ signal via standard $\ell_1$-based recovery in the unitary transform domain. We provide end-to-end guarantees that explicitly combine shadow estimation error with compressed sensing recovery bounds. For exactly $s$-sparse signals in a unitary transform basis, we show that $m=O \left(s\log^2 s \log N\right)$ random timesteps suffice (with high probability), leading to total-shot savings scaling as $\widetildeΘ(N/s)$ (i.e., up to polylogarithmic factors) relative to collecting shadows at all $N$ timesteps. For approximately sparse signals, the reconstruction error decomposes into a compressibility (tail) term plus a noise term. We present numerical experiments on noisy many-qubit dynamics that support strong Fourier compressibility of Pauli traces and demonstrate substantial shot reductions with accurate reconstruction.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12539v1
- Title: Predicting properties of quantum thermal states from a single trajectory
- Authors: Jiaqing Jiang, Jiaqi Leng, Lin Lin
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12539v1  pdf=https://arxiv.org/pdf/2602.12539v1.pdf

Abstract:
Estimating thermal expectation values of observables is a fundamental task in quantum physics, quantum chemistry, and materials science. While recent quantum algorithms have enabled efficient quantum preparation of thermal states, observable estimation via sampling remains costly: a straightforward implementation separates successive measurements by a full mixing time in order to ensure samples are approximately independent. In this work, we show that the sampling cost can be substantially reduced by using a single Gibbs-sampling trajectory. After a single burn-in period, we interleave coherent measurements that satisfy detailed balance with respect to the target Gibbs state. The efficiency of this approach rests on the fact that, in many settings, the autocorrelation time can be significantly shorter than the mixing time. For energy estimation (and more generally for observables commuting with the Hamiltonian), we implement the required measurements using Gaussian-filtered quantum phase estimation with only logarithmic overhead. We also introduce a weighted operator Fourier transform technique to mitigate measurement-induced disturbance for general observables.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12664v1
- Title: Sperner state and multipartite entanglement signals
- Authors: Xin-Xiang Ju, Ya-Wen Sun, Yang Zhao
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12664v1  pdf=https://arxiv.org/pdf/2602.12664v1.pdf

Abstract:
We establish a systematic classification scheme for multipartite entanglement structures. We define Sperner states -- a broad class of states where apparent multipartite entanglement decomposes into fewer-partite entanglement among subsystems of each party. Each class of Sperner states is associated with one antichain hypergraph and each hypergraph encodes the maximal entanglement structure permissible under its constraints. We introduce a Multi-entanglement Measure Space (MEMS) where each Sperner class corresponds to a linear subspace defined by the vanishing of specific linear combinations of bipartite and multipartite measures. The nonvanishing of such combinations signals multipartite entanglement beyond the associated hypergraph, thereby distinguishing entanglement structures. We build a two way connection between each hypergraph entanglement structure and a distinct set of combinations, thereby quantifying the entanglement pattern and providing a unified basis for classifying all multipartite entanglement.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12685v1
- Title: Floquet implementation of a 3d fermionic toric code with full logical code space
- Authors: Yoshito Watanabe, Bianca Bannenberg, Simon Trebst
- Categories: quant-ph (primary); quant-ph; cond-mat.str-el
- Links: abs=https://arxiv.org/abs/2602.12685v1  pdf=https://arxiv.org/pdf/2602.12685v1.pdf

Abstract:
Floquet quantum error-correcting codes provide an operationally economical route to fault tolerance by dynamically generating stabilizer structures using only two-body Pauli measurements. But while it is well established that stabilizer codes in higher spatial dimensions gain additional levels of intrinsic robustness, higher-dimensional Floquet codes have hitherto been explored only in limited scope. Here we introduce a 3d generalization of a Floquet code whose instantaneous stabilizer group realizes a 3d fermionic toric code, while crucially preserving all three logical qubits throughout the entire measurement sequence. One central ingredient is the identification of a 3d lattice geometry that generalizes the features of the Kekulé lattice underlying the 2d Hastings-Haah code - specifically, a structure where deleting any one edge color yields a two-color subgraph that decomposes into short, closed loops rather than homologically nontrivial chains. This loop property avoids the collapse of logical information that plagues naive sequential two-color measurement schedules on many 3d lattices. Although, for our lattice geometry, a simple 3-round cycle that sequentially measures the three types of parity checks does not expose the full error syndrome set, we show that one can append a measurement sequence to extract the missing syndromes without disturbing the logical subspace. Beyond code design, 3d tricoordinated lattice geometries define a family of 3d monitored Kitaev models, in which random measurements of the non-commuting parity checks give rise to dynamically created entangled phases with nontrivial topology. In discussing the general structure of their underlying phase diagrams and, in particular, the existence of certain quantum critical points, we again make a connection to the general preservation of logical information in time-ordered Floquet protocols.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12712v1
- Title: Reverse Delegated Training and Private Inference via Perfectly-Secure Quantum Homomorphic Encryption
- Authors: Sergio A. Ortega, Miguel A. Martin-Delgado
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12712v1  pdf=https://arxiv.org/pdf/2602.12712v1.pdf

Abstract:
Quantum machine learning in cloud environments requires protecting sensitive data while enabling remote computation. Here we demonstrate the first realistic implementations of a perfectly-secure quantum homomorphic encryption (QHE) scheme applied to quantum neural networks (QNN). Using efficient Clifford+$T$ decomposition, we implement quantum convolutional neural networks for two complementary scenarios: (i) reverse delegated training, where encrypted data from multiple providers trains a user's network via federated aggregation; (ii) private inference, where users process encrypted data with remote quantum networks. Moreover, analysis of server circuit privacy reveals probabilistic model protection through Pauli gate concealment. These results establish perfectly-secure QHE as a practical framework for multi-party quantum machine learning.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12767v1
- Title: Preparing Quantum Backflow States by Large Momentum Transfer
- Authors: Yuchong Chen, Yijun Tang
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12767v1  pdf=https://arxiv.org/pdf/2602.12767v1.pdf

Abstract:
A quantum backflow state refers to a quantum state exhibiting negative probability density flux albeit a completely positive momentum spectrum. Extending earlier work that uses single laser pulse to prepare quantum backflow state in an ultracold atomic BEC [1], we theoretical investigated flexible quantum backflow state preparation via large momentum transfer technique, which to our knowledge, has not been studied before. By combining atom interferometry theory and non-interacting BEC wave function, we solve for the evolution of a BEC wavepacket under atom interferometry sequence. Simulation results show a highly tunable backflow flux and critical density under our scheme, and can be manipulated to go beyond existing numbers.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12773v1
- Title: Design and Operation of Wafer-Scale Packages Containing >500 Superconducting Qubits
- Authors: Oscar W. Kennedy, Waqas Ahmad, Robert Armstrong, Amir Awawdeh, Anirban Bose, Kevin G. Crawford, Sergey Danilin, William D. David, et al.
- Categories: quant-ph (primary); quant-ph; physics.app-ph; physics.ins-det
- Links: abs=https://arxiv.org/abs/2602.12773v1  pdf=https://arxiv.org/pdf/2602.12773v1.pdf

Abstract:
Packages capable of supporting large arrays of high-coherence superconducting qubits are vital for the realisation of fault-tolerant quantum computers and the necessary high-throughput metrology required to optimise fabrication and manufacturing processes. We present a wafer-scale packaging architecture supporting over 500 qubits on a single 3-inch die. The package is engineered to suppress parasitic RF modes, and to mitigate material loss through simulation-informed design while managing differential thermal contraction to ensure robust operation at millikelvin temperatures. System-level heat-load calculations from a large wiring payload show this package may be operated in commercial dilution refrigerators. Measurements of the qubits loaded into the package show median $T_1$, $T_{2e} \sim 100~μ$s ($\sim$100 qubits) alongside readout with median fidelity of 97.5% (54 qubits) and a median qubit temperature of 36 mK (54 qubits). These results validate the performance of these packages and demonstrate that large-scale integration can be achieved without compromising device performance. Finally, we highlight the utility of these packages as a tool for high throughput feedback on qubit figures of merit over large sample sizes, allowing identification of performance outliers in the tails of the coherence distribution, a critical capability for informing fabrication and manufacture of high-quality quantum qubits and quantum processors.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12787v1
- Title: Equilibrium thermometry in the multilevel quantum Rabi model
- Authors: Tabitha Doicin, Luis A. Correa, Jonas Glatthard, Andrew D. Armour, Gerardo Adesso
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12787v1  pdf=https://arxiv.org/pdf/2602.12787v1.pdf

Abstract:
The temperature sensitivity of a probe in equilibrium can be gauged by its thermal quantum Fisher information (QFI). It is known that probes exhibiting degeneracy in their energy-level structure can achieve larger sensitivities, while probes with a more uniform spectrum may remain sensitive over a broader temperature range. Here, we study the thermometric performance of a multilevel quantum Rabi model in which two well-separated atomic manifolds of near-degenerate levels couple to a single cavity mode. We generalise the standard quantum Rabi treatment in the adiabatic regime to find an approximate closed-form expression for the thermal QFI. We then characterise two complementary limits. On the one hand, a large dark-state manifold (dark-manifold saturation) produces a robust peak in thermal sensitivity due to bright--dark population transfer. Such increase in sensitivity is further maximised at an intermediate light--matter coupling strength. Maximising instead the number of bright states (bright-manifold saturation) generates a broadband thermal response that becomes increasingly stable under random light--matter couplings as the number of levels is increased. The rich spectral structure of our cavity-QED model thus makes it a versatile and sensitive equilibrium thermometer over a broad range of temperatures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12823v1
- Title: Towards Trapped-Ion Thermometry Using Cavity-Based EIT
- Authors: Abhijit Kundu, Vijay Bhatt, Arijit Sharma
- Categories: quant-ph (primary); quant-ph; physics.atom-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2602.12823v1  pdf=https://arxiv.org/pdf/2602.12823v1.pdf

Abstract:
We present a technique for measuring ion temperature using cavity-based electromagnetically induced transparency (EIT) applicable for cavity-qed systems in the strong coupling regime. This method enables efficient extraction of the ion's phonon occupation number following sub-Doppler cooling close to the motional ground state. The proposed method relies on monitoring the cavity probe transmission while scanning the probe laser frequency once cavity EIT is established using the control beam, significantly simplifying the measurement procedure. We theoretically establish a model that demonstrates influence of thermal state of the trapped ion vis a vis the EIT linewidth measured. We show how the cavity EIT transmission may be used as a thermometry tool to deduce the ion temperature as well as the motional state for an ion in the sub-Doppler cooling regime. The current method can only be used for operation in the resolved-sideband regime, where individual motional states can be selectively addressed for all relevant transitions either by selecting appropriate energy levels for the three-level system or by employing strong confinement with high secular frequencies ($\sim 10 MHz$).

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12831v1
- Title: Optimized Compilation of Logical Clifford Circuits
- Authors: Alexander Popov, Nico Meyer, Daniel D. Scherer, Guido Dietl
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12831v1  pdf=https://arxiv.org/pdf/2602.12831v1.pdf

Abstract:
Fault-tolerant quantum computing hinges on efficient logical compilation, in particular, translating high-level circuits into code-compatible implementations. Gate-by-gate compilation often yields deep circuits, requiring significant overhead to ensure fault-tolerance. As an alternative, we investigate the compilation of primitives from quantum simulation as single blocks. We focus our study on the [[n,n-2,2]] code family, which allows for the exhaustive comparison of potential compilation primitives on small circuit instances. Based upon that, we then introduce a methodology that lifts these primitives into size-invariant, depth-efficient compilation strategies. This recovers known methods for circuits with moderate Hadamard counts and yields improved realizations for sparse and dense placements. Simulations show significant error-rate reductions in the compiled circuits. We envision the approach as a core component of peephole-based compilers. Its flexibility and low hand-crafting burden make it readily extensible to other circuit structures and code families.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12840v1
- Title: Airline Fleet Assignment Problems with Binary and Integer Programming models: Classical vs Quantum Annealing
- Authors: Kuntal Adak, Sakshi Kaushik, Rahul Rana
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.12840v1  pdf=https://arxiv.org/pdf/2602.12840v1.pdf

Abstract:
This research highlights the potential of quantum annealing in tackling large-scale optimization problems within the airline industry,demonstrating its efficiency for certain problem sizes while also acknowledging its current limitations. The comparative analysis provides valuable insights into the performance of advanced computational techniques, paving the way for further advancements in optimizing fleet assignments in the aviation sector.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12909v1
- Title: Quantum logic control and entanglement in hybrid atom-molecule arrays
- Authors: Chi Zhang, Sara Murciano, Nathanan Tantivasadakarn, Ran Finkelstein
- Categories: quant-ph (primary); quant-ph; physics.atom-ph
- Links: abs=https://arxiv.org/abs/2602.12909v1  pdf=https://arxiv.org/pdf/2602.12909v1.pdf

Abstract:
Polar molecules, with their rich internal structure, offer immense potential for fundamental physics, quantum technology, and controlled chemistry. However, their utilization is currently limited because of slow and imperfect state detection and weak dipolar interaction, limiting fast and large-scale entanglement generation. We propose and analyze a scheme for quantum logic control and measurement-based state preparation in a hybrid platform of polar molecules and neutral atoms. The method leverages fast, high-fidelity atom-molecule gates and high-fidelity atomic ancilla measurements to overcome the common challenges in molecule-only platforms, while preserving their diverse structural advantages. The proposed atom-molecule controlled-phase gate is based on resonant dipole-dipole exchange between a molecular rotational transition and an atomic Rydberg transition, rendering it three orders of magnitude faster than any direct molecule-molecule entangling gate. We further study several applications of our scheme including the preparation of molecular GHZ states for quantum enhanced precision measurements, the preparation of exotic molecular qudit states with topological order, and measurement-altered criticality. Our scheme is applicable to any polar molecule. It expands the paradigm of quantum logic control and paves the way to large-scale molecular entangled states. More generally, it highlights a concrete hybrid quantum system in which each qubit is utilized in an optimal way and where the measurement-based approach can yield a significant advantage in near-term devices.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12914v1
- Title: Quantum metrology with partially accessible chaotic sensors
- Authors: Harshita Sharma, Sayan Choudhury, Jayendra N. Bandyopadhyay
- Categories: quant-ph (primary); quant-ph; cond-mat.other; nlin.CD
- Links: abs=https://arxiv.org/abs/2602.12914v1  pdf=https://arxiv.org/pdf/2602.12914v1.pdf

Abstract:
Most quantum metrology protocols harness highly entangled probe states and globally accessible measurements to surpass the standard quantum limit. However, it is challenging to satisfy these requirements in realistic many-body sensors. We demonstrate that both of these constraints can be overcome in quantum chaotic sensors. Crucially, we establish that even in the presence of partial measurement accessibility, chaotic dynamics enables initial unentangled states to exhibit Heisenberg scaling of the quantum Fisher information, $I_α$ with time. In the weakly chaotic regime, we identify spin-coherent states placed at the edge of the regular islands in the mixed classical phase space as optimal initial states for enhanced sensitivity. On the other hand, in the strongly chaotic regime, $I_α$ is insensitive to the choice of the initial state. Notably, quantum-enhanced sensitivity is achieved even when a very low fraction ($\sim 5\%$) of the qubits are accessible. These results establish quantum chaos as a robust resource for quantum-enhanced sensing under realistic accessibility constraints on accessibility.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13006v1
- Title: Effective classical potential for quantum statistical averages
- Authors: Vijay Ganesh Sadhasivam, Stuart C. Althorpe, Venkat Kapil
- Categories: quant-ph (primary); quant-ph; physics.chem-ph
- Links: abs=https://arxiv.org/abs/2602.13006v1  pdf=https://arxiv.org/pdf/2602.13006v1.pdf

Abstract:
We present an effective potential that allows quantum thermal expectation values of a position-dependent observable to be estimated as a classical ensemble average of the corresponding function. We follow the approach of Feynman and Hibbs, but perform the mean-field treatment of quantum fluctuations about the path starting point rather than the path centroid. Furthermore, rather than performing a full variational optimization of the potential, we explore approximate functional forms that yield a numerical robustness. The resulting closed-form potential is exact in the classical and harmonic limits; benchmarks against exact position distributions for one-dimensional quartic, Morse, and double-well potentials, show good agreement for potentials with harmonic support.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13026v1
- Title: Weighted graph states as a resource for quantum metrology
- Authors: B. J. Alexander, Ş. K. Özdemir, M. S. Tame
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.13026v1  pdf=https://arxiv.org/pdf/2602.13026v1.pdf

Abstract:
Quantum metrology exploits quantum mechanical effects to increase the precision of measurements of physical quantities. A wide variety of applications are currently being developed for scientific and technological purposes, however, most research relies on the use of highly entangled resource states that are challenging to generate and control in a given physical system. Here, we study the use of weighted graph states as more accessible resources for quantum metrology, which yield a favorable precision beyond the classical limit, approaching the Heisenberg limit. We find a notable robustness to variation in weights and less challenging weight requirements compared to standard graph states, which require a maximal weight at all edges. Both of these aspects reduce the practical demands in a physical setup, with the latter implying significantly less entanglement is required to gain a quantum advantage in metrology. We study the quantum Fisher information and optimized estimator variance of two identified sub classes of weighted graph states for an arbitrary number of N qubits, providing analytical forms and investigating their scaling. Our work opens up opportunities for using weakly entangled states in quantum-enhanced metrology.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13094v1
- Title: A Quantum Reservoir Computing Approach to Quantum Stock Price Forecasting in Quantum-Invested Markets
- Authors: Wendy Otieno, Alexandre Zagoskin, Alexander G. Balanov, Juan Totero Gongora, Sergey E. Savel'ev
- Categories: quant-ph (primary); quant-ph; physics.data-an
- Links: abs=https://arxiv.org/abs/2602.13094v1  pdf=https://arxiv.org/pdf/2602.13094v1.pdf

Abstract:
We present a quantum reservoir computing (QRC) framework based on a small-scale quantum system comprising at most six interacting qubits, designed for nonlinear financial time-series forecasting. We apply the model to predict future daily closing trading volumes of 20 quantum-sector publicly traded companies over the period from April 11, 2020, to April 11, 2025, as well as minute-by-minute trading volumes during out-of-market hours on July 7, 2025. Our analysis identifies optimal reservoir parameters that yield stock trend (up/down) classification accuracies exceeding $86 \%$. Importantly, the QRC model is platform-agnostic and can be realized across diverse physical implementations of qubits, including superconducting circuits and trapped ions. These results demonstrate the expressive power and robustness of small-scale quantum reservoirs for modeling complex temporal correlations in financial data, highlighting their potential applicability to real-world forecasting tasks on near-term quantum hardware.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13095v1
- Title: Theory of Steady States for Lindblad Equations beyond Time-Independence: Classification, Uniqueness and Symmetry
- Authors: Hironobu Yoshida, Ryusuke Hamazaki
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; math-ph
- Links: abs=https://arxiv.org/abs/2602.13095v1  pdf=https://arxiv.org/pdf/2602.13095v1.pdf

Abstract:
We present a rigorous and comprehensive classification of the asymptotic behavior of time-quasiperiodic Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) equations under the assumption of Hermitian jump operators. Our main contributions are twofold: first, we establish a criterion for the uniqueness of steady states. The criterion is formulated in terms of the algebra generated by the GKSL generators and provides a necessary and sufficient condition when the generators are analytic functions of time. We demonstrate the utility of our criterion through prototypical examples, including quantum many-body spin chains. Second, we extend the concept of strong symmetry for time-dependent GKSL equations by introducing two distinct forms, strong symmetry in the Schrödinger picture and that in the interaction picture, and completely classify the asymptotic dynamics with them. More concretely, we rigorously uncover that the strong symmetry in the interaction picture is responsible for non-trivial time-dependent steady states, such as coherent oscillations, whereas that in the Schrödinger picture controls the existence of time-independent steady states. This classification not only encompasses established mechanisms underlying non-trivial oscillatory steady states, such as strong dynamical symmetry and Floquet dynamical symmetry, but also reveals symmetry-predicted, time-dependent asymptotic dynamics in a novel class of open quantum systems. Our framework thus provides a rigorous foundation for controlling dissipative quantum systems in a time-dependent manner.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13099v1
- Title: Stronger Welch Bounds and Optimal Approximate $k$-Designs
- Authors: Riccardo Castellano, Dmitry Grinko, Sadra Boreiri, Nicolas Brunner, Jef Pauwels
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2602.13099v1  pdf=https://arxiv.org/pdf/2602.13099v1.pdf

Abstract:
A fundamental question asks how uniformly finite sets of pure quantum states can be distributed in a Hilbert space. The Welch bounds address this question, and are saturated by $k$-designs, i.e. sets of states reproducing the $k$-th Haar moments. However, these bounds quickly become uninformative when the number of states is below that required for an exact $k$-design. We derive strengthened Welch-type inequalities that remain sharp in this regime by exploiting rank constraints from partial transposition and spectral properties of the partially transposed Haar moment operator. We prove that the deviation from the Welch bound captures the average-case approximation error, hence characterizing a natural notion of minimum achievable error at fixed cardinality. For $k=3$, we prove that SICs and complete MUB sets saturate our bounds, making them optimal approximate 3-designs of their cardinality. This leads a natural variational criterion to rule out the existence of a complete set MUBs, which we use to obtain numerical evidence against such set in dimension $6$. As a key technical ingredient, we compute the complete spectrum of the partially transposed symmetric-subspace projector, including multiplicities and eigenvectors, which may find applications beyond the present work.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13145v1
- Title: Single snapshot non-Markovianity of Pauli channels
- Authors: Alireza Seif, Moein Malekakhlagh, Swarnadeep Majumder Luke C. G. Govia
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.13145v1  pdf=https://arxiv.org/pdf/2602.13145v1.pdf

Abstract:
Pauli channels are widely used to describe errors in quantum computers, particularly when noise is shaped via Pauli twirling. A common assumption is that such channels admit a Markovian generator, namely a Pauli-Lindblad model with non-negative rates, but the validity of this assumption has not been systematically examined. Here, using CP-indivisibility as our criterion for non-Markovianity, we study multi-qubit Pauli channels from a single snapshot of the dynamics. We find that while the generator always has the same structure as the standard Pauli-Lindblad model, the rates may be negative or complex. We show that random Pauli channels are almost always non-Markovian, with the probability of encountering a negative rate converging doubly exponentially to unity with the number of qubits. For physically motivated noise models shaped by Pauli twirling, including single-qubit over-rotations and two-qubit amplitude damping errors, we find that negative rates are generic, even when the underlying physical noise is Markovian. We generalize probabilistic error amplification and cancellation to non-Markovian generators, and quantify the sampling overhead introduced by negative and complex rates. Experiments on superconducting qubits confirm that allowing negative rates in the learned noise model yields more accurate predictions than restricting to non-negative rates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13146v1
- Title: Mean-Force Hamiltonians from Influence Functionals
- Authors: Gerard McCaul
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2602.13146v1  pdf=https://arxiv.org/pdf/2602.13146v1.pdf

Abstract:
The Hamiltonian of mean force (HMF) provides the standard starting point for strong-coupling thermodynamics, yet explicit operator forms are known only in restricted settings. We present a quenched density framework that uses the Hubbard-Stratonovich transformation to rewrite the reduced equilibrium state as an average over local propagators in imaginary time. This approach rigorously separates the statistical definition of the environment from the algebraic structure of the system response. We apply this framework to the minimal case of a harmonic environment with a coupling commuting with the system Hamiltonian. In this scenario the correction to the HMF has an exact, closed-form expression. We validate this result against finite-bath trace-out calculations and stochastic imaginary-time sampling in a five-level projector-coupled model.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12320v1
- Title: Observing dissipationless flow of an impurity in a strongly repulsive quantum fluid
- Authors: Milena Horvath, Sudipta Dhar, Elisabeth Wybo, Dimitrios Trypogeorgos, Yanliang Guo, Mikhail Zvonarev, Michael Knap, Manuele Landini, et al.
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12320v1  pdf=https://arxiv.org/pdf/2602.12320v1.pdf

Abstract:
The frictionless motion of an object through a fluid medium is commonly viewed as a hallmark of superfluidity. According to Landau, kinematic constraints prohibit superfluid behavior in one-dimensional (1D) bosonic systems. Here, using ultracold atoms, we show how a microscopic impurity can propagate through a strongly interacting 1D Bose gas without any friction, at odds with conventional expectations. We inject the impurity with initial velocities ranging from the subsonic to supersonic regime, and subsequently track its dynamics. For supersonic initial velocities, we observe the formation of a shock wave and a remarkably fast relaxation to a stationary regime, on a time scale that increases with decreasing impurity velocity. After reaching the stationary state, the impurity continues its motion through the system with a finite velocity. Our findings demonstrate how quantum effects can conspire to eliminate dissipation of a microscopic object immersed in a quantum fluid, thereby bringing novel insights into the propagation of matter and information in the quantum realm.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12330v1
- Title: Consistent inclusion of triple substitutions within a coupled cluster based static quantum embedding theory
- Authors: Avijit Shee, Fabian M. Faulstich, K. Birgitta Whaley, Lin Lin, Martin Head-Gordon
- Categories: physics.chem-ph (primary); physics.chem-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12330v1  pdf=https://arxiv.org/pdf/2602.12330v1.pdf

Abstract:
We incorporate a solver for the fragment problem with accuracy beyond coupled cluster singles and doubles (CCSD) into the previously proposed static embedding framework, MPCC. To this end, we employ a CCSDT solver for the fragment subsystem. For the environment subsystem, we construct a perturbative estimate of the triples amplitudes, explicitly accounting for feedback from all fragment amplitudes. The resulting approach is denoted MPCCSDT(pt). We further introduce a more complete formulation in which feedback from the environment amplitudes to the fragment amplitudes is also included. This scheme involves an iterative treatment of the environment triples amplitudes and is denoted MPCCSDT(it). In addition, we assess the accuracy of the previously proposed low-level method by introducing a modified low-level approach that incorporates a lowest-order treatment of selected long-range effects, including spin fluctuations and charge polarization. All resulting approaches may be viewed as post-CCSD(T) methods. We therefore consider test cases for which CCSD(T) exhibits substantial deviations from CCSDT. Our results demonstrate that inclusion of triples amplitudes at the fragment level alone is insufficient; a perturbative treatment of the environment triples amplitudes is required. For many energy-difference applications, feedback from the environment triples amplitudes to the fragment amplitudes, is not essential, but it does play a role in the very challenging molecules. A very interesting finding from our study is that in some challenging cases, we need an improved (second-order) perturbative method for the SD amplitudes, going beyond the first-order one used in our earlier work.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12339v1
- Title: Magic and Wormholes in the Sachdev-Ye-Kitaev Model
- Authors: Valérie Bettaque, Brian Swingle
- Categories: hep-th (primary); hep-th; cond-mat.str-el; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12339v1  pdf=https://arxiv.org/pdf/2602.12339v1.pdf

Abstract:
Any quantum state is fully specified by the expectation values of a complete set of Hermitian operators. For a system of Majorana fermions, such as the Sachdev-Ye-Kitaev (SYK) model, this set of observables can be taken to be all possible strings of Majorana fermion operators. The expectation values of these fermion strings in a thermal state depend erratically on the microscopic couplings that specify the SYK Hamiltonian, and we study their statistical properties directly in the thermodynamic limit using path integral techniques. When the underlying SYK Hamiltonian is chaotic, we find that these expectation values are well-modeled as real Gaussian random variables with zero mean and a variance that we compute. In contrast, for the integrable variant of SYK, we find that the expectation values are actually non-Gaussian. We then use these results to study measures of magic in the SYK thermal state, including the robustness of magic and the stabilizer Rényi entropy. We also show that our results can be quantitatively reproduced with a dual gravity calculation in the chaotic case at sufficiently low temperature. In this dual gravity model the variance of a given microscopic operator string is related to a wormhole geometry stabilized by a massive particle which is dual to the operator string. Our results thus provide a concrete and quantitative setting in which to study the relationship between randomness, wormholes, and closed universes as well as a holographic dual of quantum magic.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12417v1
- Title: Information lattice approach to the metal-insulator transition
- Authors: William Skoglund, Elton Giacomelli, Yiqi Yang, Jens H. Bardarson, Erik van Loon
- Categories: cond-mat.str-el (primary); cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12417v1  pdf=https://arxiv.org/pdf/2602.12417v1.pdf

Abstract:
Correlation functions and correlation lengths are frequently used to describe phase transitions in quantum systems, but they require an explicit choice of observables. The recently introduced information lattice instead provides an observable-independent way to identify where and at which scale information is contained in quantum lattice models. Here, we use it to study the difference between the metallic and insulating regime of one-dimensional tight-binding chains. We find that the information per scale follows a power law in metals at low temperature and that Friedel-like oscillations are visible in the information lattice. At high temperature or in insulators at low temperature, the information per scale decays exponentially. Thus, the information lattice is a useful tool for analyzing the metal-insulator transition.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12550v1
- Title: Effects of magnonic Kerr nonlinearity on magnon-polaritons with a soft-mode
- Authors: Takahiro Chiba
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; nlin.CD; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12550v1  pdf=https://arxiv.org/pdf/2602.12550v1.pdf

Abstract:
We theoretically study the effects of magnonic Kerr nonlinearity on magnon-polaritons (MPs) with a soft-mode in easy-axis ferromagnets coupled to a microwave cavity. Using an effective circuit model capable of describing MPs up to the nonperturbative strong-coupling regime, we show that chaotic and frequency-comb-like behaviors of MPs emerge at the original modes crossing point. Furthermore, we demonstrate that the Kerr nonlinearity induces a finite excitation gap in the soft-mode, particularly in the strong-coupling regime.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12588v1
- Title: Topology and edge modes surviving criticality in non-Hermitian Floquet systems
- Authors: Longwen Zhou
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12588v1  pdf=https://arxiv.org/pdf/2602.12588v1.pdf

Abstract:
The discovery of critical points that can host quantized nonlocal order parameters and degenerate edge modes relocate the study of symmetry-protected topological phases (SPTs) to gapless regions. In this letter, we reveal gapless SPTs (gSPTs) in systems tuned out-of-equilibrium by periodic drivings and non-Hermitian couplings. Focusing on one-dimensional models with sublattice symmetry, we introduce winding numbers by applying the Cauchy's argument principle to generalized Brillouin zone (GBZ), yielding unified topological characterizations and bulk-edge correspondence in both gapped phases and at gapless critical points. The theory is demonstrated in a broad class of Floquet bipartite lattices, unveiling unique topological criticality of non-Hermitian Floquet origin. Our findings identify gSPTs in driven open systems and uncover robust topological edge modes at phase transitions beyond equilibrium.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12627v1
- Title: Boundary mutual information in double holography
- Authors: Yuxuan Liu, Yi Ling, Zhuo-Yu Xian
- Categories: hep-th (primary); hep-th; cond-mat.str-el; gr-qc; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12627v1  pdf=https://arxiv.org/pdf/2602.12627v1.pdf

Abstract:
We consider a composite system where AdS$_3$ gravity is coupled to a flat heat bath and investigate the mutual information between two subregions on the intersection of the AdS$_3$ and bath, referred to as the boundary mutual information (BMI). The corresponding entanglement entropy is captured via quantum extremal surfaces (QES), which holographically be computed by a surface optimization algorithm based on ``Surface Evolver''. We focus on both connected and disconnected configurations of the quantum entanglement wedge (Q-EW) in the AdS$_3$ bulk and analyze the finite corrections to the BMI. Our numerical results reveal a phase transition of the BMI as the separation between two subregions increases. Furthermore, we find that the BMI can naturally be decomposed into two distinct components: a geometric term arising from the areas of the quantum extremal surfaces, and a correction term resulting from bulk quantum fields within the Q-EW. Interestingly, the geometric contribution always exceeds the total BMI, indicating a negative correction from the bulk matter fields. This negativity can be understood as the result of subtracting a greater contribution from quantum fields in the connected Q-EW than in the disconnected one. We also reproduce the negative contribution of bulk quantum fields to BMI within a random tensor network (RTN) toy model of double holography. Modeling the bulk as a highly mixed state entangled with a large bath leads to a volume-law bulk entropy. In the large bond-dimension limit, the geometric part of the BMI remains non-negative, while the bulk entropy contribution becomes non-positive when the Q-EWs merge.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12704v1
- Title: QTabGAN: A Hybrid Quantum-Classical GAN for Tabular Data Synthesis
- Authors: Subhangi Kumari, Rakesh Achutha, Vignesh Sivaraman
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12704v1  pdf=https://arxiv.org/pdf/2602.12704v1.pdf

Abstract:
Synthesizing realistic tabular data is challenging due to heterogeneous feature types and high dimensionality. We introduce QTabGAN, a hybrid quantum-classical generative adversarial framework for tabular data synthesis. QTabGAN is especially designed for settings where real data are scarce or restricted by privacy constraints. The model exploits the expressive power of quantum circuits to learn complex data distributions, which are then mapped to tabular features using classical neural networks. We evaluate QTabGAN on multiple classification and regression datasets and benchmark it against leading state-of-the-art generative models. Experiments show that QTabGAN achieves up to 54.07% improvement across various classification datasets and evaluation metrics, thus establishing a scalable quantum approach to tabular data synthesis and highlighting its potential for quantum-assisted generative modelling.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.12729v1
- Title: Fractional $k$-positivity: a continuous refinement of the $k$-positive scale
- Authors: Mohsen Kian
- Categories: math.FA (primary); math.FA; math-ph; quant-ph
- Links: abs=https://arxiv.org/abs/2602.12729v1  pdf=https://arxiv.org/pdf/2602.12729v1.pdf

Abstract:
We introduce a real-parameter refinement of the classical integer hierarchies underlying Schmidt number, block-positivity, and $k$-positivity for maps between matrix algebras. Starting from a compact family of $α$-admissible unit vectors ($α\in[1,d]$), we define closed cones $\mathsf K_α$ of bipartite positive operators that interpolate strictly between successive Schmidt-number cones, together with their dual witness cones. Via the Choi--Jamiołkowski correspondence this yields a matching filtration of map cones $\mathsf P_α$, recovering the usual $k$-positive/$k$-superpositive classes at integer parameters and complete positivity at the top endpoint.   Two results show that the fractional levels capture genuinely new structure. First, we prove a \emph{fractional Kraus theorem}: $α$-superpositive maps are precisely the completely positive maps admitting a Kraus decomposition whose Kraus operators satisfy an explicit singular-value (Ky--Fan) constraint, extending the classical rank-$k$ characterization. Second, for non-integer $α$ the cones $\mathsf P_α$ fail stability under CP post-composition, highlighting a sharp structural transition away from the integer theory. Finally, we derive sharp thresholds on canonical symmetric families (including the depolarizing ray and the isotropic slice), turning familiar stepwise criteria into continuous, computable profiles.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13050v1
- Title: Topology of the Fermi surface and universality of the metal-metal and metal-insulator transitions: $d$-dimensional Hatsugai-Kohmoto model as an example
- Authors: Gennady Y. Chitov
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.stat-mech; quant-ph
- Links: abs=https://arxiv.org/abs/2602.13050v1  pdf=https://arxiv.org/pdf/2602.13050v1.pdf

Abstract:
The earlier theory [1] of the quantum phase transitions related to the change of the Fermi Surface Topology (FST) is advanced. For such transitions the Fermi surface as a quantum critical manifold determined by the Lee-Yang zeros, the order parameter $\mathcal{P}$ as the $d$-volume of the Fermi sea, and the special FST universality class were introduced in [1]. The exactly solvable Hatsugai-Kohmoto (HK) $d$-dimensional ($d=1,2,3$) model of interacting fermions is analyzed. We explore the relation between the Lee-Yang zeros, the Luttinger and the plateau (Oshikawa) theorems. The validity of the Luttinger theorem in the HK model is confirmed. It is shown that the order parameter $\mathcal{P}$ and the FST universality class describe the transitions between metal and band/Mott insulators, as well as the Lifshitz and van Hove gapless-to-gapless transitions. The gapless phases are established to be the Landau Fermi liquids (metals). In addition to the conventional paradigm with a continuous order parameter, we apply the homology theory to analyze the FST transitions. They are critical points of the Morse function. To quantify FST we use the Euler characteristic, which is calculated for each phase of the HK model. We claim that the FST universality class is robust with respect to interactions and other model details, under the condition that the critical points are non-degenerate.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13060v1
- Title: Quantitative imaging of Abrikosov vortices by scanning quantum magnetometry
- Authors: Clemens Schäfermeier, Ankit Sharma, Christopher Kelvin von Grundherr, Andrea Morales, Jan Rhensius, Gabriel Puebla-Hellmann, Mirko Bacani
- Categories: cond-mat.supr-con (primary); cond-mat.supr-con; physics.ins-det; quant-ph
- Links: abs=https://arxiv.org/abs/2602.13060v1  pdf=https://arxiv.org/pdf/2602.13060v1.pdf

Abstract:
Understanding vortex matter in type-II superconductors is central to controlling dissipation and flux pinning in superconducting materials and devices. Here, we use cryogenic scanning nitrogen vacancy magnetometry (NVM) to image Abrikosov vortices in the cuprate superconductors BSCCO-2212 and YBCO under controlled field-cooled conditions. Measurements, which are performed using continuous-wave optically detected magnetic resonance (cw-ODMR) in a closed-cycle cryostat, yield quantitative magnetic-field maps with nanoscale spatial resolution. In BSCCO-2212 at 71 K, we resolve a well-ordered triangular vortex lattice, whose symmetry and spacing are confirmed through 2D Fourier analysis and are consistent with flux quantization. YBCO thin films imaged at 3 K exhibit a more disordered vortex arrangement reflecting stronger pinning, while maintaining quantitative agreement between measured vortex density and the applied magnetic field. These results render our cryogenic scanning NVM a reliable quantitative tool for real-space studies of vortices in high-$T_c$ superconductors, in particular since such a remarkable magnetic resolution has been achieved within relatively short acquisition times of 2 to 4 h.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13147v1
- Title: Non-chiral ephemeral edge states and cascading of exceptional points in the non-reciprocal Haldane model
- Authors: Aditi A. Prabhudesai, H. S. Chhabra, Suraj S. Hegde
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; quant-ph
- Links: abs=https://arxiv.org/abs/2602.13147v1  pdf=https://arxiv.org/pdf/2602.13147v1.pdf

Abstract:
We study a variant of the Haldane honeycomb model that has non-reciprocal hoppings between the next-nearest neighbours. The system on a torus hosts time-reversal symmetry protected exceptional rings(ER) in the spectrum. The ERs act as Berry-curvature flux tubes i.e the Berry curvature is non-zero only inside the ERs. The system on a cylinder having zig-zag boundaries (and transverse momentum $k_x$) hosts edge-states that have zero group velocity at $k_x=π$ and are therefore `non-chiral'. The edge states undergo a bifurcation transition at an exceptional point(EP)in the BZ and delocalise into the bulk. As the non-reciprocity is increased, the bulk states that are approaching each other are converted into pairs of EPs due to non-Hermiticity. As the non-reciprocity is further increased, there is a `Russian doll'-like nested proliferation of pairs of EPs, leading to an EP-cascade. The proliferation of EPs takes place only at specific values of the non-hermiticity parameter, leading to a step-like structure in the EP-pair density when plotted as a function of non-Hermiticity. Further, using wave packet dynamics, we find a tunable regime where the non-chiral edge states can be dynamically stabilised for large timescales. The `self-acceleration' term in the equations of motion tends to diffuse the wave packets into the bulk, thus making them `ephemeral edge states'. But we find that for small non-hermiticity, the edge localisation is stabilised until late times for sufficiently wider wave packets. Thus, we have brought forth an intriguing phenomenology of the exceptional phase of the non-reciprocal Haldane model, which may bear direct relevance for systems such as disordered Kitaev honeycomb model, wherein such ERs have been predicted.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2602.13192v1
- Title: Matter-induced plaquette terms in a $\mathbb{Z}_2$ lattice gauge theory
- Authors: Matjaž Kebrič, Fabian Döschl, Umberto Borla, Jad C. Halimeh, Ulrich Schollwöck, Annabelle Bohrdt, Fabian Grusdt
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; cond-mat.str-el; hep-lat; quant-ph
- Links: abs=https://arxiv.org/abs/2602.13192v1  pdf=https://arxiv.org/pdf/2602.13192v1.pdf

Abstract:
Lattice gauge theories (LGTs) provide a powerful framework for studying confinement, topological order, and exotic quantum matter. In particular, the paradigmatic phenomenon of confinement, where dynamical matter is coupled to gauge fields and forms bound states, remains an open problem. In addition, LGTs can provide low-energy descriptions of quantum spin liquids, which is the focus of ongoing experimental research. However, the study of LGTs is often limited theoretically by their numerical complexity and experimentally in implementing challenging multi-body interactions, such as the plaquette terms crucial for the realization of many exotic phases of matter. Here we investigate a $(2+1)$D $\mathbb{Z}_2$ LGT coupled to hard-core bosonic matter featuring a global U(1) symmetry, and show that dynamical matter naturally induces sizable plaquette interactions even in the absence of explicit plaquette terms in the Hamiltonian. Using a combination of density matrix renormalization group simulations and neural quantum state calculations up to a system size of $20 \times 20$, we analyze the model across different fillings and electric field strengths. At small coupling strength, we find a large plaquette expectation value, independent of system size, for a wide range of fillings, which decreases in the presence of stronger electric fields. Furthermore, we observe signatures of a confinement-deconfinement transition at weak coupling strengths. Our results demonstrate that dynamical U(1) matter can induce complex multi-body interactions, suggesting a natural route to the realization of strong plaquette terms and paving the way for realizing a topological quantum spin liquid protected by a large gap.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2407.06006v2
- Title: Heisenberg-limited Bayesian phase estimation with low-depth digital quantum circuits
- Authors: Su Direkci, Ran Finkelstein, Manuel Endres, Tuvia Gefen
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2407.06006v2  pdf=https://arxiv.org/pdf/2407.06006v2.pdf

Abstract:
Optimal phase estimation protocols require complex state preparation and readout schemes, generally unavailable or unscalable in many quantum platforms. We develop and analyze a scheme that achieves near-optimal precision up to a constant overhead for Bayesian phase estimation, using simple digital quantum circuits with depths scaling logarithmically with the number of qubits. We find that for Gaussian prior phase distributions with arbitrary widths, the optimal initial state can be approximated with products of Greenberger-Horne-Zeilinger states with varying number of qubits. Using local, adaptive measurements optimized for the prior distribution and the initial state, we show that Heisenberg scaling is achievable and that the proposed scheme outperforms known schemes in the literature that utilize a similar set of initial states. For an example prior width, we present a detailed comparison and find that is also possible to achieve Heisenberg scaling with a scheme that employs non-adaptive measurements, with the right allocation of copies per GHZ state and single-qubit rotations. We also propose an efficient phase unwinding protocol to extend the dynamic range of the proposed scheme, and show that it outperforms existing protocols by achieving an enhanced precision with a smaller number of additional atoms. Lastly, we discuss the impact of noise and imperfect gates.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2408.07067v3
- Title: Asymptotic quantification of entanglement with a single copy
- Authors: Ludovico Lami, Mario Berta, Bartosz Regula
- Categories: quant-ph (primary); quant-ph; cs.IT; math-ph
- Links: abs=https://arxiv.org/abs/2408.07067v3  pdf=https://arxiv.org/pdf/2408.07067v3.pdf

Abstract:
Despite the central importance of quantum entanglement in quantum technologies, the understanding of the optimal ways to exploit it is still beyond our reach, and even measuring entanglement in an operationally meaningful way is prohibitively difficult. Here we study two fundamental tasks in the processing of entanglement: entanglement testing, which is a quantum state discrimination problem concerned with entanglement detection in the many-copy regime, and entanglement distillation, concerned with purifying entanglement from noisy entangled states. We introduce a way of benchmarking the performance of distillation that focuses on the best achievable error rather than its yield in the asymptotic limit. When the underlying set of operations used for entanglement distillation is the axiomatic class of non-entangling operations, we show that the two figures of merit for entanglement testing and distillation coincide. We solve both problems by proving a generalised quantum Sanov's theorem, enabling the exact evaluation of asymptotic error rates of composite quantum hypothesis testing. We show in particular that the asymptotic figure of merit is given by the reverse relative entropy of entanglement, a single-letter quantity that can be evaluated using only a single copy of a quantum state -- a distinct feature among measures of entanglement that quantify the optimal performance of information-theoretic tasks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2503.03838v3
- Title: Quantum metasurfaces as probes of vacuum particle content
- Authors: Germain Tobar, Joshua Foo, Sofia Qvarfort, Fabio Costa, Rivka Bekenstein, Magdalena Zych
- Categories: quant-ph (primary); quant-ph; gr-qc
- Links: abs=https://arxiv.org/abs/2503.03838v3  pdf=https://arxiv.org/pdf/2503.03838v3.pdf

Abstract:
The quantum vacuum of the electromagnetic field is inherently entangled across distinct spatial sub-regions resulting in entangled particle content across these sub-regions. However accessing this particle content in a controlled laboratory experiment has remained out of experimental reach. Here we propose to overcome this challenge with a quantum mirror made from a two-dimensional sub-wavelength array of atoms that divides a photonic cavity. The array response to light is tunable between transmissive and reflective states by a control atom that is excited to a Rydberg state. We find that vacuum photon content from non-perturbative changes of the boundary conditions and therefore distinct spatial sub regions of the vacuum causes subtle frequency shifts that are accessible to sub-wavelength atom array platforms. This novel approach for probing vacuum particle content stems from the unique ability to create coherent dynamics of superpositions of transmissive and reflective states providing a quantum enhanced platform for observing vacuum particle creation from highly non-perturbative boundary condition changes of the electromagnetic field vacuum.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2505.20042v2
- Title: Quasi-Adiabatic Processing of Thermal States
- Authors: Reinis Irmejs, Mari Carmen Bañuls, J. Ignacio Cirac
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2505.20042v2  pdf=https://arxiv.org/pdf/2505.20042v2.pdf

Abstract:
We investigate the performance of an adiabatic evolution protocol when initialized from a Gibbs state at finite temperature. Specifically, we identify the diagonality of the final state in the energy eigenbasis, as well as the difference in energy and in energy variance with respect to the ideal adiabatic limit as key benchmarks for success and introduce metrics to quantify the off-diagonal contributions. Provided these benchmarks converge to their ideal adiabatic values, we argue that thermal expectation values of observables can be recovered, in accordance with the eigenstate thermalization hypothesis. For the transverse-field Ising model, we analytically establish that these benchmarks converge polynomially in both the quasi-adiabatic evolution time $T$ and system size. We perform numerical studies on non-integrable systems and find close quantitative agreement for the off-diagonality metrics, along with qualitatively similar behavior in the energy convergence.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2506.09555v3
- Title: More entropy from shorter experiments using polytope approximations to the quantum set
- Authors: Hyejung H. Jee, Florian J. Curchod, Mafalda L. Almeida
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2506.09555v3  pdf=https://arxiv.org/pdf/2506.09555v3.pdf

Abstract:
We introduce a systematic method for constructing polytope approximations to the quantum set in a variety of device-independent quantum random number generation (DI-QRNG) protocols. Our approach relies on two general-purpose algorithms that iteratively refine an initial outer-polytope approximation, guided by typical device behaviour and cryptographic intuition. These refinements strike a balance between computational tractability and approximation effectiveness. By integrating these approximations into the probability estimation (PE) framework [Zhang et al., PRA 2018], we obtain significantly improved certified entropy bounds in the finite-size regime. We test our method on various bipartite and tripartite DI-QRNG protocols, using both simulated and experimental data. In all cases, it yields notably higher entropy rates with fewer device uses than the existing techniques. We further extend our analysis to the more demanding task of randomness amplification, demonstrating major performance gains without added complexity. These results offer an effective and ready-to-use method to prove security-with improved certified entropy rates-in the most common practical DI-QRNG protocols. Our algorithms and entropy certification with PE tools are publicly available under a non-commercial license at https://github.com/CQCL/PE_polytope_approximation.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2506.09576v2
- Title: Real-time adaptive tracking of fluctuating relaxation rates in superconducting qubits
- Authors: Fabrizio Berritta, Jacob Benestad, Jan A. Krzywda, Oswin Krause, Malthe A. Marciniak, Svend Krøjer, Christopher W. Warren, Emil Hogedal, et al.
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall
- Links: abs=https://arxiv.org/abs/2506.09576v2  pdf=https://arxiv.org/pdf/2506.09576v2.pdf

Abstract:
The fidelity of operations on a solid-state quantum processor is fundamentally bounded by environmental decoherence. Characterizing environmental fluctuations is challenging because the acquisition time of nonadaptive experimental protocols limits temporal precision and can average out rapid features of the underlying dynamics. Here, we overcome this temporal-resolution limit by two orders of magnitude using a field-programmable gate-array (FPGA) powered classical controller that adaptively and continuously tracks the relaxation-time fluctuations of two fixed-frequency superconducting transmon qubits, which exhibit average relaxation times of approximately 0.17 ms and occasionally exceed 0.5 ms. We report events in which the relaxation time switches by nearly an order of magnitude over timescales of just tens of milliseconds, rather than minutes or hours as previously reported. Our real-time Bayesian estimation protocol estimates relaxation times within a few milliseconds, close to the decoherence timescale itself. Our statistical analysis further suggests that some of these fast fluctuations arise from two-level systems switching at rates up to 10 Hz, four orders of magnitude faster than earlier reports. These results redefine the timescales relevant for calibration in superconducting quantum processing units, establish a reference for rapid relaxation-rate characterization in device screening, and improve our understanding of fast relaxation dynamics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2507.00187v2
- Title: Optomechanical systems with linear and quadratic position couplings: Dynamics and optimal estimation
- Authors: Yaqing Xy Wang, Claudio Sanavio, József Zsolt Bernád
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2507.00187v2  pdf=https://arxiv.org/pdf/2507.00187v2.pdf

Abstract:
We study the dynamics of an optomechanical system consisting of a single-mode optical field coupled to a mechanical oscillator, where the nonlinear interaction includes both linear and quadratic terms in the oscillator's position. We present an analytical solution to this quantum-mechanical Hamiltonian problem by employing the formalism of two-phonon coherent states. Quantum estimation theory is applied to the resulting state of the optical field, with a focus on evaluating the quantum Fisher information with respect to the strength of the quadratic coupling. Our estimation scheme employs balanced homodyne photodetection and demonstrates that the corresponding classical Fisher information can reach the quantum Fisher information limit, with the phase of the local coherent oscillator playing a crucial role.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2507.17424v2
- Title: Universal properties of the many-body Lanczos algorithm at finite size
- Authors: Luca Capizzi, Leonardo Mazza, Sara Murciano
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech; hep-th
- Links: abs=https://arxiv.org/abs/2507.17424v2  pdf=https://arxiv.org/pdf/2507.17424v2.pdf

Abstract:
We study the universal properties of the Lanczos algorithm applied to finite-size many-body quantum systems. Focusing on autocorrelation functions of local operators and on their infinite-time behaviour at finite size, we conjecture that in the large $n$ limit, the ratios between consecutive Lanczos coefficients should have specific scalings with the size of the lattice that we make precise and that depend on the hydrodynamic tail of the autocorrelation function. The scaling associated with strong or approximate zero-modes is also discussed. We support our conjecture with a numerical study of different models.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2508.17273v2
- Title: A complete set of transformation rules for reversible circuits
- Authors: Shiguang Feng, Lvzhou Li
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2508.17273v2  pdf=https://arxiv.org/pdf/2508.17273v2.pdf

Abstract:
Reversible logic synthesis is a crucial component in quantum electronic design automation. While rule-based methodologies have gained prominence in reversible circuit optimization, the completeness of the transformation rule systems is a longstanding problem in this domain. In this work, we propose the first complete set of transformation rules for reversible circuits, comprising five fundamental rules: any two equivalent reversible circuits can be transformed into each other using the rules. To prove the completeness, a canonical circuit representation for reversible functions is introduced, and we show that every reversible function is computed by a unique reversible circuit in the canonical form, and any reversible circuit can be transformed into its canonical form by applying the rules.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2508.19726v2
- Title: Casimir-Lifshitz interaction between bodies integrated in a microelectromechanical/nanoelectromechanical quantum damped oscillator
- Authors: Yu. S. Barash
- Categories: quant-ph (primary); quant-ph; cond-mat.mes-hall; cond-mat.other
- Links: abs=https://arxiv.org/abs/2508.19726v2  pdf=https://arxiv.org/pdf/2508.19726v2.pdf

Abstract:
A theory is proposed for the component of the Casimir-like force that arises between bodies embedded in a macroscopic quantum damped oscillator. When the oscillator's parameters depend on the distance between the bodies, the oscillator-induced Casimir-like force is generally determined by a broad spectral range extending to high frequencies, limited by the frequency dispersion of the damping function. Here it is shown that there is a large class of systems in which the low-frequency range dominates the forces. This allows for the use of the Ohmic approximation, which is crucial for extending the theory to the lumped element description of fluctuation-induced forces in electrical circuits. Estimates of the circuit-induced Casimir-Lifshitz force suggest that under certain conditions it can be identified experimentally due to its dependence on various circuit elements.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.02620v2
- Title: Quantum aspects of the classical Maxwell's equations in free space from the perspective of the correspondence principle
- Authors: M. F. Araujo de Resende, Leonardo S. F. Santos, R. Albertini Silva
- Categories: quant-ph (primary); quant-ph; physics.class-ph
- Links: abs=https://arxiv.org/abs/2509.02620v2  pdf=https://arxiv.org/pdf/2509.02620v2.pdf

Abstract:
Due to the advent of Quantum Mechanics' 100th anniversary in 2025, we wrote this review paper in order to present a discussion that addresses the foundations of this theory. And since the creation of this Mechanics and other quantum theories was guided, for instance, by correspondence principles that needed to be identified between them and other well-established physical theories, this paper will be devoted to discussing the correspondence between these quantum theories and Maxwell's theory of electromagnetism. More precisely, what we will do throughout this paper is discuss how the Maxwell's electromagnetic theory in free space and the stronger formulation of the correspondence principle already pointed, together, to the basis of a Quantum Mechanics that was only be formulated half a century later. And, in order to make this very clear, we will show that the quantum-mechanical description of a photon can already be identified, simply, by manipulating Maxwell's equations in free space with mathematical resources that, for instance, were already well known before the advent of Quantum Mechanics.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.02795v2
- Title: Geodesics of Quantum Feature Maps on the Space of Quantum Operators
- Authors: Andrew Vlasic
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.02795v2  pdf=https://arxiv.org/pdf/2509.02795v2.pdf

Abstract:
This manuscript rigorously displays how the Riemannian structure of a point cloud--taking the manifold hypothesis--impacts the encoded subspace of quantum gates, exhibiting a direct effect of data on quantum circuits. Selecting a scheme to encode real-world data onto a quantum circuit, or quantum feature map, is an essential step in quantum machine learning. There have been many proposed encoding schemes and proposed techniques to test the efficacy of a map. However, very few techniques address how the data is 'deformed' when mapped to quantum state space--complex projective space--or the state of quantum operators--the Lie group of (special) unitary operators--and the potential downstream effects on an algorithm. This paper takes the assumption that a point cloud is a smooth Riemannian manifold and establishes a rigorous computational/theoretical framework to study how an encoding scheme deforms this geometry once mapped to the space of quantum operators, $\SU(2^N)$. Since the Riemannian manifold structure of the codomain of a quantum feature map has yet to be formalized, this rigorous framework is required to ensure the validity of analysis. Using a ground-up approach, we mathematically establish a Riemannian geometry for a general class of Hamiltonian quantum feature maps--which describes the vast majority of encoding methods--that are induced from a given Euclidean embedded manifold. We then establish analytic and computational tangible forms for curvature, volume, frames and coframes, and harmonic maps, which is the main tool for deformation analysis. Interestingly, the form of vector fields, and by extension, the form of covector fields, shows the interconnection between the change of a path on the real embedded manifold influences the change of a path in the respective subspace of special unitary operators, revealing the effect data has on a quantum circuit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.18033v2
- Title: Quantitative comparison of quantum pseudo-telepathy games and Bell inequalities
- Authors: Gábor Homa, András Bodor, József Zsolt Bernád
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2509.18033v2  pdf=https://arxiv.org/pdf/2509.18033v2.pdf

Abstract:
Quantum pseudo-telepathy games, such as the Mermin-Peres magic square and the doily game, theoretically allow players to win with unit probability when using entangled quantum strategies. We quantitatively characterize the quantum advantage in these games and compare it with violations of two Bell inequalities: the Clauser-Horne-Shimony-Holt and the Collins-Gisin inequalities. The analysis is restricted to two families of two-qubit states: modified Werner states and Bell-diagonal states. For each case, we identify and quantify the regions of quantum state space that exhibit either a quantum advantage or a Bell inequality violation, relative to the set of all entangled states. Within these families, the doily game captures a larger fraction of entangled states than the Mermin-Peres magic square game, though both are significantly more limited than the regions associated with Bell inequality violations. Although both approaches are fundamentally linked to quantum contextuality, our analysis of the examined two-qubit state families indicates that Bell inequalities are more effective at revealing entanglement, even if pseudo-telepathy games offer a more intuitive and conceptually appealing perspective.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.23875v2
- Title: Non-Abelian interference of topological edge states
- Authors: Shi Hu, Meiqing Hu, Zhoutao Lei
- Categories: quant-ph (primary); quant-ph; cond-mat.other
- Links: abs=https://arxiv.org/abs/2509.23875v2  pdf=https://arxiv.org/pdf/2509.23875v2.pdf

Abstract:
Topological boundary states exhibit distinctive properties, including unidirectional propagation and noise robustness, which hold significant potential for advancing the performance of quantum science and technology. Here, we demonstrate the implementation of non-Abelian quantum interference and entanglement generation, protected by dual symmetries (time-independent inversion and time-dependent interchain), in coupled Su-Schrieffer-Heeger chains. Specifically, in a multichain system, we first achieve tunable topological transfer of a single particle, where the destination chain is selected by the permutation sequence. We then extend this to two particles, observing a non-Abelian Hong-Ou-Mandel interference that generates spatially entangled NOON states whose properties are dictated by the permutation sequence. Our work establishes an alternative pathway for exploring non-Abelian topology applied to quantum science and technology, enabled by the unique protection of time-dependent symmetry.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.26135v3
- Title: Progress in the study of the (non)existence of genuinely unextendible product bases
- Authors: Maciej Demianowicz
- Categories: quant-ph (primary); quant-ph; math.CO
- Links: abs=https://arxiv.org/abs/2509.26135v3  pdf=https://arxiv.org/pdf/2509.26135v3.pdf

Abstract:
We investigate the open problem of the existence of genuinely unextendible product bases (GUPBs), that is, multipartite unextendible product bases (UPBs) which remain unextendible even with respect to biproduct vectors across all bipartitions of the parties. To this end, we exploit the well-known connection between UPBs and graph theory through orthogonality graphs and orthogonal representations, together with recent progress in this framework, and employ forbidden induced subgraph characterizations to single out the admissible local orthogonality graphs for GUPBs. Using this approach, we establish that GUPBs of size thirteen in three-qutrit systems-the smallest candidate GUPBs-do not exist. We further provide a partial characterization of graphs relevant to larger bases and systems with ququart subsystems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2510.14905v2
- Title: Continuous-time quantum walk on a random graph using quantum circuits
- Authors: Sabyasachi Chakraborty, Rohit Sarma Sarkar, Sonjoy Majumder, Rohit Kishan Ray
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.14905v2  pdf=https://arxiv.org/pdf/2510.14905v2.pdf

Abstract:
Quantum-circuit implementations of continuous-time quantum walks (CTQWs) can provide an efficient route to model graph-based algorithms. However, constructing circuits that faithfully reproduce CTQW dynamics across arbitrary graphs remains a major challenge. In this work, we introduce a Laplacian partitioning algorithm (LPA) that enables an efficient and scalable quantum-circuit realization of CTQWs on random graphs. A common algorithm to simulate a general graph (of size $N = 2^n$ for $n$ qubits) on a quantum circuit is based on Pauli decomposition of the graph Hamiltonian, which can yield $O(4^n)$ terms, and require $O(N^2\log N)$ time for coefficient computation. In contrast, our LPA uses $O(2^n)$ terms, in $O(N^2)$ time. Our circuit provides a graph-agnostic framework for CTQWs, implemented via a Trotter-Suzuki product formula and confirming error scaling consistent with theoretical Trotter error bounds. To further test the circuit performance, we study the localization behavior of the CTQW. In our case, localization originates from Laplacian spectral degeneracies rather than disorder (Anderson-type), and our circuit faithfully reproduces these localization phenomena and spectral structure for a random graphs with high accuracy.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2510.20885v2
- Title: Picosecond Wireless Synchronization with Entangled Photons via Grid-Based Quantum Coverage in Indoor Optical Systems
- Authors: Hossein Safi, Mohammad Taghi Dabiri, Mazen Hasna, Iman Tavakkolnia, Harald Haas
- Categories: quant-ph (primary); quant-ph; physics.optics
- Links: abs=https://arxiv.org/abs/2510.20885v2  pdf=https://arxiv.org/pdf/2510.20885v2.pdf

Abstract:
In this paper, we present a robust entanglement-assisted synchronization framework for indoor optical wireless systems that explicitly captures the coupling between spatial beam geometry and temporal synchronization accuracy. Unlike conventional approaches that treat beam steering and timing estimation independently, a unified spatio temporal model is developed that links user position uncertainty to the Cramer Rao lower bound of the synchronization error. The framework incorporates key physical impairments, including multipath dispersion, non Gaussian detector jitter, and spatially correlated localization errors. Through analytical modeling and extensive simulations, we show that the proposed system exhibits graceful performance degradation under heavy tailed positioning uncertainty and remains stable in the presence of multipath induced bias. Using realistic single photon detector parameters, the results indicate that synchronization accuracy below $10$ picoseconds can be maintained across a wide range of operating conditions. This level of precision provides a scalable foundation for quantum enabled indoor wireless networks.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2510.24082v2
- Title: Exploring the Fidelity of Flux Qubit Measurement in Different Bases via Quantum Flux Parametron
- Authors: Yanjun Ji, Susanna Kirchhoff, Frank K. Wilhelm
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2510.24082v2  pdf=https://arxiv.org/pdf/2510.24082v2.pdf

Abstract:
High-fidelity qubit readout is a fundamental requirement for practical quantum computing systems. In this work, we investigate methods to enhance the measurement fidelity of flux qubits via a quantum flux parametron-mediated readout scheme. Through theoretical modeling and numerical simulations, we analyze the impact of different measurement bases on fidelity in single-qubit and coupled two-qubit systems. For single-qubit systems, we show that energy bases consistently outperform flux bases in achieving higher fidelity. In coupled two-qubit systems, we explore two measurement models: sequential and simultaneous measurements, both aimed at reading out a single target qubit. Our results indicate that the highest fidelity can be achieved either by performing sequential measurement in a dressed basis over a longer duration or by conducting simultaneous measurement in a bare basis over a shorter duration. Importantly, the sequential measurement model consistently yields more robust and higher fidelity readouts compared to the simultaneous approach. These findings quantify achievable fidelities and provide valuable guidance for optimizing measurement protocols in emerging quantum computing architectures.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2511.12799v3
- Title: When does numerical pulse optimization actually help? Error budgets,robustness tradeoffs, and calibration guidance for transmon single-qubit gates
- Authors: Rylan Malarchick
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.12799v3  pdf=https://arxiv.org/pdf/2511.12799v3.pdf

Abstract:
Numerical optimal control (GRAPE) can in principle discover pulse shapes that suppress all coherent gate error to machine precision. But when does that capability actually matter? We present a systematic comparison of Gaussian, DRAG, and GRAPE pulses for single-qubit gates on a three-level transmon model parameterized by IQM Garnet hardware ($T_1 = 37\,μ$s, $T_2 = 9.6\,μ$s,$α/2π= -200$ MHz), with the explicit goal of identifying the regimes where numerical optimization provides genuine practical advantage over analytical methods.   Our central finding is that properly calibrated DRAG already operates near the decoherence floor. At 20 ns gate time, GRAPE eliminates all coherent error ($1 - F < 10^{-15}$), but DRAG achieves $1 - F = 4.9 \times 10^{-4}$ in coherent error alone,and $8.4 \times 10^{-4}$ under full decoherence -- only $1.2\times$ above GRAPE's decoherence-limited performance. More surprisingly,DRAG is \emph{more robust} than GRAPE to qubit frequency detuning (minimum fidelity 0.990 vs.\ 0.931 over $\pm 5$ MHz), the dominant calibration uncertainty in charge-noise-limited transmons. GRAPE retains superior amplitude robustness (minimum fidelity 0.994 vs.\ 0.990) and provides the only route to guaranteed zero coherent error, which matters at short gate times ($\lesssim 15$ ns) where perturbative corrections break down.   These results lead to concrete calibration guidance: (1) properly calibrated DRAG is sufficient for gate times $\gtrsim 20$ ns on hardware with $T_2/T \gtrsim 500$, (2) GRAPE is necessary at short gate times or when targeting error rates well below the decoherence floor, and (3) robust optimal control incorporating frequency uncertainty should be used when detuning is the dominant noise source. We decompose the full error budget (coherent, $T_1$, $T_2$, control noise) and provide the open-source QubitPulseOpt framework for reproducing all results.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2511.16855v2
- Title: Orthogonal frequency-division multiplexing for simultaneous gate operations on multiple qubits via a shared control line
- Authors: Haruki Mitarai, Yukihiro Tadokoro, Hiroya Tanaka
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.16855v2  pdf=https://arxiv.org/pdf/2511.16855v2.pdf

Abstract:
The increasing number of qubits in quantum processors necessitates a corresponding increase in the number of control lines between the processor, which is typically operated at cryogenic temperatures, and external electronics. Scaling poses significant challenges in terms of the thermal loads, forming a major bottleneck in the realization of large-scale quantum computers. In this study, we analyze simultaneous gate operations on multiple qubits using microwaves transmitted via a single cable in a frequency-division multiplexing (FDM) scheme. By employing rectangular control microwave pulses, we reveal the contribution of drive frequency spacing to gate fidelity. Through theoretical and numerical analyses, we demonstrate that orthogonal and quasi-orthogonal microwave signals suppress interference in simultaneously driven qubits, thereby ensuring high gate fidelity. Additionally, we provide design guidelines for key parameters, including pulse length, number of multiplexed microwave signals, and rotation angle, to achieve precise qubit operations. Our findings enable a scalable FDM-based microwave control scheme suitable for quantum processors with a large number of qubits.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2511.21502v2
- Title: Modeling dissipation in quantum active matter
- Authors: Alexander P. Antonov, Sangyun Lee, Benno Liebchen, Hartmut Löwen, Jannis Melles, Giovanna Morigi, Yehor Tuchkov, Michael te Vrugt
- Categories: quant-ph (primary); quant-ph; cond-mat.stat-mech
- Links: abs=https://arxiv.org/abs/2511.21502v2  pdf=https://arxiv.org/pdf/2511.21502v2.pdf

Abstract:
Active matter denotes a system of particles immersed in an external environment, from which the particles extract energy continuously in order to perform directed motion. Extending the paradigm of active matter to a quantum framework requires an appropriate description of the environment. In this work, we consider a driven quantum particle undergoing noise and dissipation, with external driving exhibiting characteristics of classical activity. We model the non-unitary dynamics with time-local master equations and analyze the particle motion at different time scales for different forms of the master equations, satisfying different criteria. We systematically compare predictions on the dynamics of particle trajectories and thereby we uncover how the particle motion evolves under the interplay of quantum effects, dissipation, and active-like dynamics. These results are essential for guiding possible experiments aimed at realizing quantum analogues of classical active systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2511.23237v2
- Title: Systems that saturate the Margolus-Levitin quantum speed limit
- Authors: Ole Sönnerborn
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2511.23237v2  pdf=https://arxiv.org/pdf/2511.23237v2.pdf

Abstract:
We provide a complete characterization of all finite-dimensional quantum systems that saturate the Margolus-Levitin quantum speed limit at arbitrary Uhlmann-Jozsa fidelity. Employing a purification-based approach, we prove that mixed-state saturation occurs precisely when three structural criteria are fulfilled: the state's support is confined to the sum of two energy eigenspaces (the ground level and a single excited level); each eigenvector of the state with nonzero weight is a fixed superposition of one ground- and one excited-state energy eigenvector (determined by the minimizer of the objective function identified by Giovannetti et al.) and all such eigenvectors evolve in mutually orthogonal subspaces. These requirements impose a strict rank bound, ruling out saturation by any faithful state. For quantum bits, we derive a purity-resolved and tight Margolus-Levitin bound that reduces to the pure-state result in the limit of unit purity. Through a time-reversal argument, we further extend the dual Margolus-Levitin quantum speed limit to mixed states and establish the corresponding saturation conditions.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2512.06260v2
- Title: Trade-offs between Quantum and Classical Resources in the Linear Combination of Unitaries
- Authors: Kaito Wada, Hiroyuki Harada, Yasunari Suzuki, Yuuki Tokunaga, Naoki Yamamoto, Suguru Endo
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.06260v2  pdf=https://arxiv.org/pdf/2512.06260v2.pdf

Abstract:
The randomized linear combination of unitaries (LCU) method with many applications to early fault-tolerant quantum computing algorithms has been proposed. This quantum algorithm computes the same expectation values as the original, fully coherent LCU algorithm using a shallower quantum circuit with a single ancilla qubit, at the cost of a quadratically larger sampling overhead. In this work, we propose a quantum algorithm intermediate between the original and randomized LCU that manages the trade-off between the sampling overhead and circuit complexity. Our algorithm divides the set of unitary operators into several groups and then randomly samples LCU circuits from these groups to evaluate the target expectation value. Notably, we reveal that across all grouping strategies, the mechanism of the sampling overhead reduction can be solely characterized by a metric we call the reduction factor. Moreover, we analytically prove an underlying monotonicity of the reduction factor in the group size: larger group sizes entail smaller sampling overhead. Finally, our framework enables a more flexible algorithmic design by systematically yielding intermediate implementations of LCU-based algorithms; we provide intermediate implementations of non-Hermitian dynamics simulation, ground-state property estimation, and quantum error detection. Besides, we demonstrate this principle by deriving intermediate trade-off scaling in sample complexity and ancillary space for quantum linear system solver.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2512.08687v2
- Title: Non-Hermitian symmetry breaking and Lee-Yang theory for quantum XYZ and clock models
- Authors: Tian-Yi Gu, Gaoyong Sun
- Categories: quant-ph (primary); quant-ph
- Links: abs=https://arxiv.org/abs/2512.08687v2  pdf=https://arxiv.org/pdf/2512.08687v2.pdf

Abstract:
Lee-Yang theory offers a unifying framework for understanding classical phase transitions and dynamical quantum phase transitions through the analysis of partition functions and Loschmidt echoes. Recently, this framework is extended to characterize quantum phase transitions of quantum Ising models by introducing the concepts of non-Hermitian parity-symmetry breaking and fidelity zeros. Here, we generalize the theory by studying a broad class of quantum models, including the XY, the XXZ, the XYZ, and the $\mathbb{Z}_p$ clock models in one dimension, subject to a complex magnetic field. For the XY, XXZ and XYZ models, we find that the complex field breaks parity symmetry and induces oscillations of the ground state between the two parity sectors, giving rise to fidelity zeros within the ordered phases. For the $\mathbb{Z}_3$ clock model, the complex field splits the real part of the ground-state energy between the neutral sector ($q=0$) and the charged sectors ($q=1,2$), while preserving the degeneracy within the charged sector. Fidelity zeros arise only after projecting out one of the charged sectors. In contrast, for the $\mathbb{Z}_4$ clock model, the ground state oscillates between the neutral sector ($q=0$) and the charged sector ($q=2$), which directly gives rise to fidelity zeros. Finite-size scaling of these zeros yields critical exponents in full agreement with analytical predictions, demonstrating that this approach is applicable not only to the Ising model with $\mathbb{Z}_2$ symmetry, but also to more general Heisenberg-type models and systems with higher discrete symmetries.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2512.11613v2
- Title: Boltzmann to Lindblad: Classical and Quantum Approaches to Out-of-Equilibrium Statistical Mechanics
- Authors: Stefano Giordano, Giuseppe Florio, Giuseppe Puglisi, Fabrizio Cleri, Ralf Blossey
- Categories: quant-ph (primary); quant-ph; math-ph
- Links: abs=https://arxiv.org/abs/2512.11613v2  pdf=https://arxiv.org/pdf/2512.11613v2.pdf

Abstract:
Open quantum systems play a central role in contemporary nanoscale technologies, including molecular electronics, quantum heat engines, quantum computation and information processing. A major theoretical challenge is to construct dynamical models that are simultaneously consistent with classical thermodynamics and complete positivity. In this work, we develop a framework that addresses this issue by extending classical stochastic dynamics to the quantum domain. We begin by formulating a generalized Langevin equation in which both friction and noise act symmetrically on the two Hamiltonian equations. From this, we derive a generalized Klein-Kramers equation expressed in terms of Poisson brackets, and we show that it admits the Boltzmann distribution as its stationary solution while satisfying the first and second laws of thermodynamics along individual trajectories. Applying canonical quantization to this classical framework yields two distinct quantum master equations, depending on whether the friction operators are taken to be Hermitian or non-Hermitian. By analyzing the dynamics of a harmonic oscillator, we determine the conditions under which these equations reduce to a Lindblad-type generator. Our results demonstrate that complete positivity is ensured only when friction and noise are included in both Hamiltonian equations, thus fully justifying the classical construction. Moreover, we find that the friction coefficients must satisfy the same positivity condition in both the Hermitian and non-Hermitian formulations, revealing a form of universality that transcends the specific operator representation. The formalism offers a versatile tool for deriving quantum versions of the thermodynamic laws and is directly applicable to a wide class of nonequilibrium nanoscale systems.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 1906.00641v2
- Title: Perturbative calculation of field space entanglement entropy
- Authors: James Brister
- Categories: hep-th (primary); hep-th; quant-ph
- Links: abs=https://arxiv.org/abs/1906.00641v2  pdf=https://arxiv.org/pdf/1906.00641v2.pdf

Abstract:
We present a general method for the perturbative calculation of the entanglement entropy between two interacting quantum fields. Previous attempts at calculating this quantity perturbatively have encountered a seemingly pathological divergence; we explain why this divergence is a result of improperly truncating a series expansion and give a prescription for avoiding this problem. We then apply our method to a simple example of two mass-mixing scalar fields.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2403.01903v4
- Title: Online Locality Meets Distributed Quantum Computing
- Authors: Amirreza Akbari, Xavier Coiteux-Roy, Francesco d'Amore, François Le Gall, Henrik Lievonen, Darya Melnyk, Augusto Modanese, Shreyas Pai, et al.
- Categories: cs.DC (primary); cs.DC; cs.CC; math.PR; quant-ph
- Links: abs=https://arxiv.org/abs/2403.01903v4  pdf=https://arxiv.org/pdf/2403.01903v4.pdf

Abstract:
We connect three distinct lines of research that have recently explored extensions of the classical LOCAL model of distributed computing: A. distributed quantum computing and non-signaling distributions [e.g. STOC 2024], B. finitely-dependent processes [e.g. Forum Math. Pi 2016], and C. locality in online graph algorithms and dynamic graph algorithms [e.g. ICALP 2023].   We prove new results on the capabilities and limitations of all of these models of computing, for locally checkable labeling problems (LCLs). We show that all these settings can be sandwiched between the classical LOCAL model and what we call the randomized online-LOCAL model. Our work implies limitations on the quantum advantage in the distributed setting, and we also exhibit a new barrier for proving tighter bounds. Our main technical results are these: 1. All LCL problems solvable with locality $O(\log^\star n)$ in the classical deterministic LOCAL model admit a finitely-dependent distribution with locality $O(1)$. This answers an open question by Holroyd [2024], and also presents a new barrier for proving bounds on distributed quantum advantage using causality-based arguments. 2. In rooted trees, if we can solve an LCL problem with locality $o(\log \log \log n)$ in the randomized online-LOCAL model (or any of the weaker models, such as quantum-LOCAL), we can solve it with locality $O(\log^\star n)$ in the classical deterministic LOCAL model. One of many implications is that in rooted trees, $O(\log^\star n)$ locality in quantum-LOCAL is not stronger than $O(\log^\star n)$ locality in classical LOCAL.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2410.14123v2
- Title: Generation of wave turbulence in dipolar gases driven across their phase transitions
- Authors: G. A. Bougas, K. Mukherjee, S. I. Mistakidis
- Categories: cond-mat.quant-gas (primary); cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2410.14123v2  pdf=https://arxiv.org/pdf/2410.14123v2.pdf

Abstract:
Ultracold quantum gases with long-range anisotropic interactions host novel exotic phases of matter, such as supersolids, exhibiting both rigid and superfluid characteristics. The impact of this interplay on the out-of-equilibrium dynamics of dipolar gases, and in particular its connection with universal turbulent behavior, remains highly unexplored. Here, upon considering a dipolar Bose-Einstein condensate of dysprosium atoms being dynamically driven across the supersolid-superfluid phase transition and vice versa, we unveil the emergence of a robust nonequilibrium quasi-steady state. This state displays self-similar momentum distributions exhibiting algebraic decay at large momenta, with scaling exponents supporting the existence of wave turbulence. We demonstrate that supersolidity sustaining higher-lying momenta, associated with the roton minimum, promotes the development of turbulence. Our results provide a stepping stone toward unraveling and exploiting turbulent and self-similar behavior in anisotropically long-range interacting quantum gases amenable in current experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2506.09141v4
- Title: The Role of Exceptional Points and Transmission Peak Degeneracies in Non-Hermitian Sensing
- Authors: Alexander S. Carney, Juan S. Salcedo-Gallo, Salil K. Bedkihal, Mattias Fitzpatrick
- Categories: physics.app-ph (primary); physics.app-ph; physics.optics; quant-ph
- Links: abs=https://arxiv.org/abs/2506.09141v4  pdf=https://arxiv.org/pdf/2506.09141v4.pdf

Abstract:
Transmission peak degeneracies (TPDs) have emerged as a promising alternative to exceptional points (EPs) for non-Hermitian sensing, providing square-root frequency splitting without the eigenbasis collapse and associated noise amplification that limit EP sensors. However, existing treatments of TPDs remain fragmented, lacking a unified theoretical framework, systematic figures of merit, or design principles for practical implementation. Here, we develop a comprehensive theory of two-dimensional TPDs that clarifies their relationship to EPs, maps their locations in parameter space, and provides analytic figures of merit for sensor design. We validate our theory using a tunable cavity-magnonics platform with in situ control of mode frequency, dissipation, and complex coupling via an effective synthetic gauge field. Our platform enables systematic exploration of six representative EP-TPD configurations spanning PT-symmetric, anti-PT-symmetric and anyonic-PT-symmetric regimes. Crucially, we show that TPDs, unlike EPs, retain square-root splitting even under nuisance parameter drift through generalized transmission extrema degeneracies (TEDs). We further identify specific robust TPD configurations that minimize the impact of nuisance drift. These findings establish a unified theoretical and experimental framework for TPD-based non-Hermitian sensing.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2507.02783v2
- Title: Uniform semiclassical observable error bound of Trotter-Suzuki splitting: a simple algebraic proof
- Authors: Di Fang, Conrad Qu
- Categories: math.NA (primary); math.NA; quant-ph
- Links: abs=https://arxiv.org/abs/2507.02783v2  pdf=https://arxiv.org/pdf/2507.02783v2.pdf

Abstract:
Efficient simulation of the semiclassical Schrödinger equation has garnered significant attention in the numerical analysis community. While controlling the error in the unitary evolution or the wavefunction typically requires the time step size to shrink as the semiclassical parameter $h$ decreases, it has been observed -- and proved for first- and second-order Trotterization schemes -- that the error in certain classes of observables admits a time step size independent of $h$. In this work, we explicitly characterize this class of observables and present a new, simple algebraic proof of uniform-in-$h$ error bounds for arbitrarily high-order Trotterization schemes. Our proof relies solely on the algebraic structure of the underlying operators in both the continuous and discrete settings. Unlike previous analyses, it avoids Egorov-type theorems and bypasses heavy semiclassical machinery. To our knowledge, this is the first proof of uniform-in-$h$ observable error bounds for Trotterization in the semiclassical regime that relies only on algebraic structure, without invoking the semiclassical limit.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2508.15897v2
- Title: Entanglement entropy as a probe of topological phase transitions
- Authors: Manish Kumar, Bharadwaj Vedula, Suhas Gangadharaiah, Auditya Sharma
- Categories: cond-mat.str-el (primary); cond-mat.str-el; cond-mat.dis-nn; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2508.15897v2  pdf=https://arxiv.org/pdf/2508.15897v2.pdf

Abstract:
Entanglement entropy (EE) provides a powerful probe of quantum phases, yet its role in identifying topological phase transitions in disordered systems remains underexplored. We introduce an exact EE-based framework that captures topological phase transitions even in the presence of disorder. Specifically, for a class of Su-Schrieffer-Heeger (SSH) model variants, we show that the difference in EE between half-filled and near-half-filled ground states, $ΔS^{\mathcal{A}}$, vanishes in the topological phase but remains finite in the trivial phase, a direct consequence of edge-state localization. This behavior persists even in the presence of quasiperiodic or binary disorder. By analyzing domain-wall configurations in the SSH chain, we further show how subsystem tuning allows one to distinguish genuine topological zero-energy eigenstates from trivial localized states. Exact phase boundaries, derived from Lyapunov exponents via transfer matrices, agree closely with numerical results from $ΔS^{\mathcal{A}}$ and the topological invariant $\mathcal{Q}$, with instances where $ΔS^{\mathcal{A}}$ outperforms $\mathcal{Q}$. Our results highlight EE as a robust diagnostic tool and a potential bridge between quantum information and condensed matter approaches to topological matter.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.00341v2
- Title: Solving Conic Programs over Sparse Graphs using a Variational Quantum Approach: The Case of the Optimal Power Flow
- Authors: Thinh Viet Le, Mark M. Wilde, Vassilis Kekatos
- Categories: eess.SY (primary); eess.SY; cs.LG; math.OC; quant-ph
- Links: abs=https://arxiv.org/abs/2509.00341v2  pdf=https://arxiv.org/pdf/2509.00341v2.pdf

Abstract:
Conic programs arise broadly in physics, quantum information, machine learning, and engineering, many of which are defined over sparse graphs. Although such problems can be solved in polynomial time using classical interior-point solvers, the computational complexity scales unfavorably with graph size. In this context, this work proposes a variational quantum paradigm for solving conic programs, including quadratically constrained quadratic programs (QCQPs) and semidefinite programs (SDPs). We encode primal variables via the state of a parameterized quantum circuit (PQC), and dual variables via the probability mass function of a second PQC. The Lagrangian function can thus be expressed as scaled expectations of quantum observables. A primal-dual solution can be found by minimizing/maximizing the Lagrangian over the parameters of the first/second PQC. We pursue saddle points of the Lagrangian in a hybrid fashion. Gradients of the Lagrangian are estimated using the two PQCs, while PQC parameters are updated classically using a primal-dual method. We propose permuting the primal variables so that related observables are expressed in a banded form, enabling efficient measurement. The proposed framework is applied to the OPF problem, a large-scale optimization problem central to the operation of electric power systems. Numerical tests on the IEEE 57-node power system using Pennylane's simulator corroborate that the proposed doubly variational quantum framework can find high-quality OPF solutions. Although showcased for the OPF, this framework features a broader scope, including conic programs with numerous variables and constraints, problems defined over sparse graphs, and training quantum machine learning models to satisfy constraints.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.03612v2
- Title: Universal Crossover in the Three-Channel Charge Kondo Model at High Transparency
- Authors: Nicolas Paris, Nicolas Dupuis, Christophe Mora
- Categories: cond-mat.mes-hall (primary); cond-mat.mes-hall; cond-mat.str-el; quant-ph
- Links: abs=https://arxiv.org/abs/2509.03612v2  pdf=https://arxiv.org/pdf/2509.03612v2.pdf

Abstract:
Quantum impurity models provide a central framework for correlated electron physics, with quantum dots enabling controlled experimental realizations. While their weak-coupling behavior is well understood through mappings to Kondo Hamiltonians, the opposite regime of highly transparent contacts has lacked a controlled theoretical description. Using the functional renormalization group (FRG), we resolve this regime for the three-channel charge Kondo device of Ref.~\cite{iftikhar2018}, benchmarking against conformal field theory by reproducing the universal zero-frequency conductance and, crucially, going beyond it to obtain the full frequency crossover of the conductance and the full temperature crossover of the impurity entropy, together with a continuous line of fixed points for interacting leads. These results establish FRG as a powerful nonperturbative tool for quantum impurity problems in regimes inaccessible to conventional approaches, with direct implications for mesoscopic experiments.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2509.04416v2
- Title: $^{171}$Yb Reference Data
- Authors: Ronen M. Kroeze, Sofus Laguna Kristensen, Sebastian Pucher
- Categories: physics.atom-ph (primary); physics.atom-ph; cond-mat.quant-gas; quant-ph
- Links: abs=https://arxiv.org/abs/2509.04416v2  pdf=https://arxiv.org/pdf/2509.04416v2.pdf

Abstract:
Ytterbium-171 is a versatile atomic species often used in quantum optics, precision metrology, and quantum computing. Consolidated atomic data is essential for the planning, execution, and evaluation of experiments. In this reference, we present physical and optical properties of neutral $^{171}$Yb relevant to these applications. We emphasize experimental results and supplement these with theoretical estimates. We present equations to convert values and derive important parameters. Tabulated results include key parameters for commonly used transitions in $^{171}$Yb (${}^1\mathrm{S}_0\rightarrow{}^1\mathrm{P}_1$, ${}^1\mathrm{S}_0\rightarrow{}^3\mathrm{P}_{0,1,2}\,$, ${}^3\mathrm{P}_{0,2}\rightarrow{}^3\mathrm{S}_1$, and ${}^3\mathrm{P}_0\rightarrow{}^3\mathrm{D}_1$). This dataset serves as an up-to-date reference for studies involving fermionic $^{171}$Yb.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2510.21767v2
- Title: Quantum-inspired space-time PDE solver and dynamic mode decomposition
- Authors: Raghavendra Dheeraj Peddinti, Stefano Pisoni, Narsimha Rapaka, Yacine Addad, Mohamed K. Riahi, Egor Tiunov, Leandro Aolita
- Categories: physics.comp-ph (primary); physics.comp-ph; math.NA; quant-ph
- Links: abs=https://arxiv.org/abs/2510.21767v2  pdf=https://arxiv.org/pdf/2510.21767v2.pdf

Abstract:
The curse of dimensionality is ubiquitous in both numerical and data-driven methods. This is particularly severe for space-time methods, which treat the combined space-time domain simultaneously. We investigate the effectiveness of a quantum-inspired approach in alleviating this curse, both for solving PDEs and making data-driven predictions. We achieve this goal by treating both spatial and temporal dimensions within a single matrix product state (MPS) encoding. First, we benchmark our MPS space-time solver for both linear and nonlinear PDEs, observing that the MPS ansatz accurately captures the underlying spatio-temporal correlations while having significantly fewer degrees of freedom. Second, we develop an MPS-DMD algorithm for accurate long-term predictions of nonlinear systems, with runtime scaling logarithmically with both spatial and temporal resolution. We also demonstrate an application where both methods can be combined for cheap and accurate prediction of long-term dynamics. This research highlights the role of tensor networks in developing effective, interpretable models that bridge the gap between numerical methods and data-driven approaches.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2510.23919v2
- Title: Thermal nature of confining strings
- Authors: Sebastian Grieninger, Dmitri E. Kharzeev, Eliana Marroquin
- Categories: hep-ph (primary); hep-ph; hep-lat; hep-th; nucl-th; quant-ph
- Links: abs=https://arxiv.org/abs/2510.23919v2  pdf=https://arxiv.org/pdf/2510.23919v2.pdf

Abstract:
We investigate the quantum statistical properties of the confining string connecting a static fermion-antifermion pair in the massive Schwinger model. By analyzing the reduced density matrix of the subsystem located in between the fermion and antifermion, we demonstrate that as the interfermion separation approaches the string-breaking distance, the overlap between the microscopic density matrix and an effective thermal density matrix exhibits a pronounced, narrow peak, approaching unity at the onset of string breaking. This behavior reveals that the confining flux tube evolves toward a genuinely thermal state as the separation between the charges grows, even in the absence of an external heat bath. In other words, one cannot tell whether a reduced state of the subsystem arises from a surrounding heat bath or from entanglement with the rest of the system. The entanglement spectrum near the critical string-breaking distance exhibits a rapid transition from the dominance of a single state describing the confining electric string towards a strongly entangled state containing virtual fermion-antifermion pairs. Our findings establish a quantitative link between confinement, entanglement, and emergent thermality, and suggest that string breaking corresponds to a microscopic thermalization transition within the flux tube.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

- Date (JST ingest): 2026-02-17 09:54
- arXiv: 2512.06630v2
- Title: Quantum Temporal Convolutional Neural Networks for Cross-Sectional Equity Return Prediction: A Comparative Benchmark Study
- Authors: Chi-Sheng Chen, Xinyu Zhang, En-Jui Kuo, Rong Fu, Qiuzhe Xie, Fan Zhang
- Categories: cs.LG (primary); cs.LG; quant-ph
- Links: abs=https://arxiv.org/abs/2512.06630v2  pdf=https://arxiv.org/pdf/2512.06630v2.pdf

Abstract:
Quantum machine learning offers a promising pathway for enhancing stock market prediction, particularly under complex, noisy, and highly dynamic financial environments. However, many classical forecasting models struggle with noisy input, regime shifts, and limited generalization capacity. To address these challenges, we propose a Quantum Temporal Convolutional Neural Network (QTCNN) that combines a classical temporal encoder with parameter-efficient quantum convolution circuits for cross-sectional equity return prediction. The temporal encoder extracts multi-scale patterns from sequential technical indicators, while the quantum processing leverages superposition and entanglement to enhance feature representation and suppress overfitting. We conduct a comprehensive benchmarking study on the JPX Tokyo Stock Exchange dataset and evaluate predictions through long-short portfolio construction using out-of-sample Sharpe ratio as the primary performance metric. QTCNN achieves a Sharpe ratio of 0.538, outperforming the best classical baseline by approximately 72\%. These results highlight the practical potential of quantum-enhanced forecasting model, QTCNN, for robust decision-making in quantitative finance.

Notes:
- Keywords (auto):
- Why it matters (auto):
- Related cluster (auto):

---

