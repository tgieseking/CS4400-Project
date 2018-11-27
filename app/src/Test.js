import React, { Component } from "react";
import SimpleTable from "./SimpleTable";

class Test extends Component {
    constructor(props) {
        super(props);
        this.state = {value:0}
    }

  render() {
    return (
      <div>
        <h2>Test</h2>

        <button onClick={() => this.increment()}>Increment</button>

        <p>{this.state.value}</p>
        <SimpleTable header={["Column 1", "Column 2"]} rows={[["Cell 1", "Cell 2"], ["Cell 7", "Cell 10"]]}></SimpleTable>

      </div>
    );
  }

  increment() {
      this.setState({value: this.state.value + 1})
  }
}

export default Test;
