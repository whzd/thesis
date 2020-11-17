import React, { Component } from 'react';
import { Collapse,  Alert } from 'antd';
import './Display.css';
import Board from '../board/Board.js';
import i18n from '../../i18next';

const { Panel } = Collapse;


class Display extends Component {

    constructor(props){
        super(props)
        this.state = {
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

    render() {

        let lng = this.state.language

        let displayContent
        let moreInfo
        let definition
        if(this.props.content != null) {

            console.log(this.props.content)
            if (this.props.content === "Não foram encontrados resultados."){
                displayContent = <div><Alert
                message={ i18n.t('display.notFound.title', { lng }) }
                description={ i18n.t('display.notFound.msg', { lng }) }
                type="error"
                showIcon
            /></div>
            }else if(this.props.content === "Funcionalidade ainda não implementada."){
                displayContent = <div>
                    <Alert message={ i18n.t('display.notSupported.title', { lng }) }
                    description={ i18n.t('display.notSupported.msg', { lng }) }
                    type="warning"
                    showIcon/>
                    </div>
            }else{


                moreInfo = this.props.content.additionalInfo.map((item, index) => (
                    <p><a href={item} key={index}>{item}</a></p>
                ));


                definition = this.props.content.definition.map((item, index) => (
                    <Board index={index} item={item} expression={this.props.content.expression} handleAvatar={this.props.handleAvatar} handleLanguageChange={this.props.handleLanguageChange} language={this.props.language}/>
                ));


                displayContent =
                    <div>
                        {definition}
                        <Collapse defaultActiveKey={['1','2']} style={{ width: '90%' }}>
                            <Panel header={ i18n.t('display.source', { lng }) } key="1">
                                <p><a href={this.props.content.source}>{this.props.content.source}</a></p>
                            </Panel>
                            <Panel header={ i18n.t('display.additionalInfo', { lng }) } key="2">
                                {moreInfo}
                            </Panel>
                        </Collapse>
                    </div>
            }
        }else{
            displayContent = ""
        }

        return (
            <div className="Display">
                { displayContent }
            </div>
        )
    }
}

export default Display;
