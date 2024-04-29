
import ctranslate2
import sentencepiece as spm

def translate_to_arabic(summary):
    ct_model_path = "Models/ct2_model"
    sp_model_path = "Models/flores200_sacrebleu_tokenizer_spm.model"
    device = "cuda" 
    sp = spm.SentencePieceProcessor()
    
    sp.load(sp_model_path)

    translator = ctranslate2.Translator(ct_model_path, device)
    src_lang = "</s> eng_Latn"
    tgt_lang = "arb_Arab"

    beam_size = 4

    for i in range(len(summary)):
        summary1 = summary[i].split(".")

        summary1 = [sent.strip() for sent in summary1]
        target_prefix = [[tgt_lang]] * len(summary1)

        summary_subworded = sp.encode_as_pieces(summary1)
        summary_subworded = [[src_lang] + sent + ["</s>"] for sent in summary_subworded]

        translator = ctranslate2.Translator(ct_model_path, device=device)
        translations = translator.translate_batch(summary_subworded, batch_type="tokens", max_batch_size=2024, beam_size=beam_size, target_prefix=target_prefix)
        translations = [translation.hypotheses[0] for translation in translations]

        translated_summary = sp.decode(translations)
        translated_summary = [sent[len(tgt_lang):].strip() for sent in translated_summary]

        return translated_summary