package aip

import "time"

// Capability describes a capability that an agent can advertise.
type Capability struct {
	ID          string   `json:"id"`
	Name        string   `json:"name"`
	Version     string   `json:"version"`
	Description string   `json:"description,omitempty"`
	Actions     []string `json:"actions,omitempty"`
}

// ActionRequest represents a request for an agent to perform an action.
type ActionRequest struct {
	ID        string                 `json:"id"`
	Type      string                 `json:"type"`
	Payload   map[string]interface{} `json:"payload,omitempty"`
	Timestamp time.Time              `json:"timestamp"`
}

// ActionResponse represents the result of an action execution.
type ActionResponse struct {
	ID        string                 `json:"id"`
	RequestID string                 `json:"request_id"`
	Status    string                 `json:"status"` // "success", "error", "pending"
	Result    map[string]interface{} `json:"result,omitempty"`
	Error     string                 `json:"error,omitempty"`
}

// Receipt is the top-level envelope for an agent interaction protocol message.
type Receipt struct {
	ID           string          `json:"id"`
	Protocol     string          `json:"protocol"`
	Version      string          `json:"version"`
	Timestamp    time.Time       `json:"timestamp"`
	Capabilities []Capability    `json:"capabilities,omitempty"`
	Actions      []ActionRequest `json:"actions,omitempty"`
	Responses    []ActionResponse `json:"responses,omitempty"`
	Metadata     map[string]interface{} `json:"metadata,omitempty"`
}
