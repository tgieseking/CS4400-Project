import React, { Component } from "react";
import {
  Redirect
} from "react-router-dom";
import TextField from '@material-ui/core/TextField';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import InputLabel from '@material-ui/core/InputLabel';
import Button from '@material-ui/core/Button';

import SimpleTable from "./SimpleTable";


class SearchExhibits extends Component {
    constructor(props) {
        super(props);
        this.state = {name: "", min_size: "", max_size: "", min_animals: "", max_animals: "", water_feature: "", errorMessage: "", result_table: null};
    }

    render() {
        return (
        <div
            style={{display: "flex", flexDirection: "column", alignItems: "start"}}
        >
            <h1>Search Exhibits</h1>
            <TextField
                label = "Name"
                value = {this.state.name}
                onChange = {e => this.setState({name: e.target.value})}
            />
            <TextField
                label = "Minimum size"
                type = "number"
                value = {this.state.min_size}
                onChange = {e => this.setState({min_size: e.target.value})}
            />
            <TextField
                label = "Maximum size"
                type = "number"
                value = {this.state.max_size}
                onChange = {e => this.setState({max_size: e.target.value})}
            />
            <TextField
                label = "Minimum animals"
                type = "number"
                value = {this.state.min_animals}
                onChange = {e => this.setState({min_animals: e.target.value})}
            />
            <TextField
                label = "Maximum animals"
                type = "number"
                value = {this.state.max_animals}
                onChange = {e => this.setState({max_animals: e.target.value})}
            />
            <InputLabel>Water feature</InputLabel>
            <Select
                label = "Water feature"
                value = {this.state.water_feature}
                onChange = {e => this.setState({water_feature: e.target.value})}
            >
                <MenuItem value={null} />
                <MenuItem value={true}>Yes</MenuItem>
                <MenuItem value={false}>No</MenuItem>
            </Select>
            <Button variant = "contained"
                onClick = {this.submit.bind(this)}
            >Search</Button>
            <p>{this.state.errorMessage}</p>
            {
                this.state.result_table != null ?
                <SimpleTable
                    header = {this.state.result_table.header}
                    rows = {this.state.result_table.rows}
                />
                : null
            }
        </div>
        );
    }

    submit() {
        this.setState({result_table:
            {header: ["Column 1", "Column 2"],
            rows: [["Cell 1", "Cell 2"], ["Cell 3", "Cell 4"]]}
        });
    }
    //
    // login(username, password) {
    //     if(username == password) {
    //         return Promise.resolve({
    //             loginSuceeded: true,
    //             authToken: "auth",
    //             username: "user",
    //             userType: "Visitor"
    //         });
    //     } else {
    //         return Promise.resolve({
    //             loginSuceeded: false,
    //             errorMessage: "Error"
    //         });
    //     }
    // }
}

export default SearchExhibits;
