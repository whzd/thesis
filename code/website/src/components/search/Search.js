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
    }

    render() {
        return (
            <div className="Search">
                <form onSubmit={this.handleSubmit} className='ui form'>
                    <Input.Search style={{ width: '40%' }} placeholder="Pesquisa" size="large" onChange={this.handleChange} onSearch={this.handleSubmit} enterButton/>
                </form>
            </div>
        )
    }
}

export default Search;
