Sessions
- session_id




sessions_tasks
- session_task_id
- sessions_id
- tasks_output_id

sessions_contexts
- session_context_id
- sessions_id
- context_output_id


Tasks_contexts
- tasks_context_id
- tasks_output_id
- context_output_id


---

tasks_input ## secondary interactive core
- task_id
- is_reconsume (?)

tasks_breakdown
- task_breakdown_id
- task_input_id
- breakdown_logic_id

tasks_compose
- tasks_compose_id
- task_breakdown_id
- compose_logic_id


tasks_output  ## main interactive core
- tasks_output_id
- task_compose_id

---

compose_logic ## logic store to get get reasoning and traceback
- compose_logic_id

breakdown_logic ## logic store to get get reasoning and traceback
- breakdown_logic_id

---

context_input (?) ## still thinking on whether we really should have this or not
- context_input_id


context_breakdown
- context_decompose_id
- context_input_id

context_compose
- context_compose_id
- compose_logic_id

context_output
- context_output_id
- context_compose_id
- compose_logic_id

---


## algo

There are some notions that we could you jump point search to search to constructs
the search for the /perspectives.
