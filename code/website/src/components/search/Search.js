import React, { Component } from 'react';
import { Input } from 'antd';
import './Search.css';
import i18n from '../../i18next';

class Search extends Component {

    constructor(props) {
        super(props);
        this.state = {
            term: '',
            language: this.props.language
        }
    }
    componentWillUpdate(nextprops) {
        if(nextprops.language !== this.props.language){
            this.setState({
                language: nextprops.language
            })
        }
    }



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
        let lng = this.state.language
        return (
            <div className="Search">
            <Input.Search style={{ width: '50%' }} placeholder={ i18n.t('searchbar.placeholder', { lng }) } size="large" onChange={this.handleChange} onSearch={this.handleSubmit} enterButton/>
            </div>
        )
    }
}

export default Search;
