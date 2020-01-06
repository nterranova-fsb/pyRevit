# pylint: skip-file
import hooks_logger as hl
hl.log_hook(__file__,
    {
        "cancellable?": str(__eventargs__.Cancellable),
        "focus_gained": str(__eventargs__.FocusGained),
        "pane_id": str(__eventargs__.PaneId),
    },
    log_doc_access=True
)