import React, { Component } from 'react';
import { Input } from 'antd';
import './Search.css';

class Search extends Component {

    state = {
        term: ''
    };

    handleChange = (event) => {
        this.setState({
            term: event.target.value
        });
    };

    handleSubmit = event => {
        this.props.handleFormSubmit(this.state.term);
        return false;
    }

    render() {
        return (
            <div className="Search">
            <Input.Search style={{ width: '50%' }} placeholder='Pesquisa' size="large" onChange={this.handleChange} onSearch={this.handleSubmit} enterButton/>
            </div>
        )
    }
}

export default Search;
