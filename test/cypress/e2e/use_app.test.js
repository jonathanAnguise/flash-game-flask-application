function checkWordsAreDifferents(){
        cy.get('.card_front > .card-text > p').then( firstWord => {
            const firstWordText = firstWord.text()
	    cy.get('.card_back > .card-text > p').then( secondWord => {
                const secondWordText = secondWord.text()
	        expect(firstWordText).to.not.equal(secondWordText)
            })
        })
}

describe('testing the flash card game', () => {
  beforeEach(() => {
    cy.visit('/')
  })


    it('test button "New Word!" is reloading the page', () => {
        checkWordsAreDifferents()

    })

    it('test word is different from the answer word', () => {
        
        cy.get('.card_front > .card-text > p').then( firstWord => {
            const firstWordBeforeClicking = firstWord.text()
	    cy.get('.card_back > .card-text > p').then( secondWord => {
                const secondWordBeforeClicking = secondWord.text()
		cy.get('.custom-btn').click()
                    cy.get('.card_front > .card-text > p').then( firstWord => {
                    const firstWordAfterClicking = firstWord.text()
	                cy.get('.card_back > .card-text > p').then( secondWord => {
                        const secondWordAfterClicking = secondWord.text()
	                expect(firstWordBeforeClicking).to.not.equal(firstWordAfterClicking)
	                expect(secondWordBeforeClicking).to.not.equal(secondWordAfterClicking)
                        })
                    })
            })
        })
            checkWordsAreDifferents()

    })
})

