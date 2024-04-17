def mcc(tp, fp, tn, fn: int) -> float:
    """
    Calculates the Matthews correlation coefficient, or MCC, to measure performance of machine learning algorithms.
    
    Args:
        tp: True Positive, integer
        fp: False Positive, integer
        fn: False Negative, integer
        tn: True Negative, integer
    
    Returns:
        MCC value, a float between -1 and +1, where +1 is a perfectly correlated prediction and -1 is anti-correlated. A score of 0 indicates random prediction.
    """
    import math
    MCC = ((tp * tn) - (fp * fn)) / math.sqrt( (tp + fp)*(tp + fn)*(tn + fp)*(tn + fn) )
    return MCC
    
def f_measure(tp, fp, fn: int) -> float:
    """
    Calculates the F-measure, or F1 Score - a weighted measure of accuracy and precision. 
    
    Args:
        tp: True Positive, integer
        fp: False Positive, integer
        fn: False Negative, integer
        
    Returns:
        The F1 binary classification between 0 and 1, where 1 is the most accurate/precise score.
    """
    
    F1 = (2 * tp) / ((2 * tp) + fp + fn)
    return F1