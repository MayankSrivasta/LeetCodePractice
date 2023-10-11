package graphs;

public class Employee {

	String name;
	String employeeId;
	String status;

	public Employee(String name, String employeeId, String status) {
		super();
		this.name = name;
		this.employeeId = employeeId;
		this.status = status;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getEmployeeId() {
		return employeeId;
	}

	public void setEmployeeId(String employeeId) {
		this.employeeId = employeeId;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	@Override
	public String toString() {
		return "Employee [name=" + name + ", employeeId=" + employeeId + ", status=" + status + "]";
	}

}
