import i18next from 'i18next';

i18next
    .init({
        interpolation: {
            // React already does escaping
            escapeValue: false,
        },
        lng: 'pt', // 'en' | 'es'
        // Using simple hardcoded resources for simple example
        resources: {
            pt: {
                translation: {
                    navbar: {
                        language: 'Idioma',
                    },
                    searchbar: {
                        placeholder: 'Pesquisa',
                    },
                    display: {
                        board: {
                            button: {
                                display: 'Visualizar',
                            },
                            feedback: {
                                tooltip: {
                                    text: 'Deseja uma nova explicação?',
                                    negativeBtn: 'Não',
                                    positiveBtn: 'Sim',
                                },
                            },
                        },
                        source: 'Fonte',
                        additionalInfo: 'Informação Adicional',
                        notFound: {
                            title: 'Erro!',
                            msg: 'Não foram encontrados resultados.',
                        },
                        notSupported: {
                            title: 'Aviso!',
                            msg: 'Pesquisa por mais do que uma palavra ainda não suportada.',
                        },
                    },
                },
            },
            en: {
                translation: {
                    navbar: {
                        language: 'Language',
                    },
                    searchbar: {
                        placeholder: 'Search',
                    },
                    display: {
                        board: {
                            button: {
                                display: 'Display',
                            },
                            feedback: {
                                tooltip: {
                                    text: 'Generate a new explanation?',
                                    negativeBtn: 'No',
                                    positiveBtn: 'Yes',
                                },
                            },
                        },
                        source: 'Source',
                        additionalInfo: "Additional Information",
                        notFound: {
                            title: 'Error!',
                            msg: 'None explanations found.',
                        },
                        notSupported: {
                            title: 'Warning!',
                            msg: 'Multi-word search not supported.',
                        },
                    },
                },
            }
        },
    })

export default i18next
