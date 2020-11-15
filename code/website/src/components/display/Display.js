import React, { Component } from 'react';
import { Collapse,  Alert } from 'antd';
import './Display.css';
import Board from '../board/Board.js';

const { Panel } = Collapse;


class Display extends Component {

    render() {

        let displayContent
        let moreInfo
        let definition
        if(this.props.content != null) {

            console.log(this.props.content)
            if (this.props.content === "Não foram encontrados resultados."){
                displayContent = <div><Alert
                message="Erro!"
                description="Não foram encontrados resultados."
                type="error"
                showIcon
            /></div>
            }else{


                moreInfo = this.props.content.additionalInfo.map((item, index) => (
                    <p><a href={item} key={index}>{item}</a></p>
                ));


                definition = this.props.content.definition.map((item, index) => (
                    <Board index={index} item={item} expression={this.props.content.expression} handleAvatar={this.props.handleAvatar}/>
                ));


                displayContent =
                    <div>
                        {definition}
                        <Collapse defaultActiveKey={['1','2']} style={{ width: '90%' }}>
                            <Panel header="Fontes" key="1">
                                <p><a href={this.props.content.source}>{this.props.content.source}</a></p>
                            </Panel>
                            <Panel header="Informação Adicional" key="2">
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
