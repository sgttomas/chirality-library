# Interrupted maintenance and exceptional custody

Use this resource when interrupted work must be recovered or an identified
operation requires exclusive custody. It supplements the owning repository's
instructions and actual assignment; it grants no authority and is not a Git
workflow. Ordinary uninterrupted maintenance needs no extra record or exercise.

Read current steering, owning work, actual Git/operation state and the review
record together. Establish source basis, usable partial work/result, applicable
checks, open conditions, next needed action and current authority. Inspect active
operations and uncommitted/ignored work before repeating a command whose
confirmation was lost. A failed check holds affected integration; repair within
scope, route it to its owner, or return a reserved decision. History alone does
not authorize restarting work. Keep at most one replaceable recovery note only
when the existing work and review record do not suffice.

For exceptional custody, name the holder, exact item, reserved operation,
authorized interruption resolver and release/transfer conditions in the existing
assignment or review record. Use an existing coordination or locking mechanism
and preserve last checked-in reader access. An acknowledged disjoint-write
reservation coordinates cooperating workers; it does not exclude another
process. If stronger exclusion is needed but unavailable, hold that operation
and expose the missing capability rather than claiming a lock.

On interruption, preserve partial work and establish active ownership before
resuming or transferring. The authorized maintainer decides the disposition;
silence or elapsed time grants no disposal authority. Record release or transfer
in the existing coordination record so the next worker can tell who may proceed,
and check retained work and reader access. Before claiming enforcement, exercise
the applicable release/recovery behavior and state its observed limits. Reuse
passing evidence only where its basis and conditions support the actual claim;
no fresh exercise is required for every custody use. A procedural walkthrough
cannot establish a host-enforced guarantee. Label simulated cases and distinguish
same-holder resumption from transfer, live interruption or timeout behavior.
